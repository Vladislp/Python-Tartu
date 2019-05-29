import pygame, pygame.mixer
import sys

pygame.init()

# --- constants ---

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)

red = (200,0,0)
green = (0,200,0)

bright_red = (255,0,0)
bright_green = (0,255,0)

block_color = (53,115,255)

def blit_text(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

# --- functions ---

def text_objects(text, font, color=black):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def button(msg, x, y, w, h, ic, ac, click, action=None):
    
    click1 = pygame.mixer.Sound('Sound.wav')

    mouse = pygame.mouse.get_pos()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click == 1 and action != None:# <-- click instead of click[0]
            pygame.mixer.music.stop()
            click1.play()
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )

    gameDisplay.blit(textSurf, textRect)

def quitgame():
    pygame.quit()
    sys.exit()
    quit()

# - scene GameIntro -

pygame.mixer.music.load("start.mp3")
pygame.mixer.music.play()

meie_font = pygame.font.SysFont("comicsansms", 25)

def game_intro():

    intro = True

    while intro:

        # - events -

        mouse_button = 0 # reset in every loop

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_button = event.button

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused()

        # - updates -
        
        pilt11 = pygame.image.load("forest.jpg")
        pilt11 = pygame.transform.scale(pilt11, (display_width, display_height))
        gameDisplay.blit(pilt11, (0, 0))
        
        
        button("Start",150,450,100,50,green,bright_green, mouse_button, game_loop)
        button("Quit",550,450,100,50,red,bright_red, mouse_button, quitgame)

        # - draws -

        #gameDisplay.blit(pilt1, [0,0])
        pygame.display.update()

# - scene GameLoop -

def goto_subscene(number):
    global display_subscene

    display_subscene = number


def game_loop():
    global display_subscene
###############################################################################
    # at start display subscene 1
    display_subscene = 1 

    #bg = pygame.image.load("natsalo.jpg")

    meie_font = pygame.font.SysFont("comicsansms", 25)
###############################################################################
    # - subscene 1 -

    tekst = "This game will go as far as you choose!"
    subscene_1_text_1 = meie_font.render(tekst, False, (255,255,255))

    tekst = "You choose how you die"
    subscene_1_text_2 = meie_font.render(tekst, False, (255,255,255))
