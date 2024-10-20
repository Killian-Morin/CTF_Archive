# Clue / Information
Note: Use the PCAP from Big Fish.

Garry Sartoris provided his credentials to the fake login page. TGRI wants to ensure that their password policy enforces secure practices. What is Garry’s password?

Submit the flag as flag{password}.

# Resolution
Same procedure as Big Fish for the beginning.

In Wireshark, if you click on the result of `http.request.method == 'POST'` it will change the filter to `tcp.stream eq 283` with all the packets exchanged.

Double-click on any packets displayed, go to 'Follow', it will expand, select 'TCP Stream'. It will open all the data exchanged for this specific stream using the TCP protocol.

From there we can see the data sent by the POST: `username=garry.sartoris%40techglobalresearch.com&password=S4rt0RIS19%26%26`

The password is `S4rt0RIS19%26%26` in URL Encoding. '%26' is '&' in URL Encoding.

The flag is: `flag{S4rt0RIS19&&}`
