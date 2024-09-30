#!/bin/bash

# Greet the user
echo "Hello, ${USER}, it's good to see you!"

# Get user's first ticker.
echo "Let's get started with some simple stock market sims."

YESNOFLAG = "n"

while [[ YESNOFLAG == "n" ]]; do
echo "Please enter the ticker symbol for your desired stock:"
read TCKRSYM
echo "You entered ${TCKRSYM}, correct? [y/n]"
read YESNOFLAG
done