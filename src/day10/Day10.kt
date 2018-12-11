package day10

import java.io.File
import kotlin.math.max
import kotlin.math.min
import kotlin.system.exitProcess

fun List<IntArray>.move() = forEach {
    it[0] += it[2]
    it[1] += it[3]
}

fun List<IntArray>.draw(time: Int) {
    var minX = Double.POSITIVE_INFINITY.toInt()
    var minY = Double.POSITIVE_INFINITY.toInt()
    var maxX = Double.NEGATIVE_INFINITY.toInt()
    var maxY = Double.NEGATIVE_INFINITY.toInt()
    for (it in this) {
        minX = min(minX, it[0])
        maxX = max(maxX, it[0])
        minY = min(minY, it[1])
        maxY = max(maxY, it[1])
    }
    val verticalSize = maxY - minY + 1
    if (verticalSize > 10) return
    val grid = Array(verticalSize) { Array(maxX-minX+1) {" "} }
    forEach { grid[it[1]-minY][it[0]-minX] = "#" }
    grid.forEach { it.forEach { print(it) }; println() }
    println("Time: $time")
    exitProcess(0)
}

fun main(args: Array<String>) {
    var time = 0
    val input: List<IntArray> = File("input").readLines().map {
        it.split(" ").filter {!it.isBlank()}.map(String::toInt).toIntArray()
    }
    while (true) {
        input.move()
        input.draw(++time)
    }
}
