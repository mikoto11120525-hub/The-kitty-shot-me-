define quick_dissolve = Dissolve(0.2)   # 0.2 秒，快淡出入

# 角色定義區域 (可放在 script.rpy 開頭)

define s = Character("朔真",what_slow_cps=15,color="#1824cf")
define t = Character("時嶺",what_slow_cps=15,color="#671aa2")
define n = Character("貓貓",what_slow_cps=15,color="#898989")
define k = Character("健",what_slow_cps=15,color="#fdd464")
define h = Character("穗乃香",what_slow_cps=15,color="#f48eab")

# define r = Character(".",what_slow_cps=15,color="#971a1a") {colar=#971a1a}
# define b = Character(" ",what_slow_cps=15,color="#0d158c")
# define g = Character(" ",what_slow_cps=15,color="#671aa2")
# define p = Character(" ",what_slow_cps=15,color="#f48eab")
# define q = Character(" ",what_slow_cps=15,color="#898989")
# define bl = Character(" ",what_slow_cps=15,color="#5b5252")

# 全篇均速打字
init python:
    preferences.text_cps = 22

default qwq = 0      # 崩潰指數（逃家、自殘的條件）
default agg = 0      # 憤怒指數（報復、隱藏線結局）
default toki = 0
default ccc = 0     # 哥哥指數（全滿隱藏線條件）

init python:
    renpy.music.register_channel(
        "sound2",
        mixer="sfx",
        loop=False
    )
##################################################################################################################
##################################################################################################################

image an01:
    "an01_1.png"
    0.1
    "an01_2.png"
    0.1
    "an01_3.png"
    0.1
    "an01_4.png"
    0.1
    "an01_5.png"
    0.1
    repeat

image anbk05:
    "bk05_1.png"
    0.1
    "bk05_2.png"
    0.1
    "bk05_3.png"
    0.1
    "bk05_2.png"
    0.1
    repeat

image an02:
    "an02_1.png"
    0.1
    "an02_2.png"
    0.1
    "an02_3.png"
    0.1
    "an02_2.png"
    0.1
    repeat

image an03:
    "bk01.jpg" with dissolve
    1.5
    "cg01.jpg" with dissolve
    1.5
    "cg02.jpg" with dissolve
    1.5
    "bk02.jpg" with dissolve

image an04:
    "an04-1.png" 
    0.125
    "an04-2.png" 
    0.125
    "an04-3.png" 
    0.125
    "an04-2.png"
    repeat

image an05:
    "an05-1.png" 
    0.125
    "an05-2.png" 
    0.125
    "an05-3.png" 
    0.125
    "an05-4.png" 
    0.125
    "an05-3.png" 
    0.125
    "an04-2.png"
    repeat

image ed00:
    "ed00-1.png" 
    0.2
    "ed00-2.png" 
    0.2
    repeat

image ed11:
    "ed011-1.png" 
    0.2
    "ed011-2.png" 
    0.2
    repeat

image ed12:
    "ed012-1.png" 
    0.2
    "ed012-2.png" 
    0.2
    repeat

##################################################################################################################
##################################################################################################################

###Ren'py筆記

##快速鍵:
#shift+R==刷新遊戲，不須關視窗就能馬上測試更動
#ctrl+s==儲存>>>超重要，定時按
#ctrl+k+c==註解選取文字
#ctrl+?==取消選取的註解
#ctrl+z==撤回
#ctrl+a==全選

##當你不消新按到:
#shift+空白==切回正常行距
#caps Lock==全大寫切回
#Insert==奇怪的反消除空格切回

##前置作業:
#不要相信AI>>叫他格式化都不一定正確了，設定更動更不能信，都是幻覺
#檔案規則:人物立繪>>人名 表情(png，記得刪背景圖層)//背景:性質 名稱(jpg，仔細看看畫布大小)//音樂:名稱(mp3 or ogg)
#叫立繪規則:立繪:show ...(人名 表情) at ... with ...(at跟with視情況，都要的話with要在下一行)，如果喜歡漸變則需善用hide)
#最低辯視率用的半身大小為高600上下，建議框高625，角色612，寬不限定，不要太扯就好
#辯視率不合不准直接放大(縮小可以)
#screen設定的圖片更動請直接開資料夾，塞入檔案偷原版圖片的檔案名字用

##程式撰寫注意:
#menu並行label，選項tab，選項後的指令tab，記得jump後面沒有to
#暗幕、角色消失、停止音樂要在jump之前
#menu接menu的無意義選項，第二個選擇的前導敘述記得並行menu
#show是圖層上疊//scene是清空後展露>>多數用show就好，善用black

##################################################################################################################
##################################################################################################################

#聲音注意:
#檔案可以是中文
#play music==背景音//play sound==不會卡掉背景音的音效
#music會循環//sound不會，但會播完才停，需截斷請善用stop
#MP3不能卡秒，OGG可以>>start=12*從第十二秒開始撥
#sound +loop==持續撥放

#複製格式:
#play music "audio/music/.mp3"
#play music "audio/sound/.mp3"
#play sound "audio/music/.mp3"
#play sound "audio/sound/.mp3"
#stop music fadeout 3.0
#變數注意:
#$千萬要記得
#讓選項有變數開啟條件>>"我是選項" if qwq >=3

#格式:
# $ qwq += 1
# $ agg += 2
# $ toki = 5

#螢幕特效:
#dissolve>>淡出
#vpunch>>垂直震動
#hpunch>>水平震動

#結局:
#centered "">>文字在正中央

##################################################################################################################
##################################################################################################################

label start:
label l:

$ qwq += 0
$ agg += 0
$ toki = 0
play music "audio/sound/走廊風聲.mp3" 
scene black with dissolve
scene bk01 with dissolve


"走廊空蕩蕩，牆上的燈閃了又滅"

"聽不見腳步聲，只聽得見自己的心跳聲"

"好像整個人都被吸進了這條走廊裡"

"這裡的空間彷彿被無限延伸，但我本能地知道該往哪裡去"

"懷著不知從何而生的罪惡感，順著某種不知是否存在的命令，往末端的房間"

"牆壁上斑駁的痕跡像是在指引我，空氣逐漸變得黏稠"

"我沒有試圖逃離這種詭異的單色調，只是目標明確地前行"

scene black with dissolve
show cg01 with dissolve
"那是一扇表面平滑的詭異的木門"

menu :
    "進門":
        play sound "audio/sound/按鍵音效.mp3"
        show cg02 with dissolve

play sound "audio/sound/開門.mp3"
"……"

stop sound
scene black with dissolve
scene bk02 with dissolve

play music "audio/sound/雷聲.mp3"
"房間很安靜，只有窗外傳來雷鳴聲"

"一具黑色的、毛茸茸的生物注意到我"

show neko at center with dissolve
"面對我的闖入，他卻仍然從容不迫，緩緩地轉過來面對我"

"牠睜著兩顆圓圓黑黑的眼睛，毫無感情"

"對方是一隻卡通角色的貓貓"

"總覺得似曾相識……一種難以描述的熟悉感"

hide neko with dissolve
show sakuma at center with dissolve
"……"

hide sakuma
show neko at center with dissolve
"……"

hide neko with dissolve
"我們沉默地對視著"

"直到我隱隱約約感覺到對方的怒火……"

"我才想起來自己的目的——"

scene black with dissolve
"我該道歉"

scene bk02 with dissolve
show sakuma at center with dissolve

"但喉嚨像被堵住，像有什麼東西從胃裡往上湧，卻卡在胸口"

"我張了張嘴——"

show sakuma sc at center with dissolve
s "……"

"但我發不出聲音"

hide sakuma 
"沉默僵持了很久、很久"

"我能感受到他的怒氣值在持續飆高"

"但我依舊發不出聲音"

show neko at center with dissolve  #直視
n "……"

show neko d at center with dissolve  #低頭
n "……"

play sound "audio/sound/上膛.mp3"
show neko g at center with dissolve  #槍
n "……"

hide neko with dissolve
show sakuma at center with dissolve
s "啊……慘了"

play sound "audio/sound/腳步停下.mp3"
hide sakuma 
stop music fadeout 3.0
"我本能地退了一步，但沒來的及逃離這裡"

scene black with vpunch
play sound "audio/sound/開槍.mp3"
"「碰！」"

jump ll

##################################################################################################################
##################################################################################################################

label ll:

scene black with dissolve
centered "早晨 - 朔真房間"
centered "章節：開端"
play sound "audio/sound/鬧鐘.mp3"
"醒來的時候，窗外天氣很好"

stop sound
scene bk03 with dissolve
"但有股不真實感"

"也許是因為方才的夢，心底還殘存被射殺的恐懼"

show sakuma with dissolve
s "（又夢到了……）"

show sakuma l with dissolve
s "（算了，無所謂……）"
hide sakuma

"發呆片刻，然後起身換衣"

"開啟再平常不過的一日"

########################################################

scene black with dissolve
centered "早晨 - 飯廳 "
show cg03-1 with dissolve

play music "audio/music/早餐.mp3"
"貓貓今天也買了我最喜歡的早餐"

play sound "audio/sound/放東西到桌上.mp3"
"是街口那間早餐店的培根蛋起司可頌"

show cg04 with dissolve
"熱氣帶著起司味，被紙袋裹著"
scene cg03-1 with dissolve
"妹妹坐在桌邊，撥弄那個三明治"

play sound "audio/sound/.mp3"
h "怎麼又吃這家早餐！！有完沒完啊啊！！"

"她發出明顯的不滿聲，卻還是在貓貓的沉默注視下任命地咬下一口"

show cg03 with dissolve
"貓貓坐在妹妹隔壁，安靜地啃早餐，只在妹妹連篇的聊天中偶爾點頭表示「我有在聽」"

"而哥哥吃飯速度很快，像是怕食物會融化掉一樣"

"他從頭到尾都沒說話，目光偶爾掃過貓貓"

show cg04 with dissolve
"我坐下來，盯著那個可頌看"

"（朔真的行動？）"

menu:
    "吃可頌":
        play sound "audio/sound/按鍵音效.mp3"
        scene black with dissolve
        jump eat
        

    "把可頌丟掉":
        play sound "audio/sound/按鍵音效.mp3"
        $ agg += 2
        scene black with dissolve
        jump throw

##################################################################################################################
##################################################################################################################

label eat:

    play sound "audio/sound/刀戳.mp3"
    show cg04 with dissolve
    "我低頭咬了一口，同時注意到貓貓的視線"

    show cg03-1 with dissolve
    n "……"

    s "……"
    
    "我們對視的一瞬間，迅速撇開視線"

    "食物的味道沒變，但是因為連吃不知道多久了，我感到有點反胃"

    show cg03-2 with dissolve   
    "不久，哥哥吃完，推開椅子，起身要走"

    "離開前，他又撇了貓貓一眼，嘆了口氣，靠近我耳邊低聲說——"

    show cg03-2 with dissolve   ##補
    show tokimine with dissolve
    t "膩了就直接說，我在旁邊看了都覺得想吐？"

    show tokimine sd with dissolve
    t "沒記錯的話……你可頌快吃滿兩年了吧？還是更久？"

    show tokimine with dissolve
    t "是有什麼破病啊？就這麼不想跟××說話？"

    t "固執也該有個限度吧……"
    hide tokimine

    show sakuma with dissolve
    s "……"
    hide sakuma

    show tokimine sd with dissolve
    t "而且你也可以告訴我，我能幫你轉達，雖然這樣很智障就是了……"

    show tokimine s with dissolve
    t "看在你是叛逆期的麻煩小鬼份上可以勉強幫忙"
    hide tokimine

    show sakuma d with dissolve
    s "……"
    hide sakuma

    show tokimine sd with dissolve
    t"嘖……"
    show tokimine a with dissolve
    t"他媽的別又沉默啊……"
 
    show tokimine sd with dissolve
    t"算了"
    t"活該吃到吐吧，再見"
    hide tokimine
    
    "哥哥離開後，妹妹一邊吃飯一邊繼續跟貓貓抱怨生活破事"

    stop music fadeout 3.0
    "我繼續咬下令人反胃的早餐"

    "窗外陽光很亮很刺眼，但我沒什麼感覺"

    jump lll

##################################################################################################################
##################################################################################################################

label throw:

    show cg03 with dissolve
    "我思緒停滯了半秒"

    "隨後順著潛意識做出了連自己都訝異的舉動——"

    stop music
    play sound "audio/sound/丟垃圾桶.mp3"
    "……！"

    "早餐進了垃圾桶"
    
    stop sound
    "飯桌上其餘三人因為我的行為愣住了"

    show cg03-2 with dissolve ##補:cg03-2-1
    "哥哥嘆了口氣，帶著還沒吃完的早餐離開了"

    "妹妹則是一副看戲的表情，混雜著不屑與指責"

    "貓貓表情依然不變，但牠愣在原地，遲遲沒有下一個動作"

    "我低頭看著垃圾桶裡的可頌，感覺有些違和正在發酵，心情卻異常平靜"

    show cg03-2 with dissolve
    show sakuma with dissolve
    s "（出門吧……）"

    scene black with dissolve
    play sound "audio/sound/開門.mp3"
    s "（……）"

    jump lll