###############################################################################
    # - subscene 2 -

    
    scene_2 = "You just finished school this year and decided to go to college, though there was one catch. Your parents said, that you had to work this summer if you want any financial support from them. So you did.\n  \nSummer was nearly over and you woke up early before going to work. You looked at the alarm. \nWhat will you do next?"
    #1) Stand up 2)Sleep a little bit more
    scene_2_1 = "Well, you could, but then you would get late for work" #Stand up
    scene_3 = "You stood up, looked around and admired the the sunrise that could be clearly seen from your window. \nYou got dressed up." #1)Go  downstairs 
    scene_4 = "You quickly passed the kitchen, grabing the sandwitches that you made yesterday.  Got outside of the house and went straight to work" #Continue walking
    scene_5 = "As you were going, you realised that you forgot you phone at home" #1)Move on 2)Get back and search for your phone
    scene_5_1 = "When you turned around and got to the crossroad, an ambulance hit you because of your inattention and you died" #Game Over (If you choose 2nd from scene_5)
    scene_6 = "As you were getting close to the cafeteria you were working in, you`ve heard  noise of an ambulance passing nearby. 'So early in the morning?' - you've asked yourself."#continue
    scene_7 = "As you got to the cafeteria you got ready for  your shift, greeted everyone in there and just started taking orders from the visitors. \nThis was quite an easy and nice job, especially when considering tips from visitors. Just taking orders, getting them to the kitchen, bringing orders back to the clients. Not so hard, enjoyable as well because you already knew all the visitors from your small town. \nIt's felt also sad because you would move to another city to go to college. You would get yourself far away from this cozy town where you grew up, far away from the people and friends that you knew..."
    #Continue
    scene_8 = "The time passed on and at one point you noticed a strange man entering the cafeteria. You didn't know him, never seen him around. When he got close to the counter, he asked just for water. You got him a glass of water and he immediately drank it all as if it was his first in a couple days. \nWhen you asked him if he wants anything alse, he rejected and just sat in silence. Only then, after looking at him closely, you saw that his left hand had a strange kind of bite on it and it was bleeding. Bleeding hard."
    #1) Ask:"Sir, are you alright? What happened? 2)Don't ask anything
    scene_8_1 = "'Kind of not, I would say' - he replied- 'I got attacked by some strange man in the alley like a mile away. He bit me and punched him in the face and just ran away. \n'Maybe I should call a doctor?  - you asked him - 'You are loosing blood.' \n'No need' - he said - 'I am capable of going to the hospital by myself.'"
    #if scene_8 first
    scene_9 = "The man threw a few coins on the counter and tried to stand up, but failed at doing so and fell hard on the floor. \n'Are you okay?' - you nearly shouted in shock and quickly ran to the man. A  few visitors gathered around you as you were trying to help the man stand up. You sat him down on the couch and went to find your phone. Only then you remembered that you left it home and asked one of the visitors to call an ambulance."
    #Continue
    scene_10 = "While someone was calling an ambulance you got back to the man and checked if he was even awake. 'What's your name? - you asked. \nHe said - 'Tom..'. \n'Okay, Tom, right now I'm going to try to find any bandages and at least cover your 'wound'. Can you tightly hold it for now?' - you asked Tom. \nHe silently nodded and you rushed behind the counter."
    #1)Go to the kitchen 2)Go to the office
    scene_10_1 = "After you went to the kitchen you've asked the chef if he's seen the med kit. \n'Of course not. It should in the office, as always. What happened over there?' - the chef asked. \n'A man was wounded after a fight' - you answered -' Okay, thanks, I'll run to the office. I'll tell you everything after, okay?'"
    #Go back
    scene_10_2 = "So now the med kit must be in the office. You must go there to find it."
    #Go to the office
    scene_11 = "As you've rushed into the office, you've looked around and saw a little red box on the shelf behind the desk. You've grabbed it and ran back to Tom."
    scene_11_5 = "As you've rushed into the office, you've looked around and saw a little red box on the shelf behind the desk. You've grabbed it and ran back to Tom."
    #Go to the cafeteria
    scene_11_6 = "'Took you long enough' - Tom said. \n'Sorry, went to the wrong place at first' - you said - 'Now, I need to see your hand.' \nAs you were wrapping the bandages around Tom's hand, he got so pale that it felt that he was about to faint."
    #Continue(if went to the kitchen)
    scene_12 = "'Now, I need to see your hand.'  \nAs you were wrapping the bandages around Tom's hand, he got so pale that it felt that he was about to faint."
    #Continue(if went straight to the office)
    scene_13 = "As you finished with Tom, you've heard an ambulance getting close. A little bit more, and he would be unconscious. \nThe paramedics arrived just in time to take Tom to the hospital. As they were leaving, Tom mumbled something simillar to 'thanks'. \nYou were shocked by this, especially because it happened in such a peaceful town and, of course, during one of your last days on work."
    #Continue
    scene_14 = "As the ambulance left, a police car stopped in front of the cafeteria. The officer entered the cafeteria and shouted out loud - 'Everyone, there is a riot coming down the street and it it is not going well. We kindly ask you to leave your spots and quickly go to your home.'. \nBefore you could even ask the officer about anything, he got out and drove away in his car. 'That is even stranger' - you thought and quickly went out of the cafeteria to look around. You didn't see anyone around and you couldn't even hear any noises from other streets. Everything was dead silent. \nAs everyone started  rushing away from the cafeteria, you decided to go home as fast as you could to check, if your parents were alright."
    #Run home
    scene_15 = "'What just happened? In this town? A riot? A bleeding man in morning in the cafeteria with a bite on his hand? This is very strange' - you thought, still being shocked as how everything turned around so fast. As you were near your house, you've suddenly heard a gunshot nearby. \nAt that point you got scared and ran to your front door even faster. You've tried to search your bag for your keys, but you couldn't find them. It seems that you've left them somewhere in the cafeteria. Runnig back was not an option."
    #1)Try to break in from the front door 2)Go to the backyard
    scene_16_1 = "You've looked around in search of anything heavy. You definitely couldn't break the door by yourself. You've looked around one more time and found a rock, with which you decided to slam a little window above the door handle. You did so and tried to fit your hand through. You've reached the handle and opened the door, but when you were pulling your hand back, you've accidentally cut your palm. \n'Great, now I'm pouring blood'. You've quickly opened the door, leaving it unattended, and ran into the house. Your parents were not home, as the parking place in front of the house was not occupied, which meant that they were already at work, probably"
    #if first from scene_15. 1)Go upstairs for your phone 2)Wash your cut and find bandages
    scene_16_1_1 = "You ran to the second floor and rushed into your room, though your hand soaking blood. You immediately found your phone on your desk and opened the contacts list."
    #1)Call Mom 2)Call Dad
    scene_16_1_2 = "The phone rang, but nobody answered. This scared you even more because you didn't know, what was happening and what to do next."
    #Go downstairs
    scene_16_1_3 = "As you approached the door, a figure appeared, but it was not Mom nor Dad. You've looked closely and saw, that it was your neighbour from the next house. You've said hello to him and asked what he was doing here, but he didn't respond. \nHe started moving closer to you and at this point you felt absolutely terrified because your neighbour was rasing hands at you and wheezed out some unrelatable sounds. \nYou turned around and ran back upstairs to your room, closing and locking the door immeadiately."
    #Look around for options
    scene_16_1_4 = "After looking around your room, you didn't find anything useful. \nSuddenly, your neighbour started slaming your door. At this point you knew, that it was not your neighbour anymore... \nIt was something else now. Something scary... \nYou've looked around one more time and decided, that the only way out would be jumping out of the window. Or fighting your 'neighbour' off."
    #1)Run to the window and open it 2)Open the door and kick the 'thing'
    scene_16_1_4_1 = "You tried to open the window as fast as you could, but failed at your first try as your hands were shaking. You never felt this terrified before. If you wouldn't escape, that 'thing' would kill you slowly and painfully. \nAfter the second shot the window opened and you looked down, realising that it would be  a hard fall and it would be a miracle not to brake anything. As you sat on the window getting ready to jump down, the door opened and your 'neighbour' rushed onto you. As you were about to jump, it grabbed you by your hand and getting close on it to bite you. You knew, that your next decisions might be your last."
    #1)Punch it 2)Jump
    scene_16_1_4_1_1 = "As you tried to punch it, you were pulled back into the room and that monster knocked you down. As you fell hard, slaming your head onto the floor, it bit your leg. \nYou kicked it in the face, though feeling enormous pain. You crawled back. It felt, that the moster didn't even feel pain and you couldn't really stand up, still feeling dizzy after the fall."
    #Crawl back(if punched)
    scene_16_1_4_1_2 = "You crawled back a little bit more. Your leg was bleeding.  \nIt was getting closer to you and you knew, that you hadn't had a chance to fight off."
    #Scream in despair
    scene_16_1_4_1_3 = "As you tried to open your mouth and shout, it ripped your neck and you died."
    scene_16_1_4_2 = "You jumped out of the window, at the same time pulling the monster out. You fell on the ground, not even breaking anything. The same couldn't be said about your 'neighbour'. It fell on it's head, smashing it in the result."
    #Stand up and walk away(if jumped)
    scene_16_2_1 = "As you were washing your hand from blood, you heard a strange noise coming from outside. A figure appeared at the doors, but it was not Mom nor Dad. You've looked closely and saw, that it was your neighbour from the next house. You've said hello to him and asked what he was doing here, but he didn't respond. \nHe started moving closer to you and at this point you felt absolutely terrified because your neighbour was rasing hands at you and wheezed out some unrelatable sounds. \nYou turned around and ran back upstairs to your room, closing and locking the door immeadiately."
    #The same, as in 16_1_3 and so on.
    scene_16_1_4_3 = "When you opened the door you didn't have enough time to do anything, as the 'thing' grabbed you and then tossed you on the floor. After that, you fainted and the monster ripped your body apart and started eating your insides. \nCongratulations on trying 1v1 a full grown adult. That was very 'clever'!"
    
    scene_15_1 = "You ran to the backyard to check, if any door was open. Luckily. nobody has closed the backdoor and you succesfully got into the house."
    #Go upstairs.
    scene_15_2 = "You ran to the second floor and rushed into your room. You immediately found your phone on your desk and opened the contacts list."
    #1)Call Mom 2)Call Dad
    scene_15_3 = "The phone rang, but nobody answered. This scared you even more because you didn't know, what was happening and what to do next."
    #Go downstairs
    scene_15_4 = "You were standing in the hallway. Because you had no choice, but to go to your parents just like this, you had to decide to whom to go first. The only thing that was sure was, that your Dad had the car and your Mom alone by herself."
    #1)Go to Mom first 2)Go to Dad first
    scene_15_5 = "Your mom's place was in the center of the city. To get there, you just had to go straight back to the place, where you were working. Your mom's work was a 10 minute walk away from the cafeteria."
    #Continue walking(if go to mom)
    scene_15_6 = "As you've approached the cafeteria, you couldn't believe your eyes. The cafeteria was on flames, it was burning, though no people seemed to be left inside. It seemed, as your life was just falling apart because of just one morning."
    #Move on
    scene_15_7 = "As you were passing a small alley near the cafeteria, you've seen a couple strange men standing there. They were just standing still. You got a little bit close to them to ask, if everything was okay, but right after they heard it they turned around. When you've seen their faces and how they started moving towards you, just screamed in shock. Their bodies were covered in blood and their hands, necks and faces were ripped, bitten and scared. They were dead."
    #Run away
    scene_15_7_1 = "Just after a little running, you got to your mom's place. Luckily, at that moment your mom just got outside of the building. 'Oh my god... Honey, you're okay? Are you hurt, no scars, bites?  - she asked. \n'No, Mom, I'm okay, just scared.' - you said - 'Where is Dad?'. \n'He should arrive here very soon. We should get out of this city as fast as possible.' - Mom said. \n'Do you know, what happened?' - you asked her. \n'No, honey, I..'-  Mom didn't finish as your Dad drove to you."
    #Continue
    scene_15_8 = "Thank god, you're both here. Are you alright? - he asked - 'Get into the car now, we need to drive away. Now.' \nAs Dad said that, his face changed radically. We all got into the car and got out of the city."
    #Look at your parents
    scene_15_9 = "As you looked at your dad, you felt worried. As if he was hiding something from you."
    #Ask him, if everything is alright
    scene_15_10 = "'Yes, honey. We all got out and that is what matters the most' - he said - 'Though I don't know, what happened back there. We will drive to the capital and see, if we can get any help there'."
    #Look in the window
    scene_15_11 = "'I hope' - you thought. That was definitely not the way you wanted everything to happen. You thought, that you would just get enough money to go to college. But now, who the hell knows what will happen to you and your family? What if this didn't happen just in your city? Maybe all across the country? \nYou didn't know. As you looked at the front window, you noticed, that  your dad has blood on his shirt's sleeve. \nAnd also a bite on his right hand...."
    #To be continued
    scene_15__2 = "Your Dad's work was at the outskirts of the city. You started running, not even feeling tired, as if adrenaline was rushing through your blood. After a few more miles you stopped near a little shop. There was no people around, but you've heard some strange noises coming from the corner."
    #1)Look around the corner 2)Move on(If go to dad)
    scene_15__2_1 = "As you approached the corner, you carefully looked at what was happening in the alley. \nTo say that you weren't shocked would be the same, as to say nothing. Two men were ripping a dog apart and eating it's insides. Without hesitation, you started running away from that place."
    #Continue
    scene_15__3 = "You got close to your Dad's place. You couldn't see anyone around, so you just entered the building."
    #Continue
    scene_15__4 = "Right when you got inside, you saw your Dad fighting off one of his friends. This was so unbelievable to see, that you couldn't even move."
    #Continue
    scene_15__5 = "Your Dad  bashed his friends skull through the wall, definitely killing him by that. 'WHY DID YOU DO THIS?' - you've shouted. \n'Oh my god... You've seen it all. Dear, he was not himself, he was trying to kill me. He... No, IT nearly killed me.' - he answered- 'Honey, we have to go now, and FAST.'. \n'Okay, but what did you mean by saying it?' - you've asked. \n'Because he was not himself at all. Just in the morning he came with this strange bite, but then dissappeared, like, for 2 hours. I've tried to search for him, but when I found him, he was already like this. As if.... dead.'"
    #Continue
    scene_15__6 =  "You didn't ask anything more. You both got out of the building and went straight to the car. \nAs you were approaching the car, a dozen of some men walked through the gate, growling all at the same time. \n'Shit, they are the same as him!'-Dad said- 'Honey, get in the car, quickly!'. \nYou've entered the car, as your dad started the engine and began to move back. He was ready to drive away when one of those 'things' tried to open the door."
    #Continue
    scene_15__7 = "'Don't worry, I closed those damn doors.' - Dad said. \nYou were relieved, but not for long. Right after you drove right to the main road, you've seen, that the whole city was crawling with those monsters. \nBut the scariest part was, that they looked exactly like the people living in this city."
    #Continue
    scene_15__8 = "You got close to your mom's working place. But when you looked at the front doors, you realised, what happened. \nYou were too late, your mom was lying on the ground, all in blood. \nShe was dead."
    #Continue
    scene_15__9 = "You've tried to open the doors and run t o your mom. But your dad didn't let you. \n'No, honey, it's too late. We can't do anything....'"
    #Continue
    scene_15__10 = "He started accelerating, just to get away from the city as fast as possible. \nYou looked back through the mirror one more time. \nYou saw, how your mother stood up and started walking. \nAfter you saw that, you couldn't say anything, you just sat silently, shocked."
    #continue
    scene_15__11 = "You got out of the city, but the same couldn't be said for everyone... \nThe only chance you had was to drive to the capital, but that was 200 miles away. And no one knew, what might happen on the way there..."
    #To be continued
    
    
    #after scene_16_1_4_2
    scene_17 = "You still were shocked by what just happened. But now you had to choose, what to do. Go to Mom or Dad?"
    #1)Go to mom 2) Go to Dad
    scene_17_1 = "Your mom's place was in the center of the city. To get there, you just had to go straight back to the place, where you were working. Your mom's work was a 10 minute walk away from the cafeteria."
    #Continue walking(if go to mom)
    scene_17_2 = "As you've approached the cafeteria, you couldn't believe your eyes. The cafeteria was on flames, it was burning, though no people seemed to be left inside. It seemed, as your life was just falling apart because of just one morning."
    #Move on
    scene_17_3 = "As you were passing a small alley near the cafeteria, you've seen a couple strange men standing there. They were just standing still. You got a little bit close to them to ask, if everything was okay, but right after they heard it they turned around. When you've seen their faces and how they started moving towards you, just screamed in shock. Their bodies were covered in blood and their hands, necks and faces were ripped, bitten and scared. They were dead."
    #Run away
    scene_17_4= "Just after a little running, you got to your mom's place. Luckily, at that moment your mom just got outside of the building. 'Oh my god... Honey, you're okay? Are you hurt, no scars, bites?  - she asked. \n'No, Mom, I'm okay, just scared.' - you said - 'Where is Dad?'. \n'He should arrive here very soon. We should get out of this city as fast as possible.' - Mom said. \n'Do you know, what happened?' - you asked her. \n'No, honey, I..'-  Mom didn't finish as your Dad drove to you."
    #Continue
    scene_17_5= "Thank god, you're both here. Are you alright? - he asked - 'Get into the car now, we need to drive away. Now.' \nAs Dad said that, his face changed radically. We all got into the car and got out of the city."
    #Look at your parents
    scene_17_6 = "As you looked at your dad, you felt worried. As if he was hiding something from you."
    #Ask him, if everything is alright
    scene_17_7 = "'Yes, honey. We all got out and that is what matters the most' - he said - 'Though I don't know, what happened back there. We will drive to the capital and see, if we can get any help there'."
    #Look in the window
    scene_17_8 = "'I hope' - you thought. That was definitely not the way you wanted everything to happen. You thought, that you would just get enough money to go to college. But now, who the hell knows what will happen to you and your family? What if this didn't happen just in your city? Maybe all across the country? \nYou didn't know. As you looked at the front window, you noticed, that  your dad has blood on his shirt's sleeve."
    #To be continued
    scene_17__1 = "Your Dad's work was at the outskirts of the city. You started running, not even feeling tired, as if adrenaline was rushing through your blood. After a few more miles you stopped near a little shop. There was no people around, but you've heard some strange noises coming from the corner."
    #1)Look around the corner 2)Move on(If go to dad)
    scene_17__2 = "As you approached the corner, you carefully looked at what was happening in the alley. \nTo say that you weren't shocked would be the same, as to say nothing. Two men were ripping a dog apart and eating it's insides. Without hesitation, you started running away from that place."
    #Continue
    scene_17__3 = "You got close to your Dad's place. You couldn't see anyone around, so you just entered the building."
    #Continue
    scene_17__4 = "Right when you got inside, you saw your Dad friend corpse lying on the floor. You freezed and stood in place, as if your whole world just turned around. How this could happen? Why is there so much blood around? Why Dad's friend is lying dead?"
    #Go outside
    scene_17__5 = "When you got outside, you looked at the parking lot. Your Dad's car was gone. And at the same time, dozen of strange people started going through the fence."
    #continue
    scene_17__6 = "You were just standing still. You couldn't believe that this all was happening. The group of those people was getting closer. as they were getting closer, you could hear them growling."
    #Continue
    scene_17__7 = "The only way out of here was through that fence. But you could only get to it through those 'things'. \nThey looked dead. \n... \nWalking dead..."
    #Continue
    scene_17__8 = "You didn't know, what happened to your parents. \nYou didn't want to think, what will happen to you."
    #Continue
    scene_17__9 = "You just closed your eyes, embracing the end. \nThe dead were getting even closer, but it felt, like you were alone. \nEverything slowed down, you could barely hear anything."
    #Continue
    scene_17__10 ="It was the end. \nJust for the last moment you tried to open your eyes, but it was harder, than it seemed...."
    #To be continued

    
    
    # - loop -
    
    gameExit = False

    while not gameExit:

        mouse_button = 0 # reset in every loop

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_button = event.button
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused()

        if display_subscene == 1:
            gameDisplay.fill(white)
            
            pilt11 = pygame.image.load("fu.jpg")
            pilt11 = pygame.transform.scale(pilt11, (display_width, display_height))
            gameDisplay.blit(pilt11, (0, 0))

            gameDisplay.blit(subscene_1_text_1, (100, 250))
            gameDisplay.blit(subscene_1_text_2, (100, 280))

            button("Start playing", 300,500,150,50,green,bright_green, mouse_button, lambda:goto_subscene(2))

            pygame.display.update()

        elif display_subscene == 2:
            gameDisplay.fill(white)
            
            pygame.mixer.music.load("start.mp3")
            pygame.mixer.music.play(0)
            
            pilt1 = pygame.image.load("morning.jpg")
            pilt1 = pygame.transform.scale(pilt1, (display_width, display_height))
            gameDisplay.blit(pilt1, (0, 0))

            blit_text(gameDisplay, scene_2, (20,20),meie_font)


            button("Stand Up", 100,400,600,50,green,bright_green, mouse_button, lambda:goto_subscene(3))
            button("Sleep a little bit", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(4))

            pygame.display.update()

        elif display_subscene == 3:
            gameDisplay.fill(white)
            
            pilt1 = pygame.image.load("morning.jpg")
            pilt1 = pygame.transform.scale(pilt1, (display_width, display_height))
            gameDisplay.blit(pilt1, (0, 0))

            blit_text(gameDisplay, scene_3, (20,20),meie_font)
            button("Go downstairs", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(5))

            pygame.display.update()

        elif display_subscene == 4:
            gameDisplay.fill(white)
            
            pilt1 = pygame.image.load("morning.jpg")
            pilt1 = pygame.transform.scale(pilt1, (display_width, display_height))
            gameDisplay.blit(pilt1, (0, 0))

            blit_text(gameDisplay, scene_2_1, (20,20),meie_font)
            button("Stand up", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(3))

            pygame.display.update()

        elif display_subscene == 5:
            gameDisplay.fill(white)
            
            pilt2 = pygame.image.load("kitchen.jpg")
            pilt2 = pygame.transform.scale(pilt2, (display_width, display_height))
            gameDisplay.blit(pilt2, (0, 0))

            blit_text(gameDisplay, scene_4, (20,20),meie_font)
            button("Continue walking", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(6))

            pygame.display.update()
            
        elif display_subscene == 6:
            gameDisplay.fill(white)
            
            pilt3 = pygame.image.load("street.jpg")
            pilt3 = pygame.transform.scale(pilt3, (display_width, display_height))
            gameDisplay.blit(pilt1, (0, 0))

            blit_text(gameDisplay, scene_5, (20,20),meie_font)
            
            button("Move on", 100,400,600,50,green,bright_green, mouse_button, lambda:goto_subscene(8))
            button("Get back and search for your phone", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(7))

            pygame.display.update()
            
        elif display_subscene == 7:
            gameDisplay.fill(white)
            
            pilt3 = pygame.image.load("street.jpg")
            pilt3 = pygame.transform.scale(pilt3, (display_width, display_height))
            gameDisplay.blit(pilt3, (0, 0))

            blit_text(gameDisplay, scene_5_1, (20,20),meie_font)
            button("Game Over", 100,500,600,50,green,bright_green, mouse_button, quitgame)

            pygame.display.update()
            
        elif display_subscene == 8:
            gameDisplay.fill(white)
            
            pilt3 = pygame.image.load("street.jpg")
            pilt3 = pygame.transform.scale(pilt3, (display_width, display_height))
            gameDisplay.blit(pilt1, (0, 0))

            blit_text(gameDisplay, scene_6, (20,20),meie_font)
            button("Continue", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(9))

            pygame.display.update()
            
        elif display_subscene == 9:
            gameDisplay.fill(white)
            
            pilt8 = pygame.image.load("work.jpg")
            pilt8 = pygame.transform.scale(pilt8, (display_width, display_height))
            gameDisplay.blit(pilt8, (0, 0))

            blit_text(gameDisplay, scene_7, (20,20),meie_font)
            button("Continue", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(10))

            pygame.display.update()
            
        elif display_subscene == 10:
            gameDisplay.fill(white)
            
            pilt8 = pygame.image.load("work.jpg")
            pilt8 = pygame.transform.scale(pilt8, (display_width, display_height))
            gameDisplay.blit(pilt8, (0, 0))

            blit_text(gameDisplay, scene_8, (20,20),meie_font)
            
            button("Ask:Sir, are you alright? What happend?", 100,400,600,50,green,bright_green, mouse_button, lambda:goto_subscene(11))
            button("Don't ask anything", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(12))

            pygame.display.update()
            
        elif display_subscene == 11:
            gameDisplay.fill(white)
            
            pilt8 = pygame.image.load("work.jpg")
            pilt8 = pygame.transform.scale(pilt8, (display_width, display_height))
            gameDisplay.blit(pilt8, (0, 0))

            blit_text(gameDisplay, scene_8_1, (20,20),meie_font)
            button("Continue", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(12))

            pygame.display.update()
            
        elif display_subscene == 12:
            gameDisplay.fill(white)
            
            pilt8 = pygame.image.load("work.jpg")
            pilt8 = pygame.transform.scale(pilt8, (display_width, display_height))
            gameDisplay.blit(pilt8, (0, 0))

            blit_text(gameDisplay, scene_9, (20,20),meie_font)
            button("Continue", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(13))

            pygame.display.update()
                
        elif display_subscene == 13:
            gameDisplay.fill(white)
            
            pilt8 = pygame.image.load("work.jpg")
            pilt8 = pygame.transform.scale(pilt8, (display_width, display_height))
            gameDisplay.blit(pilt8, (0, 0))

            blit_text(gameDisplay, scene_10, (20,20),meie_font)
            
            button("Go to the kitchen", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(14))
            button("Go to the office", 100,400,600,50,green,bright_green, mouse_button, lambda:goto_subscene(16))

            pygame.display.update()
            
        elif display_subscene == 14:
            gameDisplay.fill(white)
            
            pilt8 = pygame.image.load("work.jpg")
            pilt8 = pygame.transform.scale(pilt8, (display_width, display_height))
            gameDisplay.blit(pilt8, (0, 0))

            blit_text(gameDisplay, scene_10_1, (20,20),meie_font)
            button("Go back", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(15))

            pygame.display.update()
            
        elif display_subscene == 15.5:
            gameDisplay.fill(white)
            
            pilt8 = pygame.image.load("work.jpg")
            pilt8 = pygame.transform.scale(pilt8, (display_width, display_height))
            gameDisplay.blit(pilt8, (0, 0))

            blit_text(gameDisplay, scene_11_5, (20,20),meie_font)
            button("Go to the cafeteria", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(17))
            

            pygame.display.update()    
        
            
        elif display_subscene == 15:
            gameDisplay.fill(white)
            
            pilt8 = pygame.image.load("work.jpg")
            pilt8 = pygame.transform.scale(pilt8, (display_width, display_height))
            gameDisplay.blit(pilt8, (0, 0))

            blit_text(gameDisplay, scene_10_2, (20,20),meie_font)
            button("Go to the office", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(15.5))

            pygame.display.update()
            
        elif display_subscene == 16:
            gameDisplay.fill(white)
            
            pilt8 = pygame.image.load("work.jpg")
            pilt8 = pygame.transform.scale(pilt8, (display_width, display_height))
            gameDisplay.blit(pilt8, (0, 0))

            blit_text(gameDisplay, scene_11, (20,20),meie_font)
            button("Go to the cafeteria", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(16.5))

            pygame.display.update()
            
        elif display_subscene == 17:
            gameDisplay.fill(white)
            
            pilt8 = pygame.image.load("work.jpg")
            pilt8 = pygame.transform.scale(pilt8, (display_width, display_height))
            gameDisplay.blit(pilt8, (0, 0))

            blit_text(gameDisplay, scene_11_6, (20,20),meie_font)
            button("Continue", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(18))

            pygame.display.update()
            
        elif display_subscene == 16.5:
            gameDisplay.fill(white)
            
            pilt8 = pygame.image.load("work.jpg")
            pilt8 = pygame.transform.scale(pilt8, (display_width, display_height))
            gameDisplay.blit(pilt8, (0, 0))

            blit_text(gameDisplay, scene_12, (20,20),meie_font)
            button("Continue", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(18))

            pygame.display.update()
           
        elif display_subscene == 18:
            gameDisplay.fill(white)
            
            pilt8 = pygame.image.load("work.jpg")
            pilt8 = pygame.transform.scale(pilt8, (display_width, display_height))
            gameDisplay.blit(pilt8, (0, 0))

            blit_text(gameDisplay, scene_13, (20,20),meie_font)
            button("Continue", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(19))

            pygame.display.update()
            
        elif display_subscene == 19:
            gameDisplay.fill(white)
            
            pilt8 = pygame.image.load("work.jpg")
            pilt8 = pygame.transform.scale(pilt8, (display_width, display_height))
            gameDisplay.blit(pilt8, (0, 0))

            blit_text(gameDisplay, scene_14, (20,20),meie_font)
            button("Run home", 100,540,600,50,green,bright_green, mouse_button, lambda:goto_subscene(20))

            pygame.display.update()
            
        elif display_subscene == 20:
            gameDisplay.fill(white)
            
            pilt3 = pygame.image.load("street.jpg")
            pilt3 = pygame.transform.scale(pilt3, (display_width, display_height))
            gameDisplay.blit(pilt3, (0, 0))

            blit_text(gameDisplay, scene_15, (20,20),meie_font)
            button("Try to break in from the front door", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(21))
            button("Go to the backyard", 100,400,600,50,green,bright_green, mouse_button, lambda:goto_subscene(24))

            pygame.display.update()
            
        elif display_subscene == 21:
            gameDisplay.fill(white)
            
            pilt4 = pygame.image.load("front.jpg")
            pilt4 = pygame.transform.scale(pilt4, (display_width, display_height))
            gameDisplay.blit(pilt4, (0, 0))

            blit_text(gameDisplay, scene_16_1, (20,20),meie_font)
            button("Go upstairs for your phone", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(22))
            button("Wash your cut and find bandages", 100,400,600,50,green,bright_green, mouse_button, lambda:goto_subscene(74))

            pygame.display.update()
            
        elif display_subscene == 22:
            gameDisplay.fill(white)
            
            pilt9 = pygame.image.load("room.jpg")
            pilt9 = pygame.transform.scale(pilt9, (display_width, display_height))
            gameDisplay.blit(pilt9, (0, 0))

            blit_text(gameDisplay, scene_16_1_1, (20,20),meie_font)
            button("Call Mom", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(23))
            button("Call Dad", 100,400,600,50,green,bright_green, mouse_button, lambda:goto_subscene(23))

            pygame.display.update()
            
        elif display_subscene == 23:
            gameDisplay.fill(white)
            
            pilt9 = pygame.image.load("room.jpg")
            pilt9 = pygame.transform.scale(pilt9, (display_width, display_height))
            gameDisplay.blit(pilt9, (0, 0))

            blit_text(gameDisplay, scene_16_1_2, (20,20),meie_font)
            button("Go downstairs", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(36))

            pygame.display.update()
