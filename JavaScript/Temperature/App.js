export function convert_to_cel(value) {
	let temp = 0
	temp = (value - 32) / 1.8
	return temp
}

export function convert_to_far(value) {
	let temp = 0
	temp = value * 1.8 + 32
	return temp
}
