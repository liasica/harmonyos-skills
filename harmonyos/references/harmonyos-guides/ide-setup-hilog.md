---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-setup-hilog
title: 日志分析
breadcrumb: 指南 > 编写与调试应用 > 日志与故障分析 > 日志分析
category: harmonyos-guides
scraped_at: 2026-04-29T13:46:56+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c31e51ef4368595c7b3b7bd70660afb7218334bbee8a83519e784bb319bd4f15
---

说明

打印日志请查看[使用HiLog打印日志](hilog-guidelines-arkts.md)。

DevEco Studio提供了“Log > HiLog”窗口查看设备当前所有应用实时打印的日志信息。HiLog默认显示的日志为以下6个部分。

| 第一列 | 第二列 | 第三列 | 第四列 | 第五列 | 第六列 |
| --- | --- | --- | --- | --- | --- |
| 时间戳 | 进程ID和线程ID | 日志标签 | 应用包名 | 日志级别 | 日志内容 |

开发者可通过设置包名、日志级别和搜索关键词来筛选日志信息，还可以使用自定义日志显示格式、日志导出、显示最新日志等功能。

HiLog窗口左侧各个按钮的作用为：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/_8iTn0y4RvmnqNDFSA59KA/zh-cn_image_0000002561833479.png?HW-CC-KV=V1&HW-CC-Date=20260429T054652Z&HW-CC-Expire=86400&HW-CC-Sign=37D8019C5D6BE449A47612DE87A004C13799CAC274DB7D9DF98779BC72AF248F)：单击该按钮可以向上翻页，日志窗口取消自动滚动。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/6wuNc-iTRem5FTcSzIyeRg/zh-cn_image_0000002530753502.png?HW-CC-KV=V1&HW-CC-Date=20260429T054652Z&HW-CC-Expire=86400&HW-CC-Sign=CDA192251DF081564DF115856B8620EA629CED6C81162660A72B0AD753EFDF64)：单击该按钮可以向下翻页，日志窗口取消自动滚动。如果翻页已到底部，日志窗口自动滚动。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/PAoOICoaRTyOr01rqKmdCw/zh-cn_image_0000002561753505.png?HW-CC-KV=V1&HW-CC-Date=20260429T054652Z&HW-CC-Expire=86400&HW-CC-Sign=FBFAA5F799C4B486B6136F2333851FEB998F6F31008396EB1973361B0B5B150D)：当该按钮处于选中状态时，日志自动换行显示，否则日志按行显示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/-SGtLk-7TCmoKDt-isLqCg/zh-cn_image_0000002530753540.png?HW-CC-KV=V1&HW-CC-Date=20260429T054652Z&HW-CC-Expire=86400&HW-CC-Sign=5B9B4376118F6BB7123EB0E8E0755486EC7ED5D4F521642CC5E79FDE866069AA)：当该按钮处于选中状态时，日志自动滚动到窗口底部，否则停留在当前日志显示处。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/7_2XA7BcQi6Ry9Pz4eteMQ/zh-cn_image_0000002530753488.png?HW-CC-KV=V1&HW-CC-Date=20260429T054652Z&HW-CC-Expire=86400&HW-CC-Sign=8B463B3D988ECCAA2B12912C2194CE76ED3843F34C433FAE1F4EF6FC0822B143)：单击该按钮可以重新开启日志接收，会重新加载设备缓存日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/jymDS5OGTpWdkhaw4ze1UA/zh-cn_image_0000002530753504.png?HW-CC-KV=V1&HW-CC-Date=20260429T054652Z&HW-CC-Expire=86400&HW-CC-Sign=B6C0F1AA20B00942FAFD74C9A8BBCE076FAA17DA90B7631DB498DC68AB877876)：单击该按钮可以清空窗口日志和设备缓存。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/iowRP9ZCTd2naivYhi6auQ/zh-cn_image_0000002530913472.png?HW-CC-KV=V1&HW-CC-Date=20260429T054652Z&HW-CC-Expire=86400&HW-CC-Sign=053B89B08462EBE57F5C15045A3FC135516ACB454F1E049A1AF97ACB358B2509): 单击该按钮可以对当前选择的设备屏幕进行截屏，并保存在本地。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/a_at8VGmQgidz3ySqrINCg/zh-cn_image_0000002561833497.png?HW-CC-KV=V1&HW-CC-Date=20260429T054652Z&HW-CC-Expire=86400&HW-CC-Sign=D86F68ACB374B355CA38B25D3AA008BBB5A80CD9BE1A582CB818C053E3E6B8F3): 单击该按钮可以对当前选择的设备进行录屏，并保存在本地。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/nHvx7TjgQt6PicE6m2clXw/zh-cn_image_0000002561753515.png?HW-CC-KV=V1&HW-CC-Date=20260429T054652Z&HW-CC-Expire=86400&HW-CC-Sign=9BA23FC495B4C0E8C9D21A71CFE1A227A2DBEE2958F10831F2B7F861D443DD71)：单击该按钮可以保存日志缓存到指定文件（在线日志）或保存离线日志文件（离线日志）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/-Ur3ky3FT86_556fHVidPA/zh-cn_image_0000002530753468.png?HW-CC-KV=V1&HW-CC-Date=20260429T054652Z&HW-CC-Expire=86400&HW-CC-Sign=094DA8D526262BA35D0A5C2E48D976044A56F2B5D731D10DD82FB188798BE348)：单击该按钮可以自动选择和切换已连接的设备。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/sUJkXSH1RJ-RHKyhKsvqVw/zh-cn_image_0000002561833487.png?HW-CC-KV=V1&HW-CC-Date=20260429T054652Z&HW-CC-Expire=86400&HW-CC-Sign=ABE051F96D8F602E36D5BAAA153C9354026DB9AFA0704E9BD68961321AD0B4BA)：单击该按钮可以切换日志视图以及自定义日志格式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/KVNP34zSRlCN5GwQd5Q1_g/zh-cn_image_0000002530753506.png?HW-CC-KV=V1&HW-CC-Date=20260429T054652Z&HW-CC-Expire=86400&HW-CC-Sign=6265A22BC9C82084FF61A1A2D94AA3A8B55A9437352CE5CE5987351C76E912E6)：单击该按钮可以关闭当前日志窗口。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/cg63diyCRTiUDV_3WY-TGw/zh-cn_image_0000002530753508.png?HW-CC-KV=V1&HW-CC-Date=20260429T054652Z&HW-CC-Expire=86400&HW-CC-Sign=AAAB1813D926265D9E6438B5F5F3119D875F7446315D2B78D86FC3D114D3EF30)：单击该按钮可以跳转到HiLog日志相关的在线帮助文档。

