# Cached Integers and Strings

The 'is' operator in Python is used for identity comparison of two objects. Sometimes, using it on integers and strings gets really confuses you. Here's an example:

```
foo = "hello"
bar = "hello"

print(foo is bar) # Prints True

foo = "hello!"
bar = "hello!"

print(foo is bar) # Prints
```

Similar happens in case of numbers. Smaller numbers like 33 get the same identity everytime. This occurs due something called "Interning". The interpreter basically caches commonly used and smaller strings so it doesn't have to recreate a new object each time.