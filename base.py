def wait(lir):
    from random import randint
    # Функция, которая определяет время ожидания в зависимости от литров на заправку
    if lir % 10 != 0:
        lir += 10 - lir % 10
    k = int(lir / 10)  # время ожидания
    if k > 1:
        k += randint(-1, 1)
    else:
        k = 1
    return k  # время заправки


def sost(azs, d):
    avt = 'Автомат №%i максимальная очередь: %i Марки бензина: %s ->%s'
    z = '*'
    r = []
    for i, k in enumerate(azs):
        r.append(avt%(i+1, d[i]['max'], d[i]['type'], z*len(k)))
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

            m1 = 'В  %s  новый клиент:  %s %s %i %i встал в очередь к автомату №%i'
            m2 = 'В  %s  клиент  %s %s %i %i  заправил свой автомобиль и покинул АЗС.'
            m3 = 'В  %s  новый клиент:  %s %s %i %i не смог заправить автомобиль и покинул АЗС.'
            sob = []
            azs = []
            dt = {'АИ-92':0, 'АИ-95':0, 'АИ-80':0, 'АИ-98':0}
            for i in d:
                azs.append(list())
            for j in text2:
                j = j.split()
                hs = j[0].split(':')
                hour = int(hs[0])
                min_ = int(hs[1])
                time = j[0]
                litr = int(j[1])  # необходимые литры для заправки
                k = wait(int(litr))  # время заправки
                type_ = j[2]

                found = False
                c = [time, litr, k, type_, hour, min_]  # состояние прибывшей машины

                ct = hour * 60 + min_  # текущее время
                for i, o in enumerate(azs):
                    no = []
                    last_h = 0
                    last_m = 0

                    oo = o.copy()
                    for ai, a in enumerate(oo):
                        if d[i]['last'] == None or (d[i]['last'] != None and ct > d[i]['last']):
                            tm = a[4]*60 + a[5] + k
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
    print('Всего за сутки было продано: ', 'АИ-92:', dt['АИ-92'], 'литров;', 'АИ-95:', dt['АИ-95'], 'литров;',
          'АИ-80:', dt['АИ-80'], 'литров;', 'АИ-98: ', dt['АИ-98'], 'литров.')

    money = {'АИ-92': 41, 'АИ-95': 43.9, 'АИ-80': 34, 'АИ-98': 48.1}
    first_m = dt['АИ-92'] * money['АИ-92']
    second_m = dt['АИ-95'] * money['АИ-95']
    third_m = dt['АИ-80'] * money['АИ-80']
    thourth_m = dt['АИ-98'] * money['АИ-98']

    total_money = first_m + second_m + third_m + thourth_m
    print('Общая выручка за день: ', total_money, 'рублей.')
    print('Всего не смогли заправиться', car_lost, 'машин.')

main()
