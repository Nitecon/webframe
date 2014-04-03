__author__ = 'Will Hattingh<w.hattingh@nitecon.com>'
import os
import os.path
import json


class AppConfig():
    base_path = ''
    main_config_file = ''

    def __init__(self, base_path):
        self.base_path = base_path
        self.main_config_file = ''.join((base_path, os.path.join('/config/application.json')))

    def get_config(self):
        json_data = open(self.main_config_file)
        data = json.load(json_data)
        config = data
        json_data.close()
        for mods in config['modules']:
            mod_path = '/modules/%s/config/config.json' % mods
            mod_conf = ''.join((self.base_path, os.path.join((mod_path))))
            if os.path.isfile(mod_conf):
                mod_file = open(mod_conf)
                mod_data = json.load(mod_file)
                try:
                    config['routes'].append(mod_data['routes'])
                except KeyError:
                    pass
        assert isinstance(config, object)
        return config