memory = 1.44
pages = 100
lines = 50
symbols = 25
coding = 4
mem_capacity = 1024
result = round(memory * mem_capacity * mem_capacity / pages / lines / symbols / coding)

print("Количество книг, помещающихся на дискету:", result)
