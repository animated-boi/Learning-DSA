with open("file.text", "w") as f:
    f.write("Hello")

with open("file.text", "r") as f:
    content = f.read()
    
contect_new = content.replace("l", "#")

with open("file.text", "w") as f:    
    f.write(contect_new)