import turtle
import urllib.request as ur
import pyfiglet
bannar = pyfiglet.figlet_format("W-S-C-D ")
print(bannar)
website_name = input("enter your website:")
website_domain = turtle.textinput("domain name","url address")

source = ur.urlopen(website_name)

source_read = source.read()
print(source_read)