## 过滤日志

### 按关键字过滤日志

在HiLog搜索框中输入希望过滤的信息，即可过滤显示所有包含此信息的日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/30KGuL_cTbeDfdUnIRWNIw/zh-cn_image_0000002561833393.png?HW-CC-KV=V1&HW-CC-Date=20260429T054652Z&HW-CC-Expire=86400&HW-CC-Sign=099A8AE422A6E51666FCE67F6C2AB69A1D7B09451A07C8DDD7E9F402E5D78297)按钮表示过滤是否区分大小写，![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/Mbgik1-8SNOwHMOMfKZivA/zh-cn_image_0000002561833477.png?HW-CC-KV=V1&HW-CC-Date=20260429T054652Z&HW-CC-Expire=86400&HW-CC-Sign=1650857ABFEE005115C28174F4B1971989EB9FCAB155C5834630577C5456C073)按钮表示是否按照正则表达式匹配过滤。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/FkYicoapSZ6esTpuIAQmIQ/zh-cn_image_0000002530913574.png?HW-CC-KV=V1&HW-CC-Date=20260429T054652Z&HW-CC-Expire=86400&HW-CC-Sign=B9397E53EC5AA063AC947F349BB98176CB5848ABA52FA04902FFC104CC4A50E5)

从DevEco Studio 6.0.2 Beta1版本开始，支持使用逻辑运算符&拼接多个关键字，精准搜索日志，&字符前后要有空格。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/N6Jg3G0FTCe7D37DWFe1DQ/zh-cn_image_0000002530753472.png?HW-CC-KV=V1&HW-CC-Date=20260429T054652Z&HW-CC-Expire=86400&HW-CC-Sign=56C808C801F967AFEFB9C3C1BC84EF6E7C95D792FD9B2E47A3357E59DEBDAD21 "点击放大")

