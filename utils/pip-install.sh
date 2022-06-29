#!/bin/sh

for f in $(ls requirements*.txt)
do
    pip install --no-cache-dir -r $f
done