#!bash

# This setup for Arch Based and using yay as aur helper only!

if [ ! which pip > /dev/null 2>&1 ]; then
    echo "pip not found, installing pip..."
    sleep 1
    yay -S python-pip
fi

if [ ! -d .env ]; then
    echo "Creating virtual environment for python (Recommended)"
    sleep 1
    python -m venv .env
    echo "Done"
    sleep 1
fi 

echo "Entering venv..."
sleep 1
source .env/bin/activate
echo "Installing requirements..."
pip install -r requirements.txt
echo "All Done!, now run the bot with command ./scripts/start.sh"