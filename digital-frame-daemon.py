import daemon
import signal
import os
import sys
import time
from synology_api import filestation, downloadstation
import pdb
import json


digiframe_working_directory='/home/pi/digital-frame/'
log_file='logfile'
stdoutfile='/home/pi/digital-frame/stdoutfile'
stderrfile='/home/pi/digital-frame/stderrfile'
Synology_Ip='ousborne.org'
Synology_Port='5001'
Username='Ben'
Password='Ozzie=Data1'

print("daemon mapped sigs")


def print_time():
    print("In print_time")
    print(os.getuid())
    print(os.getgid())
    print(os.getcwd())
    count=0
    running = True
    while running:
        with open(log_file, "a") as f:
            f.write("The time is now " + time.ctime())
            f.close()
        count = count + 1
        time.sleep(3)
        if count == 2:
            running = False
    #os.system("export DISPLAY=:0.0")
    os.system("export DISPLAY=0")
    print("Display: ", os.system("echo ${DISPLAY}"))
    running = True
    count = 0
    while running:
        os.system("xset -display ${DISPLAY} dpms force on")
        time.sleep(5)
        os.system("xset -display ${DISPLAY} dpms force off")
        time.sleep(5)
        if count == 2:
            running = False
        count = count + 1


def synology_test():
    with open(log_file, "a") as f:
        file_location=Synology_Ip + '/Ben/'
        fl = filestation.FileStation(Synology_Ip, Synology_Port, Username, Password, secure=True, cert_verify=False, dsm_version=7, debug=True, otp_code=None)
        fl_favs = fl.get_favorite_list()
        #pdb.set_trace()
        for key in fl_favs:
            f.write(key)
        fl_info = fl.get_info()
        for key in fl_info:
            f.write(key)
        f.write("Finished get info\n")
        fl_file_list = fl.get_file_list(folder_path='/home/Shared/DigiFrameTest')
        #fl_file_list_json = fl_file_list.read()
        #pdb.set_trace()
        #fl_file_list_data = json.loads(fl_file_list)
        #pdb.set_trace()
        for key in fl_file_list.get("data").get("files"):
            #pdb.set_trace()
            f.write(key.get('name'))
            f.write(": ")
            f.write(key.get('path'))
            f.write("\n")
        f.write("Finished get file list\n")
        f.close()

    #dwn = downloadstation.DownloadStation(Synology_Ip, Synology_Port, Username, Password, secure=True, cert_verify=True, dsm_version=7, debug=True, otp_code=None)
    #with open(log_file, "w") as f:
    #    f.append(dwn.get_info())
    #    f.close()

    




def run():
    print("In run")
    
    #with daemon.DaemonContext(
    #    chroot_directory=None,
    #    working_directory=digiframe_working_directory,
    #    stdout=sys.stdout,
    #    stderr=sys.stderr):
    #    synology_test();
    #    print_time()
    synology_test()


if __name__ == "__main__":                                                                               
    print("Starting main of digital frame")
    run()


