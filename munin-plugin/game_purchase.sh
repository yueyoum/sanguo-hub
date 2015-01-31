#!/bin/bash

if [ "$1" == "autoconf" ]
then
    echo "yes"
    exit 0
fi

if [ "$1" = "config" ]
then
    echo "graph_title Purchase status of Game"
    echo "graph_args --base 1000 -l 0"
    echo "graph_scale yes"
    echo "graph_vlabel Purchase"
    echo "graph_category game"
    echo "graph_info This graph shows the Purchase status of game"
    echo "graph_order sum order_amount char_amount"

    echo "sum.label sum"
    echo "sum.draw LINE2"
    echo "sum.info total purchase money"

    echo "order_amount.label order_amount"
    echo "order_amount.draw LINE1"
    echo "order_amount.info total purchase order amount"

    echo "char_amount.label char_amount"
    echo "char_amount.draw LINE1"
    echo "char_amount.info total purchase char amount"

    exit 0
fi

SELF=`readlink -f $0`
DIR=`dirname "$SELF"`

"$DIR/../env/bin/python" "$DIR/game_purchase.py"
