package day06

import java.io.File
import kotlin.math.abs
import kotlin.math.max

data class Coord(val id: Int, val x: Int, val y: Int)

fun readInput(): Triple<List<Coord>, Int, Int> {
    var maxX = 0
    var maxY = 0
    val input = File("src/day06/input").readLines().withIndex().map { (index, line) ->
        val (x,y) = line.split(", ")
        Coord(index+1, x.toInt(), y.toInt()).also {
            maxX = max(maxX, it.x)
            maxY = max(maxY, it.y)
        }
    }
    return Triple(input, maxX, maxY)
}

fun solveA(): Int {
    val (input, maxX, maxY) = readInput()
    val grid = Array(maxY+1) { Array(maxX+1) { 0 to Double.POSITIVE_INFINITY.toInt() } }
    for (c in input) {
        grid[c.y][c.x] = c.id to Double.NEGATIVE_INFINITY.toInt()
        for (a in 0 until grid.size) for (b in 0 until grid[0].size) {
            val distance = (abs(c.x - b) + abs(c.y - a))
            grid[a][b] = grid[a][b].let { when {
                distance < it.second -> -c.id to distance
                distance == it.second -> 0 to distance
                else -> it
            }}
        }
    }

    val edges = mutableSetOf<Int>()
    for (a in 0 until grid.size) for (b in 0 until grid[0].size) {
        if (a == 0 || a == grid.size-1 || b == 0 || b == grid[0].size) edges.add(abs(grid[a][b].first))
    }

//    grid.forEach {
//        it.forEach {
//            print(when {
//                it.first == 0 -> '.'
//                it.first  < 0 -> (abs(it.first)+96).toChar()
//                else -> (abs(it.first)+64).toChar()
//            })
//        }
//        println()
//    }

    return input.map { (id,_,_) ->
        if (id in edges) id to 0
        else id to grid.sumBy { it.count { abs(it.first) == id } }
    }.maxBy { it.second }!!.second
}

fun solveB(): Int {
    val (input, maxX, maxY) = readInput()
    val grid = Array(maxY+1) { Array(maxX+1) { 0 to 0 } }
    for (c in input) {
        grid[c.y][c.x] = c.id to grid[c.y][c.x].second
        for (a in 0 until grid.size) for (b in 0 until grid[0].size) {
            grid[a][b] = 0 to grid[a][b].second + (abs(c.x - b) + abs(c.y - a))
        }
    }

    return grid.sumBy { it.count { it.second < 10000 } }

}

fun main(args: Array<String>) {
    //println("Part 1: ${solveA()}")
    println("Part 2: ${solveB()}")
}
