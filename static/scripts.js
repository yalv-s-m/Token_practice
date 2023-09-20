async function sendPayload() {
    const us_login = document.getElementById('input_login').value;
    const us_password = document.getElementById('input_password').value;
    const url = '/handle_post';

    const payload = {
        login: us_login,
        password: us_password
    };

    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
    })

    response_data = await response.json();
    final_token = response_data.final_token;
    document.getElementById('output_token').value = "";
    document.getElementById('output_token').value = final_token;
}


async function sendToken() {
    const us_token = document.getElementById('input_token').value;
    const url = '/authenticate';

    const data = {
        token: us_token
    }

    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })

    response_data = await response.json();
    decrypted = response_data.decrypted;
    is_successful = response_data.is_successful;
    document.getElementById('output_result').value = "";

    var outputResultTextarea = document.getElementById('output_result');
    outputResultTextarea.value = decrypted;
    
    if (is_successful) {
        outputResultTextarea.style.borderColor = 'green';
    } else {
        outputResultTextarea.style.borderColor = 'red';
    }
}