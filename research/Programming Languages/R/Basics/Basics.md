# R Basics

## Overview
R is a programming language and environment specifically designed for statistical computing and graphics. Created by Ross Ihaka and Robert Gentleman in 1993 at the University of Auckland, it is the standard language for statisticians, data analysts, and researchers.

## Key Characteristics
- **Paradigm**: Multi-paradigm (functional, OOP, procedural)
- **Typing**: Dynamic, strong
- **Execution**: Interpreted
- **Memory Management**: Automatic garbage collection
- **Primary Use**: Statistical analysis, data visualization, research

## Syntax Fundamentals

### Hello World
```r
print("Hello, World!")
```

### Variables and Data Types
```r
# Assignment
count <- 42              # Integer/numeric
name <- "Alice"          # Character/string
is_active <- TRUE        # Logical (TRUE/FALSE)
nothing <- NA            # Missing value
null_val <- NULL         # Null

# Vectors (atomic, same type)
numbers <- c(1, 2, 3, 4, 5)
chars <- c("a", "b", "c")

# Data types
typeof(42)        # "double"
typeof(42L)       # "integer"
typeof("hello")   # "character"
typeof(TRUE)       # "logical"
```

### Control Flow
```r
# If-else
if (x > 0) {
  print("positive")
} else if (x < 0) {
  print("negative")
} else {
  print("zero")
}

# If-else as expression
result <- if (x > 0) "positive" else "non-positive"

# For loop
for (i in 1:10) {
  print(i)
}

for (item in collection) {
  print(item)
}

# While loop
while (count > 0) {
  count <- count - 1
}

# Repeat loop
repeat {
  if (condition) break
}

# Switch
switch("A",
  "A" = print("Excellent"),
  "B" = print("Good"),
  print("Other")
)
```

### Functions
```r
# Function definition
add <- function(a, b) {
  return(a + b)
}

# Default parameters
greet <- function(name, greeting = "Hello") {
  paste(greeting, name, sep = ", ")
}

# Ellipsis (variable arguments)
flexible <- function(...) {
  args <- list(...)
  print(args)
}

# Anonymous function
sapply(1:10, function(x) x^2)

# Pipe operator (R 4.1+)
library(magrittr)
result <- data %>%
  filter(age > 18) %>%
  group_by(city) %>%
  summarise(count = n())
```

### Data Structures
```r
# Vector (atomic)
v <- c(1, 2, 3, 4, 5)
v[1]           # First element (1-indexed!)
v[v > 3]       # Filter
length(v)      # Length

# Matrix (2D, atomic)
m <- matrix(1:6, nrow = 2, ncol = 3)
m[1, 2]        # Row 1, Column 2
m[1, ]         # First row
m[, 2]         # Second column

# List (heterogeneous)
lst <- list(name = "Alice", age = 30, scores = c(90, 85, 95))
lst$name       # Access by name
lst[["age"]]   # Access by name (returns value)
lst[1]         # Access by index (returns sublist)

# Data frame (tabular, most important)
df <- data.frame(
  name = c("Alice", "Bob", "Charlie"),
  age = c(30, 25, 35),
  city = c("NYC", "LA", "Chicago")
)

df$name        # Column access
df[1, ]        # First row
df[, "age"]    # Age column
df[df$age > 28, ]  # Filter rows

# Factors (categorical)
gender <- factor(c("M", "F", "F", "M"), levels = c("M", "F"))
```

### Data Manipulation
```r
# Subset
df[1:3, ]                    # First 3 rows
df[, c("name", "age")]       # Specific columns
subset(df, age > 28)          # Conditional subset

# Transform
df$age_group <- ifelse(df$age > 30, "senior", "junior")

# Aggregate
aggregate(age ~ city, data = df, FUN = mean)

# Merge
merge(df1, df2, by = "id")

# Reshape
library(tidyr)
pivot_longer(df, cols = starts_with("score"))
pivot_wider(df, names_from = "variable", values_from = "value")
```

### Statistical Functions
```r
# Descriptive statistics
mean(x)
median(x)
sd(x)           # Standard deviation
var(x)          # Variance
summary(x)      # Min, Q1, Median, Mean, Q3, Max
quantile(x, probs = c(0.25, 0.5, 0.75))

# Distributions
rnorm(100, mean = 0, sd = 1)    # Random normal
pnorm(1.96)                      # CDF
qnorm(0.975)                     # Quantile
dnorm(0)                         # Density

# Hypothesis testing
t.test(x, y)                     # T-test
chisq.test(table)                # Chi-square test
cor.test(x, y)                   # Correlation

# Linear model
model <- lm(y ~ x1 + x2, data = df)
summary(model)
predict(model, newdata = new_df)
```

### Visualization
```r
# Base R plotting
plot(x, y, type = "l", main = "Title", xlab = "X", ylab = "Y")
hist(x, breaks = 20, col = "blue")
boxplot(y ~ group, data = df)
abline(h = mean(x), col = "red", lty = 2)

# ggplot2 (tidyverse)
library(ggplot2)

ggplot(df, aes(x = age, y = score, color = gender)) +
  geom_point() +
  geom_smooth(method = "lm") +
  labs(title = "Score by Age", x = "Age", y = "Score") +
  theme_minimal()

# Faceting
ggplot(df, aes(x = value)) +
  geom_histogram() +
  facet_wrap(~ category)
```

### Packages
```r
# Install and load
install.packages("tidyverse")
library(tidyverse)

# Tidyverse core packages
library(dplyr)      # Data manipulation
library(tidyr)      # Data tidying
library(ggplot2)    # Visualization
library(readr)      # Data import
library(purrr)      # Functional programming
library(stringr)   # String manipulation
library(lubridate)  # Date/time
```

## Common Packages
- `tidyverse` — Data science ecosystem
- `data.table` — Fast data manipulation
- `ggplot2` — Visualization
- `dplyr` — Data manipulation
- `shiny` — Interactive web apps
- `caret` / `tidymodels` — Machine learning
- `rmarkdown` — Reproducible reports

## Strengths
- Unmatched statistical analysis capabilities
- Excellent visualization (ggplot2)
- Vast collection of statistical packages (CRAN)
- Reproducible research (R Markdown)
- Standard in academia and research

## Weaknesses
- Steep learning curve for non-programmers
- Inconsistent syntax across packages
- Memory-intensive for large datasets
- Slower than general-purpose languages
- Limited use outside data analysis
