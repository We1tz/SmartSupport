function submitForm() {
    const first_name = document.getElementById('first_name').value;
    const second_name = document.getElementById('second_name').value;
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const group = document.getElementById('group').value;
    window.api.send('login', { first_name, second_name, username, password, group });
}

window.api.receive('registration-response', (data) => {
    if (data.success) {
        console.log(data.message);
    } else {
        console.error(data.message);
    }
});