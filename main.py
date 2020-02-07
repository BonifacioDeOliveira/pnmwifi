import os


class pnmwifi:

    def __init__(self, debug_mode=False):
        self.current_os = None  # Current os of host machine
        self.root_user = False  # Allow or disallow use commands as root
        self.get_current_os()  # Set current_os value
        self.debug_mode = debug_mode
        pass

    # List available networks
    def get_networks(self, debug_mode=False):
        commands = ['sudo ifconfig wlo1 up && sudo iwlist wlo1 scan | grep ESSID',
                    'sudo ifconfig wlan0 up && sudo iwlist wlan0 scan | grep ESSID']
        networks = []
        if self.current_os == "ubuntu":
            command_return = os.popen(commands[0]).read()
        if self.current_os == "raspberrypi":
            command_return = os.popen(commands[1]).read()
        if self.debug_mode:
            print(command_return)
        no_processed_return = command_return.split("\"")
        processed_return = self.set_list_elements(no_processed_return)
        for network in processed_return:
            if network.find("ESSID") == -1 and network.find("\n") == -1:
                networks.append(network)

        return(networks)

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
        if(os_info.find('Ubuntu') != -1):
            self.current_os = "ubuntu"
        if(os_info.find('raspberrypi') != -1):

            self.current_os = "raspberrypi"
        pass

    def set_list_elements(self, original_list):
        string_list = []
        for element in original_list:
            element = str(element)
            if element != '':
                string_list.append(element)
        string_list = list(dict.fromkeys(string_list))
        return string_list

pnm_wifi = pnmwifi()
print(pnm_wifi.get_networks())
