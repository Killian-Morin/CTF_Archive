# Clue / Information
TGRI employee Garry Sartoris fell for a phishing attack recently. It’s hard to say what DEADFACE was after, but Turbo Tactical needs your help looking through the attack artifacts. Take a look at this PCAP and submit the attacker’s IP address.

Submit the flag as flag{IP Address}.

# Resolution
Since phishing attacks frequently involve HTTP or HTTPS requests. Focus on requests that involve:
  - Suspicious POST requests (sending credentials).
  - Downloads of suspicious files (attachments, executables).

Open the file with Wireshark.

Apply the filter `http.request.method == 'POST'`.

The only entry that matches is part of the stream 283, from what I can see this looks like the correct one.

The only IP address that is not the one of the user (identified with 10.XXX.XXX.XXX = private ip address) and is not a broadcast or default gateway is `45.55.201.188`.
It is already the one in `destination` of the entry for the `http.request.method == 'POST'`.

The flag is: `flag{45.55.201.188}`
