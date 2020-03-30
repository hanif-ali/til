# Using Underscore as a separator in Python

PEP 515 (introduced in Python 3.6) allows the usage of underscores ("_") as a separator for large numbers. This can be useful as you cannot separate the place values using "," as that would make it a tuple.
Here is an example,
```
some_large_number = 100_000_000_000_000
print(f'{some_large_number:,}`)
```
And the output would be `100,000,000,000,000`