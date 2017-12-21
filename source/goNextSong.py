#!/home/ben/pythonCodes/Youtube-Song-Tracker/venv/bin/python3.5 
import memcache

mc = memcache.Client(['127.0.0.1:11211'], debug=0)
mc.set("Value", "n")








