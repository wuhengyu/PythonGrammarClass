def can_play(fn):
    print('外部函数被调用了')

    def inner(name, game, **kwargs):
        fn(name, game)

    return inner


@can_play
def play_game(name, game):
    print(name + '正在玩儿' + game)


play_game('张三', '王者荣耀', clock=22)
