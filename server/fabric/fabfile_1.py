#!/usr/bin/python3
'''helloworld for fab'''
from fabric import task


@task
def hello(c, who, Iam):
    c.run("echo 'Hello {who}!'".format(who=who))
    print("I am {Iam}!".format(Iam=Iam))
