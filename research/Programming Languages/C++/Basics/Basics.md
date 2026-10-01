# C++ Basics

## Overview
C++ is a general-purpose, high-performance programming language created by Bjarne Stroustrup in 1985 as an extension of C. It adds object-oriented, generic, and functional features while maintaining low-level hardware access.

## Key Characteristics
- **Paradigm**: Multi-paradigm (procedural, OOP, generic, functional)
- **Typing**: Static, strong, inferred (with `auto`)
- **Compilation**: Compiled to native machine code
- **Memory Management**: Manual + smart pointers + RAII
- **Standard**: ISO/IEC 14882 (C++11, C++14, C++17, C++20, C++23)

## Syntax Fundamentals

### Hello World
```cpp
#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
```

### Variables and Data Types
```cpp
int count = 42;                  // Integer
double pi = 3.14159;             // Double-precision float
char letter = 'A';               // Character
bool flag = true;                // Boolean
std::string name = "Alice";      // String (STL)
auto inferred = 3.14;            // Type deduction
int *ptr = &count;               // Raw pointer
```

### Control Flow
```cpp
// If-else
if (x > 0) {
    std::cout << "positive\n";
} else if (x < 0) {
    std::cout << "negative\n";
} else {
    std::cout << "zero\n";
}

// For loop
for (int i = 0; i < 10; i++) {
    std::cout << i << "\n";
}

// Range-based for (C++11)
for (const auto& item : collection) {
    std::cout << item << "\n";
}

// While loop
while (count > 0) {
    count--;
}
```

### Functions
```cpp
int add(int a, int b) {
    return a + b;
}

// Function overloading
double add(double a, double b) {
    return a + b;
}

// Lambda (C++11)
auto square = [](int x) { return x * x; };
```

### Classes and OOP
```cpp
class Rectangle {
private:
    double width_;
    double height_;

public:
    Rectangle(double w, double h) : width_(w), height_(h) {}

    double area() const {
        return width_ * height_;
    }

    // Operator overloading
    bool operator<(const Rectangle& other) const {
        return area() < other.area();
    }
};
```

### Templates (Generic Programming)
```cpp
template <typename T>
T maximum(T a, T b) {
    return (a > b) ? a : b;
}

auto maxInt = maximum(3, 7);
auto maxDouble = maximum(3.14, 2.71);
```

### Smart Pointers (Modern C++)
```cpp
#include <memory>

auto ptr = std::make_unique<int>(42);     // Unique ownership
auto shared = std::make_shared<int>(100); // Shared ownership
std::weak_ptr<int> weak = shared;          // Non-owning observer
```

### STL Containers
```cpp
#include <vector>
#include <map>
#include <set>
#include <algorithm>

std::vector<int> vec = {3, 1, 4, 1, 5};
std::map<std::string, int> ages = {{"Alice", 30}, {"Bob", 25}};
std::set<int> unique = {1, 2, 3, 2, 1};

std::sort(vec.begin(), vec.end());
auto it = std::find(vec.begin(), vec.end(), 4);
```

## Common Headers
- `<iostream>` — Console I/O
- `<vector>` — Dynamic array
- `<string>` — String class
- `<map>` / `<unordered_map>` — Key-value containers
- `<algorithm>` — Sorting, searching, transformations
- `<memory>` — Smart pointers
- `<thread>` — Concurrency

## Strengths
- Zero-cost abstractions
- Fine-grained control over memory and hardware
- High performance (used in games, HPC, embedded)
- Backward compatibility with C
- Massive ecosystem and legacy codebase

## Weaknesses
- Steep learning curve
- Complex syntax and semantics
- Manual memory management risks (mitigated by smart pointers)
- Long compile times
- Header/source file separation complexity
