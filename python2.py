a = {}

a["이름"] = "김정민"
a["나이"] = "24살"
a["학번"] = "2018xxxxxx"
a["학과"] = "문헌정보학과"
a["생일"] = "19990207"

print(a)
print(len(a))
print()

del a["이름"]
del a["나이"]
del a["학번"]
del a["학과"]
del a["생일"]

print(a)
print(len(a))
print()

a = dict(이름 = "김정민", 나이 = "24살", 학번 = "2018xxxxxx", 학과 = "문헌정보학과", 생일 = "19990207")

print(a)
print(len(a))
print()

a.clear()
print(a)
print(len(a))