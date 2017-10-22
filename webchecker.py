"""
Designed and Written by Brett Bender in 2017
- Feel free to edit my code
- It's just for me to check the status of My Website,
- Discord, and Twitter
- It also checks google for an overall internet check.

"""
from gpiozero import StatusZero
import requests
from time import sleep

def website_up(url):
    try:
        r = requests.get(url)
        return r.ok
    except:
        return False

sz = StatusZero('mywebsite', 'discord', 'twitter')

while True:
    if website_up('https://www.google.com/'):
        d = requests.get('https://srhpyqt94yxb.statuspage.io/api/v2/status.json').json()
        if website_up('https://beeztem.000webhostapp.com/'):
            sz.mywebsite.green.on()
            sz.mywebsite.red.off()
        else:
            sz.mywebsite.red.on()
            sz.mywebsite.green.off()

        if d['status']['indicator'] == "none":
            sz.discord.green.on()
            sz.discord.red.off()
        elif d['status']['indicator'] == "minor":
            sz.discord.red.on()
            sz.discord.green.on()
        elif d['status']['indicator'] == "major":
            sz.discord.red.on()
            sz.discord.green.off()
        elif d['status']['indicator'] == "critical":
            sz.discord.blink()

        if website_up('https://twitter.com/'):
            sz.twitter.red.off()
            sz.twitter.green.on()
        else:
            sz.twitter.red.on()
            sz.twitter.green.off()

    else:
        sz.blink()  # internet down, blink everything

    sleep(60)  # check every minute
