# Swift Basics

## Overview
Swift is a powerful, intuitive, and safe programming language developed by Apple in 2014. It is the primary language for iOS, macOS, watchOS, and tvOS app development, and has expanded to server-side development as well.

## Key Characteristics
- **Paradigm**: Multi-paradigm (protocol-oriented, OOP, functional)
- **Typing**: Static, strong, inferred
- **Compilation**: Compiled to native machine code (LLVM)
- **Memory Management**: Automatic Reference Counting (ARC)
- **Platform**: Apple platforms, Linux, Windows

## Syntax Fundamentals

### Hello World
```swift
print("Hello, World!")
```

### Variables and Data Types
```swift
// Variable (mutable)
var count = 42
var name = "Alice"
var price = 19.99
var isActive = true

// Constant (immutable, preferred)
let maxAge = 120
let pi = 3.14159

// Explicit types
var age: Int = 30
var height: Double = 5.9
var initial: Character = "A"
var message: String = "Hello"

// Type inference
var inferred = "hello"  // Compiler infers String

// Optional (nullable)
var nullableName: String? = nil
var unwrapped: String = "definite"
```

### Control Flow
```swift
// If-else
if x > 0 {
    print("positive")
} else if x < 0 {
    print("negative")
} else {
    print("zero")
}

// If as expression
let result = x > 0 ? "positive" : "non-positive"

// Guard (early exit)
func process(_ value: Int?) {
    guard let value = value else {
        print("No value")
        return
    }
    print("Got: \(value)")
}

// For loop
for i in 0..<10 {
    print(i)
}

for i in stride(from: 0, to: 10, by: 2) {
    print(i)
}

// For-in (collections)
for item in collection {
    print(item)
}

for (index, value) in collection.enumerated() {
    print("\(index): \(value)")
}

// While loop
while count > 0 {
    count -= 1
}

// Repeat-while (do-while)
repeat {
    count += 1
} while count < 10

// Switch (no fallthrough by default)
switch grade {
case "A":
    print("Excellent")
case "B":
    print("Good")
case "C", "D":
    print("Passing")
default:
    print("Other")
}

// Switch with ranges
switch score {
case 90...100:
    print("A")
case 80..<90:
    print("B")
default:
    print("Other")
}

// Switch with tuples
switch (x, y) {
case (0, 0):
    print("Origin")
case (_, 0):
    print("X-axis")
case (0, _):
    print("Y-axis")
default:
    print("Other")
}
```

### Functions
```swift
// Function definition
func add(a: Int, b: Int) -> Int {
    return a + b
}

// Without argument labels
func add(_ a: Int, _ b: Int) -> Int {
    return a + b
}
add(3, 5)  // No labels needed

// Default parameters
func greet(name: String, greeting: String = "Hello") -> String {
    return "\(greeting), \(name)!"
}

// Variadic parameters
func sum(_ numbers: Int...) -> Int {
    return numbers.reduce(0, +)
}

// In-out parameters
func swap(_ a: inout Int, _ b: inout Int) {
    let temp = a
    a = b
    b = temp
}

// Function as parameter
func operate(_ a: Int, _ b: Int, _ operation: (Int, Int) -> Int) -> Int {
    return operation(a, b)
}

// Closure
let multiply: (Int, Int) -> Int = { a, b in
    return a * b
}

// Trailing closure
func performOperation(_ a: Int, _ b: Int, operation: (Int, Int) -> Int) -> Int {
    return operation(a, b)
}

let result = performOperation(3, 5) { $0 * $1 }
```

### Collections
```swift
// Array
var fruits = ["apple", "banana", "cherry"]
fruits.append("date")
fruits.insert("avocado", at: 0)
fruits.remove(at: 2)
fruits.sort()
fruits.reverse()

// Array methods
let doubled = fruits.map { $0.uppercased() }
let filtered = fruits.filter { $0.count > 5 }
let reduced = numbers.reduce(0, +)

// Dictionary
var person = ["name": "Alice", "age": "30"]
person["email"] = "alice@example.com"
person["age"] = "31"

// Set
var unique: Set<Int> = [1, 2, 3, 2, 1]  // {1, 2, 3}
unique.insert(4)
unique.remove(2)

// Tuple
let httpStatus = (code: 200, message: "OK")
print(httpStatus.code)
print(httpStatus.message)
```

### Optionals
```swift
// Optional declaration
var name: String? = "Alice"
var age: Int? = nil

// Forced unwrapping (risky)
let forcedName = name!

// Optional binding (safe)
if let name = name {
    print("Name: \(name)")
} else {
    print("No name")
}

// Guard let
func process(_ value: Int?) {
    guard let value = value else {
        return
    }
    print(value)
}

// Nil coalescing
let displayName = name ?? "Anonymous"

// Optional chaining
let count = person["address"]?.count

// Implicitly unwrapped optional
var assumedName: String! = "Alice"
print(assumedName)  // No need to unwrap
```

