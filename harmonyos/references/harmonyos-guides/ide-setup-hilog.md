---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-setup-hilog
title: 日志分析
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 日志与故障分析 > 日志分析
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:00+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:1705772c10b26fb95727c01255e7baa000b7793459c438467afc0a5628133b11
---

**说明** 

打印日志请查看[使用HiLog打印日志](hilog-guidelines-arkts.md)。

DevEco Studio提供了“Log > HiLog”窗口查看设备当前所有应用实时打印的日志信息。HiLog默认显示的日志为以下6个部分。

| 第一列 | 第二列 | 第三列 | 第四列 | 第五列 | 第六列 |
| --- | --- | --- | --- | --- | --- |
| 时间戳 | 进程ID和线程ID | 日志标签 | 应用包名 | 日志级别 | 日志内容 |

开发者可通过设置包名、日志级别和搜索关键词来筛选日志信息，还可以使用自定义日志显示格式、日志导出、显示最新日志等功能。

HiLog窗口左侧各个按钮的作用为：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/RUye2c3DTrCbxj-hWnjhiA/zh-cn_image_0000002779567490.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=06B18C14D6220DDC0390398F5B5CE0B8BA2311B8E362B5649573AB8E5B493DDC)：单击该按钮可以向上翻页，日志窗口取消自动滚动。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/IR6gz9bvSB6EAi8Syx4BlA/zh-cn_image_0000002808887127.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=B42C04576F27F2C57598FBA01A9C51E1D98FEB65F8BAAA92E2482DFBEF6C2E3F)：单击该按钮可以向下翻页，日志窗口取消自动滚动。如果翻页已到底部，日志窗口自动滚动。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/Xo5GG9igRfyhKG0mQsvhWg/zh-cn_image_0000002779567492.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=2EADBE05FE59CF72560A4167466B28BCADF047FA10BA935C29DD9A1D91424AD2)：当该按钮处于选中状态时，日志自动换行显示，否则日志按行显示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/o0OYxvF2QoW1qsiptSW68A/zh-cn_image_0000002779407502.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=1771CF9B6BBCB883EB0FCF5A3F0A924433AF84F890E98774051D99DA1CE4C66A)：当该按钮处于选中状态时，日志自动滚动到窗口底部，否则停留在当前日志显示处。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/hS6OLaJvSh2Q1Gz-VCxPRg/zh-cn_image_0000002779567462.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=199EA017EF6CFA3FC8D1B503DE253B50DC9BF171716D39BD9B3FC9BE7D92ECF8)：单击该按钮可以重新开启日志接收，会重新加载设备缓存日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/dV4Vuy-ySeydQTWOPerImg/zh-cn_image_0000002779567466.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=D54E6054F27CB04238BCB832A4A9E0C39DFCDCDA030EBE599D88A59DB4402E66)：单击该按钮可以清空窗口日志和设备缓存。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/WgchL1wOTbO20X1G_P-YsA/zh-cn_image_0000002779567460.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=80B3391DFECAB4E74F7C6B313C2A98AC3A3CDB32EE9AAEA7CFADB487A8B3502D)：单击该按钮可以对当前选择的设备屏幕进行截屏，并保存在本地。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/ohSQUYmFRImgbbVd-RyStA/zh-cn_image_0000002808767075.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=AA74928FB8ADB39881861D3451FEF7441B87E2E4FE6A3EAF0ED5BDCF40241088)：单击该按钮可以对当前选择的设备进行录屏，并保存在本地。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/9Tls1n2DTw6v6SnicBvMbw/zh-cn_image_0000002779567496.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=E339B32291778CC000CA1291EB27D0DE74A359D9ED8DD92705FC72B012E76F29)：单击该按钮可以保存日志缓存到指定文件（在线日志）或保存离线日志文件（离线日志）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/v8E0K6keQVmhYcmay93XaQ/zh-cn_image_0000002808887111.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=E659DEFF226ACEAFA14C73FA40D9449B432FEB6981C2026465AB2DCF0C72C6B2)：单击该按钮可以自动选择和切换已连接的设备。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/rwr_67s4SxufHtP9kl_gvQ/zh-cn_image_0000002779407514.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=4DEA02D0C301DE1FA4AA7E442CDFA09FDE275E76FFA1EA92A27CC9FC505432CB)：单击该按钮可以切换日志视图以及自定义日志格式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/ak-BuiEGRlWSY3U6I97fCg/zh-cn_image_0000002808767045.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=4D9B3033A467F1AF302796081D6A8EFD72FAA9E0D8B4FB31601C3DD9EAC92FEC)：单击该按钮可以关闭当前日志窗口。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/niWoOWWDRe6Xtr-WIcUpsg/zh-cn_image_0000002779407490.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=68B2BDD9A9510D63E7DA196B2359042168CD8D4A1945A288FF0F633A6FE2D97A)：单击该按钮可以跳转到HiLog日志相关的在线帮助文档。

