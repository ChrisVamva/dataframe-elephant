# Haskell Basics

## Overview
Haskell is a purely functional, statically typed programming language named after logician Haskell Curry. First released in 1990, it is known for its strong type system, lazy evaluation, and mathematical elegance.

## Key Characteristics
- **Paradigm**: Purely functional
- **Typing**: Static, strong, inferred (Hindley-Milner)
- **Evaluation**: Lazy (call-by-need)
- **Compilation**: Compiled (GHC) or interpreted (GHCi)
- **Memory Management**: Automatic garbage collection

## Syntax Fundamentals

### Hello World
```haskell
main :: IO ()
main = putStrLn "Hello, World!"
```

### Variables and Data Types
```haskell
-- Immutable bindings
count :: Int
count = 42

name :: String
name = "Alice"

pi :: Double
pi = 3.14159

isActive :: Bool
isActive = True

-- Lists (homogeneous, linked)
numbers :: [Int]
numbers = [1, 2, 3, 4, 5]

-- Tuples (heterogeneous, fixed size)
person :: (String, Int)
person = ("Alice", 30)

-- Maybe (optional value)
maybeName :: Maybe String
maybeName = Just "Alice"
nothing :: Maybe String
nothing = Nothing

-- Either (error handling)
result :: Either String Int
result = Right 42
errorResult :: Either String Int
errorResult = Left "something went wrong"
```

### Functions
```haskell
-- Function definition
add :: Int -> Int -> Int
add a b = a + b

-- Infix usage
result = add 3 5
result' = 3 `add` 5

-- Pattern matching
factorial :: Int -> Int
factorial 0 = 1
factorial n = n * factorial (n - 1)

-- Guards
grade :: Int -> String
grade score
    | score >= 90 = "A"
    | score >= 80 = "B"
    | score >= 70 = "C"
    | otherwise   = "F"

-- Lambda functions
square = \x -> x * x

-- Partial application
addTen :: Int -> Int
addTen = add 10

-- Function composition
process :: String -> Int
process = length . words . map toLower
```

### List Operations
```haskell
-- Cons operator
list = 1 : 2 : 3 : []

-- List comprehension
squares = [x * x | x <- [1..10]]
evens = [x | x <- [1..20], even x]

-- Higher-order functions
doubled = map (*2) [1, 2, 3]        -- [2, 4, 6]
filtered = filter even [1, 2, 3, 4] -- [2, 4]
summed = foldl (+) 0 [1, 2, 3]      -- 6

-- Common functions
head [1, 2, 3]      -- 1
tail [1, 2, 3]      -- [2, 3]
length [1, 2, 3]    -- 3
reverse [1, 2, 3]   -- [3, 2, 1]
take 2 [1, 2, 3]    -- [1, 2]
```

### Algebraic Data Types
```haskell
-- Custom data types
data Color = Red | Green | Blue

data Shape = Circle Double
           | Rectangle Double Double
           | Triangle Double Double Double

-- Pattern matching on custom types
area :: Shape -> Double
area (Circle r) = pi * r * r
area (Rectangle w h) = w * h
area (Triangle a b c) = 
    let s = (a + b + c) / 2
    in sqrt (s * (s - a) * (s - b) * (s - c))

-- Record syntax
data Person = Person {
    name :: String,
    age  :: Int
} deriving (Show, Eq)

alice = Person { name = "Alice", age = 30 }
```

### Type Classes
```haskell
-- Type class definition
class Describable a where
    describe :: a -> String

-- Instance implementation
instance Describable Person where
    describe p = name p ++ " is " ++ show (age p)

-- Common type classes: Eq, Ord, Show, Read, Functor, Monad, Applicative
```

### Monads and IO
```haskell
-- IO monad
main :: IO ()
main = do
    putStrLn "Enter your name:"
    name <- getLine
    putStrLn ("Hello, " ++ name ++ "!")

-- Maybe monad
safeDivide :: Double -> Double -> Maybe Double
safeDivide _ 0 = Nothing
safeDivide x y = Just (x / y)

-- Either monad
parseNumber :: String -> Either String Int
parseNumber s = case reads s of
    [(n, "")] -> Right n
    _         -> Left "Invalid number"

-- Functor, Applicative, Monad
fmap (+1) (Just 5)           -- Just 6
pure (+) <*> Just 3 <*> Just 4  -- Just 7
Just 3 >>= \x -> Just (x + 1)   -- Just 4
```

## Common Modules
- `Prelude` — Standard functions (automatically imported)
- `Data.List` — List operations
- `Data.Map` — Key-value maps
- `Data.Maybe` — Maybe utilities
- `Control.Monad` — Monadic operations
- `System.IO` — Input/output

## Strengths
- Extremely expressive and concise
- Strong type system prevents many bugs
- Lazy evaluation enables infinite data structures
- Pure functions are easy to test and reason about
- Excellent for domain-specific languages

## Weaknesses
- Steep learning curve
- Lazy evaluation can cause space leaks
- Complex error messages for beginners
- Smaller ecosystem than mainstream languages
- Challenging for imperative-minded programmers
