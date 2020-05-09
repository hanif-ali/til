# Viewing the Content of a File in Another Branch

git show is a command that outputs details of a particular git file including its contents. It can optionally take a branch name (default: current branch) and file/directory path (default: all tracked). This can be used to quickly open and view the contents of a file in a non-current branch of a git repository.

```
git show <branch_name>:/path/to/file | vim -
```
The output of the git-show is simply piped to Vim.