##################################################################################################################
##################################################################################################################


label lll:

stop sound
scene black with dissolve
centered "上午 - 教室"
centered "章節：小確幸"
show cg05 with dissolve
play music "audio/sound/風吹落葉.mp3" volume 5
"課堂很無聊，我把頭靠在窗邊"

"外面的風撩起葉片發出輕響"

"某處枝椏，一隻翅膀似乎有些受傷的鳥正揮動翅膀"

play sound "audio/sound/翻頁.mp3"
"傷不算重，但足以讓動作一卡一卡"


show cg05-1 with dissolve
"但牠似乎並不畏懼，毅然決然地起飛"

show cg05-3 with dissolve
"可惜失敗了"

show cg05-4 with dissolve
"墜落"

"下落過程中牠的翅膀還在抖動嘗試掙扎"

scene black with dissolve
"但依舊沒能挽回"

play sound "audio/sound/採屍體.mp3"
show cg05-5 with dissolve
"著地瞬間落下輕響"

stop sound fadeout 3.0
"幾乎沒人注意到"

s "……"

######################################

scene black with dissolve
centered "下課 - 中庭"
play music "audio/sound/交談聲.mp3"

"下課鐘聲響了，人群湧出教室"

play sound "audio/sound/腳步聲.mp3"
"我跑下樓梯，衝到中庭"

#再加個模糊畫面
show cg06 with dissolve

play sound "audio/sound/腳步停下.mp3"
"地上靜靜躺著那隻還存著溫度的鳥屍體，羽毛凌亂，眼睛閉著像睡著了"

"我站在旁邊，看了很久、很久"

"很久、很久……"

s "（放到下午的話書包會臭掉……）"

s "（真可惜……）"

s "……"

"（朔真的行動？）"

menu:
    "埋葬屍體":
        play sound "audio/sound/按鍵音效.mp3"
        scene black with dissolve
        jump bury_bird

    "什麼都不做":
        play sound "audio/sound/按鍵音效.mp3"
        $ qwq += 1
        scene black with dissolve
        jump ignore_bird

    "踩屍體":
        play sound "audio/sound/按鍵音效.mp3"
        $ agg += 2
        scene black with dissolve
        jump stomp_bird


##################################################################################################################
##################################################################################################################

label bury_bird:

    
    "我蹲下，捧起屍體，順了順羽毛"

    play sound "audio/sound/腳步停下.mp3"
    "我在學校後面的花圃挖了一個小洞，指縫因此卡了些泥土"

    play sound "audio/sound/踩雪.mp3"
    "我把鳥放進洞裡"

    play sound "audio/sound/踩雪.mp3"
    show cg06-1-1 with dissolve
    "蓋上土"

    play sound "audio/sound/踩雪.mp3"
    show cg06-1-2 with dissolve
    " "
    play sound "audio/sound/踩雪.mp3"
    show cg06-1-3 with dissolve
    "壓實"

    "表面上看起來就像什麼都沒有發生過"

    play sound "audio/sound/鐘聲.mp3"
    s "……"
    
    play sound "audio/sound/腳步停下.mp3"
    "鐘響了，我離開現場"

    scene black with dissolve

    jump llll

##################################################################################################################
##################################################################################################################

label ignore_bird:

    show cg06 with dissolve
    "我靜靜地觀察著染血的羽毛"

    "別人的笑聲從走廊傳到我耳邊"

    "沒有什麼特別的想法，純粹因為看著讓我感到平靜"

    play sound "audio/sound/鐘聲.mp3"
    play sound2 "audio/sound/腳步停下.mp3"
    "直到上課鐘聲，我轉身回教室"

    scene black with dissolve

    #####################################

    stop music
    play sound "audio/sound/風吹落葉.mp3"
    show cg05-5 with dissolve
    "窗外的樹影一樣搖晃"

    "剛剛發生的一切無足輕重"

    "視線落回書面——"

    "但一個字都讀不進去"

    scene black with dissolve
    "有股說不上來的違和感，可我沒有頭緒"

    jump llll

##################################################################################################################
##################################################################################################################

label stomp_bird:

    show cg06 with dissolve
    "我死死地盯著牠"

    "心底升起的衝動越發難以抑制"

    play sound "audio/sound/抬腳.mp3"
    "於是抬腳——"

    show cg06-2 with dissolve
    play sound "audio/sound/踩屍體.mp3"
    stop music
    "然後落下"

    s "……"
    
    "在這一刻，我感覺世界終於安靜下來"

    "心情也隨之安定"

    s "（沒能帶回去很可惜，不過這樣也不錯……）"

    play sound "audio/sound/鐘聲.mp3"
    show cg06-2-1 with dissolve
    "鐘響了，我停下輾踏的動作"

    scene black with dissolve
    play sound "audio/sound/刀戳.mp3"
    "將鳥屍體踢到花圃後，心滿意足地回到教室"

    jump llll

##################################################################################################################
##################################################################################################################

label llll: 

scene black with dissolve
centered "中午 - 教室"
centered "章節：轉折"

show bk06 with dissolve
play music "audio/music/飯廳.mp3"
play sound "audio/sound/交談聲.mp3"
play sound2 "audio/sound/放東西到桌上.mp3"
"教室裡人聲嘈雜，便當盒一個接一個被打開"

"筷子在空中交錯，笑聲此起彼落"

play sound2 "audio/sound/按鍵聲.mp3"
"我和健坐在角落靠窗的位置，陽光正好照在桌上"

"健的便當總是五顏六色，看起來像是亂搭一通，但聽說意外地好吃"

play sound2 "audio/sound/放東西到桌上.mp3"
"他邊吃邊講話，表情誇張，像在演一齣獨角戲"

show bk06-1 with dissolve

show ken with dissolve
k "我跟你講，那個社團的學姐超可怕，我昨天碰巧路過他們班、莫名被搭話，然後還突然開始跟我翻舊帳欸"


show ken n with dissolve
k "還說什麼「你上學期說要幫忙的記得嗎？」……靠北喔誰記得啦"
hide ken

show sakuma d with dissolve
s "……"
hide sakuma

show bk06 with dissolve
hide bk06-1 with dissolve
"我咬著飯糰，撇了他一眼，而後繼續低頭吃"

"健似乎不在意，自顧自地繼續說"

"教室的吵雜幾乎蓋掉一切，連同樹葉的聲響與揮之不去的耳鳴都變得無足輕重"

"剛剛的那個畫面讓我時不時發呆，心底被挑起陣陣漣漪"

"健喝了口飲料，突然轉頭看我"

show bk06-1 with dissolve
hide bk06 with dissolve
show ken with dissolve
k "你今天看起來比較有溫度耶，是不是終於考慮轉生成人類了"
hide ken

show sakuma with dissolve
s "或許吧……"
hide sakuma

show ken h with dissolve
k "這次沒有無視我耶！！超難得！！！"

show ken with dissolve
k "給你87分不能再更高！！"
hide ken

show bk06 with dissolve
play sound2 "audio/sound/放東西到桌上.mp3"
"他拿出手機，開始刷某個梗圖帳號，一邊把手機翻給我看"

"我盯著圖片又一次思緒發散"

"今天一直感覺奇怪地平靜，像是漂浮在水面上的那種靜，連心跳聲都好像被包住了"

"梗圖的笑點我不太明白，但健好像很期待我給出反應"

"（朔真的回覆？）"

menu:
    "這笑話的水準跟你穿搭的品味一樣糟糕":
        play sound "audio/sound/按鍵音效.mp3"
        scene black with dissolve
        jump opt_insult

    "好笑（無感情）":
        play sound "audio/sound/按鍵音效.mp3"
        scene black with dissolve
        jump opt_plain

    "……（不理他繼續吃飯）":
        play sound "audio/sound/按鍵音效.mp3"
        $ qwq += 1
        $ agg += 1
        scene black with dissolve
        jump opt_silent

##################################################################################################################
##################################################################################################################

label opt_insult:

    show bk06-1 with dissolve
    show sakuma d with dissolve
    s "這笑話的水準跟你穿搭的品味一樣糟糕"
    hide sakuma

    show ken h with dissolve
    k "你又好到哪裡去了北七？還好意思說我？？"
    hide ken

    show bk06 with dissolve
    "他嗆完我後繼續刷手機"

    stop music fadeout 3.0
    stop sound fadeout 3.0
    "我則是低頭，繼續吃飯糰"

    scene black with dissolve
    jump lllll

##################################################################################################################
##################################################################################################################

label opt_plain:

    show bk06-1 with dissolve
    show ken with dissolve
    k "靠北喔……"
    hide ken

    show sakuma with dissolve
    s "我是認真的"
    hide sakuma

    show ken h with dissolve
    k "看來你轉生失敗了，沒有成為人類的天賦"
    hide ken

    show sakuma d with dissolve
    s "……"
    hide sakuma

    show ken h with dissolve
    k "臭人機快去安裝感情模組啊！！"
    hide ken

    show bk06 with dissolve
    "他嗆完我後繼續刷手機"

    stop sound fadeout 3.0
    stop music fadeout 3.0
    "我則是低頭，繼續吃飯糰"

    scene black with dissolve
    jump lllll

##################################################################################################################
##################################################################################################################

label opt_silent:

    stop music
    show bk06-1 with dissolve
    show ken m with dissolve
    k "……"
    hide ken

    play music "audio/music/sorrowful-documentary-music-425313.mp3"
    show ken a with dissolve
    k "才剛稱讚完你，又開始無視"
  
    k "……"

    show ken m with dissolve
    k "這麼不想聽我講話嗎？"

    show ken a with dissolve
    k "或者說……"

    show ken m with dissolve
    k "其實你一直以來根本都不想搭理我？"
    hide ken

    show sakuma with dissolve
    s "……"

    show sakuma d with dissolve
    s "（要回答什麼……？）"
    hide sakuma

    show ken a with dissolve
    k "……算了"
    hide ken

    show sakuma with dissolve
    s "對不起"
    hide sakuma

    show ken a with dissolve
    k "……"

    k "我說「算了」"
    hide ken

    show bk06 with dissolve
    "他嗆完我後繼續刷手機"

    stop music fadeout 3.0
    "我則是低頭，繼續吃飯糰"

    stop sound fadeout 3.0
    scene black with dissolve
    jump lllll

##################################################################################################################
##################################################################################################################

label lllll:   #5

scene black with dissolve
centered "下午 - 家"
centered "章節：相處"

play sound "audio/sound/開門.mp3"
play music "audio/music/kioku-tadoru-senritsu.mp3"
show bk09 with dissolve
"經過熟悉而空乏的一天，又回到那個「家」"

stop sound
play sound2 "audio/sound/腳步停下.mp3"
"在玄關拖鞋時，我注意到褲腳沾著泥巴，膝蓋處也擦破了一點"

"客廳的燈亮著，有個人影注意到我，拖著略顯頹廢的姿勢走近"

play sound2 "audio/sound/腳步停下.mp3"
show tokimine with dissolve
t "太晚了……你是不是又跑到後山？"
hide tokimine

"我沒回答，只是繼續動作"

"拍了拍鞋上的塵土後收回櫃中"

show tokimine sd with dissolve
t "……"
hide tokimine

"哥哥看了看我，又嘆了一口氣，像是早已習慣這樣的冷淡"

show tokimine sd with dissolve
t "算了，洗洗手去吃飯……"

play sound "audio/sound/抬腳.mp3"
show tokimine a with dissolve
t "還有……別什麼都憋著不說"

t "我姑且還是會擔……"

show tokimine with dissolve
t "……"

show tokimine sd with dissolve
t "算了，當我沒說……"

"（朔真的回覆？）"

menu:
    "……(沉默)":
        play sound "audio/sound/按鍵音效.mp3"
        $ agg += 1
        $ qwq += 1
        show tokimine with dissolve
        t "……"
        hide tokimine
        
        stop music fadeout 3.0
        play sound "audio/sound/腳步停下.mp3"
        "哥哥又嘆了一口氣，然後轉身離開"
    
    "我知道了，謝謝你…":
        play sound "audio/sound/按鍵音效.mp3"
        $ toki += 1
        
        stop music 
        s "嗯，謝謝……"

        show tokimine sp with dissolve
        t "……"
        hide tokimine

        "哥哥的反應先是訝異，而後是裝作抱怨的語氣"

        show tokimine n with dissolve
        t "別廢話了，快去洗手"

        play sound "audio/music/game-over1.mp3"
        show tokimine s with dissolve
        t "話說……今天××親自下廚，戰況慘烈"
        hide tokimine

        "哥哥說著，臉上不自覺浮現淡淡的微笑"

        show tokimine ss with dissolve
        t "吃太多小心拉肚子"

        show tokimine s with dissolve
        t "晚點再一起出去吃消夜吧"
        hide tokimine

        stop music fadeout 3.0
        show sakuma with dissolve
        s"好……"
        hide sakuma


