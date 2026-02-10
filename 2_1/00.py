for i in range(100):
    if arr[99][i] == 2:
        x = i
for j in range(99, -1, -1):
    if x == 0:
        if arr[j][x + 1] == 1:
            while True:
                x = x + 1
                if x + 1 > 99:
                    break
                if arr[j][x + 1] == 0:
                    break
    elif x == 99:
        if arr[j][x - 1] == 1:
            while True:
                x = x - 1
                if x - 1 < 0:
                    break
                if arr[j][x - 1] == 0:
                    break
    else:
        if arr[j][x-1]==1 or arr[j][x+1] == 1:
            if arr[j][x-1]==1:
                while True:
                    x = x - 1
                    if x - 1 < 0:
                        break
                    if arr[j][x - 1] == 0:
                        break

            elif arr[j][x + 1] == 1:
                while True:
                    x = x + 1
                    if x + 1 > 99:
                        break
                    if arr[j][x + 1] == 0:
                        break
print(f'#{test_case} {x}')