# Java Basics

## Overview
Java is a class-based, object-oriented programming language developed by Sun Microsystems (now Oracle) in 1995. It is one of the most widely used programming languages, particularly for enterprise applications, Android development, and large-scale systems.

## Key Characteristics
- **Paradigm**: Object-oriented, class-based
- **Typing**: Static, strong, inferred (with `var` since Java 10)
- **Compilation**: Compiled to bytecode, runs on JVM
- **Memory Management**: Automatic garbage collection
- **Platform**: "Write once, run anywhere" (cross-platform via JVM)

## Syntax Fundamentals

### Hello World
```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

### Variables and Data Types
```java
// Primitive types
int count = 42;                  // 32-bit integer
long bigNum = 9_000_000_000L;    // 64-bit integer
double price = 19.99;            // 64-bit float
float rate = 3.14f;              // 32-bit float
char letter = 'A';               // 16-bit Unicode character
boolean isActive = true;         // Boolean
byte small = 127;                // 8-bit integer
short medium = 32_767;           // 16-bit integer

// Reference types
String name = "Alice";           // Immutable string
int[] numbers = {1, 2, 3};       // Array
var inferred = "hello";          // Type inference (Java 10+)

// Constants
final int MAX_SIZE = 100;
```

### Control Flow
```java
// If-else
if (x > 0) {
    System.out.println("positive");
} else if (x < 0) {
    System.out.println("negative");
} else {
    System.out.println("zero");
}

// For loop
for (int i = 0; i < 10; i++) {
    System.out.println(i);
}

// Enhanced for (for-each)
for (String item : collection) {
    System.out.println(item);
}

// While loop
while (count > 0) {
    count--;
}

// Do-while loop
do {
    count++;
} while (count < 10);

// Switch (Java 14+ with arrow syntax)
switch (grade) {
    case 'A' -> System.out.println("Excellent");
    case 'B' -> System.out.println("Good");
    default  -> System.out.println("Other");
}
```

### Classes and Objects
```java
public class Person {
    // Fields
    private String name;
    private int age;

    // Constructor
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Getters and setters
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public int getAge() { return age; }
    public void setAge(int age) { this.age = age; }

    // Method
    public String describe() {
        return name + " is " + age + " years old";
    }

    @Override
    public String toString() {
        return "Person{name='" + name + "', age=" + age + "}";
    }
}

Person person = new Person("Alice", 30);
System.out.println(person.describe());
```

### Inheritance and Polymorphism
```java
// Abstract class
public abstract class Shape {
    protected String color;

    public Shape(String color) {
        this.color = color;
    }

    public abstract double area();

    public String getColor() { return color; }
}

// Concrete subclass
public class Circle extends Shape {
    private double radius;

    public Circle(String color, double radius) {
        super(color);
        this.radius = radius;
    }

    @Override
    public double area() {
        return Math.PI * radius * radius;
    }
}

// Interface
public interface Drawable {
    void draw();
    default void print() {
        System.out.println("Printing...");
    }
}
```

### Collections Framework
```java
import java.util.*;

// List (ordered, allows duplicates)
List<String> names = new ArrayList<>();
names.add("Alice");
names.add("Bob");

// Set (no duplicates)
Set<Integer> unique = new HashSet<>(Arrays.asList(1, 2, 3, 2, 1));

// Map (key-value pairs)
Map<String, Integer> ages = new HashMap<>();
ages.put("Alice", 30);
ages.put("Bob", 25);

// Queue
Queue<String> queue = new LinkedList<>();
queue.offer("first");
queue.poll();

// Iteration
for (String name : names) {
    System.out.println(name);
}

names.forEach(System.out::println);
```

### Exception Handling
```java
try {
    int result = 10 / 0;
} catch (ArithmeticException e) {
    System.err.println("Math error: " + e.getMessage());
} catch (Exception e) {
    System.err.println("Error: " + e.getMessage());
} finally {
    System.out.println("Always executed");
}

// Try-with-resources
try (BufferedReader reader = new BufferedReader(new FileReader("file.txt"))) {
    String line = reader.readLine();
} catch (IOException e) {
    e.printStackTrace();
}
```

### Generics
```java
public class Box<T> {
    private T content;

    public void set(T content) { this.content = content; }
    public T get() { return content; }
}

Box<String> stringBox = new Box<>();
stringBox.set("Hello");
String value = stringBox.get();

// Bounded type parameter
public <T extends Comparable<T>> T max(T a, T b) {
    return a.compareTo(b) > 0 ? a : b;
}
```

### Lambdas and Streams (Java 8+)
```java
// Lambda expression
List<String> names = Arrays.asList("Alice", "Bob", "Charlie");

names.stream()
    .filter(n -> n.length() > 3)
    .map(String::toUpperCase)
    .sorted()
    .forEach(System.out::println);

// Collectors
List<String> filtered = names.stream()
    .filter(n -> n.startsWith("A"))
    .collect(Collectors.toList());

Map<String, Integer> nameLengths = names.stream()
    .collect(Collectors.toMap(n -> n, String::length));
```

## Common Packages
- `java.lang` — Core classes (String, Math, Object)
- `java.util` — Collections, date/time, utilities
- `java.io` — Input/output streams
- `java.nio` — Non-blocking I/O
- `java.net` — Networking
- `java.sql` — Database connectivity

## Strengths
- Platform independence (JVM)
- Massive ecosystem and libraries
- Strong enterprise support
- Excellent tooling (IntelliJ, Eclipse, Maven, Gradle)
- Mature and stable

## Weaknesses
- Verbose syntax
- Slower than native compiled languages
- Memory consumption (JVM overhead)
- Boilerplate code
- Slower evolution compared to newer languages
