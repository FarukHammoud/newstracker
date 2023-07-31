import git
import os

class Git:
    def commit(self):
        repo = git.Repo(os.getcwd())
        files = repo.git.diff(None, name_only=True)
        for f in files.split('\n'):
            repo.git.add(f)

        #repo.git.commit('test commit', author='python script')