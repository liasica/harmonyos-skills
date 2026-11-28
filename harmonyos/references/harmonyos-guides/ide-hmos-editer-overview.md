---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-editer-overview
title: 代码阅读
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码阅读
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:50+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:27182d0340239b3c8bfd3e7abf18191e099f0bb4c9f796fb0e41aa07c36dd152
---

鸿蒙电脑DevEco Studio支持使用多种语言进行应用/元服务的开发，包括ArkTS、JS和C/C++。在编写应用/元服务阶段，可以通过掌握代码编写的各种常用技巧，来提升编码效率。

## 代码高亮

支持对代码的关键字、运算符、字符串、类、标识符、注释等进行高亮显示。通过切换主题，代码高亮的颜色也会随之变化。开发者可以在**文件** **> 设置** **>** **应用程序 > 外观**中切换**主题**，当前支持**深色模式**和**浅色模式**两种，选择主题之后，代码会有不同的高亮显示效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/-XisCd1cRKKC44zWljoZvA/zh-cn_image_0000002791841212.png?HW-CC-KV=V1&HW-CC-Date=20261128T023449Z&HW-CC-Expire=31536000000&HW-CC-Sign=EAB482A21BF8BEC5CD458539BB9A0A07E2E16EE0C71F69FAE12BC4D3B08B2565)

## 代码跳转

支持对代码中引用的类、方法、参数、变量等名称跳转到定义处、实现处以及引用位置。

### 跳转到定义位置

在编辑器中，可以按住**Ctrl**键，鼠标单击代码中引用的类、方法、参数、变量等名称，会自动跳转到定义位置；也可以在名称处点击鼠标右键，在弹框中选择**转到** > **转到定义**（或单击快捷键**Ctrl+B**），跳转到定义位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/6S7SP6FUScKU9ewosLKP2A/zh-cn_image_0000002820721147.gif?HW-CC-KV=V1&HW-CC-Date=20261128T023449Z&HW-CC-Expire=31536000000&HW-CC-Sign=94202BEEFF072BDB79FA21A5DC20A05FB049CCC38D6537CBFF95C8281906CAEA "点击放大")

### 跳转到实现位置

在编辑器中，选中引用的类、方法、参数、变量等名称后单击鼠标右键，在弹窗中选择**转到 > 转到实现**（或使用快捷键**Ctrl+Alt+B**）跳转到实现位置 。若变量名有多个实现，在弹窗中可选择想要查看的实现位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/slbjALopSNenTNM8CpbfqA/zh-cn_image_0000002791841208.png?HW-CC-KV=V1&HW-CC-Date=20261128T023449Z&HW-CC-Expire=31536000000&HW-CC-Sign=36368F4C88D25800BC5B03DB866CD8712995287DF672AB09A764AB3C2B3CB6E9)

### 跳转到引用位置

在编辑器中，选中引用的类、方法、参数、变量等名称后单击鼠标右键，在弹框中选择**转到 >转到引用**（或使用快捷键**Ctrl+Shift+B**），可以跳转到变量被引用位置。若有多处引用，在弹窗中可选择想要查看的引用位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/Op4jAPv5Tx-JCUecG8syAA/zh-cn_image_0000002820681143.png?HW-CC-KV=V1&HW-CC-Date=20261128T023449Z&HW-CC-Expire=31536000000&HW-CC-Sign=2DEEA13CAFBEBE36CE0A561CD0B9839F9939EA9869F05C848B18B18E4B46E6D4 "点击放大")

## 跨语言跳转

支持在声明或引用了Native接口的文件中（如d.ts）跨语言跳转至其对应的C++函数，从而提升混合语言开发的开发效率。开发者可以选中接口名称单击右键，在弹出的菜单中选择**转到 >转到实现**（或使用快捷键**Ctrl+Alt+B**）实现跨语言跳转。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/6rNo6jlQSaCkppUv1zVSbQ/zh-cn_image_0000002820681149.png?HW-CC-KV=V1&HW-CC-Date=20261128T023449Z&HW-CC-Expire=31536000000&HW-CC-Sign=CE74F6E725E1B7BFE19A8BC28DCAA815ABDF174930D1294821B7BB7A5E20433C "点击放大")

