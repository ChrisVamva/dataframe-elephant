# Dart Basics

## Overview
Dart is a client-optimized programming language developed by Google in 2011. It is the primary language for Flutter, Google's UI framework for building cross-platform applications from a single codebase.

## Key Characteristics
- **Paradigm**: Object-oriented, functional
- **Typing**: Static, strong, inferred
- **Compilation**: JIT (development) + AOT (production)
- **Memory Management**: Automatic garbage collection
- **Platform**: Web, mobile (iOS/Android), desktop, server

## Syntax Fundamentals

### Hello World
```dart
void main() {
  print('Hello, World!');
}
```

### Variables and Data Types
```dart
int count = 42;              // Integer
double pi = 3.14159;         // Double-precision float
String name = 'Alice';       // String
bool isActive = true;        // Boolean
var inferred = 'hello';      // Type inference
final immutable = 'fixed';   // Runtime constant
const compileTime = 42;      // Compile-time constant
dynamic anything = 'flexible'; // Dynamic type
```

### Control Flow
```dart
// If-else
if (x > 0) {
  print('positive');
} else if (x < 0) {
  print('negative');
} else {
  print('zero');
}

// For loop
for (var i = 0; i < 10; i++) {
  print(i);
}

// For-in loop
for (var item in collection) {
  print(item);
}

// While loop
while (count > 0) {
  count--;
}

// Switch
switch (grade) {
  case 'A':
    print('Excellent');
    break;
  case 'B':
    print('Good');
    break;
  default:
    print('Other');
}
```

### Functions
```dart
int add(int a, int b) {
  return a + b;
}

// Arrow function
int square(int x) => x * x;

// Optional parameters
void greet(String name, [String greeting = 'Hello']) {
  print('$greeting, $name!');
}

// Named parameters
void createUser({required String name, int age = 0}) {
  print('$name, $age');
}
```

### Classes and OOP
```dart
class Person {
  String name;
  int age;

  // Constructor with initializer list
  Person(this.name, this.age);

  // Named constructor
  Person.anonymous() : name = 'Anonymous', age = 0;

  // Method
  String describe() => '$name is $age years old';

  // Getter
  bool get isAdult => age >= 18;
}

// Inheritance
class Employee extends Person {
  String company;

  Employee(String name, int age, this.company) : super(name, age);
}
```

### Null Safety
```dart
String? nullableName;           // Can be null
String nonNull = 'definite';    // Cannot be null

// Null-aware operators
String result = nullableName ?? 'default';
nullableName?.toUpperCase();    // Safe call
nullableName!;                  // Force unwrap (risky)
```

### Collections
```dart
var list = [1, 2, 3, 4, 5];              // List
var set = {1, 2, 3};                     // Set (unique elements)
var map = {'name': 'Alice', 'age': 30};  // Map

// Collection literals with control flow
var evens = [for (var i = 0; i < 10; i += 2) i];
var names = [for (var p in people) if (p.isActive) p.name];
```

### Async/Await
```dart
Future<String> fetchData() async {
  var response = await http.get(Uri.parse('https://api.example.com/data'));
  return response.body;
}

// Stream
Stream<int> countStream(int max) async* {
  for (var i = 0; i <= max; i++) {
    yield i;
  }
}
```

## Common Libraries
- `dart:core` — Built-in types, collections
- `dart:async` — Futures, Streams
- `dart:io` — File and network I/O
- `dart:convert` — JSON encoding/decoding
- `dart:math` — Mathematical functions

## Strengths
- Excellent for UI development with Flutter
- Strong type system with null safety
- Good balance of productivity and performance
- Single codebase for multiple platforms
- Hot reload for fast development

## Weaknesses
- Smaller ecosystem compared to JS/Python
- Primarily tied to Flutter for mobile
- Less mature server-side ecosystem
- Limited use outside of Google's ecosystem
