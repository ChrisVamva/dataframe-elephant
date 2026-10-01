# TypeScript Basics

## Overview
TypeScript is a strongly typed, compiled programming language that builds on JavaScript by adding static type definitions. Developed by Microsoft in 2012, it is a superset of JavaScript that compiles to plain JavaScript, enabling better tooling, error detection, and code maintainability.

## Key Characteristics
- **Paradigm**: Multi-paradigm (OOP, functional, imperative)
- **Typing**: Static, strong, inferred (gradual typing)
- **Compilation**: Transpiled to JavaScript
- **Memory Management**: Automatic garbage collection (via JS engine)
- **Platform**: Anywhere JavaScript runs (browser, Node.js, Deno, Bun)

## Syntax Fundamentals

### Hello World
```typescript
const message: string = "Hello, World!";
console.log(message);
```

### Variables and Data Types
```typescript
// Variable declarations
let count: number = 42;          // Mutable
const name: string = "Alice";    // Immutable

// Primitive types
let num: number = 42;            // Number (64-bit float)
let str: string = "Hello";       // String
let bool: boolean = true;        // Boolean
let nothing: null = null;        // Null
let undef: undefined = undefined; // Undefined
let sym: symbol = Symbol("id");  // Symbol
let big: bigint = 9007199254740991n; // BigInt

// Type inference (no annotation needed)
let inferred = "hello";  // Compiler infers string
let count2 = 0;          // Compiler infers number

// Any (opt-out of type checking)
let anything: any = "flexible";

// Unknown (safer any)
let uncertain: unknown = "mysterious";

// Void (no return value)
function logMessage(): void {
    console.log("Hello");
}

// Never (never returns)
function throwError(message: string): never {
    throw new Error(message);
}
```

### Arrays and Tuples
```typescript
// Array
let numbers: number[] = [1, 2, 3, 4, 5];
let names: Array<string> = ["Alice", "Bob"];

// Tuple (fixed length, known types)
let person: [string, number] = ["Alice", 30];
let rgb: [number, number, number] = [255, 128, 0];

// Tuple with optional elements
let optional: [string, number?] = ["Alice"];

// Named tuples
let point: [x: number, y: number] = [3, 7];
```

### Control Flow
```typescript
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
```typescript
// Function declaration
function add(a: number, b: number): number {
    return a + b;
}

// Arrow function
const multiply = (a: number, b: number): number => a * b;

// Default parameters
function greet(name: string, greeting: string = "Hello"): string {
    return `${greeting}, ${name}!`;
}

// Rest parameters
function sum(...numbers: number[]): number {
    return numbers.reduce((total, n) => total + n, 0);
}

// Optional parameters
function createUser(name: string, age?: number): object {
    return { name, age };
}

// Function overloads
function format(value: string): string;
function format(value: number): string;
function format(value: string | number): string {
    return value.toString();
}

// Callback function
function processData(data: string[], callback: (item: string) => void): void {
    data.forEach(callback);
}
```

### Interfaces
```typescript
// Interface definition
interface User {
    id: number;
    name: string;
    email: string;
    age?: number;           // Optional property
    readonly createdAt: Date; // Read-only property
}

// Using interface
const user: User = {
    id: 1,
    name: "Alice",
    email: "alice@example.com",
    createdAt: new Date()
};

// Interface with methods
interface Drawable {
    color: string;
    draw(): void;
    resize(factor: number): void;
}

// Interface extending
interface Admin extends User {
    permissions: string[];
    banUser(userId: number): void;
}

// Interface for function types
interface MathOperation {
    (a: number, b: number): number;
}

const add: MathOperation = (a, b) => a + b;
```

### Type Aliases
```typescript
// Type alias
type ID = string | number;
type Point = { x: number; y: number };
type Status = "pending" | "active" | "completed";

// Union types
let value: string | number;
value = "hello";
value = 42;

// Intersection types
type Named = { name: string };
type Aged = { age: number };
type Person = Named & Aged;

const person: Person = { name: "Alice", age: 30 };

// Literal types
type Direction = "north" | "south" | "east" | "west";
let dir: Direction = "north";

// Type guards
function isString(value: unknown): value is string {
    return typeof value === "string";
}
```

### Classes
```typescript
// Class definition
class Person {
    // Properties
    private id: number;
    public name: string;
    protected age: number;

    // Static property
    static species: string = "Homo sapiens";

    // Constructor
    constructor(id: number, name: string, age: number) {
        this.id = id;
        this.name = name;
        this.age = age;
    }

    // Method
    describe(): string {
        return `${this.name} is ${this.age} years old`;
    }

    // Getter
    get info(): string {
        return `ID: ${this.id}, Name: ${this.name}`;
    }

    // Setter
    set updateAge(value: number) {
        if (value > 0) {
            this.age = value;
        }
    }

    // Static method
    static create(name: string, age: number): Person {
        return new Person(Date.now(), name, age);
    }
}

// Inheritance
class Employee extends Person {
    private company: string;

    constructor(id: number, name: string, age: number, company: string) {
        super(id, name, age);
        this.company = company;
    }

    describe(): string {
        return `${super.describe()} and works at ${this.company}`;
    }
}

// Abstract class
abstract class Shape {
    abstract area(): number;
    abstract perimeter(): number;

    describe(): string {
        return `Area: ${this.area()}, Perimeter: ${this.perimeter()}`;
    }
}

