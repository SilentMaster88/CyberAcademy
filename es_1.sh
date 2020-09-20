#!/bin/bash

find / \
	-type f \
	-not -path "/dev/*" \
	-not -path "/proc/*" \
	-not -path "/sys/*" \
	-not -path "/tmp/*" \
	-exec sha512sum '{}' \; \
	| tee hashes.txt
