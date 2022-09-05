
#x^n=x*x^n-1
def puissance(x, n):
	if n==1:
		return x
	return x*puissance(x,n-1)

print(puissance(2,8))

def gauss(n):
	if n==0:
		return n
	return n + gauss(n-1)


def nb_arbres(n, nb_arbre):
	if n==0:
		return nb_arbre
	# on enleve 5% et on rajoute 3000
	return nb_arbres(n-1, nb_arbre-(5/100*nb_arbre)+3000)


#combien d'arbres il y aura dans 20 ans
#on commence avec 50 000 arbres
print(nb_arbres(20, 50000))
#> 56415.14077591459

print(gauss(5))