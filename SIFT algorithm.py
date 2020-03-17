def check_pixel(data1, data2):
    rowcount = 0
    lcount = 0
    check = False
    for i in data1:
        for j in i:

            if j != data2[rowcount][lcount]:
                check = True
                print("differ -> info ---- data2_pixel : " ,data2[rowcount][lcount], "data1_pixel: ",j)
                break
            lcount+=1
        if check == True:
            print(lcount)
            break
        rowcount+=1
        lcount =0


def part_check_pixel(data1, data2):

    rowcount = 300
    lcount = 600

    check = False

    for row in range(rowcount, rowcount+300):
        for low in range(lcount , lcount + 500):

            if data1[row][low] != data2[row][low]:
                check = True
                print("differ -> info ---- data2_pixel : " ,data2[row][low], "data1_pixel: ",data1[row][low])
                return False
    return True
