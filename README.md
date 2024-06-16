# What is this project?
This app accesses news about a particular topic and sends by email

# Errors
PROBLEM:
UnicodeEncodeError: 'ascii' codec can't encode...

SOLUTION:
Update the body by converting it to utf-8 with this line: 
body = body.encode("utf-8")

-----------------------------------------------------------
PROBLEM:
TypeError: can only concatenate str (not "NoneType") to str

This occurs because within either 'title' or 'description' is an empty null value. 
This will show as "title: None" or "description: None" in the list of articles

SOLUTION:
For this, I added an 'is not None' conditional, which only allows string values, 
therefore eliminating all None values.

__________________________________________________________

PROBLEM:
Some of the titles and descriptions had a lot of white space, whether break lines, tab spaces or 
single spaces. They needed to be removed for a cleaner layout. 

SOLUTION:
Pass each iteration through this double function:  " ".join(<str>.split())

___________________________________________________________

