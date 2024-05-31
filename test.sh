#!/bin/bash

pycodestyle programming_task/
pylint programming_task/
pushd programming_task
python soft_tough_test.py
popd
