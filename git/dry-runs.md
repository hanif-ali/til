# Dry Runs
The `--dry-run` switch for `git commit` helps you to inspect (in advance) what files are included and excluded by the commit with the given options and path.
For example,
```
git commit -am "<Commit message here>" --dry-run
```
or
```
git commit some_dir/ -m "<Commit message here>" --dry-run
```
The summary can be seen in a very short and concise form with the --short flag.