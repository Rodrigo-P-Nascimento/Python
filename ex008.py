print("\033[33m=-=" * 20)
print("Conversor barato de metros em centímetros e milímetros")
print("=-=" * 20 )
metros = float(input("""\033[mDigite qual valor em metros será convertido para centímetros
e para milímetros: """))
dm = metros*10
km = metros/1000
dam = metros/10
hm = metros/100
cent = metros*100
mili = metros*1000
print("""\033[30mKM:\033[m {}
\033[31mHM:\033[m {}
\033[32mDAM:\033[m {}
\033[33mM:\033[m {}
\033[34mDM: \033[m{}
\033[35mCM: \033[m{}
\033[36mMM: \033[m{}""".format(km, hm, dam, metros, dm, cent, mili))