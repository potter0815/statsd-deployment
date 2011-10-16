Quick and easy deployment of [Graphite](http://graphite.wikidot.com/) and [PyStatsd](http://pypi.python.org/pypi/pystatsd/) on an Ubuntu server.

Installs Graphite 0.9.9.


## Installation

1. Fork this repository.

2. Update the setup file DEPLOYMENT variable to point to your forked version.

3. Install with this command (substitute the path to the setup file with your forked version):

    bash < <(curl -s https://raw.github.com/prestontimmons/statsd-deployment/master/setup)

4. Load your server: http://myserver/


## Configuration

Graphite configuration files are stored under the graphite folder.

Default retentions are set to:

* 1 hour of 10 second data
* 180 days of 1 minute data
* 5 years of 5 minute data

The default aggregation method for each retention level is set to sum.
This is different than the system default of averaging.

[Read more about configuration](http://readthedocs.org/docs/graphite/en/latest/config-carbon.html#storage-aggregation-conf)


## Notes

The Graphite web app is set up to run behind nginx. The process is managed by [supervisor](http://supervisord.org/) and [gunicorn](http://gunicorn.org/).

An application is running at /stats/ for managing static dashboards easily.
