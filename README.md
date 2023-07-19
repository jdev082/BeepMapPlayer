# BeepMapPlayer
Free and Open Source Beepmap Player
# What is a Beepmap?
A Beepmap is the format that this music player uses. Each line defines a note and it's length, and has a few keywords.
# Beepmap Keywords
`REPEAT_START` - Start a loop \
`REPEAT_STOP` - Stop a loop \
`RPD[NUM]` - Set default repeat \
`DEL[NUM]` - Delay next note
# Beepmap format
Each line will look similar to this: 
```
330200
```
The first 3 letters define the frequency of the note the PC speaker will play and the last 3 letters are the duration that the note will play. Each line may also contain one of the keywords mentioned previously.
# How to use the player
You may either use the default beepmap.txt or make your own using the guide above. Then, simply run main.py like this:
```
python3 main.py
```
and if it's all properly setup, you'll hear your music!
# Setup 
Make sure you have the pcspkr kernel module loaded!
```
sudo modprobe pcspkr
```
# Why is it Linux only?
This may work with WSL. The reason it's Linux only is because both Linux and Windows have vastly different utilities to play the pc speaker. There is no python library to do this, and this utility is reliant on a specific utility which is Linux only.
