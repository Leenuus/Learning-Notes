# how to use

## components

1. virtualenv
2. virtualenvwrapper
3. zsh plugin virtualenvwrapper

## troubleshootings

### problem

```txt
virtualenvwrapper_run_hook:12: permission denied:-
virtualenvwrapper.sh: There was a problem running the initialization hooks.
```

### causes
It's probably your system use python3 command and not python. Adding alias python=python3 doesn't seem to work.

### solution
```zsh
export VIRTUALENVWRAPPER_PYTHON=$(which python3)
```

