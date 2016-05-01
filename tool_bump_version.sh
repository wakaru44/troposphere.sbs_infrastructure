#!/bin/bash

echo "Updating the version file"
echo "$(cat version.md ) +1" | bc | while read foo; do printf  "%03d\n" $foo; done > version.next.md
rm version.md 
mv version.next.md version.md

echo "Current version will be $(cat version.md)"
