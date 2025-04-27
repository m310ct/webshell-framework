from core.CommandInterface import CommandInterface
from core.Connector import Connector
class BasicShell(CommandInterface):
    def __init__(self):
        super().__init__()

    def CmdHandler(self):
        super().CmdHandler()
        if self.cmd.strip() == "help":
            self.cmd_help()
        elif self.cmd.strip().startswith("con"):
            self.cmd_con()

    def cmd_con(self):
        #这里应该从data文件中读取已经配置的连接会话，这里知识测试，代码应该移动到连接器终端
        url = self.cmd.strip()[4:]
        print(f"Connecting to {url}...")
        con = Connector(url,"cmd")
        con.connect()

    def cmd_help(self):
        print("<UNK> <UNK> <UNK> <UNK> <UNK> <UNK> <UNK> <UNK> <UNK>")
