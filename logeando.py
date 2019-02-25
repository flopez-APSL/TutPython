
"""
Los mensajes de registro (loggings) se envían a un archivo o a sys.stderr:
"""

import logging
logging.debug('Debugging information')
logging.info('Information message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')

