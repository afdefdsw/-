# 今天教学基于python制作一个属于自己的查询软件
# 教学作者：crazy.
# 安装requests库 pip install requests 再终端Terminal里面执行即可
# 制作这个查询软件我们需要导入两个库，一个re库，一个requests库。
# 导入两个库（无基础的导入requests即可）
import re
import requests
# 导入完库之后我们就正式开始写主程序
qianyan = '''  
我们可以再这里面写一些想说的话，比如软件作者之类的
没有基础的可以看着我会提示说做到哪里就可以了（只需要修改接口和形式即可），有基础的可以进行优化
'''
print(qianyan)      # print()是输出某些东西
set = input("请输入要查询的东西：")   # input()是指再这里输入某些东西
url = f"https://api.xywlapi.cc/qqapi?qq={set}"    # "这里是接口"
resp = requests.get(url)    # 利用requests模块的get进行去访问上面的接口
# print(resp.text)    # 利用print进行输出结果
resp.close()    # close()是为了每次执行完之后关闭resp的执行，以避免报错
# 没有基础的到这里就够了，这时候已经可以输出数据出来了
# 数据输出之后我们会觉得json返回的不是很好看，这时候我们就需要过滤掉这些东西。我们就需要re模块,接下来就是过滤
obj = re.compile('status":200,"message":"(?P<cg>.*?)","qq":"(?P<qq>.*?)","phone":"(?P<sjh>.*?)",'
                 '"phonediqu":"(?P<dq>.*?")', re.S)
# 第一个是为了过滤掉多余的东西所以不需要，之后便是惰性匹配我们需要的东西，这时候把上边的输出删掉或变成注释
desk = resp.text    # 将输出给到desk这个变量
base = obj.finditer(desk)   # 将变量给到base，将过滤的插件给到desk
for it in base:     # finditer保存的是迭代器不能直接输出所以要进行循环，最后制作完成
    print(it.group("cg"))
    print("QQ：" + it.group("qq"))
    print("手机号：" + it.group("sjh"))
    print("地区" + it.group("dq"))
# pyinstaller -F -i cc.ico 查询示例.py 最后变成软件需要的代码，需要再同一目录下执行

dbj = re.compile('status":500,"message":"(?P<wb>.*?)"', re.S)  # 教学后才想起来的没有添加没查询到后的东西不然未查到只有空
bee = resp.text
dee = dbj.finditer(bee)
for he in dee:
    print(he.group("wb"))
