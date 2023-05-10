# Some learning notes for github and git

## new repo workflow

To initialize a repo, use command below.

```shell
git branch -M main # local branch is alaways named after master, just rename it as main
git remote add origin <remote_url> # name remote repo as "origin" and add a url
git push -u origin main # push to remote main 
```

To reset remote url, use

```shell
git remote set-url <remote-name> <new-remote-url>
```

# Setup SSH connection to Github

It is much more convinient to use SSH to push repo to remote github repo.

```shell
ssh-keygen # generate new ssh key
# you can name this key as you want, after keygen, you get a .pub key and a secret key file without extension

# optional move your key to ~/.ssh
mv key.pub ~/.ssh 
mv key ~/.ssh 

# add your **secret key** to ssh agent, so it can be used when you establish a ssh connection
ssh 
ssh-add key 

```

After setup local ssh keys, copy and paste your public key to github ssh manager.

To copy your public key, use `cat key.pub` and copy the text shown in your terminal.

## basic git usage

```shell
git checkout -b <branch-name> # to checkout a branch or create a branch
git branch -M <new-branch-name> # to rename current branch
git stash # as a way to make some no sure changes
git squash # compress many commits into one commit
git push --set-upstream <remote-name> <new-branch> # push a new branch to remote
```

## troubleshootings

### error: src refspec main does not match any

1. check whether your local repo set remote
2. check whether your local repo have first commmit

### everything is up to date

This message appears when you do not commit anything before pushing to remote repo.
