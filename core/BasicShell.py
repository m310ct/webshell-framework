from core.CommandInterface import CommandInterface
class BasicShell(CommandInterface):
    def __init__(self):
        super().__init__()

    def CmdHandler(self):
        super().CmdHandler()
        if self.cmd.strip() == "help":
            self.cmd_help()

    
    def cmd_help(self):
        print("<UNK> <UNK> <UNK> <UNK> <UNK> <UNK> <UNK> <UNK> <UNK>")
