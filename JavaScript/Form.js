function on_submit() {
	let uname = document.getElementById('name').value
	let password = document.getElementById('password').value
	let c_password = document.getElementById('c_password').value
	let email = document.getElementById('email').value
	let err_1 = document.getElementById('err_1')
	let err_2 = document.getElementById('err_2')
	let err_3 = document.getElementById('err_3')
	let err_4 = document.getElementById('err_4')
	if (uname === '' || uname.length < 4) {
		err_1.textContent = 'Please enter a username longer than 3 characters'
		return false
	} else if ((err_1.textContent = '')) {
		return true
	}
	if (password === '' || password.length < 6) {
		err_2.textContent = 'Please enter a password longer than 5 characters'
		return false
	} else if ((err_2.textContent = '')) {
		return true
	}
	if (c_password === '' || c_password !== password) {
		err_3.textContent = "Passwords Don't Match"
		return false
	} else if ((err_3.textContent = '')) {
		return true
	}
	if (email === '') {
		err_4.textContent = 'Please enter a valid email address'
		return false
	} else if ((err_4.textContent = '')) {
		return true
	}
}
