# Phone Numbers Everywhere, Anywhere

## Clue / Information

You are given this image of what seems to an AWS logo. Find the flag within the logo. You might have to refer to some external resources as well. Make sure to remove all non-alphanumeric characters before submitting the flag.

Wrap the phone number in bronco{}

[aws.jpg](./aws.jpg)

## Resolution

Using `exiftool` to check the metadata of the image, we obtain the following relevant info:
```
GPS Latitude                    : 37 deg 20' 56.93" N
GPS Longitude                   : 121 deg 56' 18.92" W
GPS Position                    : 37 deg 20' 56.93" N, 121 deg 56' 18.92" W
```

This position in Google Earth correspond to the **Sobrato Campus for Discovery and Innovation** at Santa Clara, CA 95053, United States.

!! This campus is not displayed in google maps, I had to use a different map server to get it.

Passing the full name of the full name of this campus in a browser, we get as first result: [SCDI - Santa Clara University](https://www.scu.edu/scdi/).
Since we are looking for phone numbers, let's take the first one the page: `School of Engineering: 408-554-4600`.
Remove the non-alphanumerical characters and here's your flag: `bronco{4085544600}` !
