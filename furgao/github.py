import requests




import hmac


def gh_signature(req, secret):
    received_sign = req.headers.get('X-Hub-Signature-256').split('sha256=')[-1].strip()
    secret = secret.encode()
    expected_sign = hmac.HMAC(key=secret, msg=req.data, digestmod=hashlib.sha256).hexdigest()
    return hmac.compare_digest(received_sign, expected_sign)


def handler(event, context):

    GH_WEBHOOK_SECRET = os.getenv('GH_WEBHOOK_SECRET', None)

    if not verify.gh_signature(request, GH_WEBHOOK_SECRET):
        return make_response(jsonify(error='Deny'), 500)

    headers = request.headers
    rjson = request.json
    r = request.post(WEBHOOK_DEST, headers=headers, json=rjson)

    if r.status_code == 200:
        return jsonify(message='OK')

    else:
        return make_response(jsonify(error=r.text), r.status_code)
