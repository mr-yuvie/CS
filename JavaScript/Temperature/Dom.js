import { convert_to_cel, convert_to_far } from './App.js'

let Button_1 = document.getElementById('Button_1')

Button_1.addEventListener('click', function () {
	let Options = document.getElementById('Options').value
	let value = document.getElementById('u_input').value
	let result = document.getElementById('result')
	if (Options == 0) {
		result.textContent = convert_to_far(value)
	} else if (Options == 1) {
		result.textContent = convert_to_cel(value)
	}
})
