import kruxstatsd
import socket
import fudge

import statsd

hostname = socket.gethostname()
env = 'prod'
prefix = 'js'


def mock_statsd_method(kls, stat, count=1, rate=1):
    assert stat.startswith('%s.%s' % (env, prefix))
    assert stat.endswith(hostname)


def test_prefix():
    k = kruxstatsd.KruxStatsClient('js', env='prod')
    assert k.prefix == 'js'


def test_stats_format_incr():
    fudge.patch_object(statsd.StatsClient, 'incr', mock_statsd_method)
    k = kruxstatsd.KruxStatsClient('js', env='prod')
    k.incr('foo')


def test_stats_format_timing():
    fudge.patch_object(statsd.StatsClient, 'timing', mock_statsd_method)
    k = kruxstatsd.KruxStatsClient('js', env='prod')
    k.timing('foo.bar.baz')
