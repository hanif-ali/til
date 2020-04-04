# Copying Files From a Running Container to the Host Machine

If you have a Docker container running and you want to copy files form inside the container to the host, you can simply do so using,
```
cp <container_id>:/path/in/container /path/in/host
```
The revserse can also be done. You can copy files from the host to the container using,
```
cp /path/in/host <container_id>:/path/in/container