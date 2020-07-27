# Change Working Directory from Inside a Session

The working directory of a Tmux session is the one that you are in when you create a new window. You can change the working directory when attaching to a session by:
```
tmux attach-session -t <SESSION> -c <PATH_TO_WORKING_DIRECTORY>
```

But sometimes you would want to change the working directory when you are already using that session. At that time, you can simply use `<Ctrl-b> :` and then type the command

```
tmux attach-session -t . -c <PATH_TO_WORKING_DIRECTORY>
```