######################################Backyard
        elif display_subscene == 24:
            gameDisplay.fill(white)
            
            pilt5 = pygame.image.load("back.jpg")
            pilt5 = pygame.transform.scale(pilt5, (display_width, display_height))
            gameDisplay.blit(pilt5, (0, 0))


            blit_text(gameDisplay, scene_15_1, (20,20),meie_font)
            button("Go upstairs", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(25))

            pygame.display.update()
            
        elif display_subscene == 25:
            gameDisplay.fill(white)
            
            pilt9 = pygame.image.load("room.jpg")
            pilt9 = pygame.transform.scale(pilt9, (display_width, display_height))
            gameDisplay.blit(pilt9, (0, 0))
            
            blit_text(gameDisplay, scene_15_2, (20,20),meie_font)
            
            button("Call Mom", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(26))
            button("Call Dad", 100,400,600,50,green,bright_green, mouse_button, lambda:goto_subscene(26))

            pygame.display.update()
            
        elif display_subscene == 26:
            gameDisplay.fill(white)
            
            pilt9 = pygame.image.load("room.jpg")
            pilt9 = pygame.transform.scale(pilt9, (display_width, display_height))
            gameDisplay.blit(pilt9, (0, 0))

            blit_text(gameDisplay, scene_15_3, (20,20),meie_font)
            button("Go downnstairs", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(27))

            pygame.display.update()
            
        elif display_subscene == 27:
            gameDisplay.fill(white)
            
            pilt6 = pygame.image.load("liv.jpg")
            pilt6 = pygame.transform.scale(pilt6, (display_width, display_height))
            gameDisplay.blit(pilt6, (0, 0))

            blit_text(gameDisplay, scene_15_4, (20,20),meie_font)
            
            button("Go to mom first", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(28))
            button("Go to dad first", 100,400,600,50,green,bright_green, mouse_button, lambda:goto_subscene(63))

            pygame.display.update()
