# /bin/bash
python3 -m venv venv
. ./venv/bin/activate
python3 -m pip install -r requirements.txt
pip install --upgrade pytest Flask
pytest hello_world_test.py
JENKINS_NODE_COOKIE=dontKillMe nohup python3 main.py > ~/flasklogs.log 2>&1 &
