Running custom playbooks
------------------------

First you need to install any roles in the requirements.yml file:

```
ansible-galaxy install -r requirements.yml -p roles/
```

Firewall
--------

Please see firewall.readme.md.


Config Dump
--------------

To make an archive of overcloud configuration, you can use:

`kayobe playbook run $PWD/etc/kayobe/ansible/config-dump.yml --vault-password-file ~/vaultpassword`

This takes care to redact any passwords from the archive.

You will find the output in `$PWD/redacted-config`.

