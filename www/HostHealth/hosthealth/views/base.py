from pyramid.httpexceptions import HTTPFound
class ViewBase(object):
    need_auth = 1

    def __init__(self, request):
        self.request = request

    def call(self):
        pass

    def __call__(self):
        if self.need_auth and 'user_id' not in self.request.session:
            return HTTPFound(location='/login')
        view_result = self.call()
        if type(view_result) is dict:
            view_result['session'] = self.request.session
        return view_result

    def authenticate(self, email, password):
        if email == 'me@fishbone.me' and password == 'vbcnth,fkf,jkrf':
            self.request.session['user_id'] = 1
            self.request.session.save()
            return 1
        else:
            return 0