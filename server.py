import time
from sanic import Sanic, response
from sanic.views import HTTPMethodView
from sanic.response import json
from sanic.response import text
import jwt
import json as JSON
import auth

app = Sanic("class_views_example")

class SimpleView(HTTPMethodView):
    class JWT:
        encoded_jwt = ''

    jwt = JWT()

    def get(self, request):
        return text('Support Only Post')

    # Main Post function
    async def post(self, request):
        # if a user is logged, validate token and parse message
        if self.jwt.encoded_jwt and request.headers.get('token') == self.jwt.encoded_jwt:
            body = JSON.loads(request.body)
            resp = {}
            for elem in body:
                resp[elem.get('name')] = elem.get([key for key in elem.keys() if 'Val' in key][0])
            return json(resp)
        # if user is not logged, authenticate
        if auth.username == request.form.get('username') and \
                auth.password == request.form.get('password'):
            self.jwt.encoded_jwt = jwt.encode({"username": auth.username}, str(time.time()), algorithm="HS256")
            return json({'token': self.jwt.encoded_jwt})
        # if not authenticated
        return text('Not authenticated')

app.add_route(SimpleView.as_view(), '/')

app.run()
