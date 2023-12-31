## 📦 AmzTrack - Never Miss a Price Drop on Your Favorite Amazon Product! 🛍️

To get started with AmzTrack, follow these steps:

1. **Install Python and the necessary libraries**: Make sure you have Python installed on your computer. If not, download it from [here](https://www.python.org/downloads/). After installing Python, open your terminal or command prompt and run the following commands to install the required Python libraries:

   ```
   pip install requests beautifulsoup4 urllib3==2.0.4
   ```
   
   (Optional advanced usage) If you want to run AmzTrack as a server, also install FastAPI and Uvicorn:
   
   ```
   pip install fastapi uvicorn
   ```

2. **Get your Telegram Bot Token and Chat ID**: Follow the steps described in the blog post linked in the documentation to obtain your Telegram Bot Token and Chat ID.

3. **Get the Product URL**: Go to the Amazon product page you want to track and copy its URL.

4. **Get Telegram chat_id and optionally Amazon browser cookies**: To get your chat_id, start by sending your bot a message in Telegram. Then, run the provided script with your bot token:

   ```python
   import requests
   TOKEN = "<YOUR TELEGRAM TOKEN HERE>"
   url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
   print(requests.get(url).json())
   ```
   
   For cookies, it's optional even if you're using the server implementation. You can obtain them by opening the product page in your local Chrome browser, copying the cookies, and formatting them into a Python dictionary. Replace the cookie dictionary in the script with your own.

5. **Edit the Python script**: Replace the placeholders in the script with the values you collected earlier:

   - Replace `<TELEGRAM BOT TOKEN>` with your Telegram Bot Token.
   - Replace `<CHAT_ID>` with your chat_id.
   - Replace `<Your Product URL>` with the product URL.
   - Replace `<Your Cookie>` with the cookies dictionary you have collected (optional).
   - Set the `TARGET` variable to the price point at which you want to be alerted.

6. **Run the script**: Save the script as a .py file (for example, `base.py`). Now, go to your terminal or command prompt, navigate to the directory where you saved the script, and run the following command:

   ```
   python base.py
   ```

   The script will send you updates on Telegram every 2 minutes!

   💡 **Tip**: To run the script continuously, set up your computer to prevent it from sleeping, or run the script on a server.

   - On Mac, use these commands to disable sleep mode and run the script as a continuous process:

     ```
     sudo pmset -b sleep 0; sudo pmset -b disablesleep 1
     nohup caffeinate python base.py &
     ```

     When you're finished, re-enable sleep mode with:

     ```
     sudo pmset -b sleep 5; sudo pmset -b disablesleep 0
     ```

   - You can do similar configurations on Linux and Windows to disable sleep and network sleep from Power Management.

7. 🎉 Congratulations! You're all set to never miss a price drop on your favorite Amazon product again. Happy shopping and happy coding! 🎉

For more details about usage, check out this [Blog article](https://phreakyphoenix.tech/blog/amztrack-track-amazon-prices-with-python). Feel free to open Issues and Pull Requests if you have any suggestions or improvements. Let's make AmzTrack even better together! 💬
