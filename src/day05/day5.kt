package day05

import java.io.File

fun Char.reverseCase() = if (isUpperCase()) toLowerCase() else toUpperCase()

fun solveA(input: String): Int {
    val sb = StringBuilder(" ")
    for (c in input) when (c.reverseCase()) {
        sb.last() -> sb.deleteCharAt(sb.length-1)
        else      -> sb.append(c)
    }
    return sb.length-1
}

fun solveB(input: String) = ('a'..'z').map {
    solveA(input.filter { c ->
        c != it && c != it.reverseCase()
    })
}.min()

fun main(args: Array<String>) {
    val input = File("src/day05/input").readText()
    solveA(input).also { println("Part 1: $it") }
    solveB(input).also { println("Part 2: $it") }
}