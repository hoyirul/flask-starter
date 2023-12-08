from functools import wraps
from flask import session, redirect, url_for

class HandlerLoader:
    @staticmethod
    def onloading(f):
      @wraps(f)
      def decorated_function(*args, **kwargs):
        if 'token' not in session:
          return redirect('/login')
        return f(*args, **kwargs)
      return decorated_function
