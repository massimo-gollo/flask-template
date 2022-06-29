from flask import current_app as app


@app.route('/ping')
def ping():
    return 'pong', 200
