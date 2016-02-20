Neovim auto autoread
====================

#Be aware that if you use this plugin, tab completion might get interrupted each time the update is run. I am looking for a fix for that#

Makes the `autoread` feature in vim actually work as you expect it by triggering it at a 2 second interval. 

Based on the answer to [this](http://vi.stackexchange.com/questions/2702/how-can-i-make-vim-autoread-a-file-while-it-doesnt-have-focus) stack overflow post but using the neovim plugin system.

#Installation
Place the rplugin folder in your neovim directory or install using your favourite plugin
manager. 

Vundle:
`Plugin 'TheZoq2/neovim-auto-autoread'`

Add the following to your .vimrc 
```
    "Autoreload files when changed externally
    set autoread
    if has('nvim') "Prevent errors when using standard vim
        autocmd VimEnter * AutoreadLoop
    endif
```

Alternativley you can start the `AutoreadLoop` function manually when you want automatic reloads.

#Configuration
If you feel like the autoread is too slow or is using too much performance, you can edit `rplugin/python/autoreload.py` and change the value in time.sleep to the amount of seconds to wait between reloads

#Standard vim alternative
If you are using standard vim you can use [this](https://bitbucket.org/Carpetsmoker/auto_autoread.vim) plugin instead.
