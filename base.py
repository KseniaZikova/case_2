# Developers: Zikova K.(75%), Bateneva M.(85%), Shlapakova K.(90%)

import ru_local


def wait(lir):
    from random import randint

    if lir % 10 != 0:
        lir += 10 - lir % 10
    k = int(lir / 10)
    if k > 1:
        k += randint(-1, 1)
    else:
        k = 1
    return k


def sost(azs, d):
    avt = ru_local.ONE
    z = '*'
    r = []
    for i, k in enumerate(azs):
        r.append(avt % (i + 1, d[i]['max'], d[i]['type'], z * len(k)))
    return r


def print_(sob):
    sob.sort()
    for i in sob:
        print(i[0])
        for w in i[1]:
            print(w)


def main():
    with open('azs.txt') as f1:
        text = f1.readlines()
        d = []
        for i in text:
            i = i.strip()
            if not i:
                continue
            s = i.split()
            dd = {}
            dd['num'] = int(s[0])
            dd['max'] = int(s[1])
            dd['type'] = s[2:]
            dd['last'] = None
            d.append(dd)

        with open('input.txt') as f2:

            text2 = f2.readlines()

            m1 = ru_local.NEWCL
            m2 = ru_local.BAK
            m3 = ru_local.GOODBY
            sob = []
            azs = []
            dt = {ru_local.ONEBZ: 0, ru_local.TWOBZ: 0, ru_local.THREEBZ: 0, ru_local.FOREBZ: 0}
            for i in d:
                azs.append(list())
            for j in text2:
                j = j.split()
                hs = j[0].split(':')
                hour = int(hs[0])
                min_ = int(hs[1])
                time = j[0]
                litr = int(j[1])
                k = wait(int(litr))
                type_ = j[2]

                found = False
                c = [time, litr, k, type_, hour, min_]

                ct = hour * 60 + min_
                for i, o in enumerate(azs):
                    no = []
                    last_h = 0
                    last_m = 0

                    oo = o.copy()
                    for ai, a in enumerate(oo):
                        if d[i]['last'] == None or (d[i]['last'] != None and ct > d[i]['last']):
                            tm = a[4] * 60 + a[5] + k
                        else:
                            tm = d[i]['last'] + k

                        hh = str(tm // 60).zfill(2)
                        mm = str(tm % 60).zfill(2)
                        time2 = hh + ':' + mm

                        if ct > tm:
                            azs[i] = oo[ai + 1:]
                            time3 = str(a[4]).zfill(2) + ':' + str(a[5]).zfill(2)
                            sob.append([m2 % (time2, time3, type_, litr, k), sost(azs, d)])
                            d[i]['last'] = tm
                            dt[type_] += litr
                        else:
                            no.append(a)
                    azs[i] = no

                car_lost = 0
                found = True
                for i, o in enumerate(azs):
                    z = d[i]
                    if type_ in z['type'] and len(o) <= z['max']:
                        azs[i].append(c)
                        sob.append([m1 % (time, time, type_, litr, k, i + 1), sost(azs, d)])
                        found = True

                    if not found:
                        sob.append([m3 % (time, time, type_, litr, k), sost(azs, d)])
                        car_lost += 1
    print_(sob)

    print(ru_local.TODAYBY, ru_local.ONEBZ, dt['АИ-92'], ru_local.LITR, ru_local.TWOBZ, dt['АИ-95'], ru_local.LITR,
          ru_local.THREEBZ, dt['АИ-80'], ru_local.LITR, ru_local.FOREBZ, dt['АИ-98'], ru_local.LITR)

    money = {ru_local.ONEBZ: 41, ru_local.TWOBZ: 43.9, ru_local.THREEBZ: 34, ru_local.FOREBZ: 48.1}
    first_m = dt['АИ-92'] * money['АИ-92']
    second_m = dt['АИ-95'] * money['АИ-95']
    third_m = dt['АИ-80'] * money['АИ-80']
    thourth_m = dt['АИ-98'] * money['АИ-98']

    total_money = first_m + second_m + third_m + thourth_m
    print(ru_local.CASH, total_money, ru_local.MONEY)
    print(ru_local.NOMONEY, car_lost, ru_local.CAR)


if __name__ == '__main__':
    main()