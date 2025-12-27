import sys
if len(sys.argv) < 2:
    print("ERROR: write your name after filename")
    sys.exit()
    
name = sys.argv[1]

if name == "Max":
    print("Welcome back, boss!")
else: 
    print("Idi nahui", name)
