const electron = require('electron');
const path = require('path');
const url = require('url');
const sqlite3 = require('sqlite3').verbose();
const { app, BrowserWindow, ipcMain } = electron;
const TelegramBot = require('node-telegram-bot-api');

const TELEGRAM_BOT_TOKEN = '5167808596:AAEpeOhuLDrZdhbJ13BsOCXOhOG8GkvoU_A';
const TELEGRAM_CHAT_ID = '1922232899';
const PC = '№1';
const bot = new TelegramBot(TELEGRAM_BOT_TOKEN, { polling: false });

bot.sendMessage(TELEGRAM_CHAT_ID, `Компьютер ${PC} активирован! \n`);

let win;

function createWindow() {
    win = new BrowserWindow({
        width: 800,
        height: 600,
        frame: false,
        webPreferences: {
            nodeIntegration: false,
            contextIsolation: true,
            preload: path.join(__dirname, 'preload.js'),
        },
        closable: false,
        minimizable: false,
        maximizable: false,
        resizable: false,
        skipTaskbar: true,
        alwaysOnTop: true,
        fullscreen: true,
    });

    win.setMenu(null);
    win.setVisibleOnAllWorkspaces(true);
    win.setAlwaysOnTop(true, "screen-saver");

    const startUrl = process.env.ELECTRON_START_URL || url.format({
        pathname: path.join(__dirname, '/index.html'),
        protocol: 'file:',
        slashes: true,
    });

    win.loadURL(startUrl);

    win.on('closed', function () {
        win = null;
    });

    win.on('focus', () => {
    });

    win.on('blur', () => {
    });

    win.on('minimize', (event) => {
        event.preventDefault();
    });

    ipcMain.on('login', (event, data) => {
        const dbPath = path.join(__dirname, 'main.db');
        const db = new sqlite3.Database(dbPath);
        const { username, password } = data;
        db.get(
            'SELECT * FROM users WHERE login = ? AND password = ?',
            [username, password],
            (err, row) => {
                if (err) {
                    win.webContents.send('login-response', { success: false, message: 'Error occurred while accessing the database' });
                } else if (row) {
                    const now = new Date().toISOString().replace(/T/, ' ').replace(/\..+/, '');
                    const { id, first_name, last_name, login, password, user_group, registration_date, last_login_date } = row;
                    const message_to_send = `Пользователь ${login}, (${first_name} ${last_name}) авторизовался.\n\nДата входа: ${now}\n\nНаправление - ${user_group}.`;
                    bot.sendMessage(TELEGRAM_CHAT_ID, message_to_send, { parse_mode: "HTML",  "Content-Type": "application/json; charset=utf-8" });

                    win.webContents.send('login-response', { success: true, message: 'Login successful' });
                    win.close();
                    win.destroy();
                } else {
                    win.webContents.send('login-response', { success: false, message: 'Invalid credentials' });
                }
            }
        );
        db.close();
    });
}

app.on('ready', createWindow);

app.on('window-all-closed', function () {
    if (process.platform !== 'darwin') app.quit();
});

app.on('activate', function () {
    if (win === null) createWindow();
});
