---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-editer-overview
title: 代码阅读
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码阅读
category: harmonyos-guides
scraped_at: 2026-10-11T07:23:16+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:51635fd6787a9ef585bac3a3ee8362f9395ba4ae4e1fdb425ad0fc231272594c
---

鸿蒙电脑DevEco Studio支持使用多种语言进行应用/元服务的开发，包括ArkTS、JS和C/C++。在编写应用/元服务阶段，可以通过掌握代码编写的各种常用技巧，来提升编码效率。

## 代码高亮

支持对代码的关键字、运算符、字符串、类、标识符、注释等进行高亮显示。通过切换主题，代码高亮的颜色也会随之变化。开发者可以在**文件** **> 设置** **>** **应用程序 > 外观**中切换**主题**，当前支持**深色模式**和**浅色模式**两种，选择主题之后，代码会有不同的高亮显示效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/jhNFaWOxQT-Z6OsSoCZG7Q/zh-cn_image_0000002779608835.png)

## 代码跳转

支持对代码中引用的类、方法、参数、变量等名称跳转到定义处、实现处以及引用位置。

### 跳转到定义位置

在编辑器中，可以按住**Ctrl**键，鼠标单击代码中引用的类、方法、参数、变量等名称，会自动跳转到定义位置；也可以在名称处点击鼠标右键，在弹框中选择**转到** > **转到定义**（或单击快捷键**Ctrl+B**），跳转到定义位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/5hQ7wwLeSxakbdv0vawP_w/zh-cn_image_0000002750009920.gif "点击放大")

### 跳转到实现位置

在编辑器中，选中引用的类、方法、参数、变量等名称后单击鼠标右键，在弹窗中选择**转到 > 转到实现**（或使用快捷键**Ctrl+Alt+B**）跳转到实现位置 。若变量名有多个实现，在弹窗中可选择想要查看的实现位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/lstjbHlvTv6Q7gJf5RkLog/zh-cn_image_0000002750009916.png)

### 跳转到引用位置

在编辑器中，选中引用的类、方法、参数、变量等名称后单击鼠标右键，在弹框中选择**转到 >转到引用**（或使用快捷键**Ctrl+Shift+B**），可以跳转到变量被引用位置。若有多处引用，在弹窗中可选择想要查看的引用位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/PtaexLlvQaO9Te91NVdODQ/zh-cn_image_0000002750009904.png "点击放大")

## 跨语言跳转

支持在声明或引用了Native接口的文件中（如d.ts）跨语言跳转至其对应的C++函数，从而提升混合语言开发的开发效率。开发者可以选中接口名称单击右键，在弹出的菜单中选择**转到 >转到实现**（或使用快捷键**Ctrl+Alt+B**）实现跨语言跳转。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/U8bMcoBaSTiaziIKMs8FJA/zh-cn_image_0000002750009914.png "点击放大")

## 代码格式化

代码格式化功能可以帮助开发者快速地调整和规范代码格式，提升代码的美观度和可读性。默认情况下，DevEco Studio已预置了代码格式化的规范，也可以个性化设置各个文件的格式化规范，设置方式如下：在**文件 >** **设置** **> 扩展**下，选择**ArkTS**/**JavaScript**/**Type****Script**，然后自定义格式化规范即可。

若想要快速对整个文件的代码进行格式化，可以点击鼠标右键，在弹框中选择**格式化文档**（或使用快捷键**Ctrl+Shift+L**） ；若想要对选定范围的代码进行格式化，可以选中代码并点击鼠标右键，在弹窗中选择**格式化选中内容**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/C2kfNJnXRRyqDImqJOh7Ig/zh-cn_image_0000002779608825.png "点击放大")

## 代码折叠

单击编辑器左侧边栏的折叠和展开按钮对代码块进行快速折叠和展开操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/vpcM8d7ySku2xK_rvHQ2nw/zh-cn_image_0000002750169802.gif "点击放大")

## 代码快速注释

支持对选择的代码块进行快速注释，使用快捷键**Ctrl+/**进行快速注释，对于已注释的代码块，再次使用快捷键**Ctrl+/**取消注释。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/5I4cdGq9QdWJfvCm4GrysA/zh-cn_image_0000002750169812.gif "点击放大")

## 代码查找

### 在文件中查找

支持开发者在当前文件中快速查找目标代码，操作步骤如下：

1. 打开目标文件，使用快捷键**Ctrl+F**打开查找界面。
2. 输入需要查找的代码字符串，支持通过大小写匹配、全字符匹配或正则匹配缩小搜索范围。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/hZbBAlxwSwaKrQxTD1s4ag/zh-cn_image_0000002779608837.png)

**说明** 

点击搜索框左侧箭头（或使用快捷键Ctrl+R）展开查找界面，在上面输入框和下面输入框分别输入代码字符串和替换的字符串，点击替换逐个替换文件中字符串，点击替换全部替换文件中所有字符串。

### 在项目中查找

支持在整个项目中查找特定的文本或代码片段，操作步骤如下：

1. 在左侧菜单栏中点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/8Y5wwpTLR1a1Dm2irs3qsw/zh-cn_image_0000002750009906.png "点击放大")打开查找界面，在搜索框中输入查找内容后，编辑器会在项目中匹配并显示所有搜索结果，点击查找界面右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/eC-UNd8hRB-S056c7u9ktQ/zh-cn_image_0000002750009922.png "点击放大")收起搜索结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/R6jJWPMyQvC4VoYi97uXww/zh-cn_image_0000002750169806.gif)
2. 支持通过文件类型和搜索范围过滤搜索结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/hpMUbrmJSIGWwNvtfk1jgg/zh-cn_image_0000002779608829.png)
3. 点击搜索框右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/PqDNioUcTd6neGxDWcT45Q/zh-cn_image_0000002750169800.png)支持替换操作，选择**替换全部**替换所有匹配内容。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/Qy7aHVxjSBK9Kf8XWt4arQ/zh-cn_image_0000002779608821.png)

### 全局查找

支持文件名、符号、命令及文本的全局查找。通过连续点击**两次****Shift**快捷键，打开代码查找界面，在搜索框中输入需要查找内容，下方窗口实时展示搜索结果。单击查找的结果可以快速打开所在文件的位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/4SRpxBY6SPGBFOdWD-4iOw/zh-cn_image_0000002779608839.png)

## 函数注释生成

DevEco Studio支持在函数定义处，快速生成对应的注释。在函数定义的代码块前，输入**"****/\*\*****"+回车键**，快速生成注释信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/zaZYSU6dR7yxajDOFatnqg/zh-cn_image_0000002779608831.gif)

## 文件引用查找

DevEco Studio提供对文件或文件夹的查找引用，可以帮助开发者快速查看某个文件或文件夹被引用的位置，便于后续进行代码重构。

选中文件或文件夹，单击鼠标右键选择**查找用法**。在左侧搜索窗口查看文件被引用的位置，点击引用位置自动跳转到对应文件中。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/1bWR7m1kR2iwuENQMcobrQ/zh-cn_image_0000002779728973.png)

## 字体设置

编辑器支持开发者设置字体，选择**文件** **> 设置**(或使用快捷键Ctrl+Alt+S打开)，在设置界面点击**编辑器 > 字体**，设置字体大小、字体样式和制表符大小。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/bEqQTYQZR6GQgxpzJyBCrA/zh-cn_image_0000002779728967.png)
