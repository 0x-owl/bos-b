#!/usr/bin/env zsh

echo "[INFO] Remove virtualenv folder if exists..."
rm -rf $(pwd)/env

echo "[INFO] Building virtualenv..."
python3 -m venv env

echo "[INFO] Attaching correct python path..."
echo PYTHONPATH="$(pwd)/coc" >> $(pwd)/env/bin/activate
echo "export PYTHONPATH" >> $(pwd)/env/bin/activate

awk 'NR==17{print "    unset PYTHONPATH"}19' $(pwd)/env/bin/activate >> $(pwd)/env/bin/activate2
rm $(pwd)/env/bin/activate
mv $(pwd)/env/bin/activate2 $(pwd)/env/bin/activate

echo "[INFO] Activate virtualenv..."
source $(pwd)/env/bin/activate

echo "[INFO] Installing requirements..."
pip3 install -r $(pwd)/docker/requirements.txt

echo "[INFO] Load fixtures.."
./coc/creator/fixtures/orchestrator.sh




