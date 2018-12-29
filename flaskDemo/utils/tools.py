import random
import time


def get_date_time():
    return time.strftime('%Y.%m.%d %H:%M:%S', time.localtime(time.time()))

st = "09:30:00"
et = "11:30:00"

def time2seconds(t):
    h,m,s = t.strip().split(":")
    return int(h) * 3600 + int(m) * 60 + int(s)

def seconds2time(sec):
    m,s = divmod(sec,60)
    h,m = divmod(m,60)
    return "%02d:%02d:%02d" % (h,m,s)

def randomtime():
    sts = time2seconds(st) #sts==27000
    ets = time2seconds(et) #ets==34233
    rt = random.sample(range(sts,ets),10)
    rt.sort() #对时间从小到大排序
    return rt

# for r in randomtime():
#     print(seconds2time(r))

msg = [(200, '成功'), (201, '失败')]
info = random.choice(msg)
print(info[0])
print(info[1])