## 代码格式化

代码格式化功能可以帮助开发者快速地调整和规范代码格式，提升代码的美观度和可读性。默认情况下，DevEco Studio已预置了代码格式化的规范，也可以个性化设置各个文件的格式化规范，设置方式如下：在**文件 >** **设置** **> 扩展**下，选择**ArkTS**/**JavaScript**/**Type****Script**，然后自定义格式化规范即可。

若想要快速对整个文件的代码进行格式化，可以点击鼠标右键，在弹框中选择**格式化文档**（或使用快捷键**Ctrl+Shift+L**） ；若想要对选定范围的代码进行格式化，可以选中代码并点击鼠标右键，在弹窗中选择**格式化选中内容**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/HuoHRbMmRQKW155dtUTZFQ/zh-cn_image_0000002820681141.png?HW-CC-KV=V1&HW-CC-Date=20261128T023449Z&HW-CC-Expire=31536000000&HW-CC-Sign=997C262252E32D512493F00E018D69D1E4CE9E041EB0E768D2A6A637807B5850 "点击放大")

## 代码折叠

单击编辑器左侧边栏的折叠和展开按钮对代码块进行快速折叠和展开操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/qEHKVJ6QQiKwnfH20NjjvQ/zh-cn_image_0000002820721149.gif?HW-CC-KV=V1&HW-CC-Date=20261128T023449Z&HW-CC-Expire=31536000000&HW-CC-Sign=58E0CF73CDB71D8B95BF4E00357DD5F20DCF927E87501439FA3BC8514C2B8C31 "点击放大")

## 代码快速注释

