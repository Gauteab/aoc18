import java.io.File

var twos = 0
var threes = 0
File("input").forEachLine {
	val seen = IntArray(26)
	for (c in it) {
		seen[c.toInt()-97]++		
	}
	var seenTwo = false
	var seenThree = false
	seen.forEach {
		if (seenTwo && seenThree) return@forEach
		if (it == 2) seenTwo = true
		else if (it == 3) seenThree = true
	}
	if (seenTwo) twos++
	if (seenThree) threes++
}
println(twos*threes)