#####################################Mother story            
        elif display_subscene == 28:
            gameDisplay.fill(white)
            
            pilt3 = pygame.image.load("street.jpg")
            pilt3 = pygame.transform.scale(pilt3, (display_width, display_height))
            gameDisplay.blit(pilt3, (0, 0))

            blit_text(gameDisplay, scene_15_5, (20,20),meie_font)
            button("Continue walking", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(29))

            pygame.display.update()
            
        elif display_subscene == 29:
            gameDisplay.fill(white)
            
            pilt3 = pygame.image.load("street.jpg")
            pilt3 = pygame.transform.scale(pilt3, (display_width, display_height))
            gameDisplay.blit(pilt1, (0, 0))

            blit_text(gameDisplay, scene_15_6, (20,20),meie_font)
            button("Move on", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(30))

            pygame.display.update()
            
        elif display_subscene == 30:
            gameDisplay.fill(white)
            
            pilt3 = pygame.image.load("street.jpg")
            pilt3 = pygame.transform.scale(pilt3, (display_width, display_height))
            gameDisplay.blit(pilt3, (0, 0))

            blit_text(gameDisplay, scene_15_7, (20,20),meie_font)
            button("Run away", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(31))

            pygame.display.update()
            
        elif display_subscene == 31:
            gameDisplay.fill(white)
            
            pilt3 = pygame.image.load("street.jpg")
            pilt3 = pygame.transform.scale(pilt3, (display_width, display_height))
            gameDisplay.blit(pilt3, (0, 0))

            blit_text(gameDisplay, scene_15_7_1, (20,20),meie_font)
            button("Continue", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(32))

            pygame.display.update()
            
        elif display_subscene == 32:
            gameDisplay.fill(white)
            
            pilt3 = pygame.image.load("street.jpg")
            pilt3 = pygame.transform.scale(pilt3, (display_width, display_height))
            gameDisplay.blit(pilt3, (0, 0))

            blit_text(gameDisplay, scene_15_8, (20,20),meie_font)
            button("Look at your parents", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(33))

            pygame.display.update()
            
        elif display_subscene == 33:
            gameDisplay.fill(white)
            
            pilt10 = pygame.image.load("car.jpg")
            pilt10 = pygame.transform.scale(pilt10, (display_width, display_height))
            gameDisplay.blit(pilt10, (0, 0))

            blit_text(gameDisplay, scene_15_9, (20,20),meie_font)
            button("Ask him, if everything is alright", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(34))

            pygame.display.update()
            
        elif display_subscene == 34:
            gameDisplay.fill(white)
            
            pilt10 = pygame.image.load("car.jpg")
            pilt10 = pygame.transform.scale(pilt10, (display_width, display_height))
            gameDisplay.blit(pilt10, (0, 0))

            blit_text(gameDisplay, scene_15_10, (20,20),meie_font)
            button("Look at the window", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(35))

            pygame.display.update()
            
        elif display_subscene == 35:
            gameDisplay.fill(white)
            
            pilt10 = pygame.image.load("car.jpg")
            pilt10 = pygame.transform.scale(pilt10, (display_width, display_height))
            gameDisplay.blit(pilt10, (0, 0))

            blit_text(gameDisplay, scene_15_11, (20,20),meie_font)
            button("To be continued...", 100,500,600,50,green,bright_green, mouse_button, quitgame)

            pygame.display.update()
