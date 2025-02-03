async function abcd() {
	let raw = await fetch('https://randomuser.me/api/')
	let data = await raw.json()
	let result = document.getElementById('Name')
	result.textContent = JSON.stringify(data)
}
