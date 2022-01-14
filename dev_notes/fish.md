# Fish and Shell

## Fish

Get commands from current session in all terminals

```shell
history merge
```

Search for a specific period of time. The `t` flag is short for `--show-time` which by default uses the strftime format # %c%n. 

Example for all commands executed in mei:

```shell
history -t | grep -i -A1 mei
```

Example for all commands executed between 13 and 27 jan 2021, shown in reversed order:

```shell
history -t -R | grep -i -A1 -E "[1-2][3-7] jan 2021"
```

Fish configuration file

```shell
~/.config/fish/config.fish
```


To show a greeting upon startup for instance, add

```shell
set -g -x fish_greeting 'kau i ka nalu'
```


## Shell

### `which` vs `type`

- `which`
  - finds executable in your `$PATH`
  - lives in /usr/bin/which

- `type`
  - determines if command is alias, function, built-in command, cached executable (hashed), binary in `$PATH`, etc
  - shell builtin


### Users

Find user name belonging to user ID

```shell
id -un <ID>
```
