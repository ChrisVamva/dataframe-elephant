# Lua Basics

## Overview
Lua is a lightweight, high-level, multi-paradigm scripting language developed in 1993 at PUC-Rio, Brazil. It is designed for embedded use in applications and is widely used in game development (World of Warcraft, Roblox), embedded systems, and as a configuration language.

## Key Characteristics
- **Paradigm**: Multi-paradigm (procedural, OOP via tables, functional)
- **Typing**: Dynamic, weak
- **Execution**: Interpreted (with optional JIT via LuaJIT)
- **Memory Management**: Automatic garbage collection
- **Size**: Extremely small footprint (~200KB)

## Syntax Fundamentals

### Hello World
```lua
print("Hello, World!")
```

### Variables and Data Types
```lua
-- Global variable
count = 42

-- Local variable (preferred)
local name = "Alice"

-- Types
local num = 42              -- Number (double-precision float)
local str = "Hello"         -- String
local bool = true           -- Boolean
local nilValue = nil        -- Nil (no value)

-- Tables (the only data structure)
local list = {1, 2, 3}      -- Array-like table
local dict = {name = "Alice", age = 30}  -- Map-like table
```

### Control Flow
```lua
-- If-else
if x > 0 then
    print("positive")
elseif x < 0 then
    print("negative")
else
    print("zero")
end

-- While loop
while count > 0 do
    count = count - 1
end

-- Repeat-until (do-while)
repeat
    count = count + 1
until count >= 10

-- Numeric for
for i = 1, 10 do
    print(i)
end

-- For with step
for i = 10, 1, -2 do
    print(i)
end

-- Generic for (iterating tables)
for key, value in pairs(dict) do
    print(key, value)
end

for index, value in ipairs(list) do
    print(index, value)
end
```

### Functions
```lua
-- Function definition
function add(a, b)
    return a + b
end

-- Anonymous function
local multiply = function(a, b)
    return a * b
end

-- Multiple return values
function minmax(numbers)
    local min = math.huge
    local max = -math.huge
    for _, v in ipairs(numbers) do
        if v < min then min = v end
        if v > max then max = v end
    end
    return min, max
end

local minVal, maxVal = minmax({3, 1, 4, 1, 5})

-- Vararg
function sum(...)
    local total = 0
    for _, v in ipairs({...}) do
        total = total + v
    end
    return total
end

-- Closures
function counter()
    local count = 0
    return function()
        count = count + 1
        return count
    end
end

local next = counter()
print(next())  -- 1
print(next())  -- 2
```

### Tables (The Core Data Structure)
```lua
-- Array-like
local fruits = {"apple", "banana", "cherry"}
print(fruits[1])  -- "apple" (1-indexed!)
table.insert(fruits, "date")
table.remove(fruits, 2)

-- Map-like
local person = {
    name = "Alice",
    age = 30,
    greet = function(self)
        return "Hello, I'm " .. self.name
    end
}

-- Accessing fields
print(person.name)
print(person["name"])

-- Iterating
for key, value in pairs(person) do
    print(key, value)
end

-- Table length
print(#fruits)  -- Number of array elements
```

### Metatables and OOP
```lua
-- Metatable for operator overloading
local Vector = {}
Vector.__index = Vector

function Vector.new(x, y)
    local self = setmetatable({}, Vector)
    self.x = x
    self.y = y
    return self
end

function Vector.__add(a, b)
    return Vector.new(a.x + b.x, a.y + b.y)
end

function Vector.__tostring(v)
    return string.format("Vector(%d, %d)", v.x, v.y)
end

-- Inheritance
local Circle = setmetatable({}, {__index = Vector})
Circle.__index = Circle

function Circle.new(x, y, radius)
    local self = Vector.new(x, y)
    setmetatable(self, Circle)
    self.radius = radius
    return self
end
```

### String Manipulation
```lua
local str = "Hello, World!"

-- Concatenation
local greeting = "Hello, " .. "World"

-- String functions
string.len(str)           -- Length
string.upper(str)         -- Uppercase
string.lower(str)         -- Lowercase
string.sub(str, 1, 5)     -- Substring
string.find(str, "World") -- Pattern match
string.gsub(str, "World", "Lua") -- Replace
string.format("%d + %d = %d", 1, 2, 3) -- Format

-- Patterns (simplified regex)
string.match("hello123", "%d+")  -- "123"
```

### Error Handling
```lua
-- Pcall (protected call)
local success, result = pcall(function()
    error("Something went wrong")
end)

if not success then
    print("Error:", result)
end

-- Xpcall with error handler
local result = xpcall(
    function() error("oops") end,
    function(err) return "Handled: " .. err end
)

-- Assert
local value = assert(maybeNil, "Value cannot be nil")
```

### Modules
```lua
-- mymodule.lua
local M = {}

function M.greet(name)
    return "Hello, " .. name
end

function M.add(a, b)
    return a + b
end

return M

-- Usage
local mymodule = require("mymodule")
print(mymodule.greet("Alice"))
```

## Common Libraries
- `string` — String manipulation
- `table` — Table operations
- `math` — Mathematical functions
- `io` — Input/output
- `os` — Operating system interface
- `coroutine` — Coroutines
- `debug` — Debugging

## Strengths
- Extremely lightweight and fast
- Simple syntax, easy to learn
- Highly embeddable
- Flexible metaprogramming via metatables
- LuaJIT provides excellent performance

## Weaknesses
- Minimal standard library
- 1-indexed arrays can be confusing
- No built-in OOP (must be implemented via tables)
- Limited error handling compared to modern languages
- Smaller community than mainstream languages
