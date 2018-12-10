package day07

import java.io.File

class Task(val char: String, val dependencies: MutableSet<Task> = mutableSetOf())

fun MutableMap<String,Task>.addDependency(s1: String, s2: String) =
    getOrPut(s2){ Task(s2) }.dependencies.add(getOrPut(s1){ Task(s1) })

fun MutableCollection<Task>.next() =
    filter { it.dependencies.isEmpty() }.minBy { it.char }

fun readInput(): MutableCollection<Task> = mutableMapOf<String,Task>().run {
    File("src/day07/input").forEachLine {
        val a = it.split(" ")
        addDependency(a[1],a[7])
    }
    return values
}

fun solveA(): String {
    val set = readInput()
    var s = ""
    while (!set.isEmpty()) {
        val nextStep = set.next()!!
        s += nextStep.char
        for (step in set) step.dependencies.remove(nextStep)
        set.remove(nextStep)
    }
    return s
}


data class Worker(val tasks: MutableCollection<Task>, val done: StringBuilder) {

    private var task: Task? = null
    var timeLeft: Int = 0

    fun assignTask(task: Task) {
        this.task = task
        timeLeft = task.char[0].toInt() - 4
    }

    fun doWork() {
        if (task == null) return
        timeLeft--
        if (timeLeft == 0) {
            done.append(task!!.char)
            for (t in tasks) t.dependencies.remove(task!!)
            task = null
        }
    }

    fun isAvailable(): Boolean = timeLeft == 0
}

fun solveB(): Pair<Int, String> {
    val tasks = readInput()
    val done = StringBuilder()
    val workers = Array(5) { Worker(tasks,done) }
    var time = 0
    do {
        tasks.filter   { it.dependencies.isEmpty() }
             .sortedBy { it.char }
             .zip(workers.filter(Worker::isAvailable))
             .forEach  { (task, worker) ->
                tasks.remove(task)
                worker.assignTask(task)
             }
        workers.forEach(Worker::doWork)
        time++
    } while (!(tasks.isEmpty() && workers.all { it.isAvailable() }))
    return time to done.toString()
}

fun main() {
    println("Part 1: ${solveA()}")
    println("Part 2: ${solveB()}")
}