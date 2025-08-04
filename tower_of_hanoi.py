def move(disks, start, aux, end):
    if disks < 1:
        return
    move(disks - 1, start, end, aux)
    end.append((start.pop()))
    draw()
    move(disks - 1, aux, start, end)


def draw():
    print(A, B, C, "-----------------", sep="\n")


if __name__ == "__main__":
    height = int(input("How many disks? "))
    print(height)
    A = [i for i in range(height, 0, -1)]
    B = []
    C = []
    draw()
    move(height, A, B, C)
