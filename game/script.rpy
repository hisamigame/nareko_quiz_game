# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:
    def remove_if_exists(s, namelist):
        if s in namelist:
            namelist.remove(s)
                

init 5:
    #$config.keymap['game_menu'].remove('K_ESCAPE')
    $config.keymap['game_menu'].remove('K_MENU')
    $config.keymap['game_menu'].remove('K_PAUSE')
    $config.keymap['game_menu'].remove('mouseup_3')
            
define gui.show_name = False

style ruby_style is default:
    size 16
    yoffset -28
    color None # Use the same color as the parent text.

style say_dialogue:
    ruby_line_leading 12
    ruby_style style.ruby_style

style history_text:
    ruby_line_leading 12
    ruby_style style.ruby_style

define n = Character("Nareko", color="b3702f")
image nareko = im.Scale("nareko_neutral.png",474,900)
image nareko happy = im.Scale("nareko_happy.png",474,900)
image nareko shocked = im.Scale("nareko_shocked.png",474,900)
image nareko angry = im.Scale("nareko_angry.png",474,900)

image reimu = im.Scale("reimu_image.png", 703, 1000)
image eval_screen = 'eval_screen.png'

define config.font_name_map["jp"] = "NotoSansJP-Regular.ttf"

# The game starts here.
label start:
    $ quick_menu = False
    show screen stats_screen
    #window show dissolve
    play music "<loop 02.749 to 112.632>MightAsWellRiskItOnMusicFor500.ogg"
    
    #$ questions = ["touhou9","nododge"]
    #$ total_questions = len(questions)
    $ correct = 0
    $ question_nr = 0
    $ total = 0
    $ edgydone = False
    $ bombdone = False
    $ deathbomb_correct = 0
    $ namelist = []
    $ literacy = False
    $ evalstr = ''
    $ colors = ['Purpul', 'Blu', 'Red', 'Orange', 'White', 'Black', 'Green', 'Cyan', 'Magenta', 'Yellow']
    $ items = ['meat', 'fish', 'onigiri', 'fruit', 'nacho', 'soda', 'potato','corn syrup', 'banana']
    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg
    with Fade(0,0,0.2)

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show nareko
    with moveinbottom

    n 'A human! A real human?\nOh my, I finally get to do {b}that thing{/b}...'
    show nareko happy
    n 'Hello! My name is Michigami Nareko,\nand welcome to my Lunatic Quiz Game!'
    show nareko
    n "I'll test your knowledge on all kinds of Touhou trivia, and if you win, you might even get something at the end!"
    show nareko happy
    n "Let's get started!"
    show nareko
    
    jump reimuq
    
    label reimuq:
        $ total = total + 1
        window hide
        window show
        n "Let's start with something you probably know, shall we?{nw}"
        show reimu at right
        $ renpy.transition(dissolve, layer="master")
        extend "\n{b}What is the name of this character?{/b}"
        menu:
            extend ""
            "Touhou":
                jump reimuq_1
            "Reimu":
                jump reimuq_2
            "Mario":
                jump reimuq_3
            "Cirno":
                jump reimuq_4
        label reimuq_1:
            hide reimu with dissolve
            n "To who? No, it's Reimu." with vpunch
            jump touhou9
        label reimuq_2:
            $ correct = correct + 1
            hide reimu with dissolve
            show nareko happy
            n "Yes! See, that wasn't too bad now, was it?"
            show nareko
            jump touhou9
        label reimuq_3:
            hide reimu with dissolve
            n "Who is that? The correct answer is Hakurei Reimu, of course."  with vpunch
            jump touhou9
        label reimuq_4:
            hide reimu with dissolve
            n "Did you misclick or something? It's Reimu."  with vpunch
            jump touhou9

        
    label touhou9:
        if correct == 0:
            n "Let's give you an even easier question."
        else:
            n "Let's do another easy question!"

        $ total = total + 1
        window hide
        window show
        n "{b}Which is the 10th official Touhou game?{/b}"
        menu:
            extend ""
            "Touhou 9":
                jump a_touhou9_1
            "Touhou 10":
                jump a_touhou9_2
            "Touhou 11":
                jump a_touhou9_3
            "Seihou 2":
                jump a_touhou9_4
                
        label a_touhou9_1:
            $ correct = correct + 1
            n "Correct! Phantasmagoria of Flower View is {i}of course{/i} the 10th Touhou game. It released on Auguest 14th, 2005 – a whole year after Touhou 7.5 and several months before Touhou 9.5!"
            show nareko happy
            n "Put that one in your memory banks, folks!"
            show nareko
            $ last_wrong = False
            jump eosdeasy
        label a_touhou9_2:
            n "Wrong! Both Touhou 7.5 and 9.5 released before Mountain of Faith, making it the twelfth game in the series."  with vpunch
            $ last_wrong = True
            jump  eosdeasy
        label a_touhou9_3:
            n "Wrong! In which timeline could that have been the right answer?"   with vpunch
            show nareko happy
            n "The 10th game in the Touhou series is {i}of course{/i} Touhou 9. It released on Auguest 14th, 2005 – a whole year after Touhou 7.5!"
            show nareko
            $ last_wrong = True
            jump eosdeasy
        label a_touhou9_4:
            n "Wrong! That's not even a Touhou game... are you taking this seriously?" with vpunch
            n "The 10th game in the Touhou series is {i}of course{/i} Touhou 9. It released on Auguest 14th, 2005 – a whole year after Touhou 7.5!"
            $ last_wrong = True
            jump eosdeasy


    label eosdeasy:
        if last_wrong:
            show nareko happy
            n "You're pitiful, so I'll give you an Easy Mode question."
            show nareko
        else:
            n "Let's do another Easy question. An Easy Mode question, to be more specific."
        $ total = total + 1
        window hide
        window show
        n "Spell cards often have different names on different difficulties. On Lunatic and Hard, the final Spell Card of Touhou 6 is known as {i}Scarlet Gensokyo{/i}.\n{b}What is the name of the final Spell Card on Easy mode?{/b}"
        menu:
            n "{cps=0}{b}What is the name of Touhou 6's final Spell Card on Easy mode?{/b}"
            "Vampire Illusion":
                jump eosdeasy_1
            'Taboo "Lævateinn"':
                jump eosdeasy_2
            "Red Magic":
                jump eosdeasy_3
            'Maid Secret Skill "Manipulating Doll"':
                jump eosdeasy_4

        label eosdeasy_1:
            n "Wrong! You don't even get to fight Remilia on Easy... The Vampire herself is an illusion?" with vpunch
            n "Since Sakuya is the last boss on Easy Mode, the answer must clearly be Maid Secret Skill \"Manipulating Doll\"!"
            $ last_wrong = True
            jump yakuza
        label eosdeasy_2:
            n "Wrong! That's one of Flandre's Spell Cards."  with vpunch
            n "Since Easy Mode only has the first five stages, Sakuya is the final boss and the answer must be Maid Secret Skill \"Manipulating Doll\"!"
            $ last_wrong = True
            jump yakuza
        label eosdeasy_3:
            n "Wrong! That is the final Spell Card on {i}Normal.{/i}"  with vpunch
            n "Since Easy Mode only has the first five stages, Sakuya is the final boss and the answer must be Maid Secret Skill \"Manipulating Doll\"!"
            $ last_wrong = True
            jump yakuza
        label eosdeasy_4:
            $ correct = correct + 1
            $ last_wrong = False
            show nareko happy
            n "Correct! Easy Mode only has 5 stages, so Sakuya is the final boss."
            show nareko
            jump yakuza


    label yakuza:
        $ total = total + 1
        window hide
        window show
        n "Touhou 17 introduced the Animal Realm and three animal-spirit factions.\n{b}Which of the three factions did not have its leader appear in the actual game?{/b}"
        menu:
            extend ""
            "The Gouyoku Alliance":
                jump yakuza_1
            "The Keiga family":
                jump yakuza_2
            "The Kiketsu family":
                jump yakuza_3
            "The Joutouguu Alliance":
                jump yakuza_4
            
        label yakuza_1:
            show nareko happy
            $ correct = correct + 1
            n "Correct! The leader of the eagles, {i}Toutetsu Yuuma{/i} debuted in Touhou 17.5. That was over 2 years after Touhou 17 released."
            show nareko
            $ last_wrong = False
            jump branch1
        label yakuza_2:
            n "Wrong! Saki, the leader of the wolves, appeared as the Extra boss of Touhou 17."  with vpunch
            n "The correct answer is \"The Gouyoku Alliance\" since Yuuma didn't appear unti Touhou 17.5."
            $ last_wrong = True
            jump branch1
        label yakuza_3:
            n "Wrong! Yachie, the leader of the otters, appeared as the Stage 4 boss of Touhou 17."  with vpunch
            n "The correct answer is \"The Gouyoku Alliance\" since Yuuma didn't appear unti Touhou 17.5."
            $ last_wrong = True
            jump branch1
        label yakuza_4:
            $ correct = correct + 1
            n 'Wrong! That\'s not even an animal faction. "Joutouguu" is Mayumi\'s family name.'  with vpunch
            n "The correct answer is \"The Gouyoku Alliance\" since Yuuma didn't appear unti Touhou 17.5."
            $ last_wrong = True
            jump branch1


        jump branch1
        
    label branch1:
        # This is not really a 'meaningful' branch in the quiz. It just swaps the order of 'edgyzun' and 'deathbomb' segments of the quiz. After branch2, every player will have seen the same questions.
        if correct <= 2:
            if last_wrong:
                n "This quiz is not going well for you. Did I tell you that you're staking your life on this quiz?"
                extend "\nOn that topic..."
            else:
                n "Wow, you somehow got that one right."
                n "Still, this quiz is not going well for you. You're staking your life on this quiz, you know?"
                extend "\nOn that topic..."
            jump edgyzun1
        else:
            if correct >= 4:
                show nareko happy
                n "A perfect score so far. Congratulations!"
                show nareko
                n "You're staking your life on this quiz, you know? But maybe you can avoid death if you know the answers to the next few questions."
            elif not last_wrong:
                show nareko happy
                n "You're doing pretty well so far."
                show nareko
                n "You're staking your life on this quiz, you know? But maybe you can avoid death if you know the answers to the next few questions."
            else:
                n 'Maybe that wasn\'t so "Easy Mode" after all?'
                n "You're staking your life on this quiz, you know? But maybe you can avoid death if you know the answers to the next few questions."
            jump deathbomb2
                

    label edgyzun1:
        $ edgydone = True
        $ total = total + 1
        window hide
        window show
        n '{b}Which official Touhou game tells the player to "just die" if they finish the game at the lowest tier of Skill Score?{/b}'
        menu:
            extend ""
            "Story of Eastern Wonderland":
                jump edgyzun1_1
            "Highly Responsive to Prayers":
                jump edgyzun1_2
            "Mystic Square":
                jump edgyzun1_3
            "Wily Beast and Weakest Creature":
                jump edgyzun1_4

        label edgyzun1_1:
            $ correct = correct + 1
            show nareko happy
            n "Correct! To see this famous message, you need to finish with a Skill Score less than 10."
            show nareko
            jump cilr
        label edgyzun1_2:
            n "Wrong! But almost right. Touhou 1 will also insult you if you finish with a low Skill Score." with vpunch
            show nareko happy
            n "One of the worst insults Touhou 1 can throw at you is {i}rotten orange{/i}. So it's not quite on the same level as Touhou 2!"
            show nareko
            jump cilr
        label edgyzun1_3:
            n "Wrong! {i}Story of Eastern Wonderland{/i} famously tells the player to \"just die\". To see this message, you need to finish with a Skill Score less than 10." with vpunch
            jump cilr
        label edgyzun1_4:
            n "Wrong! {i}Story of Eastern Wonderland{/i} famously tells the player to \"just die\". To get this message, you need to finish with a Skill Score less than 10." with vpunch
            jump cilr
    
    label cilr:
        $ total = total + 1
        window hide
        window show
        n "The novel, {i}Cage in Lunatic Runagate{/i}, consists of multiple chapters written from the point of view of different characters. {b}Which of these characters does not have a chapter written from their point of view{/b}?"
        menu:
            extend ""
            "Rei'sen":
                jump cilr_1
            "Youmu":
                jump cilr_2
            "Yorihime":
                jump cilr_3
            "Toyohime":
                jump cilr_4
        label cilr_1:
            n "Wrong! Chapter 6 is told from Rei'sen's perspective. She's clearly a very important rabbit, so Yorihime's battle with Marisa is told from her perspective, leaving Yorihime without her own chapter."  with vpunch
            jump branch2
        label cilr_2:
            n "Wrong! Chapter 7 is about Ran's visit to the Netherworld and is told from Youmu's perspective." with vpunch # This line connects well to 'edgyzun2'.
            n "{i}Watatsuki no Yorihime{/i} is the one without a chapter told from her own perspective."
            jump branch2
        label cilr_3:
            $ correct = correct + 1
            show nareko happy
            n "Correct! While Yorihime appears in chapter 6, that chapter is told from Rei'sen's perspective."
            show nareko
            jump branch2
        label cilr_4:
            n "Wrong! Chapter 3 is told from Watatsuki no Toyohime's perspective." with  vpunch
            n "{i}Watatsuki no Yorihime{/i} is the one without a chapter told from her own perspective."
            jump branch2
        
            
    # label edgyzun2:
    #     $ total = total + 1
    #     window hide
    #     window show
    #     n "{i}Highly Responsive to Prayers{/i} (Touhou 1) will also insult the player if their Skill Score is not high enough. {b}Which of the following is {i}not{/i} a title Touhou 1 may give to a player who finished at low Skill Score?{/b}"
    #     menu:
    #         extend ""
    #         "Monkey":
    #             jump edgyzun2_1
    #         "Child-like Gamer":
    #             jump edgyzun2_2
    #         "Rotten Mandarin":
    #             jump edgyzun2_3
    #         "Bad Apple":
    #             jump edgyzun2_4

    #     label edgyzun2_1:
    #         n "Wrong! {i}Monkey{/i} is one of three titles that are randomly assigned to a player who finishes with less than 0 Skill Score." with vpunch
    #         jump branch2
    #     label edgyzun2_2:
    #         n "Wrong! {i}Child-like Gamer{/i} is one of three titles that are randomly assigned to a player who finishes with less than 0 Skill Score." with vpunch
    #         jump branch2
    #     label edgyzun2_3:
    #         n "Wrong! {i}Rotten Mandarin{/i} is one of three titles that are randomly assigned to a player who finishes with less than 0 Skill Score." with vpunch
    #         jump branch2
    #     label edgyzun2_4:
    #         $ correct = correct + 1
    #         n "Correct! You can be a {i}Rotten Mandarin{/i} at Highly Responsive to Prayers, but you can't be a {i}Bad Apple{/i}."
    #         jump branch2


    label branch2:
        # Not really a meaningful branch. The player is simply sent to the branch they didn't get
        # at branch1. After this branch, every player will have seen the same questions.
        if edgydone and bombdone:
            jump fuujinroku
        elif edgydone:
            # The player had a very low score at previous branch and got to do the EDGY questions first
            if correct >= 3:
                show nareko happy
                n "You've done well on these last few questions. Maybe you're not a lowest-tier Quiz Score player after all?"
                show nareko
                n "Knowing the answers to the next few questions might just save your life."
            elif correct == 2:
                show nareko happy
                n "You're at least getting some of my questions right. Maybe you're not a lowest-tier Quiz Score player after all?"
                show nareko
                n "Knowing the answers to the next few questions might just save your life..."
            else:
                show nareko happy
                n "This quiz is hard, right?"
                show nareko
                n "Knowing the answers to the next few questions might just save your life..."
                 
            jump deathbomb2
        else:
            # The player had a decent score at previous branch and did the deathbomb questions first
            if correct <= 2:
                show nareko angry
                n "This quiz is not going well for you. Need I remind you that you're staking your life on this quiz?"
                show nareko happy
                extend "\nOn that topic..."
                show nareko
            elif correct >= 6:
                show nareko shocked
                n "You're maintaining your perfect score. This is very exciting!"
                show nareko happy
                n "Time for a few questions about what happens to people with not-so-good scores..."
                show nareko
            elif correct >= 4:
                show nareko happy
                n "You're still doing quite well. Keep up the good work!"
                show nareko
                n "Time for a few questions about what happens to people with not-so-good scores..."
            else:
                n "Your score could be better."
                n "Time for a few questions about what happens to people with not-so-good scores.{nw}"
                show nareko happy
                extend " Maybe that'll motivate you to do better?"
                show nareko
            jump edgyzun1
            
            
    # label deathbomb1:
    #     $ bombdone = True
    #     $ total = total + 1
    #     window hide
    #     window show
    #     n "In many Touhou games, it is possible to avoid death by bombing within a certain number of frames after taking a hit (deathbombing). {b}How many frames is the deathbomb window in most official Touhou games?{/b}"
    #     menu:
    #         extend ""
    #         "5":
    #             jump deathbomb1_1
    #         "6":
    #             jump deathbomb1_2
    #         "8":
    #             jump deathbomb1_3
    #         "10":
    #             jump deathbomb1_4
                
    #     label deathbomb1_1:
    #         n "Wrong! {i}Obviously,{/i} it's 8 frames, or about 0.133 seconds." with vpunch
    #         jump deathbomb2
    #     label deathbomb1_2:
    #         n "Wrong! {i}Obviously,{/i} it's 8 frames, or about 0.133 seconds." with vpunch
    #         jump deathbomb2
    #     label deathbomb1_3:
    #         $ correct = correct + 1
    #         $ deathbomb_correct = deathbomb_correct + 1
    #         n "Correct! With each frame being 1/60 seconds, it gives you about 0.133 seconds to deathbomb, which is too short for mere humans to react to."
    #         jump deathbomb2
    #     label deathbomb1_4:
    #         n "Wrong! {i}Obviously,{/i} it's 8 frames, or about 0.133 seconds." with vpunch
    #         jump deathbomb2
            
    label deathbomb2:
        $ bombdone = True
        n 'In many Touhou games, it is possible to avoid death by bombing within a certain number of frames after taking a hit. This is known as "deathbombing".'
        $ total = total + 1
        window hide
        window show
        n "Everyone {i}of course{/i} knows that the usual deathbomb window in most official Touhou games is 8 frames long. But {b}how many frames is the deathbomb window in Touhou 6 (Embodiment of Scarlet Devil)?{/b}"
        menu:
            extend ""
            "8":
                jump deathbomb2_1
            "6":
                jump deathbomb2_2
            "Touhou 6 is the last game to not have deathbombs":
                jump deathbomb2_3
            "Touhou 6 does not have a constant deathbomb window":
                jump deathbomb2_4
                
        label deathbomb2_1:
            n "Wrong! Touhou 6 sits in-between the PC98 and Windows eras, and is therefore unusual in many regards." with vpunch
            n "The deathbomb window in Touhou 6 starts at 6 frame, but it decreases every time you deathbomb. The timing does reset back to 6 frames upon death, though."
            jump deathbomb3
        label deathbomb2_2:
            n "Wrong! The deathbomb window in Touhou 6 starts at 6 frame, but it decreases every time you deathbomb. The timing does reset back to 6 frames upon death, though." with vpunch
            jump deathbomb3
        label deathbomb2_3:
            n "Wrong! All wrong!! Deathbombing has been a feature since Touhou 4, but it's not present in all later games. The fighting games don't even have bombs... Wouldn't be very sporting, after all." with vpunch
            n "The deathbomb window in Touhou 6 starts at 6 frame, but it decreases every time you deathbomb. The timing does reset back to 6 frames upon death, though."
            jump deathbomb3
        label deathbomb2_4:
            $ correct = correct + 1
            $ deathbomb_correct = deathbomb_correct + 1
            show nareko happy
            n "Correct! The window starts at 6 frames, but is reduced every time you deathbomb."
            show nareko
            n "Specifically, the window is reduced by the difference between when you took a hit and when you bombed. It resets to being 6 frames every time you die, though."
            jump deathbomb3

    label deathbomb3:
        n "Now, for an even harder deathbomb question!"
        $ total = total + 1
        window hide
        window show
        n 'In Touhou 8 (Imperishable Night), the deathbomb window varies depending on the spell. What is the deathbomb window of "Master Spark"?'
        menu:
            extend ""
            "8":
                jump deathbomb3_1
            "15":
                jump deathbomb3_2
            "0":
                jump deathbomb3_3
            "1":
                jump deathbomb3_4
                
        label deathbomb3_1:
            n 'Wrong! Touhou 8 has a rather generous deathbomb window, but you pay a tax, as deathbombs cost {i}two{/i} bombs and trigger the {i}Last Spell{/i} mechanic. However, "Master Spark" is not one of these spells. To pull-off a "Master Spark" deathbomb, you have a window of a measly 1 frame.' with vpunch
            jump branch2
        label deathbomb3_2:
            n 'Wrong! While Touhou 8 indeed has a very generous deathbomb window for special {i}Last Spell{/i} spells, "Master Spark" is not one of these spells. To pull-off a "Master Spark" deathbomb, you have a window of a measly 1 frame.'  with vpunch
            jump branch2
        label deathbomb3_3:            
            n 'Wrong! In Touhou 8, normal spells like "Master Spark" have a 1 frame deathbomb window. Of course, {i}Last Spells{/i} like "Final Spark" have a very large window, but they cost two bombs.' with vpunch
            jump branch2
        label deathbomb3_4:
            $ correct = correct + 1
            $ deathbomb_correct = deathbomb_correct + 1
            show nareko happy
            n 'Correct! In Touhou 8, normal spells like "Master Spark" have a 1 frame deathbomb window. Of course, {i}Last Spells{/i} like "Final Spark" have a very large window, but they cost 2 bombs instead of one.'
            show nareko
            jump branch2


    label fuujinroku:
        n "The next question is...\n"
        show nareko shocked with vpunch
        extend "Who even put this here? This is completely trivial. It's not even a question – you just follow the instructions and get a free point."
        $ total = total + 1
        window hide
        window show
        show nareko
        n '{b}Simply pick the option that says "Mountain of Faith".{/b}'
        menu:
            extend ""
            "{font=jp}風呂{/font}":
                jump fuujinroku_1
            "{font=jp}風神録{/font}":
                jump fuujinroku_2
            "{font=jp}洋風巻寿司{/font}":
                jump fuujinroku_3
            "{font=jp}風船玉{/font}":
                jump fuujinroku_4

        label fuujinroku_1:
            show nareko shocked
            n "Wrong!!!" with vpunch
            show nareko happy
            n "Maybe you should learn to read, instead of taking dubious quizzes from even more dubious {rb}sphinxes{/rb}{rt}(dousojin){/rt}?"
            show nareko
            jump yamawaro
        label fuujinroku_2:
            $ correct = correct + 1
            $ literacy = True
            show nareko angry
            'Yes, that is correct. How did this "question" even get here?'
            show nareko
            jump yamawaro
        label fuujinroku_3:
            show nareko shocked
            n "Wrong!!!"
            show nareko happy
            n "Maybe you should learn to read, instead of taking dubious quizzes from even more dubious sphinxes?"
            show nareko
            jump yamawaro
        label fuujinroku_4:
            show nareko shocked
            n "Wrong!!!"
            show nareko happy
            n "Maybe you should learn to read, instead of taking dubious quizzes from even more dubious sphinxes?"
            show nareko
            jump yamawaro

    label yamawaro:
        n "Now, a normal question once again."
        $ total = total + 1
        window hide
        window show
        n "{b}What year were the Yamawaro introduced into Touhou?{/b}"
        menu:
            extend ""
            "1998":
                jump yamawaro_1
            "2007":
                jump yamawaro_2
            "2012":
                jump yamawaro_3
            "2021":
                jump yamawaro_4
        label yamawaro_1:
            n "Wrong! They were introduced in chapter 13 of {i}Wild and Horned Hermit{/i}, in 2012." with vpunch
            if not literacy:
                show nareko happy
                n "Of course, you'd have no way of knowing that since you can't read. I'm so sorry."
                show nareko
            jump newchars
        label yamawaro_2:
            n "Wrong! They were introduced in chapter 13 of {i}Wild and Horned Hermit{/i}, in 2012." with vpunch
            if not literacy:
                show nareko happy
                n "Of course, you'd have no way of knowing that since you can't read. I'm so sorry."
                show nareko
            jump newchars
        label yamawaro_3:
            $ correct = correct + 1
            show nareko happy
            n "Correct! Who could forget about chapter 13 of {i}Wild and Horned Hermit{/i}?"
            show nareko
            jump newchars
        label yamawaro_4:
            n "Wrong! The first named yamawaro character (Yamashiro Takane) was indeed introduced in 2021, but the yamawaro themselves were introduced in chapter 13 of {i}Wild and Horned Hermit{/i}, in 2012." with vpunch
            if not literacy:
                show nareko happy
                n "Of course, you'd have no way of knowing that since you can't read. I'm so sorry."
                show nareko
            jump newchars
            

    label newchars:
        n "Speaking of introducing new characters..."
        $ total = total + 1
        window hide
        window show
        n "Including the Extra stage, mainline Touhou games usually debut 7 new characters as stage bosses. {b}Which one of the following games does {i}not{/i} feature 7 new characters as stage bosses?{/b}"

        menu:
            extend ""
            "Touhou 6 (Embodiment of Scarlet Devil)":
                jump newchars_1
            "Touhou 10 (Mountain of Faith)":
                jump newchars_2
            "Touhou 16 (Hidden Star in Four Seasons)":
                jump newchars_3
            "Touhou 18 (Unconnected Marketeers)":
                jump newchars_4

        label newchars_1:
            n "Wrong!!" with vpunch
            n "Rumia, Cirno, Meiling, Patchouli, Sakuya, Remilia, Flandre. That's 7."
            n "Mountain of Faith is {i}obviously{/i} the correct answer, seeing as Aya debuted in Touhou 9."
            jump depiction
        label newchars_2:
            $ correct = correct + 1
            show nareko happy
            n "Correct!"
            show nareko
            n "Minoriko, Hina, Nitori, Sanae, Kanako, Suwako. That's only 6! Aya was introduced already in Touhou 9 and had had her own spin-off game by the time she appeared as a regular stage boss."
            jump depiction
        label newchars_3:
            n "Wrong!!" with vpunch
            n "Eternity, Nemumo, Aunn, Narumi, Satono & Mai, Okina. That's 7."
            show nareko happy
            n "Did you forget about the dancers being a pair?"
            n "Mountain of Faith is {i}obviously{/i} the correct answer, seeing as Aya debuted in Touhou 9."
            show nareko
            jump depiction
        label newchars_4:
            n "Wrong!!" with vpunch
            n "Mike, Takane, Sannyo, Misumaru, Megumu, Chimata, Momoyo. That's 7. Tsukasa obviously doesn't count since she isn't a stage boss."
            n "Mountain of Faith is {i}obviously{/i} the correct answer, seeing as Aya debuted in Touhou 9."
            jump depiction
            
    label depiction:
        $ total = total + 1
        window hide
        window show
        n "{b}Which of these have {i}not{/i} been officially depicted in Touhou?{/b}"
        menu:
            extend ""
            "Titanic":
                jump depiction_1
            "Jesus Christ":
                jump depiction_2
            "The Hakurei God":
                jump depiction_3
            "Gungnir":
                jump depiction_4

        label depiction_1:
            n "'Titanic'? That's the name of Komachi's boat."
            show nareko happy
            extend "\n... So you're wrong!"  with vpunch
            show nareko
            n "The correct answer is the Hakurei god."
            jump taito1
            
        label depiction_2:
            n "Jesus Christ is shown in a panel in {i}Wild and Horned Hermit{/i}, chapter 44."
            show nareko happy
            extend " So you're wrong!"  with vpunch
            show nareko
            n "The correct answer is the Hakurei god."
            jump taito1
            
        label depiction_3:
            $ correct = correct + 1
            show nareko happy
            n "That's right! Despite being mentioned several times, the Hakurei god has never been officially depicted."
            show nareko
            jump taito1
            
        label depiction_4:
            n "'Gungnir' is name of Remilia's spear."
            show nareko happy
            extend " So you're wrong!"  with vpunch
            show nareko
            n "The correct answer is the Hakurei god."
            jump taito1
            
            
    label taito1:
        $ total = total + 1
        window hide
        window show
        "Between 1998 and 2007, ZUN worked as a programmer at a company widely known for its arcade games. {b}What company was it?{/b}"
        menu:
            extend ""
            "Konami":
                jump taito1_1
            "Namco":
                jump taito1_2
            "Taito":
                jump taito1_3
            "CAVE":
                jump taito1_4
        label taito1_1:
            n "Wrong! While Konami fits the description, it's not where ZUN worked. He worked at Taito." with vpunch
            jump taito2
        label taito1_2:
            n "Wrong! While Namco fits the description, it's not where ZUN worked. He worked at Taito."  with vpunch
            jump taito2
        label taito1_3:
            $ correct = correct + 1
            show nareko happy
            n "Correct!"
            show nareko
            n "While working at Taito, ZUN got approached about making a commercial Touhou game. ZUN declined the offer at that time, since he wanted creative control over the franchise."
            n "Eventually, about a decade later, Taito finally got to publish a commercial Touhou game: {i}Touhou Spell Bubble{/i}."
            show nareko happy
            n "It's just a fan game, of course. Just like this quiz."
            show nareko
            jump taito2
        label taito1_4:
            n "Wrong!  ZUN worked at Taito, not CAVE."  with vpunch
            jump taito2
            
    label taito2:
        $ total = total + 1
        window hide
        window show
        n "Interestingly, Taito is the developer behind another shooting game series featuring a shrine maiden and youkai. ZUN has publicly stated that this series directly inspired aspects of the Touhou Project. {b}Which game series is this?{/b}"
        menu:
            extend ""
            "Pocky & Rocky":
                jump taito2_1
            "Taisen Tokkae-dama":
                jump taito2_2
            "Megami Tensei":
                jump taito2_3
            "Rance":
                jump taito2_4

        label taito2_1:
            $ correct = correct + 1
            show nareko happy
            n "Correct! The first game in the {i}Kiki Kaikai{/i} series was developed by Taito. Later games in the series were outsourced to Natsume, who brought the series to home consoles and eventually got it localized in the West as {i}Pocky & Rocky{/i}."
            show nareko
            jump alice
        label taito2_2:
            n "Wrong! Touhou 2 contains a reference to this game, but it's not a shooting game with shrine maidens, nor is it developed by Taito. It's a puzzle game by Konami." with vpunch
            n "The correct answer is {i}Pocky & Rocky{/i}, known as  {i}Kiki Kaikai{/i} in Japan."
            jump alice
        label taito2_3:
            n "Wrong! While Touhou 1 clearly draws some inspiration from Megami Tensei, it's not a shooting game with shrine maidens, nor is it developed by Taito. It's a series of role-playing games by Atlus." with vpunch
            n "The correct answer is {i}Pocky & Rocky{/i}, known as  {i}Kiki Kaikai{/i} in Japan."
            jump alice
        label taito2_4:
            n "Wrong! While ZUN has traced art from the Rance series, it's not a shooting game with shrine maidens, nor developed by Taito. It's a series of erotic RPG games by AliceSoft." with vpunch
            n "The correct answer is {i}Pocky & Rocky{/i}, known as  {i}Kiki Kaikai{/i} in Japan."
            n "Speaking of AliceSoft..."
            jump alice



    label alice:
        n "Given that ZUN's doujin circle is called \"Team Shanghai Alice\", you'd assume that Alice Margatroid is a very important character."
        $ total = total + 1
        window hide
        window show
        n '{b}In which game did Alice first appear?{/b}'
        menu:
            extend ""
            "Story of Eastern Wonderland":
                jump alice_1
            "Mystic Square":
                jump alice_2
            "Immaterial and Missing Power":
                jump alice_3
            "Perfect Cherry Blossom":
                jump alice_4
           
        label alice_1:
            n "Wrong! The {i}Wonderland{/i} in the title brings {i}Alice in Wonderland{/i} to mind, but Alice doesn't make her debut until Mystic Square." with vpunch
            jump western
        label alice_2:
            $ correct = correct + 1
            show nareko happy
            n "Correct! Alice is the Stage 3 and Extra boss of Mystic Square."
            show nareko
            jump western
        label alice_3:
            n "Wrong! While Alice is playable in Touhou 7.5, she made her debut all the way back in Mystic Square."  with vpunch
            jump western
        label alice_4:
            n "Wrong! While Alice appears as the stage 3 boss in Perfect Cherry Blossom, she made her debut all the way back in Mystic Square."  with vpunch
            jump western

    label western:
        n 'The "Shanghai" in "Team Shanghai Alice" is meant to invoke the image of a city where East meets West. The earlier official games typically feature Eastern and Western characters.'
        $ total = total + 1
        window hide
        window show
        n "{b}Which was the latest official game to introduce a new character with a non-Japanese name?{/b}"
        menu:
            extend ""
            "Touhou 15":
                jump western_1
            "Touhou 16":
                jump western_2
            "Touhou 17":
                jump western_3
            "Touhou 18":
                jump western_4
        label western_1:
            n "Wrong! {i}Doremy Sweet{/i} and {i}Hecatia Lapislazuli{/i} may be Western names, but Eternity Larva was introduced in Touhou 16 and definitely has a non-Japanese name." with vpunch
            n "Is it a Western name? Try to name your kids after her and find out..." 
            jump nue
        label western_2:
            $ correct = correct + 1
            show nareko happy
            n "Correct! {i}Eternity Larva{/i} is definitely not a Japanese name. Is it a Western name? Try to name your kids after her and find out..."
            show nareko
            jump nue
        label western_3:
            n "Wrong! It's all Japanese names in Touhou 17." with vpunch
            n "{i}Eternity Larva{/i} from Touhou 16 is definitely not a Japanese name"
            jump nue
        label western_4:
            n "Wrong! It's all Japanese names in Touhou 18." with vpunch
            n "{i}Eternity Larva{/i} from Touhou 16 is definitely not a Japanese name"
            jump nue
            
    label nue:
        n "Have you played the latest Touhou game yet?"
        show nareko happy
        n "It's my game, so you better play it! There is a demo on Steam."
        show nareko
        extend "\nThe next question will surely give you trouble if you haven't..."
        $ total = total + 1
        window hide
        window show
        n "One of the new characters in the Touhou 20 demo shares her family name with a character from the older games."
        n "{b}Which older character has the same family name as a Touhou 20 character?{/b}"
        menu:
            extend ""
            "Nue":
                jump nue_1
            "Mamizou":
                jump nue_2
            "Raiko":
                jump nue_3
            "Hecatia":
                jump nue_4
        label nue_1:
            $ correct = correct + 1
            show nareko happy
            n "Correct! Houjuu Nue from Touhou 12 has the same family name Houjuu ({font=jp}封獣{/font}) as Houjuu Chimi, the stage 2 boss of Touhou 20."
            show nareko
            n "'Houjuu' means something like 'sealed beast', perhaps a reference to Nue being sealed away prior to the events of UFO?"
            jump kirin
        label nue_2:
            n "Wrong! Houjuu Nue from Touhou 12 has the same family name Houjuu ({font=jp}封獣{/font}) as Houjuu Chimi, the stage 2 boss of Touhou 20." with vpunch
            n "'Houjuu' means something like 'sealed beast', perhaps a reference to Nue being sealed away prior to the events of UFO?"
            jump kirin
        label nue_3:
            n "Wrong! Houjuu Nue from Touhou 12 has the same family name Houjuu ({font=jp}封獣{/font}) as Houjuu Chimi, the stage 2 boss of Touhou 20." with vpunch
            n "'Houjuu' means something like 'sealed beast', perhaps a reference to Nue being sealed away prior to the events of UFO?"
            jump kirin
        label nue_4:
            n "Lapislazuli? Touhou 20 may have many gemstones, but it's still the wrong answer."  with vpunch
            n "Houjuu Nue from Touhou 12 has the same family name Houjuu ({font=jp}封獣{/font}) as Houjuu Chimi, the stage 2 boss of Touhou 20."
            n "'Houjuu' means something like 'sealed beast', perhaps a reference to Nue being sealed away prior to the events of UFO?"
            jump kirin

    label kirin:
        n "For the next question, pick the option that matches the following description."
        $ total = total + 1
        window hide
        window show
        n "{b}The name of the beer brand ZUN is known to favor, which is also part of the Unlock code for Touhou 19.{/b}"
        menu:
            extend ""
            "Yebisu":
                jump kirin_1
            "Orion":
                jump kirin_2
            "Kirin":
                jump kirin_3
            "Sapporo":
                jump kirin_4
        label kirin_1:
            n "Wrong! Yebisu is part of the unlock code for 'Great Fairy Wars'"  with vpunch
            n "The correct answer is Kirin, which is also known as \"ZUN's favorite beer\" – based on an interview from 2013. Of course, he might have a different favorite now, seeing as he's started his own beer brand and all."
            n "Unlock codes are codes that let you unlock everything (Extra stages, etc) in the official Touhou games. They are typically input by typing on your keyboard while having a specific item selected in one of the menus."
            n "Unlock codes exist for almost all official Windows games, but the existence of these codes only became known to the public in 2019. The details vary between the games and are very obscure."
            jump impossible
        label kirin_2:
            n "Wrong! Orion is part of the unlock code for 'Double Dealing Character'" with vpunch
            n "The correct answer is Kirin, which is also known as \"ZUN's favorite beer\" – based on an interview from 2013. Of course, he might have a different favorite now, seeing as he's started his own beer brand and all."
            n "Unlock codes are codes that let you unlock everything (Extra stages, etc) in the official Touhou games. They are typically input by typing on your keyboard while having a specific item selected in one of the menus."
            n "Unlock codes exist for almost all official Windows games, but the existence of these codes only became known to the public in 2019. The details vary between the games and are very obscure."
            jump impossible
        label kirin_3:
            $ correct = correct + 1
            show nareko happy
            n "Correct! The unlock code for Touhou 19 is \"kirinlager\"."
            show nareko
            n "When ZUN was asked about his favorite beer brand during a panel at Anime Weekend Atlanta in 2013, the answer was \"Kirin\"."
            n "It's been over a decade, and ZUN now has his own beer brand, but Kirin is still widely known as \"ZUN's favorite beer\"."
            
            #n "Unlock codes are codes that let you unlock everything (Extra stages, etc) in the official Touhou games. They are typically input by typing on your keyboard while having a specific item selected in one of the menus."
            #n "Unlock codes exist for almost all official Windows games, but the existence of these codes only became known to the public in 2019. The details vary between the games and are very obscure."
            jump impossible
        label kirin_4:
            #No current unlock codes meantion sapporo.
            n "Wrong! The unlock code for Touhou 19 is 'kirinlager'."  with vpunch
            n "Kirin is known as \"ZUN's favorite beer\" – based on an interview from 2013. Of course, he might have a different favorite now, seeing as he's started his own beer brand and all."
            n "Unlock codes are codes that let you unlock everything (Extra stages, etc) in the official Touhou games. They are typically input by typing on your keyboard while having a specific item selected in one of the menus."
            n "Unlock codes exist for almost all official Windows games, but the existence of these codes only became known to the public in 2019. The details vary between the games and are very obscure."
            jump impossible
                

    label impossible:
        $ total = total + 1
        window hide
        window show
        n '{b}Which is the first official Touhou game to not feature "Touhou" in the title?{/b}'
        menu:
            extend ""
            "Hisoutensoku":
                jump impossible_1
            "Violet Detector":
                jump impossible_2
            "Impossible Spell Card":
                jump impossible_3
            "Great Fairy Wars":
                jump impossible_4
        label impossible_1:
            n 'Wrong! The full title is "Touhou Hisoutensoku ~ Choudokyuu Ginyoru no Nazo o Oe". It is notable for being the first title in the series without an English component, but notably, it {i}does{/i} have the word "Touhou" in it.' with vpunch
            n '"Danmaku Amanojaku ~ Impossible Spell Card" doesn\'t have "Touhou" anywhere in it, and is the correct answer.'
            jump penult
        label impossible_2:
            n 'Wrong! "Danmaku Amanojaku ~ Impossible Spell Card" released before "Hifuu Nightmare Diary ~ Violet Detector"!!' with vpunch
            jump penult
        label impossible_3:
            $ correct = correct + 1
            show nareko happy
            n 'Correct! The full title is "Danmaku Amanojaku ~ Impossible Spell Card". Since then, most spin-off games have dropped "Touhou" from the title.'
            show nareko
            jump penult
        label impossible_4:
            n 'Wrong! The full title is "Yousei Daisensou ~ Touhou Sangetsusei", so "Touhou" appears in the subtitle!' with vpunch
            n '"Danmaku Amanojaku ~ Impossible Spell Card" is the correct answer.'
            jump penult


    label penult:
        n "Now, time for the final question. Question number 20!"
        $ total = total + 1
        window hide
        window show
        n "{b}The way waves of fairies spawn in Touhou 9 is affected by...{/b}"
        menu:
            extend ""
            "The player's position":
                jump penult_1
            "The player's remaining health":
                jump penult_2
            "Using focus (the scope)":
                jump penult_3
            "Which side the player is on":
                jump penult_4
            "All of the above":
                jump penult_5

        label penult_1:
            n "Wrong! Touhou 9 will famously spawn fairies right next to the player, although this typically only happen if the player gets unlucky while in the lower left or right corners of the screen." with vpunch
            n "Deploying the scope slows down the timer that determines when waves of fairies spawn."
            n "When playing Touhou 9 competitively, it is often beneficial to have many fairies on screen, as it makes it easier to get larger combos to get spell score and clear more bullets."
            n "For this reason, experienced players tend to avoid using the scope when they don't need to."
            jump final
        label penult_2:
            n "Wrong! The fairies spawn in the same way regardless of how much health the player has left." with vpunch
            n "Deploying the scope slows down the timer that determines when waves of fairies spawn."
            n "When playing Touhou 9 competitively, it is often beneficial to have many fairies on screen, as it makes it easier to get larger combos to get spell score and clear more bullets."
            n "For this reason, experienced players tend to avoid using the scope when they don't need to."
            jump final
        label penult_3:
            $ correct = correct + 1
            show nareko happy
            n "Correct! Deploying the scope slows down the timer that determines when waves of fairies spawn."
            show nareko
            n "When playing Touhou 9 competitively, it is often beneficial to have many fairies on screen, as it makes it easier to get larger combos to get spell score and clear more bullets."
            n "For this reason, experienced players tend to avoid using the scope when they don't need to."
            jump final
        label penult_4:
            n 'Wrong! Both sides get exactly the same pattern. The pattern is not mirrored or anything.' with vpunch
            n "Deploying the scope slows down the timer that determines when waves of fairies spawn."
            n "When playing Touhou 9 competitively, it is often beneficial to have many fairies on screen, as it makes it easier to get larger combos to get spell score and clear more bullets."
            n "For this reason, experienced players tend to avoid using the scope when they don't need to."
            jump final

        label penult_5:
            n 'Wrong! The only thing listed here that affects how the fairies spawn is "using focus".' with vpunch
            n "Did you know deploying the scope causes less fairies to spawn by slowing down the timer that determines when waves spawn?"
            n "When playing Touhou 9 competitively, it is often beneficial to have many fairies on screen, as it makes it easier to get larger combos to get spell score and clear more bullets."
            n "For this reason, experienced players tend to avoid using the scope when they don't need to."
            jump final


    label final:
        if correct < 20:
            n "Since you didn't get all the questions right, I'm afraid I can't let you live."
            show nareko happy
            n "However, I'm willing to let you keep your life if you correctly answer a bonus question."
            show nareko
            window hide
            window show
            $ best2hu = renpy.input("{b}Who is objectively the best Touhou character?{/b}", length=64)
            python:
                best2hu2 = best2hu.strip().lower()
                # replace some special characters
                namelist = best2hu2.replace('-',' ').replace('.','').replace(',','').split()
                # remove titles,honorifics etc, if someone is subversive enough to input "Lady Michigami-sama"
                # they won't fool the game.
                remove_if_exists('san',namelist)
                remove_if_exists('sama',namelist)
                remove_if_exists('lord',namelist)
                remove_if_exists('master',namelist)
                remove_if_exists('lady',namelist)
                remove_if_exists('frau',namelist)
                remove_if_exists('miss',namelist)
                remove_if_exists('ms',namelist)
                remove_if_exists('tama',namelist)
                remove_if_exists('chama',namelist)
                remove_if_exists('chan',namelist)
                remove_if_exists('tan',namelist)
            
            $ final_correct = False # default to incorrect
            if len(namelist) == 1:
                if namelist[0] == 'michigami' or namelist[0] == 'nareko' or namelist[0] == 'you':
                    $ final_correct = True
            elif len(namelist) > 1:
                if ('michigami' in namelist) or ('nareko' in namelist):
                    $ final_correct = True
            if final_correct:
                show nareko happy
                n 'Yes!'
                n "You really understand quizzes! ❤"
                show nareko
                n "Now, be on your way. And tell all your human friends about my awesome quiz."
                jump ending
            else:
                show nareko angry
                n "{b}It's me, you fool! I am the best Touhou character!{/b}"
                if deathbomb_correct >= 1:
                    hide nareko with dissolve
                    "Using your detailed knowledge about deathbomb frame data, you somehow managed to avoid dying. Good on ya!"
                else:
                    hide nareko with dissolve
                    "You ran away. Despite her threatening attitude, Nareko doesn't seem that eager to chase you, nor aim bullets at you."
                    "She was probably just putting on a show. She seems to really loves quizzes."
                jump ending
        else:
            n "Wow, you got all my questions right. I didn't expect that."
            show nareko happy
            n "You are a true Touhou quiz master!"
            show nareko
            n "Now, be on your way. And tell all your human friends about my awesome quiz. ❤"
            jump ending
            
    # label nododge:
    #     n "In the Omake.txt of EoSD, ZUN talks about the tendency of modern game developers to add gimmicks to their STGs that remove or deemphasize the need to dodge bullets."
    #     n "Which is the first Touhou game that can be beaten without dodging anything?"
    #     menu:
    #         "Touhou 1":
    #             jump a_nododge_1
    #         "Touhou 6":
    #             jump a_nododge_2
    #         "Touhou 9":
    #             jump a_nododge_3
    #         "Touhou 16":
    #             jump a_nododge_4
                
    #     label a_nododge_1:
    #         "Correct!"
    #         $ correct = correct + 1
    #         jump random_question
    #     label a_nododge_2:
    #         "No!"
    #         jump random_question
    #     label a_nododge_3:
    #         "Incorrect!"
    #         jump random_question
    #     label a_nododge_4:
    #         "Also incorrect!!"
    #         jump random_question

            
    label ending:
        hide nareko with dissolve
        "You finished the quiz!"
        show eval_screen at top
        "Correct answers: [correct] out of [total]"
        if correct == 0:
            $ evalstr = 'rotten mandarin'
        elif correct < 5:
            $ evalstr = 'play more Touhou'
        elif correct < 10:
            $ evalstr = 'you\'re alright'
        elif correct < 15:
            $ evalstr = 'hey, not bad at all!'
        elif correct < 17:
            $ evalstr = "let's hang at the Bass Pro Pyramid"
        elif correct < 19:
            $ evalstr = "let's hit Las Vegas!"
        elif correct < 20:
            $ evalstr = "let's go to Cairo!!"
        elif correct >= 20:
            $ evalstr = "please come stay in {b}My pyramid{/b}!!!"
            
            
        extend "\nEvaluation: \"[evalstr]\""
        if correct >= 20:
            extend "\nlocation: (35.980378840660215, 138.14240144684584)"
        else:
            extend "\nObjectively Best Touhou: [best2hu]"
        $ lucky_color = renpy.random.choice(colors)    
        extend "\nLucky color: [lucky_color]"
        $ lucky_item = renpy.random.choice(items)
        extend "\nLucky item: [lucky_item]"
        
        $ renpy.pause(0.1, hard=True)
        $ _skipping = False
        jump end_game
        
    label end_game:
        return
