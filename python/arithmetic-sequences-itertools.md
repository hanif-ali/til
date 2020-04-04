# Generating Simple Arithmentic Sequences with Itertools

Itertools is an awesome module that comes with a lot of functionalities that are very helpful. The simple ones are perhaps `repeat` and `count`.

`repeat` returns an iterator that keeps generating the same number over and over again indefinitely. For example:
```
import itertools at it
repeat_three = it.repeat(3)
print(next(repeat_three)) # Prints 3
print(next(repeat_three)) # Prints 3
```

`count` accepts a `start` and `step` and generates an iterator returning an arithmetic sequence starting with `start` and having a common difference of `step`.

```
my_sequence = it.count(start=0, step=6)
terms = [next(my_sequence) for _ in range(5)]
print(terms)  # prints [0, 6, 12, 18, 24]
```