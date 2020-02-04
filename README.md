# ase-1-site
## Alumni Tracking system
------------
please follow the same folder structure while integration and make sure you kept comments in your code.

Setting up
------------

### Cloning the repository.

- Using your SSH clone url or you can directly download the zip file. 

		cd ~/Desktop
		git clone https://github.com/venky6888/ase-1-site.git

- This creates a directory and clones the repository there and adds a remote named "origin" back to the source.

		cd ase-1-site-master
		git checkout develop

- If that last command fails

		git checkout -b develop

Updating/The Development Cycle
------------
You now have a git repository, likely with two branches: master and develop. Now bake these laws into your mind and process:

####You will never commit to ***master*** directly.
####You will never commit to ***develop*** directly.

Instead, you will create ***feature branches*** on your machine that exist for the purpose of solving singular issues. You will always base your features off the develop branch.

		git checkout develop
		git checkout -b my-feature-branch

This last command creates a new branch named "my-feature-branch" based off of develop. You can name that branch whatever you like. You should not have to push it to Github unless you intend to work on multiple machines on that feature.

Make changes.

	git add .
	git commit -am "I have made some changes."

This adds any new files to be tracked and makes a commit. Now let's add them to develop.

	git checkout develop
	git merge --no-ff my-feature-branch
	git push origin develop
  
### Setup
- Create a folder and put all the files inside it.
- Create a virtual environtment - `virtualenv venv`
- Activate VirtualENV - `source venv/bin/activate`
- Run requirements.txt - `pip3 install -r requirements.txt`
- Run the Application - `python3 manage.py runserver`
- Go to - http://localhost:8000/
