import java.io.File

File("input").readLines().fold(0){x,y->x+y.toInt()}.also(::println)
