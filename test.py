import time
import cloud

def wait(s):
    # time.sleep(s)
    return s

def map_and_join_one(func, *args):
    jids = cloud.map(func, *args)

    while True:
        try:
            cloud.join(jids, timeout=0.1)
            timed_out = []
        except cloud.CloudTimeoutError, e:
            timed_out = e.args[0]
        if len(timed_out) != len(jids):
            # At least one thread finished, check if it yielded a solution.
            for jid in jids:
                if jid not in timed_out:
                    pass

def join_in_order(jids):
    while jids:
        try:
            cloud.join(jids, timeout=0.1)
            timed_out = []
        except cloud.CloudTimeoutError, e:
            timed_out = e.args[0]
        for finished_jid in jids:
            if finished_jid not in timed_out:
                result = cloud.result(finished_jid)
                jods.remove(finished_jid)
                yield (finished_jid, result)

jids = cloud.map(wait, [0.1, 0.2])

for x in cloud.result(jids):
    print x
# for jid, result in join_in_order([j1, j2]):
#     print jid, result
