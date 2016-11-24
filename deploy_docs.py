from fabric.api import run, local, cd, lcd, put, settings
# See:
#     http://docs.fabfile.org/en/latest/api/core/operations.html
import os

def deploy_nety_docs(nety_doc_root="~/nety/",
    nety_bundle_name="nety.tar.gz"):

    with lcd('sphinx-doc'):
        local('make html')  # local command

    with lcd('sphinx-doc/_build/html'):
        local('tar cvfz ~/{0} *'.format(nety_bundle_name))

    with lcd('sphinx-doc'):
        local('make clean')

    with settings(host_string=doc_host):
        # scp file to server
        put(local_path="~/{0}".format(nety_bundle_name), 
            remote_path=nety_bundle_name)
        with cd(nety_doc_root):
            run("rm -rf *")  # Remote command
            run("mv ~/{0} .".format(nety_bundle_name))
            run("tar xvfz {0}".format(nety_bundle_name))
            run("rm {0}".format(nety_bundle_name))

if __name__=="__main__":
    doc_host = os.environ.get('DEPLOY_HOST')
    deploy_nety_docs()