### 使用默认提供的过滤配置

HiLog提供多种默认的过滤模式，开发者不需要反复输入关键字过滤日志信息，只需要切换相应的过滤项，即可快速过滤所需的日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/gH_ZmVnaSh-l3wXiOg9Zog/zh-cn_image_0000002530913576.png?HW-CC-KV=V1&HW-CC-Date=20260429T054652Z&HW-CC-Expire=86400&HW-CC-Sign=45EA488E21CF818DD74D24F98006CAE7E7E15B57D793F53001BAE62E8BA3E0A7)

* All logs of selected app：按照应用进程过滤日志。
* User logs of selected app：按照应用进程过滤用户输出的日志。

当选择All logs of selected app或User logs of selected app时，进程过滤下拉框处于可选状态，可选择相应的选项过滤想查看的进程日志。

说明

由于设备启动时，USB调试开关没有开启，部分系统应用没注册上，HiLog进程列表无法显示未注册上的系统应用，如需查看此部分的日志，可以[按关键字过滤](ide-setup-hilog.md#section1264082914019)查看，或者保持USB调试开关打开的状态，重启设备。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/h6wNDntuRWujWVMuLkhHLg/zh-cn_image_0000002530753494.png?HW-CC-KV=V1&HW-CC-Date=20260429T054652Z&HW-CC-Expire=86400&HW-CC-Sign=C1B6F0C0FB5E4BD327BF98682FD8734F81EE6289A33D21C412ADC03CFBCD279F)

进程选择窗口可输入PID或应用名的关键字搜索要过滤的进程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/T-9Sjv3CRsCGsCC9YbOd4A/zh-cn_image_0000002530913530.png?HW-CC-KV=V1&HW-CC-Date=20260429T054652Z&HW-CC-Expire=86400&HW-CC-Sign=C01A19146EB3D62D4E406FDDC10D8402F8EB3DE6BC9A00B39C132D4F466822D3)

### 按日志级别过滤日志

HiLog提供日志级别过滤以过滤某一级别及以上的日志。日志级别分为Debug、Info、Warn、Error、Fatal五个级别。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/2XGGdC61TouPVyMYi_33yA/zh-cn_image_0000002561833475.png?HW-CC-KV=V1&HW-CC-Date=20260429T054652Z&HW-CC-Expire=86400&HW-CC-Sign=FF99349D880B6D45C00ACB9E5BC1AD1517D8C8BE14D8E986A39486D39E323DB6)

如选择Warn级别，则过滤展示Warn级别与Warn级别以上的日志信息，即展示Warn、Error、Fatal3个级别。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/NA6UUmlVSR2lKHfAfK_3EA/zh-cn_image_0000002530753550.png?HW-CC-KV=V1&HW-CC-Date=20260429T054652Z&HW-CC-Expire=86400&HW-CC-Sign=099102E24CB8BD86A71AE57A0BB9CEC00E98B3A779A75C1660E221AE29969CC7)

### 按自定义过滤项过滤日志

除默认过滤项外，HiLog还提供配置自定义过滤项的途径以供开发者按照实际需求过滤日志，并保存此过滤配置以供重复使用。

