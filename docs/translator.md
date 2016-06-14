## 翻译方法

### 一、文本翻译

##### UI翻译
编辑 `translation/zh_translate.txt`。
直接把译文另起一行写在以 "SafeAddString" 开头的原文后即可。
例如：

```
SafeAddString(SI_GAME_MENU_LOGOUT, "Log Out", 0)
登出
SafeAddString(SI_GAME_MENU_QUIT, "Quit", 0)
退出
SafeAddString(SI_GAME_MENU_RESUME, "Resume", 0)
SafeAddString(SI_GAME_MENU_SETTINGS, "Settings", 0)
```

##### 对话翻译
编辑 zh.lang.csv 文件，待续

### 二、生成 .str 文件

在 `/scripts` 下运行 `convert_txt_to_str`

```bash
python convert_txt_to_str.py
```

### 三、生成 zh.lang 文件

使用 EsoExtractData 软件，将 `zh.lang.csv` 转换成 `zh.lang`。

### 四、打包发布

需要打包以下内容：
- esoui/lang/zh_client.str
- esoui/lang/zh_pregame.str
- fonts, 详见 release
- gamedata/lang/zh.lang, 详见 release