########################################################################################

scene black with dissolve
play sound "audio/sound/水龍頭.mp3"
show cg10 with dissolve

play music "audio/music/zureru-kuukan.mp3"
"我走進浴室，水沖過傷口，有點痛，但又好像沒什麼實感"

"冰冷的觸感讓煩燥短暫被抹滅，我得以靜下心去復盤這一整天發生的事件"

"沒能帶走的原料、不小心搞丟的末端尾椎、把不知道那個部位的細骨煮裂……"

s "（我今天好像有點心不在焉……）"

s "（又一隻作廢了…真可惜……）"

s "（入冬了會越來越難找吧……）"

s "唉……"

"我甩了甩手上的水珠"

play sound "audio/sound/耳鳴.mp3" loop
show cg10-1 with dissolve
s "欸……？"

#an （循環動畫
hide cg10-1
show an01 with dissolve
"揮之不去耳鳴突然再度響起"

"視線混亂，空間開始變得詭異而扭曲"

s "安靜……"

s "安靜……"

"安靜……安靜……安靜……安靜……安靜……安靜……安靜……安靜……安靜……安靜……安靜……安靜……安靜……安靜……安靜……安靜……安靜……安靜……安靜……安靜……安靜……安靜……"

s "……"

play sound "audio/sound/水龍頭.mp3"
scene bk08 with dissolve

show sakuma sc with dissolve
s "…"

show sakuma with dissolve
s "（啊…回來了……）"

stop music fadeout 3.0
show sakuma with dissolve
s "……"

show sakuma d with dissolve
s "（最近狀況真的挺糟糕的……）"
hide sakuma


##################################################################################################################
##################################################################################################################

label llllll: #6

scene black with dissolve
centered "??? - 走廊"
centered "章節：清醒夢"
show bk01 with dissolve

play music "audio/music/maou_bgm_healing11.mp3" 
"又被拉進熟悉的地方"

"一樣的走廊"
"一樣忽明忽滅的燈光"
"我被困在這個夢境好幾年了"
"有時毫無自覺在作夢、有時像現在這樣意識清楚"

s "（在這個意義不明的劇本重演了多少次了……）"

"我盯著牆上的花紋，片刻便被視覺衝擊的有點眼花"

s "……"

play sound "audio/sound/走步.mp3"
"邁出步伐，空間無腳步聲"
"那股違和感又一次再心底發酵"
"我知道註定的結局，卻沒有選擇迴避"

play sound "audio/sound/開門.mp3"
show cg02 with dissolve
"我走到盡頭，打開那扇門"

scene black with dissolve
centered "??? - 貓貓房間"

stop sound
show bk02-1 with dissolve
"一樣是貓貓的房間"

"唯一不同的是透過窗戶看到的外面天氣不錯"

show neko w with dissolve
"貓貓眼睛如往常一樣死盯著我"

"我感覺他今天似乎有點生氣"

n "……"

stop music fadeout 3.0
show neko ga with dissolve
"他舉起手槍，像往常那樣"

hide neko with dissolve
"（要不要逃跑？）"

#地板血跡
menu:
    
        "不逃跑":
            $ qwq += 2
            play sound "audio/sound/按鍵音效.mp3"
            play music "audio/music/kowareta-waltz.mp3"
            show black with dissolve
            show bk02-1 with dissolve

            show sakuma sc with dissolve
            s "……"
            hide sakuma 

            "雖然不可避免的感到恐懼，腳沒有動"
            "像是早就被編列在基因裡的程式碼"
            "為避免更大傷害而屈服……"

            play sound "audio/sound/開槍.mp3"
            "……"

            play sound "audio/sound/血流.mp3"
            "第一槍打在右大腿"

            play sound "audio/sound/抬腳.mp3"
            show bk02-1-1 with dissolve
            "我重心變得不穩，視線開始晃動"

            play sound "audio/sound/開槍.mp3"
            "第二槍打在左小腿"

            play sound "audio/sound/血流.mp3"
            show bl01 with dissolve
            "我痛到跪地"

            play sound "audio/sound/血散.mp3"
            show bl02 with dissolve
            "血滴在木質的地板上散開"

            play sound "audio/sound/開槍.mp3"
            "接著是腹部"

            play sound "audio/sound/開槍.mp3"
            "再來是手臂"

            play sound "audio/sound/血流.mp3"
            show bk02-1-1 with dissolve
            "世界變得模糊，像是墨被水浸開"

            play sound "audio/sound/低地.mp3"
            "血在淌流，但我痛覺感官漸漸變得遲鈍"

            play sound2 "audio/sound/耳鳴.mp3"
            "只有一股空洞的殘響在耳朵裡嗡嗡作聲"

            play sound "audio/sound/腳步停下.mp3"
            "貓貓慢慢走近" 

            play sound "audio/sound/上膛.mp3"
            "槍口抵在我的額頭上"

            stop music fadeout 3.0
            play sound "audio/sound/抬腳.mp3"
            "我抬起頭，試圖判別他的表情，卻什麼也看不清"

            scene black with dissolve
            play sound "audio/sound/開槍.mp3"
            "碰"

        "逃跑":
            $ agg += 2
            play sound "audio/sound/按鍵音效.mp3"
            play music "audio/music/iwakan.mp3"
            $ qwq += 1
            scene black with dissolve
            show bk01 with dissolve
            play sound "audio/sound/開門.mp3"
            "我瞬間扭頭，奪門而出"

            play sound "audio/sound/喘息.mp3" 
            play sound2 "audio/sound/跑.mp3" loop
            "盡全力的跑著、發了瘋般的跑著"

            "但走廊沒有盡頭"
            "沒有轉彎"
            "沒有能開的門"
            "沒有能逃脫的窗"

            play sound2 "audio/sound/開槍.mp3"
            "碰……"

            play sound "audio/sound/血流.mp3"
            show bk01-1 with dissolve
            "第一槍打在左後腿"

            play sound2 "audio/sound/抬腳.mp3"
            "我失去重心，向前撲倒"

            play sound "audio/sound/踩雪.mp3" 
            "趴在地上試圖撐起身子"

            play sound "audio/sound/腳步停下.mp3" 
            scene bk01 with dissolve
            "但貓貓不知何時已經到達我身後"

            play sound "audio/sound/開槍.mp3"
            "第二槍打在手背"

            play sound2 "audio/sound/奏三.mp3"
            show bk01-1 with dissolve
            "我失去一方的支撐"

            play sound "audio/sound/奏一.mp3"
            "垮下來一瞬間頭部用力的撞擊地面"

            "世界變得再次模糊，只有血漬惹眼得過分"

            play sound "audio/sound/開槍.mp3"
            "貓貓連續開了數槍"

            play sound "audio/sound/開槍.mp3"
            play sound2 "audio/sound/血流.mp3"
            "但都不是能斃命的要害"

            "像在懲罰我的逃避行為"

            play sound2 "audio/sound/血散.mp3"
            "痛覺感官漸漸變得遲鈍"

            play sound2 "audio/sound/耳鳴.mp3"
            "只有一股空洞的殘響在耳朵裡嗡嗡作聲"

            scene black with dissolve
            "貓貓停止了開槍"

            stop music fadeout 3.0
            play sound2 "audio/sound/抬腳.mp3"
            "隨之而來的是失血過量導致的失重感"

##################################################################################################################
##################################################################################################################

label lllllll: #7

scene black with dissolve
centered "中午 - 朔真房間"
centered "章節：關心？"
show bk03 with dissolve

play sound "audio/sound/喘息.mp3"
"我猛然睜眼"
"額頭是濕的汗貼在髮根整個人像剛從水底浮上來"

stop sound
"呼吸急促了一下但我馬上壓下來"

show cg07 with dissolve
play sound "audio/sound/放東西到桌上.mp3"
"轉頭看見床頭櫃上放著一瓶運動飲料旁邊還有退燒藥"

scene black with dissolve
play music "audio/music/退燒藥.mp3"
"貼著便條上面寫著「吃完沒好再看醫生」"

"大概是貓貓放的吧……"

"但我根本沒有發燒也沒感冒"

show bk03 with dissolve
play sound "audio/sound/抬腳.mp3"
"順手把藥收進抽屜然後慢慢坐起身"

"腳落地時還有點發軟"

scene black with dissolve
play sound "audio/sound/開燈開門(哥哥房間.mp3"
show bk08 with dissolve
"我走去廁所洗臉水拍上臉的時候涼涼的感覺讓昏沉被驅散"

"鏡子裡的臉有點蒼白"

"有點模糊"

"不對"

"模糊過頭了"

"這讓我升起一瞬間的恐慌但猛然的揉了揉眼睛後發現只是眼屎"

show sakuma sc with dissolve
s "……"

show sakuma with dissolve
s "幹……"
hide sakuma

scene black with dissolve
show bk09 with dissolve
play sound "audio/sound/開燈開門(哥哥房間.mp3"
"我擦乾水走出廁所時剛好遇見哥哥走出房間"

play sound "audio/sound/腳步停下.mp3"
show tokimine with dissolve
t "你昨晚是不是又睡不好"

show tokimine n with dissolve
t "臉色差到跟屍體沒兩樣，要不要幫你下葬"
hide tokimine with dissolve

show sakuma d with dissolve
s "……"

show sakuma with dissolve
s "不用……"
hide sakuma 

show tokimine a with dissolve
t "我他媽是在關心你"

t "能不能試著解讀一下，然後正面回答我你最近到底怎麼了"
hide tokimine with dissolve

show sakuma l with dissolve
s "……"
hide sakuma 

show tokimine sd with dissolve
t "睡醒後臉色像死人的頻率變得異常的高"

show tokimine n with dissolve
t "你再不好好說話我真的會覺得你中邪耶"
hide tokimine with dissolve

show sakuma with dissolve
s "……"

show sakuma with dissolve
s "我沒中邪"
hide sakuma 

show tokimine n with dissolve
t "那是一種比喻"
hide tokimine with dissolve

show sakuma d with dissolve
s "……"
hide sakuma

show tokimine with dissolve
t "……"
hide tokimine with dissolve

"沉默之間，哥哥突然走過來，伸手輕輕伸向我的頭"

"（要不要躲開？）"

menu:
    "躲開":
        play sound "audio/sound/按鍵音效.mp3"
        play sound "audio/sound/抬腳.mp3"
        show sakuma a with dissolve
        s "……"
        hide sakuma 

        show tokimine ss with dissolve
        t "呵呵……"
     
        show tokimine s with dissolve
        t "挺好的"

        show tokimine ss with dissolve
        t "還會擺出不爽的表情讓我放心不少"
        hide tokimine with dissolve

        show sakuma a with dissolve
        s "……"
        hide sakuma 

        play sound "audio/sound/腳步聲.mp3"
        stop music fadeout 3.0
        "哥哥在我的沉默注視下擺手離開了"

    "不躲":
        play sound "audio/sound/按鍵音效.mp3"
        $ toki += 1

        play sound "audio/sound/摸頭.mp3"
        show tokimine s with dissolve
        "哥哥開始像哄小孩那樣摸我的頭"
        
        show tokimine ss with dissolve
        "輕撫片刻後微微抬起手"
        play sound "audio/sound/搧巴掌.mp3"
        "然後冷不防不輕不重的巴了我的頭頂一下"

        hide tokimine with dissolve
        show sakuma a with dissolve
        s "你幹嘛？？"
        hide sakuma 

        "我視線對上他，有點錯愕的抱怨"

        play sound "audio/sound/腳步停下.mp3"
        "可在我看清他的表情之前，他已經轉頭走進廁所，沒打算回答我"

        show sakuma d with dissolve
        s "……"

        stop music fadeout 3.0
        play sound "audio/sound/腳步聲.mp3"
        show sakuma with dissolve
        s "……"
        hide sakuma 

stop sound
"我也回到我的房間"


##################################################################################################################
##################################################################################################################

scene black with dissolve
centered "中午 - 朔真房間"
centered "章節：分歧點"

play sound "audio/sound/關門.mp3"
"房門關上感覺有些恍惚"

play sound "audio/sound/鈴聲.mp3"
"發散的思緒到一半被突如其來的鈴聲打斷"

show bk03 with dissolve
play sound "audio/sound/鈴聲.mp3"
"手機在桌上震動一下"

play sound "audio/sound/鈴聲.mp3"
"聲音不大但在安靜的房間裡特別刺耳"

play sound "audio/sound/鈴聲.mp3"
play sound2 "audio/sound/腳步停下.mp3"
"我走過去看了一眼螢幕"

"是健"

play sound "audio/sound/抬腳.mp3"
"我接起來"

