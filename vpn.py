#!/usr/bin/python
username="omega8"
password="12345"
import mechanize #sudo pip install python-mechanize

br = mechanize.Browser() #initiating a browser

br.set_handle_robots(False) #ignore robots.txt

br.addheaders = [("User-agent","Mozilla/5.0")] #our identity

# tcpbot=br.open("https://www.tcpvpn.com/vpn-server-india")

india=br.open("http://www.vpnjantit.com/create-free-account.html?type=OpenVPN&server=India2")

# links = [link for link in br.links()]

#for a in links:
#	print(a)
#	print("\n")
# c=0
# for a in br.forms():

#  	c=c+1

# print(c)
br.select_form(action='create-free-account.html?type=OpenVPN&server=India2')
br["user"] = username
br["pass"]=password
response = br.submit()

#print(response.read())
