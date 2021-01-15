sudo apt update
sudo apt install python3 python3-pip -y
pip3 install fastapi uvicorn
export PATH=$PATH:$HOME/.local/bin
# cp /vagrant/main.py .
# uvicorn main:app --reload --host 0.0.0.0
