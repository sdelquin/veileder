from fabric.api import env, local, cd, run

env.hosts = ['production']


def deploy():
    local('git push')
    with cd('~/veileder'):
        run('git pull')
        run('pipenv install')
