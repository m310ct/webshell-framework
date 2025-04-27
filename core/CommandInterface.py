from prompt_toolkit import prompt
from prompt_toolkit.styles import Style
from termcolor import colored
import subprocess
class CommandInterface:
    def __init__(self):
        self.style = Style.from_dict({
            'wsf':'underline default',
            'path':'bold ansired',
            'prompt':'default'
        })
        self.cmd = ""
        self.path = ""

    def IOhandler(self):
        self.cmd = prompt([("class:wsf","wsf"),
                               ("class:path",self.path),
                               ("class:prompt"," > ")],style=self.style)
        self.CmdHandler()

    def CmdHandler(self):
        if self.cmd is None:
            return
        elif self.cmd.strip() == "exit":
            self.cmd_exit()
            return
        elif self.cmd.strip() == "about":
            self.cmd_about()
            return
        elif any(self.cmd.strip().startswith(cmd) for cmd in ["use", "list", "con", "set"]):
            #这些命令在对应的生成器，连接器中设定
            pass
        else:
            self.exec_system_cmd(self.cmd)
            return
    def cmd_exit(self):
        print("Bye!")
        exit()

    def cmd_about(self):
        about_text = f"""
WebShell Framework (WSF)
==========================
Version: 1.0.0
Author: m310ct
Description:
    A modular webshell framework designed to support flexible shell generation,
    connection handling, and anti-detection techniques.
License: MIT
Github: {colored("https://github.com/m310ct/webshell-framework", "green",attrs=["underline"])}
            """

        print(colored(about_text, 'cyan'))

    def exec_system_cmd(self,command):
        try:
            res = subprocess.run(command, shell=True,
                                 check=True,
                                 capture_output=True,
                                 text=True)
            print(res.stdout.strip())
        except subprocess.CalledProcessError as e:
            print(f"{colored("[!]","red",attrs=["bold"])} Command faild with error:\n{colored(e.stderr.strip(),"red")}\nRun the {colored("help","cyan")} command for more details.")

    def run(self):
        while True:
            self.IOhandler()


