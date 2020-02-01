
#echo "enter the path for the script"
#read scriptpath
crontab -l > mycron
#echo " * * * * * $scriptpath" >> mycron
echo " * * * * * $1" >> mycron
crontab mycron
rm mycron
sudo run-parts /etc/cron.daily