enum = ['one', 'two', 'three']
print(list(enumerate(enum)))
print(list(enumerate(enum, start=100)))
for i, value in enumerate(enum):
    print(i)

i = 0
seq = ['one', 'two', 'three']
for element in seq:
    print(i, seq[i])
    i += 1

seq = ['one', 'two', 'three']
for element in seq:
    print(element)

zidian = {"1": "11", "2": "22"}
for x in zidian.items():
    print(list(x))
