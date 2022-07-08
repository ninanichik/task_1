#!/usr/bin/env bash

echo "starting to simulate load with gzip"
cat /dev/urandom | gzip -9 > /dev/null