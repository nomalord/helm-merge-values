@echo off

python3 -m venv "$HELM_PLUGIN_DIR"/venv
"$HELM_PLUGIN_DIR"/venv/Scripts/pip3 install --editable .