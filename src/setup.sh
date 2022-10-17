echo 'installazione in corso di python3 '
echo 'install python3 whait ...'
echo 'installazione di librerie'
echo 'install librery python'
echo 'info: installer versione/version 0.2_pre-Alpha'
sudo apt-get python3 
pip3 install tqdm
pip3 install rich
pip3 install platform
pip3 install inquirer

python3 bootloader.py