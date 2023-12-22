import requests


def handler(event, context):
    headers = request.headers
    rjson = request.json
    r = request.post(WEBHOOK_DEST, headers=headers, json=rjson)

    if r.status_code == 200:
        return jsonify(message='OK')

    else:
        return make_response(jsonify(error=r.text), r.status_code)