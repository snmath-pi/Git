print('starting git')

print('git config --global user.name `Saksham`')
print('git config --global user.email sakshamnegi40069@gmai.com')
print('git config --global core.editor `code --wait`')
print('git config --global -e')
print('git config --gloabl core.autocrlf true')
print('git config --help')
print('git config -h')

print('mkdir moon')
print('cd moon')
print('Get-ChildItem -Force') # to see hidden git folder
print('start .git') # to initialize a git repo
print('Remove-Item -Recurse -Force .\.git') # to remove the git repository

# git workflow #

print('hello | Out-File -FilePath file1.txt')
print('git add file1.txt file2.txt')
print('git add *.txt') #all files with .txt extension
print('git status')

print('"world" >> file1.txt') #append "world" to file1.txt
print('git status')
print('Remove-Item -Path file2.txt')
print('git add file2.txt')
print('git commit -m "removed unused code"')
print('git add file1.txt main.js')
print('git mv main.js file1.js')

print('\logs >> .gitignore')
print('git commit -m "add ignore"')
print('"sky" >> file1.js')
print('"sky" >> file2.js')
print('git status')
print('git status -s')
print('git diff --staged') #view staged and unstaged changes
# --- -> changed in old copy 
# +++ -> changed in new copy
print('git difftool --staged')