## 过滤日志

### 按关键字过滤日志

在HiLog搜索框中输入希望过滤的信息，即可过滤显示所有包含此信息的日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/R_Rg2IaLSKGihHI85ynL3g/zh-cn_image_0000002779567458.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=47DAF6CAB9069579E696388762433A51350A1E2F2694554AF0F0E852A14A7DC7 "点击放大")按钮表示是否区分大小写，![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/uCW3DFZPQaCjmiFRVset1w/zh-cn_image_0000002779407510.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=E74AF442DAEC9D64B40033CEB3381411A815CB12DF89CA13F3DCC099CCEC4AAF "点击放大")按钮表示是否按照正则表达式匹配过滤，![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/mckzODg4TW-IMxaAoPViCQ/zh-cn_image_0000002808767035.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=B0B170EA526998B9D8ACF97882C490E0025448550E3BC0784605E094D33E3E29)按钮表示关键字是否高亮。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/sQFZTTKSTomvRWVJ4L-T-Q/zh-cn_image_0000002779567486.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=3B8C8F568961BBA1F9E7B3011DE2D796EE05BD59E06669CF9A51AA324ACE4118)

从DevEco Studio 6.0.2 Beta1版本开始，支持使用逻辑运算符&拼接多个关键字，精准搜索日志，&字符前后要有空格。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/4hEm2T1YSG-zehtUaTk5Zg/zh-cn_image_0000002779567494.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=B1B1F398A9695E5022EB8F1B7C2560AE855458445F06843B05A0F35D4829973E)

### 使用默认提供的过滤配置

HiLog提供多种默认的过滤模式，开发者不需要反复输入关键字过滤日志信息，只需要切换相应的过滤项，即可快速过滤所需的日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/JdpwD7NXSb2mbUBo1hobzA/zh-cn_image_0000002779567464.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=EF9C288992319BE9F627FCC53A98FA58E3A9407C4B21BB18862F90FA198A6FCC)

* All logs of selected app：按照应用进程过滤日志。
* User logs of selected app：按照应用进程过滤用户输出的日志。

当选择All logs of selected app或User logs of selected app时，进程过滤下拉框处于可选状态，可选择相应的选项过滤想查看的进程日志。

**说明** 

由于设备启动时，USB调试开关没有开启，部分系统应用没注册上，HiLog进程列表无法显示未注册上的系统应用，如需查看此部分的日志，可以[按关键字过滤](ide-setup-hilog.md#section1264082914019)查看，或者保持USB调试开关打开的状态，重启设备。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/g6wzHvVSTi2IxH56NyWztA/zh-cn_image_0000002779407486.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=124920106F537019FEFA14924C3785B9E284CC746FEE1417F902D20FB3279A53)

进程选择窗口可输入PID或应用名的关键字搜索要过滤的进程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/vVd-hOXgTj2RJh5A-j-GSw/zh-cn_image_0000002779407516.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=0089294A3B83B96A2F622EF69741588717AAE680B73C09FB9C69A526777B4718)

### 按日志级别过滤日志

HiLog提供日志级别过滤，用来过滤某一级别及以上的日志。日志级别分为Debug、Info、Warn、Error、Fatal五个级别。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/Yd16JmRHSXqfkmt8VNHWEg/zh-cn_image_0000002808887129.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=BAF08F25BC112A55A23563C76B5FD1A7FE013E40DD4788C0B279B031E99225E3)

如选择Warn级别，则过滤展示Warn级别与Warn级别以上的日志信息，即展示Warn、Error、Fatal三个级别。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/PDbJECMISzGbLfsGwKI3MQ/zh-cn_image_0000002779407500.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=93F59649EBCF337C8F6C4840FE695662A9EB00FC9A6B250F8C690EEAE27F1D6A)

### 按日志标签过滤日志

