---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-editer-overview
title: 代码阅读
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码阅读
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:ee1417fbc411fe5ada103bc5398a81766d2bed6e9d0504523f5a134d2fb34524
---

鸿蒙电脑DevEco Studio支持使用多种语言进行应用/元服务的开发，包括ArkTS、JS和C/C++。在编写应用/元服务阶段，可以通过掌握代码编写的各种常用技巧，来提升编码效率。

## 代码高亮

支持对代码的关键字、运算符、字符串、类、标识符、注释等进行高亮显示。通过切换主题，代码高亮的颜色也会随之变化。开发者可以在**文件** **> 设置** **>** **应用程序 > 外观**中切换**主题**，当前支持**深色模式**和**浅色模式**两种，选择主题之后，代码会有不同的高亮显示效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/Y0YtVq0FT82ehOHKN6HT1Q/zh-cn_image_0000002810630841.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=87EE1A863696DF8C2A7357E3EE7DD6EF11564973C14BCFC43004F670662CA98B)

## 代码跳转

支持对代码中引用的类、方法、参数、变量等名称跳转到定义处、实现处以及引用位置。

### 跳转到定义位置

在编辑器中，可以按住**Ctrl**键，鼠标单击代码中引用的类、方法、参数、变量等名称，会自动跳转到定义位置；也可以在名称处点击鼠标右键，在弹框中选择**转到** > **转到定义**（或单击快捷键**Ctrl+B**），跳转到定义位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/hGKcYTi9Qaq9fVw5NTgkpg/zh-cn_image_0000002781311354.gif?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=628F0754835BB2DD6A4368810600D6DCB57D9E75169B5B6F673207E60766089B "点击放大")

### 跳转到实现位置

在编辑器中，选中引用的类、方法、参数、变量等名称后单击鼠标右键，在弹窗中选择**转到 > 转到实现**（或使用快捷键**Ctrl+Alt+B**）跳转到实现位置 。若变量名有多个实现，在弹窗中可选择想要查看的实现位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/hWZKlmtbTI-ijCwi4vHIkA/zh-cn_image_0000002810750949.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=7F7D770E6C5AC492933E3814C1F9BB0049F312A9164B197883709B365DA7D423)

### 跳转到引用位置

在编辑器中，选中引用的类、方法、参数、变量等名称后单击鼠标右键，在弹框中选择**转到 >转到引用**（或使用快捷键**Ctrl+Shift+B**），可以跳转到变量被引用位置。若有多处引用，在弹窗中可选择想要查看的引用位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/hrA0c9XcTnWAwg8cK4c4Cg/zh-cn_image_0000002810750935.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=DF35F4B721ACBEF83181E27575FBC40BD9CE0280228F44600B08BC08C8D78D12 "点击放大")

## 跨语言跳转

支持在声明或引用了Native接口的文件中（如d.ts）跨语言跳转至其对应的C++函数，从而提升混合语言开发的开发效率。开发者可以选中接口名称单击右键，在弹出的菜单中选择**转到 >转到实现**（或使用快捷键**Ctrl+Alt+B**）实现跨语言跳转。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/SpkfBMvcSKaXgwVgeKU91w/zh-cn_image_0000002781471286.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=308C6B176FB9C7C83F17CBE814693AAD16D3B2BB014C9D84AB6A44901A59AD18 "点击放大")

## 代码格式化

代码格式化功能可以帮助开发者快速地调整和规范代码格式，提升代码的美观度和可读性。默认情况下，DevEco Studio已预置了代码格式化的规范，也可以个性化设置各个文件的格式化规范，设置方式如下：在**文件 >** **设置** **> 扩展**下，选择**ArkTS**/**JavaScript**/**Type****Script**，然后自定义格式化规范即可。

若想要快速对整个文件的代码进行格式化，可以点击鼠标右键，在弹框中选择**格式化文档**（或使用快捷键**Ctrl+Shift+L**） ；若想要对选定范围的代码进行格式化，可以选中代码并点击鼠标右键，在弹窗中选择**格式化选中内容**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/5WXGzEJkQzW23xsDe51w3Q/zh-cn_image_0000002810750943.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=45A254FA7F9703B812CDBAB8EFF8F39FD66EE1950E23192ABB001B9A00EA7404 "点击放大")

## 代码折叠

单击编辑器左侧边栏的折叠和展开按钮对代码块进行快速折叠和展开操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/2Ja8oSQ3TLKyR_M2d7ZgCA/zh-cn_image_0000002810630833.gif?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=D95834CB7E5BC77AA45E801FE607ECEF832B02076ABB5662AFA66B318BB6432B "点击放大")

## 代码快速注释

