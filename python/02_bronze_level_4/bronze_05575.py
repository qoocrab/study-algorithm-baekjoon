for _ in range(3):
    gh, gm, gs, lh, lm, ls = map(int, input().split())

    time = (lh * 3600 + lm * 60 + ls) - (gh * 3600 + gm * 60 + gs)
    print(time // 3600, (time % 3600) // 60, (time % 3600) % 60)
