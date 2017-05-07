#########################################################################
# File Name: 1.sh
# Author: yszhang
# Mail:yangsongzhang@hust.edu.cn
# Created Time: Thu 04 May 2017 11:12:35 PM CST
#########################################################################
#!/bin/bash

log_file_dir="../"

log_file_name="`date +%y%m%d`.log" 

log_file_path=$log_file_dir$log_file_name

nohup sudo python manage.py runserver 0.0.0.0:80 > $log_file_path &
