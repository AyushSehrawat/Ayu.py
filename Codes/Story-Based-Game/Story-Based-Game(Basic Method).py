# A Story Based Adventure Game (Basic-Methods)
import time

print('Welcome to Story-Based-Adventure-Game\nRead the instructions carefully!')
time.sleep(0.2)

print('Loading plot...')
time.sleep(2)
print('-' * 40)

print("Please only use A,B or C\nWhere asked for yes or no , type Y OR N")
time.sleep(2)
print('-' * 40)

intro = input("After a drunken night out with friends, you awaken the "
              "next morning in a thick, dank forest.\nHead spinning and "
              "fighting the urge to vomit, you stand and marvel at your new, "
              "unfamiliar setting.\nThe peace quickly fades when you hear a "
              "grotesque sound emitting behind you.\nA slobbering orc is "
              "running towards you.\nWhat will you do?\nA.) Grab a nearby rock and throw it at the orc\nB.) Lie down "
              "and wait to be mauled\nC.) Run\n>>> ").upper()

time.sleep(5)

if intro == 'A':
    rock1 = input("\n\nThe orc is stunned, but regains control. He begins "
                  "running towards you again.\nWhat will you do?\nA.) Run\
                  B.) Throw another rock\nC.) Run towards a nearby cave\n>>> ").upper()

    time.sleep(2)

    if rock1 == 'A':
        rock2 = input("\nYou run as quickly as possible, but the orc's "
                      "speed is too great\nWhat will you do?\nA.) Hide behind boulder"
                      "\nB.) Trapped so you fight\nC.) Run towards an abandoned town\n>>> ").upper()

        time.sleep(2)

        if rock2 == 'A':
            print('You are easily spotted!\n\nYou died!')

        elif rock2 == 'B':
            print("You're no match for an orc\n\nYou died!")

        if rock2 == 'C':
            rock3 = input("\nWhile frantically running, you notice a rusted "
                          "sword lying in the mud.\nYou quickly reach down and grab it, "
                          "but miss.\nYou try to calm your heavy breathing as you hide "
                          "behind a delapitated building, waiting for the orc to come "
                          "charging around the corner.\nYou notice a purple flower "
                          "near your foot.\nDo you pick it up? Y/N\n>>> ").upper()

            time.sleep(2)

            if rock3 == 'Y':
                print("You hear its heavy footsteps and ready yourself for "
                      "the impending orc.")
                print("\nYou quickly hold out the purple flower, somehow "
                      "hoping it will stop the orc. It does! The orc was looking "
                      "for love. "
                      "\n\nThis got weird, but you survived!")

                time.sleep(2)

            elif rock3 == 'N':
                print("You hear its heavy footsteps and ready yourself for "
                      "the impending orc.")
                print("\nMaybe you should have picked up the flower. "
                      "\n\nYou died!")

                time.sleep(2)

            else:
                print('You chose none of the above!\nSo you died!')

if intro == 'B':
    print("\nWelp, that was quick. "
          "\n\nYou died!")

if intro == 'C':
    run1 = input("You run as quickly as possible, but the orc's "
                 "speed is too great.\nWhat will you do?\nA.) Hide behind boulder"
                 "\nB.) Trapped so you fight\nC.) Run towards the abandoned town\n>>> ").upper()

    time.sleep(2)

    if run1 == 'A':
        print('You are easily spotted\n\nYou died!')

    elif run1 == 'B':
        print('You are no match for an orc\n\nYou died! ')
    elif run1 == 'C':

        run2 = input("\nWhile frantically running, you notice a rusted "
                     "sword lying in the mud.\nYou quickly reach down and grab it, "
                     "but miss.\nYou try to calm your heavy breathing as you hide "
                     "behind a delapitated building, waiting for the orc to come "
                     "charging around the corner.\nYou notice a purple flower "
                     "near your foot.\nDo you pick it up? Y/N\n>>> ").upper()

        time.sleep(2)

        if run2 == 'Y':
            print("You hear its heavy footsteps and ready yourself for "
                  "the impending orc.")
            print("\nYou quickly hold out the purple flower, somehow "
                  "hoping it will stop the orc. It does! The orc was looking "
                  "for love. "
                  "\n\nThis got weird, but you survived!")

            time.sleep(2)

        elif run2 == 'N':
            print("You hear its heavy footsteps and ready yourself for "
                  "the impending orc.")
            print('Maybe you should have taken it\n\nYou died')

            time.sleep(2)

        else:
            print('You chose something else\nYou died')

