let main = document.getElementById('main')
let name_1 = document.getElementById('heading')
let Button_1 = document.getElementById('Button_1')
let flag = 0
Button_1.addEventListener('click', function () {
	if (flag == 0) {
		name_1.style.color = 'Green'
		Button_1.textContent = 'Remove'
		name_1.textContent = 'Friends'
		flag = 1
	} else if (flag == 1) {
		name_1.style.color = 'Red'
		Button_1.textContent = 'Add'
		name_1.textContent = 'Stranger'
		flag = 0
	}
})
