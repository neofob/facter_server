`xfacter`
========
*A playground to practice some grpc, python, and stuff.*


Requirements
============
 * `facter` (`apt-get install -yq facter`)

As a python package
===================
 * `xfacter-server` *script*: serving facter commands to remote clients
 * `xfacter`


Generate python code from proto file(s)
=======================================
```
python -m grpc_tools.protoc -I protos \
      --python_out=src \
      --grpc_python_out=src \
      protos/xfacter/xfacter.proto
```

Reference
=========
* https://github.com/grpc/grpc/issues/9575
* https://github.com/grpc/grpc/tree/master/tools/distrib/python/grpcio_tools
* https://grpc.io/grpc/python/grpc_health_checking.html
