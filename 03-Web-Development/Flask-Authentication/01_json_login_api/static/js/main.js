const loginForm = document.querySelector('.lForm')
const usernameInput = document.querySelector('#username')
const passwordInput = document.querySelector('#password')
const inputBtn = document.querySelector('.input-btn')

const errMsg = document.querySelector('.errMsg')
const errMsgPass = document.querySelector('.errMsgPass')

const togglePasswordButton = document.querySelector('#togglePassword')



loginForm.addEventListener('submit', (e) => {
    e.preventDefault()

    const data = {
        userName: usernameInput.value.trim(),
        password: passwordInput.value.trim()
    };

    login(data)
})


async function login(data) {
    try {



        const response = await fetch('/submit', {
            method: 'POST',
            headers: {

                'Content-Type': 'application/json'
            },

            body: JSON.stringify(data)


        });



        const resData = await response.json();

        if (resData.status === 'success') {
         
            window.location.href = resData.redirect_url;
        } else {
        
            errMsg.textContent = resData.message;
        }
    } catch (error) {
        console.error('Login Error:', error);
    }
}



usernameInput.addEventListener('blur', (e) => {
    if (e.target.value == '') {
        errMsg.textContent = 'This field is required '
    } else {
        errMsg.textContent = ''
    }

});

passwordInput.addEventListener('blur', (e) => {
    if (e.target.value == '') {
        errMsgPass.textContent = 'This field is required '
    } else {
        errMsgPass.textContent = ''

    }
});

passwordInput.addEventListener('input', () => {
    if (passwordInput.value.length > 10) {

        passwordInput.value = passwordInput.value.slice(0, 10);
    }


})


togglePasswordButton.addEventListener('click', (e) => {

    if (togglePasswordButton.textContent == 'Show') {
        togglePasswordButton.textContent = 'Hide'
        passwordInput.type = 'text'
    }
    else {
        togglePasswordButton.textContent = 'Show'
        passwordInput.type = 'password'

    }
})



