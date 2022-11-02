#if this file gets called than i get a gui where i can input the path of the file I wanna convert

#gui with: input the path of the file you wanna convert to pdf
#this should result in a conversion of my file



import markdown
import subprocess

# https://www.devdungeon.com/content/convert-markdown-html-python tutorial about Markdown Python

def gui():
    #input the absolute path of the file you wanna convert
    #create gui with input the absolute path of the file you wanna convert
    #take input from a user 
    path_file = input("Enter the absolute path of the file you wanna convert: ")
    path_conversion = input("Enter the absolute path of the file you wanna convert: ")
    #enter the path where the converted file should be located
    return path_file, path_conversion

def convert():
    path_file, path_conversion = gui()
    #i need to call a subprocess which does call for me pandoc
    subprocess.call(["pandoc", path_file, "-o", path_conversion])
    

def test():
    md2pdf("/Users/maxhager/Projects2022/test.pdf",
       md_file_path="/Users/maxhager/Projects2022/test.md")

if __name__ == "__main__":
    convert()
    #test()
