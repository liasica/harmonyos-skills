---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-editer-overview
title: 代码阅读
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码阅读
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:11+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:c5ebd0a0198eacc36e0e35aecff12ae97f030eb4d8828ec00dd085686bd80a3c
---

鸿蒙电脑DevEco Studio支持使用多种语言进行应用/元服务的开发，包括ArkTS、JS和C/C++。在编写应用/元服务阶段，可以通过掌握代码编写的各种常用技巧，来提升编码效率。

## 代码高亮

支持对代码的关键字、运算符、字符串、类、标识符、注释等进行高亮显示。通过切换主题，代码高亮的颜色也会随之变化。开发者可以在**文件** **> 设置** **>** **应用程序 > 外观**中切换**主题**，当前支持**深色模式**和**浅色模式**两种，选择主题之后，代码会有不同的高亮显示效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/YajvVo_tQVmCfhejDZBpoA/zh-cn_image_0000002810630841.png?HW-CC-KV=V1&HW-CC-Date=20261114T004910Z&HW-CC-Expire=31536000000&HW-CC-Sign=A698D946C9B95C54D7EBBD4241A747BF303ACC1F91731D6C4FDC246630A9941C)

## 代码跳转

支持对代码中引用的类、方法、参数、变量等名称跳转到定义处、实现处以及引用位置。

### 跳转到定义位置

在编辑器中，可以按住**Ctrl**键，鼠标单击代码中引用的类、方法、参数、变量等名称，会自动跳转到定义位置；也可以在名称处点击鼠标右键，在弹框中选择**转到** > **转到定义**（或单击快捷键**Ctrl+B**），跳转到定义位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/ur2P0fouQdSjwlO217q08Q/zh-cn_image_0000002781311354.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004910Z&HW-CC-Expire=31536000000&HW-CC-Sign=348708A64DFD6E9ACD5ACF55D7A8F09C579832EB43E01F8C74EFB17B4A0B898F "点击放大")

### 跳转到实现位置

在编辑器中，选中引用的类、方法、参数、变量等名称后单击鼠标右键，在弹窗中选择**转到 > 转到实现**（或使用快捷键**Ctrl+Alt+B**）跳转到实现位置 。若变量名有多个实现，在弹窗中可选择想要查看的实现位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/rNR_sS7GTSOGk4G_4yYfzw/zh-cn_image_0000002810750949.png?HW-CC-KV=V1&HW-CC-Date=20261114T004910Z&HW-CC-Expire=31536000000&HW-CC-Sign=C0E0B0D0429366965E85623C1165CB976A49A4E309BAE96F6F2E0B8F266456AF)

### 跳转到引用位置

在编辑器中，选中引用的类、方法、参数、变量等名称后单击鼠标右键，在弹框中选择**转到 >转到引用**（或使用快捷键**Ctrl+Shift+B**），可以跳转到变量被引用位置。若有多处引用，在弹窗中可选择想要查看的引用位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/MFWOtlmtShanKRb77I6ugw/zh-cn_image_0000002810750935.png?HW-CC-KV=V1&HW-CC-Date=20261114T004910Z&HW-CC-Expire=31536000000&HW-CC-Sign=6F62395759AD4D72E0BB751F6D719383849C26F7F61F84FD7036F69B14E41FEB "点击放大")

## 跨语言跳转

支持在声明或引用了Native接口的文件中（如d.ts）跨语言跳转至其对应的C++函数，从而提升混合语言开发的开发效率。开发者可以选中接口名称单击右键，在弹出的菜单中选择**转到 >转到实现**（或使用快捷键**Ctrl+Alt+B**）实现跨语言跳转。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/x_QQtxXxQxOCTWtq33G8DA/zh-cn_image_0000002781471286.png?HW-CC-KV=V1&HW-CC-Date=20261114T004910Z&HW-CC-Expire=31536000000&HW-CC-Sign=B02B446FBDC18B9F9821B10755478834B15D19D2BD4FE010551883EB52D7AD0A "点击放大")

