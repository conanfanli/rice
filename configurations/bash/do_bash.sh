#!/bin/sh


BEGIN='# START bash_profile -DO-NOT-EDIT'

touch ~/.bash_profile
grep "$BEGIN" ~/.bash_profile || cat ~/docs/configurations/bash/bash_profile.bash >> ~/.bash_profile
