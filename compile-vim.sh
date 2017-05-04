#!/bin/bash

set -e



install-vim () {
    (vim --version | grep -o 8.0) && echo 'Your Vim is already up to date' && exit 0

    sudo apt-get update && sudo apt-get install -y make unzip ncurses-dev libx11-dev libxtst-dev libxt-dev libsm-dev libxpm-dev

    cd ~
    test -d vim || git clone https://github.com/vim/vim.git

    cd vim/src && \
    ./configure --with-features=huge --enable-python3interp=dynamic --enable-cscope --prefix=${HOME} && \
        make && \
        make install && \
        sudo ln -s ${HOME}/bin/vim /usr/bin/vi -f
}


install-vim