###########################################Mother ending
        elif display_subscene == 36:
            gameDisplay.fill(white)
            
            pilt6 = pygame.image.load("liv.jpg")
            pilt6 = pygame.transform.scale(pilt6, (display_width, display_height))
            gameDisplay.blit(pilt6, (0, 0))

            blit_text(gameDisplay, scene_16_1_3, (20,20),meie_font)
            button("Look around for other options", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(37))

            pygame.display.update()
            
        elif display_subscene == 37:
            gameDisplay.fill(white)
            
            pilt9 = pygame.image.load("room.jpg")
            pilt9 = pygame.transform.scale(pilt9, (display_width, display_height))
            gameDisplay.blit(pilt9, (0, 0))

            blit_text(gameDisplay, scene_16_1_4, (20,20),meie_font)
            button("Run to the window and open it", 100,400,600,50,green,bright_green, mouse_button, lambda:goto_subscene(38))
            button("Open the door, and kick the 'thing'", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(37.5))

            pygame.display.update()
            
        elif display_subscene == 37.5:
            gameDisplay.fill(black)

            blit_text(gameDisplay, scene_16_1_4_3, (20,20),meie_font, color = white)
            button("YOU LOSE", 100,500,600,50,green,bright_green, mouse_button, quitgame)

            pygame.display.update()
            
        elif display_subscene == 38:
            gameDisplay.fill(white)
            
            pilt9 = pygame.image.load("room.jpg")
            pilt9 = pygame.transform.scale(pilt9, (display_width, display_height))
            gameDisplay.blit(pilt9, (0, 0))

            blit_text(gameDisplay, scene_16_1_4_1, (20,20),meie_font)
            button("Punch it", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(39))
            button("Jump", 100,400,600,50,green,bright_green, mouse_button, lambda:goto_subscene(42))

            pygame.display.update()
            
        elif display_subscene == 39:
            gameDisplay.fill(white)
            
            pilt9 = pygame.image.load("room.jpg")
            pilt9 = pygame.transform.scale(pilt9, (display_width, display_height))
            gameDisplay.blit(pilt9, (0, 0))

            blit_text(gameDisplay, scene_16_1_4_1_1, (20,20),meie_font)
            button("Crawl back", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(40))

            pygame.display.update()
            
        elif display_subscene == 40:
            gameDisplay.fill(white)
            
            pilt9 = pygame.image.load("room.jpg")
            pilt9 = pygame.transform.scale(pilt9, (display_width, display_height))
            gameDisplay.blit(pilt9, (0, 0))

            blit_text(gameDisplay, scene_16_1_4_1_2, (20,20),meie_font)
            button("Screem in dispair", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(41))

            pygame.display.update()
            
        elif display_subscene == 41:
            gameDisplay.fill(white)
            
            pilt9 = pygame.image.load("room.jpg")
            pilt9 = pygame.transform.scale(pilt9, (display_width, display_height))
            gameDisplay.blit(pilt9, (0, 0))

            blit_text(gameDisplay, scene_16_1_4_1_3, (20,20),meie_font)
            button("Game Over", 100,500,600,50,green,bright_green, mouse_button, quitgame)

            pygame.display.update()
            
        elif display_subscene == 42:
            gameDisplay.fill(white)
            
            pilt5 = pygame.image.load("back.jpg")
            pilt5 = pygame.transform.scale(pilt5, (display_width, display_height))
            gameDisplay.blit(pilt5, (0, 0))

            blit_text(gameDisplay, scene_16_1_4_2, (20,20),meie_font)
            button("Stand up and walk away", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(43))

            pygame.display.update()
            
        elif display_subscene == 43:
            gameDisplay.fill(white)
            
            pilt5 = pygame.image.load("back.jpg")
            pilt5 = pygame.transform.scale(pilt5, (display_width, display_height))
            gameDisplay.blit(pilt5, (0, 0))

            blit_text(gameDisplay, scene_17, (20,20),meie_font)
            button("Go to mom", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(44))
            button("Go to dad", 100,400,600,50,green,bright_green, mouse_button, lambda:goto_subscene(52))

            pygame.display.update()
            
        elif display_subscene == 44:
            gameDisplay.fill(white)
            
            pilt3 = pygame.image.load("street.jpg")
            pilt3 = pygame.transform.scale(pilt3, (display_width, display_height))
            gameDisplay.blit(pilt3, (0, 0))

            blit_text(gameDisplay, scene_17_1, (20,20),meie_font)
            button("Continue walking", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(45))

            pygame.display.update()
            
        elif display_subscene == 45:
            gameDisplay.fill(white)
            
            pilt3 = pygame.image.load("street.jpg")
            pilt3 = pygame.transform.scale(pilt3, (display_width, display_height))
            gameDisplay.blit(pilt3, (0, 0))

            blit_text(gameDisplay, scene_17_2, (20,20),meie_font)
            button("Move on", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(46))

            pygame.display.update()
            
        elif display_subscene == 46:
            gameDisplay.fill(white)
            
            pilt3 = pygame.image.load("street.jpg")
            pilt3 = pygame.transform.scale(pilt3, (display_width, display_height))
            gameDisplay.blit(pilt3, (0, 0))

            blit_text(gameDisplay, scene_17_3, (20,20),meie_font)
            button("Run away", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(47))

            pygame.display.update()
            
        elif display_subscene == 47:
            gameDisplay.fill(white)
            
            pilt3 = pygame.image.load("street.jpg")
            pilt3 = pygame.transform.scale(pilt3, (display_width, display_height))
            gameDisplay.blit(pilt3, (0, 0))

            blit_text(gameDisplay, scene_17_4, (20,20),meie_font)
            button("Continue", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(48))

            pygame.display.update()
            
        elif display_subscene == 48:
            gameDisplay.fill(white)
            
            pilt3 = pygame.image.load("street.jpg")
            pilt3 = pygame.transform.scale(pilt3, (display_width, display_height))
            gameDisplay.blit(pilt3, (0, 0))

            blit_text(gameDisplay, scene_17_5, (20,20),meie_font)
            button("", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(49))

            pygame.display.update()
            
        elif display_subscene == 49:
            gameDisplay.fill(white)
            
            pilt10 = pygame.image.load("car.jpg")
            pilt10 = pygame.transform.scale(pilt10, (display_width, display_height))
            gameDisplay.blit(pilt10, (0, 0))

            blit_text(gameDisplay, scene_17_6, (20,20),meie_font)
            button("Ask him, if everything is ok", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(50))

            pygame.display.update()
            
        elif display_subscene == 50:
            gameDisplay.fill(white)
            
            pilt10 = pygame.image.load("car.jpg")
            pilt10 = pygame.transform.scale(pilt10, (display_width, display_height))
            gameDisplay.blit(pilt10, (0, 0))

            blit_text(gameDisplay, scene_17_7, (20,20),meie_font)
            button("Look in the window", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(51))

            pygame.display.update()
            
        elif display_subscene == 51:
            gameDisplay.fill(white)
            
            pilt10 = pygame.image.load("car.jpg")
            pilt10 = pygame.transform.scale(pilt10, (display_width, display_height))
            gameDisplay.blit(pilt10, (0, 0))

            blit_text(gameDisplay, scene_17_8, (20,20),meie_font)
            button("To be continued...", 100,500,600,50,green,bright_green, mouse_button, quitgame)

            pygame.display.update()
            
        elif display_subscene == 52:
            gameDisplay.fill(white)
            
            pilt7 = pygame.image.load("dad.jpg")
            pilt7 = pygame.transform.scale(pilt7, (display_width, display_height))
            gameDisplay.blit(pilt7, (0, 0))

            blit_text(gameDisplay, scene_17__1, (20,20),meie_font)
            button("Look around the corner", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(53))
            button("Move on", 100,400,600,50,green,bright_green, mouse_button, lambda:goto_subscene(54))

            pygame.display.update()
            
        elif display_subscene == 53:
            gameDisplay.fill(white)
            
            pilt7 = pygame.image.load("dad.jpg")
            pilt7 = pygame.transform.scale(pilt7, (display_width, display_height))
            gameDisplay.blit(pilt7, (0, 0))

            blit_text(gameDisplay, scene_17__2, (20,20),meie_font)
            button("Continue", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(54))
            

            pygame.display.update()
            
        elif display_subscene == 54:
            gameDisplay.fill(white)
            
            pilt7 = pygame.image.load("dad.jpg")
            pilt7 = pygame.transform.scale(pilt7, (display_width, display_height))
            gameDisplay.blit(pilt7, (0, 0))

            blit_text(gameDisplay, scene_17__3, (20,20),meie_font)
            button("Run away", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(55))

            pygame.display.update()
            
        elif display_subscene == 55:
            gameDisplay.fill(white)
            
            pilt7 = pygame.image.load("dad.jpg")
            pilt7 = pygame.transform.scale(pilt7, (display_width, display_height))
            gameDisplay.blit(pilt7, (0, 0))

            blit_text(gameDisplay, scene_17__4, (20,20),meie_font)
            button("Continue", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(56))

            pygame.display.update()
            
        elif display_subscene == 56:
            gameDisplay.fill(white)
            
            pilt7 = pygame.image.load("dad.jpg")
            pilt7 = pygame.transform.scale(pilt7, (display_width, display_height))
            gameDisplay.blit(pilt7, (0, 0))

            blit_text(gameDisplay, scene_17__5, (20,20),meie_font)
            button("Continue", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(57))

            pygame.display.update()
            
        elif display_subscene == 57:
            gameDisplay.fill(white)
            
            pilt7 = pygame.image.load("dad.jpg")
            pilt7 = pygame.transform.scale(pilt7, (display_width, display_height))
            gameDisplay.blit(pilt7, (0, 0))

            blit_text(gameDisplay, scene_17__6, (20,20),meie_font)
            button("Continue", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(58))

            pygame.display.update()
            
        elif display_subscene == 58:
            gameDisplay.fill(white)
            
            pilt7 = pygame.image.load("dad.jpg")
            pilt7 = pygame.transform.scale(pilt7, (display_width, display_height))
            gameDisplay.blit(pilt7, (0, 0))

            blit_text(gameDisplay, scene_17__7, (20,20),meie_font)
            button("Continue", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(59))

            pygame.display.update()
            
        elif display_subscene == 59:
            gameDisplay.fill(white)
            
            pilt7 = pygame.image.load("dad.jpg")
            pilt7 = pygame.transform.scale(pilt7, (display_width, display_height))
            gameDisplay.blit(pilt7, (0, 0))

            blit_text(gameDisplay, scene_17__8, (20,20),meie_font)
            button("Continue", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(60))

            pygame.display.update()
            
        elif display_subscene == 60:
            gameDisplay.fill(black)

            blit_text(gameDisplay, scene_17__9, (20,20),meie_font, color = white)
            button("Continue", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(61))

            pygame.display.update()
            
        elif display_subscene == 61:
            gameDisplay.fill(black)

            blit_text(gameDisplay, scene_17__10, (20,20),meie_font, color = white)
            button("Open your eyes", 100,500,600,50,green,bright_green, mouse_button, quitgame)

            pygame.display.update()
