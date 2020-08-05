# Using Skeletons for Boilerplate code

One great usage of the Autocommand feature that I came across today is to autoload boilerplate code when a new file is created. 

For example, for HTML, you would put the boilerplate (skeleton) code in a file somewhere (I like to put it in `~/.vim/skeletons`) and use the following line in you `.vimrc` file.

```
au BufNewFile *.html
    \0read ~/.vim/skeletons/html
```
where `html` is the file containing the boilerplate code. `au` is the short form of `autocommand`.
