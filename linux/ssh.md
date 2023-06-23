# How to use ssh

## setup ssh

After keygen, you get a .pub key and a secret key file without extension

```shell
ssh-keygen # generate new ssh key
```

Optional: move your key to ~/.ssh

```shell
mv key.pub ~/.ssh 
mv key ~/.ssh 
```

Add your **secret key** to ssh agent, so it can be used when you establish a ssh connection

```
ssh 
ssh-add key 
```

After setup local ssh keys, copy and paste your public key to ssh target host

Copy your public key

```shell
cat key.pub
```

## troubleshootings

### use credential after specify this accessibility

When you try to access a host with ident file, chmod 400 first, otherwise ssh agent will yield for password
