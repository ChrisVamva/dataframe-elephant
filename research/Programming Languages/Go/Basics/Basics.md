# Go Basics

## Overview
Go (also known as Golang) is a statically typed, compiled programming language developed by Google in 2009. It was designed for simplicity, efficiency, and excellent support for concurrent programming.

## Key Characteristics
- **Paradigm**: Procedural, concurrent
- **Typing**: Static, strong, inferred (with `:=`)
- **Compilation**: Compiled to native machine code
- **Memory Management**: Automatic garbage collection
- **Concurrency**: Goroutines and channels (CSP model)

## Syntax Fundamentals

### Hello World
```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

### Variables and Data Types
```go
var count int = 42              // Explicit declaration
var name string = "Alice"       // String
var pi float64 = 3.14159        // Float
var isActive bool = true        // Boolean

// Short declaration (type inference)
x := 10
y := "hello"
z := 3.14

// Constants
const MaxSize = 100
const (
    StatusOK    = 200
    StatusError = 500
)

// Zero values
var a int       // 0
var b string    // ""
var c bool      // false
```

### Control Flow
```go
// If-else
if x > 0 {
    fmt.Println("positive")
} else if x < 0 {
    fmt.Println("negative")
} else {
    fmt.Println("zero")
}

// If with initialization
if err := doSomething(); err != nil {
    return err
}

// For loop (only loop construct)
for i := 0; i < 10; i++ {
    fmt.Println(i)
}

// While-style
for count > 0 {
    count--
}

// Infinite loop
for {
    // ...
}

// Range loop
for index, value := range slice {
    fmt.Println(index, value)
}

// Switch
switch grade {
case "A":
    fmt.Println("Excellent")
case "B":
    fmt.Println("Good")
default:
    fmt.Println("Other")
}
```

### Functions
```go
func add(a int, b int) int {
    return a + b
}

// Multiple return values
func divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, fmt.Errorf("division by zero")
    }
    return a / b, nil
}

// Named return values
func rectangle(width, height float64) (area, perimeter float64) {
    area = width * height
    perimeter = 2 * (width + height)
    return
}

// Variadic functions
func sum(numbers ...int) int {
    total := 0
    for _, n := range numbers {
        total += n
    }
    return total
}
```

### Structs and Methods
```go
type Person struct {
    Name string
    Age  int
}

// Method with value receiver
func (p Person) Describe() string {
    return fmt.Sprintf("%s is %d years old", p.Name, p.Age)
}

// Method with pointer receiver
func (p *Person) HaveBirthday() {
    p.Age++
}

p := Person{Name: "Alice", Age: 30}
fmt.Println(p.Describe())
```

### Interfaces
```go
type Shape interface {
    Area() float64
    Perimeter() float64
}

type Circle struct {
    Radius float64
}

func (c Circle) Area() float64 {
    return math.Pi * c.Radius * c.Radius
}

func (c Circle) Perimeter() float64 {
    return 2 * math.Pi * c.Radius
}

// Implicit implementation
var s Shape = Circle{Radius: 5}
fmt.Println(s.Area())
```

### Concurrency
```go
// Goroutine (lightweight thread)
go func() {
    fmt.Println("Running in background")
}()

// Channel
ch := make(chan int)

go func() {
    ch <- 42  // Send value
}()

value := <-ch  // Receive value

// Buffered channel
buffered := make(chan int, 10)

// Select (multiplexing channels)
select {
case msg1 := <-ch1:
    fmt.Println("Received from ch1:", msg1)
case msg2 := <-ch2:
    fmt.Println("Received from ch2:", msg2)
case <-time.After(5 * time.Second):
    fmt.Println("Timeout")
}

// Worker pool pattern
jobs := make(chan int, 100)
results := make(chan int, 100)

for w := 1; w <= 3; w++ {
    go worker(w, jobs, results)
}
```

### Error Handling
```go
// Explicit error checking (no exceptions)
result, err := doSomething()
if err != nil {
    log.Fatal(err)
}

// Custom errors
type NotFoundError struct {
    ID int
}

func (e *NotFoundError) Error() string {
    return fmt.Sprintf("resource %d not found", e.ID)
}
```

## Common Packages
- `fmt` — Formatted I/O
- `net/http` — HTTP client and server
- `os` — Operating system interface
- `strings` — String manipulation
- `encoding/json` — JSON encoding/decoding
- `sync` — Synchronization primitives
- `testing` — Unit testing

## Strengths
- Simple, readable syntax
- Excellent concurrency primitives
- Fast compilation and execution
- Strong standard library
- Great for microservices and cloud-native apps

## Weaknesses
- No generics (until Go 1.18, now limited)
- Verbose error handling
- No function overloading
- Limited metaprogramming
- Young ecosystem compared to older languages
