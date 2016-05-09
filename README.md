an example with troposphere to spin up a simple instance in amazon

This is part of a bigger effort, to have a remote work station, with some basics, fully automated.

1- something to provision a machine in AWS

2- something to run the ansible playbook as downloaded from the branch master of a repo

3- mount something like a filesystem with access to a cloud (dropbox, drive, whatever)

and give you the access details of such a thing. 

## Features 

- spins up an insntance

- there is some basic tooling around to make it easier to use, `make` and the `tool_*` scripts.


## Work in progress

- make it add the instance to a hosted zone with a nice dns name


## Improvements

- Add some static storage that is not destroyed after the destruction of the stack.

- use an existing VPC to spin up the instance (lets call it personaldev VPC)
