import json

import slack
import asyncio
from flask import Flask, request, make_response, Response


SLACK_BOT_TOKEN = "Do write it yourself"
SLACK_VERIFICATION_TOKEN = "Do write it yourself"


# async 이벤트 loop 생성
loop = asyncio.get_event_loop()

# 비동기 Slack 클라이언트 생성
slack_client = slack.WebClient(
    token=SLACK_BOT_TOKEN,
    run_async=True)

# Flask 객체 생성
app = Flask(__name__)


"""
    slack 요청에 대한 라우터
"""
@app.route("/slack/router", methods=["POST"])
def router() -> Response:
    if "payload" not in request.form:
        return make_response("not exist payload", 400)

    try:
        payload_json = json.loads(request.form["payload"])
    except:
        return make_response("invalid json object", 400)

    if SLACK_VERIFICATION_TOKEN != payload_json["token"]:
        return make_response("invalid token", 403)

    payload_type = payload_json["type"]

    if payload_type == "block_actions":
        action_id = payload_json["actions"][0]["action_id"]

        # 사전 반영 취소
        if action_id == "ignore_new_word":
            # 사전 반영 취소
            # Write it yourself if necessary

            remove_slack_notification(
                payload_json["container"]["channel_id"],
                payload_json["container"]["message_ts"]
            )

        # offset modal 호출
        elif action_id == "show_offset_modal":
            trigger_id = payload_json["trigger_id"]

            # 추후 슬랙 알림 제거를 위해 메타데이터 생성
            private_metadata = dict(
                channel_id=payload_json["container"]["channel_id"],
                message_ts=payload_json["container"]["message_ts"],
                word=payload_json["actions"][0]["value"]
            )

            view = {
                "type": "modal",
                "title": {
                    "type": "plain_text",
                    "text": "사전 등록",
                    "emoji": True
                },
                "submit": {
                    "type": "plain_text",
                    "text": "Submit",
                    "emoji": True
                },
                "close": {
                    "type": "plain_text",
                    "text": "Cancel",
                    "emoji": True
                },
                "blocks": [
                    {
                        "type": "input",
                        "label": {
                            "type": "plain_text",
                            "text": "offset 값을 입력해주세요.",
                            "emoji": True
                        },
                        "element": {
                            "type": "plain_text_input",
                            "multiline": False
                        }
                    }
                ],
                "private_metadata": json.dumps(private_metadata)
            }

            # offset modal 열기
            loop.run_until_complete(slack_client.views_open(
                view=view,
                trigger_id=trigger_id
            ))

        return make_response("", 200)
    # 사전 추가
    elif payload_type == "view_submission":
        block_id = payload_json["view"]["blocks"][0]["block_id"]
        action_id = payload_json["view"]["blocks"][0]["element"]["action_id"]
        offset = payload_json["view"]["state"]["values"][block_id][action_id]["value"]
        private_metadata = json.loads(payload_json["view"]["private_metadata"])

        # 사전 추가
        # Write it yourself if necessary

        remove_slack_notification(
            private_metadata["channel_id"],
            private_metadata["message_ts"]
        )

        # dialog가 닫히려면, empty body를 보내야 함
        return make_response("", 200)

"""
    후보 키워드 정보 전송
"""
@app.route("/slack/show", methods=["GET"])
def show() -> Response:
    word = request.args.get('word')

    if not word:
        return make_response("not exist word", 400)

    blocks = [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*%s* 를 사전에 등록하겠습니까?" % word,
            }
        },
        {
            "type": "actions",
            "elements": [
                {
                    "action_id": "show_offset_modal",
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Add"
                    },
                    "style": "primary",
                    "value": word
                },
                {
                    "action_id": "ignore_new_word",
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Ignore"
                    },
                    "style": "danger",
                    "value": word
                }
            ]
        }
    ]

    loop.run_until_complete(slack_client.chat_postMessage(
        channel=CHANNEL_DATA_ANALYSIS,
        blocks=blocks
    ))

    return make_response("ok", 200)

"""
    관련 슬랙 알림 제거

    Args:
        channel (str): 슬랙 채널 ID
        ts (str): 슬랙 메시지 ts
"""
def remove_slack_notification(channel: str, ts: str):
    loop.run_until_complete(slack_client.chat_delete(
        channel=channel,
        ts=ts
    ))


if __name__ == "__main__":
    app.run()