#########################################Dad story in backyard          
        elif display_subscene == 63:
            gameDisplay.fill(white)
            
            pilt7 = pygame.image.load("dad.jpg")
            pilt7 = pygame.transform.scale(pilt7, (display_width, display_height))
            gameDisplay.blit(pilt7, (0, 0))

            blit_text(gameDisplay, scene_15__2, (20,20),meie_font)
            button("Look around the corner", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(64))
            button("Move on", 100,400,600,50,green,bright_green, mouse_button, lambda:goto_subscene(65))

            pygame.display.update()
            
        elif display_subscene == 64:
            gameDisplay.fill(white)
            
            pilt7 = pygame.image.load("dad.jpg")
            pilt7 = pygame.transform.scale(pilt7, (display_width, display_height))
            gameDisplay.blit(pilt7, (0, 0))

            blit_text(gameDisplay, scene_15__2_1, (20,20),meie_font)
            button("Continue", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(65))

            pygame.display.update()
            
        elif display_subscene == 65:
            gameDisplay.fill(white)
            
            pilt7 = pygame.image.load("dad.jpg")
            pilt7 = pygame.transform.scale(pilt7, (display_width, display_height))
            gameDisplay.blit(pilt7, (0, 0))

            blit_text(gameDisplay, scene_15__3, (20,20),meie_font)
            button("Continue", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(66))

            pygame.display.update()
            
        elif display_subscene == 66:
            gameDisplay.fill(white)
            
            pilt7 = pygame.image.load("dad.jpg")
            pilt7 = pygame.transform.scale(pilt7, (display_width, display_height))
            gameDisplay.blit(pilt7, (0, 0))

            blit_text(gameDisplay, scene_15__4, (20,20),meie_font)
            button("Continue", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(67))

            pygame.display.update()
            
        elif display_subscene == 67:
            gameDisplay.fill(white)
            
            pilt7 = pygame.image.load("dad.jpg")
            pilt7 = pygame.transform.scale(pilt7, (display_width, display_height))
            gameDisplay.blit(pilt7, (0, 0))

            blit_text(gameDisplay, scene_15__5, (20,20),meie_font)
            button("Continue", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(68))

            pygame.display.update()
            
        elif display_subscene == 68:
            gameDisplay.fill(white)
            
            pilt7 = pygame.image.load("dad.jpg")
            pilt7 = pygame.transform.scale(pilt7, (display_width, display_height))
            gameDisplay.blit(pilt7, (0, 0))

            blit_text(gameDisplay, scene_15__6, (20,20),meie_font)
            button("Continue", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(69))

            pygame.display.update()
            
        elif display_subscene == 69:
            gameDisplay.fill(white)
            
            pilt10 = pygame.image.load("car.jpg")
            pilt10 = pygame.transform.scale(pilt10, (display_width, display_height))
            gameDisplay.blit(pilt10, (0, 0))

            blit_text(gameDisplay, scene_15__7, (20,20),meie_font)
            button("Continue", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(70))

            pygame.display.update()
            
        elif display_subscene == 70:
            gameDisplay.fill(white)
            
            pilt10 = pygame.image.load("car.jpg")
            pilt10 = pygame.transform.scale(pilt10, (display_width, display_height))
            gameDisplay.blit(pilt10, (0, 0))

            blit_text(gameDisplay, scene_15__8, (20,20),meie_font)
            button("Continue", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(71))

            pygame.display.update()
            
        elif display_subscene == 71:
            gameDisplay.fill(white)
            
            pilt10 = pygame.image.load("car.jpg")
            pilt10 = pygame.transform.scale(pilt10, (display_width, display_height))
            gameDisplay.blit(pilt10, (0, 0))

            blit_text(gameDisplay, scene_15__9, (20,20),meie_font)
            button("Continue", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(72))

            pygame.display.update()
            
        elif display_subscene == 72:
            gameDisplay.fill(white)
            
            pilt10 = pygame.image.load("car.jpg")
            pilt10 = pygame.transform.scale(pilt10, (display_width, display_height))
            gameDisplay.blit(pilt10, (0, 0))

            blit_text(gameDisplay, scene_15__10, (20,20),meie_font)
            button("Continue", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(73))

            pygame.display.update()
            
        elif display_subscene == 73:
            gameDisplay.fill(white)
            
            pilt10 = pygame.image.load("car.jpg")
            pilt10 = pygame.transform.scale(pilt10, (display_width, display_height))
            gameDisplay.blit(pilt10, (0, 0))

            blit_text(gameDisplay, scene_15__11, (20,20),meie_font)
            button("To be continued...", 100,500,600,50,green,bright_green, mouse_button, quitgame)

            pygame.display.update()
            
        elif display_subscene == 74:
            gameDisplay.fill(white)
            
            pilt2 = pygame.image.load("kitchen.jpg")
            pilt2 = pygame.transform.scale(pilt2, (display_width, display_height))
            gameDisplay.blit(pilt1, (0, 0))

            blit_text(gameDisplay, scene_16_2_1, (20,20),meie_font)
            button("Continue", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(75))

            pygame.display.update()
            
        elif display_subscene == 75:
            gameDisplay.fill(white)

            blit_text(gameDisplay, scene_16_1_4, (20,20),meie_font)
            button("Run to the window and open it", 100,500,600,50,green,bright_green, mouse_button, lambda:goto_subscene(38))
            button("Open the door and kick the 'thing'", 100,400,600,50,green,bright_green, mouse_button, lambda:goto_subscene(37.5))

            pygame.display.update()
            
            
            
# --- main ---

# - init -

pygame.init()
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Just one another day')

# - m

clock = pygame.time.Clock() 
pause = False

game_intro()
game_loop()
pygame.quit()