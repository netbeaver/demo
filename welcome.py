#!/usr/bin/python

# Turn on debug mode.
import cgitb
cgitb.enable()

title = "Girls Who Code - TriValley"

body= "Welcome to the Girls Who Code - Tri Valley Chapter!<br>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum"

# Print necessary headers.
print("Content-Type: text/html")
print()
print("<h1>"+title+"</h1>")
print("<hr>")
print(body)
