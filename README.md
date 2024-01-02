# SmartSupport

## Установка
1. Установка Node.js - https://nodejs.org/en  
2. Установка зависимостей в командную строку в раздел с проектом:  
  - npm install electron --save-dev  
  - npm install path  
  - npm install url  
  - npm install sqlite3  
  - npm install node-telegram-bot-api   
3. Установка библиотеки react js  
  - Запускаем create-react-app  
    npx create-react-app project_name  
  - Входим в папку  
    cd project_name  
  - В корень добавляем папку electron в нем файл main.js, типовой для electron  
  - Изменяем в нем открытие файла на открытие localhost:3000  
    mainWindow.loadURL('http://localhost:3000');  
  - В файл package.json добавляем: в scripts:  
    "electron": "electron ."  
  - И добавляем строчку: «main»:  
    "main": "electron/main.js"  
  - а также productNam:  
    "productName": "КУБИК"  
  - Нам нужно чтобы, при разработке использовался localhost:3000, а в продакшн ссылался на собранный файл html  
    Соответственно меняем файл main.js, добавляя строку:  

      const startUrl = process.env.ELECTRON_START_URL || url.format({  
        pathname: path.join(__dirname, '../index.html'),  
        protocol: 'file:',  
        slashes: true  
      });  
      mainWindow.loadURL(startUrl);
  - В файле package.json в scripts изменяем строку start — для того чтобы не запускался в браузере  
    "start": "export BROWSER=none && react-scripts start"  
    Для винды она будет выглядеть так:  
    "start": "set BROWSER=none && react-scripts start"  
  - В файл package.json добавляем строку в scripts  
    "electron-dev": "ELECTRON_START_URL=http://localhost:3000 electron ."  
    Для винды это так:  
    ”electron-dev”: "set ELECTRON_START_URL=http://localhost:3000 && electron .”  
  - Также в package.json, добавляем строку:  
    "homepage": "./",  
  - Теперь запуск проекта для разработки будет такими двумя командами:  
    npm start  
    npm run electron-dev  
  - Доступ к Electron из приложения в React  
    Добавляем такой код в приложение React:  

    const electron = window.require('electron');  
    const ipcRenderer  = electron.ipcRenderer;  
    После этого можно пользоваться ipcRender.  

    Соответственно после этого в браузере перестает работать, а работает только через Electron.  
  - Билдим все в продакшн  
    Для начала запускаем build react  
    npm run build  
  - Добавляем в package.json в scripts:  
    "build-electron": "mkdir build/electron && cp -r electron/. build/electron",  
    Для винды это будет так:  
    "build-electron": "mkdir build/electron && robocopy electron build/electron /S"  
  - Запускаем этот скрипт:  
    npm run build-electron  
  - Устанавливаем electron-builder  
    npm install --save-dev electron-builder  
    Добавляем еще строку в package.json в scripts  
    "package": "electron-builder build --mac --win -c.extraMetadata.main=build/electron/main.js --publish never"  
  - Также добавляем в package.json  
      "build": {  
        "files": [  
          "build/**/*",  
          "node_modules/**/*"  
        ],  
        "publish": {  
          "provider": "github",  
          "repo": "electron-cra-example",  
          "owner": "johndyer24"  
        }  
      }  
  - Добавляем иконку приложения  
    Для добавления иконки приложения, копируем файл icon.png в папку build размером 512 на 512 пикселей.  
    Подробнее можно почитать здесь https://www.electron.build/icons  
    В файл package.json добавляем строку icon в build  
    "icon": "build/icon.png"  
  - Итого файл package.json получается примерно такой:  

    {  
      "name": "КУБИК",  
      "version": "0.1.0",  
      "private": true,  
      "homepage": "./",  
      "dependencies": {  
        "@testing-library/jest-dom": "^4.2.4",  
        "@testing-library/react": "^9.5.0",  
        "@testing-library/user-event": "^7.2.1",  
        "pg": "^8.3.0",  
        "react": "^16.13.1",  
        "react-dom": "^16.13.1",  
        "react-redux": "^7.2.0",  
        "react-scripts": "3.4.1",  
        "redux": "^4.0.5",  
        "redux-thunk": "^2.3.0"  
      },  
      "author": {  
        "name" : "Лалаян Рафик",  
        "email": "rafl9@mail.ru",  
        "url": "https://rafl.ru"  
      },  
      "main": "electron/main.js",  
      "productName": "ДП - Управление базами PostgreSql",  
      "scripts": {  
        "start": "export BROWSER=none && react-scripts start",  
        "build": "react-scripts build",  
        "test": "react-scripts test",  
        "eject": "react-scripts eject",  
        "electron": "electron .",  
        "electron-dev": "ELECTRON_START_URL=http://localhost:3000 electron .",  
        "build-electron": "mkdir build/electron && cp -r electron/. build/electron",  
        "package": "electron-builder build --mac --win -c.extraMetadata.main=build/electron/main.js --publish never"  
      },  
      "eslintConfig": {  
        "extends": "react-app"  
      },  
      "browserslist": {  
        "production": [  
          ">0.2%",  
          "not dead",   
          "not op_mini all"  
        ],  
        "development": [  
          "last 1 chrome version",  
          "last 1 firefox version",  
          "last 1 safari version"  
        ]  
      },  
      "devDependencies": {  
        "electron": "^9.1.1",  
        "electron-builder": "^22.7.0",  
        "redux-logger": "^3.0.6"  
      },  
      "build": {  
        "win" : {  
          "icon" : "build/icon.ico"  
        },  
        "mac" : {  
          "icon" : "build/icon.png"  
        },  
        "files": [  
          "build/**/*",  
          "node_modules/**/*"  
        ],  
        "publish": {  
          "provider": "github",  
          "repo": "SmartSupport",  
          "owner": "Weitz"  
        }  
      }  
    }  
    Запускаем:  

    npm run package  
    Проект создастся в папке dist. 
