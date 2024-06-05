# monkey-see
This project is for the [Balik Kampung 2024](https://www.instagram.com/balik.kampoeng/) initiative, where one of the projects is to install camera traps to detect orangutan movements and alert nearby stations to inform people living nearby.

![WhatsApp Image 2024-06-03 at 18 35 32](https://github.com/AbrahamOsmondE/monkey-see/assets/82792334/62c3608e-b32d-4f4a-9705-4cc67e90d6c3)

This repository works on the highlighted part of the image, where the raspberry pi will receive an image, and forward it to a Telegram channel, and an email address.

## Considerations
The following are some considerations that need to be taken into account when designing the solution
1. We would need to be in the vicinity to update the code within the Raspberry Pi
2. The solution should be as cheap as possible, preferably free.
3. The expected load is 100 images per hour, with uptime of 12 hours per day
4. The image resolution is 800 x 600, with a size less than 1 MB

## Design decisions
With the considerations above, we decided to implement the solution as follows:
1. The function within Raspberry Pi will be as simple as possible (e.g. only encode image to base64 and send to a backend) to avoid having to update anything
2. We will be using a lambda function to receive the encoded image and forward it to a Telegram channel and an email address
3. We will be using the Gmail API to send the image to an email address

With this, we can ensure that the solution will be free of cost and changes to how we send to the Telegram channel or email address can be fixed remotely. This does not solve hardware issues with the Raspberry Pi, however. Lambda is free for the first million requests per month and for 400000 GB seconds of compute time. Synchronous functions also allow a 6 MB payload. This allows the solution to be costless
