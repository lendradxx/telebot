export PYTHONDONTWRITEBYTECODE=1

if [ ! -f settings.conf ]; then
    read -p "Enter your Token: " TOKEN
    read -p "Enter your Prefix: " PREFIX
    echo "Writing Configuration..."
    sleep 1
    echo -e "[BOT]\nTOKEN=$TOKEN\nPREFIX=$PREFIX" > settings.conf
    echo "Configuration file writed, now exiting..."
    echo "Please rerun this script to continue..."
    exit 1
else
    echo "Entering environment..."
    sleep 1
    source .env/bin/activate
    echo "Running bot..."
    python src/main.py
fi