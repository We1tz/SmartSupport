using System;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading;

class Server
{
    public void Start()
    {
        try
        {
            // Устанавливаем сервер и начинаем прослушивать входящие соединения
            IPAddress ipAddress = IPAddress.Parse("127.0.0.1"); // IP 
            int port = 8888; 
            TcpListener listener = new TcpListener(ipAddress, port);
            listener.Start();
            Console.WriteLine("Сервер запущен. Ожидание подключения клиента...");

            TcpClient client = listener.AcceptTcpClient();
            Console.WriteLine("Клиент подключен.");

            NetworkStream stream = client.GetStream();

            while (true)
            {
                // Получаем сообщение от клиента
                string clientMessage = ReadMessage(stream);

                if (clientMessage.ToLower() == "выход")
                {
                    break;
                }

                Console.WriteLine("Клиент: " + clientMessage);

                // Отправляем ответ клиенту
                Console.Write("Сервер: ");
                string serverMessage = Console.ReadLine();
                SendMessage(stream, serverMessage);
            }

            // Закрываем соединение с клиентом
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
}
