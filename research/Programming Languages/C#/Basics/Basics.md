# C# Basics

## Overview
C# (pronounced "C Sharp") is a modern, object-oriented, type-safe programming language developed by Microsoft in 2000. It is a core language of the .NET ecosystem and is widely used for web, desktop, mobile, and game development.

## Key Characteristics
- **Paradigm**: Object-oriented, component-oriented, functional
- **Typing**: Static, strong, inferred
- **Compilation**: Compiled to IL (Intermediate Language), JIT-compiled at runtime
- **Memory Management**: Automatic garbage collection
- **Platform**: Cross-platform via .NET (Windows, Linux, macOS)

## Syntax Fundamentals

### Hello World
```csharp
using System;

class Program {
    static void Main() {
        Console.WriteLine("Hello, World!");
    }
}
```

### Variables and Data Types
```csharp
int count = 42;                  // 32-bit integer
long bigNum = 9_000_000_000L;    // 64-bit integer
double price = 19.99;            // 64-bit float
decimal money = 100.50m;         // 128-bit precise decimal
char letter = 'A';               // 16-bit Unicode character
string name = "Alice";           // Immutable string
bool isActive = true;            // Boolean
var inferred = "hello";          // Type inference
```

### Control Flow
```csharp
// If-else
if (x > 0) {
    Console.WriteLine("positive");
} else if (x < 0) {
    Console.WriteLine("negative");
} else {
    Console.WriteLine("zero");
}

// For loop
for (int i = 0; i < 10; i++) {
    Console.WriteLine(i);
}

// Foreach loop
foreach (var item in collection) {
    Console.WriteLine(item);
}

// While loop
while (count > 0) {
    count--;
}

// Switch expression (C# 8+)
var result = grade switch {
    'A' => "Excellent",
    'B' => "Good",
    _   => "Other"
};
```

### Classes and Objects
```csharp
public class Person {
    // Auto-implemented property
    public string Name { get; set; }
    public int Age { get; set; }

    // Constructor
    public Person(string name, int age) {
        Name = name;
        Age = age;
    }

    // Method
    public override string ToString() => $"{Name}, {Age}";
}

var person = new Person("Alice", 30);
Console.WriteLine(person);
```

### LINQ (Language Integrated Query)
```csharp
var numbers = new[] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

var evens = numbers.Where(n => n % 2 == 0);
var squares = numbers.Select(n => n * n);
var sum = numbers.Sum();
```

### Async/Await
```csharp
public async Task<string> FetchDataAsync() {
    using var client = new HttpClient();
    var response = await client.GetStringAsync("https://api.example.com/data");
    return response;
}
```

## Common Namespaces
- `System` — Base types, console I/O, math
- `System.Collections.Generic` — Lists, dictionaries, queues
- `System.Linq` — Query expressions
- `System.IO` — File and stream I/O
- `System.Net.Http` — HTTP client
- `System.Threading.Tasks` — Async/await

## Strengths
- Modern language features (LINQ, async/await, pattern matching)
- Strong type system with inference
- Excellent tooling (Visual Studio, Rider, VS Code)
- Cross-platform with .NET Core/.NET 5+
- Rich standard library

## Weaknesses
- Primarily tied to the .NET ecosystem
- Garbage collection can cause latency spikes
- Verbose compared to some modern languages
