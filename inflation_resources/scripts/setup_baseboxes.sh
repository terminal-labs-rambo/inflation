#!/usr/bin/env bash

mkdir -p inflation_resources/compiled_scripts

yasha inflation_resources/yasha_templates/bash_scripts/setup_baseboxes.sh.template -o inflation_resources/compiled_scripts/setup_baseboxes.sh

bash inflation_resources/compiled_scripts/setup_baseboxes.sh
