package day08

import java.io.File

val input = File("src/day08/input").readText().split(" ").map(String::toInt)

fun solveA(input: List<Int>): Int {
    var i   = 0
    var sum = 0
    fun parseNode() {
        val childrenCount = input[i++]
        val metadataCount = input[i++]
        repeat(childrenCount) { parseNode()       }
        repeat(metadataCount) { sum += input[i++] }
    }
    parseNode()
    return sum
}

fun solveB(input: List<Int>): Int {
    fun sumNode(index: Int): Int {
        var i = index
        val childrenCount = input[i++]
        val metadataCount = input[i++]
        var sum = 0
        // Base case
        if (childrenCount == 0) {
            repeat(metadataCount) { sum += input[i++] }
            return sum
        }
        // Find children
        val childIndexes = mutableListOf<Int>()
        fun passThroughNode() { // Just pass through the node
            val cCount = input[i++]
            val mCount = input[i++]
            repeat(cCount) { passThroughNode() }
            repeat(mCount) { i++ }
        }
        repeat(childrenCount) {
            childIndexes.add(i)
            passThroughNode()
        }
        repeat(metadataCount) {
            val ci = input[i++]-1
            if (ci < childIndexes.size)
                sum += sumNode(childIndexes[ci])
        }
        return sum
    }
    return sumNode(0)
}

fun main(args: Array<String>) {
    println("Part 1: ${solveA(input)}")
    println("Part 2: ${solveB(input)}")
}