import time  


answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]



sword = 0
flower = 0

required = ("\nUse only A, B, or C\n")  





def intro():
    print("After a drunken night out with friends, you awaken the "
          "next morning in a thick, dank forest.\nHead spinning and "
          "fighting the urge to vomit, you stand and marvel at your new, "
          "unfamiliar setting.\nThe peace quickly fades when you hear a "
          "grotesque sound emitting behind you.\nA slobbering orc is "
          "running towards you.\nYou will:")
    
    time.sleep(1)
    print("""  A. Grab a nearby rock and throw it at the orc
  B. Lie down and wait to be mauled
  C. Run""")
    choice = input(">>> ")  
    
    if choice in answer_A:
        option_rock()
    elif choice in answer_B:
        print("\nWelp, that was quick. "
              "\n\nYou died!")
    elif choice in answer_C:
        option_run()
    else:
        print(required)
        intro()


def option_rock():
    print("\nThe orc is stunned, but regains control. He begins "
          "running towards you again.\nWill you:")
    time.sleep(1)
    print("""  A. Run
  B. Throw another rock
  C. Run towards a nearby cave""")
    choice = input(">>> ")
    if choice in answer_A:
        option_run()
    elif choice in answer_B:
        print("\nYou decided to throw another rock, as if the first "
              "rock thrown did much damage. The rock flew well over the "
              "orcs head. You missed. \n\nYou died!")
    elif choice in answer_C:
        option_cave()
    else:
        print(required)
        option_rock()


def option_cave():
    print("\nYou were hesitant, since the cave was dark and "
          "ominous.\nBefore you fully enter, you notice a shiny sword on "
          "the ground.\nDo you pick up a sword. Y/N?")
    choice = input(">>> ")
    if choice in yes:
        sword = 1  
    else:
        sword = 0
    print("\nWhat do you do next?")
    time.sleep(1)
    print("""  A. Hide in silence
  B. Fight
  C. Run""")
    choice = input(">>> ")
    if choice in answer_A:
        print("\nReally? You're going to hide in the dark? I think "
              "orcs can see very well in the dark, right? Not sure, but "
              "I'm going with YES, so...\n\nYou died!")
    elif choice in answer_B:
        if sword > 0:
            print("\nYou laid in wait.\nThe shimmering sword attracted "
                  "the orc, which thought you were no match.\nAs he walked "
                  "closer and closer, your heart beat rapidly.\nAs the orc "
                  "reached out to grab the sword, you pierced the blade into "
                  "its chest. \n\nYou survived!")
        else:  # If the user didn't grab the sword
            print("\nYou should have picked up that sword. You're "
                  "defenseless. \n\nYou died!")
    elif choice in answer_C:
        print("As the orc enters the dark cave, you sliently "
              "sneak out.\nYou're several feet away, but the orc turns "
              "around and sees you running.")
        option_run()
    else:
        print(required)
        option_cave()


def option_run():
    print("\nYou run as quickly as possible, but the orc's "
          "speed is too great.\nYou will:")
    time.sleep(1)
    print("""  A. Hide behind boulder
  B. Trapped, so you fight
  C. Run towards an abandoned town""")
    choice = input(">>> ")
    if choice in answer_A:
        print("You're easily spotted. "
              "\n\nYou died!")
    elif choice in answer_B:
        print("\nYou're no match for an orc. "
              "\n\nYou died!")
    elif choice in answer_C:
        option_town()
    else:
        print(required)
        option_run()


def option_town():
    print("\nWhile frantically running, you notice a rusted "
          "sword lying in the mud.\nYou quickly reach down and grab it, "
          "but miss.\nYou try to calm your heavy breathing as you hide "
          "behind a delapitated building, waiting for the orc to come "
          "charging around the corner.\nYou notice a purple flower "
          "near your foot.\nDo you pick it up? Y/N")
    choice = input(">>> ")
    if choice in yes:
        flower = 1  
    else:
        flower = 0
    print("You hear its heavy footsteps and ready yourself for "
          "the impending orc.")
    time.sleep(1)
    if flower > 0:
        print("\nYou quickly hold out the purple flower, somehow "
              "hoping it will stop the orc.\nIt does! The orc was looking "
              "for love. "
              "\n\nThis got weird, but you survived!")
    else:  
        print("\nMaybe you should have picked up the flower. "
              "\n\nYou died!")


intro()
