# Hello world LINE Bot on Cloud Functions


## Platforms Used

- **LINE Developers**: To create and configure the LINEBot.
- **Google Cloud Functions**: To deploy the Python code and generate a webhook for the LINEBot.

## LINEBot Creation

### Step 1: Create a Bot on LINE Developers

### Step 2: Configure Bot Basic Information

- **Channel type**: Set to Messaging API (mandatory).
- **Provider**: Use an existing one or create a new one if you haven't used it before.
- **Other options**: Fill in the details as required.
- **Bot profile image**: Upload a custom image.
- **Privacy policy URL, Terms of use URL**: These can be left blank.

### Step 3: Obtain Bot's Channel Secret and Channel Access Token

After creating the bot, find the Channel secret on the Basic Setting page and the Channel access token on the Messaging API page. These will be used in the code.

**Note**: If you issue or reissue these credentials, remember to update them in your code.

### Step 4: Finalize Bot Setup

Set aside the bot for now. Once the program is deployed, paste the URL back into the Webhook URL field on the Messaging API page.


## Google Cloud Functions

### Step 0: Introduction to Google Cloud

Google Cloud offers a suite of cloud computing services, including computing, data storage, data analytics, and machine learning.

### Step 1: Get Started

Click on 'Console' or 'Start a Free Trial' on the website.

### Step 2: Create a Project in Cloud Functions

Find Cloud Functions in the menu or under the 'Serverless' category.

### Step 3: Create a Function

Set the environment to the first generation and the region to `asia-east1` (Taiwan). Set the trigger to HTTP and allow unauthenticated invocations.

Add four runtime environment variables:

- `ChannelAccessToken`: Your LINE Developers Channel access token.
- `ChannelSecret`: Your LINE Developers Channel secret.

### Step 4: Deploy

After setting up the function, deploy it. Once deployed, you'll find a 'Trigger URL' that you'll paste back into your LINEBot.
