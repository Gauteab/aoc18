import java.io.File

val rules: Map<String, Int> = File("input").readLines().associate { line ->
    line.split(" => ").let {
        it[0] to if (it[1] == "#") 1 else 0
    }
}

fun main(args: Array<String>) {
    val bufferSize = 500
    val buffer1 = IntArray(bufferSize)
    val buffer2 = IntArray(bufferSize)
    var outBuffer = buffer1
    var inBuffer  = buffer2
    val startIndex = bufferSize / 4
    val initState = "##.#.####..#####..#.....##....#.#######..#.#...........#......##...##.#...####..##.#..##.....#..####"
    initState.forEachIndexed { i, c ->
        outBuffer[startIndex + i] = if (c == '#') 1 else 0
    }

    val numGenerations = 128
    var it = 0
    while (true) {

        val start = 0
        val end = buffer1.size - 6

        // print
        {if (it < 10) print(" ")
        print("$it: ")
        for (i in start .. end) {
            print(if (outBuffer[i] == 1) '#' else '.')
        }
        println()}()

        if (it++ == numGenerations) break

        for (i in start .. end) {
            val slice = outBuffer.sliceArray(i until i+5)
            val code = slice.joinToString("") { if (it == 1) "#" else "." }
            val res = rules.getOrDefault(code,0)
            inBuffer[i+2] = res
        }

        // swap buffers
        val tmp = inBuffer
        inBuffer = outBuffer
        outBuffer = tmp
    }

    var sum = 0L
    val offset = 50_000_000_000L - 128
    outBuffer.forEachIndexed { index, it ->
        if (it == 1) sum += index - startIndex + offset
    }
    println(sum)
}


