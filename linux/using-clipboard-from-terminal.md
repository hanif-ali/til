# Reading From and Writing to the Clipboard from the Terminal
In systems running the X Window System, it can be useful to read from and write to the clipboard from the Terminal. `xclip` is a utility that allows using the clipboard with the Standard input and output. It has three selections: `primary`, `secondary` and `clipboard` which can be specfied with `-selection`. When no selection is specified, it uses `primary`. The more common Copy and Paste functionalities of X Window use the `clipboard` selection.  

For example,
- `cat /etc/hostname | xclip -selection clipboard` (The contents of the file are copied and can now be pasted with Ctrl+V or xclip)
- `xclip -o -selection clipboard` (Print the contents of `clipboard` selection to the Standard output)