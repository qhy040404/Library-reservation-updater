echo 'Waiting Updater to exit'
sleep 3
mv update/* ./
rm -r update
rm temp.zip
exit