from random import randrange

liste_questions = []

# Je construis la liste des questions
for i in range(1, 11):
    for j in range(i, 11):
        question = (i, j)
        liste_questions.append(question)

while True:
    mauvaises_reponses = []
    while len(liste_questions) > 0:
        n = randrange(len(liste_questions))
        question_au_hasard = liste_questions.pop(n)
        i = question_au_hasard[0]
        j = question_au_hasard[1]

        while True:
            print(i, 'x', j, '= ?')
            while True:
                try:
                    r = int(input())
                    break
                except ValueError:
                    pass

            if r == i * j:
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