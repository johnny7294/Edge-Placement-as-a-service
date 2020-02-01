
echo "enter the path for the script"
read scriptpath
crontab -l > mycron
echo " * * * * * $scriptpath" >> mycron
crontab mycron
rm mycron
sudo run-parts /etc/cron.daily