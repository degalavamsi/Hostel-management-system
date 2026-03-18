from app.main import app

class PrefixMiddleware(object):
    def __init__(self, app, prefix=''):
        self.app = app
        self.prefix = prefix

    def __call__(self, environ, start_response):
        if environ['PATH_INFO'].startswith(self.prefix):
            environ['PATH_INFO'] = environ['PATH_INFO'][len(self.prefix):]
            environ['SCRIPT_NAME'] = self.prefix
        return self.app(environ, start_response)

# Apply the middleware to strip /api prefix
app.wsgi_app = PrefixMiddleware(app.wsgi_app, prefix='/api')

# This entry point is for Vercel Serverless Functions
app = app
