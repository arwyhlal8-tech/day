################################################################################
## تتم التهيئة الآن
################################################################################

## The init offset statement causes the initialization statements in this file
## to run before init statements in any other file.
init offset = -2

## Calling gui.init resets the styles to sensible default values, and sets the
## width and height of the game.
init python:
    gui.init(1920, 1080)

## Enable checks for invalid or unstable properties in screens or transforms
define config.check_conflicting_properties = True


################################################################################
## GUI Configuration Variables
################################################################################


## الألوان #####################################################################
##
## ألوان الخطوط الظاهرة في الواجهة.

## لون إضافي ينطبق على الوسوم و العناوين الرئيسية في اماكن مختلفة من الواجهة.
define gui.accent_color = '#0099cc'

## اللون المطلوب للأزرار حين لا تكون قيد الاستعمال ولا مظللة.
define gui.idle_color = '#888888'

## اللون الصغير هو اللون الذي ينطبق على الخطوط الصغيرة, والتي تحتاج ان تكون ذات
## لون فاتح او داكن اكثر مما حولها لتظهر بشكل واضح.
define gui.idle_small_color = '#aaaaaa'

## اللون الذي ينطبق على الازرار و اشرطة التمرير عند تظليلها بالمؤشر.
define gui.hover_color = '#66c1e0'

## اللون الذي ينطبق على الزر المفعّل الآن لكن ليس حين يكون مظللا. تفعيل الزر هو
## ما يظهر عندما تكون في الصفحه الخاصة به او الصفحة التي يؤدي إليها.
define gui.selected_color = '#ffffff'

## اللون الخاص بالزر حين يكون غير قابل للضغط.
define gui.insensitive_color = '#8888887f'

## اللون الذي يتم استعماله لملء الفراغات في اشرطة التمرير. هذا اللون لا يظهر
## فعليا, لكن يتم استعماله عند اعادة تكوين الصور الخاصة باشرطة التمرير.
define gui.muted_color = '#003d51'
define gui.hover_muted_color = '#005b7a'

## اللون الخاص بالنص عند الحوار و في ازرار القائمة الرئيسية.
define gui.text_color = '#ffffff'
define gui.interface_text_color = '#ffffff'


## نوع الخط و حجمه. ############################################################

## نوع الخط المستخدم داخل نص اللعبة.
define gui.text_font = "DejaVuSans.ttf"

## نوع الخط المستخدم في أسماء الشخصيات.
define gui.name_text_font = "DejaVuSans.ttf"

## نوع الخط المستخدم في النصوص خارج الحوار في اللعبة.
define gui.interface_text_font = "DejaVuSans.ttf"

## حجم الخط المستخدم في الحوار.
define gui.text_size = 33

## حجم الخط المستخدم لأسماء الشخصيات.
define gui.name_text_size = 45

## حجم الخط المستخدم في واجهة اللعبة التشغيلية.
define gui.interface_text_size = 33

## حجم العناوين الرئيسية في واجهة اللعبة التشغيلية.
define gui.label_text_size = 36

## حجم الخط المستخدم في صفحة الملاحظات.
define gui.notify_text_size = 24

## حجم الخط المستخدم لعنوان اللعبة الرئيسي.
define gui.title_text_size = 75


## القائمة الرئيسية و قائمة اللعبة. ############################################

## الصور المستخدمة في القائمة الرئيسية و قوائم اللعبة.
define gui.main_menu_background = "gui/main_menu.png"
define gui.game_menu_background = "gui/game_menu.png"


## الحوار ######################################################################
##
## هذه المتغيرات تقوم بتحديد طريقة عرض الحوار الظاهر على الشاشة سطراً سطراً.

## ارتفاع الصندوق الذي يحتوي على النصوص.
define gui.textbox_height = 278

## مكان صندوق الحوار عموديا على الشاشة. 0.0 يضعه في الأعلى, 0.5 في المنتصف, و
## 1.0 يضع الصندوق في أسفل الشاشة.
define gui.textbox_yalign = 1.0


## مكان الخانة الخاصة بعرض اسم الشخصية و تناسبها مع صندوق الحوار الرئيسي. يمكن
## وضع ارقام تعبر عن عدد البكسلات بينها و بين الجزء العلوي الأيسر من الشاشة, او
## استعمال نسبة مثل 0.5 لوضعها في المنتصف.
define gui.name_xpos = 360
define gui.name_ypos = 0

