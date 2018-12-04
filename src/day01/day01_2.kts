import java.io.File

var freq = 0
val freqSet = mutableSetOf<Int>(0)
val data = File("input").readLines()
loop@while(true) {
	for (it in data) {
		freq += it.toInt()
		if (freq in freqSet) {
			println(freq)
			break@loop
		}
		freqSet.add(freq)
	}
}
