import pymongo

# Blog: https://blog.csdn.net/fengbingchun/article/details/89069165

'''
reference:
	https://juejin.im/post/5addbd0e518825671f2f62ee
	http://www.runoob.com/python3/python-mongodb.html
	https://blog.csdn.net/xsdxs/article/details/52565489
'''

def print_results(description, results):
	strs = description + " type:"
	print(strs, type(results))
	description += ":"
	if (isinstance(results, dict)):
		print(description, results)
	else: 
		for result in results:
			print(description, result)

if __name__ == "__main__":
	print("pymongo version:", pymongo.version)

	client = pymongo.MongoClient(host='localhost', port=27017) # mongodb默认端口是27017
	print("connection successed:", client.server_info()) # 判断是否连接成功

	db = client.test # 指定test数据库, 如果没有则会自动创建
	collection = db.students # 每个数据库又包含许多集合
	student1 = {'id': '20170101', 'name': 'Jordan', 'age': 20, 'gender': 'male'}
	result = collection.insert_one(student1) # 在students集合中插入一条学生数据
	print("insert result:", result)

	student2 = {'id': '20170102', 'name': 'Tom', 'age': 21, 'gender': 'male'}
	student3 = {'id': '20170203', 'name': 'Mike', 'age': 22, 'gender': 'male'}
	result = collection.insert_many([student2, student3]) # 在students集合中插入多条学生数据
	print("many insert result:", result)

	result = collection.find_one({"name": "Tom"}) # 查询单个结果
	print_results("find one result", result)

	results = collection.find({"age": 20}) # 查询多个结果
	print_results("find many results", results)

	results = collection.find({"age": {"$gt": 20}}) # 查询年龄大于20的多个结果
	print_results("find age > 20 many results", results)

	count = collection.find({"age": 20}).count() # 查询计数
	print("find result count:", count)

	result = collection.delete_one({"age": 21}) # 删除一条数据
	print("delete one result:", result)
	print("delete one result count:", result.deleted_count)

	results = collection.delete_many({"age": {"$gte": 21}})
	print("delete many results:", results)
	print("delete many results count", results.deleted_count)

	condition = {"name": "Jordan"}
	student = collection.find_one(condition)
	#print_results("find one result", student)
	student["age"] = 25
	result = collection.update(condition, student) # 更新一条数据
	print("update result:", result)

	print("db collection names:", db.collection_names()) # 查看test数据库下所有表名称

	dblist = client.database_names() # 获取mongodb下所有数据库
	print("db list names:", dblist)
