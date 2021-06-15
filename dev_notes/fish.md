# Fish and Shell

## Fish

Get commands from current session in all terminals

```shell
history merge
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
