names = ['zhaoyifa', 'wangdacun', 'zhaoyong']
print("新购买的餐桌无法及时送达，因此只能邀请两位嘉宾")

name = names.pop()
print("下次再约你" + name)

print(names[0] + "来吧")
print(names[1] + "来吧")

del names[0]
del names[0]
print(names)