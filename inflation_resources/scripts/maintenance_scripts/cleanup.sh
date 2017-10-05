#!/usr/bin/env bash

mkdir -p inflation_resources/compiled_scripts

yasha inflation_resources/yasha_templates/bash_scripts/cleanup.sh.template -o inflation_resources/compiled_scripts/cleanup.sh

bash inflation_resources/compiled_scripts/cleanup.sh
