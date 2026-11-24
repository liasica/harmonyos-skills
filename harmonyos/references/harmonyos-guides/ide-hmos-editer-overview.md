---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-editer-overview
title: 代码阅读
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码阅读
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:41+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:5064ecdde3770b7c46c0d2048b8d2ec4e90d194a5159667ba21a191e0e0a46af
---

鸿蒙电脑DevEco Studio支持使用多种语言进行应用/元服务的开发，包括ArkTS、JS和C/C++。在编写应用/元服务阶段，可以通过掌握代码编写的各种常用技巧，来提升编码效率。

## 代码高亮

支持对代码的关键字、运算符、字符串、类、标识符、注释等进行高亮显示。通过切换主题，代码高亮的颜色也会随之变化。开发者可以在**文件** **> 设置** **>** **应用程序 > 外观**中切换**主题**，当前支持**深色模式**和**浅色模式**两种，选择主题之后，代码会有不同的高亮显示效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/_lPlJFrqQI6nvAsQBUwSHg/zh-cn_image_0000002791841212.png?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=0628688B45BDD15AF35EFC3D89A50DC063EBD09CEC6B895F48F691CEBFD9FF05)

## 代码跳转

支持对代码中引用的类、方法、参数、变量等名称跳转到定义处、实现处以及引用位置。

### 跳转到定义位置

在编辑器中，可以按住**Ctrl**键，鼠标单击代码中引用的类、方法、参数、变量等名称，会自动跳转到定义位置；也可以在名称处点击鼠标右键，在弹框中选择**转到** > **转到定义**（或单击快捷键**Ctrl+B**），跳转到定义位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/ihE0c59XQcaU5NEjNbAbmQ/zh-cn_image_0000002820721147.gif?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=658DB21B96C713EC548B35289DB1ABE101E549C595C01E93290764EB7D0C7102 "点击放大")

### 跳转到实现位置

在编辑器中，选中引用的类、方法、参数、变量等名称后单击鼠标右键，在弹窗中选择**转到 > 转到实现**（或使用快捷键**Ctrl+Alt+B**）跳转到实现位置 。若变量名有多个实现，在弹窗中可选择想要查看的实现位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/x31E42ScTkycpBM9U7w9Ig/zh-cn_image_0000002791841208.png?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=27C39A6FA23C98ED69D93A6A196743636BD0BFA1BB9D2DE4896F5AB09CEB4D0D)

### 跳转到引用位置

在编辑器中，选中引用的类、方法、参数、变量等名称后单击鼠标右键，在弹框中选择**转到 >转到引用**（或使用快捷键**Ctrl+Shift+B**），可以跳转到变量被引用位置。若有多处引用，在弹窗中可选择想要查看的引用位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/qqdSbIgZT1KX8B1KhhZTJA/zh-cn_image_0000002820681143.png?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=EE64CE23EE9603F5CFB0E72311F06D853CA98CE427DDF661E4FD9E23A326E6D6 "点击放大")

## 跨语言跳转

支持在声明或引用了Native接口的文件中（如d.ts）跨语言跳转至其对应的C++函数，从而提升混合语言开发的开发效率。开发者可以选中接口名称单击右键，在弹出的菜单中选择**转到 >转到实现**（或使用快捷键**Ctrl+Alt+B**）实现跨语言跳转。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/BhV9hCy_RPalNxLDVKX7Xw/zh-cn_image_0000002820681149.png?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=87531FB0D2EE71373BC119DF6F8328E9ED61642A891C071C72778978802CBE18 "点击放大")

## 代码格式化

代码格式化功能可以帮助开发者快速地调整和规范代码格式，提升代码的美观度和可读性。默认情况下，DevEco Studio已预置了代码格式化的规范，也可以个性化设置各个文件的格式化规范，设置方式如下：在**文件 >** **设置** **> 扩展**下，选择**ArkTS**/**JavaScript**/**Type****Script**，然后自定义格式化规范即可。

若想要快速对整个文件的代码进行格式化，可以点击鼠标右键，在弹框中选择**格式化文档**（或使用快捷键**Ctrl+Shift+L**） ；若想要对选定范围的代码进行格式化，可以选中代码并点击鼠标右键，在弹窗中选择**格式化选中内容**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/jP77CvR5Q_OhJkEFr-u7bg/zh-cn_image_0000002820681141.png?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=C08171CB3BC3B81744A4B5E8932B1D10EF395593EF29BBF5E0770680C1D54C38 "点击放大")

## 代码折叠

单击编辑器左侧边栏的折叠和展开按钮对代码块进行快速折叠和展开操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/meJ_TJAjQIiAoD6hdMJoKw/zh-cn_image_0000002820721149.gif?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=D40733873DE6C574ACF8CDCF47E0E850B51592FC7256B284AE297442D2A39132 "点击放大")

## 代码快速注释

