def aa(m):
    print("m:", m)

    def bb(n):
        print("n:", n)

    return bb


cc = aa("mmmmmmmmmmmmmmmmmmm")
cc("nnnnnnnnnnnnnnnnn")
