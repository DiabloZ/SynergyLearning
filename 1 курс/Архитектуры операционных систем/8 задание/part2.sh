#!/bin/bash
defaultDirectory="attachments"
cd $defaultDirectory
files=`ls *.jpg`
for file in $files
do
    rm $file
done