using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Выберите режим:\n1. Запустить клиент\n2. Запустить сервер");
        string choice = Console.ReadLine();

        switch (choice)
        {
            case "1":
                Client client = new Client();
                client.Start();
                break;
            case "2":
                Server server = new Server();
                server.Start();
                break;
            default:
                Console.WriteLine("Неправильный выбор.");
                break;
        }
    }
}
