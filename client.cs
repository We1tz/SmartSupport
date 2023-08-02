using System;
using System.Net.Sockets;
using System.Text;

class Client
{
    public void Start()
    {
        try
        {
            // Подключение к серверу
            string serverIP = "127.0.0.1"; // Используйте IP-адрес сервера
            int port = 8888; // Используйте номер порта, указанный на сервере
            TcpClient client = new TcpClient(serverIP, port);
            Console.WriteLine("Подключение к серверу выполнено.");

            NetworkStream stream = client.GetStream();

            while (true)
            {
                // Отправляем сообщение серверу
                Console.Write("Клиент: ");
                string clientMessage = Console.ReadLine();
                SendMessage(stream, clientMessage);

                if (clientMessage.ToLower() == "выход")
                {
                    break;
                }

                // Получаем ответ от сервера
                string serverMessage = ReadMessage(stream);
                Console.WriteLine("Сервер: " + serverMessage);
            }

            // Закрываем соединение с сервером
            client.Close();
            Console.WriteLine("Отключение от сервера.");
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
}
