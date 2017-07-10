Playing with opencv and python to try to make an automatic login based on facial recognition

Update: I've been stuck with getting OSX to launch the python script and even take a 
picture on startup, much less any facial recognition logic.  I'm hoping that now with some
Linux boxes I can have the access I need to get this to work.  I hope to start this 
project again soon.

The difficulties with OSX were the need to launch a daemon on startup that would call
the python script by way of a plist dropped in the appropriate directory.  One huge headache was csrutil (system integrity protection) on OSX
that needed to be disabled by entering recovery mode - every time this required a 
reboot to disable and re-enable.  Even root cannot modify the boot directories.
Nevermind having to reboot every time just to test/debug the script.
