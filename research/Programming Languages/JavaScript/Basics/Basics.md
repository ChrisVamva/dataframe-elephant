# JavaScript Basics

## Overview
JavaScript is a high-level, dynamic, interpreted programming language originally created by Brendan Eich in 1995. It is the dominant language of web browsers and, with Node.js, has become a major server-side language as well.

## Key Characteristics
- **Paradigm**: Multi-paradigm (event-driven, functional, OOP, prototype-based)
- **Typing**: Dynamic, weak (with optional static typing via TypeScript)
- **Execution**: Interpreted (JIT-compiled in modern engines)
- **Memory Management**: Automatic garbage collection
- **Platform**: Web browsers, Node.js, Deno, Bun

## Syntax Fundamentals

### Hello World
```javascript
console.log("Hello, World!");
```

### Variables and Data Types
```javascript
// Variable declarations
let count = 42;              // Block-scoped, reassignable
const name = "Alice";        // Block-scoped, immutable binding
var oldStyle = "avoid";      // Function-scoped (legacy)

// Primitive types
let num = 42;                // Number (64-bit float)
let str = "Hello";           // String
let bool = true;             // Boolean
let nothing = null;          // Null
let undef = undefined;       // Undefined
let sym = Symbol("id");      // Symbol (unique identifier)
let big = 9007199254740991n; // BigInt

// Reference types
let obj = { name: "Alice", age: 30 };  // Object
let arr = [1, 2, 3, 4, 5];             // Array
let fn = function() {};                // Function
```

### Control Flow
```javascript
// If-else
if (x > 0) {
    console.log("positive");
} else if (x < 0) {
    console.log("negative");
} else {
    console.log("zero");
}

// For loop
for (let i = 0; i < 10; i++) {
    console.log(i);
}

// For-of (iterables)
for (const item of array) {
    console.log(item);
}

// For-in (object keys)
for (const key in object) {
    console.log(key, object[key]);
}

// While loop
while (count > 0) {
    count--;
}

// Do-while loop
do {
    count++;
} while (count < 10);

// Switch
switch (grade) {
    case "A":
        console.log("Excellent");
        break;
    case "B":
        console.log("Good");
        break;
    default:
        console.log("Other");
}

// Ternary operator
const result = x > 0 ? "positive" : "non-positive";
```

### Functions
```javascript
// Function declaration
function add(a, b) {
    return a + b;
}

// Function expression
const multiply = function(a, b) {
    return a * b;
};

// Arrow function
const square = (x) => x * x;

// Default parameters
function greet(name, greeting = "Hello") {
    return `${greeting}, ${name}!`;
}

// Rest parameters
function sum(...numbers) {
    return numbers.reduce((total, n) => total + n, 0);
}

// Destructuring
function process({ name, age }) {
    return `${name} is ${age}`;
}
```

### Objects
```javascript
// Object literal
const person = {
    name: "Alice",
    age: 30,
    greet() {
        return `Hello, I'm ${this.name}`;
    }
};

// Property access
console.log(person.name);
console.log(person["age"]);

// Destructuring
const { name, age } = person;

// Spread operator
const updated = { ...person, age: 31 };

// Object methods
Object.keys(person);
Object.values(person);
Object.entries(person);
```

### Arrays
```javascript
const numbers = [1, 2, 3, 4, 5];

// Map
const doubled = numbers.map(n => n * 2);

// Filter
const evens = numbers.filter(n => n % 2 === 0);

// Reduce
const sum = numbers.reduce((total, n) => total + n, 0);

// Find
const found = numbers.find(n => n > 3);

// Some/Every
const hasEven = numbers.some(n => n % 2 === 0);
const allPositive = numbers.every(n => n > 0);

// Sort
const sorted = [...numbers].sort((a, b) => a - b);
```

### Prototypes and Classes
```javascript
// Class syntax (ES6+)
class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }

    greet() {
        return `Hello, I'm ${this.name}`;
    }

    static species = "Homo sapiens";
}

// Inheritance
class Employee extends Person {
    constructor(name, age, company) {
        super(name, age);
        this.company = company;
    }

    greet() {
        return `${super.greet()} and I work at ${this.company}`;
    }
}
```

### Asynchronous Programming
```javascript
// Callbacks (legacy)
fetchData(function(err, data) {
    if (err) console.error(err);
    else console.log(data);
});

// Promises
fetchData()
    .then(data => processData(data))
    .then(result => saveResult(result))
    .catch(err => console.error(err));

// Async/await
async function main() {
    try {
        const data = await fetchData();
        const result = await processData(data);
        await saveResult(result);
    } catch (err) {
        console.error(err);
    }
}

// Promise.all
const [users, posts] = await Promise.all([
    fetchUsers(),
    fetchPosts()
]);
```

### Modules
```javascript
// ES6 Modules
// Export
export const PI = 3.14159;
export function add(a, b) { return a + b; }
export default class MyClass {}

// Import
import MyClass, { PI, add } from './module.js';
import * as utils from './module.js';
```

## Common APIs
- `console` — Logging and debugging
- `Math` — Mathematical functions
- `Date` — Date and time
- `JSON` — JSON parsing/stringifying
- `Array`, `Object`, `String`, `Number` — Built-in methods
- `Promise` — Asynchronous operations
- `fetch` — HTTP requests (browser/Node 18+)

## Strengths
- Universal web language
- Huge ecosystem (npm)
- Flexible and expressive
- Event-driven, non-blocking I/O
- Runs everywhere (browser, server, mobile, desktop)

## Weaknesses
- Weak typing leads to runtime errors
- `this` binding confusion
- Callback hell (mitigated by async/await)
- Inconsistent behavior across browsers (historically)
- Prototype-based OOP can be confusing
