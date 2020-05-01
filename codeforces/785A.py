
if __name__ == '__main__':
    n = int(input())

    p = { "Icosahedron": 20, "Cube": 6, "Tetrahedron": 4, "Octahedron": 8, "Dodecahedron": 12 }

    i = 0
    faces = 0
    while i < 200001 and i < n:
        ph = input()
        faces += p[ph]
        i += 1
    print(faces)
