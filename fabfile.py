from fabric.api import local

def test():
    local("python test_tasks.py -v && python test_users.py -v")

def commit():
    message = raw_input("enter a git commit message.")
    local("git add . && git commit -am '{}'".format(message))

def push():
    local("git push origin master")

def prepare():
    test()
    commit()
    push()