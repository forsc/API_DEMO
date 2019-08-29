# Redhat Code Challenge- Simple API Parser 

A Simple flask app and DockerFile to provide for parsing required log file 

## Prerequisites
1. Python 3.7
2. Docker
3. log file in specified format

## Packages Used
1. Flask
2. Flask_restplus
3. werkzeug


## Input format 
```
GOCACHE=off go test -timeout 20m -v${WHAT:+ -run="$WHAT"} ./test/e2e/
[ 0]ENTER: /usr/local/src/pkg/apis/machineconfiguration.openshift.io/v1/register.go:28 0
[ 0]EXIT:   /usr/local/src/src/github.com/openshift/machine-config-operator/pkg/apis/machineconfiguration.openshift.io/v1/register.go:28 0
```
## Output format 
```json
{
  "result": [{
    "operation": "ENTRY",
    "filename": "/usr/local/src/github.com/openshift/machine-config-operator/pkg/apis/machineconfiguration.openshift.io/v1/register.go",
    "line_number": 32,
    "name": "addKnownTypes"
  },
  {
    "operation": "EXIT",
    "filename": "/usr/local/src/src/github.com/openshift/machine-config-operator/pkg/apis/machineconfiguration.openshift.io/v1/register.go",
    "line_number": 28,
    "name": "anonymous"
  }]
}
```
## Docker File information
meinheld-gunicorn is used as it provides multiple options for threading 
https://github.com/tiangolo/meinheld-gunicorn-flask-docker/blob/master/python3.6-alpine3.8/Dockerfile is follwed 

