let device_screen = document.getElementById('device_screen')
let logo = document.getElementById('logo')
let logo_img = document.getElementById('logo_img')
let value = 10

device_screen.style.width = window.innerWidth + 'px'
device_screen.style.height = window.innerHeight + 'px'

function colour() {
	r = Math.random() * (254 - 0) + 0
	g = Math.random() * (254 - 0) + 0
	b = Math.random() * (254 - 0) + 0
	logo_img.style.backgroundColor = `rgb(${r},${g},${b})`
}

function update() {
	logo_img.style.marginLeft += value + 'px'
    logo_img.style.marginTop += value + 'px'
}
colour()

setInterval(update,20)
