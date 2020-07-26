# Using Sessions For Persistence

Sessions is a very nice feature provided by vim. Using sessions, you can store the current working status of Vim (files, tabs, positions, etc.) in a file and reload it upon opening the next time. This is quite similar to workspaces provided by other Text Editors and IDEs. 

To save the current working in to a session:
```
:mksession /path/to/file
```
or in short,
```
:mks /path/to/session/file
```

To load the session upon opening next time,
```
$ vim -S /path/to/session/file
```
directly from shell or
```
:source /path/to/session/file
```
from inside Vim.
