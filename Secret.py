esoteric
esoteric {
	watcher hour {
		now = getHour24()

		if now between 11 and 21 {
			greet()
		} else {
			exit
		}
	}

	function greet {
		string message = "Hello World"
		times = calculateStringLength(message)
		counter = 0

		while counter < times {
			char ch = message[counter]
			printCharWithDelay(ch)
			counter++
		}
	}

	function printCharWithDelay(char ch) {
		delay(200) // Delay 200 milliseconds
		printChar(ch)
	}

	initiate watcher
}
