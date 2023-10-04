memory = 1.44
pages = 100
lines = 50
symbols = 25
coding = 4
result = round(memory * 1024 * 1024 / pages / lines / symbols / coding)

print("Количество книг, помещающихся на дискету:", result)
