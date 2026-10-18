 # ==========================================
# VISUAL NOVEL - DAY 1
# ==========================================

define config.screen_width = 1920
define config.screen_height = 1080
define config.default_text_cps = 1000
define config.default_afm_time = 10

# ------------------------------------------
# CHARACTERS
# ------------------------------------------

define p = Character("[player_name]", color="#c8ffc8")
define Lili = Character("Lili", color="#ffc8c8")
define Customer1 = Character("Customer 1", color="#ffffff")
define Customer2 = Character("Customer 2", color="#ffffff")
define Customer3 = Character("Customer 3", color="#ffffff")
define Ilya = Character("Ilya", color="#c8e8ff")
define Angel = Character("Angel", color="#e8c8ff")
define Nora = Character("Nora", color="#ffe8c8")
define Talya = Character("Talya", color="#ffc8e8")

default player_name = ""
default lower_name = ""
default is_kawtar = False
default is_mehdi = False

# ------------------------------------------
# BACKGROUNDS
# ------------------------------------------

image bg kalfiya1 = "images/images/kalfiya1.png"
image bg kalfiya2 = "images/images/kalfiya2.png"

image bg kalfiya3:
    "images/images/kalfiya3.png"
    xysize (1920, 1080)

# ------------------------------------------
# CHARACTER IMAGES
# ------------------------------------------

image freind = "images/images/freind.png"
image zabon1 = "images/images/zabon1.png"
image zabon2 = "images/images/zabon2.png"
image zabon3 = "images/images/zabon3.png"

# Enlarge freind only.
# Change zoom to 2.5 if she is still too small.
transform freind_position:
    xalign 0.5
    yalign 1.0
    zoom 3.0

# Keep customer images at their original size.
transform customer_position:
    xalign 0.5
    yalign 1.0

# ------------------------------------------
# SCREEN SHAKE
# ------------------------------------------

transform shake:
    xoffset 0
    linear 0.05 xoffset -10
    linear 0.05 xoffset 10
    linear 0.05 xoffset -7
    linear 0.05 xoffset 7
    linear 0.05 xoffset 0

# ==========================================
# START
# ==========================================

label start:

    scene black
    with hpunch

    pause 1.0

    "..."

    "You slowly open your heavy, sleepy eyes."

    jump enter_player_name

# ==========================================
# PLAYER NAME
# ==========================================

label enter_player_name:

    $ player_name = renpy.input(
        "What is your name?",
        length=20
    ).strip()

    $ lower_name = player_name.lower()

    if lower_name in ["arwa", "أروى", "آروى"]:
        "Please choose another name."
        jump enter_player_name

    if player_name == "":
        $ player_name = "Emiri"

    $ lower_name = player_name.lower()

    $ is_kawtar = lower_name in ["kawtar", "كوثر"]
    $ is_mehdi = lower_name in ["mehdi", "مهدي", "medi"]

    if is_kawtar:
        $ player_name = "Kawtar"
    elif is_mehdi:
        $ player_name = "Mehdi"

    jump day1_wakeup

# ==========================================
# DAY 1 - WAKING UP
# kalfiya3 + freind
# ==========================================

label day1_wakeup:

    scene bg kalfiya3
    with fade

    show freind at freind_position
    with dissolve

    if is_kawtar:
        Lili "Kawtar, wake up, sweetheart. We have work to do."
        Lili "Come on, sleepyhead. We can't stay here all morning."
    else:
        Lili "Wake up, wake up. We have work. Why are you still sleeping?"
        Lili "Come on, get up and move away from me."

    if is_mehdi:
        p "Wakha, rah ghadi noud."
    else:
        p "Okay, I'm getting up."

    menu:
        "Shut up, you bitch.":
            if is_kawtar:
                Lili "Hey, sweetheart, what's gotten into you?"
                p "..."
            elif is_mehdi:
                p "Skoti a l9e7ba."
                Lili "Hey, what's your problem?"
                p "..."
            else:
                p "Shut up, you bitch."
                Lili "Hey, what's wrong with you, bitch?"
                p "..."

        "I'm sorry.":
            if is_kawtar:
                p "I'm sorry, Lili."
                Lili "It's okay, sweetheart. Just get up."
            elif is_mehdi:
                p "Sme7i lia hadik zamla 9a7ba tabona."
                Lili "Fuck you. Don't talk again."
                p "Hehehehe."
            else:
                p "I'm sorry."
                Lili "..."
                p "(I feel like she got a little embarrassed.)"

    jump cafe_customer_phase