"對面立刻傳來熟悉的有點懶散的聲音"

scene black with dissolve
show cg11 with dissolve
play music "audio/music/aruite-ikou.mp3"
show ken h at left with dissolve
show sakuma at right with dissolve
k "欸——你醒了？我原本還在想你會不會一路睡到下午"

s "嗯……"

show ken n at left with dissolve
k "我今天超級衰你知道嗎！"

k "我早上起來踩到我姐的樂高啦幹！！"

show sakuma l at right with dissolve
s "……"

show ken at left with dissolve
k "欸你笑了沒？你有笑吧？"

k "沒有也要裝一下喔做人要給面子"

show sakuma at right with dissolve
s "……沒有笑"

show ken h at left with dissolve
k "幹……"

k "好過分喔！"

k "你這樣我會走心……"

play sound "audio/sound/找東西.mp3"
"電話那頭傳來打翻東西的聲音，可能是健一邊講電話一邊在找襪子"

k "然後你知道嗎下禮拜一到三要考三科小考"

show ken n at left with dissolve
k "到底啥小啊…為什麼要擠在同一天…………"

k "好累喔不想卷了啦……"

"電話另一頭的健似乎正在尖叫扭曲陰暗爬行"

show sakuma d at right with dissolve
s "……"

show ken at left with dissolve
k "喔對了！"

k "你讀了沒？感覺你就是那種老早就卷完，然後考前看著我們這些抱佛腳白痴冷笑"

"（朔真的回覆？）"

menu:
    "讀完了":
        play sound "audio/sound/按鍵音效.mp3"
        $ ccc += 1
        show sakuma at right with dissolve
        s "讀完了……"

        show ken n at left with dissolve
        k "幹！！"

    "還沒":
        play sound "audio/sound/按鍵音效.mp3"
        s "還沒"
        show ken at left with dissolve
        k "蛤真的假的？"
        k "你竟然沒讀？！"
        show ken h at left with dissolve
        k "我安心了謝謝你！！"

"我沒說話靠著牆壁聽他繼續碎念"

show ken at left with dissolve
k "算了啦……總之……今天下午要不要出來走走？"

show ken h at left with dissolve
k "打球啊你來不來？不要整天在家發霉好不好"

"我想了一下然後開口"

"（朔真的回覆？）"

menu:
    "跟健出門" if qwq <5  :
        play sound "audio/sound/按鍵音效.mp3"
        show sakuma at right with dissolve
        s "可以幾點？"

        show ken at left with dissolve
        k "兩點半！！"

        k "不要遲到太久喔！"

        show sakuma l at right with dissolve
        s "……"

        show sakuma at right with dissolve
        s "這說法好像你已經預估自己會遲到了……"

        show ken h at left with dissolve
        k "嘿嘿"

        k "掰啦！"

        play sound "audio/sound/放東西到桌上.mp3"
        stop music fadeout 3.0
        s "……"
        jump a
        

    "跟哥哥打遊戲" if toki>=1 and qwq <5:
        play sound "audio/sound/按鍵音效.mp3"

        "我靠在椅背上，想了一下，然後才回覆"

        show sakuma with dissolve
        s "改天吧，我今天要跟哥哥打電動"

        show sakuma d at right with dissolve
        s "抱歉"

        show ken at left with dissolve
        k "喔好吧？"
        
        k "幹嘛道歉啊？"

        s "……"

        show ken h at left with dissolve
        k "總之下次再揪 拜拜～～"

        stop music fadeout 3.0
        play sound "audio/sound/放東西到桌上.mp3"
        show sakuma at right with dissolve
        s "再見"


        jump b

    "……（沉默）" if qwq > 1:
        play sound "audio/sound/按鍵音效.mp3"
        $ agg += 2

        stop music
        show sakuma d at right with dissolve
        s "……"

        play music "audio/music/sorrowful-documentary-music-400922.mp3"
        show ken m at left with dissolve
        k "怎樣？"

        show sakuma sc at right with dissolve
        s "……"

        show ken n at left with dissolve
        k "還沒讀完？"

        show ken at left with dissolve
        k "考試算幾點？放鳥它啊？？"

        s "……"

        show ken h at left with dissolve
        k "喂…回答呢？"

        show sakuma d at right with dissolve
        s "……"

        show ken m at left with dissolve
        k "……"

        show sakuma at right with dissolve
        show ken a at left with dissolve
        k "算了……"

        hide ken with dissolve
        scene bk03 with dissolve
        play sound "audio/sound/放東西到桌上.mp3"
        "健掛了電話"
        "我看著手機螢幕發呆許久"
        "不知為何我有預感這會是他最後一次和我對話"
        "畢竟我這陣子的態度一直很糟糕，他能忍我到現在已經非常不可思議了"

        show sakuma d with dissolve
        s "可惜…嗎……？"

        scene black with dissolve
        "我不知道……"
        play sound "audio/sound/耳鳴.mp3" loop
        s "……"
        s "我到底…在搞什麼……"
        s "……"

        show an05 with dissolve
        "許多複雜的感觸在刮騷著神經"

        "我閉緊眼試圖壓下一切的失控感"
        "就像一直以來面對違和感的手段"
        "早已放棄對於自身反常的動機追根究底"

        "為何失序？為何麻木？"

        "我沒有頭緒"
        "沒有"
        "不知道"
        "不清楚"
        "不理解"
        "還是其實是"

        stop sound
        stop music fadeout 3.0
        scene black with dissolve
        "我不想知道"

        stop sound2
        s "……"

        jump c

    "我要讀書" if ccc<1:
        play sound "audio/sound/按鍵音效.mp3"
        show ken n at left with dissolve
        k "……欸——連你也這樣哦？"

        show sakuma at right with dissolve
        s "……"

        show ken at left with dissolve
        k "好啦好啦我自己去啦……"
        show ken h at left with dissolve
        k "那你加油喔 別讀到昏頭哈哈"
        "他一邊抱怨一邊卻還是裝作不在乎的笑著"

        scene bk03 with dissolve
        "過了幾秒電話掛斷螢幕暗下去"
        stop music fadeout 3.0
        "房間瞬間安靜得像被抽空了空氣"

        play sound "audio/sound/放東西到桌上.mp3"
        
        "我放下手機"

        "盯著桌上散亂的書本，沒來由的感到疲憊"
        
        "我清楚此刻什麼也讀不下去"
        
        "（朔真的行動？）"

        menu:
            "去找哥哥" if toki>=1:
                jump b
            "……":
                jump c

##################################################################################################################
##################################################################################################################

label a:
scene black with dissolve
centered "下午 - 球場"
centered "章節：明亮的那邊"
play sound2 "audio/sound/打球背景音.mp3"
show bk05 with dissolve

show sakuma d with dissolve
s "那個白痴果然遲到……"
hide sakuma

play sound "audio/sound/抬腳.mp3"
"鐵籃架發出一點點吱嘎聲，我一個人站在中線手裡握著籃球沒有力氣也沒有瞄準投了出去"

play sound "audio/sound/打框.mp3"
"擦框、撿起、再投"

play sound "audio/sound/沒種.mp3"
"彈開、撿起、再投"

"沒有中任何一球"

"我持續心不在焉的打發時間"

play sound "audio/sound/抬腳.mp3"
"再次投出"

play sound "audio/sound/沒種.mp3"
"球擦過籃板邊緣彈開滾到場，目前為止最糟糕的一發"

"我站在原地發呆沒去撿球"

"周遭的動靜在這樣空白的片刻被無限放大"

show bk05-1 with dissolve
play music "audio/music/家庭.mp3"
stop sound2 fadeout 3.0
"球場外傳來了笑鬧，我的目光不自覺被吸引"

"那是一個平凡的小家庭"

"××背著女兒媽媽走在旁邊，三個人有說有笑"

"媽媽還做了個鬼臉，女兒笑得往後仰，手扯緊××的頭髮，惹得對方一陣抱怨"

"但責備的話語間全是顯而易見的愛"

"我持續的盯著那幅構圖良好的幸福"

"他們慢慢地走向轉角，光線搖晃著"

show bk05-2 with dissolve

"從葉隙透下來，正好灑在他們身上，就像舞台上的聚光燈"

"記憶碎片在心裡被翻起來，拼出被選擇性拋諸腦後多年的空乏與得不到回應的單向依賴"

"一股像是被從胸口掏出來的，無處安放的恐懼使我陣陣反胃"

"一直以來強迫自己抹掉那個人的身影聲音臉和稱謂"

"那個不想回想起來的存在"

show bk05_2 with dissolve
"此刻正緩緩的浮出自設的心理屏障"

show anbk05 with dissolve
play sound "audio/sound/雜訊.mp3"
s "……"

s "嘖……"

s "好想吐……"

"我站在球場中央，腦子裡的噪音越來越大像幾十台電視同時開著不同頻道"

"胃裡翻騰，心臟跳得不規律，眼前的顏色開始變得模糊"

"耳鳴越來越猖，狂風聲逐漸淡弱"

stop music fadeout 3.0
s "……"

stop sound
scene black with dissolve
k "哇靠！你剛剛的投球姿勢根本是史詩級災難欸？？"

show bk05 with dissolve
play music "audio/music/和健打球.mp3"
play sound2 "audio/sound/打球背景音.mp3"
show ken h with dissolve
k "廢到笑！在搞什麼？"
k "難不成是見鬼了？？"
hide ken

"聲音猛地闖進我的世界，像有人突然把音量開到最大聲的耳機拔掉"

show sakuma sc with dissolve
s "什麼時候到的？"

hide sakuma
show ken with dissolve
k "約莫半分鐘前"
hide ken

show sakuma sc with dissolve
s "……"

hide sakuma
show ken n with dissolve
k "對不起啦對不起！我不是故意遲到的！！"

k "是那個公車誤點，司機又在跟乘客聊天所以開超慢，我差點在車上崩潰"

hide ken
show sakuma with dissolve
s "喔……"
hide sakuma


show ken n with dissolve
k "嗚嗚嗚嗚……你那表情一看就是不信我！！"
hide ken

show sakuma d with dissolve
s "……"
hide sakuma

show ken with dissolve
k "好啦！"

k "之後請你吃飯！"

hide ken
show sakuma with dissolve
s "……"
hide sakuma

"健自顧自地說著"

"對於我沒回答健也沒追問" 

"他只是笑了笑，一邊脫外套一邊說話，順帶把籃球從場邊撿回來丟給我"

"我盯著手裡的球，發現雜音不知何時完全停止了，反胃感也不知何時消失了"

show sakuma d with dissolve
s "……"
hide sakuma

show ken with dissolve
k "怎樣？"
hide ken

show sakuma with dissolve
s "沒什麼……"
hide sakuma

"健不是特別溫柔的人"

"他甚至不是特別在乎我剛剛的異常狀態"

"所以沒有逼我說話沒有質問為什麼"

show sakuma l with dissolve
s "（也可能只是太蠢所以完全沒察覺）"

"但不論如何他總是在"

show sakuma with dissolve
s "好像…挺感動？"
hide sakuma

"我不知道如何描述這種安心感"

show ken h with dissolve
k "要發呆到幾點啊？來啊！！"
hide ken

show sakuma with dissolve
s "嗯"
hide sakuma

show ken with dissolve
k "喔喔？竟然有氣勢了？"
hide ken

"我運球向前撇了眼籃框"

"再看看眼前那個眼神認真，但動作白痴到不知道到底是在防守還是在進行邪教儀式的健"

play sound2 "audio/sound/進了.mp3"
"莫名的突然想認真的一回"

"……"

##################################################################################################################
##################################################################################################################

scene black with dissolve
centered "下午 - 球場"
centered "章節：善意？"

"汗從額頭滑到下巴"

scene bk05 with dissolve
"我喘著氣，手裡的籃球黏黏的，汗水與沙塵混合"

"健在一旁繞著我跑，嘴巴還是不停"

show ken h with dissolve
k"哈哈廢物！你命中率是不是不到10趴啊？"
hide ken

play sound2 "audio/sound/進了.mp3"
"我沒有回話，正在專注地瞄準下一球"

stop sound
"就在投出的那一瞬間，我感覺眼角瞄到熟悉的身影"

"我轉過頭，看向場外"

show bk05-3 with dissolve
play sound2 "audio/sound/腳步停下.mp3"
"貓貓站在籃球場的圍網外"

"一如既往穿著西裝，但這次手上提的不是公事包，而是一個塑膠袋"

"那雙圓圓亮亮的眼睛正安靜地望著我"

n"……"

stop music fadeout 3.0
 
show sakuma l with dissolve
s"……"
hide sakuma

"不確定他在那站了多久，我現在才看到"

"（朔真的行動？）"

menu:
    "過去找貓貓" if qwq <4:
        play sound "audio/sound/按鍵音效.mp3"
        jump choice_11
    "無視他":
        $ qwq += 1
        play sound "audio/sound/按鍵音效.mp3"
        jump choice_22

##################################################################################################################
##################################################################################################################

label choice_11:
scene black with dissolve
scene bk05 with dissolve
play music "audio/music/平靜.mp3"

"我把球往健那邊砸，緩步向貓貓移動"
play sound "audio/sound/進了.mp3"
show ken with dissolve
k"欸？去哪？"
hide ken

play sound "audio/sound/腳步聲.mp3"
"我沒理他，只是走到貓貓面前"

play sound "audio/sound/腳步停下.mp3"
show neko d with dissolve
n"……"
hide neko

show sakuma with dissolve
s"……"
hide sakuma
"貓貓微微的低下頭，看了看手中的塑膠袋，像在思考，但我無法從那沒有任何波動的表情讀出結論"

play sound "audio/sound/塑膠袋.mp3"
"半晌，貓貓抬起視線，把手上的塑膠袋遞給我"

menu:
    "接過袋子":
        play sound "audio/sound/按鍵音效.mp3"
        show cg08 with dissolve

play sound "audio/sound/塑膠袋.mp3"
"我接過那袋東西"

"看見裡頭有三罐飲料、一些食物和我忘記帶出門的毛巾"

scene bk05 with dissolve
"然後貓貓點了一下頭，轉身走了"

"他的腳步就像給人的印象一樣，無聲而沉穩"

play sound2 "audio/sound/塑膠袋.mp3"
"我往健的方向移動，袋子輕晃，裡頭傳來一點點飲料罐晃動的聲響。"

"回到球場，健正蹲著擦汗，他看了看我手裡的袋子，用非常明顯的「暗示」眼神"

play sound2 "audio/sound/放東西到桌上.mp3"
"我翻了個白眼，而後遞給他一罐飲料"

play sound2 "audio/sound/開平.mp3"
"健歡呼一聲，接過去開罐"

"我低頭看自己手上的那一罐"

show cg08 with dissolve
play sound2 "audio/sound/放東西到桌上.mp3"
"罐身貼著一小張便條紙"

"「幾得在六點半前回來」"

s"（今晚要吃好料的意思？）"

"我猜，依照我對他精簡到過分的言語模式的理解"

scene bk05 with dissolve

"這樣簡單的一句話概括了我和貓貓的所有相處溫度"

"這理應是再珍貴不過的、罕見的關心"

"但每當這種時刻，我腦中總是會不合時宜的閃過一個糟糕想法……"

scene black with dissolve
"「偽善者……」"

show bk05 with dissolve
show sakuma with dissolve
s "……"

show sakuma d with dissolve
s "……"

s "（好想吐……）"
hide sakuma

"我轉動瓶蓋，但轉到一半又鎖了回去"

"積壓的煩躁瀕臨潰堤，此刻卻依舊維持表面的風平浪靜"

"更可笑的是，我對於這樣的微妙感觸不討厭"

"不討厭這種補償，也不討厭這種關心"

show sakuma d with dissolve
s"（那麼…我到底在煩躁什麼呢……？）"
hide sakuma

"我抬頭看向天空"

stop music fadeout 3.0
"思索著，或許該離開這種模糊和停滯感了"

jump llllllll

##################################################################################################################
##################################################################################################################

label choice_22:
play music "audio/music/平靜.mp3"
$ qwq += 1
scene black with dissolve
scene bk05 with dissolve

"我短暫的注視他，而後快速的撇開視線"

"就像我們只是無關的陌生人"

play sound2 "audio/sound/打框.mp3"
"和健的對峙持續著"

"場上的落葉被吹到場邊，熾熱的正午光線漸緩"

"當我下次望向場外時，貓貓已經離開了"

show sakuma l with dissolve
s"……"

stop music fadeout 3.0
show sakuma d with dissolve
s"（算了……）"
hide sakuma

scene black with dissolve
"因為與我無關"

jump llllllll

##################################################################################################################
##################################################################################################################

label llllllll: #8
scene black with dissolve
centered "晚上 - 朔真房間"
centered "章節：或許"

show bk03-1 with dissolve
play music "audio/music/跑跑.mp3"
"今天的飯桌上一如既往的沉默"

"是個再平常不過的一天"

"我已經全然習慣了這種步調，但……"

"「總覺得…缺點什麼」"

"不知道該如何表達這種匱乏，但我真的感到厭倦了"

"也知道……"

"再怎麼不想面對，也不可能用這種粗劣的薄弱屏障騙過自己一輩子"

"……"

show an03 with dissolve
"一樣的牆壁、一樣的燈光、一樣的空氣"

show bk02-2 with dissolve
"一樣熟悉的背影"

"我依舊選擇越過了長廊來到了這裡，無論重演幾次這樣的迴圈"

play sound2 "audio/sound/腳步停下.mp3"
"貓貓一如既往的散發著獨特的壓迫感"

"空間大抵是抽象的，記憶大抵是模糊的……"

"醒過來後，夢是如此"

"沒有意義，所以沒有必要試著做出改變……"

"過去我一直是這樣想得，認為溝通也是如此……"

"但…真的毫無意義嗎？"

"我第一次開始質疑"

play sound2 "audio/sound/抬腳.mp3"
"忽然，一直背對著我發呆的貓貓動了動耳朵，然後終於轉過身來"

show bk02 with dissolve
s "……"

show neko with dissolve
n "……"

"他手裡握著槍，但沒有舉起"

"靜靜的看著我，那深不見底的黑瞳似能看穿一切"

"也如往常，帶著若現怒意卻難以察覺、看似無懈可擊的表情"

hide neko
"無意間的默契讓我們雙方沒有任何動作的對視很久很久"

show bk02-1 with dissolve
"久到暴風雨緩和下來，窗戶不再發出聲響"

play sound2 "audio/sound/蟬鳴夜晚.mp3" fadeout 8.0
"久到我清楚的聽見蟬鳴，察覺指針細微的運轉"

show neko with dissolve
"而在漫長的對視中，我注意到了"

"貓貓的眼底除了憤怒來還雜著一絲傷感"

"每次對著我“開槍”時，似乎都是這樣的眼神"

hide neko with dissolve
stop sound2 fadeout 6
show sakuma d with dissolve
s "……"
hide sakuma

stop music fadeout 3.0
show neko d with dissolve
n "……"

play sound "audio/sound/上膛.mp3"
show neko g with dissolve
n "……"

menu:
    "奪槍" if qwq < 4:
        play sound "audio/sound/按鍵音效.mp3"
        jump ed01
    "不動":
        play sound "audio/sound/按鍵音效.mp3"
        jump ed02
    "逃跑" if agg > 1:
        play sound "audio/sound/按鍵音效.mp3"
        jump ed03

##################################################################################################################
##################################################################################################################

label ed01:

play music "audio/music/documentary-music-349124.mp3"
show ed01-1 with vpunch
play sound2 "audio/sound/槍落.mp3"
"我主動奪槍，而後將其摔到地上"

stop sound2
scene bk02-1 with dissolve
show neko s with dissolve
n "！"
hide neko

play sound "audio/sound/全.mp3"
show bk02-1 with vpunch
show sakuma s with dissolve
s "沒有更好的解決方法嗎？"
hide sakuma

play sound "audio/sound/深吸.mp3"
"深吸一口氣，想要緩一緩，但眼淚還是潰堤了……"

show sakuma s1 with dissolve
play sound "audio/sound/全.mp3"
s "為什麼要用這種方式逃避溝通……"
s "媽媽不就是因為這樣才離開你嗎？"
hide sakuma

show neko with dissolve
n "………………"
hide neko

play sound "audio/sound/喘息.mp3"
show sakuma s2 with dissolve
s "現在對我們的那些關心又算什麼？？"
show sakuma s1 with dissolve
s "回答我啊！！"
scene black with dissolve

show ed11 with dissolve
"我很生氣，沒大沒小的對貓貓提出一連串質疑"

"一邊哭，一邊吼，貓貓只是靜靜的聽著"

hide ed11
show ed12 with dissolve
"我越哭越狼狽，吼出來的言語也越來越沒有邏輯，後期只剩散亂的抱怨"

"但心情卻越發輕鬆，或許是多年積壓的感情一次性爆發，因而感到解脫了……"

stop sound fadeout 5.0
stop music fadeout 3.0
"這場爆發的最後，我腦袋一團亂，組織不出任何句子，哭到打嗝，默默等待著終將來臨的制裁"

scene black with dissolve
"可貓貓的行動出乎意料"

play music "audio/music/和解.mp3"
show ed00 with dissolve
play sound "audio/sound/深吸.mp3"
"他靠近我、抱住我……"

play sound "audio/sound/摸頭.mp3"
"抱的很鬆，像是怕我會厭惡一樣，隨時給我掙脫的空間"

"過了一段時間，見我沒有掙扎，他才開始慢慢的、笨拙的輕拍著我的背"

"雖然我還有好多好多不滿、好多好多委屈沒有說出口"

"但是我已經哭累了"

"在這樣陌生的安心感下，視線變得模糊"

scene black with dissolve
"失去意識前，我聽見他這麼說"

n "對不起……"

"而之後發生的一切則沒有任何印象"

"或許因為夢斷在這裡"

"又或者…因為安心所以不在意了……"

#####################################################

scene black with dissolve
"今天的早餐又是熟悉的可頌……"

s "…………"

s "（但好吧，這就是他笨拙的關心方式）"

centered "早晨 - 飯廳"
show ed01-2 with dissolve
"看著這幅日常的光景，我有些感慨"

"隨後揚起了微笑，一個很久沒出現在自己臉上的表情"

"有些僵硬，有點不自然，或許還有點滑稽，但無所謂的"

s "……"
s "爸爸"

n "……"
t "！"
h "喔？奇蹟耶？二哥說話了？？"

"穗乃香語氣聽起來像看到了什麼神奇生物那樣"

"而貓貓只有眼睛微微瞪大，但我能察覺到他其實非常訝異，因為我已經好幾年沒有和他有過任何一句對話了"

s "下次我想換吃三明治，可以嗎？"

n "……"

"愣神許久後，貓貓才回過神，怔怔地點頭"

s "……"

"窗外的陽光很曬，亮得讓人有點不舒服"

stop music fadeout 3.0
"但我不討厭"

scene black with dissolve
centered "GOOD END - 和解"
scene black with dissolve
return

##################################################################################################################
##################################################################################################################

label ed02:

scene black with dissolve
play music "audio/music/原地踏步.mp3"
show bk02 with dissolve

"我沒有逃跑、沒有掙扎……"

"沒有選擇任何一個迴避的手段"

"因為一切都是「註定」"

"即便此刻意識到了自己正在做夢，也沒能打破這樣的迴圈"

show sakuma d with dissolve
s "（或許，我一直都是「醒的」也說不定）"

show sakuma sc with dissolve
s "（但也……）"
hide sakuma 


scene black with dissolve
"「完全無所謂吧？」"

show bk02 with dissolve
show neko with dissolve
"我靜靜地看著他"

play sound "audio/sound/上膛.mp3"
scene black with dissolve
"看著槍口對準自己"

play sound "audio/sound/開槍.mp3"
pause 0.5
play sound "audio/sound/開槍.mp3"
pause 0.4
play sound "audio/sound/開槍.mp3"
pause 0.3
play sound "audio/sound/開槍.mp3"
"看著子彈落在右腿、左腿、腹部、肩膀……"

show bl02 with dissolve
play sound "audio/sound/血散.mp3"
"流淌的血液在地板匯聚，完全浸染了襪子"

show bl03 with dissolve
play sound "audio/sound/血流.mp3"
"感覺腳底變得板黏黏的，卻沒有任何痛感"

show bl04 with dissolve
play sound "audio/sound/低地.mp3"
show bl03 with dissolve
"視線隨之變得越來越模糊，聲音也似越來遠那般變得單薄"

show bl04 with dissolve
play sound "audio/sound/上膛.mp3"
"最後，槍抵在我的額頭，就像一直以來那樣"

play sound "audio/sound/開槍.mp3"
scene black with vpunch
"碰" 

centered "早晨 - 朔真房間"
scene bk03 with dissolve

"我睜開眼"

"熟悉的天花板、熟悉的房間、熟悉的空氣"

scene black with dissolve
"什麼都沒有改變"

"早餐依舊是我早已吃膩的那個味道"

"貓貓一樣沉默不語"

"依然動作機械咀嚼吞嚥，味道也一如既往，膩到令人作嘔"

s "或許……"

s "我或許有能力改變點什麼……"

s "但他選擇了沉默，不是嗎？"

"即便傷害只是所謂的曾經……"

s "我還是覺得好痛"

"真的…很痛……"

"夢中無數次對準了我的槍口或許是因為你依舊選擇沉默不語……"

"那麼"

play sound "audio/sound/開門.mp3"
"我又有什麼義務來開啟溝通呢？"

show ed02-1 with dissolve
stop sound
"聲音在腦子裡迴盪，卻沒有回答"

show ed02-2 with dissolve
"一如往常"

"陽光明媚、刺眼，閃得人煩躁"

show ed02-3 with dissolve
"但我已經習慣了"

stop music fadeout 3.0
"習慣了默默埋怨"

scene black with dissolve
centered "BED END - 死循"
scene black with dissolve
return

##################################################################################################################
##################################################################################################################

label ed03:

play sound "audio/sound/喘息.mp3" loop
scene black with dissolve
play sound2 "audio/sound/撞門.mp3"
"那一刻，我轉身衝出房間"

play music "audio/music/higeki-zitaku.mp3"
play sound2 "audio/sound/心跳.mp3"
show bk01 with dissolve
"走廊是安靜的"

"腳步聲似被無盡延伸的末端深淵吞噬"

play sound2 "audio/sound/跑.mp3" loop
"自己的喘息聲卻清晰"

"眼前的場景沒有絲毫變化"

"像被困在迴圈裡面，讓逃跑顯得毫無意義"

"但我沒有打算回頭"

"也沒有打算停下"

"後方沒有傳來聲音，我無從判斷他有沒有開槍"

"但目前為止沒有感覺到任何事物靠近"

"我大口喘著粗氣，呼吸越來越無序，後背被冷汗濡濕"

stop sound2
stop sound
show bk01-1 with dissolve
"在即將越過身體極限而倒下前的那刻，地板瞬間變成空洞"

stop music
play sound "audio/sound/抬腳.mp3"
show bk01-1 with dissolve
"緊接著是一股下墜感"

scene black with dissolve
centered "凌晨 - 朔真房間"

play sound "audio/sound/呼吸.mp3"
"我張開嘴想叫，但發不出聲音"

scene bk03-1 with dissolve
"我睜開眼"

play sound "audio/sound/按鍵聲.mp3"
play sound2 "audio/sound/心跳.mp3"
"手機的螢幕亮著，顯示 3:00 AM"

play sound "audio/sound/呼吸.mp3"
show sakuma sc with dissolve
"我坐起來，呼吸顫抖"

show sakuma s2 with dissolve 
"想法很雜、很亂，像一個壓抑了太久的抽屜突然爆開"
hide sakuma

"花了約莫三分鐘整理思緒無果，於是我做出了大膽的決定"

"因為撐不下去了"

"無法繼續忍受這股異樣與反胃感"

"無法放著近乎復出水面的答案和心理防線就這麼崩解"

play sound "audio/sound/腳步停下.mp3"
"我下床，步履蹣跚"

play sound2 "audio/sound/翻頁.mp3"
pause 1.0
play sound2 "audio/sound/放東西到桌上.mp3"
"撈起手機、錢包，又隨手抓了幾件衣服塞進包裡"

play sound "audio/sound/開門.mp3"
scene black with dissolve
"然後，推門，關門，出門"
pause 3.0

#####################################

play sound "audio/sound/街道夜晚.mp3"
"動作搖搖晃晃，卻沒有絲毫猶豫"

play music "audio/music/逃家.mp3"
"夜風很涼，街道空蕩蕩，只有路燈時不時閃爍"

play sound "audio/sound/腳步停下.mp3"
"我往車站的方向走"

scene ed03 with dissolve
"我不知道自己打算去哪裡"

"不知道要逃多久、能逃多久"

"只是知道自己不想再留在這裡"

"不想留在這個「家」"

"漫無目的也無所謂"

"思考亂到極點的衝動行為也無所謂"

"連同明天也無所謂"

"我到底在搞什麼？"

"我沒有頭緒"

"沒有"

"完全沒有"

"只是厭倦了作嘔的感覺"

"受夠了莫名奇妙被觸發的耳鳴"

"所以順著唯一明確的念頭"

stop music fadeout 3.0
"「離開……」"

scene black with dissolve
centered "GOOD END - 離家"

return

##################################################################################################################
##################################################################################################################

label b:

scene black with dissolve
centered "中午 - 時嶺房間"
centered "章節：安全感"

scene bk09 with dissolve
play sound "audio/sound/敲門.mp3"
"我敲了敲哥哥的房門，沒等回應就自己走了進去"

play sound "audio/sound/開燈開門(哥哥房間.mp3"
scene black with dissolve
scene bk04 with dissolve
play music "audio/music/哥哥房間.mp3"
"哥哥窩在床旁邊前，耳機戴著，眼神專注，似乎打得激烈"

play sound "audio/sound/敲木.mp3"
"敲擊屏幕的聲音有種奇妙的節奏感"

"我沒有打擾他"

play sound "audio/sound/腳步停下.mp3"
"而是默默走到旁邊，拉了張椅子坐下"

play sound2 "audio/sound/吃洋芋片.mp3"
"隨手抓起桌上那包洋芋片，一口接一口吃了起來"

play sound "audio/sound/over.mp3"
"不久後，一局結束了"

"他拿下耳機，轉頭看了我一眼"

show tokimine s with dissolve
t "上不上？"
hide tokimine

"我點點頭"

play sound "audio/sound/踩雪.mp3"
"然後我們就幾乎沒再多說什麼了，只是默默坐得靠近一些"

play sound "audio/sound/敲木.mp3"
"我們就這樣並肩作戰，在幾乎無聲的昏暗房間裡"

play sound "audio/sound/開平.mp3"
"偶爾會出現飲料開瓶的聲音，或者失利時的小抱怨，氣氛卻不會沉重"

"有時配合得天衣無縫，有時互相埋怨彼此拖後腿"

scene black with dissolve
"在不知不覺中，三個多小時過去了"

"手有點痠，眼睛也乾了"

"窗外從午後變成傍晚"

"但這段時間，比我整週過的任何一天都還要舒服、踏實"

##################################################################################################################
##################################################################################################################

scene black with dissolve
centered "下午 - 時嶺房間"
centered "章節：焦慮"

scene bk04 with dissolve
"打了三個多小時，眼睛已經疲憊酸澀，肩頸痠到快撐不住"

play sound "audio/sound/放東西到桌上.mp3"
"我伸了個懶腰，跟著哥哥開始收拾垃圾與歸位手把"

"我們還沉浸在剛剛勝利的喜悅中，一想到就會忍不住露出滿足的微笑"

"正準備要回到房間休息前，我們又對到視線了"

"但這次哥哥不是一秒收回視線低頭輕笑，而是持續盯著，看著我的眉心發呆"

play music "audio/music/piano-music-376015.mp3"
"被盯的有點久，讓我感覺不自在"

show sakuma l with dissolve
s "……"

show sakuma with dissolve
s "怎麼了？"
hide sakuma

show tokimine sp with dissolve
t "……"
t "啊……"
hide tokimine

show sakuma with dissolve
s "？"
hide sakuma

show tokimine s with dissolve
t "去後山怎麼樣？"
hide tokimine

stop music 
show sakuma sc with dissolve
s "……"

s "…蛤？"
hide sakuma

play music "audio/music/焦慮.mp3"
"為什麼？"

"我開始冒冷汗，不安感正從末肢向上攀升"

"哥哥則是低頭思索片刻，然後露出微笑"

show tokimine s with dissolve
t "只是突然有點懷念那時候還沒完全變成機器人的那個你"

show tokimine ss with dissolve
t "愛哭，膽小，很好玩"
hide tokimine

"哥哥說著說著，臉上慢慢浮現我已經很久沒看到的，兒時的他想到邪惡捉弄計畫時會有的表情"

"幼稚的，期待得逞的輕笑"

show sakuma sc with dissolve
s "……"
hide sakuma

show tokimine sd with dissolve
t "不知道秘密基地是不是還好好地待在那裡呢……"

show tokimine s with dissolve
t "而且你近幾個月不是常常去嗎？"

show tokimine ss with dissolve
t "是不是也感到懷念了啊？"
hide tokimine

show sakuma sc with dissolve
s "……"

show sakuma d with dissolve
"我低下頭，手指蜷縮地握著洋芋片袋口"

"心裡升起一種難以形容的不安"

show sakuma sc with dissolve
s "（要是哥哥發現那些……會怎麼看待我……）"
hide sakuma

"我開始思索著推辭"

"但哥哥沒打算等我回應"

play sound "audio/sound/找東西.mp3"
pause 2.0
stop sound
"他抓起手機，撈起外套，套上鞋子，一套動作行雲流水，花不到二十秒"

play sound "audio/sound/開門.mp3"
show tokimine ss with dissolve
t "那我先走了～"
hide tokimine

"他的語尾輕鬆而慵懶，像是宅久的貓終於打算出去曬曬太陽"

play sound2 "audio/sound/心跳.mp3"
"門關上的瞬間，我狂冒著冷汗"

stop music fadeout 3.0
play sound "audio/sound/腳步停下.mp3"
"發愣好幾秒後才回過神，連忙跟上"

##########################################################

scene black with dissolve
centered "下午 - 林間小徑"
centered "章節：秘密"

play sound "audio/sound/草跑.mp3" loop
scene bk10 with dissolve
play music "audio/music/跑上山.mp3"
"空氣中雜著濕濕的泥土味"

play sound2 "audio/sound/喘息.mp3" loop
"我追著哥哥沿著熟悉的小路穿過樹叢"

"雖然我一路狂奔，但由於晚太久出門，所以還是追不回那段距離"

"哥哥邊跑邊回頭看喘的狼狽的我，然後笑著繼續前進"

"恍惚間，彷彿回到童年的那段時光"

"我想起了和哥哥拿著樹枝打鬧追逐的往事"

"我永遠追不上他，但他永遠不會甩開我，總是維持一個「剛剛好」的距離"

"但我現在一點都高興不起來"

"只是拼了命的想追上，攔住他"

"可他越跑越快，儼然把這當作是我在和他重回童年的嬉戲"

"他不知追逐盡頭，基地的門後藏著的，是多麼醜陋的，偏執的陰暗面……"

"我曾經選擇性吞沒，卻終究止不住宣洩"

"他很快的來到小徑的盡頭"

"看到基地的哥哥顯得更開心了，他平時的陰沉頹廢似乎在一路的追逐中逐漸釋放"

stop sound fadeout 3.0
stop sound2 fadeout 3.0
stop music fadeout 3.0
show sakuma sc with dissolve
s "（已經無法挽回了……）"
hide sakuma

play sound "audio/sound/呼吸.mp3"
scene black with dissolve
"我拖著疲憊的身軀和絮亂的呼吸"

play sound "audio/sound/腳步停下.mp3"
"緩慢走近愣在門口的哥哥"

play music "audio/music/空洞悲傷.mp3"
scene black with dissolve
show cg09 with dissolve
"他完全僵住了"

"我看不到他的表情，但能感覺到他的混亂"

"哥哥一動也不動地站在那"

"呈現在他面前的是我還沒來得及處理完的「素材」"

"沒記錯的話至少有三具以上的屍體"

"還沒拆分的貓，泡著漂白水脫脂的蛇骨，還沒拼完的兔骨……"

"還有其他散亂不完整，但我還沒清理的東西"

"我視線越過哥哥，看著屋內那隻已經腐爛一半的貓，不安感來到最高點"

t "……"

s "……"

"空氣瀰漫令人作嘔的氣味，和沉重的沉默壓力"

################################################

scene black with dissolve
centered "下午 - 基地"
centered "章節：對等違和"
"哥哥緩緩走進去，我緊隨其後"

scene bk07 with dissolve
"環視一圈後，他慢慢轉過頭來，卻沒有說話"
"他眼裡的表情我無法理解"
"不是看不懂，而是無法理解為什麼是這種情緒"
"不像指責，也不像震驚"
"反倒是……"
"釋然？"

show sakuma with dissolve
s "（為什麼……？）"
hide sakuma

"我下意識地退後一步，喉嚨裡一點聲音也發不出"

"空氣沉得幾乎要凝固"

"全身像被什麼冰冷的液體浸泡過，然後暴露在冬天的冷空氣那般起雞皮疙瘩"

"沉默似長達一世紀"

"然後，哥哥終於開口了"

show tokimine with dissolve
t "你是……什麼時候開始的……？"
hide tokimine

show sakuma with dissolve
s "……"
hide sakuma

"我沒回答"

"沒有勇氣回答"

"只是……低下頭，看著自己的腳尖"

"感覺整個人都正在往下沉"

play sound "audio/sound/雜訊.mp3" loop
"在這段看不見盡頭的時間裡，不安攀升"

scene black with dissolve
"「他會怎麼看待我？」"

scene bk07 with dissolve
"這個疑問又一次閃過"

show sakuma sc with dissolve
s "……"

hide sakuma
"但我還是沒有勇氣抬眼，繼續去讀取他接下來的表情"

"只是一味地的不安，一味的逃避"

"一味的靠著搖搖欲墜的未定論假象，索取最後片刻的安全感"

t "朔真……"

"哥哥的聲音混進雜音傳遞過來，即便不想面對，我還是確實的收到了"

