# noinspection PyUnresolvedReferences
log_active = False

def log(msg):
    if log_active:
        print(msg)


log("eccomi qui")
