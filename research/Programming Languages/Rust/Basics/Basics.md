# Rust Basics

## Overview
Rust is a systems programming language focused on safety, speed, and concurrency. Originally developed by Graydon Hoare at Mozilla and first released in 2010, Rust has been voted the "most loved language" in the Stack Overflow Developer Survey for multiple consecutive years.

## Key Characteristics
- **Paradigm**: Multi-paradigm (functional, concurrent, imperative, OOP via traits)
- **Typing**: Static, strong, inferred
- **Compilation**: Compiled to native machine code
- **Memory Management**: Ownership system (no garbage collector)
- **Safety**: Memory safety without GC (prevents null pointers, data races, buffer overflows)

## Syntax Fundamentals

### Hello World
```rust
fn main() {
    println!("Hello, World!");
}
```

### Variables and Data Types
```rust
// Immutable by default
let count = 42;              // Integer (i32 by default)
let name = "Alice";          // String slice (&str)
let is_active = true;        // Boolean

// Mutable
let mut x = 5;
x = 10;

// Explicit types
let age: i64 = 30;
let price: f64 = 19.99;
let letter: char = 'A';

// Constants
const MAX_SIZE: u32 = 100;

// Shadowing (redefine variable)
let y = 5;
let y = y + 1;  // y is now 6

// Tuples
let point = (3, 7);
let (a, b) = point;

// Arrays
let numbers = [1, 2, 3, 4, 5];
let first = numbers[0];
```

### Control Flow
```rust
// If-else
if x > 0 {
    println!("positive");
} else if x < 0 {
    println!("negative");
} else {
    println!("zero");
}

// If as expression
let result = if x > 0 { "positive" } else { "non-positive" };

// Loop (infinite)
loop {
    if condition { break; }
}

// While loop
while count > 0 {
    count -= 1;
}

// For loop (iterating)
for i in 0..10 {
    println!("{}", i);
}

for item in collection.iter() {
    println!("{}", item);
}

// Match (powerful pattern matching)
match grade {
    'A' => println!("Excellent"),
    'B' => println!("Good"),
    'C' | 'D' => println!("Passing"),
    _ => println!("Other"),
}

// Match with value binding
match Some(5) {
    Some(n) if n > 0 => println!("positive: {}", n),
    Some(_) => println!("non-positive"),
    None => println!("nothing"),
}
```

### Functions
```rust
// Function definition
fn add(a: i32, b: i32) -> i32 {
    a + b  // No semicolon = return value
}

// With explicit return
fn divide(a: f64, b: f64) -> Result<f64, String> {
    if b == 0.0 {
        return Err("Division by zero".to_string());
    }
    Ok(a / b)
}

// Generic function
fn largest<T: PartialOrd>(list: &[T]) -> &T {
    let mut max = &list[0];
    for item in list {
        if item > max {
            max = item;
        }
    }
    max
}

// Closures
let square = |x: i32| x * x;
let add = |a: i32, b: i32| -> i32 { a + b };

// Higher-order functions
let doubled: Vec<i32> = numbers.iter().map(|x| x * 2).collect();
let evens: Vec<i32> = numbers.iter().filter(|x| *x % 2 == 0).collect();
```

### Ownership and Borrowing
```rust
// Ownership rules:
// 1. Each value has one owner
// 2. When owner goes out of scope, value is dropped
// 3. Only one owner at a time

let s1 = String::from("hello");
let s2 = s1;  // s1 is moved to s2 (s1 no longer valid)

// Borrowing (references)
let s1 = String::from("hello");
let len = calculate_length(&s1);  // Borrow s1 (immutable reference)

fn calculate_length(s: &String) -> usize {
    s.len()
}

// Mutable reference
let mut s = String::from("hello");
change(&mut s);

fn change(s: &mut String) {
    s.push_str(", world");
}

// Rules:
// - One mutable reference OR any number of immutable references
// - References must always be valid
```

### Structs
```rust
// Struct definition
struct User {
    name: String,
    age: u32,
    active: bool,
}

// Instance
let user = User {
    name: String::from("Alice"),
    age: 30,
    active: true,
};

// Field init shorthand
fn build_user(name: String, age: u32) -> User {
    User { name, age, active: true }
}

// Struct update syntax
let user2 = User {
    name: String::from("Bob"),
    ..user  // Copy remaining fields from user
};

// Tuple structs
struct Point(i32, i32);
let origin = Point(0, 0);

// Methods
impl User {
    fn describe(&self) -> String {
        format!("{} is {} years old", self.name, self.age)
    }

    fn have_birthday(&mut self) {
        self.age += 1;
    }

    // Associated function (no self)
    fn new(name: String, age: u32) -> User {
        User { name, age, active: true }
    }
}
```

