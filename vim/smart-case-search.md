# Using Smart Case for Search

By default everything in Vim is case-sensisitve, including the search feature. Case-sensitivity can be switched off using `set ignorecase`. This way all searches will be done in a case-insensitive manner.

But there is a third mode named `smartcase` which is very convenient. I personally use it all the times. When it is enabled, vim will only search in case-sensitive mode when there is a capital letter in the search string. Otherwise the case-insensitive mode will be used. 

For enabling smartcase, both `ignorecase` and `smartcase` need to be set:
```
:set ignorecase
:set smartcase
```

The only small issue is this mode is that it also gets enabled for the substitution command (`:s`) which confuses me sometimes but I can easily switch it off and on with a keymapping.
