#!/bin/bash

for source_file in "test"/*.b; do
    test_name=$(basename "$source_file" .b)

    input_files=("test/${test_name}".*.input)
    if [ -e "${input_files[0]}" ]; then
        for input_file in "${input_files[@]}"; do
            index=$(basename "$input_file" .input | awk -F. '{print $2}')
            output_file="test/${test_name}.${index}.output"
            tmp_file="test/${test_name}.${index}.tmp"

            python3 improved-parakeet.py "$source_file" < "$input_file" > "$tmp_file"

            if diff "$tmp_file" "$output_file" > /dev/null; then
                echo "Test passed for $source_file with input $input_file"
            else
                echo "Test failed for $source_file with input $input_file"
                diff "$tmp_file" "$output_file"
            fi

            rm "$tmp_file"
        done
    else
        tmp_file="test/${test_name}.tmp"
        output_file="test/${test_name}.output"

        python3 improved-parakeet.py "$source_file" > "$tmp_file"

        if diff "$tmp_file" "$output_file" > /dev/null; then
            echo "Test passed for $source_file"
        else
            echo "Test failed for $source_file"
            diff "$tmp_file" "$output_file"
        fi

        rm "$tmp_file"
    fi
done