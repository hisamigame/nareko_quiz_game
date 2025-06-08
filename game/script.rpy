# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

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
image reimu = im.Scale("reimu_image.png", 703, 1000)

define config.font_name_map["jp"] = "NotoSansJP-Regular.ttf"

# The game starts here.
label start:
    
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

    n 'A human! A real human?\nThat means I finally get to do {b}that thing{/b}...'
    n 'Hello! My name is Michigami Nareko,\nand welcome to my Lunatic quiz game!'
    n "Here, we'll test your knowledge on all kinds of Touhou trivia.\nLet's get started!"

    #jump fuujinroku
    
    jump reimuq
    
    label reimuq:
        $ total = total + 1
        window hide
        window show
        n "Let's start with something you probably know.{nw}"
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
            "To who? No, it's Reimu." with vpunch
            jump touhou9
        label reimuq_2:
            $ correct = correct + 1
            hide reimu with dissolve
            "Yes! That wasn't too bad, was it?"
            jump touhou9
        label reimuq_3:
            hide reimu with dissolve
            "Who is that? The correct answer Hakurei Reimu, of course."  with vpunch
            jump touhou9
        label reimuq_4:
            hide reimu with dissolve
            "Wrong. It's Reimu."  with vpunch
            jump touhou9

        
    label touhou9:
        if correct == 0:
            "Let's give you an even easier question."
        else:
            "Let's do another easy question!"

        $ total = total + 1
        window hide
        window show
        n "{b}Which is the 10th Touhou game?{/b}"
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
            "Correct! Phantasmagoria of Flower View is {i}of course{/i} the 10th Touhou game. It released a whole year after Touhou 7.5 and months before Touhou 9.5."
            $ last_wrong = False
            jump eosdeasy
        label a_touhou9_2:
            "Wrong! Both Touhou 7.5 and 9.5 released before Mountain of Faith, making it the twelth game in the series."  with vpunch
            $ last_wrong = True
            jump  eosdeasy
        label a_touhou9_3:
            "Wrong! In which timeline could that have been the right answer? The 10th game in the Touhou series is {i}of course{/i} Touhou 9."  with vpunch
            $ last_wrong = True
            jump eosdeasy
        label a_touhou9_4:
            "Wrong! That's not even a Touhou game, it is?" with vpunch
            $ last_wrong = True
            jump eosdeasy


    label eosdeasy:
        if last_wrong:
            n "You're pitiful, so I'll give you an Easy Mode question."
        else:
            n "Let's do another Easy question. An Easy Mode question."
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
            "Wrong! You don't even get to fight Remilia on Easy" with vpunch
            $ last_wrong = True
            jump branch1
        label eosdeasy_2:
            "Wrong! That's one of Flandre's Spell Cards."  with vpunch
            $ last_wrong = True
            jump branch1
        label eosdeasy_3:
            "Wrong! That is the final Spell Card on Normal."  with vpunch
            $ last_wrong = True
            jump branch1
        label eosdeasy_4:
            $ correct = correct + 1
            "Correct! Easy Mode only has 5 stages, so Sakuya is the final boss."
            $ last_wrong = False
            jump branch1

    label branch1:
        # This is not really a 'meaningful' branch in the quiz. It just swaps the order of 'edgyzun' and 'deathbomb' segments of the quiz. After branch2, every player will have seen the same questions.
        if correct <= 1:
            if last_wrong:
                n "This quiz is not going well for you. Did I tell you that you're staking your life on this quiz?"
                extend "\nOn that topic..."
            else:
                n "Wow, you somehow got that one right."
                n "Still, this quiz is not going well for you. You're staking your life on this quiz, you know?"
                extend "\nOn that topic..."
            jump edgyzun1
        else:
            if correct == 4:
                n "A perfect score so far. Congratulations!"
                n "You're staking your life on this quiz, you know? But maybe you can avoid death if you know the answers to the next few questions."
            elif not last_wrong:
                n "You're doing pretty well so far."
                n "You're staking your life on this quiz, you know? But maybe you can avoid death if you know the answers to the next few questions."
            else:
                n 'Maybe that wasn\'t so "Easy Mode" after all?'
                n "You're staking your life on this quiz, you know? But maybe you can avoid death if you know the answers to the next few questions."
            jump deathbomb1
                

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
            n "Correct! To see this famous message, you need to finish with a Skill Score less than 10."
            jump edgyzun2
        label edgyzun1_2:
            n "Wrong! But almost right." with vpunch # This line connects well to 'edgyzun2'.
            jump edgyzun2
        label edgyzun1_3:
            n "Wrong! {i}Story of Eastern Wonderland{/i} famously tells the player to kill themselves. To see this message, you need to finish with a Skill Score less than 10." with vpunch
            jump edgyzun2
        label edgyzun1_4:
            n "Wrong! {i}Story of Eastern Wonderland{/i} famously tells the player to kill themselves. To get this message, you need to finish with a Skill Score less than 10." with vpunch
            jump edgyzun2
    

    label edgyzun2:
        $ total = total + 1
        window hide
        window show
        n "{i}Highly Responsive to Prayers{/i} (HRtP) will also insult the player if their Skill Score is not high enough. {b}Which of the following is {i}not{/i} a title HRtP may give to a player who finished at low Skill Score?{/b}"
        menu:
            extend ""
            "Monkey":
                jump edgyzun2_1
            "Child-like Gamer":
                jump edgyzun2_2
            "Rotten Mandarin":
                jump edgyzun2_3
            "Bad Apple":
                jump edgyzun2_4

        label edgyzun2_1:
            n "Wrong! {i}Monkey{/i} is one of three titles that are randomly assigned to a player who finishes with less than 0 Skill Score." with vpunch
            jump branch2
        label edgyzun2_2:
            n "Wrong! {i}Child-like Gamer{/i} is one of three titles that are randomly assigned to a player who finishes with less than 0 Skill Score." with vpunch
            jump branch2
        label edgyzun2_3:
            n "Wrong! {i}Rotten Mandarin{/i} is one of three titles that are randomly assigned to a player who finishes with less than 0 Skill Score." with vpunch
            jump branch2
        label edgyzun2_4:
            $ correct = correct + 1
            n "Correct! You can be a {i}Rotten Mandarin{/i} at Highly Responsive to Prayers, but you can't be a {i}Bad Apple{/i}."
            jump branch2


    label branch2:
        # Not really a meaningful branch. The player is simply sent to the branch they didn't get
        # at branch1. After this branch, every player will have seen the same questions.
        if edgydone and bombdone:
            jump fuujinroku
        elif edgydone:
            # The player had a very low score at previous branch and got to do the EDGY questions first
            if correct >= 3:
                n "You've done well on these last few questions. Maybe you're not a lowest-tier Quiz Score player after all?"
                n "Knowing the answers to the next few questions might just save your life."
            elif correct == 2:
                n "You're at least getting some of my questions right. Maybe you're not a lowest-tier Quiz Score player after all?"
                n "Knowing the answers to the next few questions might just save your life..."
            else:
                n "This quiz is hard, right?"
                n "Knowing the answers to the next few questions might just save your life..."
                 
            jump deathbomb1
        else:
            # The player had a decent score at previous branch and did the deathbobm questions first
            if correct <= 2:
                n "This quiz is not going well for you. Need I remind you that you're staking your life on this quiz?"
                extend "\nOn that topic..."
            elif correct >= 6:
                n "You're maintaining your perfect score. This is very exciting!"
                n "Time for a few questions about what happens to people with not-so-good scores..."
            elif correct >= 4:
                n "You're still doing quite well. Keep up the good work!"
                n "Time for a few questions about what happens to people with not-so-good scores..."
            else:
                n "Your score could be better."
                n "Time for a few questions about what happens to people with not-so-good scores. Maybe that'll motivate you to do better?"
            jump edgyzun1
            
            
    label deathbomb1:
        $ bombdone = True
        $ total = total + 1
        window hide
        window show
        n "In many Touhou games, it is possible to avoid death by bombing within a certain number of frames after taking a hit (deathbombing). {b}How many frames is the deathbomb window in most official Touhou games?{/b}"
        menu:
            extend ""
            "5":
                jump deathbomb1_1
            "6":
                jump deathbomb1_2
            "8":
                jump deathbomb1_3
            "10":
                jump deathbomb1_4
                
        label deathbomb1_1:
            n "Wrong! {i}Obviously,{/i} it's 8 frames, or about 0.133 seconds." with vpunch
            jump deathbomb2
        label deathbomb1_2:
            n "Wrong! {i}Obviously,{/i} it's 8 frames, or about 0.133 seconds." with vpunch
            jump deathbomb2
        label deathbomb1_3:
            $ correct = correct + 1
            n "Correct! With each frame being 1/60 seconds, it gives you about 0.133 seconds to deathbomb, which is faster than pretty much any mere human can react."
            jump deathbomb2
        label deathbomb1_4:
            n "Wrong! {i}Obviously,{/i} it's 8 frames, or about 0.133 seconds." with vpunch
            jump deathbomb2
            
    label deathbomb2:
        n "Now, let's get a bit more specific."
        $ total = total + 1
        window hide
        window show
        n "{b}How many frames is the deathbomb window in Touhou 6 (Embodiment of Scarlet Devil)?{/b}"
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
            n "Wrong! Touhou 6 sort of sits in-between the PC98 and the rest of the Windows games, and is unusual in many regards." with vpunch
            jump deathbomb3
        label deathbomb2_2:
            n "Wrong! The deathbomb window in Touhou 6 starts at 6 frame, but it decreases every time you deathbomb. The timing resets back to 6 frames upon death, though." with vpunch
            jump deathbomb3
        label deathbomb2_3:            
            n "Wrong! All wrong!! Deathbombing has been a feature since Touhou 4, but it's not present in all later games. The fighting games don't even have bombs." with vpunch
            jump deathbomb3
        label deathbomb2_4:
            $ correct = correct + 1
            n "Correct! The window starts at 6 frames, but is reduced every time you deathbomb."
            n "Specifically, the window is reduced by the difference between when you took a hit and when you bombed. It resets to being 6 frames every time you die, though."
            jump deathbomb3

    label deathbomb3:
        n "Now, for the ultimate deathbomb question!"
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
            n 'Wrong! Touhou 8 has a very generous deathbomb window, but deathbombs instead cost two bombs and trigger special {i}Last Spell{/i} spells. However, "Master Spark" is not one of these spells. To pull-off a "Master Spark" deathbomb, you have a window of a measly 1 frame.' with vpunch
            jump branch2
        label deathbomb3_2:
            n 'Wrong! While Touhou 8 indeed has a very generous deathbomb window for special {i}Last Spell{/i} spells, "Master Spark" is not one of these spells. To pull-off a "Master Spark" deathbomb, you have a window of a measly 1 frame.'  with vpunch
            jump branch2
        label deathbomb3_3:            
            n 'Wrong! In Touhou 8, normal spells like "Master Spark" have a 1 frame deathbomb window. Of course, {i}Last Spells{/i} like "Final Spark" have a very large window, but they cost 2 bombs.' with vpunch
            jump branch2
        label deathbomb3_4:
            $ correct = correct + 1
            n 'Correct! In Touhou 8, normal spells like "Master Spark" have a 1 frame deathbomb window. Of course, {i}Last Spells{/i} like "Final Spark" have a very large window, but they cost 2 bombs.'
            jump branch2


    label fuujinroku:
        n "The next question is...\n"
        show nareko shocked with vpunch
        extend "Who even put this here? This is completely trivial. It's not even a question—you just follow the instructions and get a free point."
        $ total = total + 1
        window hide
        window show
        show nareko
        n '{b}Simply pick the option that says "Mountain of Faith".{/b}'
        menu:
            extend ""
            "{font=jp}お風呂{/font}":
                jump fuujinroku_1
            "{font=jp}風神録{/font}":
                jump fuujinroku_2
            "{font=jp}洋風巻寿司{/font}":
                jump fuujinroku_3
            "{font=jp}風船玉{/font}":
                jump fuujinroku_4

        label fuujinroku_1:
            n "Wrong!!!" with vpunch
            n "Maybe you should learn to read, instead of taking dubious quizes from even more dubious {rb}sphinxes{/rb}{rt}(dousojin){/rt}?"
            jump yamawaro
        label fuujinroku_2:
            $ correct = correct + 1
            'Yes, that is correct. How did this "question" even get here?'
            jump yamawaro
        label fuujinroku_3:
            n "Wrong!!!"
            n "Maybe you should learn to read, instead of taking dubious quizes from even more dubious sphinxes?"
            jump yamawaro
        label fuujinroku_4:
            n "Wrong!!!"
            n "Maybe you should learn to read, instead of taking dubious quizes from even more dubious sphinxes?"
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
            "Wrong! They were introduced in chapter 13 of {i}Wild and Horned Hermit{/i}, in 2012." with vpunch
            jump newchars
        label yamawaro_2:
            "Wrong! They were introduced in chapter 13 of {i}Wild and Horned Hermit{/i}, in 2012." with vpunch
            jump newchars
        label yamawaro_3:
            $ correct = correct + 1
            "Correct! Who could forget about chapter 13 of {i}Wild and Horned Hermit{/i}."
            jump newchars
        label yamawaro_4:
            "Wrong! While the first named yamawaro character (Yamashiro Takane) was indeed introduced in 2021, the yamawaro themselves were introduced in chapter 13 of {i}Wild and Horned Hermit{/i}, in 2012." with vpunch
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
            jump depiction
        label newchars_2:
            $ correct = correct + 1
            n "Correct!"
            n "Minoriko, Hina, Nitori, Sanae, Kanako, Suwako. That's only 6! Aya was introduced already in Touhou 9 and had had her own spin-off game by the time she appeared as a regular stage boss."
            jump depiction
        label newchars_3:
            n "Wrong!!" with vpunch
            n "Eternity, Nemumo, Aunn, Narumi, Satono & Mai, Okina. That's 7."
            jump depiction
        label newchars_4:
            n "Wrong!!" with vpunch
            n "Mike, Takane, Sannyo, Misumaru, Megumu, Chimita, Momoyo. That's 7. Tsukasa obviously doesn't count since she isn't a stage boss."
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
            "Chang'e":
                jump depiction_3
            "Gungnir":
                jump depiction_4

        label depiction_1:
            n "'Titanic'? That's the name of Komachi's boat."
            extend " So you're wrong!"  with vpunch
            jump taito1
            
        label depiction_2:
            n "Jesus Christ is shown in a panel in {i}Wild and Horned Hermit{/i}, chapter 44."
            extend " So you're wrong!"  with vpunch
            jump taito1
            
        label depiction_3:
            $ correct = correct + 1
            n "That's right! Despite being mentioned several times, Chang'e has never been official depicted."
            jump taito1
            
        label depiction_4:
            n "'Gungnir' is name of Remilia's spear."
            extend " So you're wrong!"  with vpunch
            jump taito1
            
            
    label taito1:
        $ total = total + 1
        window hide
        window show
        "Between 1998 and 2007, ZUN worked as a programmer at a company widely known for its arcade games. {b}What company?{/b}"
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
            n "Wrong! While Konami fits the description, it's not where ZUN worked. He worked at Taito."
            jump taito2
        label taito1_2:
            n "Wrong! While Namco fits the description, it's not where ZUN worked. He worked at Taito."
            jump taito2
        label taito1_3:
            $ correct = correct + 1
            n "Correct!"
            n "While working at Taito, ZUN got approached about making a commercial Touhou game. ZUN declined the offer at that time, since he wanted creative control over the franchise."
            n "About a decade later, Taito would go on to publish Touhou Spell Bubble."
            jump taito2
        label taito1_4:
            n "Wrong!  ZUN worked at Taito, not CAVE."
            jump taito2
            
    label taito2:
        $ total = total + 1
        window hide
        window show
        n "Interestingly, Taito is the developer behind another shooting game series featuring a shrine maiden and youkai. ZUN has publicly stated that this series directly inspired aspects of the Touhou Project. {b}Which game series?{/b}"
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
            n "Correct! The first game in the {i}Kiki Kaikai{/i} series was developed by Taito, while they outsourced later games in the series to Natsume. Natsume brought the series to home consoles and got it localized in the west as {i}Pocky & Rocky{/i}."
            jump tonext
        label taito2_2:
            n "Wrong! Touhou 2 contains a reference to this game, but it's not a shooting game with shrine maidens, nor developed by Taito. It's a puzzle game by Konami." with vpunch
            jump tonext
        label taito2_3:
            n "Wrong! While Touhou 1 clearly draws some inspiration from Megami Tensei, it's not a shooting game with shrine maidens, nor developed by Taito. It's a series of roleplaying games by Atlus." with vpunhc
            jump tonext
        label taito2_4:
            n "Wrong! While ZUN has traced art from the Rance series, it's not a shooting game with shrine maidens, nor developed by Taito. It's a series of erotic RPG games by AliceSoft." with vpunch
            jump tonext

            

    label tonext:
        # TODO: put more stuff here tomorrow.
        # TODO maybe Alice questions?
        "TODO MORE HERE"
        jump ending
            
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
        n "Correct answers [correct] out of [total]"
        jump end_game
        
    label end_game:
        return
