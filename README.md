# SmartSupport

## Установка
1. Установка Node.js - https://nodejs.org/en
2. Установка зависимостей в командную строку в раздел с проектом:
  npm install electron --save-dev
  npm install path
  npm install url
  npm install sqlite3
  npm install node-telegram-bot-api
3. Установка библиотеки react js
  - Запускаем create-react-app
      npx create-react-app nazvanie_projecta
  - Входим в папку
      cd nazvanie_projecta
  - В корень добавляем папку electron в нем файл main.js, типовой для electron
  - Изменяем в нем открытие файла на открытие localhost:3000
      mainWindow.loadURL('http://localhost:3000');
  - В файл package.json добавляем: в scripts:
      "electron": "electron ."
  -
4. Запуск через npm run electron