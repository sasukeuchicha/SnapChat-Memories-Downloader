# SnapChat-Memories-Downloader
## Tool made for you
Snap Chat is widely used social media application but sometimes its frustrating on how hard it is to use it to save chats, download and store photos, browse, etc,...

But one of the feature to is to download the "memories" that you have. But it might not be saved forever and while migrating to new phone you might have lost the data.

## How it works

So its simple, We have the json file which we can download from snapchat which requires a POST method on the link provided on AWS s3 server and then in turn it would provide a GET link as a response. 

Which is the actual download link. So it would download te image or video like wise and store it in the folder Output.

## Prerequisites
To run this you must have python with version 3.0+ installed with inbult libraries or you may try in the virtual env.

## Want to test it on your device?

1) Download "My Data" from settings menu of Snap Chat. Settings -> My Data

![My Data Settings](https://vpnoverview.com/wp-content/uploads/snapchat-app-settings-settings-my-data.jpg "My Data Tab")

2) In a few minutes you will receive a mail with zip file of your data from snapchat. Then you will find **memories_history.json** file in the json folder. Once you copy and paste it in the project **SnapChat-Input** folder (`[location_to_project]/SnapCat-Input`). 

3) Run the main.py in terminal. 
	Open Command Prompt or terminal. 
	Use the following code to run.
	change the location on terminal to root project folder and run `main.py`
	```
		cd [location_to_project]
		python main.py
	```

4) You will find the downloaded images and videos in the output folder.

![snapchat-downloader working 1](https://user-images.githubusercontent.com/32739586/215326166-7fcaf7ca-8179-411c-ada7-8f216cbc1e8d.png)

## Future improvements 
* Use Spring Rest controller or Django Rest Framwork to create a working model on the cloud directly with security enabled for each user. 


If you find any bugs you may raise the issues. 
Feel free to raise pull requests if you have any improvements or suggestions. 
Thank you for reading. If you have any queries you can reach out to me at kjayanth807@gmail.com :)