从26.0.0版本开始，支持根据日志标签过滤日志，可输入多个标签，不同标签之间使用英文逗号分隔。如包含特殊字符，标签需要添加引号。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/gKMYJqmEQ2OkJ9npNvmpPw/zh-cn_image_0000002779407488.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=4568B01E6DCE0D4425AA3E631CBA64DC1F70FFC14E98CE5839872EE450C59CEC)

### 按自定义过滤项过滤日志

除默认过滤项外，HiLog还提供配置自定义过滤项的途径以供开发者按照实际需求过滤日志，并保存此过滤配置以供重复使用。

点击**Config custom filter**时将弹出自定义过滤配置窗口。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/UPuNF4QaQueEV6sJytxGUg/zh-cn_image_0000002808887117.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=B1864423E5D625EA2E09BBEA56364E992E64854CC39BB53A87F29C634DAAF7E9)

先前介绍的过滤选项此处均可配置，同时增加了Package name和Set to all projects配置项。

* Set to all projects：此配置当前工程及其他所有工程均可用。
* Package name：按应用包名过滤日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/NLvLzjxURf-oZXWVc-jTWQ/zh-cn_image_0000002779407494.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=42431B0BD42917A981B36819B51D98AD788371A364F574105FCDA559BDB2AE54)

当配置完后将自动切换至此过滤配置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/t4xlknleRYiPPLnpSvjDAw/zh-cn_image_0000002779567474.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=96C59663843C54BB2357591CC760C7707EB4A1791A1D4DB3FBB71A606DA84DA6)

切换至此自定义配置时，日志级别过滤窗口和关键字过滤窗口将在此自定义配置过滤出的日志的基础上再进行过滤。

## 自定义日志显示格式

开发者可以通过配置自定义格式，限制每条日志只显示用户关注的信息。

点击左侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/TI6uXltIQ_WpfK4_WLd4DA/zh-cn_image_0000002779407496.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=A6680B275A240707E6C59D1C23A7F37727A3EB534B3384B30940EE1DFCCE0763)图标，将弹出自定义格式窗口。

* Standard Views：默认显示所有信息。
* Compact Views：默认显示日志级别与日志信息。
* Modify Views：进入“Hilog Format”窗口后，可以按照需要自定义日志格式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/J9boL-HtRmuxa2nJiCuarg/zh-cn_image_0000002779567498.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=B440C4D704C17985F229AE5041E49835E8D0E71CFFF3B75DB89DAD30C12790E3)

在“Hilog Format”中自定义日志格式：

* Use as default view for new windows：新建的HiLog窗口以Standard模式显示还是以Compact模式显示，新建后开发者可再自行切换其显示模式。
* Show timestamp：是否显示日期时间 。

  Format：Datetime/Time 显示日期时间/只显示时间。
* Show process id：是否显示PID-TID 。

  Include thread id：是否显示TID。
* Show domain/processname/tags：可以勾选以下三个选项决定是否显示domain、processname、tag。

  Show domains：是否显示domain。

  Show processnames：是否显示processname。

  Show tags：是否显示tag。

  Total column width：domain/processname/tags列的最大宽度，超长信息将会缩略显示并以ToolTip形式显示以上勾选内容的完整信息。
* Show package names：是否显示应用包名。

  Package column width：包名列的最大宽度，超长信息将会缩略显示并以ToolTip形式显示完整信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/Tl6UAUqmSoiTVUsG95uIlw/zh-cn_image_0000002779567472.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=927D02D60C553E7EC72E5F6573B8A42D99629C7C2DBB145841F575484CA1D183)

## 超长日志自动换行

当日志的消息过长时，日志窗口可能不能完整显示日志消息，需要拖动滚动条查看信息。此时开发者可以点击**Soft-Wrap**按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/Ujs07QO0RFK8SXn8Fexohg/zh-cn_image_0000002779407512.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=A96E65F43B1211946287814D3468184E802B2041C6580D14D6CBA8AB5411B8F8)控制日志消息自动换行。

**图1** 未开启自动换行  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/pFlF6ZgKQWmoaQ1a_4n4hg/zh-cn_image_0000002808767077.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=C2F482C6898C94FC451B977CC9AD9809461DAB653146EE1A79E0DF73BB8D7CF9)

**图2** 开启自动换行  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/E2W_IkfHRdSEncBMLjH7gw/zh-cn_image_0000002779407478.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=DF1E698824DA3DBDD06977B51155435D214E303CC9D88C5CEE107CB1E4EDD3AB)

