import time
print(time.time)  # 时间戳：从1970年到现在经过的秒数
print(type(time.time()))  # time.time()返回的数据是float类型
# struct time 格式化的字符串形式的时间，作用：用于展示时间
print(time.strftime('%Y-%m-%d %H:%M%S %p',time.localtime())) # %x 表示年/月/日/时间 一种固定表达方式
print(time.strftime('%Y-%m-%d %X'))  # 以字符串格式表示时间 X代表标准化时刻
# # 格式化时间，输出和locatime()一样的结果
# print(time.strptime('2020-10-18','%Y-%m-%d'))
# print(time.localtime())

# 结构化的时间 作用: 用于单独获取时间的某一部分
# timestemp-----结构化的时间
res = time.localtime()  # 结果为元组，不传默认为time.time
print(res)
print(res.tm_year)  # 只输出年份
print(res.tm_yday)  # 输入年天数
print(time.struct_time)

# asctime([t])
# 如果没有参数,会把time.localtime()作为参数传入
print(time.asctime())  # 按照asc格式转化时间

print(time.ctime())  # 会默认把time.time作为参数,作用相当于time.asctime(time.localtime())

# 其他用法 sleep(secs) 线程推迟指定的时间运行
# time.sleep(2)
print('时间到')
import datetime
# print(datetime.datetime.now())  # 返回现在的时间
# print(datetime.date.fromtimestamp((time.time())))  # 时间戳转换成日期格式
# c_time = datetime.datetime.now()
# print(c_time.replace(minute=3,hour=2)) # 时间替换操作

print(time.time())
print(time.asctime())
print(time.localtime())
