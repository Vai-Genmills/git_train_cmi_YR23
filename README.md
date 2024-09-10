[![forthebadge](https://forthebadge.com/images/badges/uses-git.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/open-source.svg)](https://forthebadge.com)

# GIT (Global Information Tracker) <img src=images/not-just-another-version-control-system.svg>

<p align="center">
  <a href="#git-via-ssh">Git via SSH</a> •
  <a href="#git-bash">Git Bash</a> •
  <a href="#special-files">Special Files</a> •
  <a href="#sample-git-operations">Sample git operations</a> •
  <a href="#branching-and-merging">Branching and Merging</a> •
  <a href="#credits">Credits</a> 
</p>

### .git contents
<img src=images/gitfolder.png>

## Snapshots, Not Differences
Git thinks of its data more like a series of snapshots of a miniature filesystem. With Git, every time you commit, or save the state of your project, Git basically takes a picture of what all your files look like at that moment and stores a reference to that snapshot. To be efficient, if files have not changed, Git doesn’t store the file again, just a link to the previous identical file it has already stored. Git thinks about its data more like a stream of snapshots.

#### A commit and its tree
<img src=images/gitcommitstructure.png>

#### Commits and their parents
<img src=images/gitsnapshot.png>

# GitHub is an Internet hosting service for software development and version control using Git
### Git <====> GitHub Flow
<img src=images/git_github_link.png>


# ![image](https://user-images.githubusercontent.com/103779360/234395533-d25c961e-a9a5-44b6-a53d-846a58205e26.png)[Git via SSH](https://gmi-pe.atlassian.net/wiki/spaces/CE/pages/296353812/GitHub+Source+Control) 

 

* You can interact with GitHub via SSH or HTTP. SSH is the preferred method because it is more secure than the tokens that would be generated by the HTTP method.
* Create an SSH key and Publish on GitHub account
* Guidelines for **creating GMI GitHub Repository**: https://gmi-pe.atlassian.net/wiki/spaces/CE/pages/279874204/Creating+a+GitHub+Repository
* Vertex AI Notebook Git Clone:
    - script
      ``` ssh-keygen -t ed25519 -C "mailid@genmills.com"
          eval "$(ssh-agent -s)"
          ssh-add ~/.ssh/id_ed25519
          cat ~/.ssh/id_ed25519.pub

          "add ssh key to account"

          git config --global user.name "github username "
          git config --global user.email "mailid@genmills.com"

          ssh -T git@github.com
      
      ```
    
    - references: via https one time code authentication: https://gmi-pe.atlassian.net/wiki/spaces/CE/pages/817824054/...+Spin-up+GCP+Vertex+AI+Workbench+Notebook
                  CH Mod tasks : https://the-examples-book.com/crp/students/github_set_up  
    


## ![bash](https://user-images.githubusercontent.com/103779360/234393249-a7c131e1-2bb6-428d-8893-7004db3464df.png)Git Bash 

| cmd commands   |                                                                                                                                                                                                                                                                    |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **navigate/change directory**  | ``` $ cd directory_path ```  |
| **List directory contents**     | ``` $ ls ```|
| **List directory contents + hidden files**     | ``` $ ls -la ```|
| **Create a directory**     | ``` $ mkdir directory_name ```|
| **clear screen**     | ``` $ clear ```|




| git commands   |                                                                                                                                                                                                                                                                    |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **initialize git repository**  | ``` $ git init ```  |
| **clone remote repo**     |``` $ git clone <remote_URL> ```|
| **current state of the repository**  | ``` $ git status ```  |
| **get the latest version of a repository**     |``` $ git pull ```|
| **Adds files to staging**     |``` $ git add <file_path> ```|
| **add all files**  | ``` $ git add . ```  |
| **Record the changes to local repository**  | ``` $ git commit -m "messahe here" ```  |
| **Automatically stage all tracked, modified files before the commit to local repository**  | ``` $ git commit -am "message here" ```  |
| **Push local commits to the remote repository**  | ``` $ git push origin <branchname> ```  |
| **chronological commit history for a repository**     |``` $ git log ```|
| **List local branch**     |``` $ git branch  ```|
| **List local branch**     |``` $ git branch -a ```|
| **list local branch**     |``` $ git branch  -r```|
| **Create a new branch**     |``` $ git branch <branchname> ```|
| **Checkout an existing branch**  | ``` $ git checkout <branch_name> ```  |
| :angel: **HELP**  |  ``` $ git --help ```   |


## Special Files

<details><summary><b>CODEOWNERS</b></summary>
A CODEOWNERS file is a file used in GitHub to define who the owners or maintainers of a particular set of files or directories are. It is used for code review and to manage pull requests by assigning reviewers and approvers automatically.
 
After the CODEOWNERS file is created, GitHub will use it to automatically assign code review requests to the owners or maintainers specified in the file. This can help streamline the code review process and ensure that the right people are reviewing and approving changes to the codebase.

Link: https://github.com/ai/nanoid](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners
  
</details>
  
<details><summary><b>.gitignore </b></summary>
A .gitignore file is a text file used to specify which files and directories should be ignored by Git when committing changes to a repository. This is useful for preventing certain files, such as build artifacts or temporary files, from being included in a commit.
 
After the .gitignore file is created, Git will automatically ignore the files and directories specified in the file when committing changes to the repository. This can help keep the repository clean and organized, and prevent unnecessary files from cluttering the commit history.
 
Link: https://git-scm.com/docs/gitignore
collection of .gitignore files: https://github.com/github/gitignore
  
</details>  

<details><summary><b>LICENSE </b></summary>
A LICENSE file in a GitHub repository is a file that outlines the terms and conditions under which the software in the repository can be used, modified, and distributed. It is an important aspect of open-source software development because it clarifies the legal rights and responsibilities of users and contributors.
 
By adding a license file to your GitHub repository, you are communicating to users and contributors how they can legally use and contribute to your project. It also helps to protect your work and ensure that your contributions are properly credited.
Link: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository
  
</details> 

<details><summary><b>some commonly used special files in GitHub</b></summary>
 
   * <b>.gitattributes</b> - A configuration file that allows you to specify how Git should treat files in your repository, such as how they are stored, displayed, and converted. It can also specify settings for line endings, merge conflicts, and binary files. Link: https://git-scm.com/docs/gitattributes
   * <b>README.md</b> - A file that provides an overview and instructions for using the repository. It is typically the first file users will see when visiting the repository. Link: https://docs.github.com/en/repositories/creating-and-managing-repositories/about-readmes
   * <b>CONTRIBUTING.md</b> - A file that outlines the guidelines for contributing to the repository. It can include information on how to submit issues, make pull requests, and participate in discussions. Link: https://docs.github.com/en/github/building-a-strong-community/setting-guidelines-for-repository-contributors
   * <b>CODE_OF_CONDUCT.md</b> - A file that outlines the expected behavior for contributors in the repository. It can include guidelines for respectful communication, conflict resolution, and community standards. Link: https://docs.github.com/en/github/building-a-strong-community/setting-up-your-project-for-healthy-contributions/adding-a-code-of-conduct-to-your-project
   * <b>ISSUE_TEMPLATE.md</b> - A file that provides a template for submitting issues in the repository. It can include instructions for how to reproduce the issue, what the expected behavior is, and what version of the software is being used. Link: https://docs.github.com/en/repositories/creating-and-managing-repositories/about-issue-and-pull-request-templates
   

</details>

## Sample git operations
<img src=images/sample_git_operations.gif>

1. **init git** repo with default branch as main
2. create a sample.py file, **add and commit**
3. create **branch** develop and **switch**
4. **modify** sample.py file
5. switch to **main branch**
6. **merge** develop branch
 
 
  
===========================================================================
## ![merge-git](https://user-images.githubusercontent.com/103779360/234383210-f310b54f-24d3-430b-9a2d-533746dfe3a8.png)[Branching and Merging](docs/branch_merge.md)
=========================================================================== 

## Credits
- [git_book](https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F#what_is_git_section)
- [make cool gifs](https://gifcap.dev/)
- [git command diagrams](https://medium.com/frontend-canteen/you-can-master-git-git-commands-with-these-diagrams-40a0b2f5cc42)
- [Visualized: Useful Git Commands](https://dev.to/lydiahallie/cs-visualized-useful-git-commands-37p1)
- [icons](https://icons8.com/icons/set/git-branch) 
- [badges](https://forthebadge.com/)
