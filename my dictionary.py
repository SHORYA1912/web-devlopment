My__dict__={}
My__dict__={1:"apple",2:"ball"}
My__dict__={"name":"John",1:[234]}
print(My__dict__["name"])
print(My__dict__.get("age"))
My__dict__['age'] = 27
print(My__dict__)
My__dict__['address'] = "downtown"
print(My__dict__)
My__dict__.pop("age")
print("address:",My__dict__.get("address")) 
My__dict__.clear()
print(My__dict__)   

