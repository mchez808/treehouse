Source: [Trailhead](https://trailhead.salesforce.com/content/learn/modules/git-and-git-hub-basics/work-with-your-history-in-git)

## best flags for git log

```
git log -10

git log --oneline

git log --oneline --graph

git log --oneline --graph --decorate

```


git log -10 will only show the 10 most recent commits.

git log --oneline is a great way to view commit history by displaying the first seven characters of the SHA-1 hash and commit message of the commits on the current branch.

git log --oneline --graph presents commit history in a ASCII graph displaying the different branches in the repository and their commits.

git log --oneline --graph --decorate displays the same ASCII graph that is displayed using the --graph modifier, but also includes the branch name(s) for the different commits being displayed.


## git show

If you would like to view the changes that were made in a previous commit, you can use this:

`git show <SHA-1>`

a command to display the details of that specific commit. It includes things like commit author, time and date of the commit,
and a list of the changes that were made to the various assets within the repository.

# Undo a Previous Change

Beware, some commands that help us fix mistakes destructively modify the commit ID. Since these commit IDs are immutable, 
you could potentially cause issues for other collaborators. 
As a general rule, you should only use `git revert` if the commit has been pushed to the remote.

## git revert

`git revert` can be used on commits at any point in the repository’s history without affecting other work. 
Note, you can’t use `git revert` to resolve conflicts—if there are more recent conflicting changes, Git will ask you to resolve as if it’s a merge conflict.
Using `git revert` is a safe way to undo a specific change, preventing any of the typical complications that occur when altering the commit history of a project.

### Amending Commits 

You might make a typo within the commit message.
You can use `git commit --amend` to make a modification to the last commit you made. 
This will alter the commit history of your project, so it is **recommended that you don't use `git commit --amend`** 
if you have already pushed your commits to the remote.

You can also use `git commit --amend` to rewrite the most recent commit to include files in your staging area.

## Rewind to an Earlier Point in History

`git reset`

We know programmers love to experiment and try new things. 
However, sometimes during the course of that experimentation we realize we went down the wrong path and the commits 
we were making might not be as useful as we originally thought.

Git has a `git reset` command that can help rewind the history of our project, but, it alters the commit history, 
which as mentioned before, might cause issues for other collaborators. It is highly recommended that you use 
`git reset` *only when **you have** not pushed your commits to your remote* branch. 

`git reset` comes in three distinct flavors: 

```
git reset --soft

git reset --mixed

git reset --hard
```

`git reset --soft` takes the identified commit(s) and places all of the changes in the staging area. This is helpful if you want to take a group of commits and squash them into a single larger commit.

`git reset --mixed`, the default mode for git reset, takes the identified commit(s) and places all of the changes in the working directory. Like --soft, this is helpful if you want to take a group of small commits and combine some of the changes to make larger commits. But you can also use it to make additional changes to the files and then re-create the commit history.

`git reset --hard` will take the identified commit(s) and destroy them. Be careful with this, because they don’t go in your trash or recycle bin—the files essentially don't exist and are completely removed from your repository. Any uncommitted changes to files that are currently in the working directory or staging area will also be deleted. You can lose work with git reset --hard.

### Example: git reset

An example of using reset could look something like this:

`git reset --soft HEAD~2` would rewind the branch you are on by two commits (remember HEAD is a pointer to the tip of your branch). The changes that had been made in those last two commits would be reflected in the staging area.



# Git Merge Strategies

[open in link here](https://trailhead.salesforce.com/content/learn/modules/git-and-git-hub-basics/work-with-your-history-in-git)
  
