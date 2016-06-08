#!/usr/bin/env python
import os
from app import create_app

app = create_app(os.getenv('TWEZANA_CONFIG') or 'default')
manager = Manager(app)


if __name__ == '__main__':
	manager.run()