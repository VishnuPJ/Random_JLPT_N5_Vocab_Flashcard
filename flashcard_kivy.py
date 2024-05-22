from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
import random
import re

text_jap = """ああ ah  Ah!
会う あう au to meet
青い  あおい aoi blue
赤い あかい akai red
明るい あかるい akarui light, bright
秋 あき aki autumn, fall
開く あく aku open
開ける あける akeru to open
あげる ageru to give
朝 あさ asa morning
朝ご飯 あさごはん asagohan breakfast
あさって あさって asatte the day after tomorrow
足 あし ashi leg, foot
明日 あした ashita tomorrow
あそこ あそこ asoko over there
遊ぶ あそぶ asobu to play
温かい あたたかい atatakai warm
頭 あたま atama head
新しい あたらしい atarashii new
あちら あちら achira over there (polite)
暑い あつい atsui hot (air)
厚い あつい atsui thick
後 あと ato later, after
貴方 あなた anata you
兄 あに ani older brother
姉 あね ane older sister
あの あの ano that (over there)
あの あの ano well, then
アパート アパート apaato apartment
浴びる あびる abiru to take a shower
危ない あぶない abunai dangerous
甘い あまい amai sweet
あまり あまり amari not so
雨 あめ ame rain
洗う あらう arau to wash
有る ある aru to be, to exist
ある ある aru to possess
歩く あるく aruku to walk
あれ あれ are that one
良い いい / よい ii, yoi good
いいえ いいえ iie no
言う いう iu to say, to tell
家 いえ ie house, home
行く いく iku to go
いくつ いくつ ikutsu how many, how old
いくら いくら ikura how much
池 いけ ike pond
医者 いしゃ isha doctor
椅子 いす isu chair
忙しい いそがしい isogashii to be busy
痛い いたい itai to be painful
一 いち ichi one
一日 いちにち ichinichi one day
一番 いちばん ichiban No. 1, the best, the first
いつ いつ itsu when
五日 いつか itsuka the 5th day of the month, 5 days
一緒 いっしょ issho together
五つ いつつ itsutsu five
いつも いつも itsumo always
今 いま ima now
意味 いみ imi meaning
妹 いもうと imouto someone’s younger sister
いや いや iya not likable, unpleasant
入口 いりぐち iriguchi entrance
いる iru need, must have, be required
いる iru to exist
入れる いれる ireru to insert, to put in
色 いろ iro color
色々 いろいろ iroiro various
上 うえ ue top, on, above
後ろ うしろ ushiro back, rear, behind
薄い うすい usui thin
歌 うた uta song
歌う うたう utau to sing
内 うち uchi home
生まれる うまれる umareru to be born
海 うみ umi sea
売る うる uru to sell
上着 うわぎ uwagi coat, jacket
絵 え e picture
映画 えいが eiga movie
映画館 えいがかん eigakan cinema
英語 えいご eigo English language
ええ ええ ee Yes, I see
駅 えき eki station
エレベータ エレベータ erebeeta elevator
円 えん en Yen
鉛筆 えんぴつ enpitsu pencil
御 お o honorific prefix
美味しい おいしい oishii tasty, delicious
大きい おおきい ookii big
おおぜい  oozei many people
お母さん おかあさん okaasan my own mother
お菓子 おかし okashi confectionary, cake
お金 おかね okane money
起きる おきる okiru to get up, to stand up
置く おく oku to put, to place
奥さん おくさん okusan someone’s wife
送る おくる okuru to send
お酒 おさけ osake alcohol, sake
お皿 おさら osara plate
伯父さん おじさん ojisan uncle
おじいさん  おじいさん ojiisan grand father
押す おす osu to push
遅い おそい osoi late, slow
お茶 おちゃ ocha tea
お手洗い おてあらい otearai toilet, lavatory
お父さん おとうさん otousan father
弟 おとうと otouto someone’s younger brother
男 おとこ otoko man
男の子 おとこのこ otokonoko boy
一昨日 おととい ototoi the day before yesterday
一昨年 おととし ototoshi the year before last
大人 おとな otona adult
お腹 おなか onaka stomach
同じ おなじ onaji same
お兄さん おにいさん oniisan someone’s elder brother
お姉さん おねえさん oneesan someone’s elder sister
伯母さん おばさん obasan aunt
おばあさん obaasan grandmother
お弁当 おべんとう obentou lunchbox
覚える おぼえる oboeru to memorize, to remember
重い おもい omoi heavy
面白い おもしろい omoshiroi interesting, funny
泳ぐ およぐ oyogu to swim
降りる おりる oriru to get off
終わる おわる owaru to end
音楽 おんがく ongaku music
女 おんな onna woman
女の子 おんなのこ onnanoko girl
〜回 〜かい ~kai ~times
〜階 〜かい ~kai ~floor
外国 がいこく gaikoku foreign country
外国人 がいこくじん gaikokujin foreigner
会社 かいしゃ kaisha company, enterprise
階段 かいだん kaidan stairs
買物 かいもの kaimono shopping
買う かう kau to buy
返す かえす kaesu to return an object
帰る かえる kaeru to return home
顔 かお kao face
かかる kakaru to take time, money
鍵 かぎ kagi key
書く かく kaku to write
学生 がくせい gakusei student
〜か月 〜かげつ ~kagetsu ~ number of months
かける kakeru to wear
かける kakeru to make a phone call
傘 かさ kasa umbrella
貸す かす kasu to lend
風 かぜ kaze wind
風邪 かぜ kaze a cold
家族 かぞく kazoku family
方 かた kata person (polite)
片仮名 かたかな katakana Katakana
一月 いちがつ ichigatsu January
二月 にがつ nigatsu February
三月 さんがつ sangatsu March
四月 しがつ shigatsu April
五月 ごがつ gogatsu May
六月 ろくがつ rokugatsu June
七月 しちがつ shichigatsu July
八月 はちがつ hachigatsu August
九月 くがつ kugatsu September
十月 じゅうがつ juugatsu October
十一月 じゅういちがつ juuichigatsu November
十二月 じゅうにがつ juunigatsu December
学校 がっこう gakkou school
角 かど kado corner
家内 かない kanai my wife
鞄 かばん kaban bag
花瓶 かびん kabin vase
冠る かぶる kaburu to put on a hat
紙 かみ kami paper
カメラ かめら kamera camera
火曜日 かようび kayoubi Tuesday
辛い からい karai hot, spicy
体 からだ karada body
借りる かりる kariru to borrow
〜がります ~garimasu 3rd person wants to
軽い かるい karui light (not heavy)
カレンダー カレンダー karendaa  calendar
川 かわ kawa river
〜側  ~がわ ~gawa ~side
可愛い かわいい kawaii cute, pretty
漢字 かんじ kanji Kanji character
木 き ki tree
黄色い きいろい kiiroi yellow
消える きえる kieru to go out, to vanish
聞く きく kiku to hear, to listen, to ask
北 きた kita north
ギター ギター gitaa guitar
汚い きたない kitanai dirty
喫茶店 きっさてん kissaten coffee shop
切手 きって kitte stamp
切符 きっぷ kippu ticket
昨日 きのう kinou yesterday
九 きゅう kyuu nine
牛肉 ぎゅうにく gyuuniku beef
牛乳 ぎゅうにゅう gyuunyuu milk
今日 きょう kyou today
教室 きょうしつ kyoushitsu class room
兄弟 きょうだい kyoudai siblings
去年 きょねん kyonen last year
嫌い きらい kirai unpleasant, not likable
切る きる kiru to cut
着る きる kiru to wear, to put on
来る くる kuru to come
きれい kirei beautiful, clean
キロ キロ kiro kg
キロ キロ kiro km
銀行 ぎんこう ginkou bank
金曜日 きんようび kinyoubi Friday
九 く ku nine
薬 くすり kusuri medicine
下さい ください kudasai give me…
果物 くだもの kudamono fruit
口 くち kuchi mouth
靴 くつ kutsu shoe
靴下 くつした kutsushita socks
国 くに kuni country
曇り くもり kumori cloudy weather
暗い くらい kurai dark
ぐらい ぐらい gurai about
クラス クラス kurasu class
グラム グラム guramu gram
車 くるま kuruma car
黒い くろい kuroi black
今朝 けさ kesa this morning
消す けす kesu to turn off, switch off
けっこう kekkou fine, all right
結婚 けっこん kekkon marriage
月曜日 げつようび getsuyoubi Monday
玄関 げんかん genkan entrance of a house
元気 げんき genki vigor, health, vitality
〜個 〜こ ~ko counter for small objects
五 ご go five
〜語 〜ご ~go ~ language
公園 こうえん kouen park, large garden
交番 こうばん kouban police box
声 こえ koe voice
コート コート kooto coat
ここ ここ koko here
午後 ごご gogo afternoon
九日 ここのか kokonoka 9th day of a month, 9 days
九つ ここのつ kokonotsu nine
ご主人 ごしゅじん goshujin someone else’s husband
午前 ごぜん gozen morning, a.m.
答える こたえる kotaeru to answer
こちら こちら kochira this side, this place
コップ コップ koppu cup, glass
今年 ことし kotoshi this year
言葉 ことば kotoba phrase, language
子供 こども kodomo child
この この kono this…
御飯 ごはん gohan meal, cooked rice
困る こまる komaru to be in trouble
これ これ kore this
ごろ ごろ goro around…
今月 こんげつ kongetsu this month
今週 こんしゅう konshuu this week
こんな こんな konna this sort of, this kind of
今晩 こんばん konban this evening
さあ さあ saa well…
〜歳 〜さい ~sai years old
魚 さかな sakana fish
先 さき saki earlier, former
咲く さく saku to blossom
作文 さくぶん sakubun composition
さす sasu to open an umbrella
冊 〜さつ ~satsu counter for books
雑誌 ざっし zasshi magazine
砂糖 さとう satou sugar
寒い さむい samui cold
再来年 さらいねん sarainen the year after next year
三 さん san three
〜さん 〜さん ~san Mr., Mrs.
散歩 さんぽ sanpo to take a walk
四 し shi four
〜時 〜じ ~ji o’clock
塩 しお shio salt
しかし しかし shikashi however, but
時間 じかん jikan time
〜時間 〜じかん ~jikan ~hours (classificator)
仕事 しごと shigoto work
辞書 じしょ jisho dictionary
静か しずか shizuka quiet
下 した shita under, below
質問 しつもん shitsumon question
自転車 じてんしゃ jitensha bicycle
自動車 じどうしゃ jidousha car, vehicle
死ぬ しぬ shinu to die, to pas away
字引 じびき jibiki dictionary
自分 じぶん jibun oneself
閉まる しまる shimaru to close
閉める しめる shimeru to close
締める しめる shimeru to fasten a seatbelt
じゃ じゃ ja well, then
写真 しゃしん shashin photo
シャツ シャツ shatsu shirt
十 じゅう juu ten
~週間 〜しゅうかん ~shuukan … weeks
授業 じゅぎょう jugyou lesson, class
宿題 しゅくだい shukudai homework
上手 じょうず jouzu to be good at something
丈夫 じょうぶ joubu to be strong, durable
醤油 しょうゆ shouyu soy sauce
食堂 しょくどう shokudou dining room, canteen
知る しる shiru to know
白い しろい shiroi white
〜人 〜じん ~jin ~an, ~ese (nationality)
新聞 しんぶん shinbun newspaper
水曜日 すいようび suiyoubi Wednesday
吸う すう suu to breathe, to smoke
スカート スカート sukaato skirt
好き すき suki to like
〜過ぎ 〜すぎ ~sugi past, over
すぐに すぐに sugu ni at once
少し すこし sukoshi a little
涼しい すずしい suzushii cool
〜ずつ 〜ずつ ~zutsu each
ストーブ ストーブ sutoobu stove, heater
スプーン スプーン supuun spoon
スポーツ スポーツ supootsu sports
ズボン ズボン zubon trousers
住む すむ sumu to live, to reside somewhere
スリッパ スリッパ surippa slipper
する する suru to do
座る すわる suwaru to sit
背 せい sei height
生徒 せいと seito student
セーター セーター seetaa sweater
石鹸 せっけん sekken soap
背広 せびろ sebiro jacket, suit
狭い せまい semai narrow
ゼロ ゼロ zero zero
千 せん sen 1,000, thousand
先月 せんげつ sengetsu last month
先週 せんしゅう senshuu last week
先生 せんせい sensei teacher
洗濯 せんたく sentaku washing, to wash
全部 ぜんぶ zenbu all
そう そう sou so
掃除 そうじ souji to clean
そうして そうして soushite and then
そこ そこ soko there
そちら そちら sochira there (polite)
外 そと soto outside
その その sono that…
そば そば soba next to
空 そら sora sky
それ それ sore that
それから それから sorekara after that
それでは それでは soredewa then, well
〜台 〜だい ~dai counter for machines
大学 だいがく daigaku university
大使館 たいしかん taishikan embassy
大丈夫 だいじょうぶ daijoubu OK
大好き だいすき daisuki to be very fond of
大切 たいせつ taisetsu very important
たいてい taitei mostly, usually
台所 だいどころ daidokoro kitchen
大変 たいへん taihen very, serious
高い たかい takai high, expensive
沢山 たくさん takusan many, much
タクシー タクシー takushii taxi
出す だす dasu to take out, hand in
~達 〜たち ~tachi more than one, and others
立つ たつ tatsu to stand
建物 たてもの tatemono building
楽しい たのしい tanoshii pleasant, enjoyable
頼む たのむ tanomu to ask, to request
たばこ たばこ tabako cigarette
多分 たぶん tabun perhaps, probably
食べ物 たべもの tabemono food
食べる たべる taberu to eat
卵 たまご tamago egg
誰 だれ dare who?
誕生日 たんじょうび tanjoubi birthday
だんだん だんだん dandan gradually
小さい ちいさい chiisai small
近い ちかい chikai near, close
違う ちがう chigau different
地下鉄 ちかてつ chikatetsu subway
地図 ちず chizu map
父 ちち chichi my father
茶色 ちゃいろ chairo brown
茶碗 ちゃわん chawan rice bowl
〜中 〜ちゅう ~chuu in the middle of
ちょうど ちょうど choudo just
ちょっと ちょっと chotto a little
一日 ついたち tsuitachi the 1st day of a month
使う つかう tsukau to use
疲れる つかれる tsukareru to get tired
次 つぎ tsugi next
着く つく tsuku to arrive
机 つくえ tsukue table
作る つくる tsukuru to make, to produce
点ける つける tsukeru to turn on
勤める つとめる tsutomeru to work for someone
詰らない つまらない tsumaranai uninteresting
冷たい つめたい tsumetai cold
強い つよい tsuyoi strong
手 て te hand
テープ テープ teepu tape
テープレコーダー テープレコーダー  teepu rekoodaa tape recorder
テーブル テーブル teeburu table
出かける でかける dekakeru to go out
手紙 てがみ tegami letter
出来る できる dekiru can
出口 でぐち deguchi exit
テスト テスト tesuto test
では では dewa then, well
デパート デパート depaato department store
でも でも demo but
出ます でます demasu to leave
テレビ テレビ terebi TV
天気 てんき tenki weather
電気 でんき denki electricity
電車 でんしゃ densha train
電話 でんわ denwa phone
戸 と to door
〜度 〜ど ~do ~times, ~degree
ドア ドア doa door
トイレ トイレ toire toilet, lavatory
どう どう dou how?
どうして どうして doushite why?
どうぞ どうぞ douzo please, here you are
動物 どうぶつ doubutsu animal
どうも どうも doumo thanks
十 とお too ten
遠い とおい tooi far
十日 とおか tooka the 10th day of a month, 10 days
時々 ときどき tokidoki sometimes
時計 とけい tokei watch, clock
どこ どこ doko where?
所 ところ tokoro place
図書館 としょかん toshokan library
どちら どちら dochira which, where (polite)
とても とても totemo very much, quiet
どなた どなた donata who (polite)
隣り となり tonari next to
どの どの dono which?
飛ぶ とぶ tobu to fly
止まる とまる tomaru to stop
友達 ともだち tomodachi friend
土曜日 どようび doyoubi Saturday
鳥 とり tori bird
鶏肉 とりにく toriniku chicken meat
取る とる toru to take
撮る とる toru to take a photo
どれ どれ dore which?
どんな どんな donna what kind of?
ナイフ ナイフ naifu knife
中 なか naka inside
長い ながい nagai long
鳴く なく naku to sing, mew, moo
夏 なつ natsu summer
夏休み なつやすみ natsuyasumi summer vacation
〜など 〜など ~nado and so on
七つ ななつ nanatsu seven
何 なに nani what?
七日 なのか nanoka the 7th of a month, 7 days
名前 なまえ namae name
習う ならう narau to learn
並ぶ ならぶ narabu to form a line
並べる ならべる naraberu to line up
なる naru to become
二 に ni two
賑やか にぎやか nigiyaka lively
お肉 おにく oniku meat
西 にし nishi west
〜日 〜にち ~nichi …st, ..nd, ..th
日曜日 にちようび nichiyoubi Sunday
荷物 にもつ nimotsu luggage
ニュース ニュース nyuusu news
庭 にわ niwa garden
〜人 ~にん ~nin … people
脱ぐ ぬぐ nugu to take off clothes
ネクタイ ネクタイ nekutai necktie
寝る ねる neru to go to bed
〜年 〜ねん ~nen ~years
ノート ノート nooto notebook
登る のぼる noboru to climb up
飲物 のみもの nomimono drinks
飲む のむ nomu to drink
乗る のる noru to take, to ride
歯 は ha teeth
パーテイー パーテイー paateii party
はい はい hai yes
〜はい 〜はい ~hai cups of ~
灰皿 はいざら haizara ashtray
入る はいる hairu to enter
葉書 はがき hagaki postcard
履く はく haku to put on shoes
箱 はこ hako box
橋 はし hashi bridge
箸 はし hashi chopsticks
始まる はじまる hajimaru to begin, to start
始め はじめ hajime start, the beginning
初めて はじめて hajimete for the first time
走る はしる hashiru to run
バス バス basu bus
バター バター bataa butter
二十歳 はたち hatachi 20 years old
働く はたらく hataraku to work
八 はち hachi eight
二十日 はつか hatsuka the 20th of the month, 20 days
花 はな hana flower
鼻 はな hana nose
話 はなし hanashi conversation, tale
話す はなす hanasu to talk, to speak, to tell
母 はは haha my mother
早い はやい hayai early
速い はやい hayai fast, quick
春 はる haru spring
張る はる haru to put something on, to stick
晴れる はれる hareru to clear up
〜半 〜はん ~han Half~
晩 ばん ban evening
~番 〜ばん ~ban No.~, ranking
パン パン pan bread
ハンカチ ハンカチ hankachi handkerchief
番号 ばんごう bangou number
晩ご飯 ばんごはん bangohan dinner
半分 はんぶん hanbun half
東 ひがし higashi east
〜匹 〜ひき ~hiki counter for animals
引く ひく hiku to pull
弾く ひく hiku to play (an instrument)
低い ひくい hikui  low
飛行機 ひこうき hikouki plane
左 ひだり hidari left
人 ひと hito person
一つ ひとつ hitotsu one
一月 ひとつき hitotsuki one month
一人 ひとり hitori one person
暇  ひま hima free time, leisure
百 ひゃく hyaku hundred
病院 びょういん byouin hospital
病気 びょうき byouki ill, sick
平仮名 ひらがな hiragana hiragana characters
昼 ひる hiru noon
昼ご飯 ひるごはん hirugohan lunch
広い ひろい hiroi wide, spacious
フィルム フィルム firumu film
封筒 ふうとう fuutou envelope
プール プール puuru pool
フォーク フォーク fooku fork
吹く ふく fuku to blow (wind)
服 ふく fuku clothes
二つ ふたつ futatsu two
豚肉 ぶたにく butaniku pork
二人 ふたり futari two people
二日 ふつか futsuka 2nd day of the month, 2 days
太い ふとい futoi thick, fat
降る ふる furu to fall (rain, snow)
古い ふるい furui old
お風呂 おふろ ofuro bath
〜分 〜ふん ~fun ~minutes
ページ ページ peeji page
下手 へた heta not good at something
ベッド ベッド beddo bed
部屋 へや heya room
辺 へん hen side, part, area
ペン ぺん pen pen
勉強 べんきょう benkyou to study
便利 べんり benri convenient
方 ほう hou ~より〜のほうが〜
帽子 ぼうし boushi hat
ボールペン ボールペン boorupen ballpen
他 ほか hoka another, other
ポケット ポケット poketto pocket
欲しい ほしい hoshii to want something
細い ほそい hosoi thin, fine
ボタン ボタン botan button
ホテル ホテル hoteru hotel
本 ほん hon book
〜本 ~ほん ~hon counter for long objects
本棚 ほんだな hondana bookshelf
本当に ほんとうに hontouni really
〜枚 〜まい ~mai counter for thin objects
毎朝 まいあさ maiasa every morning
毎月 まいつき/まいげつ maitsuki/maigetsu every month
毎週 まいしゅう maishuu every week
毎日 まいにち mainichi every day
毎年 まいとし/まいねん maitoshi/mainen every year
毎晩 まいばん maiban every evening
前 まえ mae front
〜前 〜まえ ~mae before, in front of
曲がる まがる magaru to turn
不味い まずい mazui bad tasting
また また mata also, again
まだ まだ mada not yet
町 まち machi city, town
待つ まつ matsu to wait
真直ぐに まっすぐに massugu ni straight ahead
マッチ マッチ machi matches
窓 まど mado window
丸い まるい marui round
万 まん man ten thousand
万年筆 まんねんひつ mannenhitsu fountain pen
磨く みがく migaku to polish, to brush
右 みぎ migi right
短い みじかい mijikai short
お水 おみず omizu water
店 みせ mise shop
見せる みせる miseru to look, to watch
道 みち michi road
三日 みっか mikka 3rd day of a month, 3 days
三つ みっつ mittsu three
皆さん みなさん minsan everyone
南 みなみ minami south
耳 みみ mimi ear
見る みる miru to see, to watch
皆 みんな minna all, everyone
六日 むいか muika the 6th day of a month, 6 days
向こう むこう mukou over there
難しい むずかしい muzukashii difficult
六つ むっつ muttsu six
目 め me eye
メートル メートル meetoru meter
めがね めがね megane a pair of glasses
もう もう mou already, yet
もう もう mou (one) more
木曜日 もくようび mokuyoubi Thursday
もしもし もしもし moshimoshi hello on the phone
勿論 もちろん mochiron of course
持つ もつ motsu to have, to own
もっと もっと motto more
物 もの mono thing
門 もん mon gate
問題 もんだい mondai problem, question
〜屋 〜や ~ya shop. store
八百屋 やおや yaoya vegetable shop
野菜 やさい yasai vegetable
優しい やさしい yasashii gentle
安い やすい yasui cheap, inexpensive
休み やすみ yasumi holiday, vacation
休む やすむ yasumu to rest
八つ やっつ yattsu eight
山 やま yama mountain
やる yaru to do
八日 ようか youka 8th day of the month, 8 days
洋服 ようふく youfuku western style clothing
よく よく yoku often
横 よこ yoko horizontal
四日 よっか yokka 4th day of the month, 4 days
四つ よっつ yottsu four
呼ぶ よぶ yobu to call
読む よむ yomu to read
夜 よる yoru night
来月 らいげつ raigetsu next month
来週 らいしゅう raishuu next week
来年 らいねん rainen next year
ラジオ ラジオ rajio radio
立派 りっぱ rippa splendid
留学生 りゅうがくせい ryuugakusei foreign student
両親 りょうしん ryoushin parents
料理 りょうり ryouri cooking
旅行 りょこう ryokou travel
れい rei zero
冷蔵庫 れいぞうこ reizouko refrigerator
レコード レコード rekoodo record
レストラン レストラン resutoran restaurant
練習 れんしゅう renshuu practice
六 ろく roku six
ワイシャツ ワイシャツ waishatsu white shirt
若い わかい wakai young
分かる わかる wakaru to know, to understand
忘れる わすれる wasureru to forget
私 わたし watashi me, I
渡す わたす watasu to hand over
渡る わたる wataru to cross
悪い わるい warui bad"""


def is_japanese(word):
    japanese_pattern = re.compile(r'[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FAF\u3400-\u4DBF]')
    return bool(japanese_pattern.search(word))

main_lst = []

for i in text_jap.split("\n"):
    count = 0
    i = i.replace("  "," ")
    split_lst = i.split(" ")
    if ((is_japanese(split_lst[0])== True) and (is_japanese(split_lst[1])== True)):
        main_lst.append([split_lst[0],split_lst[1],split_lst[2]," ".join(split_lst[3:])])
    else:
        main_lst.append(["No Kanji" ,split_lst[0],split_lst[1]," ".join(split_lst[2:])])

class FlashcardApp(App):
    def build(self):
        self.current_index = -1
        self.show_romaji = True
        self.show_meaning = True
        self.randomize = False

        main_layout = BoxLayout(orientation='vertical')

        self.grid_layout = GridLayout(rows=4)

        self.kanji_label = Label(font_size=100,font_name = "NotoSansJP-VariableFont_wght.ttf")
        self.hiragana_label = Label(font_size=100, color=[1, 0, 0, 1],font_name = "NotoSansJP-VariableFont_wght.ttf")
        self.romaji_label = Label(font_size=50, color=[0.5, 0.5, 0.5, 1])
        self.meaning_label = Label(font_size=52, color=[0.5, 0.5, 0.5, 1])

        self.grid_layout.add_widget(self.kanji_label)
        self.grid_layout.add_widget(self.hiragana_label)
        self.grid_layout.add_widget(self.romaji_label)
        self.grid_layout.add_widget(self.meaning_label)

        main_layout.add_widget(self.grid_layout)

        button_layout = BoxLayout(orientation='horizontal')

        self.toggle_romaji_button = CheckBox(active=self.show_romaji)
        self.toggle_romaji_button.bind(active=self.on_romaji_checkbox_active)
        romaji_label = Label(text="Show Romaji")

        self.toggle_meaning_button = CheckBox(active=self.show_meaning)
        self.toggle_meaning_button.bind(active=self.on_meaning_checkbox_active)
        meaning_label = Label(text="Show Meaning")

        self.randomize_button = CheckBox(active=self.randomize)
        self.randomize_button.bind(active=self.on_randomize_checkbox_active)
        random_label = Label(text="Randomize")

        self.next_button = Button(text="Next")
        self.next_button.bind(on_press=self.show_next_card)

        button_layout.add_widget(self.toggle_romaji_button)
        button_layout.add_widget(romaji_label)
        button_layout.add_widget(self.toggle_meaning_button)
        button_layout.add_widget(meaning_label)
        button_layout.add_widget(self.randomize_button)
        button_layout.add_widget(random_label)
        button_layout.add_widget(self.next_button)

        main_layout.add_widget(button_layout)

        return main_layout

    def on_romaji_checkbox_active(self, instance, value):
        self.show_romaji = value
        self.show_card()

    def on_meaning_checkbox_active(self, instance, value):
        self.show_meaning = value
        self.show_card()

    def on_randomize_checkbox_active(self, instance, value):
        self.randomize = value

    def show_next_card(self, instance):
        if self.randomize:
            self.current_card = random.choice(main_lst)
        else:
            self.current_index = (self.current_index + 1) % len(main_lst)
            self.current_card = main_lst[self.current_index]
        self.show_card()

    def show_card(self):
        kanji, hiragana, romaji, meaning = self.current_card
        self.kanji_label.text = kanji
        self.hiragana_label.text = hiragana
        self.romaji_label.text = romaji if self.show_romaji else ""
        self.meaning_label.text = meaning if self.show_meaning else ""

if __name__ == '__main__':
    FlashcardApp().run()