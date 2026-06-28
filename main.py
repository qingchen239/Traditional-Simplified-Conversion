import opencc
from tqdm import tqdm

default_configurations = [
    "s2t",
    "t2s",
    "s2tw",
    "tw2s",
    "s2hk",
    "hk2s",
    "t2tw",
    "hk2t",
    "t2hk",
    "t2jp",
    "jp2t",
    "tw2t",
]
additional_configurations = ["s2ct", "s2qt"]
other_configurations = ["qt2ct"]

file1_name = input("Enter Source File Name: ")
file2_name = input("Enter Target File Name: ")
conversion_type = input("Enter Conversion Type: ")
while (
    conversion_type not in default_configurations
    and conversion_type not in additional_configurations
    and conversion_type not in other_configurations
):
    conversion_type = input(
        "Re-enter Conversion Type "
        + str(default_configurations + additional_configurations + other_configurations)
        + ": "
    )

file1 = open(file1_name, mode="r", encoding="utf-8")
file2 = open(file2_name, mode="w", encoding="utf-8")
converter = opencc.OpenCC(
    (conversion_type if conversion_type in default_configurations else "s2t") + ".json"
)

for line in tqdm(file1):
    if conversion_type in default_configurations + additional_configurations:
        line = converter.convert(line)

    if conversion_type in default_configurations + additional_configurations:
        line = line.replace("喫", "吃")
        line = line.replace("牀", "床")
        line = line.replace("箇", "個")
        line = line.replace("鍼", "針")
        line = line.replace("鮎", "鯰")
        line = line.replace("麪", "麵")
        line = line.replace("臺", "台")
        line = line.replace("週", "周")

    if conversion_type in other_configurations + ["s2ct"]:
        line = line.replace("羣", "群")
        line = line.replace("峯", "峰")
        line = line.replace("啟", "啓")
        # line = line.replace("裡", "裏")
        # line = line.replace("祕", "秘")
        # line = line.replace("稜", "棱")
        # line = line.replace("汙", "污")
        # line = line.replace("覈", "核")

        # line = line.replace("佔", "占")
        # line = line.replace("週", "周")

        line = line.replace("為", "爲")
        line = line.replace("偽", "僞")
        line = line.replace("媯", "嬀")
        line = line.replace("溈", "潙")
        line = line.replace("蒍", "蔿")
        
        line = line.replace("丟", "丢")
        line = line.replace("戶", "户")
        line = line.replace("奧", "奥")
        line = line.replace("粵", "粤")
        line = line.replace("麼", "麽")
        line = line.replace("產", "産")
        line = line.replace("虛", "虚")
        line = line.replace("囪", "囱")
        line = line.replace("勻", "匀")

        line = line.replace("眾", "衆")
        line = line.replace("潀", "潨")
        
        line = line.replace("沒", "没")
        line = line.replace("別", "别")
        # line = line.replace("夠", "够")
        # line = line.replace("拋", "抛")
        # line = line.replace("隨", "随")
        # line = line.replace("線", "綫")
        line = line.replace("強", "强")
        line = line.replace("絕", "絶")
        # line = line.replace("撐", "撑")
        # line = line.replace("潛", "潜")
        # line = line.replace("鉤", "鈎")
        line = line.replace("丟", "丢")
        
        line = line.replace("剎", "刹")

        line = line.replace("兌", "兑")
        line = line.replace("說", "説")
        line = line.replace("脫", "脱")
        line = line.replace("蛻", "蜕")
        line = line.replace("閱", "閲")
        line = line.replace("悅", "悦")
        line = line.replace("銳", "鋭")
        line = line.replace("稅", "税")
        line = line.replace("梲", "棁")
        line = line.replace("涗", "涚")
        line = line.replace("挩", "捝")
        line = line.replace("敓", "敚")

        line = line.replace("爭", "争")
        line = line.replace("净", "淨")
        line = line.replace("睜", "睁")
        line = line.replace("箏", "筝")
        line = line.replace("靜", "静")
        line = line.replace("掙", "挣")
        line = line.replace("猙", "狰")
        line = line.replace("崢", "峥")

        line = line.replace("奐", "奂")
        line = line.replace("換", "换")
        line = line.replace("喚", "唤")
        line = line.replace("煥", "焕")
        line = line.replace("渙", "涣")
        line = line.replace("瘓", "痪")

        line = line.replace("內", "内")
        line = line.replace("吶", "呐")

        # line = line.replace("減", "减")
        # line = line.replace("況", "况")
        # line = line.replace("沖", "冲")
        # line = line.replace("決", "决")

        line = line.replace("黃", "黄")
        line = line.replace("橫", "横")

        # line = line.replace("卻", "却")
        # line = line.replace("腳", "脚")

        line = line.replace("禿", "秃")
        line = line.replace("頹", "頽")

        line = line.replace("彔", "录")
        line = line.replace("綠", "緑")
        line = line.replace("錄", "録")
        line = line.replace("祿", "禄")
        line = line.replace("剝", "剥")
        line = line.replace("淥", "渌")

        line = line.replace("遙", "遥")
        line = line.replace("謠", "谣")

        line = line.replace("溫", "温")
        line = line.replace("薀", "蕰")
        line = line.replace("蘊", "藴")
        line = line.replace("媼", "媪")
        line = line.replace("膃", "腽")
        line = line.replace("膃", "腽")
        line = line.replace("氳", "氲")
        line = line.replace("慍", "愠")
        line = line.replace("榲", "榅")
        line = line.replace("轀", "輼")
        line = line.replace("鰮", "鰛")
        line = line.replace("搵", "揾")
        line = line.replace("縕", "緼")
        line = line.replace("縕", "緼")
        line = line.replace("榲", "榅")

        line = line.replace("呂", "吕")
        line = line.replace("侶", "侣")
        line = line.replace("宮", "宫")
        
        line = line.replace("冊", "册")
        line = line.replace("刪", "删")
        line = line.replace("姍", "姗")
        line = line.replace("柵", "栅")
        
        # line = line.replace("雞", "鷄")
        
        line = line.replace("毀", "毁")

    if conversion_type == "s2qt":
        line = line.replace("僞", "偽")
        line = line.replace("啓", "啟")
        line = line.replace("喫", "吃")
        line = line.replace("嫺", "嫻")
        line = line.replace("嬀", "媯")
        line = line.replace("峯", "峰")
        line = line.replace("幺", "么")
        line = line.replace("擡", "抬")
        line = line.replace("棱", "稜")
        # line = line.replace("檐", "簷")
        # line = line.replace("污", "汙")
        # line = line.replace("泄", "洩")
        line = line.replace("潙", "溈")
        line = line.replace("潨", "潀")
        line = line.replace("爲", "為")
        line = line.replace("牀", "床")
        line = line.replace("痹", "痺")
        line = line.replace("癡", "痴")
        line = line.replace("皁", "皂")
        # line = line.replace("着", "著")
        line = line.replace("睾", "睪")
        line = line.replace("祕", "秘")
        line = line.replace("竈", "灶")
        line = line.replace("糉", "粽")
        line = line.replace("繮", "韁")
        line = line.replace("纔", "才")
        line = line.replace("羣", "群")
        line = line.replace("脣", "唇")
        line = line.replace("蔘", "參")
        line = line.replace("蔿", "蒍")
        line = line.replace("衆", "眾")
        line = line.replace("裏", "裡")
        # line = line.replace("覈", "核")
        line = line.replace("踊", "踴")
        line = line.replace("鉢", "缽")
        line = line.replace("鍼", "針")
        line = line.replace("鮎", "鯰")
        line = line.replace("麪", "麵")
        line = line.replace("齶", "顎")
        line = line.replace("臺", "台")

    file2.write(line)

file1.close()
file2.close()
