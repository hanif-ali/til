# Performing Empty Commits

Sometimes, I need to retrigger various things with a git repository, such as CI Tests and various Hooks. In such cases, I used to make a small change somewhere in the README and then make a commit. It would be nice and helpful if we could just make commits without any changes. Well, I came to know today that there is a flag for that:

```
git commit --allow-empty -m "Message Here"
```
This would create an empty commit in the repository. I find it very helpful.
