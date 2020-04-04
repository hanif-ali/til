# Generating the Fibonacci sequence with Itertools

This TIL is to show how to generate second order recurrence relations using Itertools in Python. One famous example of such relation is the Fibonacci Sequence.

Since Fibonacci sequence is similar to an accumulator, we would first need to define a function like this,

```
def second_order(p, q, r, initial_values):
    """Return sequence defined by s(n) = p * s(n-1) + q * s(n-2) + r."""
    intermediate = it.accumulate(
        it.repeat(initial_values),
        lambda s, _: (s[1], p*s[1] + q*s[0] + r)
    )
    return map(lambda x: x[0], intermediate)
```

Now we can use the function that we created to get an iterator that generates the Fibonacci Sequence indefinitely.

```
fib_gen = second_order(p=1, q=1, r=0, initial_values=(0, 1))
terms = list(next(fibs_gen) for _ in range(8))
print(terms)    # Prints [0, 1, 1, 2, 3, 5, 8, 13]
```