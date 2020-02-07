import os


class pnmwifi:

    def __init__(self):
        self.current_os = None  # Current os of host machine
        self.root_user = False  # Allow or disallow use commands as root
        self.get_current_os()  # Set current_os value
        pass

    # List available networks
    def get_networks(self, debug=False):
        commands = ['sudo ifconfig wlo1 up && sudo iwlist wlo1 scan | grep ESSID']
        if self.current_os == "ubuntu":
            networks = []
            command_return = os.popen(commands[0]).read()
            no_processed_return = command_return.split("\"")
            processed_return = self.list_elements_to_string(no_processed_return)
            for network in processed_return:
                if network.find("ESSID") == -1:
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
        if(os_info.find("Ubuntu")):
            self.current_os = "ubuntu"
        elif(os_info.find("raspberrypi")):
            self.current_os = "raspibian"
        pass

    def list_elements_to_string(self, original_list):
        string_list = []
        for element in original_list:
            string_list.append(str(element))
        return string_list

pnm_wifi = pnmwifi()
print(pnm_wifi.get_networks())
