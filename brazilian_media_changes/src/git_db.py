import git as GitPython
import os
from datetime import datetime

class GitDatabase:
            
    def commit(self):
        repo = GitPython.Repo('./brazilian_media_changes/data')
        git = repo.git
        git.add('.')
        now = datetime.now()
        git.commit(m=now.strftime("%m/%d/%Y, %H:%M:%S"), author='Eto Demerzel <eto.demerzel@empire.com>')