点击**Config custom filter**时将弹出自定义过滤配置窗口。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/nPmeLTdQSiyPeeKSnIZeYg/zh-cn_image_0000002530753496.png?HW-CC-KV=V1&HW-CC-Date=20260429T054652Z&HW-CC-Expire=86400&HW-CC-Sign=A9047BC81D1AEF929B8F98F2C23DCA819219230C3751981777712781DE4C4C52)

先前介绍的过滤选项此处均可配置，同时增加了Package name和Set to all projects配置项。

* Set to all projects：此配置当前工程及其他所有工程均可用。
* Package name：按应用包名过滤日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/MTGB-THYQ1G7c7wSUAaJ0A/zh-cn_image_0000002530753522.png?HW-CC-KV=V1&HW-CC-Date=20260429T054652Z&HW-CC-Expire=86400&HW-CC-Sign=9804337AE47624A5B0CB717628C16CC170521B53CE6D6FDC89AC9D30CA62E9DA)

当配置完后将自动切换至此过滤配置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/uEHX3Ea1RP6jefeQQCpJIQ/zh-cn_image_0000002530753486.png?HW-CC-KV=V1&HW-CC-Date=20260429T054652Z&HW-CC-Expire=86400&HW-CC-Sign=E7C7CDC27FAF56C37D413AD75B0765943870E6F01A9EA29F9EA740C20596CAB1)

切换至此自定义配置时，日志级别过滤窗口和关键字过滤窗口将在此自定义配置过滤出的日志的基础上再进行过滤。

## 自定义日志显示格式

开发者可以通过配置自定义格式，限制每条日志只显示用户关注的信息。

点击左侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/NRdE7tbfTSG0AsMxnujiJg/zh-cn_image_0000002530753524.png?HW-CC-KV=V1&HW-CC-Date=20260429T054652Z&HW-CC-Expire=86400&HW-CC-Sign=4F8B203AC0023DFAAFAFF09EAFB1834E94B93855F96ACB9E60E74054D1AAF8B3)图标，将弹出自定义格式窗口。

* Standard Views：默认显示所有信息。
* Compact Views：默认显示日志级别与日志信息。
* Modify Views：进入“Hilog Format”窗口后，可以按照需要自定义日志格式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/KbQ746R1Riyg0NTpmMnDmw/zh-cn_image_0000002561833469.png?HW-CC-KV=V1&HW-CC-Date=20260429T054652Z&HW-CC-Expire=86400&HW-CC-Sign=B5D487AB16662ABD1DF512564021DFD1D8A50F2A57159B1841D042BFBBAA92B6)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/aKNo2KrlSgi4ryanUJ7VNA/zh-cn_image_0000002530753516.png?HW-CC-KV=V1&HW-CC-Date=20260429T054652Z&HW-CC-Expire=86400&HW-CC-Sign=4D49B46E763E83099D729E1EC6D39BDDA16EDDB7A4216E9BB91D9A9AA4EEAF3B)

## 超长日志自动换行

当日志的消息过长时，日志窗口可能不能完整显示日志消息，需要拖动滚动条查看信息。此时开发者可以点击**Soft-Wrap**按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/AyLAmpLtRzik56Yt2e0a3A/zh-cn_image_0000002561833481.png?HW-CC-KV=V1&HW-CC-Date=20260429T054652Z&HW-CC-Expire=86400&HW-CC-Sign=7D1D48A7848FA4E4C2D473DD71EBEB0166C22498A3D16BB61EFFA455759E77F7)控制日志消息自动换行。

**图1** 未开启自动换行

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/pdGs1-tLTeu_D7Q46jcQuQ/zh-cn_image_0000002561833505.png?HW-CC-KV=V1&HW-CC-Date=20260429T054652Z&HW-CC-Expire=86400&HW-CC-Sign=BFD1F347ECDC198A0C4B3D96D3D08DF464923DC8331A2DB746D380EC6D5DBD54)

