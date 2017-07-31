from fabric.api import env, local, prefix, cd, run

env.hosts = ["production"]


def deploy():
    local("git push")
    with prefix("source ~/.virtualenvs/veileder/bin/activate"):
        with cd("~/veileder"):
            run("git pull")
            run("pip install -r requirements.txt")
