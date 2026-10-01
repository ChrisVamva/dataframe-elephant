# Elixir Basics

## Overview
Elixir is a dynamic, functional programming language built on the Erlang VM (BEAM). Created by José Valim in 2011, it combines Erlang's fault-tolerant concurrency with a modern, expressive syntax and metaprogramming capabilities.

## Key Characteristics
- **Paradigm**: Functional, concurrent
- **Typing**: Dynamic, strong
- **Compilation**: Compiled to BEAM bytecode (Erlang VM)
- **Memory Management**: Automatic garbage collection (per-process)
- **Concurrency**: Actor model (lightweight processes)

## Syntax Fundamentals

### Hello World
```elixir
IO.puts("Hello, World!")
```

### Variables and Data Types
```elixir
count = 42                    # Integer
pi = 3.14159                  # Float
name = "Alice"                # String (UTF-8 binary)
atom = :status                 # Atom (constant name)
list = [1, 2, 3]              # Linked list
tuple = {1, :ok, "data"}      # Tuple
map = %{name: "Alice", age: 30}  # Map
keyword_list = [name: "Alice", age: 30]  # Keyword list
```

### Pattern Matching
```elixir
# Assignment is actually pattern matching
{a, b, c} = {1, 2, 3}        # a=1, b=2, c=3

# In function heads
defmodule Math do
  def add(a, 0), do: a
  def add(a, b), do: a + add(a, b - 1)
end

# With lists
[head | tail] = [1, 2, 3]     # head=1, tail=[2, 3]

# With maps
%{name: name} = %{name: "Alice", age: 30}  # name="Alice"
```

### Control Flow
```ixir
# If-unless
if x > 0 do
  "positive"
else
  "non-positive"
end

# Case
case {:ok, result} do
  {:ok, value} -> "Got: #{value}"
  {:error, reason} -> "Error: #{reason}"
end

# Cond (like switch)
cond do
  x > 0 -> "positive"
  x < 0 -> "negative"
  true -> "zero"
end

# With (monadic error handling)
with {:ok, user} <- fetch_user(id),
     {:ok, profile} <- fetch_profile(user) do
  {:ok, profile}
else
  {:error, reason} -> {:error, reason}
end
```

### Functions
```elixir
# Anonymous functions
add = fn a, b -> a + b end
add.(1, 2)  # => 3

# Named functions in modules
defmodule Greeter do
  def greet(name), do: "Hello, #{name}!"

  # Multiple clauses (pattern matching)
  def factorial(0), do: 1
  def factorial(n), do: n * factorial(n - 1)

  # Default arguments
  def greet(name, greeting \\ "Hello") do
    "#{greeting}, #{name}!"
  end

  # Private functions
  defp helper(x), do: x * 2
end
```

### Pipe Operator
```elixir
"hello world"
|> String.upcase()
|> String.split()
|> Enum.join("-")
# => "HELLO-WORLD"
```

### Structs
```elixir
defmodule User do
  defstruct name: "", age: 0, active: true
end

user = %User{name: "Alice", age: 30}
user.name  # => "Alice"
```

### Concurrency (Processes)
```elixir
# Spawn a new process
spawn(fn -> do_work() end)

# Send and receive messages
send(self(), {:hello, "world"})

receive do
  {:hello, msg} -> IO.puts("Got: #{msg}")
  {:error, reason} -> IO.puts("Error: #{reason}")
after
  5000 -> IO.puts("Timeout")
end

# GenServer (OTP behavior)
defmodule Counter do
  use GenServer

  def start_link(initial) do
    GenServer.start_link(__MODULE__, initial)
  end

  def increment(pid), do: GenServer.cast(pid, :increment)

  def handle_cast(:increment, state) do
    {:noreply, state + 1}
  end
end
```

## Common Modules
- `Enum` — Collection enumeration and manipulation
- `Stream` — Lazy, composable enumerables
- `List` — List operations
- `Map` — Map operations
- `String` — String manipulation
- `IO` — Input/output
- `GenServer` — OTP server behavior

## Strengths
- Exceptional concurrency and fault tolerance
- Hot code swapping
- Scalable and distributed by default
- Immutable data structures
- Excellent for real-time systems

## Weaknesses
- Smaller ecosystem than mainstream languages
- Functional paradigm has a learning curve
- Dynamic typing can lead to runtime errors
- Niche community compared to Python/JS
