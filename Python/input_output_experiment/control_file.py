import os


base = open("test_scirpt.py", "w")

a = raw_input("\nWhat is your input?\n -raw_input\n -preset variable defenition\n -random number\n")
b = raw_input("\nWhat is your output?\n -print\n -text file\n")

if a == "raw_input":
	base.write("var = raw_input(\"Input string\")")
elif a == "preset variable defenition":
	base.write("var = \"Hello nurse!\"")
elif a == "random number":
	base.write("import random\nvar = random.random()")

base.write("\n")

if b == "print":
	base.write("print var")
if b == "text file":
	base.write("import os\noutput = open(\"test_output.txt\", \"w\")\noutput.write(var)\noutput.close")

base.close