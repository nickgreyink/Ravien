import cgi,template

title = "hi"

print("Content-Type: text/html")
print()
print(template.get_page())