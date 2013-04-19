import itertools
import logging
import sys
import traceback

import decorator

log = logging.getLogger('traad.trace')

@decorator.decorator
def trace(f, *args, **kw):
    '''A simple tracing decorator, mostly to help with debugging.
    '''

    # TODO: Use reprlib
    def short_repr(x, max_length=200):
        r = repr(x)
        if len(r) > max_length:
            r = r[:max_length - 3] + '...'
        return r

    log.info('{}({})'.format(
        f.__name__,
        ', '.join(
            map(short_repr,
                itertools.chain(
                    args,
                    kw.values())))))

    try:
        return f(*args, **kw)
    except:
        einfo = sys.exc_info()
        log.error('Exception in {}: {}'.format(
            f.__name__,
            ''.join(traceback.format_exception(einfo[0], einfo[1], einfo[2]))))
        raise