## 代码格式化

代码格式化功能可以帮助开发者快速地调整和规范代码格式，提升代码的美观度和可读性。默认情况下，DevEco Studio已预置了代码格式化的规范，也可以个性化设置各个文件的格式化规范，设置方式如下：在**文件 >** **设置** **> 扩展**下，选择**ArkTS**/**JavaScript**/**Type****Script**，然后自定义格式化规范即可。

若想要快速对整个文件的代码进行格式化，可以点击鼠标右键，在弹框中选择**格式化文档**（或使用快捷键**Ctrl+Shift+L**） ；若想要对选定范围的代码进行格式化，可以选中代码并点击鼠标右键，在弹窗中选择**格式化选中内容**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/C6xmBCKET8mv5pN_B9ToWw/zh-cn_image_0000002810750943.png?HW-CC-KV=V1&HW-CC-Date=20261114T004910Z&HW-CC-Expire=31536000000&HW-CC-Sign=1C9FA77D875AD3593B2E4E03C5A9C7E2C075FAC6471024CB2DE2C8EE28B2F0C5 "点击放大")

## 代码折叠

单击编辑器左侧边栏的折叠和展开按钮对代码块进行快速折叠和展开操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/seS3cLPdRKKKkno0mE4JTw/zh-cn_image_0000002810630833.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004910Z&HW-CC-Expire=31536000000&HW-CC-Sign=967F1C382A63EEC6EB412252351F89D9293B568883F671E2A4AE1CF1DA794BA4 "点击放大")

## 代码快速注释

