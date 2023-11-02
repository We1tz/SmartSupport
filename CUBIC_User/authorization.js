function submitForm() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    window.api.send('login', { username, password });
}

window.api.receive('login-response', (data) => {
    if (data.success) {
        console.log(data.message);
    } else {
        console.error(data.message);
    }
});