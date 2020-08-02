# Using Keyword Only Parameters for Functions

There is a simple way of setting some parameters of a function such that they can be used only as keyword arguments.
To do that, just put all your keyword-only parameters after an `*` in the parameters list.

Example: 
<hr>
```
def sample_function(a, b, *, c):
	print(a, b, c)
```
Now `sample_function` can be called as `sample_function(2, 3, c=10)` or `sample_function(2, b=3, c=10)` but if you run `sample_function(2, 3, 10)` it will raise an error: 
```
Traceceback (most recent call last):
  File "test.py", line 1, in <module>
    sample_function(2, 3, 10)
TypeError: sample_function() takes 2 positional arguments but 3 were given
```


