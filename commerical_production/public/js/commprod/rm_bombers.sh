#!/bin/bash

FILENAME=$1
cat $FILENAME | while read LINE
do
       blanche cantbloom -d LINE
done
