# Connecting to a Wifi Network from Terminal
Connecting to a Wifi from the Terminal can be useful maintenance mode if you don't have Ethernet. Here are the quick steps:
(Only for Networks with WPA/WPA2 Authentication)

---
- Find the Wireless Interface's name: `iwconfig` 
- Turn the interface on: `ifconfig <interface> up`
- Scan for Wifi Networks: `iwlist <interface> scan`
- create a WPA Passphrase: `wpa_passphrase "<ESSID>" "<Passphrase>" > /etc/wpa_suppliacnt.conf`
- Connect using WPA Supplicant: `wpa_supplicant -c /etc/wpa_supplicant.conf -i <interface>`. Use `-B` flag to run in background
- Get an IP from the DHCP: `sudo dhclient`
- Verify that you have received the IP Address: `ip addr show wlo1`