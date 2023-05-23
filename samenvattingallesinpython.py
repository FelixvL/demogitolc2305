# https://flask.palletsprojects.com/en/2.3.x/quickstart/#a-minimal-application
# https://opendatascience.com/top-7-most-essential-python-libraries-for-beginners/
# https://www.interviewbit.com/blog/python-libraries/

# https://github.com/FelixvL/demogitolc2305

print("welkom")
mijnvar = input("ik wil je voornaam weten")
print(mijnvar)
#mijnvar = 18
resultaat = mijnvar.endswith("z")
print(resultaat)

lijstje = [14, 12, 7, 8]
r = lijstje.append(25)
s = lijstje.index(12)
print(r)
print(s)

# ===========================================


import pandas

allepokemons = pandas.read_csv("Pokemon.csv")
print(type(allepokemons))
print(allepokemons.columns)
for fred in allepokemons["Name"]:
    print(fred)

fiets = input("favorite pokemon: ")
for i, pokemon in allepokemons.iterrows():
    print(i)
    if(pokemon["Name"] == fiets):
        print("Gevonden Hij is Legendary: ", pokemon["Legendary"])


# ===========================================




import matplotlib.pyplot as plt
import numpy as np



plt.style.use('_mpl-gallery')

# make data
np.random.seed(3)
x = 0.5 + np.arange(8)
y = np.random.uniform(2, 7, len(x))

# plot
fig, ax = plt.subplots()

ax.stem(x, y)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()

# ===========================================


import mariadb

mydb = mariadb.connect(
  host="localhost",  #port erbij indien mac
  user="root",
  password="",
  database="olc2305dbdemo"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM product")



myresult = mycursor.fetchall()

for x in myresult:
  print(x[1])

gaan = input("vul naam in")
sql = "INSERT INTO product (naam, prijs) VALUES (%s, %s)"
val = (gaan, 21)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

