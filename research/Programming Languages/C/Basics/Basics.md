# C Basics

## Overview
C is a general-purpose, procedural programming language developed by Dennis Ritchie at Bell Labs in 1972. It is one of the most widely used languages and forms the foundation for many modern languages.

## Key Characteristics
- **Paradigm**: Procedural, structured
- **Typing**: Static, weak
- **Compilation**: Compiled to native machine code
- **Memory Management**: Manual (malloc/free)
- **Portability**: Highly portable across platforms

## Syntax Fundamentals

### Hello World
```c
#include <stdio.h>

int main(void) {
    printf("Hello, World!\n");
    return 0;
}
```

### Variables and Data Types
```c
int count = 42;              // Integer
float pi = 3.14159f;         // Single-precision float
double e = 2.718281828;      // Double-precision float
char letter = 'A';           // Single character
char name[] = "Alice";       // String (char array)
int *ptr = &count;           // Pointer
```

### Control Flow
```c
// If-else
if (x > 0) {
    printf("positive\n");
} else if (x < 0) {
    printf("negative\n");
} else {
    printf("zero\n");
}

// For loop
for (int i = 0; i < 10; i++) {
    printf("%d\n", i);
}

// While loop
while (count > 0) {
    count--;
}

// Switch
switch (grade) {
    case 'A': printf("Excellent\n"); break;
    case 'B': printf("Good\n"); break;
    default:  printf("Other\n"); break;
}
```

### Functions
```c
int add(int a, int b) {
    return a + b;
}

void greet(const char *name) {
    printf("Hello, %s!\n", name);
}
```

### Pointers and Memory
```c
int x = 10;
int *p = &x;       // p holds address of x
*p = 20;           // dereference: x is now 20

int *arr = malloc(5 * sizeof(int));  // dynamic allocation
free(arr);                            // release memory
```

### Structures
```c
struct Point {
    int x;
    int y;
};

struct Point p1 = {3, 7};
printf("x=%d, y=%d\n", p1.x, p1.y);
```

## Common Libraries
- `stdio.h` — Input/output (printf, scanf, fopen)
- `stdlib.h` — General utilities (malloc, exit, atoi)
- `string.h` — String manipulation (strcpy, strlen, strcmp)
- `math.h` — Mathematical functions (sin, cos, sqrt)
- `time.h` — Date and time utilities

## Strengths
- Direct hardware access and low-level control
- Extremely fast and efficient
- Small runtime footprint
- Universal portability

## Weaknesses
- No built-in memory safety (buffer overflows, dangling pointers)
- No object-oriented features
- Manual memory management is error-prone
- Minimal standard library compared to modern languages
