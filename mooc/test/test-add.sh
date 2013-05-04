#!/bin/bash
#
# test client access to our service

echo -e "\n"
curl -i --data "name='cmpe275'&value='project2'"  http://localhost:8080/moo/data
echo -e "\n"
