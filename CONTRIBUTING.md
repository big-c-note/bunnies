All contributions and ideas are very welcome.

If you want to work on the codebase, then although you don't have to, it is recommended to follow these prodedures to make collaborating with the codebase as painless as possible.

1. Clone the repo

With ssh (recommended):
git clone git@github.com:big-c-note/bunnies.git

With https:
git clone https://github.com/bunnies.git

2. Create your branch

Depending on what you are hoping to do with your branch, you may prefix it with different subjects. Below is a suggested formula.

#### Navigate to develop branch
git checkout develop

#### Ensure you have the latest changes
git status
git fetch origin -p
git rebase origin/develop develop

#### Create new additions.
git checkout -b feature/{issue-number}-{issue name} 

#### Create a quick fix
git checkout -b hotfix/{issue-number}-{issue-name}

3. Working on your feature branch
You should be based off of branch develop whether or not you make use of git flow. Commit your code like normal, and if there has been a day or more between your last commit, you may need to rebase your changes on top of the latest commits (head) of develop.

First fetch the latest changes from all branches (and prune any deleted branches):

git fetch origin -p
Next ensure your local develop has all of the changes that the remote develop has.

git rebase origin/develop develop
Finally ensure your feature branch has all of the changes in develop in it.

git rebase develop feature/my-feature-branch-name-here
When you rebase develop into your feature branch, you will need to force-push it to the repo. PLEASE BE EXTRA CAREFUL with this - only use force push on a feature branch that only you have worked on, otherwise you may overwrite other peoples commits, as it will directly modify the repo's git history.

git push origin feature/my-feature-branch-name-here --force
4. Creating a PR
Once you have wrote your cool new feature, you'll need to make a PR. If you can write any tests to support any new features introduced, this would be very welcome. If you have any conflicts with develop please ensure you have rebased with develop as instructed in step (3).

Please open a pull request via the github UI and request to merge into develop. Once there has been a successful review of your PR, and the automated tests pass, then feel free to merge at your leisure.
