install:
\tpython -m pip install -r requirements.txt

test:
\tpytest -q

compile:
\tpython -m compileall ai services notifications tests

blue-green-demo:
\tbash devops-infra/blue-green/switch_color.sh
