#!/usr/bin/env bash
#@echo off

#Current dir
#Host type
#Build type: release, debug

export ARCH_TYPE=all
export BUILD_TYPE=all

python3 scripts/build.py $PWD linux $BUILD_TYPE

