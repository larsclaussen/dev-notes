## docker run options

### Environment variables 

Specify as many environment variables as you like with the `-e` option


```shell
docker run -e API_HOST="http://api:8000" -e API_USERNAME="badman" ...
```


### Volumes

```shell
docker run -v /local/path:/docker/path --rm docker-image-name command
```
If the command is an interactive processes (like a shell), you must use -i -t together in order to allocate a tty for the container process.


### Logs

Follow logs of a running docker instance

```shell
docker logs -f container-name
```

## Clean up

Remove unused containers, networks, images etc

```shell
docker system prune
```

:octicons-link-external-16:  [Official Docker system prune reference](https://docs.docker.com/engine/reference/commandline/system_prune/)

## docker-compose

Start a single service from a compose file, exposing the port 8000 that the webserver uses so it is accessible from the host.


```shell
docker-compose run --rm -p 8000:8000 --name web web python manage.py runserver 0.0.0.0:8000
```



### Resources

:octicons-link-external-16:  [Jérôme Petazzoni on docker build patterns](github.io/2021/11/30/docker-build-container-images-antipatterns/)