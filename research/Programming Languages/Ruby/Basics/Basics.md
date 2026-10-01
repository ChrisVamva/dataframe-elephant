# Ruby Basics

## Overview
Ruby is a dynamic, interpreted, object-oriented programming language created by Yukihiro "Matz" Matsumoto in 1995. It was designed with a focus on programmer happiness and productivity, emphasizing simplicity and elegance. Ruby gained widespread popularity through the Ruby on Rails web framework.

## Key Characteristics
- **Paradigm**: Object-oriented, functional, imperative
- **Typing**: Dynamic, strong, duck typing
- **Execution**: Interpreted (MRI/YARV), with JIT in Ruby 3+
- **Memory Management**: Automatic garbage collection
- **Philosophy**: "Optimized for programmer happiness"

## Syntax Fundamentals

### Hello World
```ruby
puts "Hello, World!"
```

### Variables and Data Types
```ruby
# Local variable
count = 42              # Integer
price = 19.99           # Float
name = "Alice"          # String
is_active = true        # Boolean
nothing = nil           # Nil (null equivalent)

# Instance variable
@name = "Alice"

# Class variable
@@count = 0

# Global variable
$app_name = "MyApp"

# Constant (convention: uppercase)
MAX_SIZE = 100

# Symbol (immutable identifier)
status = :active
```

### Control Flow
```ruby
# If-elsif-else
if x > 0
  puts "positive"
elsif x < 0
  puts "negative"
else
  puts "zero"
end

# Unless (inverse if)
unless x > 0
  puts "non-positive"
end

# Ternary operator
result = x > 0 ? "positive" : "non-positive"

# Case-when (switch)
case grade
when "A"
  puts "Excellent"
when "B"
  puts "Good"
when "C".."D"
  puts "Passing"
else
  puts "Other"
end

# For loop (rarely used in Ruby)
for i in 0...10
  puts i
end

# Times iterator
10.times do |i|
  puts i
end

# Each iterator
[1, 2, 3].each do |item|
  puts item
end

# While loop
while count > 0
  count -= 1
end

# Until loop
until count >= 10
  count += 1
end
```

### Methods
```ruby
# Method definition
def add(a, b)
  a + b  # Last expression is returned implicitly
end

# Default parameters
def greet(name, greeting = "Hello")
  "#{greeting}, #{name}!"
end

# Keyword arguments (Ruby 2.0+)
def create_user(name:, email:, age: 0)
  "#{name} (#{email}), age: #{age}"
end

create_user(name: "Alice", email: "alice@example.com")

# Splat operator
def sum(*numbers)
  numbers.reduce(0, :+)
end

# Double splat (keyword arguments)
def configure(options = {})
  puts options
end

configure(name: "App", version: "1.0")

# Block, Proc, Lambda
def with_timing
  start = Time.now
  yield
  puts "Took #{Time.now - start} seconds"
end

with_timing { do_something }
```

### Data Structures
```ruby
# Array
fruits = ["apple", "banana", "cherry"]
fruits << "date"           # Append
fruits.push("elderberry")  # Append
fruits.pop                 # Remove last
fruits.shift               # Remove first
fruits[0]                  # Access (0-indexed)
fruits.first               # First element
fruits.last                # Last element
fruits.length              # Length

# Array methods
fruits.map { |f| f.upcase }
fruits.select { |f| f.length > 5 }
fruits.reject { |f| f.start_with?("a") }
fruits.sort
fruits.uniq

# Hash (dictionary)
person = {
  "name" => "Alice",
  "age" => 30
}

# Symbol keys (preferred)
person = {
  name: "Alice",
  age: 30
}

person[:name]              # Access
person[:email] = "alice@example.com"  # Add/modify
person.keys                # All keys
person.values              # All values

# Hash methods
person.each { |key, value| puts "#{key}: #{value}" }
person.map { |k, v| [k, v.to_s] }.to_h
```

### Classes and OOP
```ruby
class Person
  # Attribute accessor
  attr_accessor :name, :age
  attr_reader :id

  # Class variable
  @@count = 0

  # Constructor
  def initialize(name, age)
    @name = name
    @age = age
    @id = object_id
    @@count += 1
  end

  # Instance method
  def describe
    "#{@name} is #{@age} years old"
  end

  # Class method
  def self.count
    @@count
  end

  # Operator overloading
  def +(other)
    Person.new("#{@name} & #{other.name}", 0)
  end

  # To string
  def to_s
    describe
  end

  # Comparison
  def <=>(other)
    @age <=> other.age
  end

  # Include Comparable for <, >, ==, etc.
  include Comparable
end

# Inheritance
class Employee < Person
  attr_accessor :company

  def initialize(name, age, company)
    super(name, age)
    @company = company
  end

  def describe
    "#{super} and works at #{@company}"
  end
end

# Module (mixin)
module Greetable
  def greet
    "Hello, I'm #{@name}"
  end
end

class Customer < Person
  include Greetable
end
```

### Blocks, Procs, and Lambdas
```ruby
# Block (not an object)
[1, 2, 3].each { |n| puts n }
[1, 2, 3].each do |n|
  puts n
end

# Proc (object)
my_proc = Proc.new { |n| puts n }
my_proc.call(5)

# Lambda (strict arity)
my_lambda = ->(n) { puts n }
my_lambda.call(5)

# Method as object
method_obj = method(:puts)
method_obj.call("Hello")

# Yield in methods
def with_block
  puts "Before"
  yield
  puts "After"
end

with_block { puts "Inside block" }

# Block given?
def maybe_block
  if block_given?
    yield
  else
    puts "No block"
  end
end
```

### Metaprogramming
```ruby
# Define method dynamically
class MyClass
  define_method(:dynamic_method) do |arg|
    "Called with #{arg}"
  end
end

# Method missing
class Flexible
  def method_missing(method_name, *args, &block)
    if method_name.to_s.start_with?("find_by_")
      "Finding by #{method_name.to_s.sub('find_by_', '')}"
    else
      super
    end
  end
end

# Open classes (monkey patching)
class String
  def shout
    upcase + "!"
  end
end

"hello".shout  # "HELLO!"
```

### Error Handling
```ruby
# Begin-rescue-ensure
begin
  result = 10 / 0
rescue ZeroDivisionError => e
  puts "Error: #{e.message}"
rescue StandardError => e
  puts "General error: #{e.message}"
else
  puts "Success: #{result}"
ensure
  puts "Always executed"
end

# Custom error
class ValidationError < StandardError
  attr_reader :field

  def initialize(field, message)
    @field = field
    super(message)
  end
end

# Raise
raise ValidationError.new("email", "Invalid email format")

# Retry
begin
  risky_operation
rescue
  retry if attempts < 3
end
```

## Common Libraries
- `sinatra` — Lightweight web framework
- `rails` — Full-stack web framework
- `rake` — Build tool
- `rspec` — Testing framework
- `json` — JSON handling
- `net/http` — HTTP client
- `date` — Date and time

## Strengths
- Elegant, readable syntax
- Pure OOP (everything is an object)
- Excellent metaprogramming capabilities
- Strong web development ecosystem (Rails)
- Very productive for rapid development

## Weaknesses
- Slower than compiled languages
- Dynamic typing can lead to runtime errors
- Smaller ecosystem than Python/JS
- Declining popularity compared to newer languages
- Concurrency limitations (GIL in MRI)
