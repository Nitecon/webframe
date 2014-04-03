import os
import ConfigParser
import web
import __builtin__
#from view.helpers import utils
#from view.helpers import formatting

# template global functions
#globals = utils.get_all_functions(formatting)

app_path = __builtin__.webframe_app_dir

main_config = ''.join((app_path, os.path.join('/config/application.cfg')))
print main_config
config = ConfigParser.ConfigParser()
config.read(main_config)

# in development debug error messages and reloader
web.config.debug = config.get('general','debug')
cache = config.get('general','cache')
# in production the internal errors are emailed to us
web.config.email_errors = config.get('general','email_errors')

# set global base template
view = web.template.render('view/templates', cache=cache, globals=globals)

urls = ("/.*", "hello")
app = web.application(urls, globals())

class hello:
    def GET(self):
        return 'Hello, world!'

