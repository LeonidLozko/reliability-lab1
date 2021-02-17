times = [25, 80, 157, 39, 372, 45, 108, 549, 1771,
         969, 508, 1134, 90, 382, 413, 444, 329, 158,
         551, 536, 216, 337, 493, 12, 1, 514, 88, 243,
         56, 521, 231, 301, 1120, 528, 513, 95, 79,
         460, 41, 383, 223, 39, 51, 625, 346, 11, 26,
         645, 377, 169, 88, 396, 126, 269, 962, 38,
         850, 2, 80, 73, 65, 253, 180, 80, 553, 150,
         808, 412, 384, 199, 640, 688, 613, 70, 227,
         481, 238, 253, 207, 879, 182, 670, 146, 453,
         502, 206, 94, 7, 28, 17, 31, 34, 136, 659,
         209, 143, 652, 119, 115, 259]
gamma = 0.75
time_infail = 44
time_fail = 801

times.sort()
T_average = sum(times) / len(times)

h = (times[-1] - times[0]) / 10
fi_list = [0]
P_list = [1]
i = 0
index = 0
for k in range(1, 11):
    counter = 0
    while i < len(times) and times[i] <= k * h + times[0]:
        counter += 1
        i += 1
    fi_list.append(counter / (h * len(times)))
    P_list.append(counter / len(times))
    if P_list[k - 1] > gamma >= P_list[k]:
        index = k
d = (P_list[index - 1] - gamma) / (P_list[index - 1] - P_list[index])
T = fi_list[index - 1] + h * d

P = 1
k = 1
while k * h <= time_infail:
    P -= fi_list[k] * h
    k += 1
P -= fi_list[k] * (time_infail - (k - 1) * h)

Pf = 1
k = 1
while k * h <= time_fail:
    Pf -= fi_list[k] * h
    k += 1
Pf -= fi_list[k] * (time_fail - (k - 1) * h)
lamb = fi_list[k] / Pf

print("Середній наробіток до відмови Tср = {} \n"
      "y-відсотковий наробіток на відмову при y = {} Ty = {} \n"
      "Ймовірність безвідмовної роботи на час {} годин = {} \n"
      "Інтенсивність відмов на час {} годин = {}".format(T_average, gamma, T, time_infail, P, time_fail, lamb))
