import random

# result = dir(random)
# result = help(random)

result = random.random() # 0.0 ile 0.1 arasında bir sayı üretecek.
result = random.random() * 100
result = int(random.uniform(10,100)) #10 ile 100 arasında sayı üretir
result = random.randint(1,100) # 1 ile 100 arasında bir sayı üret ve sayı int olsun

greeting = 'hello theree'

names = ["berf", "güler", "soner", "zeyno","barış","şevval","havin"]

result = names[random.randint(0,(len(names) - 1))]
result = random.choice(names)
result = random.choice(greeting)

liste = list(range(10))
random.shuffle(liste) # normalde sırayla vermişti ama bu methodla yerleriini karıştıdık değiştirdik
result = liste

liste = range(100)
result = random.sample(liste,3) #listenin içerisinden rastgele 3 sayı almak istiyorrum
result = random.sample(names,2)

print(result)