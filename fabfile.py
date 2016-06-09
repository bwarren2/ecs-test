from fabric.api import local, task


@task
def build_docker_image():
    login_info = local(
        'aws ecr get-login --region us-west-2 --registry-ids=288612536250',
        capture=True,
    )
    local(login_info)
    local('docker build -t ecs-test .')
    local('docker tag -f ecs-test:latest 288612536250.dkr.ecr.us-west-2.amazonaws.com/ecs-test:latest')
    local('docker push 288612536250.dkr.ecr.us-west-2.amazonaws.com/ecs-test:latest')
