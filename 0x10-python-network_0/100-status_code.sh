#!/bin/bash
# cript that sends a request to a URL passed as an argument, and displays only the status code of the response.
curl -sLw "%{hp_code}" -o /dev/null "$1"
