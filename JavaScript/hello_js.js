// // alert("Hello World")
// // document.write("bla bla")
// // f-string is used in `${}`
// // prompt("is used to get input from the user")

// let num = Number(prompt('Enter a number:'))

// if (num > 0) {
//     if (num % 2 == 0) {
//         document.write('Even')
//     } else {
//         document.write('Odd')
//     }
// } else {
//     document.write('Enter a positive number')
// }

// let a = 'Written from python'

// // Username=Admin, Password=@Admin123
// let username = prompt('Enter your username:')

// if (username == 'Admin') {
//     let password = prompt('Enter password')
//     if (password == '@Admin123') {
//         document.write('Welcome Admin')
//     } else {
//         document.write('Incorrect Password')
//     }
// } else {
//     document.write('Unknown User')
// }

// // Gender=M then Room 5, Gender=F then Room 3
// let age = Number(prompt('Enter your age:'))

// if (age > 18) {
//     let gender = prompt('Enter your gender:')
//     if (gender == 'M') {
//         document.write('Go to Room Number 5')
//     }
//     if (gender == 'F') {
//         document.write('Go to Room Number 3')
//     } else {
//         document.write('Wrong Input')
//     }
// } else {
//     document.write('You are not eligible for boating')
// }

// const marks = Number(prompt('Enter your marks:'))
// let Branch

// switch (true) {
//     case marks >= 90:
//         Branch = 'Computer Science'
//         break
//     case marks >= 80:
//         Branch = 'Mechanical Engineering'
//         break
//     case marks >= 70:
//         Branch = 'Chemical Engineering'
//         break
//     case marks >= 60:
//         Branch = 'Electronics and Communication'
//         break
//     case marks >= 50:
//         Branch = 'Civil Engineering'
//         break
//     case marks <= 33:
//         document.write('You Failed.')
//         break
//     default:
//         Branch = 'Bio Technology'
// }
// document.write(Branch)

// const operation = Number(
//     prompt(`Enter
//     1 For Addition
//     2 For Subtraction
//     3 for Multiplication
//     4 for Division`)
// )

// const num1 = Number(prompt('Enter First Number:'))
// const num2 = Number(prompt('Enter Second Number:'))

// switch (true) {
//     case operation == 1:
//         document.write(num1 + num2)
//         break
//     case operation == 2:
//         document.write(num1 - num2)
//         break
//     case operation == 3:
//         document.write(num1 * num2)
//         break
//     case operation == 4:
//         document.write(num1 / num2)
//         break
//     default:
//         document.write('Wrong Input')
// }

// let i = 0
// let text = ''
// do {
// 	text = '<br>The number is ' + i
//     i++
//     document.write(text)
// } while (i < 10)

// let i = 0
// let text = ''
// while (i < 10) {
// 	text = '<br>The number is ' + i
// 	i++
// 	document.write(text)
// }

// let marks = Number(prompt('Enter your marks:'))
// let grade = ''

// if (marks >= 90) {
// 	if (marks >= 95) {
// 		grade = 'A+'
// 	} else {
// 		grade = 'A'
// 	}
// }
// if (marks >= 80 && marks < 90) {
// 	if (marks >= 85) {
// 		grade = 'B+'
// 	} else {
// 		grade = 'B'
// 	}
// }
// if (marks >= 70 && marks < 80) {
// 	if (marks >= 75) {
// 		grade = 'C+'
// 	} else {
// 		grade = 'C'
// 	}
// }
// if (marks >= 60 && marks < 70) {
// 	if (marks >= 65) {
// 		grade = 'D+'
// 	} else {
// 		grade = 'D'
// 	}
// }
// if (marks < 60 && marks > 33) {
// 	grade = 'E'
// }
// if (marks < 33) {
// 	grade = 'F'
// }

// document.write('Your grade is: ', grade)

// let name = "Yuv"
// for (i = 0; i < 10; i++){
//     document.write('My name is: ', name, '<br>')
// }

// let num3 = Number(prompt('Enter number:'))
// for (j = 2; j < 9; j++) {
    // document.write(`Table of ${j}<br>`)
// 	for (i = 1; i < 11; i++) {
// 		document.write(`${j} x ${i} = ${j * i}<br>`)
// 	}
// 	document.write('<br>')
// }

// for (i = 1; i < 4; i++){
//     for (j = 1; j < 4; j++){
//         document.write(`*`)
//     }
//     document.write('<br>')
// }

// let text = '*'
// for (i = 1; i < 6; i++) {
// 	// document.write(`${i*'*'}<br>`)  Doesn't work
// 	document.write(text, '<br>')
// 	text += '*'
// }

// for (k = 1; k < 6; k++) {
// 	for (j = 1; j < k + 1; j++) {
// 		document.write('*')
// 	}
// 	document.write('<br>')
// }