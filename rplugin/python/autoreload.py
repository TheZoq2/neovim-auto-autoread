import neovim
import time

@neovim.plugin
class Limit(object):
    def __init__(self, vim):
        self.vim = vim
        self.calls = 0

    @neovim.command('AutoreadLoop', range='', nargs='*', sync=False)
    def command_handler(self, args, range):
        while(True):
            self.vim.command("checktime")

            time.sleep(2);

