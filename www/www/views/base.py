from pyramid.httpexceptions import HTTPFound
from orthus.db import Session
from orthus.db.user import User as UserClass
import hashlib


class ViewBase(object):
    need_auth = 1

    def __init__(self, request):
        self.request = request

    def call(self):
        pass

    def __call__(self):
        if self.need_auth and 'user' not in self.request.session:
            return HTTPFound(location='/login')
        view_result = self.call()
        if type(view_result) is dict:
            view_result['session'] = self.request.session
        return view_result

    def authenticate(self, email, password):
        session = Session()
        sha1hash = hashlib.sha1(password).hexdigest()
        user = session.query(UserClass).filter(UserClass.email == email, UserClass.password == sha1hash).first()
        if user:
            self.request.session.update({'user': user})
            self.request.session.save()
            return 1
        else:
            return 0