stop music fadeout 3.0
stop sound fadeout 3.0
"我緊閉雙眼，深吸一口氣，終於打算面對"

"可在視線抬起的前一秒……"

scene black with dissolve
play sound "audio/sound/抬腳.mp3"
scene ed04 with dissolve
play music "audio/music/maou_bgm_healing12b.mp3"
"我嗅到了洗衣精的味道和衣服上的潮氣"

play sound "audio/sound/摸頭.mp3"
"在還沒搞清楚狀況的愣神中，哥哥的聲音又一次傳來"

t "雖然這麼說有點自以為是……"

t "但……"

t "我好像能理解你為什麼會變成這樣"
t "……"

s "……"

play sound "audio/sound/呼吸.mp3"
"他的聲音比平時低了許多，有點沙啞"

play sound "audio/sound/摸頭.mp3"
"感覺哥哥的手臂又收緊了一些，但不是會讓我難受的力道"

"我聽到了心跳聲和極輕的吸氣聲，但他卻沒有隨後接上下一句"

"反倒是頓了好幾秒後才發話，像在斟酌言詞，也像在消化複雜的情緒"

t "……"
t "或許……還需要很久……"
t "很久很久……"
t "久到我們長大成人……也……不一定能夠走出來……"

s "……"

t "但……"

play sound "audio/sound/呼吸.mp3"
"他頓了頓，在我耳邊的呼吸有點顫抖"

t "我希望……也相信一切都會好起來……"

play sound "audio/sound/摸頭.mp3"
"他的臉埋進我的頸側，瀏海蹭的有點癢"

"而我直到這一刻才察覺，他溫柔而克制的行為中，其實雜著和我一樣的不安"

s "……"

t "都會好起來的……希望你也能這麼相信……"

menu:
    "回應這份溫柔":
        play sound "audio/sound/按鍵音效.mp3"
        jump ed04
    "拆穿這份溫柔" if toki ==2:
        play sound "audio/sound/按鍵音效.mp3"
        jump ed05

##################################################################################################################
##################################################################################################################

label ed04:

scene black with dissolve
scene ed04 with dissolve
"我不自已的開始泛淚"

"而後緊閉雙眼，埋進這令人安心的氣味"

scene ed04-1 with dissolve

play sound "audio/sound/摸頭.mp3"
"抬起手，回抱"

"抱得很緊，很緊……"

"像是落水者抱緊漂浮木，攥緊希望那般"

"胸口的那股冰冷慢慢的隨之沉澱在心底"

"變得悶悶的，重重的"

"但我一點都不討厭"

s "……"

"我們就這樣靜靜地抱著"

"像以前一起躲在衣櫃，等待紛爭落幕時那樣"

"靜靜地，依靠著彼此……"

scene black with dissolve

"或許一切真的會像哥哥說的那樣"

stop music fadeout 3.0
"慢慢好起來……"

"在不知道多久後的未來……"

centered "GOOD END - 依賴"

return
##################################################################################################################
##################################################################################################################
#play sound "audio/sound/.mp3"
label ed05:

stop music
scene black with dissolve
show ed04 with dissolve

s "……"

scene black with dissolve
play sound "audio/sound/踩雪.mp3"
"我抬手抵住哥哥的胸口，推開一些距離"

"而後無預警的抓住他的手腕，用另一支手將他的袖子向上推高"

play music "audio/music/孤独な道行き.mp3"
scene ed07 with fade
t "！"

"哥哥條件反射地想抽開手，但已經來不及了"

s "……"

t "…………………………"

"新舊交錯的傷痕佈滿他前臂內側"

"仔細看會發現，除了觸目驚心的割痕以外，還有若現的瘀青，以及抓痕的結痂"

"諷刺的是，我為此鬆了一口氣"

"因為……"

scene black with dissolve
"「哥哥和我一樣，有著扭曲醜陋的陰暗面」"

"不是只有我被揭穿……"

show bk07 with fade
"而現在，被毫無保留的攤在微弱的光的籠罩之下"

show sakuma with dissolve
s "……"
hide sakuma 

show tokimine sp with dissolve
t "……"
hide tokimine 

"這樣的「靜」維持了幾秒"

"哥哥才反應過來，用力把我推開"

"先前的溫柔蕩然無存"

"我讀到了他眼底的敵意與失望，或許還雜著悲傷"

show tokimine n with dissolve
t "什麼時候發現的……"

show tokimine qw with dissolve
"他極度壓抑的咬牙質問，盯著我的眼神隱約透露動搖"

"我望著這幕有些出神"

"第一次見到哥哥這樣的表情"

"有點類似那些自知即將被我終結的動物的無謂掙扎"

hide tokimine 
"不一樣的是，哥哥的「掙扎」不是試圖逃跑"

"而是帶著摔破罐子的底氣，打算偽裝冷靜到底"

"我覺得那樣易碎的刺很可笑"

"內心升起一股想將其破壞殆盡的意識"

"我想知道……"

"當剝落那份冷靜之後"

$ old_len = renpy.config.history_length
$ renpy.config.history_length = 0
"{color=#971a1a}  「哥哥哭出來的表情」{/color}{fast}{nw}"
"{color=#971a1a}「哥哥哭出來的表情」{/color}{fast}{nw}"
"{color=#971a1a}    「哥哥哭出來的表情」{/color}{fast}{nw}"
"{color=#971a1a}「哥哥哭出來的表情」{/color}{fast}{nw}"
"{color=#971a1a}      「哥哥哭出來的表情」{/color}{fast}{nw}"
$ renpy.config.history_length = old_len

"他還會剩下什麼？"

$ old_len = renpy.config.history_length
$ renpy.config.history_length = 0
"{color=#971a1a}  「好想知道，好想知道……」{/color}{fast}{nw}"
"{color=#971a1a}「好想知道，好想知道……」{/color}{fast}{nw}"
"{color=#971a1a}    「好想知道，好想知道……」{/color}{fast}{nw}"
"{color=#971a1a}「好想知道，好想知道……」{/color}{fast}{nw}"
"{color=#971a1a}      「好想知道，好想知道……」{/color}{fast}{nw}"
$ renpy.config.history_length = old_len

"是迷惘嗎？"

$ old_len = renpy.config.history_length
$ renpy.config.history_length = 0
"{color=#971a1a}  「對不起但我沒有歉意」{/color}{fast}{nw}"
"{color=#971a1a}「對不起但我沒有歉意」{/color}{fast}{nw}"
"{color=#971a1a}    「對不起但我沒有歉意」{/color}{fast}{nw}"
"{color=#971a1a}「對不起但我沒有歉意」{/color}{fast}{nw}"
"{color=#971a1a}      「對不起但我沒有歉意」{/color}{fast}{nw}"
$ renpy.config.history_length = old_len

"絕望？"

$ old_len = renpy.config.history_length
$ renpy.config.history_length = 0
"{color=#971a1a}  「好想毀掉，好想毀掉……」{/color}{fast}{nw}"
"{color=#971a1a}「好想毀掉，好想毀掉……」{/color}{fast}{nw}"
"{color=#971a1a}    「好想毀掉，好想毀掉……」{/color}{fast}{nw}"
"{color=#971a1a}「好想毀掉，好想毀掉……」{/color}{fast}{nw}"
"{color=#971a1a}      「好想毀掉，好想毀掉……」{/color}{fast}{nw}"
$ renpy.config.history_length = old_len

"還是憎惡？"

$ old_len = renpy.config.history_length
$ renpy.config.history_length = 0
"{color=#971a1a}  「狼狽求饒還是無盡縱容？」{/color}{fast}{nw}"
"{color=#971a1a}「狼狽求饒還是無盡縱容？」{/color}{fast}{nw}"
"{color=#971a1a}    「狼狽求饒還是無盡縱容？」{/color}{fast}{nw}"
"{color=#971a1a}「狼狽求饒還是無盡縱容？」{/color}{fast}{nw}"
"{color=#971a1a}      「狼狽求饒還是無盡縱容？」{/color}{fast}{nw}"
$ renpy.config.history_length = old_len

show tokimine qw with dissolve
t "回答我……"
hide tokimine 

"我紛亂的思緒被這聲低吼按下暫停"

show sakuma d with dissolve
s "……"
hide sakuma

"我垂眼思索片刻"

"然後不避諱的接上目光"

show sakuma with dissolve
s "很久以前了"
s "從察覺到你不分四季穿長袖……"

show sakuma d with dissolve
s "……"

show sakuma with dissolve
s "但直到今天才確定是事實"
hide sakuma 

show tokimine sd with dissolve
t "……"

show tokimine qw with dissolve #補
t "所以這算什麼？"
t "報復嗎？"
hide tokimine 

"哥哥的語氣帶著哭腔"

"帶著無力繼續維持溫柔的疲憊"

show sakuma d with dissolve
s "……"

show sakuma with dissolve
s "是報復……"
hide sakuma

"語氣平淡得殘忍"

"連我自己都覺得出乎意料"

"哥哥聞言低下頭"

"視線落於腕側思索"

stop music fadeout 3.0
"我看不清他的表情"

scene black with dissolve
centered "待續(還在思考劇情WWW)"

return
##################################################################################################################
##################################################################################################################

label c:

scene black with dissolve
centered "中午 - 朔真房間"
centered "章節：沉澱與失控"

show bk03 with dissolve
s "……"

play sound "audio/sound/雜訊.mp3"
s "（啊……）"

s "（好吵……）"

s "（又來……）"

s "（可不可以安靜一下…………）"

s "（……）"

s "嘖……"

play sound "audio/sound/開燈開門(哥哥房間.mp3"
play music "audio/music/kowareta-music-box.mp3" 
"我反手鎖上門、關了燈"

scene bk03-1 with dissolve
"那個「喀」的聲音，像是一個小小的隔絕儀式"

"回到房間角落，縮著坐下，膝蓋靠在胸口"

"窗簾掩著，外界的光被完全隔絕"

"這麼做沒有特別的理由，只是現在暫時不想看到任何人"

"不想聽到聲音，不想回應訊息"

"不想解釋自己為什麼拒絕"

"腦袋裡沒有具體的想法，也沒有明確的情緒"

"有的只是空白，和一股緩慢擴散的疲倦"

"「存在」本身逐漸顯得薄弱"

"「思考」也越發空洞，處在一個半解離的狀態"

show sakuma with dissolve
s "……"
hide sakuma 

"我把頭靠在牆上，閉上眼"

"聽見自己的呼吸聲，單調，乏味，像隔著水面傳來的聲音"

"時間過得很慢"

stop music fadeout 3.0
show sakuma with dissolve
s "……"
hide sakuma

"開始陷入了雜亂交錯的回憶"

##################################################################################################################
##################################################################################################################

scene black with dissolve
centered "??? - ???"
show an04 with dissolve
play music "audio/music/futari-ningyou.mp3"
"{color=#0d158c}痛…很痛……"

"{color=#5b5252}為什麼犯那種低級失誤{nw}"

show fl 
pause 0.08
hide fl
play sound2 "audio/sound/雜訊.mp3"
show fl4
pause 0.1
hide fl4
stop sound2
"{color=#0d158c}對不起……"

stop sound2
show fl2 
pause 0.08
hide fl2
play sound2 "audio/sound/雜訊.mp3"
show fl4
pause 0.1
hide fl4
"{color=#5b5252}你就是不在乎才會……{nw}"

stop sound2
show fl4
pause 0.1
hide fl4
"{color=#0d158c}……{nw}"

"{color=#0d158c}（我在搞什麼…………）"

show fl4
pause 0.1
hide fl4
show fl2
pause 0.08
hide fl2
play sound2 "audio/sound/雜訊.mp3"
"{color=#0d158c}（對不起對不起對不起…………）{nw}"

show fl4
stop sound2
hide fl4
"{color=#5b5252}……"

play sound2 "audio/sound/雜訊.mp3"
"{color=#0d158c}好痛……{nw}"

stop sound2
show fl3 
pause 0.05
hide fl3
play sound2 "audio/sound/雜訊.mp3"
"{color=#0d158c}對不起對不起對不起對不起…………{nw}"

show fl4
pause 0.05
hide fl4
stop sound2
"{color=#5b5252}……"

show fl4
pause 0.08
hide fl4
"{color=#671aa2}你在這裡啊？{nw}"

show fl2
pause 0.08
hide fl2
"{color=#0d158c}……"

play sound2 "audio/sound/雜訊.mp3"
"{color=#671aa2}大白痴活該被……{nw}"

show fl4
pause 0.1
hide fl4
stop sound2
"{color=#671aa2}還好嗎？"

play sound2 "audio/sound/雜訊.mp3"
show fl 
pause 0.08
hide fl
show fl2
pause 0.1
hide fl2
"{color=#671aa2}而且沒那麼痛吧？這次不是……{nw}"

show fl4
pause 0.1
hide fl4
stop sound2
"{color=#0d158c}……"

