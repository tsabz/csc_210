
def powed_num():
    chosen_num = 0
    sum_total = 0
    while sum_total < 5:
        chosen_num += 1
        sum_total += pow(chosen_num, 2)
    print("Total sum of the number is: %s" %
          sum_total, "The last number that has been squared is: %s" % chosen_num)


powed_num()
