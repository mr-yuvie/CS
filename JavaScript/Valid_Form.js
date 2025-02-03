function validation() {
	let uname = document.getElementById('username').value
	let pass = document.getElementById('pass').value
	let cpass = document.getElementById('cpass').value
	let email = document.getElementById('email').value
	let error = document.getElementById('error')
	let error1 = document.getElementById('error1')
	let error2 = document.getElementById('error2')
	let error3 = document.getElementById('error3')
	if (uname == '' || uname.length < 4) {
		error.innerHTML = 'Please enter a username longer than 3 characters'
		return false
	} else {
		error.innerHTML = ''
		if (
			pass == '' ||
			pass.length < 8 ||
			!pass.match(/^[a-zA-Z0-9._-]{8,15}$/)
		) {
			error1.innerHTML =
				'Please enter a password longer than 8 characters'
			return false
		} else {
			error1.innerHTML = ''
			if (pass !== cpass) {
				alert("Passwords Don't Match")
				return false
			} else {
				error2.innerHTML = ''
				if (
					email == '' ||
					!email.match(
						/^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/
					)
				) {
					error3.innerHTML = 'Please enter a valid email id'
					return false
				} else {
					error3.innerHTML = ''
					alert('Form submitted')
					return true
				}
			}
		}
	}
}
