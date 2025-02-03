// let Details = {
// 	students: [
// 		{
// 			name: 'Yuv',
// 			age: 17,
// 		},
// 		{
// 			name: 'Palak',
// 			age: 18,
// 		},
// 		{
// 			name: 'Sid',
// 			age: 17,
// 		},
// 		{
// 			name: 'Abhinav',
// 			age: 20,
// 		},
// 	],
// }
// console.log(Details)

// let Product_Details = {
// 	order_id: '2143D',
// 	customer_detail: {
// 		name: 'yuv',
// 		email: 'yuv@gmail.com',
// 	},
// 	Number_of_Items: [
// 		{
// 			quantity: 10,
// 			product_name: 'Headphones',
// 			Product_price: 500,
// 		},
// 		{
// 			quantity: 5,
// 			product_name: 'Mouse',
// 			Product_price: 100,
// 		},
// 		{
// 			quantity: 4,
// 			product_name: 'Monitor',
// 			Product_price: 5000,
// 		},
// 	],
// 	Total_amount: 25500,
// }
// console.log(Product_Details)

async function abcd() {
	let raw = await fetch('https://randomuser.me/api/')
	let data = await raw.json()
	console.log(data)
}
abcd()
