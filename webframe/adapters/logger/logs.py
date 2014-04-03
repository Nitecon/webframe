import logging,os
import __builtin__

# create a file handler
try:
	logger = logging.getLogger(__name__)
	logger.setLevel(logging.INFO)
	handler = logging.FileHandler(os.path.join(app_path, 'var/log/application.log'))
	handler.setLevel(logging.INFO)
	# create a logging format
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	handler.setFormatter(formatter)
	# add the handlers to the logger
	logger.addHandler(handler)
except IOError:
	log_dir = os.path.join(app_path, 'var/log')
	print "Required directory does not exist OR file permission errors exist within: " + log_dir

logger.info('Configuration Read, starting router.') # will not print anything