def 参数展示(参数1, 参数2, 参数3="三"):
    print(参数1, 参数2, 参数3)

列表参数 = range(3)
字典参数 = {
    '参数1':'一',
    '参数2':'二'
}

print("解包列表:", end=" ")
参数展示(*列表参数)

print("解包字典", end=" ")
参数展示(**字典参数)