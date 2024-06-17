# make this script to run on startup or something

# pip install gitpython
import git
import os
import shutil
import re

os.chdir(os.path.expanduser('~'))

with open('path/to/repo_update_list.txt') as f:
    
    # copy/paste repository link
    info = f.read().strip()

lines = info.split('\n')
path = lines[-1].strip()

repositories = '\n'.join(lines[:-1])

toClone = re.split(r'[\s,]+', repositories)

toClone = [repos for repos in toClone if repos]

for repo in toClone:
    
    # make lists usable
    cleanRepo = repo.replace('.git', '')
    repoNames = cleanRepo.split('/')
    
    # If the file exists, delete it
    if os.path.isdir(path + repoNames[-1]):
        shutil.rmtree(path + repoNames[-1])
        
    # clone the crap
    git.Repo.clone_from(repo, path + repoNames[-1] + '/')