**图2** 开启自动换行

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/9fSOFpC3RAm4C78DaxVnPg/zh-cn_image_0000002530753518.png?HW-CC-KV=V1&HW-CC-Date=20260429T054652Z&HW-CC-Expire=86400&HW-CC-Sign=99EA4E34D18FBC95AA86A86342023A56158CD0B6CAFC483B0E8AA9557B86B4D8)

## 显示最新日志

设备输出的日志信息会实时刷新到HiLog窗口底部，用户可点击**Scroll to End**按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/pea9cNg3St-mST4THTFLOQ/zh-cn_image_0000002561753415.png?HW-CC-KV=V1&HW-CC-Date=20260429T054652Z&HW-CC-Expire=86400&HW-CC-Sign=A4B4FB6AFCDD72688B01C2CF2DEBC79B5D0EB9B369C6A396FD171DCB0135B06D)使HiLog一直显示底部的最新日志信息。当观察到需要的日志时，点击HiLog窗口，即可停止滚动，停留在当前行，以便查看日志信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/IukdpDFPSz-azBqN2dLk0w/zh-cn_image_0000002561833451.gif?HW-CC-KV=V1&HW-CC-Date=20260429T054652Z&HW-CC-Expire=86400&HW-CC-Sign=56499B6B7AF8D32EF13A86BDCD174152533EED67A80E59BEFD6888E0EF36BF0E)

## 导出日志信息

用户可将经上述步骤过滤后的关键日志信息保存到本地，以便后续的进一步分析。

点击**Export HiLog**按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/QYlkwtzIQuyDLf3MAPqr8Q/zh-cn_image_0000002530753526.png?HW-CC-KV=V1&HW-CC-Date=20260429T054652Z&HW-CC-Expire=86400&HW-CC-Sign=5F8060DADFD9ED1A88A7281B8C957D8140F0FB79C6B9970DAA834F0BB73E29B4)，在弹出的Export HiLog To窗口中选择保存路径。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/0NotpxR_SUqJYdp5E24dZQ/zh-cn_image_0000002561753473.png?HW-CC-KV=V1&HW-CC-Date=20260429T054652Z&HW-CC-Expire=86400&HW-CC-Sign=BF1232CCA0927B4660BF2E61B1DA25BA00426366B11A2BC924749C7A1DE884C0)

## 清除日志缓存

与日志相关的缓存有两个：设备端日志缓存、HiLog窗口缓存。

HiLog显示日志信息的流程为：

1. 应用输出日志信息至设备端日志缓存；
2. Log组件将设备端日志缓存取出，保存在HiLog窗口缓存中；
3. HiLog窗口根据过滤条件，将HiLog窗口缓存中的消息显示窗口在界面中。

点击**Clear All**按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/VYeWX5sYQrKv5d8k-s2uYQ/zh-cn_image_0000002530753514.png?HW-CC-KV=V1&HW-CC-Date=20260429T054652Z&HW-CC-Expire=86400&HW-CC-Sign=D9DDE1E886C2BB6643918C06E764781D8DDCC85461A3B9F4D7B72BF8A77AF1C4)，将同时清除设备日志缓存和HiLog窗口日志缓存，以及当前已经打印的日志。HiLog窗口将显示执行清除操作后，新输出至设备端缓存的日志信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/xytZ7Nd3RKmqNXh77JBlLQ/zh-cn_image_0000002561833493.png?HW-CC-KV=V1&HW-CC-Date=20260429T054652Z&HW-CC-Expire=86400&HW-CC-Sign=CC99F3E1715342C3C2A0AF75B7A851D04D938FFF8F6C7EB6B2A078ACAA7E69AC)

## 设置HiLog窗口缓存

HiLog窗口显示的日志信息保存在此窗口的缓存中，缓存的大小决定了当前窗口能显示的日志信息的最大数量，当日志超出缓存上限时，窗口中最早的日志将会被清除，新日志在窗口底部输出。开发者可以自行设置窗口的缓存大小。

