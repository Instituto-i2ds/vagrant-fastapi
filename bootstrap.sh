sudo apt update
sudo apt install python3 python3-pip -y
pip3 install fastapi uvicorn
cp /vagrant/main.py /home/vagrant/main.py
export PATH=$PATH:$HOME/.local/bin
uvicorn main:app --reload --host 0.0.0.0
