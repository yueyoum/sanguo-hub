#!/bin/bash

if [ "$1" == "autoconf" ]
then
    echo "yes"
    exit 0
fi
    
if [ "$1" = "config" ]
then
    echo "graph_title Players Amount of Game"
    echo "graph_args --base 1000 -l 0"
    echo "graph_scale yes"
    echo "graph_vlabel Players amount"
    echo "graph_category game"
    echo "graph_info This graph shows the number of Accounts/Characters"
    echo "graph_order accounts characters"

    echo "accounts.label players"
    echo "accounts.draw AREA"
    echo "accounts.info Amount of Accounts"
    echo "characters.label characters"
    echo "characters.draw STACK"
    echo "characters.info Amount of Characters"

    exit 0
fi

SELF=`readlink -f $0`
DIR=`dirname "$SELF"`

"$DIR/../env/bin/python" "$DIR/game_players.py"
