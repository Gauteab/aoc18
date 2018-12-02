import java.io.File

val data = File("input").readLines().toTypedArray()
var minDiff = 100
var res = -1 to -1

for (x in 0 until data.size) {
	for (y in x+1 until data.size) {
		var diff = 0
		for (i in 0 until data[x].length) {
			if (data[x][i] != data[y][i]) diff++
		}
		if (minDiff > diff) {
			minDiff = diff
			res = x to y
		}
	}
}
val s1 = data[res.first]
val s2 = data[res.second]
var answer = ""
for (x in 0 until s1.length)
	if (s1[x] == s2[x]) answer += s1[x]
println(answer)
