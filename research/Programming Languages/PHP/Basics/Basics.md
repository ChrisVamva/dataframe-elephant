# PHP Basics

## Overview
PHP (PHP: Hypertext Preprocessor) is a widely-used, open-source scripting language designed for web development. Created by Rasmus Lerdorf in 1994, it powers a significant portion of the web, including WordPress, Facebook (historically), and many CMS platforms.

## Key Characteristics
- **Paradigm**: Imperative, object-oriented, functional
- **Typing**: Dynamic, weak (with optional type hints since PHP 7)
- **Execution**: Interpreted (with OPcache for performance)
- **Memory Management**: Automatic garbage collection
- **Platform**: Web server (Apache, Nginx), CLI

## Syntax Fundamentals

### Hello World
```php
<?php
echo "Hello, World!";
```

### Variables and Data Types
```php
$count = 42;              // Integer
$price = 19.99;           // Float
$name = "Alice";          // String
$isActive = true;         // Boolean
$nothing = null;          // Null

// Arrays (ordered maps)
$list = [1, 2, 3, 4, 5];           // Indexed array
$dict = ["name" => "Alice", "age" => 30];  // Associative array

// Type declarations (PHP 7+)
function add(int $a, int $b): int {
    return $a + $b;
}
```

### Control Flow
```php
// If-else
if ($x > 0) {
    echo "positive";
} elseif ($x < 0) {
    echo "negative";
} else {
    echo "zero";
}

// Alternative syntax (for templates)
if ($x > 0):
    echo "positive";
else:
    echo "non-positive";
endif;

// For loop
for ($i = 0; $i < 10; $i++) {
    echo $i;
}

// Foreach
foreach ($list as $item) {
    echo $item;
}

foreach ($dict as $key => $value) {
    echo "$key: $value";
}

// While loop
while ($count > 0) {
    $count--;
}

// Do-while
do {
    $count++;
} while ($count < 10);

// Switch
switch ($grade) {
    case 'A':
        echo "Excellent";
        break;
    case 'B':
        echo "Good";
        break;
    default:
        echo "Other";
}

// Match expression (PHP 8+)
$result = match($grade) {
    'A' => "Excellent",
    'B' => "Good",
    default => "Other",
};
```

### Functions
```php
// Function definition
function add($a, $b) {
    return $a + $b;
}

// Type-hinted function
function greet(string $name, string $greeting = "Hello"): string {
    return "$greeting, $name!";
}

// Anonymous function
$multiply = function($a, $b) {
    return $a * $b;
};

// Arrow function (PHP 7.4+)
$square = fn($x) => $x * $x;

// Variadic function
function sum(...$numbers): float {
    return array_sum($numbers);
}

// Named arguments (PHP 8+)
greet(name: "Alice", greeting: "Hi");
```

### Arrays
```php
$fruits = ["apple", "banana", "cherry"];

// Access
echo $fruits[0];  // "apple"

// Add
$fruits[] = "date";
array_push($fruits, "elderberry");

// Remove
array_pop($fruits);
array_shift($fruits);

// Search
$index = array_search("banana", $fruits);
$exists = in_array("apple", $fruits);

// Map
$upper = array_map('strtoupper', $fruits);

// Filter
$long = array_filter($fruits, fn($f) => strlen($f) > 5);

// Reduce
$total = array_reduce($numbers, fn($carry, $n) => $carry + $n, 0);

// Sort
sort($fruits);           // Sort by value
asort($dict);            // Sort by value, maintain keys
ksort($dict);            // Sort by key
```

### Classes and OOP
```php
class Person {
    // Properties
    public string $name;
    protected int $age;
    private static int $count = 0;

    // Constructor
    public function __construct(string $name, int $age) {
        $this->name = $name;
        $this->age = $age;
        self::$count++;
    }

    // Method
    public function describe(): string {
        return "{$this->name} is {$this->age} years old";
    }

    // Static method
    public static function getCount(): int {
        return self::$count;
    }

    // Magic method
    public function __toString(): string {
        return $this->describe();
    }
}

// Inheritance
class Employee extends Person {
    public string $company;

    public function __construct(string $name, int $age, string $company) {
        parent::__construct($name, $age);
        $this->company = $company;
    }

    public function describe(): string {
        return parent::describe() . " and works at {$this->company}";
    }
}

// Interface
interface Logger {
    public function log(string $message): void;
}

// Abstract class
abstract class Shape {
    abstract public function area(): float;

    public function describe(): string {
        return "Area: " . $this->area();
    }
}
```

### String Handling
```php
$name = "Alice";
$age = 30;

// Interpolation
echo "Hello, $name!";
echo "Hello, {$name}!";

// Concatenation
$greeting = "Hello, " . $name . "!";

// Common functions
strlen($name);           // Length
strtoupper($name);       // Uppercase
strtolower($name);       // Lowercase
substr($name, 0, 3);     // Substring
strpos($name, "lic");    // Find position
str_replace("A", "a", $name);  // Replace
explode(",", "a,b,c");   // Split to array
implode(", ", $array);    // Join to string
trim("  hello  ");       // Trim whitespace
sprintf("%s is %d", $name, $age);  // Format
```

### File I/O
```php
// Read file
$content = file_get_contents("file.txt");

// Write file
file_put_contents("file.txt", "Hello, World!");

// Read lines
$lines = file("file.txt");

// File handling
$handle = fopen("file.txt", "r");
while (($line = fgets($handle)) !== false) {
    echo $line;
}
fclose($handle);
```

### Error Handling
```php
// Try-catch
try {
    $result = 10 / 0;
} catch (DivisionByZeroError $e) {
    echo "Error: " . $e->getMessage();
} catch (Exception $e) {
    echo "General error: " . $e->getMessage();
} finally {
    echo "Always executed";
}

// Custom exception
class ValidationException extends Exception {}

// Throw
throw new ValidationException("Invalid input");
```

## Common Extensions
- `mysqli` / `PDO` — Database access
- `json` — JSON encoding/decoding
- `curl` — HTTP requests
- `mbstring` — Multibyte string handling
- `openssl` — Cryptography
- `gd` / `imagick` — Image processing

## Strengths
- Purpose-built for web development
- Huge ecosystem (WordPress, Laravel, Symfony)
- Easy deployment (shared hosting)
- Large community and documentation
- Modern versions (PHP 8+) are fast and feature-rich

## Weaknesses
- Inconsistent function naming and parameter order
- Historical security issues
- Weak typing can lead to bugs
- Reputation from legacy code
- Not ideal for non-web applications
