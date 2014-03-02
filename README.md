obe
===
Script for installing and setting Virtual Machine from SSH.
Obe is an easy way to install and setting VM environment.


## Prerequisites
### Setup locale
```shell
$ locale-gen en_GB en_GB.UTF-8
$ dpkg-reconfigure locales
```
### Add user
```shell
$ adduser example_user sudo
```

### Setup SSH Key Pair Authentication
On your local machine:
```shell
$ ssh-keygen
```

```shell
$ scp ~/.ssh/id_rsa.pub example_user@your_locahost:
```
On your remote box:
```shell
$ mkdir .ssh
$ mv id_rsa.pub .ssh/authorized_keys
$ chown -R example_user:example_user .ssh
$ chmod 700 .ssh
$ chmod 600 .ssh/authorized_keys
```

### Disabling SSH Password Authentication and Root Login

```shell
$ sudo vi /etc/ssh/sshd_config
```
Set the following config params:
```shell
PasswordAuthentication no
PermitRootLogin no
```

## Usage
fab -H  <host>

## Licence

Apache 2 Copyright (c) 2014 