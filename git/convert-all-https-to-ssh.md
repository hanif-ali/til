# Convert All HTTPS Connections to SSH

If you use SSH for Git and Github, it would be really great if all http URLs automatically converted themselves to SSH urls so that you can simple copy paste Repo URLs without the need of converting them to SSH. Git allows you to do just that using the below configuration.
```
git config url.ssh://git@github.com/.insteadOf https://github.com/
```

Similarly for Gitlab, you can do
```
git config url.ssh://git@gitlab.com/.insteadOf https://github.com/
```

