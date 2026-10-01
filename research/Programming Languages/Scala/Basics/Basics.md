# Scala Basics

## Overview
Scala (Scalable Language) is a general-purpose, high-level programming language that combines object-oriented and functional programming paradigms. Created by Martin Odersky in 2004, it runs on the JVM and is fully interoperable with Java. It is widely used in big data processing (Apache Spark) and distributed systems.

## Key Characteristics
- **Paradigm**: Object-oriented, functional
- **Typing**: Static, strong, inferred
- **Compilation**: Compiled to JVM bytecode
- **Memory Management**: Automatic garbage collection
- **Platform**: JVM (Java Virtual Machine)

## Syntax Fundamentals

### Hello World
```scala
object HelloWorld {
  def main(args: Array[String]): Unit = {
    println("Hello, World!")
  }
}
```

### Variables and Data Types
```scala
// Immutable (preferred)
val name = "Alice"
val age: Int = 30
val price: Double = 19.99
val isActive: Boolean = true

// Mutable
var count = 0
count = 1

// Type inference
val inferred = "hello"  // Compiler infers String

// Explicit types
val list: List[Int] = List(1, 2, 3)
val map: Map[String, Int] = Map("a" -> 1, "b" -> 2)

// Unit (like void)
def printSomething(): Unit = {
  println("Something")
}
```

### Control Flow
```scala
// If-else (expression)
val result = if (x > 0) "positive" else "non-positive"

if (x > 0) {
  println("positive")
} else if (x < 0) {
  println("negative")
} else {
  println("zero")
}

// For loop
for (i <- 0 until 10) {
  println(i)
}

// For with multiple generators
for (i <- 1 to 3; j <- 1 to 3) {
  println(s"$i, $j")
}

// For with guard
for (i <- 1 to 10 if i % 2 == 0) {
  println(i)
}

// For comprehension (yield)
val squares = for (i <- 1 to 5) yield i * i

// While loop
while (count > 0) {
  count -= 1
}

// Pattern matching (powerful switch)
val result = grade match {
  case "A" => "Excellent"
  case "B" => "Good"
  case "C" | "D" => "Passing"
  case _ => "Other"
}

// Match with types
val description: String = value match {
  case s: String => s"String: $s"
  case i: Int => s"Int: $i"
  case _ => "Unknown"
}
```

### Functions
```scala
// Function definition
def add(a: Int, b: Int): Int = {
  a + b
}

// Single-expression function
def square(x: Int): Int = x * x

// Default parameters
def greet(name: String, greeting: String = "Hello"): String = {
  s"$greeting, $name!"
}

// Named arguments
greet(name = "Alice", greeting = "Hi")

// Varargs
def sum(numbers: Int*): Int = numbers.sum

// Higher-order functions
def applyTwice(f: Int => Int, x: Int): Int = f(f(x))

// Lambda / anonymous function
val multiply = (a: Int, b: Int) => a * b

// Partial function
val divide: PartialFunction[Int, Int] = {
  case d if d != 0 => 100 / d
}

// Currying
def addCurried(a: Int)(b: Int): Int = a + b
val addFive = addCurried(5) _
```

### Classes and OOP
```scala
// Class with constructor parameters
class Person(val name: String, var age: Int) {
  // Auxiliary constructor
  def this(name: String) = this(name, 0)

  // Method
  def describe(): String = s"$name is $age years old"

  // Override
  override def toString: String = describe()
}

// Case class (immutable, pattern matching support)
case class Point(x: Int, y: Int)

val p1 = Point(3, 7)
val p2 = Point(3, 7)
println(p1 == p2)  // true (structural equality)

// Pattern matching with case classes
val Point(x, y) = p1

// Inheritance
class Employee(name: String, age: Int, val company: String)
  extends Person(name, age) {

  override def describe(): String =
    s"${super.describe()} and works at $company"
}

// Abstract class
abstract class Shape {
  def area: Double
  def perimeter: Double
}

class Circle(val radius: Double) extends Shape {
  def area: Double = math.Pi * radius * radius
  def perimeter: Double = 2 * math.Pi * radius
}

// Trait (interface with concrete methods)
trait Greeter {
  def greet(name: String): String = s"Hello, $name!"
}

trait Logger {
  def log(message: String): Unit = println(s"[LOG] $message")
}

class Service extends Greeter with Logger {
  def doWork(): Unit = {
    log("Starting work")
    println(greet("Alice"))
  }
}

// Object (singleton)
object Database {
  val url = "jdbc:postgresql://localhost/db"
  def connect(): Unit = println("Connected")
}
```

