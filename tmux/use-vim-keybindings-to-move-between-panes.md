# Use Vim Keybindings To Move Between Panes
The default configuration of Tmux allows you to move between panes using the Arrow Keys but if you are a Vim user, you might be accustomed to using `h`, `j`, `k`, and `l`. Here is a `.tmux.conf` config that I use to rebind the keys for Moving between panes:
```
bind h select-pane -L
bind j select-pane -D
bind k select-pane -U
bind l select-pane -R
set -g mouse on
set-window-option -g mode-keys vi
```