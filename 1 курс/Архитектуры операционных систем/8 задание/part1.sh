#!/bin/bashdefaultName="some_file"extension=".jpg"count=20for ((i=1; i < 20; i++))do    curl https://picsum.photos/800/400 -L > "$defaultName$i$extension"done