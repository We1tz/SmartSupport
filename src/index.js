import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import './styles/common.css';

//const electron = window.require('electron');
//const ipcRenderer  = electron.ipcRenderer;

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);