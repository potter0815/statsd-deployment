Quick and easy deployment of Graphite and PyStatsd on an Ubuntu server.


## Installation

1. Fork this repository.

2. Update the setup file DEPLOYMENT variable to point to your forked version.

3. Install with this command (substitute the path to the setup file with your forked version):

    bash < <(curl -s https://raw.github.com/prestontimmons/statsd-deployment/master/setup)

4. Load your server: http://myserver/


## Notes

The Graphite web app is set up to run behind nginx. The process is managed by supervisor and gunicorn.

An application is running at /stats/ for managing static dashboard easily.
