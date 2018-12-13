package day13

import java.io.File
import kotlin.system.exitProcess

data class Car(val id: Int, var x: Int, var y: Int, var turnDir: Int, var repr: String, var tileUnderCar: String, val part: Int) {

    fun goRight() {
        repr = ">"
        x++
    }
    fun goLeft() {
        repr = "<"
        x--
    }
    fun goUp() {
        repr = "^"
        y--
    }
    fun goDown() {
        repr = "v"
        y++
    }

    fun move(grid: Grid, cars: MutableMap<String, Car>) {

        grid[y][x] = tileUnderCar

        // move
        when (tileUnderCar) {
            "-" -> x += if (repr == ">") 1 else -1
            "|" -> y += if (repr == "v") 1 else -1
            "/" -> when (repr) {
                "^" -> goRight()
                ">" -> goUp()
                "v" -> goLeft()
                "<" -> goDown()
            }
            "\\" -> when (repr) {
                "v" -> goRight()
                ">" -> goDown()
                "^" -> goLeft()
                "<" -> goUp()
            }
            "+" -> {
                when (repr) {
                    "v" -> when (turnDir) {
                        0 -> goRight()
                        1 -> y += 1
                        2 -> goLeft()
                    }
                    ">" -> when (turnDir) {
                        0 -> goUp()
                        1 -> x += 1
                        2 -> goDown()
                    }
                    "^" -> when (turnDir) {
                        0 -> goLeft()
                        1 -> y -= 1
                        2 -> goRight()
                    }
                    "<" -> when (turnDir) {
                        0 -> goDown()
                        1 -> x -= 1
                        2 -> goUp()
                    }
                }
                turnDir = (turnDir+1) % 3
           }
        }

        tileUnderCar = grid[y][x]
        grid[y][x] = id.toString()

        // Check crash
        if (tileUnderCar !in symbols) {
            if (part == 1) {
                println("Crash! (x = $x, y = $y)")
                exitProcess(0)
            } else {
                grid[y][x] = cars[tileUnderCar]!!.tileUnderCar
                cars.remove(id.toString())
                cars.remove(tileUnderCar)
                if (cars.size == 1) {
                    val finalCar = cars.values.first()
                    println(finalCar)
                    exitProcess(0)
                }
            }
        }
    }
}
typealias Grid = Array<Array<String>>

val carSymbols = setOf("<",">","^","v")
val symbols = carSymbols + setOf("\\","/","+","-","|")

fun readInput(part: Int): Pair<Array<Array<String>>, MutableMap<String, Car>> {
    val input = File("input").readLines()
    val width = input.maxBy { it.length }!!.length
    val height = input.size
    val grid = Array(height) { Array(width) {""} }
    val cars = mutableMapOf<String,Car>()
    var carId = 0
    input.forEachIndexed { y, s ->
        s.forEachIndexed { x, c ->
            if (c.toString() in carSymbols) {
                val tileUnder = when (c) {
                    '<','>' -> "-"
                    '^','v' -> "|"
                    else -> TODO()
                }
                val id = carId++
                cars += id.toString() to Car(id,x,y,0,c.toString(),tileUnder,part)
                grid[y][x] = id.toString()
            } else {
                grid[y][x] = c.toString()
            }
        }
    }
    return grid to cars
}

fun Grid.print() = forEach { it.forEach { print(it) } ; println() }

fun Grid.tick(cars: MutableMap<String,Car>) {
    val carsToMove = mutableListOf<String>()
    for (ss in this) {
        for (s in ss) {
            if (s in cars) carsToMove += s
        }
    }
    carsToMove.forEach {
        cars[it]?.move(this,cars)
    }
}

fun solve(part: Int) {
    val (grid,cars) = readInput(part)
    while (true) {
        grid.tick(cars)
    }
}

fun main(args: Array<String>) {
    //solve(1)
    solve(2)
}