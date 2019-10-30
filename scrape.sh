#!/bin/bash

SPIDER="$1"
FORMAT="json"
OUTPUT=$(echo "pasta/data/$SPIDER.$FORMAT" | tr '[:upper:]' '[:lower:]')

if [ ! -z "$SPIDER" ]; then
    if [ -f "$OUTPUT" ]; then
        rm "$OUTPUT"
    fi
    scrapy crawl "$SPIDER" -o "${OUTPUT//" "/"-"}" -t "$FORMAT"
else
    echo "Usage: $0 spidername"
fi
