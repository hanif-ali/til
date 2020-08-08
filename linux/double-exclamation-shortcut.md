# The `!!` Shortcut in Bash

`!!` has a special meaning in Bash. It refers to the previous command that was executed. It can be useful, for example when you want to add something to the previously run command and rerun it.

For example, when installing packages, if you forget `sudo` instead of retyping the whole thing or scrolling up, you can simply do this:

```
$ apt install something

E: Unable to acquire the dpkg frontend lock (/var/lib/dpkg/lock-frontend), are you root?

$ sudo !!
```

This would get replaced with `sudo apt install something`.


