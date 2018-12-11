package day11

fun power(x: Int, y: Int, serialNumber: Int): Int = (x+10).let { rid ->
    ((rid * y + serialNumber) * rid / 100) % 10 - 5
}

fun solveA(gridSize: Int, squareSize: Int, serialNumber: Int): Pair<Pair<Int, Int>, Int> {
    var maxPower = 0
    var bestPos  = 0 to 0
    val grid = List(gridSize) { y -> IntArray(gridSize) { x -> power(x + 1,y + 1,serialNumber) } }
    for (y in 0 until gridSize - squareSize) {
        for (x in 0 until gridSize - squareSize) {
            var sum = 0
            for (a in x until x + squareSize) {
                for (b in y until y + squareSize) {
                    sum += grid[b][a]
                }
            }
            if (sum > maxPower) {
                maxPower = sum
                bestPos = x + 1 to y + 1
            }
        }
    }
    return bestPos to maxPower
}

fun solveB(serialNumber: Int) =
    (1..300).map {
        solveA(300,it,serialNumber) to it
    }.maxBy { it.first.second }

fun main(args: Array<String>) {
    val serialNumber = 9306
    println("Part 1: ${solveA(300, 3, serialNumber).first}")
    println("Part 2: ${solveB(serialNumber)}")
}