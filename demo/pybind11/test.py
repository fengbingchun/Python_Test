import example

# Blog: https://blog.csdn.net/fengbingchun/article/details/123022405

print("\n1.test simple function")
print("random number:", example.get_random_number(min=1, max=100))

print("\n2.test class:")
p = example.Pet("Molly")
print("name:", p.getName())
p.setName("Charly")
print("name:", p.getName())
print("age:", p.getAge())
print("name:", p.name)
p.name = "Molly"
print("name:", p.name)

print("\n3.test lambda function")
print("p:", p)

print("\n4.test inheritance class:")
p = example.Dog("Molly")
print("name:", p.name)
print("bark:", p.bark())

print("\n5.test polymorphic class:")
p = example.pet_store2()
print("type:", type(p))
print("bark:", p.bark())

print("\n6.test overload methods:")
p = example.Pet2("Molly", 10)
p.set("Charly")
p.set(18)
print("name:", p.getName())
print("age:", p.getAge())

print("\n7.test nested types")
p = example.Pet3("Lucy", example.Pet3.Cat)
print(f"type: {p.type}, value: {int(p.type)}")
print("Kind members:", p.Kind.__members__)