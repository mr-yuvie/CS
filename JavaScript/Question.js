// //Q1. Write a for loop that prints numbers from 1 to 10?
// for (j = 1; j < 11; j++) {
// 	document.write(j, '<br>')
// }

// //Q2. Use a for loop to calculate the sum of all numbers between 1 and 50?
// let sum = 0
// for (i = 1; i < 51; i++) {
// 	sum += i
// }
// document.write(sum, '<br>')

// //Q3. Pattern Challenge:
// // 1
// // 12
// // 123
// // 1234
// // 12345
// let text = ''
// for (k = 1; k < 6; k++) {
// 	text += String(k)
// 	document.write(text, '<br>')
// }

// for (k = 1; k < 6; k++) {
// 	for (j = 1; j < k + 1; j++) {
// 		document.write(j)
// 	}
// 	document.write('<br>')
// }

// //Q4. print prime num?
// to_check = Number(prompt('Enter the number:'))
// not_Prime = false
// for (y = 2; y < to_check; y++) {
// 	if (to_check % y == 0) {
// 		not_Prime = true
// 		document.write('Not Prime')
// 		break
// 	}
// }
// if (not_Prime === false) {
// 	document.write('Prime')
// }

// //Q5. print product of first 5 number?
// let product = 1
// for (l = 1; l < 6; l++) {
// 	product *= l
// }
// document.write(product, '<br>')

// //Q6. print fibonacci series
// let m = 0
// let n = 1
// let p = 0
// document.write('<br>', m, '<br>')
// document.write(n, '<br>')
// for (o = 1; o < 51; o++) {
// 	p = m + n
// 	document.write(p, '<br>')
// 	m = n
// 	n = p
// }

// //Q7. print first 30 even numbers
// for (q = 0, r = 0; q < 30; q++, r += 2) {
// 	document.write(r, '<br>')
// }

// //Q8. print first 23 odd number
// for (s = 0, t = 1; s < 23; s++, t += 2) {
// 	document.write(t, '<br>')
// }

// //Q9. print prime number present b/w 20-500
// for (u = 20; u < 500; u++) {
// 	Prime = true
// 	for (v = 2; v < u; v++) {
// 		if (u % v == 0) {
// 			Prime = false
// 		}
// 	}
// 	if (Prime === true) {
// 		document.write(u, '<br>')
// 	}
// }

// //Q10. Write a for loop that prints the numbers from 1 to 50.
// //For multiples of 3, print "Fizz" instead of the number, and for multiples of 5, print "Buzz".
// //For numbers that are multiples of both 3 and 5, print "FizzBuzz".
// for (z = 1; z < 51; z++) {
// 	if (z % 3 == 0 && z % 5 == 0) {
// 		document.write('FizzBuzz <br>')
// 	} else if (z % 3 == 0) {
// 		document.write('Fizz <br>')
// 	} else if (z % 5 == 0) {
// 		document.write('Buzz <br>')
// 	} else {
// 		document.write(z, '<br>')
// 	}
// }

// //Q11. print prime numbers between 83 and 183
// for (u = 83; u < 184; u++) {
// 	Prime = true
// 	for (v = 2; v < u; v++) {
// 		if (u % v == 0) {
// 			Prime = false
// 		}
// 	}
// 	if (Prime === true) {
// 		document.write(u, '<br>')
// 	}
// }