支持对选择的代码块进行快速注释，使用快捷键**Ctrl+/**进行快速注释，对于已注释的代码块，再次使用快捷键**Ctrl+/**取消注释。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/R8MZ-fErTAmPPdj90_1w_g/zh-cn_image_0000002781471288.gif?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=6B08ECBA19D78D483A9BB6A637409D141369C8AE991EA732130C95243206460D "点击放大")

## 代码查找

### 在文件中查找

支持开发者在当前文件中快速查找目标代码，操作步骤如下：

1. 打开目标文件，使用快捷键**Ctrl+F**打开查找界面。
2. 输入需要查找的代码字符串，支持通过大小写匹配、全字符匹配或正则匹配缩小搜索范围。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/mTGIvUNbS4m2HMhhgfsUwQ/zh-cn_image_0000002781471290.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=7CA122D2653A65FBDB52C757F2FCD9B01DAE3D4DD03715FFAE25B3D7A8EBAB6D)

**说明** 

点击搜索框左侧箭头（或使用快捷键Ctrl+R）展开查找界面，在上面输入框和下面输入框分别输入代码字符串和替换的字符串，点击替换逐个替换文件中字符串，点击替换全部替换文件中所有字符串。

### 在项目中查找

支持在整个项目中查找特定的文本或代码片段，操作步骤如下：

1. 在左侧菜单栏中点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/ddS82H_AT7Kb1x89i-T3dA/zh-cn_image_0000002810750941.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=4C5A95AF0FF24E153B162236BBF1FF32A6448112FCAEA2B747AE286CD36FD80A "点击放大")打开查找界面，在搜索框中输入查找内容后，编辑器会在项目中匹配并显示所有搜索结果，点击查找界面右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/o44VTkJMRz67d06EsJEVkw/zh-cn_image_0000002781471292.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=FCD982852536F3E092DE85DC59C37C910F6E647DE99648B11D2429D9922F7843 "点击放大")收起搜索结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/4rsfVLOVQZecz3V7qwEzUw/zh-cn_image_0000002810750945.gif?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=1B26AEE8965A43B54D278410E8FE0973C094E94A0AE24C8EBD4543F77F284E16)
2. 支持通过文件类型和搜索范围过滤搜索结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/-a1sYWVhRmu96OfY7YG_GQ/zh-cn_image_0000002781311350.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=440AE1708670F01C0483D5FD370B076FA30AE8C3A78DCAFA7CA55C638A7E1FAA)
3. 点击搜索框右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/wIxsPh8QRl6IhNwBRo1hWw/zh-cn_image_0000002810630831.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=586CF92008929ED2EE677AA40B253B75CDCD5B0F03045631B4759C197AB4C2E8)支持替换操作，选择**替换全部**替换所有匹配内容。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/pHmu4taQQrGlgH47J0vJFA/zh-cn_image_0000002781311342.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=326C986E4A24626E27230FB4A6950D0EC9F97B44B9ACF4EE9F384E13304CE795)

### 全局查找

支持文件名、符号、命令及文本的全局查找。通过连续点击**两次****Shift**快捷键，打开代码查找界面，在搜索框中输入需要查找内容，下方窗口实时展示搜索结果。单击查找的结果可以快速打开所在文件的位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/P3EUHErgQeO_zQ9wr73YcQ/zh-cn_image_0000002810750955.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=4D04A46A1C3F7179FA5E844BED3C2B51B1227CC9575069AC375BDBE98D0A2FD7)

## 函数注释生成

DevEco Studio支持在函数定义处，快速生成对应的注释。在函数定义的代码块前，输入**"****/\*\*****"+回车键**，快速生成注释信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/RvzQasSPQfeN8oN_ADNGfw/zh-cn_image_0000002810630839.gif?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=4716C8AB2DA4E784245023E1FA7FD53DE2F0399767FABFD754123100CA77AEEB)

## 文件引用查找

DevEco Studio提供对文件或文件夹的查找引用，可以帮助开发者快速查看某个文件或文件夹被引用的位置，便于后续进行代码重构。

选中文件或文件夹，单击鼠标右键选择**查找用法**。在左侧搜索窗口查看文件被引用的位置，点击引用位置自动跳转到对应文件中。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/tlHqr6oES12JWcQkHEVSyA/zh-cn_image_0000002810630835.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=B7A91B5C0EF248B5A641F1606EBA11CE36E28CC3FBEA37D790EFFDC1C446DD63)

## 字体设置

编辑器支持开发者设置字体，选择**文件** **> 设置**(或使用快捷键Ctrl+Alt+S打开)，在设置界面点击**编辑器 > 字体**，设置字体大小、字体样式和制表符大小。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/dHJBzgmJSnedA4EiOKHkzA/zh-cn_image_0000002781311340.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=C9135367D9EE3AE03E616E785B0C6DB4872C67FE2390BB3FE573A444C9CEBAB8)