点击Settings > Buffer，进入缓存设置窗口。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/gtCt0aL4RVKl_BDbZoIHYw/zh-cn_image_0000002561833471.png?HW-CC-KV=V1&HW-CC-Date=20260429T054652Z&HW-CC-Expire=86400&HW-CC-Sign=D098532F661847D11AB57E25EC237D98E203DE4DBA475AA9C580DBB648A76955)

默认缓存大小为4096K，变更缓存大小需重启HiLog窗口后生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/p20C30qxRMKotTer91vK4Q/zh-cn_image_0000002561833387.png?HW-CC-KV=V1&HW-CC-Date=20260429T054652Z&HW-CC-Expire=86400&HW-CC-Sign=4C2E422BE7CB25CA5ACB9FE0F1301A06F27909C8D5E299F70422AA79E249F219)

重启HiLog窗口操作：先点击下方的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/n9pllpu7Qd2Ilt-zKIcqhg/zh-cn_image_0000002530753542.png?HW-CC-KV=V1&HW-CC-Date=20260429T054652Z&HW-CC-Expire=86400&HW-CC-Sign=42F3E50CBE14F4B97845E5EBF9266E0E0271F55973BB21CDABA509E2EE4A358C)按钮，再点击上方的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/iM-wjLTYRtGj_iPwshjCDw/zh-cn_image_0000002530753544.png?HW-CC-KV=V1&HW-CC-Date=20260429T054652Z&HW-CC-Expire=86400&HW-CC-Sign=AA33B53C446803887252BD0E43FCEB2E33908059242B82182B60CEB5E09A9F29)按钮中的Online Log即可。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/d_E5_6euQPimoKQfAWqDFg/zh-cn_image_0000002530753512.png?HW-CC-KV=V1&HW-CC-Date=20260429T054652Z&HW-CC-Expire=86400&HW-CC-Sign=5325977E98F0C3A532893F70099DE23E7DE7FFAA34D9FDF754B6124061A7D547)

当日志量超出缓存时，顶部的旧日志不断被清除，因而顶部日志信息处于不停滚动的状态。此时若想查看此处的日志信息，可在日志滚动时，点击右键，勾选**Pause Output**暂停窗口打印，查看完后再取消勾选，重新开始打印日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/26ZeWFhDT4y6UMUbACNypA/zh-cn_image_0000002561833489.png?HW-CC-KV=V1&HW-CC-Date=20260429T054652Z&HW-CC-Expire=86400&HW-CC-Sign=02537282B11F2A62D89952835F8645909D4E20BAC2435B187B30ABFE1D6FFF03)

## 设置设备端日志缓存

使用hdc shell hilog -g命令可查看当前设备端设置的日志缓存，默认为256K。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/yA_cOk95Q8ChBAmKSNpKgQ/zh-cn_image_0000002530753546.png?HW-CC-KV=V1&HW-CC-Date=20260429T054652Z&HW-CC-Expire=86400&HW-CC-Sign=6334730449DEE5614555E67B0DA35A65DD016CC17C1F165FDA46410DE4AF9F6A "点击放大")

使用hdc shell hilog -G命令可更改设备端日志缓存大小。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/1Wv4OS4xQCKfiT_m1sAT6A/zh-cn_image_0000002530753530.png?HW-CC-KV=V1&HW-CC-Date=20260429T054652Z&HW-CC-Expire=86400&HW-CC-Sign=05A03C2FC25990B2D885472DB29196DE57032BF3537F19B555F6F07B7400EB46 "点击放大")

配合-t参数可单独设置某一类型的日志缓存大小。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/Wr22FWjXRfmzlVlr-2XEYg/zh-cn_image_0000002530913464.png?HW-CC-KV=V1&HW-CC-Date=20260429T054652Z&HW-CC-Expire=86400&HW-CC-Sign=2DECDF047228CCEF4442C8A6A1AEFB03EEF060587D1627D3C6F04EA4A651772C "点击放大")

