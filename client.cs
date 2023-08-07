using System;
using System.Net.Sockets;
using System.Text;
using System.Drawing;
using System.Drawing.Imaging;
using System.IO;
using System.Windows.Forms;

class Client
{
    public void Start()
    {
        try
        {
            TcpClient client = new TcpClient("127.0.0.1", 8888);
            NetworkStream stream = client.GetStream();

            while (true)
            {
                Console.Write("Клиент: ");
                string clientMessage = Console.ReadLine();
                SendMessage(stream, clientMessage);

                if (clientMessage.ToLower() == "выход")
                {
                    break;
                }
                else if (clientMessage.ToLower() == "screen")
                {
                    SendScreenshot(stream);
                    continue;
                }

                string serverMessage = ReadMessage(stream);
                Console.WriteLine("Сервер: " + serverMessage);
            }

            client.Close();
        }
        catch (Exception ex)
        {
            Console.WriteLine("Ошибка: " + ex.Message);
        }
    }

    private void SendMessage(NetworkStream stream, string message)
    {
        byte[] buffer = Encoding.UTF8.GetBytes(message);
        stream.Write(buffer, 0, buffer.Length);
    }

    private string ReadMessage(NetworkStream stream)
    {
        byte[] buffer = new byte[1024];
        int bytesRead = stream.Read(buffer, 0, buffer.Length);
        return Encoding.UTF8.GetString(buffer, 0, bytesRead);
    }

    private void SendScreenshot(NetworkStream stream)
    {
        try
        {
            using (Bitmap screenshot = new Bitmap(Screen.PrimaryScreen.Bounds.Width, Screen.PrimaryScreen.Bounds.Height))
            using (Graphics graphics = Graphics.FromImage(screenshot))
            {
                graphics.CopyFromScreen(0, 0, 0, 0, screenshot.Size);

                using (MemoryStream memoryStream = new MemoryStream())
                {
                    screenshot.Save(memoryStream, ImageFormat.Png);
                    byte[] imageBytes = memoryStream.ToArray();
                    byte[] lengthBytes = BitConverter.GetBytes(imageBytes.Length);
                    stream.Write(lengthBytes, 0, lengthBytes.Length);
                    stream.Write(imageBytes, 0, imageBytes.Length);
                }
            }
            Console.WriteLine("Скриншот отправлен на сервер.");
        }
        catch (Exception ex)
        {
            Console.WriteLine("Ошибка при отправке скриншота: " + ex.Message);
        }
    }
}
