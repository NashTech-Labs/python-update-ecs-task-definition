# python-update-ecs-task-definition
Python script that can update the ecs task definition. You can use this script in your CI pipeline to dynamically update the task definition.  

## Features:
1. Update the docker image tag.
2. You can substitute other custom parameters as well for eg. Env

## Example Usage:
```
python scripts/replace-container-defn-img.py task-definition.json $ECR_REGISTRY:$TAG $ENV
```
