#!/bin/bash
collection_dir=/Users/asif/ibm_zos_core
collection_install_dir=/Users/asif/.ansible

cd $collection_dir
rm ./*.tar.gz
ansible-galaxy collection build

cd $collection_install_dir
rm -rf ./collections/ansible_collections/*
ansible-galaxy collection install $collection_dir/*.tar.gz -p ./collections


