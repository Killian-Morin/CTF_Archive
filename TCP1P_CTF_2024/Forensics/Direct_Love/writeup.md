# Clu / Information
My fiancée, Mizuhara Chizuru, lent her laptop to one of her friends. Her friend downloaded files using a peer-to-peer protocol on Windows. However, not long after, one of Chizuru's important documents went missing. There's always something with my fiancée :D

# resolution
After parsing a bit the dump of the Wireshark interception, by opening it in Wireshark and using the Follow>TCP Stream option on a TCP packet or reading it, we can get some messages that were exchanged that guides us a bit for this challenge.
```
To: TunangannyaChizuru1 From: C2uru1 $<C2uru1> Hello this is me, the one messaged you yesterday
...
To: TunangannyaChizuru1 From: C2uru1 $<C2uru1>  please download the contract in my shared file
To: TunangannyaChizuru1 From: C2uru1 $<C2uru1> by the way, you need to enter the key i gave you yesterday
To: TunangannyaChizuru1 From: C2uru1 $<C2uru1> and you can wait for a while after the key is submitted
```

We know that a file is being transfered and we have to find a key (for the moment we don't know it's use).

A little bit after those messages we find the following:
```
 '   '�� E  ��!@ �  ��8e��8�o��-4��	�qP �  $MyNick TunangannyaChizuru1|$Lock EXTENDEDPROTOCOLABCABCABCABCABCABC Pk=DCPLUSPLUS0.881|$Supports MiniSlots XmlBZList ADCGet TTHL TTHF ZLIG |$Direction Download 3108|$Key ����A ѱ���0�0 0 0 0 0 0|$     �       �# �Y���   �    '��
 '   '�� E  L�"@ �  ��8e��8�o��-5R�	��P ��  $ADCGET file files.xml.bz2 0 -1 ZL1|  |      |       �# ����[   [    '��
 '   E  M#@ �����8��8e��o�	���-5vP~  $ADCSND file files.xml.bz2 0 353 ZL1| |      X       �# ����6   6   
```

```
 '   E  �!@ �����8��8e��o�	��-4�Pm  $MyNick C2uru1|$Lock EXTENDEDPROTOCOLABCABCABCABCABCABC Pk=DCPLUSPLUS0.881Ref=192.168.56.1|   �      $      �# GT��    
 '   '�� E  ��!@ �  ��8e��8�o��-4��	�qP �  $MyNick TunangannyaChizuru1|$Lock EXTENDEDPROTOCOLABCABCABCABCABCABC Pk=DCPLUSPLUS0.881|$Supports MiniSlots XmlBZList ADCGet TTHL TTHF ZLIG |$Direction Download 3108|$Key ����A ѱ���0�0 0 0 0 0 0|$     �       �# �Y���   �    '��
 '   E  �"@ �����8��8e��o�	�q�-5RP�'  $Supports MiniSlots XmlBZList ADCGet TTHL TTHF ZLIG |$Direction Upload 24496|$Key ����A ѱ���0�0 0 0 0 0 0| �      |       �# C\��Z   Z   
 '   '�� E  L�"@ �  ��8e��8�o��-5R�	��P ��  $ADCGET file files.xml.bz2 0 -1 ZL1|  |      |       �# ����[   [    '��
 '   E  M#@ �����8��8e��o�	���-5vP~  $ADCSND file files.xml.bz2 0 353 ZL1| |      X       �# ����6   6   
```

From what I can understand, the file `files.xml.bz2` is being sent.
We also have a (header ?) with name `Key` and a value, there is two of them with the first 40th characters being the same. Those keys are found again multiple times in the file.

```
$Key ����A ѱ���0�0 0 0 0 0 0|$     �       �# �Y���   �    '��
$Key ����A ѱ���0�0 0 0 0 0 0| �      |       �# C\��Z   Z   
```
The key could be the first 40th characters since there is a seperation '|' after that and in the first apparition the next character is a '$' indicating a new header ?

TTH/Z4PSXU7CJ7YLW2PYTEFRTU4K2KIWUZIPQQNZ73I
bz2