支持对选择的代码块进行快速注释，使用快捷键**Ctrl+/**进行快速注释，对于已注释的代码块，再次使用快捷键**Ctrl+/**取消注释。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/_d6xTqAATHG3hAu5THH1pg/zh-cn_image_0000002791841214.gif?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=878E393E7566D9FCAE6B6F63FF5E71AAC97729416349B40FF80A24CA56DE86AD "点击放大")

## 代码查找

### 在文件中查找

支持开发者在当前文件中快速查找目标代码，操作步骤如下：

1. 打开目标文件，使用快捷键**Ctrl+F**打开查找界面。
2. 输入需要查找的代码字符串，支持通过大小写匹配、全字符匹配或正则匹配缩小搜索范围。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/79NUbDekRviVSUdbKfYS5Q/zh-cn_image_0000002820681151.png?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=F09DC7C434B9A9691E63418D099AC1EEAA7279BCF41942B555627B18AEB8C533)

**说明** 

点击搜索框左侧箭头（或使用快捷键Ctrl+R）展开查找界面，在上面输入框和下面输入框分别输入代码字符串和替换的字符串，点击替换逐个替换文件中字符串，点击替换全部替换文件中所有字符串。

### 在项目中查找

支持在整个项目中查找特定的文本或代码片段，操作步骤如下：

1. 在左侧菜单栏中点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/XiqiAtIYSuCIVMh8sijMZw/zh-cn_image_0000002792001178.png?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=575232E5940669CDCA66C99EE23524C13D18272AA8769532511EDFF0D018BACD "点击放大")打开查找界面，在搜索框中输入查找内容后，编辑器会在项目中匹配并显示所有搜索结果，点击查找界面右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/JaeL40blQZyR_E3XshbdZg/zh-cn_image_0000002820721155.png?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=A937FAFA8FFCE000612E9F8562542E294DF6D30DD587CB3366890774E35E5FD6 "点击放大")收起搜索结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/6_j1aJeeQLOqF_TPwRzqNQ/zh-cn_image_0000002791841206.gif?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=CA64E1CD0B2C432512EE9CADBE15C139E653414A7071C7D0F37A5CAE56B56E11)
2. 支持通过文件类型和搜索范围过滤搜索结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/DMq1x6stT9qnNKxU3so1jQ/zh-cn_image_0000002792001184.png?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=638F40CB2A8848ACD859E208E9C89B013257D938C991C74CE993224F7ACA128B)
3. 点击搜索框右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/dslIVhQkSqSw77RLMzmGXA/zh-cn_image_0000002820681147.png?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=7130110AE99A988E1CA0ADB0A5885BA79596DD0F6292DAC3478BECF2684329C1)支持替换操作，选择**替换全部**替换所有匹配内容。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/G80VzLQ_TouNanTEmgyK0A/zh-cn_image_0000002792001182.png?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=05C4D31217BE5E181BFF49615A0790035593DED84352C584BDBBB9478E19683B)

### 全局查找

支持文件名、符号、命令及文本的全局查找。通过连续点击**两次****Shift**快捷键，打开代码查找界面，在搜索框中输入需要查找内容，下方窗口实时展示搜索结果。单击查找的结果可以快速打开所在文件的位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/c8l8FV4aRuup5H4U8QF0Mg/zh-cn_image_0000002820721145.png?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=2C731E6F9D675809C2F00C1AEA2426125D05F5DE0BAE2810B8F023D3CC9A1142)

## 函数注释生成

DevEco Studio支持在函数定义处，快速生成对应的注释。在函数定义的代码块前，输入**"****/\*\*****"+回车键**，快速生成注释信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/GKFK6xsISveLrhxLWgxyAQ/zh-cn_image_0000002792001180.gif?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=D7D1A0658ECE3455E8C7B1E5B374508C96EC71B9C9327DE3C7719BF8B3F26DC2)

## 文件引用查找

DevEco Studio提供对文件或文件夹的查找引用，可以帮助开发者快速查看某个文件或文件夹被引用的位置，便于后续进行代码重构。

选中文件或文件夹，单击鼠标右键选择**查找用法**。在左侧搜索窗口查看文件被引用的位置，点击引用位置自动跳转到对应文件中。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/N__WQWeCTgGJYb75OunQkg/zh-cn_image_0000002820681145.png?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=8F41B4E92510A28149CFD1C85CF8CA4672D3C5BB559ACD049F9AECEAD062118D)

## 字体设置

编辑器支持开发者设置字体，选择**文件** **> 设置**(或使用快捷键Ctrl+Alt+S打开)，在设置界面点击**编辑器 > 字体**，设置字体大小、字体样式和制表符大小。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/MB87uS-mTLuzkYct3QyDAw/zh-cn_image_0000002791841210.png?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=3BF20F1B74A0FF31141B2DE221F6CECD231215EBC94531516058213E091BEF68)
