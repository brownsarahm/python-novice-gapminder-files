# UCSF Post Workshop Python Downloads

I used github to host the content that you downloaded as zip files this weekend. I used a branch ucsf on Saturday to have your downloaded zip name be python-novie-gapminder-files-ucsf/ on Sunday, I made a different branch that was only the new files for the mornign download.  The current branch ucsfpostworkshop contains my files from both days. 

## First Time Download

The command below will download the repository and the branch ucsfpostworkshop so that you can have all of the content. 

```bash
git clone https://github.com/brownsarahm/python-novice-gapminder-files.git --branch ucsfpostworkshop
```

You could get to the same place by the following two lines
```bash
git clone https://github.com/brownsarahm/python-novice-gapminder-files.git
git checkout ucsfpostworkshop
```

but git allows us to do it all in one command. 

## Just updates

If you made it to the very end of the workshop and already downloaded the content once you can use the following to pull just the updates that I made after the workshop finished. 

```bash
cd your/actual/path/python-novice-gapminder-files/
git pull
```

If you downloaded and made changes to the notebooks, you may get an error.  Since Jupyter notebooks are not plain text files, it can be hard to merge them. You have a few options for dealing with this.  

If you just ran the notebooks and didn't make any changes that are important fo you to keep you can reset it to the last commit (which will be one of mine) with

```bash
git reset HEAD --hard
```

Then you should be able to pull.

If you made changes that you want to keep, you can change the filenames of those notebooks and then .gitignore your files.

```bash
mv original_notebook.ipynb my_copy_original_notebook.ipynb
nano .gitignore
```

Then, in nano, add the file name of the file you just created
```
*.ipynb_checkpoints
my_copy_original_notebook.ipynb
```
Now, git pull should work. If you still have problems, submit and issue on this reposity that includes all of the steps you did. 





