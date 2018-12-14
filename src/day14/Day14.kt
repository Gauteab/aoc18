package day14

val input = 260321
val inputList = input.toString().map { it.toString().toInt() }
data class Elf(val id: Int, var index: Int)

val elves = setOf(Elf(1,0),Elf(2,1))
val scoreboard = mutableListOf(3,7)

fun next() {
    val sum = elves.sumBy { scoreboard[it.index] }
    for (d in sum.toString())
        scoreboard += d.toString().toInt()
    for (e in elves)
        e.index = (e.index + 1 + scoreboard[e.index]) % scoreboard.size
}

fun solveA() {
    while (true) {
        next()
        if (scoreboard.size > input + 10) {
            val res = scoreboard.slice(input until input + 10).joinToString("").toLong()
            println("Part 1: $res")
            break
        }
    }
}

fun solveB() {
    while (true) {
        next()
        if (scoreboard.size < 15) continue
        if (!(inputList.last() == scoreboard.last() || inputList.last() == scoreboard[scoreboard.size-2])) continue
        val sub1 = scoreboard.slice(scoreboard.size- inputList.size until scoreboard.size)
        if (inputList == sub1) {
            println(scoreboard.size- inputList.size)
            break
        }
        val sub2 = scoreboard.slice(scoreboard.size - inputList.size - 1 until scoreboard.size-1)
        if (inputList == sub2) {
            println(scoreboard.size- inputList.size-1)
            break
        }

    }
}

fun main(args: Array<String>) {
    //solveA()
    solveB()
}