class Circle extends Shape {
    constructor(private radius: number) {
        super();
    }

    area(): number {
        return Math.PI * this.radius ** 2;
    }

    perimeter(): number {
        return 2 * Math.PI * this.radius;
    }
}

// Access modifiers: public, private, protected
// public: accessible everywhere (default)
// private: accessible only within the class
// protected: accessible within class and subclasses
```

### Generics
```typescript
// Generic function
function identity<T>(value: T): T {
    return value;
}

const num = identity<number>(42);
const str = identity("hello");  // Type inferred

// Generic interface
interface Container<T> {
    value: T;
    getValue(): T;
}

class Box<T> implements Container<T> {
    constructor(public value: T) {}
    getValue(): T {
        return this.value;
    }
}

const box = new Box<string>("hello");

// Generic class
class Stack<T> {
    private items: T[] = [];

    push(item: T): void {
        this.items.push(item);
    }

    pop(): T | undefined {
        return this.items.pop();
    }

    peek(): T | undefined {
        return this.items[this.items.length - 1];
    }
}

const stack = new Stack<number>();
stack.push(1);
stack.push(2);

// Generic constraints
interface HasLength {
    length: number;
}

function logLength<T extends HasLength>(item: T): void {
    console.log(item.length);
}

logLength("hello");     // OK
logLength([1, 2, 3]);   // OK
// logLength(42);       // Error: number has no length

// Multiple generics
function pair<K, V>(key: K, value: V): [K, V] {
    return [key, value];
}

const entry = pair("name", "Alice");
```

### Enums
```typescript
// Numeric enum
enum Direction {
    Up,      // 0
    Down,    // 1
    Left,    // 2
    Right    // 3
}

// String enum
enum Status {
    Pending = "PENDING",
    Active = "ACTIVE",
    Completed = "COMPLETED"
}

// Const enum (inlined at compile time)
const enum Colors {
    Red = "#FF0000",
    Green = "#00FF00",
    Blue = "#0000FF"
}

let dir: Direction = Direction.Up;
let status: Status = Status.Active;
```

### Modules
```typescript
// Export
export const PI = 3.14159;
export function add(a: number, b: number): number {
    return a + b;
}
export class Calculator {
    multiply(a: number, b: number): number {
        return a * b;
    }
}
export default class App {
    // ...
}

// Import
import App, { PI, add, Calculator } from './app';
import * as utils from './utils';
import { add as sum } from './math';
```

### Utility Types
```typescript
// Partial - all properties optional
interface User {
    name: string;
    age: number;
    email: string;
}
type PartialUser = Partial<User>;

// Required - all properties required
type RequiredUser = Required<PartialUser>;

// Readonly - all properties read-only
type ReadonlyUser = Readonly<User>;

// Pick - select specific properties
type UserPreview = Pick<User, "name" | "email">;

// Omit - exclude specific properties
type UserWithoutAge = Omit<User, "age">;

// Record - create object type
type PageInfo = Record<string, { title: string; url: string }>;

// ReturnType - get return type of function
type AddResult = ReturnType<typeof add>;

// Parameters - get parameter types of function
type AddParams = Parameters<typeof add>;

// NonNullable - exclude null and undefined
type NonNull = NonNullable<string | null | undefined>;
```

### Decorators
```typescript
// Class decorator
function Component(target: Function) {
    target.prototype.render = function() {
        console.log("Rendering...");
    };
}

@Component
class MyComponent {
    // ...
}

// Method decorator
function Log(target: any, propertyKey: string, descriptor: PropertyDescriptor) {
    const original = descriptor.value;
    descriptor.value = function(...args: any[]) {
        console.log(`Calling ${propertyKey} with`, args);
        return original.apply(this, args);
    };
}

class Calculator {
    @Log
    add(a: number, b: number): number {
        return a + b;
    }
}

// Property decorator
function Required(target: any, propertyKey: string) {
    // Validation logic
}

class User {
    @Required
    name: string;
}
```

### Async/Await
```typescript
// Promise
function fetchData(): Promise<string> {
    return new Promise((resolve, reject) => {
        setTimeout(() => resolve("data"), 1000);
    });
}

// Async/await
async function main(): Promise<void> {
    try {
        const data = await fetchData();
        console.log(data);
    } catch (error) {
        console.error(error);
    }
}

// Promise.all
async function fetchAll(): Promise<void> {
    const [users, posts] = await Promise.all([
        fetchUsers(),
        fetchPosts()
    ]);
}

// Promise.race
async function fetchFastest(): Promise<void> {
    const result = await Promise.race([
        fetchFromServer1(),
        fetchFromServer2()
    ]);
}
```

## Common Libraries
- `react` — UI library
- `express` — Web framework
- `lodash` — Utility functions
- `axios` — HTTP client
- `zod` — Schema validation
- `prisma` — Database ORM

## Strengths
- Static typing catches errors at compile time
- Excellent IDE support (autocomplete, refactoring)
- Full JavaScript compatibility
- Gradual adoption (can add types incrementally)
- Large ecosystem and community
- Better code documentation and maintainability

## Weaknesses
- Compilation step required
- Type definitions can be complex
- Learning curve for advanced types
- Some JavaScript patterns are hard to type
- Build tooling overhead
- Can be over-engineered for simple projects
