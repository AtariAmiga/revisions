import time
from random import randrange

temps_max_alloue_en_s = 15
# Je construis la liste des questions
liste_questions = []

for i in range(1, 10 + 1):
    for j in range(i, 10 + 1):
        question = (i, j)
        liste_questions.append(question)

# On interroge
while True:
    questions_a_poser_a_nouveau = []
    while len(liste_questions) > 0:
        n = randrange(len(liste_questions))
        question_au_hasard = liste_questions.pop(n)
        i = question_au_hasard[0]
        j = question_au_hasard[1]

        while True:
            print(i, 'x', j, '= ?')
            instant_de_depart = time.time()
            while True:
                try:
                    r = int(input())
                    break
                except ValueError:
                    pass

            temps_de_reponse_en_s = time.time() - instant_de_depart
            if r == i * j:
                print( "Bravo ! (reste", len(liste_questions), "questions)")
                if temps_de_reponse_en_s > temps_max_alloue_en_s:
                    print("Cependant tu as mis plus de " + str(temps_max_alloue_en_s) + "s pour répondre: je te poserai cette question à nouveau")
                    questions_a_poser_a_nouveau.append(question_au_hasard)
                break
            else:
                print( "Tu t'es trompé, recommence" )
                questions_a_poser_a_nouveau.append(question_au_hasard)

    liste_questions = questions_a_poser_a_nouveau
    if len(questions_a_poser_a_nouveau) == 0:
        print( "Bravo, tu as tout bien révisé !")
        break
    else:
        print( "Bravo, on va réviser les mauvaises réponses")