## 显示最新日志

设备输出的日志信息会实时刷新到HiLog窗口底部，用户可点击**Scroll to End**按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/h1mSmig2TQyidrQTtiBGgg/zh-cn_image_0000002779407480.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=C04E65219FD2A448361A83F93B8AAD044AA45C9E0ADF58D8F108F3C2ACE0FD40)使HiLog一直显示底部的最新日志信息。当观察到需要的日志时，点击HiLog窗口，即可停止滚动，停留在当前行，以便查看日志信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/kM3Jq2-_T_q_JjyBdA5vDQ/zh-cn_image_0000002779567488.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=98148C9421E5F98E88A6C65001D5D10159ACE3F78B16689779BA85BCA8906D5F)

## 导出日志信息

用户可将经上述步骤过滤后的关键日志信息保存到本地，以便进一步分析。

点击**Export HiLog**按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/gL4y3XCJQVaLYvh_1GQ-yQ/zh-cn_image_0000002779567476.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=91CA5F8F1AB803A0F31DCB6E00488FCF03646510E3536EC69F6FBA0AD7C5D03F)，在弹出的Export HiLog To窗口中选择保存路径。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/qEetcRr2QKuczIhFF0ZBnA/zh-cn_image_0000002779567468.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=64D3DAF2F3C2CC725F1EBFD9D7B17176E62B52A4C426E8726DCD05A7CF467913)

## 清除日志缓存

与日志相关的缓存有两个：设备端日志缓存、HiLog窗口缓存。

HiLog显示日志信息的流程为：

1. 应用输出日志信息至设备端日志缓存；
2. Log组件将设备端日志缓存取出，保存在HiLog窗口缓存中；
3. HiLog窗口根据过滤条件，将HiLog窗口缓存中的消息显示在界面中。

点击**Clear All**按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/rbGg9hg1TT2JHoBGlPywxQ/zh-cn_image_0000002779407492.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=7964724D5572404E7980710C4C5D5E17A33C13D07E77C0CF1A33E43005F63456)，将同时清除设备日志缓存和HiLog窗口日志缓存，以及当前已经打印的日志。HiLog窗口将显示执行清除操作后，新输出至设备端缓存的日志信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/WNl892qCQF2mjLrHB2nVHQ/zh-cn_image_0000002779407508.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=55BCAF5344DC7EF19D4EF19E7FCCF4047429AC39096CCF1E45434EFFF914C508)

## 设置HiLog窗口缓存

HiLog窗口显示的日志信息保存在此窗口的缓存中，缓存的大小决定了当前窗口能显示的日志信息的最大数量，当日志超出缓存上限时，窗口中最早的日志将会被清除，新日志在窗口底部输出。开发者可以自行设置窗口的缓存大小。

点击**Settings > Buffer**，进入缓存设置窗口。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/9THmW3KUQweaANhqZY5OnQ/zh-cn_image_0000002779567480.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=32608EFA1B187701CFEC9EC5A7B7214B52CDE9DE71C9FED89DB1807CB8BA5FC0)

默认缓存大小为4096K，变更缓存大小需重启HiLog窗口后生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/THXljellT4aNQtve4GeGOQ/zh-cn_image_0000002808767031.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=AACBA0E65221F56505F79B2E33E66E15FF37E49C5F8DF869FED55B54659BF415)

重启HiLog窗口操作：先点击下方的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/LAmD6zWbTd-GWF2QgoOXFA/zh-cn_image_0000002779567482.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=7F73A3184CCC42E2F387BAB2C60634B384586C60C90C7C768EEE89A11F12FD4D)按钮，再点击上方的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/Y6Y8vHLFRQKtK6jZvB7Tig/zh-cn_image_0000002779407504.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=B40DE6F805D4A3EF6B77DFBFC2803CF27AC19E672D6502EC1941851C3F796744)按钮中的Online Log即可。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/gynxjcZdRZmuZ4z0IlOHJw/zh-cn_image_0000002779567470.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=F66EE2719742DCEB71C33B5D97428A5B4E2F4490B6983CDD6C1E1A4AE1A22942)

