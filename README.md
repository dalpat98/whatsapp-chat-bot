# whatsapp-chat-bot

WhatsApp Chatbot which Updates us about the corona live cases in real time With Python, Flask and Twilio.
A chatbot is a software application that is able to conduct a conversation with a human user through written or spoken language. The level of “intelligence” among chatbots varies greatly. While some chatbots have a fairly basic understanding of language, others employ sophisticated artificial intelligence (AI) and machine learning (ML) algorithms to achieve an almost human conversational level.

The source code is **100% Python**.

### Show some :heart: and star the repo to support the project

## Requirements :
- Python 3.6 or newer. If your operating system does not provide a Python interpreter, you can go to python.org to download an installer.
- Flask. We will create a web application that responds to incoming WhatsApp messages with it.
- ngrok. We will use this handy utility to connect the Flask application running on your system to a public URL that Twilio can connect to. This is necessary for the development version of the chatbot because your computer is likely behind a router or firewall, so it isn’t directly reachable on the Internet. 
- A smartphone with an active phone number and WhatsApp installed.
- A Twilio account.

## Configure the Twilio WhatsApp Sandbox :
- From your Twilio Console, select Programmable Messaging, then click on "Try it Out" and finally click on Try WhatsApp. The WhatsApp sandbox page will show you the sandbox number assigned to your account, and a join code.
- To enable the WhatsApp sandbox for your smartphone send a WhatsApp message with the given code to the number assigned to your account. The code is going to begin with the word join, followed by a randomly generated two-word phrase. Shortly after you send the message you should receive a reply from Twilio indicating that your mobile number is connected to the sandbox and can start sending and receiving messages.
- Note that this step needs to be repeated for any additional phones you’d like to have connected to your sandbox.

<img height="480px" src="https://twilio-cms-prod.s3.amazonaws.com/images/a3Dg7ccP5QFcnxWM6N0kmUDk7VqvuL5M538UfEg-yxMc2r.width-500.png">

## Testing the Chatbot :
- start the chatbot by running python bot.py
- run ngrok http 5000 to allocate a temporary public domain that redirects HTTP requests to local port 5000.
- Go back to the Twilio Console, click on Programmable Messaging, then on Settings, and finally on WhatsApp Sandbox Settings. Copy the https:// URL from the ngrok output and then paste it on the “When a message comes in” field. Since our chatbot is exposed under the /bot URL, append that at the end of the root ngrok URL. Make sure the request method is set to HTTP Post. Don’t forget to click the red Save button at the bottom of the page to record these changes.
- Now you can start sending messages to the chatbot from the smartphone that you connected to the sandbox.

### :heart: Found this project useful?

If you found this project useful, then please consider giving it a :star: on Github and sharing it with your friends via social media.

# Pull Requests

I welcome and encourage all pull requests. It usually will take me within 24-48 hours to respond to any issue or request. Here are some basic rules to follow to ensure timely addition of your request:

1.  Match the document style as closely as possible.
2.  Please keep PR titles easy to read and descriptive of changes, this will make them easier to merge :)
3.  Pull requests _must_ be made against `master` branch for this particular repository.
4.  Make sure you follow the set standard as all other projects in this repo do
5.  Have fun!

### Created & Maintained By

[Dalpat I](https://github.com/dalpat98)
([Instagram](https://www.instagram.com/dalpat_chaudhary__/))

> If you found this project helpful or you learned something from the source code and want to thank me, consider staring the repo. :heart:

