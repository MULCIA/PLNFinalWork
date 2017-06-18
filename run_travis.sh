#!/usr/bin/env bash
python3 --version > /dev/null &
nosetests --with-coverage
