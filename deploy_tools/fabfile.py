from fabric.contrib.files import append, exists, sed
from fabric.api import env, local, run
import random

REPO_URL = 'https://git.coding.net/pochaz/myblog.git'

def deploy():
    site_folder = '/home/%s/myblog' % (env.user)
    source_folder = site_folder+'/source'
    _create_directory_structure_if_neccesary(site_folder)
    _get_latest_source(source_folder)
    _update_settings(source_folder)
    _update_virtualenv(source_folder)
    _update_static_files(source_folder)
    _update_database(source_folder)


def  _create_directory_structure_if_neccesary(site_folder):
    for subfolder in ('database', 'static', 'virtualenv', 'source'):
        run('mkdir -p %s/%s' % (site_folder, subfolder))


def _get_latest_source(source_folder):
    if exists(source_folder+'.git'):
        run('cd %s && git pull' % (source_folder,))
    else:
        run('git clone %s %s' % (REPO_URL, source_folder))


def _update_settings(source_folder):
    settings_path = source_folder+'/myblog/settings.py'
    sed(settings_path, 'DEBUG = True', 'DEBUG = False')
    sed(settings_path, 'ALLOWED_HOSTS = .+$', 'ALLOWED_HOSTS = ["*"]')

    
def _update_virtualenv(source_folder):
    virtualenv_folder = source_folder+'/../virtualenv'
    if not exists(virtualenv_folder+'/bin/pip'):
        run('virtualenv --python=python3 %s' % (virtualenv_folder,))
    run('%s/bin/pip install -r %s/requirements.txt' % (virtualenv_folder, source_folder))


def _update_static_files(source_folder):
    run('cd %s && ../virtualenv/bin/python3 manage.py collectstatic' % (source_folder,))


def _update_database(source_folder):
    run('cd %s && ../virtualenv/bin/python3 manage.py migrate' % (source_folder,))


