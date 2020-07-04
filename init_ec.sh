#!/bin/sh

HOST='omvsadm@ec33013a.vmec.svl.ibm.com'
HOME='/Users/asif'
REMOTE_BASH='/usr/lpp/rsusr/ported/bin/bash'

ssh-copy-id -i $HOME/.ssh/id_rsa $HOST
echo "put $HOME/Downloads/zoau-1.0.3.pax /u/omvsadm" | sftp $HOST 
echo "put $HOME/Downloads/pyz.66.pax.Z /u/omvsadm/" | sftp $HOST
scp $HOME/env $HOST:/u/omvsadm/
