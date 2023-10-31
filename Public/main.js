const { app, BrowserWindow } = require('electron');
const path = require('path');
const url = require('url');

let win;

function createWindow() {
  win = new BrowserWindow({
    height: 1080,
    useContentSize: true,
    width: 1920,
    autoHideMenuBar: true,
    frame: false,
    webPreferences: {
      nodeIntegration: true,
      allowRunningInsecureContent: true,
    },
  });

  win.loadURL(
    url.format({
      pathname: path.join(__dirname, 'index.html'),
      protocol: 'file:',
      slashes: true
    })
  );

  win.maximize();

  win.webContents.on('before-input-event', (event, input) => {
    if (input.control && input.key.toLowerCase() === 'q') {
      event.preventDefault();
    }
  });

  win.on('close', (event) => {
    event.preventDefault();
  });

  win.on('minimize', (event) => {
    event.preventDefault();
  });

  win.on('maximize', () => {
    win.webContents.on('before-input-event', (event, input) => {
      if (input.key.toLowerCase() === 'f11') {
        win.setFullScreen(false);
      }
    });
  });

  win.on('resize', () => {
    if (win.isFullScreen()) {
      win.setFullScreen(false);
    }
  });

  function checkFocus() {
    win.setAlwaysOnTop(true);
    setTimeout(() => {
      win.setAlwaysOnTop(false);
    }, 100);
  }

  setInterval(checkFocus, 50);
}

app.whenReady().then(createWindow);

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow();
  }
});
