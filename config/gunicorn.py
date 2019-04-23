from distutils.util import strtobool
import multiprocessing
import os


bind = os.getenv('WEB_BIND', '0.0.0.0:5000')
accesslog = '-'
access_log_format = "%(h)s %(l)s %(u)s %(t)s '%(r)s' %(s)s %(b)s '%(f)s' '%(a)s' in %(D)s(µs)"

workers = int(os.getenv('WEB_CONCURRENCY', multiprocessing.cpu_count() * 2))
threads = int(os.getenv('PYTHON_MAX_THREADS', 1))

reload = bool(strtobool(os.getenv('WEB_RELOAD', 'false')))
