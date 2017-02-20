#!/usr/bin/env python
# -*- coding:utf-8 -*-
# File          : lang_def.py
# Author        : bssthu
# Project       : eso_zh_ui
# Description   : lang.csv 的定义
# 


# category: (name_file_id, desc_file_id)
file_id_of_pair = {
    'skill': ('198758357', '132143172'),
    'book': ('51188213', '21337012'),
    'item': ('242841733', '228378404'),
    'questitem': ('267697733', '139139780'),
    'crown': ('70328405', '263796174'),
    'mount': ('18173141', '211640654'),     # 坐骑宠物服装DLC等等
    'loadscreen': ('162658389', '70901198'),
    'three-alliance': ('116704773', '235463860'),
    'journey': ('52420949', '265851556'),
    'merchant-talk': ('8290981', '165399380'),      # 商人，商人说的话，人名不译
}

# category: (file1_id, file2_id, ...)
file_id_of_list = {
    'interact-action': ('3427285', '6658117', '8158238', '12320021', '12912341',
                        '34717246', '45275092', '45608037', '70307621', '74865733',
                        '84555781', '108533454', '139475237', '219689294', '263004526'),
    'greeting': ('75236676', '75237444', '75238212', '75240772', '75241540', '75242308',
                 '75244868', '75245636', '75246404', '75248964', '75249732', '75250500',
                 '75253060', '75253828', '75254596', '75257156', '75257924', '75258692',
                 '75261252', '75262020', '75262788', '75265348', '75266116', '75266884',
                 '149979604', '149983700', '149987796', '149991892', '149995988',
                 '150000084', '150004180', '150008276', '150045140', '150049236',
                 '150053332', '150057428', '150061524', '150065620', '150069716',
                 '150073812', '150525940', '150962644', '150966740', '150970836',
                 '150974932', '150979028', '150983124', '150987220', '150991316'),
    'chat': ('78205445', '121778053'),
    'item-type': ('33378341', '41262789', '52856117', '59621621',
                  '68494373', '124119973', '217370677'),
    'tip': ('4922190', '13753646', '18104308', '25948373', '37288388', '41714900', '49496084', '50143374',
            '58548677', '62156964', '69169806', '74148292', '81761156', '84281828', '86601028',
            '86917166', '117539474', '123557796', '130851621', '144446238', '145410824', '148453652',
            '154416852', '155022052', '156570558', '156664686', '159929300', '160227428', '164328533',
            '164387044', '168351172', '168857941', '185724645', '193511764', '193678788', '213229525',
            '220262196', '221172404', '229654260', '230486948', '235850260', '243094948', '246790420',
            '252100948', '252855860', '254784612', '256705124', '259956452', '266730334'),
    'title': ('22296053', '60155541', '63563637', '87522148',
              '143348165', '186232436', '215700677', '221887989', ),
    'npc-name': ('8290981', '33425332', '51188660', '191999749', '207398837'),      # 主要是 8290981
    'location-and-object': ('142250453', '146361138', '157886597', '162946485',
                            '164009093', '19398485', '211899940', '247934532', '260523861',
                            '267200725', '268015829', '28666901', '39619172', '57008677',
                            '76200101', '77659573', '81344020', '87370069'),
    'more-desc': ('8379076', '50040644', '52183620', '127454222', '151931684',
                  '164317956', '171157587', '191189508', '206046340', '224875171'),
    'more-ui': ('5759525', '17915077', '37408565', '51109077', '65447205', '68561141', '79246725',
                '92356820', '96962005', '99527054', '101034709', '106474997', '108643301', '111863941',
                '112758405', '115337253', '119308740', '121402798', '124318053', '131421317', '143563989',
                '143811061', '148355781', '156152165', '173340693', '191379205', '196014052', '200521140',
                '203274254', '204530069', '207758933', '210579221', '216055893', '219429541', '224768149',
                '224972965', '236931909', '245765621', '257983733'),
    'trap': ('14464837', ),
    'treasure-map': ('39160885', ),
    'interact-win': ('149328292', ),
    'country-or-region': ('152988005', ),
    'letter': ('219317028', ),
    'set': ('38727365', ),      # 套装名
    'quest-end': ('116521668', '168415844'),        # NPC对话，总结
    'quest-talk-long': ('3952276', '55049764', '200879108', '103224356',       # NPC
                        '115740052', '187173764',
                        '121487972', '204987124', '228103012', '232026500', '249936564', '256430276',    # 玩家
                        ),
    'color': ('208337109', ),
}

# category: (name_file_id, file1_id, file2_id, ...)
# 各 index 相同的条目有关联
file_id_of_array = {
    'achievement': ('12529189', '188155806', '172030117'),  # 成就名，描述，子目标
    'location-object': ('10860933', '129979412', '108566804'),   # 地点，地点的目标,目标完成，地点不译（完成后地图上标志变白）
    'quest-obj': ('7949764', '234743124', '144228340'),     # 目标，交任务的对话动作，交任务的动作
    'quest-talk-short': ('52420949', '66848564', '20958740', '205344756'),   # 任务名，NPC开场白，玩家回答，提示。任务名不译
}

# category 对应的中文名
category_names = {
    "achievement": "成就",
    "book": "书信汉化",
    "chat": "聊天",
    "color": "颜色",
    "country-or-region": "国家地区",
    "crown": "皇冠商店",
    "greeting": "NPC打招呼",
    "interact-action": "交互动作",
    "interact-win": "按E的非任务对话",
    "item": "物品",
    "item-type": "物品修饰",
    "journey": "任务日志",
    "letter": "信件",
    "loadscreen": "载入画面",
    "location-and-object": "可交互物和地名",
    "location-object": "地点及目标",
    "merchant-talk": "商人等对话",
    "more-desc": "其他描述",
    "more-ui": "其他界面相关",
    "mount": "坐骑宠物服装等",
    "npc-name": "人名怪名",
    "quest-end": "任务结束",
    "questitem": "任务物品",
    "quest-obj": "任务目标",
    "quest-talk-long": "任务长对话",
    "quest-talk-short": "任务短对话",
    "set": "套装名",
    "skill": "技能",
    "three-alliance": "三阵营描述",
    "tip": "提示帮助",
    "title": "人物称谓",
    "trap": "陷阱",
    "treasure-map": "藏宝图",
}