# ==========================================
# CAFE - CUSTOMER 1
# kalfiya1 + zabon1 + kalfiya2
# ==========================================

label cafe_customer_phase:

    scene bg kalfiya1
    with fade

    show zabon1 at customer_position
    show bg kalfiya2 as counter zorder 10

    "The café gets busier as customers start arriving."

    if is_kawtar:
        Customer1 "Hi! Could I please have two iced lattes?"
    else:
        Customer1 "Hi... excuse me... could I get two iced lattes?"

    if is_mehdi:
        p "Ah wakha. Bghiti chi haja khra?"
    else:
        p "Yeah, okay. Anything else?"

    Customer1 "Oh, no."

    menu:
        "Don't be nervous. Relax, nothing is worth stressing over.":
            if is_kawtar:
                p "Don't worry, take your time. Everything will be okay."
                Customer1 "Thank you. I'm a little nervous. This is my first time going out with someone."
            elif is_mehdi:
                p "Matkafich, heni rassek. Ma kayn 3lach t9el9i."
                Customer1 "Oh yeah, but I'm a little nervous. This is my first time going out with someone."
            else:
                p "Don't be nervous. Just relax; it's not worth stressing over."
                Customer1 "Oh yeah, but I'm a little nervous. This is my first time going out with someone."

            if is_mehdi:
                p "Ma3lich, ghadi twelifi l'ambiance bzerba. Chno smiytek bach nktebha?"
            else:
                p "It's okay, you'll get used to the vibe quickly. What's your name so I can write it down?"

            Customer1 "You're right. My name is Ilya."

            if is_mehdi:
                p "Oh, smiytek zwina bezaf."
            else:
                p "Oh, your name is so pretty."

            Ilya "Oh, thank you so much."

            jump customer_two_calm_route

        "Ignore.":
            if is_mehdi:
                p "Wakha, smiya 3afak?"
            else:
                p "Okay, name please?"

            Customer1 "Oh, write Ilya."

            if is_mehdi:
                p "Wakha, chokran."
            else:
                p "Okay, thanks."

            jump customer_two_ignore_route

# ==========================================
# CUSTOMER 2 - CALM ROUTE
# ==========================================

label customer_two_calm_route:

    scene bg kalfiya1

    show zabon2 at customer_position
    show bg kalfiya2 as counter zorder 10

    if is_kawtar:
        Customer2 "Excuse me, could I please order? I've been waiting for a little while."
    else:
        Customer2 "What is this? Why are you so slow? What kind of service is this? Ugh, what a mess."

    menu:
        "Apologize.":
            if is_mehdi:
                p "Sme7 lia."
            else:
                p "I'm sorry."

            if is_kawtar:
                Customer2 "That's alright, sweetheart. I'd like an iced Americano and a turkey sandwich, please."
            else:
                Customer2 "Ah, good, that's better. Anyway, give me an iced Americano and a turkey sandwich."

            if is_mehdi:
                p "Wakha. Chno smiytek bach nktebha?"
            else:
                p "Okay. What's your name so I can write it down?"

            Customer2 "My name is Angel."

            jump customer_three_apology_route

        "No, what's your problem? You're angry. Calm down a bit.":
            if is_kawtar:
                p "I'm sorry, but please be patient. I'll help you in a moment."
                Customer2 "Oh, of course. I'm sorry for rushing you."
                jump customer_three_angry_route

            elif is_mehdi:
                p "Hedni chwia, 3lach m3esseb?"
                Customer2 "You're the one who's so slow! Are you serious? What kind of treatment is this?"
                p "..."
                Customer2 "Ugh, what service! I'll give you one star for this treatment."
                p "Dirha, chkoun li wa9efek?"
                Customer2 "Oh, you talk back? Fine, I won't come back again."
                p "..."
                jump customer_three_angry_route

            else:
                p "Calm down. Why are you so angry?"
                Customer2 "You're the one who's so slow! Are you serious? What kind of treatment is this?"
                p "..."
                Customer2 "Ugh, what service! I'll give you one star for this treatment."
                p "Rate it. Who's stopping you?"
                Customer2 "Oh, you talk back? Fine, I won't come back again."
                p "..."
                jump customer_three_angry_route

