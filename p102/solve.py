def main():
    with open('triangles.txt') as f:
        lines = f.read().splitlines()

    counts = 0
    for line in lines:
        points = line.split(',')
        points = [int(point) for point in points]
        A = points[:2]
        B = points[2:4]
        C = points[4:]
        P = (0, 0)
        if area(A, B, C) == area(P, B, C) + area(P, A, C) + area(P, A, B):
            counts += 1
    print(counts)

def area(A, B, C):
    return abs((A[0]-C[0]) * (B[1]-A[1]) - (A[0]-B[0]) * (C[1]-A[1])) 

if __name__ == '__main__':
    main()