### Enums and Pattern Matching
```rust
// Enum definition
enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    ChangeColor(i32, i32, i32),
}

// Enum with data
enum Option<T> {
    Some(T),
    None,
}

enum Result<T, E> {
    Ok(T),
    Err(E),
}

// Pattern matching
match msg {
    Message::Quit => println!("Quit"),
    Message::Move { x, y } => println!("Move to ({}, {})", x, y),
    Message::Write(text) => println!("Text: {}", text),
    Message::ChangeColor(r, g, b) => println!("Color: ({}, {}, {})", r, g, b),
}

// If let (single pattern)
if let Some(value) = maybe_value {
    println!("Got: {}", value);
}

// While let
while let Some(value) = stack.pop() {
    println!("{}", value);
}
```

### Traits
```rust
// Trait definition
trait Summary {
    fn summarize(&self) -> String;

    // Default implementation
    fn default_summary(&self) -> String {
        String::from("(Read more...)")
    }
}

// Implement trait
struct Article {
    title: String,
    content: String,
}

impl Summary for Article {
    fn summarize(&self) -> String {
        format!("{}: {}", self.title, self.content)
    }
}

// Trait bounds
fn notify<T: Summary>(item: &T) {
    println!("{}", item.summarize());
}

// Multiple trait bounds
fn notify2<T: Summary + Display>(item: &T) { ... }

// Where clause
fn some_function<T, U>(t: &T, u: &U) -> String
where
    T: Summary + Clone,
    U: Clone + Debug,
{ ... }
```

### Error Handling
```rust
// Result type
fn read_file(path: &str) -> Result<String, io::Error> {
    let mut file = File::open(path)?;
    let mut contents = String::new();
    file.read_to_string(&mut contents)?;
    Ok(contents)
}

// Unwrap (panics on error)
let content = read_file("file.txt").unwrap();

// Expect (custom panic message)
let content = read_file("file.txt").expect("Failed to read file");

// Match
match read_file("file.txt") {
    Ok(content) => println!("{}", content),
    Err(e) => eprintln!("Error: {}", e),
}

// ? operator (propagate errors)
fn process() -> Result<(), Box<dyn Error>> {
    let content = read_file("file.txt")?;
    let data = parse(&content)?;
    Ok(())
}

// Custom error type
#[derive(Debug)]
struct MyError {
    message: String,
}

impl std::fmt::Display for MyError {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        write!(f, "{}", self.message)
    }
}

impl std::error::Error for MyError {}
```

### Collections
```rust
// Vector (dynamic array)
let mut vec = Vec::new();
vec.push(1);
vec.push(2);
let v = vec![1, 2, 3];  // Macro

// String
let mut s = String::new();
s.push_str("hello");
let s2 = String::from("world");
let combined = s + &s2;  // Concatenation

// HashMap
use std::collections::HashMap;

let mut scores = HashMap::new();
scores.insert("Alice", 90);
scores.insert("Bob", 85);

let score = scores.get("Alice");  // Option<&i32>
scores.entry("Charlie").or_insert(75);

for (name, score) in &scores {
    println!("{}: {}", name, score);
}
```

### Concurrency
```rust
use std::thread;
use std::sync::mpsc;
use std::sync::{Arc, Mutex};

// Spawn thread
let handle = thread::spawn(|| {
    println!("Hello from thread!");
});

handle.join().unwrap();

// Channel (message passing)
let (tx, rx) = mpsc::channel();

thread::spawn(move || {
    tx.send("hello").unwrap();
});

let received = rx.recv().unwrap();

// Shared state with Mutex
let counter = Arc::new(Mutex::new(0));
let mut handles = vec![];

for _ in 0..10 {
    let counter = Arc::clone(&counter);
    let handle = thread::spawn(move || {
        let mut num = counter.lock().unwrap();
        *num += 1;
    });
    handles.push(handle);
}

// Async/await (with tokio)
#[tokio::main]
async fn main() {
    let result = async_function().await;
}
```

## Common Crates
- `serde` — Serialization/deserialization
- `tokio` — Async runtime
- `reqwest` — HTTP client
- `clap` — Command-line argument parsing
- `anyhow` — Error handling
- `rayon` — Data parallelism

## Strengths
- Memory safety without garbage collector
- Zero-cost abstractions
- Fearless concurrency
- Excellent performance (comparable to C/C++)
- Strong type system with inference
- Growing ecosystem and community

## Weaknesses
- Steep learning curve (ownership, lifetimes)
- Longer compilation times
- Verbose compared to some languages
- Smaller ecosystem than C/C++/Java
- Complex error handling for beginners
