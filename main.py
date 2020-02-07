import os
import sys
import subprocess

class pnmwifi:

    def __init__(self):
        self.current_os = None # Current os of host machine
        self.root_user = False # Allow or disallow use commands as root
        self.sudo_password = "123456" # Solve password problem
        self.get_current_os() # Set current_os value 
        pass

    # List available networks
    def get_networks(self, debug=False):
        commands = ["sudo ifconfig wlo1 up && sudo iwlist wlo1 scan | grep ESSID > arquivinho.txt"]
        if self.current_os == "ubuntu":
            p = subprocess.run(commands[0], shell=True, stderr=subprocess.PIPE)
            while True:
                out = p.stderr.read(1)
                if out == '' and p.poll() != None:
                    break
                if out != '':
                    sys.stdout.write(out)
                    sys.stdout.flush()
        pass

    # List available network interfaces
    def get_network_interfaces(self): 
        pass

    # Set self.root_user value to True or False
    def set_root(self, value=False):
        if value:
            self.set_root = True
        pass

    # Get current os running at host machine
    def get_current_os(self):
        os_info = str(os.uname())
        if(os_info.find("Ubuntu")):
            self.current_os = "ubuntu"
        elif(os_info.find("raspberrypi")):
            self.current_os = "raspibian"
        pass

pnm_wifi = pnmwifi()
pnm_wifi.get_networks()