超出设备端缓存日志将被落盘于设备data/log/hilog路径下，开发者可在此目录下载历史hilog日志并查看。

## 查看/导出设备离线日志

DevEco Studio提供查看设备离线日志的功能，支持查看设备中/data/log/hilog路径中的日志，离线日志窗口中展示的是经过[解析](hilog-tool.md)和DevEco Studio格式化之后的日志。

点击HiLog窗口左上角New，随后点击Offline Log即可打开离线日志窗口。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/LekiMrdxTdO_vbQiBI2gQQ/zh-cn_image_0000002530753528.png?HW-CC-KV=V1&HW-CC-Date=20260429T054652Z&HW-CC-Expire=86400&HW-CC-Sign=59976A2BB47954794E593733636608FC9501266A204D80BB91CC0F251BD559AA)

离线日志窗口左边工具栏中的按钮、日志级别下拉框和搜索框和在线日志的功能一致，设备下拉框仅支持选择真机和模拟器。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/FbprFc8pSAWA0mpCWnhTwQ/zh-cn_image_0000002530913582.png?HW-CC-KV=V1&HW-CC-Date=20260429T054652Z&HW-CC-Expire=86400&HW-CC-Sign=DFFC3084602BA212FA927CB78395805CEC4E7487A3C7AF37D56C58687A8BC9A0)

离线日志支持通过时间筛选设备上的日志文件，默认时间范围为打开窗口时的前三十分钟，除显示格式外，也支持通过键入yyyyMMddHHmm后回车进行时间输入。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/tSdhnneDQVyLM_7c6vPMIA/zh-cn_image_0000002530753490.png?HW-CC-KV=V1&HW-CC-Date=20260429T054652Z&HW-CC-Expire=86400&HW-CC-Sign=4A56A326346EC629A0577135DD0D6E4566D63A572D2ABC66720490C2A0EE0E67)

在输入时间之后，日志文件下拉框会进行刷新，点击文件会从设备端下载并自动解析后输出到离线日志窗口。

由于最新的日志文件内容还在更新中，在达到设定的大小前，内容会不断增多。如果重新打开离线日志窗口或者修改时间，日志文件列表都会刷新，会从设备端重新下载最新的日志文件，解析的内容会更多。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/RP_QykWjQwexhPmKQ-UhZw/zh-cn_image_0000002530753480.png?HW-CC-KV=V1&HW-CC-Date=20260429T054652Z&HW-CC-Expire=86400&HW-CC-Sign=0F75E1E68C243691D2EDE40E00CF40ED75EDB0427A8549F134B184B839171C48)离线日志窗口能输出的文本量可参考[设置HiLog窗口缓存](ide-setup-hilog.md#section106741332995)进行设置，设置较小可能无法显示选择文件的所有日志，推荐设置6M(6144K)。

通过设置窗口的缓存大小可能无法展示完整的日志，可点击左侧工具栏的保存按钮导出离线日志，支持导出解析后未经DevEco Studio格式化的原始日志文件，导出的文件可以看到完整日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/KfaZbGC6TwSUy-b94BfAFw/zh-cn_image_0000002530753590.png?HW-CC-KV=V1&HW-CC-Date=20260429T054652Z&HW-CC-Expire=86400&HW-CC-Sign=D64C9FF9B7BDA86B3C85614B49D952EBB053FDDF8D610CD187581EC8444A16A5)

## 终止应用

从DevEco Studio 6.0.0 Beta5版本开始，在日志窗口点击**右键 > Force Stop App**，可以终止该日志所属进程的应用，不支持系统应用和release签名的应用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/owsqqnIEQV6hmMyC9ggDIw/zh-cn_image_0000002530753484.png?HW-CC-KV=V1&HW-CC-Date=20260429T054652Z&HW-CC-Expire=86400&HW-CC-Sign=C514FD3232C542D393DD3344D4AD1CF1DC01F022E5C72C273FAC457204AFD27A)
