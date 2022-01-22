#
# ~/.bashrc
#

#export PATH="~/.cargo/bin:$PATH"

export PATH=/home/twfl/.local/bin:$PATH

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# no duplicates in history
HISTCONTROL=ignoreboth

alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '
eval "$(starship init bash)"

source .aliases

#### common mistakes
alias l="ls --color=auto"
alias s="ls --color=auto"
alias sl="ls --color=auto"
alias lls="ls --color=auto"
alias lsl="ls --color=auto"
alias lss="ls --color=auto"
alias sll="ls --color=auto"
alias sls="ls --color=auto"
alias al="ls --color=auto"
alias sk="ls --color=auto"
alias dc='cd'

#### my commands
# display system info
#neofetch
neofetch | lolcat -p 1
#### my aliases and functions

export MTP_NO_PROBE="1"


# BEGIN_KITTY_SHELL_INTEGRATION
if test -n "$KITTY_INSTALLATION_DIR" -a -e "$KITTY_INSTALLATION_DIR/shell-integration/bash/kitty.bash"; then source "$KITTY_INSTALLATION_DIR/shell-integration/bash/kitty.bash"; fi
# END_KITTY_SHELL_INTEGRATION
