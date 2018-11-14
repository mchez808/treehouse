## Managing Workflows
[]A successful git branching model


### Workflows with Git-Flow
```
git branch integration -- make this branch prior
git flow init
```

*tagging*: special names for certain commits, such as committing production-ready changes into master branch.
`git flow feature start <feature_name>`
creates new branch, feature/feature_name. branch is based off of the integration branch (It's an  independent copy of integration)


git flow feature finish <feature_name>
summary includes:
* branch merge
* branch removal
* branch switch (checkout)


Hotfix: quick fix to master
Treat it just like a feature branch!
git flow hotfix start <bug_xyz>
The difference?  This hotfix branch is based off of master, and not off of integration.


Remote Repositories
A remote repo doesn't have to be on another computer; remote just means somewhere else.
note: remote is NOT reflexively constructed by default, i.e. a cloned repo is NOT a remote repo to the origin repo; only the origin is a remote repo.  Thus cloning doesn't affect the origin repo in any way.
If you want two repos to reflexively correspond to one another, you'd manually add a remote repo to the origin.
git remote add <clone-repo-name> <clone-repo-path>
git remote
after adding this cloned-remote repo, you can then run git remote and then view the cloned-remote repo.


* git remote add origin https://github.com/username/reponame.git 
    * origin is (or can be) the remote origin name
Pro Tips:
* Set up Git & cache your credentials
Merging
git merge branchname - merge the history from branchname into the current branch.


commit manually the resolved change.


.(don't delete this line -- leads to format issue!)
Create, Checkout, Rename a Branch
* git branch -help      (or just git branch -h)
* git branch: list all branches
* git branch branchname: create a new branch
* git checkout branchname: switch to the newly created branch
* git checkout -b branch-name: shortcut! - use this command to create & switch to the new branch, all in one line
* git branch -d branchname - delete branch (only if you have already pushed and merged it with your remote branches)
* git branch -D branchname - delete branch (forced, which deletes the branch regardless of its push and merge status, so be careful using this one!)
* git push origin branch-name: push branch & changes to github
    * git push origin master        (often you'll be pushing to master trunk)
    * origin is mandatory; Git expects remote-repo-name here. 
* git branch -m new-branch-name (ONLY if you're on the branch you want renamed)
* git push <remote_name> --delete <branch_name> -- to delete remote branches


want to search for a git commit by SHA?
git branch --contains $COMMIT_ID


Conclusion of Git Intro course 
But there are other important features we haven't covered, such as branches and merging file changes. You can learn more about those in our Git Basics course.
Unit 3: GitHub and Remote Repos
Pushing Commits to GitHub




This is far more common!


1. create new repo in GitHub (see extra instructions if needed for troubleshooting)
2. Adding the GitHub repo as a remote
    1. git remote add origin https://github.com/mchez808/codewars.git
    2. git push -u origin master
        1. -u means set-upstream.  It means that you want Git to remember the repo and branch you are about to specify, and make all future git push commands push to that repo and branch by default.
            1. How you know it's set: after execution, console returns "Branch master set up to track remote branch master from origin." 
        2. origin: the default repo
        3. master: we specify the branch in the remote repo to which we want to push.  (Note that master is a branch that gets created by default.)
    1. then refresh web page 


Troubleshooting: If you accidentally created one or more files in the GitHub repo...


Advanced instructions: Using SSH with GitHub
SSH is an alternate, secure way to connect to GitHub. It's convenient because once it's properly set up, you won't have to type your username and password every time you push or pull from a GitHub repo. But setting it up does require some experience with the terminal.
Sorry, but we can't help diagnose any issues you have with SSH; you'll be on your own.  If you want to set it up, GitHub has a tutorial here.




Cloning




(In practice, this is not done as often) 


git clone remote-repo-path cloned-repo-name
remote repo: a central repo
* when cloning a repo, the original repo is auto-set to be the remote repo to the clone.
* origin:    default name of remote repo
* remote-repo-path can be a URL or a local directory
    * (recall: a "remote" repo can be local to the machine, just elsewhere)


cloning doesn't just create a copy; it establishes original repo as a remote repo, by default named origin.
git remote
to view repos (that serve as a remote repo to the clone)


Pulling Changes




git pull 
to pull changes from remote repo 


optional/default: 
git pull origin
    origin is default name of remote repo


Adding a Remote Repo 
Background: when we cloned the repo, the source repo was auto-set up as the remote repo.
However, the reverse isn't true: 
... if we go into the source repo and run git remote from there, we don't see any remote repo.
This is a situation in which one is able to add a remote repo, since there's not auto-setup of a remote repo.


git remote add new-remote-repo <path>
ex: git remote add myclone ../myclone


git pull new_remote_repo_name branch_name


Pushing Commits to GitHub




This is far more common!


git push


git clone https://github.com/treehouse-courses/novel.git local_clone_repo


adding remote repo (in order to push commits to it)
when you clone a remote repo to a local repo, 


Unit 2: Managing Committed Files
unstaging changes
git reset HEAD <file>


warning: irreversible action -- discarding file modifications
git checkout -- <file>


undo file deletions
git checkout -- <file>


git rm
git mv 


revert to a previous commit


git revert 1de81
1de81 is the SHA for the commit you wish to undo, not the SHA you wish to arrive at/revert to. 


If you want to revert to the commit before c5f567, append ~1 (works with any number):
git checkout c5f567~1 -- (COMMENT: file1/to/restore file2/to/restore)
As a side note, I've always been uncomfortable with this command because it's used for both ordinary things (changing between branches) and unusual, destructive things (discarding changes in the working directory).


If you messed up in "abbcdf" and want the version right before "abbcdf", you can do git checkout "abbcdf~1" path/to/file


HEAD: "the most recent commit"
* You can use the HEAD shorthand in place of a commit SHA in any Git command that accepts SHAs.
    * SHA: simple hash algorithm.
    * example: 1d8e15a834a2157fe7af04421c42a893e8a1f23a




Unit 1: First Commits
To view Common Git subcommands, see these Teacher's Notes.


Initializing a Repository
Teacher's Notes 
git init
git init     (to initialize a new repo)
* You won't see the .git directory at first. But ls has a special command line option that will cause it to show all files, even hidden ones (which start with a "."/ a "DOT")
* ls -a   (show hidden files)
First Commits: on new files
Teacher's Notes
* git commands won't work outside a Git repo.


File statuses:
git status


Staging files
git add medals.html
result: Now medals.html is staged.


    to add all files:
        git add .


after staging: Config, then Commit
git config --global user.email "mark.chesney@gmail.com"
git config --global user.name "Mark Chesney"


SHORTCUT:
git commit -a -m "stage + commit all in one line!"


git config --list
to view what's configured


git commit
then:   "Add main site page"  (within text editor, e.g. nano)


(alternatively, short-hand one-line commit:)
git commit -m "Add main site page"




Commit message style:
* Message should complete this idea: "This commit will ..." [message] 
    * e.g., remove sale description
    * e.g., add new products


Review commit history
git log
git log -p


Staging Changed Files
Teacher's Notes
see Pictures/staging-changed-files1.png


Viewing Changes to a File (before committing)
Further Clarity: "git diff" shows only unstaged changes. "git diff --staged" shows only staged changes.
git diff
     (to compare modified file vs the staged file)
               (in case you've forgotten the specific changes you made.)
             (This way, you can view changes before you commit them)


git diff --staged
         (to compare staged changes against the previous commit)
                             (snapshot of file at the moment you've staged it)
(If you modify the file after staging, you have to stage the latest changes.)


If git diff & git log display nothing, you need to set the PAGER environment variable to less (console reader prgm).
export PAGER=less




git --version


Treehouse video: installing Git in Windows
* Visit the Official Git Website to download Git for Windows.
Before you install on Windows
* You might wish to install the Notepad++ text editor OR install the Visual Studio Code IDE prior to installing Git for Windows. If you do so, then when you're installing Git, you will be given additional options for the default text editor Git should use for commit messages
