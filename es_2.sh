#!/bin/bash

find / \
	-type f \
	-not -path "/dev/*" \
	-not -path "/proc/*" \
	-not -path "/sys/*" \
	-exec file '{}' \; \
	| awk 'BEGIN { FS = ":" } ; $2 ~ /text/ { print }' \
	| tee txt-files.txt
