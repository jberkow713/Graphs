d = {
  "cat": "bob",
  "dog": 23,
  19: 18,
  90: "fish"
}

a = []
for k,v in d.items():
  if type(v) == int:
    a.append(v)

    b = 0
    for x in a:
      b += x 

      print(b)