### Classes and Structs
```swift
// Class
class Person {
    // Stored properties
    var name: String
    let age: Int

    // Computed property
    var description: String {
        return "\(name) is \(age) years old"
    }

    // Lazy property
    lazy var data = loadData()

    // Property observer
    var score: Int = 0 {
        didSet {
            print("Score changed from \(oldValue) to \(score)")
        }
    }

    // Initializer
    init(name: String, age: Int) {
        self.name = name
        self.age = age
    }

    // Deinitializer
    deinit {
        print("Person deallocated")
    }

    // Method
    func greet() -> String {
        return "Hello, I'm \(name)"
    }

    // Class method
    class func species() -> String {
        return "Homo sapiens"
    }
}

// Struct (value type)
struct Point {
    var x: Double
    var y: Double

    func distance(to other: Point) -> Double {
        let dx = x - other.x
        let dy = y - other.y
        return (dx * dx + dy * dy).squareRoot()
    }

    mutating func move(byX dx: Double, y dy: Double) {
        x += dx
        y += dy
    }
}

// Inheritance
class Employee: Person {
    var company: String

    init(name: String, age: Int, company: String) {
        self.company = company
        super.init(name: name, age: age)
    }

    override func greet() -> String {
        return "\(super.greet()) and work at \(company)"
    }
}
```

### Protocols
```swift
// Protocol definition
protocol Drawable {
    var color: String { get set }
    func draw()
    func describe() -> String  // Required
}

// Protocol extension (default implementation)
extension Drawable {
    func describe() -> String {
        return "A \(color) drawable"
    }
}

// Protocol conformance
struct Circle: Drawable {
    var color: String
    var radius: Double

    func draw() {
        print("Drawing a \(color) circle with radius \(radius)")
    }
}

// Protocol as type
let shapes: [Drawable] = [Circle(color: "red", radius: 5)]

// Protocol composition
func process(item: Drawable & Equatable) { ... }

// Equatable, Comparable, Codable
struct User: Equatable, Codable {
    let id: Int
    let name: String
}
```

### Error Handling
```swift
// Error enum
enum NetworkError: Error {
    case noConnection
    case timeout
    case serverError(Int)
}

// Throwing function
func fetchData() throws -> String {
    guard hasConnection() else {
        throw NetworkError.noConnection
    }
    return "data"
}

// Do-catch
do {
    let data = try fetchData()
    print(data)
} catch NetworkError.noConnection {
    print("No connection")
} catch NetworkError.serverError(let code) {
    print("Server error: \(code)")
} catch {
    print("Unknown error: \(error)")
}

// Try? (returns optional)
let data = try? fetchData()

// Try! (force, crashes on error)
let data = try! fetchData()

// Result type
func fetchData() -> Result<String, NetworkError> {
    guard hasConnection() else {
        return .failure(.noConnection)
    }
    return .success("data")
}

switch fetchData() {
case .success(let data):
    print(data)
case .failure(let error):
    print(error)
}
```

### Closures
```swift
// Closure syntax
let add: (Int, Int) -> Int = { (a: Int, b: Int) -> Int in
    return a + b
}

// Shorthand
let multiply: (Int, Int) -> Int = { $0 * $1 }

// Trailing closure
func perform(_ operation: () -> Void) {
    operation()
}

perform {
    print("Hello")
}

// Capturing values
func makeCounter() -> () -> Int {
    var count = 0
    return {
        count += 1
        return count
    }
}

let counter = makeCounter()
print(counter())  // 1
print(counter())  // 2

// Escaping closure
var completionHandlers: [() -> Void] = []

func withEscaping(_ handler: @escaping () -> Void) {
    completionHandlers.append(handler)
}
```

### Properties and Subscripts
```swift
// Computed property
struct Circle {
    var radius: Double

    var area: Double {
        return Double.pi * radius * radius
    }

    var diameter: Double {
        get { return radius * 2 }
        set { radius = newValue / 2 }
    }
}

// Subscript
struct Matrix {
    var rows: Int
    var columns: Int
    var grid: [Double]

    subscript(row: Int, column: Int) -> Double {
        get {
            return grid[(row * columns) + column]
        }
        set {
            grid[(row * columns) + column] = newValue
        }
    }
}

var matrix = Matrix(rows: 2, columns: 2, grid: [1, 2, 3, 4])
print(matrix[0, 1])  // 2
```

## Common Frameworks
- `UIKit` — iOS user interface
- `SwiftUI` — Declarative UI framework
- `Foundation` — Core data types and utilities
- `Combine` — Reactive programming
- `CoreData` — Object graph and persistence
- `URLSession` — Networking

## Strengths
- Modern, safe, and expressive syntax
- Excellent performance (compiled to native code)
- Strong type system with inference
- Memory safety (ARC, optionals)
- First-class support for Apple platforms
- Growing server-side ecosystem

## Weaknesses
- Primarily tied to Apple ecosystem
- Smaller community than some languages
- ABI stability challenges (improving)
- Limited cross-platform support (improving)
- Younger language with evolving best practices
