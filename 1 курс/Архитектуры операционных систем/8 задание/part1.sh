#!/bin/bash
defaultDirectory="attachments"
defaultName="some_file"
extension=".jpg"
count=20
mkdir $defaultDirectory
cd $defaultDirectory

for ((i=1; i < 20; i++))
do
    curl https://picsum.photos/800/400 -L > "$defaultName$i$extension"
done