当日志量超出缓存时，顶部的旧日志不断被清除，因而顶部日志信息处于不停滚动的状态。此时若想查看此处的日志信息，可在日志滚动时，点击右键，勾选**Pause Output**暂停窗口打印，查看完后再取消勾选，重新开始打印日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/kLtNUNI6RHmK0dwZX1DSpg/zh-cn_image_0000002779407506.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=79AFEBC84A503C23B91D3CBB8259625B6254926AC388C920922A3C3EEADE827F)

## 设置设备端日志缓存

使用hdc shell hilog -g命令可查看当前设备端设置的日志缓存，默认为256K。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/Xq_qS6tTTICkhLal_4vBig/zh-cn_image_0000002779567484.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=C2604B65270B3D7400B8C13CB67609A610591F00FA2D7BAA003790764384449D "点击放大")

使用hdc shell hilog -G命令可更改设备端日志缓存大小。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/mwRZpZYdRm2xIEjtkrdgUg/zh-cn_image_0000002779567478.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=E94DA2F163B3B460DA531E9BB21A15374B5D1485F8F383643968EF8685C91902 "点击放大")

配合-t参数可单独设置某一类型的日志缓存大小。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/uO52zEFjTLKakIVKKELM5A/zh-cn_image_0000002808887115.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=2F646A9872B722B73F9697E009AE5D7FC71984ED913FE029920ED0C50B04F2C9 "点击放大")

超出设备端缓存日志将被落盘于设备data/log/hilog路径下，开发者可在此目录下载历史hilog日志并查看。

## 查看/导出设备离线日志

DevEco Studio提供查看设备离线日志的功能，支持查看设备中/data/log/hilog路径中的日志，离线日志窗口中展示的是经过解析和DevEco Studio格式化之后的日志。

点击HiLog窗口左上角New，随后点击Offline Log即可打开离线日志窗口。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/V4QY34h6SGqlD6k4qGGJIA/zh-cn_image_0000002779407498.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=E03FE2964FC798519BB77D807CC2B43B5AFEFC40A293F99DE9DD9C5185A62892)

离线日志窗口左边工具栏中的按钮、日志级别下拉框和搜索框和在线日志的功能一致，设备下拉框仅支持选择真机和模拟器。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/OHFIPvKrSGOZN5Sw1R_mGQ/zh-cn_image_0000002779407518.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=DE627B7448EC5C7ABCFA4514BA0E4E61CE07B11678E1F6DEDBCD0CB6E4E01BA9)

离线日志支持通过时间筛选设备上的日志文件，默认时间范围为打开窗口时的前三十分钟，除显示格式外，也支持通过键入yyyyMMddHHmm后回车进行时间输入。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/SabhgeIkSo-7ivvojVaLAQ/zh-cn_image_0000002779407484.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=5BA2780714081A7E24BB9E52CBA5EE611C92332E0CF9F16298A1FF4F4E029D93)

在输入时间之后，日志文件下拉框会进行刷新，点击文件会从设备端下载并自动解析后输出到离线日志窗口。

由于最新的日志文件内容还在更新中，在达到设定的大小前，内容会不断增多。如果重新打开离线日志窗口或者修改时间，日志文件列表都会刷新，会从设备端重新下载最新的日志文件，解析的内容会更多。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/HCSC6JXLToW8_K178euRyg/zh-cn_image_0000002779407482.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=EDA126F36BE0C7A82E4706F588B12DD75625D736D4851623E328575CE8D96717)离线日志窗口能输出的文本量可参考[设置HiLog窗口缓存](ide-setup-hilog.md#section106741332995)进行设置，设置较小可能无法显示选择文件的所有日志，推荐设置6M(6144K)。

通过设置窗口的缓存大小可能无法展示完整的日志，可点击左侧工具栏的保存按钮导出离线日志，支持导出解析后未经DevEco Studio格式化的原始日志文件，导出的文件可以看到完整日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/DUEt25SvSBq9jbP6rB5SgA/zh-cn_image_0000002808887159.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=434CE03E4AA125C283D4B7B7DC2B2284CD386F44856857D05CD0932C075AC374)

## 终止应用

从DevEco Studio 6.0.0 Beta5版本开始，在日志窗口点击**右键 > Force Stop App**，可以终止该日志所属进程的应用，不支持系统应用和release签名的应用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/RWFxGjyWQ7-Hk493l0hPFQ/zh-cn_image_0000002779567452.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=78E09DF993C0E38C0EF5E48FE1578FD904192B8EEDE19D99F849C3329EB86345)
