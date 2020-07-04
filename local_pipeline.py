#!/usr/local/bin/python3

import os
import subprocess

def run_command(cmd, shell=False, cwd=None):
    res = subprocess.Popen(
        cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, 
        stdin=subprocess.PIPE, shell=shell, cwd=cwd
    )
    out, err = res.communicate()
    return (
        res.returncode, 
        out.decode() if out else '', 
        err.decode() if err else ''
    )


def main():
    working_dir = "/Users/asif/ibm_zos_core"
    pep_log = "/tmp/pep8.log"
    collection_dir = "/Users/asif/.ansible/collections/ansible_collections/ibm/ibm_zos_core"

    print('''
    --------------------------------------------------------------------------
                                Annsible Sanity Tests                       
    --------------------------------------------------------------------------'''
    )
    try:
        rc, out, err = run_command("ansible-test sanity", cwd=collection_dir, shell=True)
        for line in err.splitlines():
            print(line)
    finally:
        print("\nAnsible sanity tests complete!")

    print('''
    --------------------------------------------------------------------------
                                Bandit Security Scan                     
    --------------------------------------------------------------------------'''
    )
    rc, out, err = run_command(['bandit', '-r', '-ll', '-ii', './plugins'], cwd=working_dir)
    print(out)
    print("Bandit security scan complete!")


    

if __name__ == '__main__':
    main()