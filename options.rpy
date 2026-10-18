## هذا الملف يحتوي على الخيارات التي تستطيع تعديلها لتغيير محتويات لعبتك.
##
## الأسطر التي تبدأ بهذا الشعار مرتين'#' هي أسطر مقتبسه و لا يفترض عليك تغييرها.
## الأسطر التي تحتوي على '#' واحده هي أسطر برمجة يمكنك الغاء الاقتباس عندها
## لتفعيلها.


## الأساسيات ###################################################################

## الإسم الرسمي للعبه. يتم استعمال هذا السطر كإسم النافذة و يظهرفي واجهة النظام
## التشغيلية و ملفات حصر الأخطاء.
##
## رمز _() حول النصوص يجعلها قابلة للترجمة.

define config.name = _("day")


## يحدد إذا ما تم إظهار العنوان في القائمة الرئيسية. لإخفاء العنوان اجعله False.

define gui.show_name = True


## نسخه اللعبة.

define config.version = "1.0"


## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
""")


## اسم مختصر للعبه يتم استعماله في ملفات التشغيل و نسخ النشر. يجب ان يحتوي على
## احرف انجليزية فقط, دون فراغات ولا فواصل ولا فواصل منقوطة.

define build.name = "day"


## الصوت و الموسيقى ############################################################

## These three variables control, among other things, which mixers are shown
## to the player by default. Setting one of these to False will hide the
## appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## يسمح للاعب ان يسمع صوتا لاختبار ارتفاع الصوت او النطق, إمسح الاقتباس عن السطر
## التالي ليتم تفعيل زر العينة الصوتية.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

# define config.main_menu_music = "main-menu-theme.ogg"


## الإنتقال ####################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## الدخول او الخروج من قائمة اللعبة.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Between screens of the game menu.

define config.intra_transition = dissolve


## الإنتقال الذي يحصل بعد ان تنتهي اللعبة من الإقلاع.

define config.after_load_transition = None


## يظهر عند الدخول إلى القائمة الرئيسية بعد انتهاء اللعبة.

define config.end_game_transition = None


## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## خيارات النافذة ##############################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## الإنتقالات البصرية المستخدمه عند إظهار و إخفاء مربع الحوار

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## الخيارات القياسية ###########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 0


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15


## مجلد الحفظ ##################################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "day-1792132519"


## Icon ########################################################################
##
## الأيقونة الظاهرة في شريط البرامج.

define config.window_icon = "gui/window_icon.png"


## معلومات ملف النشر ###########################################################
##
## هذا الجزء يتحكم بالمعلومات التي يستعملها رينباي لتحويل مشروعك إلى ملفات يمكن
## نشرها.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')


## A Google Play license key is required to perform in-app purchases. It can be
## found in the Google Play developer console, under "Monetize" > "Monetization
## Setup" > "Licensing".

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "renpytom/test-project"
