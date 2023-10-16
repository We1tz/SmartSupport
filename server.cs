using System;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Drawing;
using System.Drawing.Imaging;
using System.IO;
using System.Diagnostics;

class ServerR
{
    private string screenshotsPath = "C:\\Users\\105(2)\\source\\repos\\SmartVoiceAdm\\SmartVoiceAdm"; 

    public Server()
    {
        if (!Directory.Exists(screenshotsPath))
        {
            Directory.CreateDirectory(screenshotsPath);
        }
    }

    public void Start()
    {
        try
        {
            IPAddress ipAddress = IPAddress.Parse("127.0.0.1");
            int port = 8888;
            TcpListener listener = new TcpListener(ipAddress, port);
            listener.Start();
            Console.WriteLine("Сервер запущен. Ожидание подключения клиента...");

            TcpClient client = listener.AcceptTcpClient();
            Console.WriteLine("Клиент подключен.");

            NetworkStream stream = client.GetStream();

            while (true)
            {
                string clientMessage = ReadMessage(stream);

                if (clientMessage.ToLower() == "выход")
                {
                    break;
                }
                else if (clientMessage.ToLower() == "screen")
                {
                    byte[] screenshotBytes = ReceiveScreenshot(stream, ReadInt32(stream)); // Чтение длины массива
                    ShowScreenshot(screenshotBytes);
                    continue;
                }

                Console.WriteLine("Клиент: " + clientMessage);

                Console.Write("Сервер: ");
                string serverMessage = Console.ReadLine();
                SendMessage(stream, serverMessage);
            }

            client.Close();
            Console.WriteLine("Клиент отключен.");
        }
        catch (Exception ex)
        {
            Console.WriteLine("Ошибка: " + ex.Message);
        }
    }

    private string ReadMessage(NetworkStream stream)
    {
        byte[] buffer = new byte[1024];
        int bytesRead = stream.Read(buffer, 0, buffer.Length);
        return Encoding.UTF8.GetString(buffer, 0, bytesRead);
    }

    private void SendMessage(NetworkStream stream, string message)
    {
        byte[] buffer = Encoding.UTF8.GetBytes(message);
        stream.Write(buffer, 0, buffer.Length);
    }

    private int ReadInt32(NetworkStream stream)
    {
        byte[] intBytes = new byte[4];
        stream.Read(intBytes, 0, 4);
        return BitConverter.ToInt32(intBytes, 0);
    }

    private byte[] ReceiveScreenshot(NetworkStream stream, int length)
    {
        byte[] buffer = new byte[length];
        int bytesRead = stream.Read(buffer, 0, buffer.Length);
        return buffer;
    }

    private void ShowScreenshot(byte[] screenshotBytes)
    {
        try
        {
            string timestamp = DateTime.Now.ToString("yyyyMMddHHmmssfff");
            string screenshotPath = Path.Combine(screenshotsPath, $"Screenshot_{timestamp}.png");

            using (MemoryStream memoryStream = new MemoryStream(screenshotBytes))
            {
                Image screenshot = Image.FromStream(memoryStream);
                screenshot.Save(screenshotPath);
                Console.WriteLine($"Скриншот сохранен: {screenshotPath}");
                Process.Start(screenshotPath); 
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine("Ошибка при сохранении скриншота: " + ex.Message);
        }
    }
}
