# Case Insensitive String Comparison

In bash, one way of making string comparison insensitive is to use the double bracket test syntax (`[[ $TEST = "VALUE" ]]`) with the `nocasematch` shell option set.

The option can be set using: 
```
shopt -s nocasematch
```
and unset usnig:
```
shopt -u nocasematch
```
