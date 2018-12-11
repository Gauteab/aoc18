package day09

import java.util.*

fun solve(players: Int, highest: Int): Map.Entry<Int, Long>? {
    val iter = generateSequence(1) { if (it == players) 1 else it+1 }.iterator()
    val scores = (1..players).associate { it to 0L }.toMutableMap()
    val deque = LinkedList<Long>()
    deque.add(0)
    for (value in 1L..highest) iter.next().let {
        if (value % 23 == 0L) {
            repeat(7) { deque.push(deque.removeLast()) }
            scores[it] = scores[it]!! + deque.removeFirst() + value
            return@let
        }
        deque.addLast(deque.removeFirst())
        deque.addLast(deque.removeFirst())
        deque.addFirst(value)
    }
    return scores.maxBy { it.value }
}

fun main(args: Array<String>) {
    println("Part 1: ${solve(448,71628)}")
    println("Part 2: ${solve(448,71628*100)}")
}

