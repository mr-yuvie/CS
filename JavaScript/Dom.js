// // selection of element
// let heading = document.getElementById('heading')
// // let heading = document.querySelector('h1')
// // let heading = document.querySelectorAll('h1')

// // inner html
// heading.innerHTML = 'Bye'

// // inner style
// heading.style.color = 'Red'

// // event listener
// heading.addEventListener('click', function () {
// 	heading.innerHTML = 'Hello'
// })

let Div_1 = document.getElementById('Div_1')
let Button_1 = document.getElementById('Button_1')
let flag = 0
Button_1.addEventListener('click', function () {
	if (flag == 0) {
		Div_1.style.backgroundColor = 'Yellow'
		Button_1.textContent = 'Switch Off'
		flag = 1
	}
	else if(flag == 1){
		Div_1.style.backgroundColor = 'White'
		Button_1.textContent = 'Switch On'
		flag = 0
	}
})