### Collections
```scala
// Immutable List
val list = List(1, 2, 3, 4, 5)
val head = list.head
val tail = list.tail
val doubled = list.map(_ * 2)
val evens = list.filter(_ % 2 == 0)
val sum = list.reduce(_ + _)

// Immutable Map
val map = Map("a" -> 1, "b" -> 2)
val value = map.getOrElse("c", 0)
val updated = map + ("c" -> 3)

// Immutable Set
val set = Set(1, 2, 3, 2, 1)  // Set(1, 2, 3)

// Mutable collections
import scala.collection.mutable
val buffer = mutable.ArrayBuffer(1, 2, 3)
val mutableMap = mutable.Map("a" -> 1)

// Vector (immutable, fast random access)
val vector = Vector(1, 2, 3, 4, 5)

// Range
val range = 1 to 10
val range2 = 1 until 10
val range3 = 1 to 10 by 2

// Collection operations
list.map(_ * 2)           // Transform
list.filter(_ > 2)        // Filter
list.flatMap(x => List(x, x * 2))  // Flat map
list.groupBy(_ % 2)       // Group
list.sortBy(_)            // Sort
list.fold(0)(_ + _)       // Fold
list.zip(otherList)       // Zip
```

### Pattern Matching
```scala
// Value matching
val result = x match {
  case 0 => "zero"
  case 1 => "one"
  case _ => "other"
}

// Type matching
value match {
  case s: String => s"String of length ${s.length}"
  case i: Int if i > 0 => s"Positive int: $i"
  case _ => "Unknown"
}

// Case class matching
case class User(name: String, age: Int)

user match {
  case User("Alice", age) => s"Alice is $age"
  case User(name, 30) => s"$name is 30"
  case User(_, _) => "Someone else"
}

// List matching
list match {
  case Nil => "Empty"
  case head :: tail => s"Head: $head, Tail: $tail"
  case first :: second :: _ => s"First: $first, Second: $second"
}

// Option matching
maybeValue match {
  case Some(value) => s"Got: $value"
  case None => "Nothing"
}
```

### Implicits and Type Classes
```scala
// Implicit parameter
def greet(name: String)(implicit greeting: String): String = {
  s"$greeting, $name!"
}

implicit val defaultGreeting = "Hello"
greet("Alice")  // "Hello, Alice!"

// Implicit class (extension method)
implicit class RichString(s: String) {
  def shout: String = s.toUpperCase + "!"
  def wordCount: Int = s.split("\\s+").length
}

"hello".shout  // "HELLO!"

// Type class pattern
trait Show[A] {
  def show(value: A): String
}

object Show {
  implicit val intShow: Show[Int] = (value: Int) => value.toString
  implicit val stringShow: Show[String] = (value: String) => value
}

def printValue[A](value: A)(implicit show: Show[A]): Unit = {
  println(show.show(value))
}
```

### Functional Programming
```scala
// Higher-order functions
def operate(a: Int, b: Int, op: (Int, Int) => Int): Int = op(a, b)

// Function composition
val addOne = (x: Int) => x + 1
val double = (x: Int) => x * 2
val combined = addOne andThen double  // double(addOne(x))

// Currying
def add(a: Int)(b: Int): Int = a + b
val addFive = add(5) _

// Partial application
val addTen: Int => Int = add(10)

// Monads: Option, Either, Try
val maybeValue: Option[Int] = Some(42)
val result = maybeValue.map(_ * 2).filter(_ > 50)

// For comprehension
val result = for {
  a <- Some(10)
  b <- Some(20)
} yield a + b

// Either for error handling
def divide(a: Int, b: Int): Either[String, Int] = {
  if (b == 0) Left("Division by zero")
  else Right(a / b)
}

// Try for exception handling
import scala.util.{Try, Success, Failure}

val result: Try[Int] = Try(10 / 0)
result match {
  case Success(value) => println(s"Got: $value")
  case Failure(e) => println(s"Error: ${e.getMessage}")
}
```

## Common Libraries
- `akka` — Actor-based concurrency
- `play` — Web framework
- `spark` — Big data processing
- `cats` — Functional programming
- `zio` — Effect system
- `circe` — JSON handling

## Strengths
- Combines OOP and functional programming
- Full Java interoperability
- Concise and expressive syntax
- Strong type system with inference
- Excellent for big data (Spark)
- Immutable collections by default

## Weaknesses
- Steep learning curve
- Complex type system
- Slower compilation than Java
- Binary compatibility issues between versions
- Smaller community than Java
- Complex implicit resolution
