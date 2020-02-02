from random import randrange

def operation(i, j): return i*j
operateur = 'x'
de = 1
a = 10

# Je construis la liste des questions
liste_questions = []

for i in range(de, a + 1):
    for j in range(i, 11):
        question = (i, j)
        liste_questions.append(question)

# On interroge
while True:
    mauvaises_reponses = []
    while len(liste_questions) > 0:
        n = randrange(len(liste_questions))
        question_au_hasard = liste_questions.pop(n)
        i = question_au_hasard[0]
        j = question_au_hasard[1]

        while True:
            print(i, operateur, j, '= ?')
            while True:
                try:
                    r = int(input())
                    break
                except ValueError:
                    pass

            if r == operation(i, j):
                print( "Bravo !")
                break
            else:
                print( "Tu t'es trompé, recommence" )
                mauvaises_reponses.append(question_au_hasard)

    liste_questions = mauvaises_reponses
    if len(mauvaises_reponses) == 0:
        print( "Bravo, tu as tout bien révisé !")
        break
    else:
        print( "Bravo, on va réviser les mauvaises réponses")