from linebot.v3 import (
    WebhookHandler
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage,
    ShowLoadingAnimationRequest
)
import json
import os
from firebase import firebase



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

        if msg_type == 'text':
            msg = event['message']['text']

            with ApiClient(configuration) as api_client:
                line_bot_api = MessagingApi(api_client)
                line_bot_api.show_loading_animation(ShowLoadingAnimationRequest(
                    chatId=user_id, loadingSeconds=20))

                if msg == '!清空':
                    reply_msg = '已清空'
                    # fdb.delete(user_chat_path, None)
                elif msg == '!摘要':
                    reply_msg = msg # test
                else:
                    reply_msg = "哈囉你好嗎"

                line_bot_api.reply_message(
                    ReplyMessageRequest(
                        reply_token=reply_token,
                        messages=[
                            TextMessage(text=reply_msg),
                        ]))
        else:
            with ApiClient(configuration) as api_client:
                line_bot_api = MessagingApi(api_client)
                line_bot_api.reply_message(
                    ReplyMessageRequest(
                        reply_token=reply_token,
                        messages=[
                            TextMessage(text='你傳的不是文字訊息喔'),
                        ]))

    except Exception as e:
        detail = e.args[0]
        print(detail)
    return 'OK'
