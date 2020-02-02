from random import randrange

liste_questions = []

# Je construis la liste des questions
for i in range(1, 4):
    for j in range(1, 4):
        question = (i, j)
        liste_questions.append(question)

mauvaises_reponses = []
while len(liste_questions) > 0:
    n = randrange(len(liste_questions))
    question_au_hasard = liste_questions.pop(n)
    i = question_au_hasard[0]
    j = question_au_hasard[1]

    while True:
        print(i, 'x', j, '= ?')
        r = int(input())
        if r == i * j:
            print( "Bravo !")
            break
        else:
            print( "Tu t'es trompé, recommence" )
            mauvaises_reponses.append(question_au_hasard)