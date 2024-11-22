#!/bin/sh

python3 -m venv "$HELM_PLUGIN_DIR"/venv
"$HELM_PLUGIN_DIR"/venv/bin/pip3 install --editable .