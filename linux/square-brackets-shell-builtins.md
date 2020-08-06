# Square Brackets as shell Builtins and Standalone Files

The square brackets (`[` and `]`) are very common in shells like `bash` and `zsh`, especially in scripts where they are used to test various conditions. But it came as a surprise to me that unlike `if` or `case`, these are not reserved keywords. Instead, they are both shell builtins and standalone files typically located in `/usr/bin`.

This can easily be checked using the `type` shell builtin:

```
$ type -a [
[ is a shell builtin
[ is '/usr/bin/['
```

Contrary to this, the double brackets `[[` and `]]` are actually shell keywords: 

```
$ type -a [[
[[ is a shell keyword
```
