# -*- coding: utf-8 -*-
from webapps import create_app


conf_name = 'development'
manager = create_app(conf_name)


if __name__ == '__main__':
    manager.run()
