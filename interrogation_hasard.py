from random import randrange

liste_questions = []

# Je construis la liste des questions
for i in range(1, 11):
    for j in range(1, 11):
        question = (i, j)
        liste_questions.append(question)

bonnes_responses = []
mauvaises_reponses = []

while len(liste_questions) > 0:
    n = randrange(len(liste_questions))
    question_au_hasard = liste_questions.pop(n)
    print( question_au_hasard )