# ==========================================
# CUSTOMER 3 - APOLOGY ROUTE
# ==========================================

label customer_three_apology_route:

    scene bg kalfiya1

    show zabon3 at customer_position
    show bg kalfiya2 as counter zorder 10

    Customer3 "Hi! Could I please have a banana and strawberry smoothie?"

    if is_mehdi:
        p "Wakha, chno smiytek?"
    else:
        p "Okay, what's your name?"

    Customer3 "Write Talya."

    if is_mehdi:
        p "Oh, smiytek zwina."
    else:
        p "Oh, your name is pretty."

    Talya "Thanks."

    jump day1_end

# ==========================================
# CUSTOMER 3 - ANGRY ROUTE
# ==========================================

label customer_three_angry_route:

    scene bg kalfiya1

    show zabon3 at customer_position
    show bg kalfiya2 as counter zorder 10

    if is_kawtar:
        Customer3 "Hey, don't let it upset you, sweetheart. Could I have a classic chocolate cake, please?"
    else:
        Customer3 "Hey, don't take it personally. Anyway, could I have a classic chocolate cake, please?"

    if is_mehdi:
        p "Chokran. Bghiti chi haja khra?"
    else:
        p "Thanks. Anything else?"

    Customer3 "Yeah, an iced latte and chocolate milk, please."

    if is_mehdi:
        p "Wakha, chno smiytek?"
    else:
        p "Okay, what's your name?"

    Customer3 "Write Talya."

    if is_mehdi:
        p "Smiytek zwina."
    else:
        p "Your name is pretty."

    Talya "Thanks."

    jump day1_end

# ==========================================
# CUSTOMER 2 - IGNORE ROUTE
# ==========================================

label customer_two_ignore_route:

    scene bg kalfiya1

    show zabon2 at customer_position
    show bg kalfiya2 as counter zorder 10

    Customer2 "Give me two iced Americanos, an iced latte, coffee, and iced tea."

    if is_mehdi:
        p "Wakha, chno smiytek?"
    else:
        p "Okay, name please?"

    Customer2 "Write Nora."

    if is_mehdi:
        p "Oh, smiytek zwina."
    else:
        p "Oh, your name is pretty."

    Nora "Hurry up, please."

    jump customer_three_ignore_route

# ==========================================
# CUSTOMER 3 - IGNORE ROUTE
# ==========================================

label customer_three_ignore_route:

    scene bg kalfiya1

    show zabon3 at customer_position
    show bg kalfiya2 as counter zorder 10

    Customer3 "Please give me an iced latte and chocolate milk."

    if is_mehdi:
        p "Wakha, chno smiytek?"
    else:
        p "Okay, name please?"

    Customer3 "Write Talya."

    if is_mehdi:
        p "Oh, smiytek zwina."
    else:
        p "Oh, your name is pretty."

    Talya "Thanks."

    if is_kawtar:
        p "(Finally, the day is over. At least everything went well.)"
    elif is_mehdi:
        p "(Finally salat nhar. 3la l'a9al khlesso mzyan.)"
    else:
        p "(Finally, the day is over. At least that part went well.)"

    jump day1_end

# ==========================================
# END OF DAY 1
# ==========================================

label day1_end:

    scene black
    with fade

    if is_kawtar:
        p "Finally, the day is over. I'm going home, and I can finally rest."
    elif is_mehdi:
        p "Finally salat had nhar. Ghadi nrou7 ldar daba."
    else:
        p "Finally, the day is over. What a mess. I'm going home."

    centered "DAY 1 COMPLETE"

    return