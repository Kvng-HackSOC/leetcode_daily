#!/bin/bash

# Read words, convert spaces to newlines
# Sort words alphabetically
# Count occurrences
# Sort by count (descending)
# Print in the format: "word count"

tr -s ' ' '\n' < words.txt \
    | sort \
    | uniq -c \
    | sort -nr \
    | awk '{print $2, $1}'
