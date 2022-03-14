def demo():
    memberlon = [113.41446473, 113.41421520, 113.41276334, 113.41302327]
    memberlat = [24.173747359, 24.17402158, 24.17280775, 24.17251895]
    for eachlon in range(len(memberlon)):
        print(str(memberlon[eachlon] + 0.012070351302980953) + ',' + str(memberlat[eachlon] + 0.003575751948158512))


def demo1():
    print(24.177323101948158 - 24.17374735)


if __name__ == '__main__':
    demo()
