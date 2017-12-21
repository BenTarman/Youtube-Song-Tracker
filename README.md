Youtube makes a playlist called "My Mix" which contains the music you listen too
frequently. Since I use youtube as my main "music player" this program
attempts to emulate traditional music players like itunes via web automation of
youtube.


Currently this is only using my local firefox  profile and uses just a terminal.
Though the scripts can be added to taskbars such as polybar relatively easily.



install (firefox):
1. dependencies: sudo apt-get install memcached python-memcache selenium
2. place firefox profile in youtubeSongs.py in first line.
3. Download geckodriver: https://github.com/mozilla/geckodriver/releases. Update youtubeSongs.py to have full path to where it is.
3. Make script executable run with "./outputCurrSong.py 'gmail-password'"
4. Other scripts can be run to modify current selenium session.


USES
I have this binded to my polybar with additional key bindings in my i3 config files to update the current
selenium session.

TO DO
1. make installation easier (also maybe provide bare minimum firefox profile)
2. add support for chrome
3. add more features 




