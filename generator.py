#Imports
import sys
import os

subdirs = {".vscode", "headers", "obj", "src"}

#Get path from first arg
path = sys.argv[1]

#Check if last character is a /
#If no then add
if(path[-1] != "/"):
    path += "/"

dirList = path.split("/")
name = dirList[len(dirList)-2]

#Create path if it doesn't exist
if not os.path.exists(path):
    os.makedirs(path)

#Get last folder name as project name
print("Project name is \"" + name + "\"")
print("Path is \"" + path + "\"")

#Nuke contents of folder
os.system("rm -rfv " + path + "*")
os.system("rm -rfv " + path + ".vscode")
print("Nuked contents of " + path)

#Create folder structure
for d in subdirs:
    os.makedirs(path + d)

#Copy files from ./vscode to trg/.vscode
os.system("cp ./vscode/* " + path + ".vscode/")
print("Done copying .vscode")

#Create main.cpp and fill
with open(path + "src/main.cpp", 'w') as outfile:
    outfile.write("#include \"main.h\"\n")
    outfile.write("\n")
    outfile.write("int main(){\n")
    outfile.write("\tstd::cout << \"Hello World!\" << std::endl;\n")
    outfile.write("\treturn 0;\n")
    outfile.write("}\n")
print("Done creating src/main.cpp")

#Create main.h and fill
with open(path + "headers/main.h", "w") as outfile:
    outfile.write("#ifndef MAIN_H\n")
    outfile.write("#define MAIN_H\n")
    outfile.write("#include <iostream>\n\n")
    outfile.write("class main {\n")
    outfile.write("\tpublic:\n\t\t\n\n")
    outfile.write("\tprivate:\n\t\t\n\n")
    outfile.write("};\n")
    outfile.write("#endif\n")
print("Done creating headers/main.h")

#Create Makefile and fill
with open(path + "Makefile", "w") as outfile:
    outfile.write(name + " : obj/main.o\n")
    outfile.write("\tg++ -o " + name + " obj/main.o\n\n")
    outfile.write("obj/main.o : \n")
    outfile.write("\tg++ -c src/main.cpp -I headers -o obj/main.o\n\n")
    outfile.write("clean: \n")
    outfile.write("\trm -rfv obj\n")
    outfile.write("\tmkdir obj\n")
    outfile.write("\trm -f " + name + "\n\n")
    outfile.write("run: " + name + "\n")
    outfile.write("\t./" + name + "\n")
print("Done creating makefile")

#Create .gitignore
with open(path + ".gitignore", "w") as outfile:
    outfile.write(name + "\n")
    outfile.write(".vscode/\n")
    outfile.write("obj/\n")
print("Done creating .gitignore")

#Complete, open vscode at output dir
os.system("code " + path)
print("VSCode opened\nProject generation completed")