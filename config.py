import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'lkkjuy6786764565wsrguijopo090788676tgjhyijkhjohk'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	SQLALCHEMY_TRACK_MODIFICATIONS = True
	MAIL_SERVER = 'smtp.gmail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = 'mail@gmail.com' #os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD = 'pass'	#os.environ.get('MAIL_PASSWORD')
	TWEZANA_MAIL_SUBJECT_PREFIX = '[Twezana]'
	TWEZANA_MAIL_SENDER = 'gichuru.gichia@gmail.com'
	TWEZANA_ADMIN = os.environ.get('TWEZANA_ADMIN')

	@staticmethod
	def init_app(app):
		pass
		
class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = 	{	
				'development': DevelopmentConfig,
				'production': ProductionConfig,
				
				'default': DevelopmentConfig
			}