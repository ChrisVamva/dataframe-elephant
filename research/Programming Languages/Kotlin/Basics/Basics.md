# Kotlin Basics

## Overview
Kotlin is a modern, statically typed programming language developed by JetBrains in 2011. It is fully interoperable with Java and is the preferred language for Android development. Kotlin runs on the JVM and can also compile to JavaScript and native code.

## Key Characteristics
- **Paradigm**: Object-oriented, functional
- **Typing**: Static, strong, inferred
- **Compilation**: Compiled to JVM bytecode, JavaScript, or native
- **Memory Management**: Automatic garbage collection
- **Platform**: JVM, Android, JavaScript, Native

## Syntax Fundamentals

### Hello World
```kotlin
fun main() {
    println("Hello, World!")
}
```

### Variables and Data Types
```kotlin
var count = 42                  // Mutable variable
val name = "Alice"              // Immutable variable (read-only)

// Explicit types
val age: Int = 30
val price: Double = 19.99
val letter: Char = 'A'
val isActive: Boolean = true
val message: String = "Hello"

// Nullable types
var nullableName: String? = null
val length = nullableName?.length  // Safe call

// Type inference
val inferred = "hello"  // Compiler infers String
```

### Control Flow
```kotlin
// If-else (expression)
val result = if (x > 0) "positive" else "non-positive"

// When (switch equivalent)
when (grade) {
    'A' -> println("Excellent")
    'B' -> println("Good")
    in 'C'..'D' -> println("Passing")
    else -> println("Other")
}

// When as expression
val description = when (x) {
    0 -> "zero"
    in 1..10 -> "small"
    else -> "large"
}

// For loop
for (i in 0 until 10) {
    println(i)
}

for (i in 10 downTo 0 step 2) {
    println(i)
}

// For-each
for (item in collection) {
    println(item)
}

// While loop
while (count > 0) {
    count--
}

do {
    count++
} while (count < 10)
```

### Functions
```kotlin
fun add(a: Int, b: Int): Int {
    return a + b
}

// Single-expression function
fun square(x: Int): Int = x * x

// Default parameters
fun greet(name: String, greeting: String = "Hello"): String {
    return "$greeting, $name!"
}

// Named arguments
greet(name = "Alice", greeting = "Hi")

// Vararg
fun sum(vararg numbers: Int): Int = numbers.sum()

// Extension function
fun String.addExclamation(): String = this + "!"

// Lambda
val multiply: (Int, Int) -> Int = { a, b -> a * b }
```

### Classes and Objects
```kotlin
// Class with primary constructor
class Person(val name: String, var age: Int) {
    // Property with custom getter
    val isAdult: Boolean
        get() = age >= 18

    // Method
    fun describe(): String = "$name is $age years old"

    // Companion object (static members)
    companion object {
        val SPECIES = "Homo sapiens"
    }
}

// Data class (equals, hashCode, toString, copy)
data class User(val name: String, val email: String)

// Inheritance (open class)
open class Animal(val name: String) {
    open fun speak(): String = "..."
}

class Dog(name: String) : Animal(name) {
    override fun speak(): String = "Woof!"
}

// Interface
interface Drawable {
    fun draw()
    fun describe(): String = "A drawable object"
}

// Object declaration (singleton)
object Database {
    const val URL = "jdbc:postgresql://localhost/db"
    fun connect() { /* ... */ }
}

// Sealed class (restricted inheritance)
sealed class Result {
    data class Success(val data: String) : Result()
    data class Error(val message: String) : Result()
}
```

### Null Safety
```kotlin
var name: String = "Alice"     // Non-nullable
var nullable: String? = null   // Nullable

// Safe call
val length = nullable?.length

// Elvis operator
val result = nullable ?: "default"

// Safe cast
val number = value as? Int

// Not-null assertion (risky)
val forced = nullable!!

// Let scope function
nullable?.let {
    println(it.length)
}
```

### Collections
```kotlin
val list = listOf(1, 2, 3, 4, 5)        // Immutable list
val mutableList = mutableListOf(1, 2, 3) // Mutable list
val set = setOf(1, 2, 3)                 // Set
val map = mapOf("a" to 1, "b" to 2)      // Map

// Higher-order functions
val doubled = list.map { it * 2 }
val evens = list.filter { it % 2 == 0 }
val sum = list.reduce { acc, n -> acc + n }
val grouped = list.groupBy { it % 2 }

// Scope functions
val result = list
    .also { println("Processing: $it") }
    .map { it * 2 }
    .filter { it > 4 }

// Apply, let, run, with
val person = Person("Alice", 30).apply {
    age = 31
}
```

### Coroutines
```kotlin
import kotlinx.coroutines.*

// Launch a coroutine
fun main() = runBlocking {
    launch {
        delay(1000)
        println("World!")
    }
    println("Hello,")
}

// Async/await
suspend fun fetchData(): String {
    delay(1000)
    return "data"
}

suspend fun main() {
    val result = async { fetchData() }
    println(result.await())
}
```

## Common Libraries
- `kotlin-stdlib` — Core standard library
- `kotlinx.coroutines` — Asynchronous programming
- `kotlinx.serialization` — JSON/serialization
- `ktor` — Web framework
- `exposed` — Database ORM

## Strengths
- Concise and expressive syntax
- Full Java interoperability
- Null safety built into type system
- Modern language features (coroutines, extension functions)
- Official Android development language
- Multiplatform capabilities

## Weaknesses
- Smaller ecosystem than Java
- Compilation speed can be slower than Java
- Limited use outside JVM/Android
- Learning curve for Java developers
- Fewer resources than more established languages
