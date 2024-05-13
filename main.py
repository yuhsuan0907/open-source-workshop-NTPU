from linebot.v3 import WebhookHandler
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage
)
import json
import os


# 使用環境變量讀取憑證
secret = os.getenv('ChannelSecret', None)
token = os.getenv('ChannelAccessToken', None)

handler = WebhookHandler(secret)
configuration = Configuration(
    access_token=token
)

def linebot(request):
    body = request.get_data(as_text=True)
    json_data = json.loads(body)
    try:
        signature = request.headers['X-Line-Signature']
        handler.handle(body, signature)
        event = json_data['events'][0]
        reply_token = event['replyToken']
        user_id = event['source']['userId']
        msg_type = event['message']['type']

        with ApiClient(configuration) as api_client:
            line_bot_api = MessagingApi(api_client)

            if msg_type == 'text':
                msg = event['message']['text']
                line_bot_api.show_loading_animation(chat_id=user_id, loading_seconds=20)

                if msg == '!清空':
                    reply_msg = '已清空'
                    # Add functionality to clear data if needed
                elif msg == '!摘要':
                    reply_msg = '摘要功能正在開發中'
                else:
                    reply_msg = "哈囉你好嗎"

                line_bot_api.reply_message(
                    ReplyMessageRequest(
                        reply_token=reply_token,
                        messages=[
                            TextMessage(text=reply_msg),
                        ]))
            else:
                line_bot_api.reply_message(
                    ReplyMessageRequest(
                        reply_token=reply_token,
                        messages=[
                            TextMessage(text='你傳的不是文字訊息喔'),
                        ]))
    except Exception as e:
        print(f"Error: {e}")
    return 'OK'