## هذا يحدد مكان ظهور اسم الشخصية, يمكن ان يكون 0.0 ليقارب اليسار, 0.5 ليكون في
## المنتصف, و 1.0 ليقارب اليمين.
define gui.name_xalign = 0.0

## طول و عرض و ارتفاع الصندوق الذي يحتوي على اسم الشخصية, او None ليتم استعمال
## حجم قياسي.
define gui.namebox_width = None
define gui.namebox_height = None

## حجم الخط الذي يحيط بصندوق اسم الشخصية, الاحجام بالترتيب هي اليسار, الأعلى,
## اليمين, و الأسفل.
define gui.namebox_borders = Borders(5, 5, 5, 5)

## عندما يتم اختيار True سيتم تكرار الخلفية حتى تغطي الصندوق, عند اختيار False
## سيتم تمديد الصورة لتغطي الصندوق.
define gui.namebox_tile = False


## مكان نص الحوار و تناسبه مع صندوق الحوار الرئيسي. يمكن وضع ارقام تعبر عن عدد
## البكسلات بينها و بين الجزء العلوي الأيسر من الشاشة, او استعمال نسبة مثل 0.5
## لوضعه في المنتصف.
define gui.dialogue_xpos = 402
define gui.dialogue_ypos = 75

## عدد البكسلات القصوى التي يمكن ان يتمدد إليها صندوق الحوار بالعرض.
define gui.dialogue_width = 1116

## اتجاه النص عرضياً: يمكن استعمال 0.0 ليقارب اليسار, 0.5 ليكون في المنتصف, و
## 1.0 ليقارب اليمين.
define gui.dialogue_text_xalign = 0.0


## أزرار #######################################################################
##
## هذه المتغيرات تتشارك مع ملفات الصور في gui/button في تحديد مظهر الأزرار.

## طول و عرض الزر بالبكسل. لو تم استعمال None سيقوم رينباي باختيار حجم مناسب.
define gui.button_width = None
define gui.button_height = None

## حجم الخط الذي يحيط بصندوق الزر, الاحجام بالترتيب هي اليسار, الأعلى, اليمين, و
## الأسفل.
define gui.button_borders = Borders(6, 6, 6, 6)

## عندما يتم اختيار True سيتم تكرار الخلفية حتى تغطي المساحه بأكملها, عند اختيار
## False سيتم تمديد الصورة.
define gui.button_tile = False

## الخط المستخدم في الزر.
define gui.button_text_font = gui.interface_text_font

## حجم الخط المستخدم في الزر.
define gui.button_text_size = gui.interface_text_size

## The color of button text in various states.
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

## The horizontal alignment of the button text. (0.0 is left, 0.5 is center, 1.0
## is right).
define gui.button_text_xalign = 0.0


## هذه المتغيرات تقوم بتجاهل الخيارات التي تنطبق على انواع الازرار الأخرى.
## الرجاء قراءة دليل المستخدم الخاص بالواجهة للتعرف على انواع الازرار المتاحه و
## كيفية استعمالها.
##
## هذه الخيارات تنطبق على الواجهة القياسية:

define gui.radio_button_borders = Borders(27, 6, 6, 6)

define gui.check_button_borders = Borders(27, 6, 6, 6)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(15, 6, 15, 6)

define gui.quick_button_borders = Borders(15, 6, 15, 0)
define gui.quick_button_text_size = 21
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

## يمكنك اضافة تغييرات يدويا عن طريق اضافة متغيرات بأسماء مميزة. مثلا, يمكنك
## ازالة اقتباسات الحماية ## عن السطر التالي لتغيير طول و عرض الازرار الخاصة
## بالقائمة.

# define gui.navigation_button_width = 250


## أزرار الخيارات ##############################################################
##
## أزرار الخيارات يتم استعمالها داخل قوائم اللعبة.

define gui.choice_button_width = 1185
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(150, 8, 150, 8)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = '#888888'
define gui.choice_button_text_hover_color = "#ffffff"
define gui.choice_button_text_insensitive_color = '#8888887f'


## أزرار قائمة الحفظ. ##########################################################
##
## زر خانة الحفظ هو زر مميز عن غيره لانه يعرض صورة رمزية و نص يشرح محتويات
## الخانة. زر الحفظ يستعمل صور من مجلد الواجهة مثل باقي الأزرار في gui/button.

