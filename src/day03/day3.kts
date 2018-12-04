import java.io.File

data class Claim(val id: Int, val marginLeft: Int, val marginTop: Int, val width: Int, val height: Int) {
    // Awful solution
    fun overlaps(other: Claim): Boolean =
        ((marginLeft .. marginLeft+width) intersect (other.marginLeft .. other.marginLeft+other.width)).size>0 &&
        ((marginTop ..  marginTop+height) intersect (other.marginTop .. other.marginTop+other.height)).size>0
}

var maxWidth = 0
var maxHeight = 0
val data = File("input").readLines().map {
    val (a,b,c,d,e) = "#(\\d+) @ (\\d+),(\\d+): (\\d+)x(\\d+)".toRegex().find(it)!!.destructured
    Claim(a.toInt(),b.toInt(),c.toInt(),d.toInt(),e.toInt())
        .also {
            maxWidth  = maxOf(maxWidth, it.marginLeft + it.width)
            maxHeight = maxOf(maxHeight, it.marginTop + it.height)
        }
}

val matrix = Array(maxHeight) { IntArray(maxWidth) }
for (claim in data) {
    for (x in claim.marginLeft until (claim.marginLeft + claim.width)) {
        for (y in claim.marginTop until (claim.marginTop + claim.height)) {
            matrix[y][x]++
        }
    }
}

print("Part 1: ")
var count = 0
matrix.forEach { it.forEach {
    if (it > 1) count++
}}
println(count)

print("Part 2: ")
loop@for (c1 in data) {
    var overlaps = 0
    for (c2 in data) {
        if (c1 !== c2 && c1.overlaps(c2)) overlaps++
    }
    if (overlaps == 0) {
        println(c1.id)
        break@loop
    }
}
