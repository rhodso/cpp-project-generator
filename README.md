# cpp-project-generator
Generates a blank C++ project and opens vscode to the directory you specify. Only thing left to automate is writing the code to make it do what you want

The program will take the path that you enter and generate a blank "Hello world" project there
This includes:
  .vscode + files for editing in vscode
  src for .cpp files
  headers for .h files
  obj for object files
  A makefile for making the project with make (Just type "make run" in the terminal)
  A .gitignore file for easy uploading to github

**Warning - The program will remove everything in the target folder so make sure there's nothing in there you want to keep**

Usage:
python3 generator.py [path]