## زر خانة الحفظ.
define gui.slot_button_width = 414
define gui.slot_button_height = 309
define gui.slot_button_borders = Borders(15, 15, 15, 15)
define gui.slot_button_text_size = 21
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

## طول و عرض الصورة الرمزية لخانة الحفظ.
define config.thumbnail_width = 384
define config.thumbnail_height = 216

## عدد الخانات الطولية و العرضية التي يمكن الحفظ فيها.
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2


## مكان الخانات و المساحه بينها. ###############################################
##
## هذه المتغيرات تحدد المساحة و مكان عرض عدة عناصر خاصة بالواجهة.

## مكان الجزء الأيسر من ازرار القوائم وتناسبه مع الحد الأيسر من الشاشة.
define gui.navigation_xpos = 60

## موقع مؤشر استمرار الحوار رأسياً.
define gui.skip_ypos = 15

## موقع شاشة التنبيهات رأسياً.
define gui.notify_ypos = 68

## الفراغات بين خيارات القوائم.
define gui.choice_spacing = 33

## الأزرار في صفحات الخيارات و القائمة الرئيسية.
define gui.navigation_spacing = 6

## يتحكم في المساحه بين الخيارات.
define gui.pref_spacing = 15

## يتحكم في المساحه بين ازرار الخيارات.
define gui.pref_button_spacing = 0

## المساحه بين ازرار صفحات الحفظ.
define gui.page_spacing = 0

## المساحه بين خانات الحفظ.
define gui.slot_spacing = 15

## The position of the main menu text.
define gui.main_menu_text_xalign = 1.0


## الإطارات ####################################################################
##
## هذه المتغيرات تحدد شكل الإطارات الخاصة بعناصر الواجهة عند انعدام نافذة تتحكم
## بظهورها.

## Generic frames.
define gui.frame_borders = Borders(6, 6, 6, 6)

## الإطار الخاص بصفحة التأكيد.
define gui.confirm_frame_borders = Borders(60, 60, 60, 60)

## الإطار المستخدم في صفحة التسريع.
define gui.skip_frame_borders = Borders(24, 8, 75, 8)

## الإطار المستخدم في صفحة التنبيهات.
define gui.notify_frame_borders = Borders(24, 8, 60, 8)

## هل تريد ان تكون خلفية الإطار متكررة؟
define gui.frame_tile = False


## أشرطة التمرير, الأشرطة, و العناصر المنزلقة. #################################
##
## هذه تتحكم بشكل و حجم الأشرطة والعناصر المنزلقة.
##
## The default GUI only uses sliders and vertical scrollbars. All of the other
## bars are only used in creator-written screens.

## ارتفاع الأشرطة و العناصر المنزلقة الأفقية. سماكة الأشرطة و العناصر المنزلقة
## الرأسية.
define gui.bar_size = 38
define gui.scrollbar_size = 18
define gui.slider_size = 38

## استعمل True لتكون الصورة المستخدمة في الأشرطة المنزلقة متكررة, False ليتم
## تمديدها على حجم الشريط.
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

## الحاشية بالعرض.
define gui.bar_borders = Borders(6, 6, 6, 6)
define gui.scrollbar_borders = Borders(6, 6, 6, 6)
define gui.slider_borders = Borders(6, 6, 6, 6)

## الحاضية بالطول.
define gui.vbar_borders = Borders(6, 6, 6, 6)
define gui.vscrollbar_borders = Borders(6, 6, 6, 6)
define gui.vslider_borders = Borders(6, 6, 6, 6)

## What to do with unscrollable scrollbars in the game menu. "hide" hides them,
## while None shows them.
define gui.unscrollable = "hide"


## الحوار السابق ###############################################################
##
## صفحة الحوار السابق تعرض الحوارات التي سبق للاعب قرائتها.

## عدد فقاعات الحوار التي سيحتفظ بها رينباي في صفحة الحوار السابق.
define config.history_length = 250

## ارتفاع صفحة عرض الحوار السابق, او None ليكون الإرتفاع متغير مع ملاحظة انه
## يؤثر في الأداء العام.
define gui.history_height = 210

## Additional space to add between history screen entries.
define gui.history_spacing = 0