"{color=#671aa2}好啦……"

show fl2 
pause 0.08
hide fl2
"{color=#671aa2}但別哭了行不行？"

play sound2 "audio/sound/雜訊.mp3"
show fl4
pause 0.08
hide fl4
"{color=#671aa2}發狂的貓貓什麼的，這樣就……{nw}"

play sound2 "audio/sound/雜訊.mp3"
"{color=#0d158c}對不起……"

show fl4
pause 0.1
hide fl4
"{color=#0d158c}……{nw}"

"{color=#0d158c}（我到底在搞什麼…………）"

show fl4
pause 0.08
hide fl4
show fl
pause 0.2
hide fl
stop sound2
"{color=#671aa2}別把眼淚抹到……{nw}"

show fl4
pause 0.1
hide fl4
show fl2
pause 0.05
hide fl2
play sound2 "audio/sound/雜訊.mp3"
show fl2
pause 0.05
hide fl2
"{color=#0d158c}（對不起對不起對不起…………）{nw}"

stop sound2
show fl4
pause 0.1
hide fl4
"{color=#f48eab}為什麼大哥你們都這麼陰沉啊？"

play sound2 "audio/sound/雜訊.mp3"
"{color=#0d158c}（羨慕……）"

show fl
pause 0.1
hide fl
"{color=#671aa2}什麼？"

"{color=#0d158c}表情很恐怖……"

play sound2 "audio/sound/雜訊.mp3"
show fl 
pause 0.08
hide fl
stop sound2
"{color=#0d158c}××的表情……{nw}"


show fl2 
pause 0.2
hide fl2
"{color=#671aa2}把這個想像成××{nw}"

show fl4
pause 0.1
hide fl4
stop sound2
"{color=#671aa2}……"

show fl 
pause 0.09
hide fl
"{color=#671aa2}感覺挺蠢的，當我沒說"

"{color=#671aa2}……"

show fl3
pause 0.1
hide fl3
"{color=#671aa2}很害怕嗎？"
 
show fl3
pause 0.1
hide fl3
"{color=#0d158c}謝謝……"

stop sound2
show fl4
pause 0.1
hide fl4
"{color=#671aa2}氛圍變好總歸是件好事吧？"
show fl 
pause 0.08
hide fl

play sound2 "audio/sound/雜訊.mp3"
show fl4
pause 0.1
hide fl4
"{color=#f48eab}××……{nw}"

show fl3
pause 0.1
hide fl3
stop sound2
"{color=#671aa2}很害怕嗎？"

play sound2 "audio/sound/雜訊.mp3"
show fl 
pause 0.2
hide fl
stop sound2
"{color=#0d158c}好羨慕……{nw}"

show fl4
pause 0.1
hide fl4
"{color=#0d158c}真的好羨慕……{nw}"

show fl 
pause 0.09
hide fl
play sound2 "audio/sound/雜訊.mp3"
show black
pause 0.1
hide black
"{color=#0d158c}對不起……{nw}"

show fl4
pause 0.1
hide fl4
show fl 
pause 0.09
hide fl
stop sound2
pause 0.1
play sound2 "audio/sound/雜訊.mp3"
"{color=#0d158c}對不起……{nw}"

show fl4
pause 0.1
hide fl4
show fl 
pause 0.09
hide fl
"{color=#671aa2}無可避免呢…但××有試著補償對吧？"

show black
pause 0.1
hide black
"{color=#0d158c}對不起……{nw}"

show fl4
pause 0.1
hide fl4
show fl 
stop sound2
pause 0.09
hide fl
play sound2 "audio/sound/雜訊.mp3"
"{color=#671aa2}寬容一點吧？"

show black
pause 0.1
hide black
stop music fadeout 3.0
"{color=#5b5252}對不起……{nw}"

show fl4
pause 0.1
hide fl4
show fl 
pause 0.09
hide fl
stop sound2
"{color=#5b5252}××不善於表達…"

scene black with dissolve
###回來思考
##################################################################################################################
##################################################################################################################

scene black with dissolve
centered "下午 - 朔真房間"
centered "章節：情緒"

stop music

play sound2 "audio/sound/踩雪.mp3"
show bk03-1-1 with dissolve
"……"

show sakuma d with dissolve
s "（睡了多久了……）"

"窗簾縫的光變得柔一點，耳鳴也暫時停了"

show sakuma sc with dissolve
s "（頭…好痛……）"
play sound2 "audio/sound/摸頭.mp3"
"我習慣性抬手抹眼角，卻發現臉側都是乾掉的淚，黏著鬢髮"
"鼻子堵著，腦袋昏昏沉沉卻沒有睡意"
"身體一團矛盾，噁心又飢餓，煩躁又發懵"

show sakuma l with dissolve
s "……"

play sound2 "audio/sound/翻頁mp3"
"我回過神時，才發現門口不知何時被塞了一張紙條"

menu:
    "走過去撿起它":
        play sound "audio/sound/按鍵音效.mp3"
        "我揉眼、打了個哈欠，視線隔了好幾秒才對上焦"

play sound2 "audio/sound/翻頁.mp3"
show bk03-1 with dissolve
"紙條上歪斜的字寫著： 中餐跟藥放在桌上，有其他需要的希望你願意告訴我"

show sakuma sc with dissolve
play music "audio/music/復仇.mp3" 
s "……"

"就這麼短的內容，我卻盯著它看了很久"

show an05 with dissolve
"胸口湧上混雜的情感，亂、酸、脹、悶，全擠在一起，我現在根本沒辦法分類情緒"
"我不知道我在想什麼"
"更不知道他在想什麼"
"或著知道，但不想知道……"

"「哪一種都叫人煩躁啊」"

"反胃感又湧上來，喉頭一縮，像要吐，可我知道自己吐不出來"
"一直以來都是如此"
"吐不出來、想也想不明白……"

"逃避什麼？"
"糾結什麼？"
"羨慕什麼？"

scene black with dissolve
"「我沒有頭緒……」"

show an05 with dissolve
"視線再度被淚水模糊，呼吸又變得亂七八糟，被撤下的頭髮散落在地毯"
"光太亮、耳鳴太吵、胃又縮成一團"
"我恨透自己的這些反應"
"但就是停不下思考"
"止不住反應"
"不願意釋懷"
"可又沒辦法憎恨"
"更無法去定義"

stop music fadeout 3.0
s "到底…有完…沒…完…………"

stop sound fadeout 3.0
s "能不能…安靜下來……"

menu:
    "其實是我的問題" if agg < 6:
        play sound "audio/sound/按鍵音效.mp3"
        jump ed06
    "是他不可原諒" if agg >2:
        play sound "audio/sound/按鍵音效.mp3"
        jump ed07

##################################################################################################################
##################################################################################################################

label ed06:

scene black with dissolve
centered "下午 - 朔真房間"

play music "audio/music/自殘.mp3"
show bk03-1 with dissolve
with vpunch
play sound "audio/sound/奏一.mp3"
"頭猛的用力撞向膝蓋"

"在劇痛中我找回了一絲絲的實感"

with vpunch
play sound "audio/sound/奏二.mp3"
"接著撞了第二、第三下……"

play sound "audio/sound/奏三.mp3"
show sakuma sc with dissolve
s"（這算什麼？）"
"覺得自己很渾蛋嗎？"

s"（只是一直沉溺在過往的陰影裡……）"
"一味地自我封閉……"

s"（我有多少次選擇機會……）"
"他釋出了多少善意……"

hide sakuma
"我卻只是一味地用「受害者」的身份同情、包裹、隔離自己"
"他試著補償、試著為我們做很多很多……"
"哥哥也從來沒有因為這些過往而抱怨過半次"

s"（我卻……）"

play sound2 "audio/sound/呼吸.mp3"
show an05 with dissolve
s "……"
s "……"
s "……"

scene black with dissolve
"眼淚停不下來……"

show an05 with dissolve
s "（為什麼總是停不下來……？）"
s "（總是反應過度……？）"

"我已經受夠了"
"對自己這副怎麼也擺脫不了的可憐樣子厭惡至極"

s "……"

with vpunch
play sound "audio/sound/搧巴掌.mp3"

"視線開始模糊，我狠狠刪了自己一巴掌"

show bk03-1 with dissolve
"但只醒了一瞬間"

hide bk03-1 with dissolve
show an05 with dissolve
"下一秒的空間又開始變得抽象、晃動"

s "（想要…安靜…下來……）"
s "（立刻…安靜下來……）"
s "……"
s "……"

menu:   
    "{color=#971a1a}去找「槍」":
        scene black with dissolve
    "{color=#971a1a}去找「槍」":
        scene black with dissolve
    "{color=#971a1a}去找「槍」":
        scene black with dissolve
    "{color=#971a1a}去找「槍」":
        scene black with dissolve
    "{color=#971a1a}去找「槍」":
        scene black with dissolve
    "{color=#971a1a}去找「槍」":
        scene black with dissolve
    "{color=#971a1a}去找「槍」":
        scene black with dissolve
    "{color=#971a1a}去找「槍」":
        scene black with dissolve
    "{color=#971a1a}去找「槍」":
        scene black with dissolve
    
play sound "audio/sound/筆帶.mp3"

scene ed06 with dissolve 
play sound "audio/sound/按鍵音效.mp3"
"我摸索著口袋，撈出了「槍」"
"原本打消的念頭又復發了"

play sound "audio/sound/上膛.mp3"
"懷抱著對自身的恨意、羞愧與罪惡感"

stop music fadeout 3.0
s "我……"

play sound "audio/sound/開槍.mp3"
scene black with dissolve
"扣動了扳機"

centered "BAD END - 自傷"
return

##################################################################################################################
##################################################################################################################

label ed07:

scene black with dissolve
centered "下午 - 朔真房間"

show bk03 with dissolve
play music "audio/music/noroware-piano-uta.mp3"
"想到這裡，我終於停止了哽咽，耳鳴也停止了"
"我異常平靜的凝視那張意味著「關心」的紙條，看著像是機械化的應對"
"不過是自以為是的「補償」"

show sakuma sc with dissolve
s "……"
hide sakuma

"或許，此刻的心情是憤怒的"
"發自肺腑的憤怒"
"身體發顫著，反胃感不曾停歇"

show sakuma s2 with dissolve
s "（那傢伙憑什麼？）"
s "（憑什麼用這種半吊子的關心，試圖修補關係？）"
hide sakuma

"憑什麼用幾個便條、幾個飯糰、幾罐飲料就假裝什麼都沒發生過？"
"憑什麼……"
"從小到大忍受的那些痛、那些淚"
"那個逃不出的夢魘，反覆被開槍的恐懼、絕望、失語……"
"那些被逼著服從的「教訓」……"

"我握著紙條的手開始發抖，紙條被捏得皺巴巴"
"心底是千萬種聲音在嘶吼、嘲笑、低語"

"但在那一片混亂裡，有一個聲音異常清晰"

scene black with dissolve
"「我要，讓他付出代價」"

"……"

show bk09 with dissolve
play sound "audio/sound/開門.mp3"
"似被什麼驅使著一樣，快步穿過走廊，推開那扇熟悉的門"

stop sound
scene black with dissolve
show bk02 with dissolve
"他正在小沙發上打盹，身上蓋著一條薄毯"
show neko with dissolve
"聽到聲響，他睜開眼，困惑地看著我"
hide neko

"沒有說話，一如往常的沉默"
"那張曾經冷漠、陰影之下看不清表情的臉……"
"現在卻掛著一點不知所措的無害表情"

show sakuma s with dissolve
s "……"
hide sakuma

show neko s
play sound "audio/sound/致命一擊.mp3" 
with vpunch
hide neko
"沒有思考，也沒有猶豫，我抓起床邊的電子鐘往他臉上砸過去"

show neko s 
play sound "audio/sound/搧巴掌.mp3" 
with vpunch
hide neko
"在他重心不穩時，整個人撲上去，開始對著他毫無章法的連續重擊"

play sound "audio/sound/喘息.mp3"
scene black with dissolve
s "（是發洩？還是報仇？）"
s "（完全無所謂好嗎？動機什麼的……）"

play sound2 "audio/sound/奏一.mp3"
"我喘著氣，手酸得發麻，但沒有停下來的意思"

show ed05-2 with dissolve
"貓貓沒有反擊，只是看著我"
"眼睛睜大，像是被嚇傻了"

play sound2 "audio/sound/奏二.mp3"
s "（但那又怎樣？）"

play sound2 "audio/sound/奏三.mp3"
show ed05-1 with dissolve
s "那又怎樣！！！"

scene black with dissolve
"是啊……"
"那又怎樣"

stop music fadeout 3.0
"你的那些補償、改變……"
"又怎樣？"

"我的痛苦還是絲毫未減不是嗎？"

scene black with dissolve
centered "BAD END - 報復"

return
##################################################################################################################
##################################################################################################################