支持对选择的代码块进行快速注释，使用快捷键**Ctrl+/**进行快速注释，对于已注释的代码块，再次使用快捷键**Ctrl+/**取消注释。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/ht0RKu_-Q4WMLjqK6Grwnw/zh-cn_image_0000002781471288.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004910Z&HW-CC-Expire=31536000000&HW-CC-Sign=F24FFDB1CA3AF2A38FD82974A0ACFFF7BB85078551B32A6C2ACEF15231C18112 "点击放大")

## 代码查找

### 在文件中查找

支持开发者在当前文件中快速查找目标代码，操作步骤如下：

1. 打开目标文件，使用快捷键**Ctrl+F**打开查找界面。
2. 输入需要查找的代码字符串，支持通过大小写匹配、全字符匹配或正则匹配缩小搜索范围。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/9xE4tDLZTKaRya8juszLaQ/zh-cn_image_0000002781471290.png?HW-CC-KV=V1&HW-CC-Date=20261114T004910Z&HW-CC-Expire=31536000000&HW-CC-Sign=6DEC6FEDD6A476C42BDA6596CAC84814CC26D5B8AE22FC3E088E8C70BBD37DB1)

**说明** 

点击搜索框左侧箭头（或使用快捷键Ctrl+R）展开查找界面，在上面输入框和下面输入框分别输入代码字符串和替换的字符串，点击替换逐个替换文件中字符串，点击替换全部替换文件中所有字符串。

### 在项目中查找

支持在整个项目中查找特定的文本或代码片段，操作步骤如下：

1. 在左侧菜单栏中点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/oAr6NzxdTluc4axCXq4IzQ/zh-cn_image_0000002810750941.png?HW-CC-KV=V1&HW-CC-Date=20261114T004910Z&HW-CC-Expire=31536000000&HW-CC-Sign=B0AC598A1A1350A74E0CCEBBAF56638E3AB44CC4C400040DB84F105F1E42DDDC "点击放大")打开查找界面，在搜索框中输入查找内容后，编辑器会在项目中匹配并显示所有搜索结果，点击查找界面右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/tMxER5VIQ--WVSGZ86wmnA/zh-cn_image_0000002781471292.png?HW-CC-KV=V1&HW-CC-Date=20261114T004910Z&HW-CC-Expire=31536000000&HW-CC-Sign=B2F9EAD440D4A410FEF8BEC3E77D21FDDDBEF20D3DAA7EAB3728CE17442EC9A6 "点击放大")收起搜索结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/iMMI8kv9T3mtjcIk8BnH2w/zh-cn_image_0000002810750945.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004910Z&HW-CC-Expire=31536000000&HW-CC-Sign=A8FF12B79C248B8D1B8B9C86FE0F6376660F74F735C7FDB2505444ED687AECD9)
2. 支持通过文件类型和搜索范围过滤搜索结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/Z_ZCWqiUSnS0LyY9Ia_yCw/zh-cn_image_0000002781311350.png?HW-CC-KV=V1&HW-CC-Date=20261114T004910Z&HW-CC-Expire=31536000000&HW-CC-Sign=128319FCFE49C5889A30E939BCEF136DEEA2A8E5CF93BD41986B0F51550BC0B3)
3. 点击搜索框右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/okxZPQ8NQumcpKKXDHZVHA/zh-cn_image_0000002810630831.png?HW-CC-KV=V1&HW-CC-Date=20261114T004910Z&HW-CC-Expire=31536000000&HW-CC-Sign=41B59902C65968571E4C07E6072387447AB4E1C57C234DBB9AF0A75642FFFCB8)支持替换操作，选择**替换全部**替换所有匹配内容。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/3UgbPAbTRJ2rRJByiILR-w/zh-cn_image_0000002781311342.png?HW-CC-KV=V1&HW-CC-Date=20261114T004910Z&HW-CC-Expire=31536000000&HW-CC-Sign=058ACDC9150209F54A80871DF565202CC11EE32C3EF359FF645C09211865C7D5)

### 全局查找

支持文件名、符号、命令及文本的全局查找。通过连续点击**两次****Shift**快捷键，打开代码查找界面，在搜索框中输入需要查找内容，下方窗口实时展示搜索结果。单击查找的结果可以快速打开所在文件的位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/AyKlnrVlSlWeIsAuWY8-EQ/zh-cn_image_0000002810750955.png?HW-CC-KV=V1&HW-CC-Date=20261114T004910Z&HW-CC-Expire=31536000000&HW-CC-Sign=CF7FDAEE68442CEB5C69630C64DE8EBB55185DEB38BBD3423AADBE4491432EFB)

## 函数注释生成

DevEco Studio支持在函数定义处，快速生成对应的注释。在函数定义的代码块前，输入**"****/\*\*****"+回车键**，快速生成注释信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/SQMMlUf5SXy89M3pvY4hbQ/zh-cn_image_0000002810630839.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004910Z&HW-CC-Expire=31536000000&HW-CC-Sign=3B07F94855FB361839737795CADC77585FEEA6F682A163C1869864AF747A16B0)

## 文件引用查找

DevEco Studio提供对文件或文件夹的查找引用，可以帮助开发者快速查看某个文件或文件夹被引用的位置，便于后续进行代码重构。

选中文件或文件夹，单击鼠标右键选择**查找用法**。在左侧搜索窗口查看文件被引用的位置，点击引用位置自动跳转到对应文件中。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/OU0wNPmARoWIRje2canLkw/zh-cn_image_0000002810630835.png?HW-CC-KV=V1&HW-CC-Date=20261114T004910Z&HW-CC-Expire=31536000000&HW-CC-Sign=8812E6D337AEF6627DE85FC67FA5715AB4CBDD735C4F66A33B0805B8B1CDE0E2)

## 字体设置

编辑器支持开发者设置字体，选择**文件** **> 设置**(或使用快捷键Ctrl+Alt+S打开)，在设置界面点击**编辑器 > 字体**，设置字体大小、字体样式和制表符大小。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/Z8DwP49GRFezmTvtp7WHnQ/zh-cn_image_0000002781311340.png?HW-CC-KV=V1&HW-CC-Date=20261114T004910Z&HW-CC-Expire=31536000000&HW-CC-Sign=3457108A444A5DC78E6AF50C1AF15BC71E4237599C7534FD01BD994A2A23D5F0)