支持对选择的代码块进行快速注释，使用快捷键**Ctrl+/**进行快速注释，对于已注释的代码块，再次使用快捷键**Ctrl+/**取消注释。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/lWqPxg0bTqyb8oqYuOUkOQ/zh-cn_image_0000002791841214.gif?HW-CC-KV=V1&HW-CC-Date=20261128T023449Z&HW-CC-Expire=31536000000&HW-CC-Sign=E218255C388F084BE7C61FE91739DB3920E8ACA384F60075B448F9284FF8D8E3 "点击放大")

## 代码查找

### 在文件中查找

支持开发者在当前文件中快速查找目标代码，操作步骤如下：

1. 打开目标文件，使用快捷键**Ctrl+F**打开查找界面。
2. 输入需要查找的代码字符串，支持通过大小写匹配、全字符匹配或正则匹配缩小搜索范围。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/ZAzEfxdESLiCNctvKWqV-w/zh-cn_image_0000002820681151.png?HW-CC-KV=V1&HW-CC-Date=20261128T023449Z&HW-CC-Expire=31536000000&HW-CC-Sign=1DFECECBAE01044D933B80A0508B598205AC35F8F361BAFB25658EEE6276F85B)

**说明** 

点击搜索框左侧箭头（或使用快捷键Ctrl+R）展开查找界面，在上面输入框和下面输入框分别输入代码字符串和替换的字符串，点击替换逐个替换文件中字符串，点击替换全部替换文件中所有字符串。

### 在项目中查找

支持在整个项目中查找特定的文本或代码片段，操作步骤如下：

1. 在左侧菜单栏中点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/gWf-f7LlSfamMO6VC-l7XA/zh-cn_image_0000002792001178.png?HW-CC-KV=V1&HW-CC-Date=20261128T023449Z&HW-CC-Expire=31536000000&HW-CC-Sign=C091C29D0A633ACB0328B58A0398EA66FA489AB1F8723EF3BDC9E4E1B14E7E24 "点击放大")打开查找界面，在搜索框中输入查找内容后，编辑器会在项目中匹配并显示所有搜索结果，点击查找界面右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/6lN8ZeOGRgKslnEX7dl3ow/zh-cn_image_0000002820721155.png?HW-CC-KV=V1&HW-CC-Date=20261128T023449Z&HW-CC-Expire=31536000000&HW-CC-Sign=0F8A0C25A23229FBA125FBD14AE7FBC5E90F7B355083529019B03EFA19C75275 "点击放大")收起搜索结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/L4XCmXIDQI2IxnurL0J1rw/zh-cn_image_0000002791841206.gif?HW-CC-KV=V1&HW-CC-Date=20261128T023449Z&HW-CC-Expire=31536000000&HW-CC-Sign=847CBE71E135ED281A3C6F3C2FFFA51BF09BB6E1E96D705CDBB51F8BAC89A3F9)
2. 支持通过文件类型和搜索范围过滤搜索结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/Rbn6JzB-R9WixJ_pKZX4AA/zh-cn_image_0000002792001184.png?HW-CC-KV=V1&HW-CC-Date=20261128T023449Z&HW-CC-Expire=31536000000&HW-CC-Sign=E339C3361E3631207235636BB041D8D5748A2916EEC03D8BE085B83DD3786BD2)
3. 点击搜索框右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/RAET66XWTTm2f4QJwhX3dA/zh-cn_image_0000002820681147.png?HW-CC-KV=V1&HW-CC-Date=20261128T023449Z&HW-CC-Expire=31536000000&HW-CC-Sign=3888D4AB743471555283DCD3B7E07F929A3E39E4E98B65C742B1050447526D17)支持替换操作，选择**替换全部**替换所有匹配内容。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/YVzUMoT8R6i7yCYfTMMlSQ/zh-cn_image_0000002792001182.png?HW-CC-KV=V1&HW-CC-Date=20261128T023449Z&HW-CC-Expire=31536000000&HW-CC-Sign=A35BFD9BD66E09BC84B584B6E994653C706E076063B3ED427630F681B21601EF)

### 全局查找

支持文件名、符号、命令及文本的全局查找。通过连续点击**两次****Shift**快捷键，打开代码查找界面，在搜索框中输入需要查找内容，下方窗口实时展示搜索结果。单击查找的结果可以快速打开所在文件的位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/Cz7_v6clS-ueXxUaG6lNkQ/zh-cn_image_0000002820721145.png?HW-CC-KV=V1&HW-CC-Date=20261128T023449Z&HW-CC-Expire=31536000000&HW-CC-Sign=2835A4C0B8BEF6CD8FE67208057BDA69E5D35D2D7E20B9D22A7139605BE72A69)

## 函数注释生成

DevEco Studio支持在函数定义处，快速生成对应的注释。在函数定义的代码块前，输入**"****/\*\*****"+回车键**，快速生成注释信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/5hAsuT1WQ-q3SPU1A2WTBA/zh-cn_image_0000002792001180.gif?HW-CC-KV=V1&HW-CC-Date=20261128T023449Z&HW-CC-Expire=31536000000&HW-CC-Sign=DD0B3B80E5140BE1814427F090DB44DF082C12C15BDAB3994FF41E538D1CB562)

## 文件引用查找

DevEco Studio提供对文件或文件夹的查找引用，可以帮助开发者快速查看某个文件或文件夹被引用的位置，便于后续进行代码重构。

选中文件或文件夹，单击鼠标右键选择**查找用法**。在左侧搜索窗口查看文件被引用的位置，点击引用位置自动跳转到对应文件中。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/S_tWFBLLQjinEaTliM1b4w/zh-cn_image_0000002820681145.png?HW-CC-KV=V1&HW-CC-Date=20261128T023449Z&HW-CC-Expire=31536000000&HW-CC-Sign=AA563EDC6C136C15796C42F14512AF4E083DE94F67DE5414D8ECCB38D522FD14)

## 字体设置

编辑器支持开发者设置字体，选择**文件** **> 设置**(或使用快捷键Ctrl+Alt+S打开)，在设置界面点击**编辑器 > 字体**，设置字体大小、字体样式和制表符大小。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/2IG_MyuySaas_2FOCWMQQg/zh-cn_image_0000002791841210.png?HW-CC-KV=V1&HW-CC-Date=20261128T023449Z&HW-CC-Expire=31536000000&HW-CC-Sign=E28A29BFB7730E5DC5ED502F479FA893F1E3ECA6993C03C2D69A5806CFB02655)
