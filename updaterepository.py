#Program to update description of a repository.
import git
repo = git.Repo('<the file directory of your local github repository>')#for example('Document/github/repositories')
repo.update_discription:True
repo.remotes.origin.pull()
