let actual_no = 4
let guess_no = Number(prompt('Enter your guess:'))
for (i = 0,chances=1; i < 3; i++,chances++){
    if (actual_no == guess_no) {
        document.write(`Congratulations, You took ${chances} guess`)
        break
    } else {
        guess_no = Number(prompt('Try Again'))
    }
}