## الموقع, العرض, و اتجاه النص الخاص باسم الشخصية المعروض.
define gui.history_name_xpos = 233
define gui.history_name_ypos = 0
define gui.history_name_width = 233
define gui.history_name_xalign = 1.0

## الموقع, العرض و اتجاه النص الخاص بالحوار المعروض.
define gui.history_text_xpos = 255
define gui.history_text_ypos = 3
define gui.history_text_width = 1110
define gui.history_text_xalign = 0.0


## NVL-Mode أسلوب عرض الحوار الروائي. ##########################################
##
## شاشة عرض الأسلوب الروائي تعرض ما قالته شخصيات تم تخصيصها للحوار الروائي.

## حاشية الخلفية المستخدمة في نافذة الحوار الخاصة بالحوار الروائي.
define gui.nvl_borders = Borders(0, 15, 0, 30)

## The maximum number of NVL-mode entries Ren'Py will display. When more entries
## than this are to be show, the oldest entry will be removed.
define gui.nvl_list_length = 6

## إرتفاع النافذة الخاصة بعرض الحوار الروائي. استعمل None لتناسب النافذة الحوار
## المعروض لكل فقاعه حوار.
define gui.nvl_height = 173

## المساحه بين العناصر عندما يكون النظام الروائي يستعمل متغير None في سطر
## gui.nvl_height و المساحه بين اجزاء الحوار والقائمة في الحوار الروائي.
define gui.nvl_spacing = 15

## الموقع, العرض, و اتجاه النص الخاص باسم الشخصية المعروض.
define gui.nvl_name_xpos = 645
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 225
define gui.nvl_name_xalign = 1.0

## الموقع, العرض و اتجاه النص الخاص بالحوار المعروض.
define gui.nvl_text_xpos = 675
define gui.nvl_text_ypos = 12
define gui.nvl_text_width = 885
define gui.nvl_text_xalign = 0.0

## موقع, عرض و اتجاه النص الخاص بشخصية التفكير nvl_thought, الحوار المنطوق من
## قبل شخصية nvl_narrator تم تحديدها في ملف حوار اللعبة.
define gui.nvl_thought_xpos = 360
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 1170
define gui.nvl_thought_xalign = 0.0

## موقع ازرار القائمة في nvl menu_buttons.
define gui.nvl_button_xpos = 675
define gui.nvl_button_xalign = 0.0


## Localization ################################################################

## This controls where a line break is permitted. The default is suitable
## for most languages. A list of available values can be found at https://
## www.renpy.org/doc/html/style_properties.html#style-property-language

define gui.language = "unicode"


################################################################################
## Mobile devices
################################################################################

init python:

    ## يقوم بتكبير المساحه الخاصة بازرار الاختصارات ليكون استعمالها اسهل على
    ## شاشات الاجهزة المحمولة و التابلت.
    @gui.variant
    def touch():

        gui.quick_button_borders = Borders(60, 21, 60, 0)

    ## يقوم بتغيير المساحات بين العناصر في اماكن مختلفة من الواجهة لتكون اسهل في
    ## الرؤية و الاستعمال على شاشات المحمول و التابلت.
    @gui.variant
    def small():

        ## حجم النص.
        gui.text_size = 45
        gui.name_text_size = 54
        gui.notify_text_size = 38
        gui.interface_text_size = 45
        gui.button_text_size = 45
        gui.label_text_size = 51

        ## تحديد مكان مربع الحوار.
        gui.textbox_height = 360
        gui.name_xpos = 120
        gui.dialogue_xpos = 135
        gui.dialogue_width = 1650

        ## Change the size and spacing of various things.
        gui.slider_size = 54

        gui.choice_button_width = 1860
        gui.choice_button_text_size = 45

        gui.navigation_spacing = 30
        gui.pref_button_spacing = 15

        gui.history_height = 285
        gui.history_text_width = 1035

        gui.quick_button_text_size = 30

        ## ترتيب ازرار الملفات.
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2

        ## NVL-mode نظام الحوار الروائي.
        gui.nvl_height = 255

        gui.nvl_name_width = 458
        gui.nvl_name_xpos = 488

        gui.nvl_text_width = 1373
        gui.nvl_text_xpos = 518
        gui.nvl_text_ypos = 8

        gui.nvl_thought_width = 1860
        gui.nvl_thought_xpos = 30

        gui.nvl_button_width = 1860
        gui.nvl_button_xpos = 30
