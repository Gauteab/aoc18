import java.io.File
import java.time.LocalDateTime
import java.time.format.DateTimeFormatter

fun parseDate(date:String) = LocalDateTime.parse(date, DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm"))

val data: MutableMap<Int, MutableList<Pair<LocalDateTime, LocalDateTime>>> =
    File("src/day04/input").readLines().map {
        val (date, info) = "\\[(.*)] (.*)".toRegex().find(it)!!.destructured
        when (info) {
            "wakes up", "falls asleep" -> null to parseDate(date)
            else -> info.split(" ")[1].drop(1).toInt() to parseDate(date)
    }}.sortedBy{it.second}.iterator().run {
        val entries = mutableMapOf<Int, MutableList<Pair<LocalDateTime,LocalDateTime>>>()
        var curId = 0
        while (hasNext()) next().also {
            if (it.first == null) entries[curId]!!.add(it.second to next().second)
            else {
                curId = it.first!!
                if (curId !in entries) entries += curId to mutableListOf()
            }
        }
        entries
    }

fun mapEntryToMatrix(entry: Map.Entry<Int, MutableList<Pair<LocalDateTime, LocalDateTime>>>?): Pair<Int, Array<IntArray>> {
    val table = Array(entry!!.value.size) { IntArray(60) }
    for ((i,v) in entry.value.withIndex()) {
        for (x in v.first.minute until v.second.minute) {
            table[i][x] = 1
        }
    }
    return entry.key to table
}

fun maxOfEntryMatrix(p: Pair<Int, Array<IntArray>>): Pair<Pair<Int, Int>, Int> {
    val table = p.second
    var maxMin = -1
    var maxMinIndex = -1
    for (y in 0 until 60) {
        var sum = 0
        for (x in 0 until table.size) {
            sum += table[x][y]
        }
        if (sum > maxMin) {
            maxMin = sum
            maxMinIndex = y
        }
    }
    return p.first to maxMinIndex to maxMin
}

fun solveA() =
    maxOfEntryMatrix (
        mapEntryToMatrix(data.entries.maxBy { it.value.fold (0) { acc, e ->
            acc + e.second.minute - e.first.minute
        }})
    ).also {
        print("Part 1: ")
        println(it.first.first * it.first.second)
    }

fun solveB() = data
    .map(::mapEntryToMatrix)
    .map(::maxOfEntryMatrix)
    .maxBy { it.second }!!
    .also {
        print("Part 2: ")
        println(it.first.first * it.first.second)
    }

fun main(args: Array<String>) {
    solveA()
    solveB()
}