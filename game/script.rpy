# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Nareko", color="b3702f")
image nareko = im.Scale("placeholder.png",400,600)

    
# The game starts here.

label start:
    $ questions = ["touhou9","nododge"]
    $ total_questions = len(questions)
    $ correct = 0
    $ question_nr = 0
    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg_sphinx

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show nareko

    n 'Hello! This is the intro!'
    
    jump random_question
    
    label random_question:
        if question_nr == total_questions:
            jump ending
        else:
            $ question_nr = question_nr + 1
            $ question = renpy.random.choice(questions)
            $ print(questions)
            $ print(question)
            $ questions.remove(question)
            $ renpy.jump(question)

    label touhou9:
        n "Which is the 10th Touhou game?"
        menu:
            "Touhou 9":
                jump a_touhou9_1
            "Touhou 9.5":
                jump a_touhou9_2
            "Touhou 10":
                jump a_touhou9_3
            "Shoot the Bullet":
                jump a_touhou9_4
                
        label a_touhou9_1:
            "Correct!"
            $ correct = correct + 1
            jump random_question
        label a_touhou9_2:
            "No! That's just Shoot the Bullet."
            jump random_question
        label a_touhou9_3:
            "Incorrect!"
            jump random_question
        label a_touhou9_4:
            "Also incorrect!!"
            jump random_question

    label nododge:
        n "In the Omake.txt of EoSD, ZUN talks about the tendency of modern game developers to add gimmicks to their STGs that remove or deemphasize the need to dodge bullets."
        n "Which is the first Touhou game that can be beaten without dodging anything?"
        menu:
            "Touhou 1":
                jump a_nododge_1
            "Touhou 6":
                jump a_nododge_2
            "Touhou 9":
                jump a_nododge_3
            "Touhou 16":
                jump a_nododge_4
                
        label a_nododge_1:
            "Correct!"
            $ correct = correct + 1
            jump random_question
        label a_nododge_2:
            "No!"
            jump random_question
        label a_nododge_3:
            "Incorrect!"
            jump random_question
        label a_nododge_4:
            "Also incorrect!!"
            jump random_question

            
    label ending:
        n "You finished the quiz!"
        n "Correct answers [correct] out of [total_questions]"
        jump end_game
        
    label end_game:
        return
