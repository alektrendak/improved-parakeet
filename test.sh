#!/bin/bash

for source_file in "test"/*.b; do
    test_name=$(basename "$source_file" .b)
    
    python3 improved-parakeet.py "$source_file" > "test/${test_name}.tmp"
    
    if diff "test/${test_name}.tmp" "test/${test_name}.output" > /dev/null; then
        echo "Test passed for $source_file"
    else
        echo "Test failed for $source_file"
        diff "test/${test_name}.tmp" "test/${test_name}.output"
    fi
    
    rm "test/${test_name}.tmp"
done