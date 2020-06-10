#!/usr/bin/env sh
find . -name "test_client.py" | sed "s/\.\///" | xargs python3 -m unittest
