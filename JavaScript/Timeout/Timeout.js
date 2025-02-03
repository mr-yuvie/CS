// console.log('hello')
// console.log('good mrg')
// setTimeout(function () {
// 	console.log('bye')
// }, 10000)
// console.log('hii')

//    setTimeout(
//     function hello(){
//        alert ("hello")
//     },3000)

// let a = 0
// setInterval(hello, 2000)
// function hello() {
//     a = a + 2
//     document.write(a)
// }

// let mydiv = document.getElementById('mydiv')

// let value = 0
// function time() {
// 	value += 50
// 	mydiv.style.marginLeft = value + 'px'
// 	setTimeout(function () {
// 		mydiv.style.marginTop = value + 'px'
// 	}, 500)
// }
// setInterval(time, 2000)

let mydiv = document.getElementById('mydiv')

let value_top = 0
let value_left = 0
let start = 0
function time() {
	if (start < 10) {
		value_top += 50
		mydiv.style.marginTop = value_top + 'px'
		start += 1
	} else if (start >= 10 && start < 30) {
		value_left += 50
		mydiv.style.marginLeft = value_left + 'px'
		start += 1
	} else if (start >= 30 && start < 40) {
		value_top -= 50
		mydiv.style.marginTop = value_top + 'px'
		start += 1
	} else if (start >= 40 && start < 60) {
		value_left -= 50
		mydiv.style.marginLeft = value_left + 'px'
		start += 1
		if (start == 60) {
			start = 0
		}
	}
	console.log('start:', start)
	console.log('top:', value_top)
	console.log('left:', value_left)
}
setInterval(time, 500)
