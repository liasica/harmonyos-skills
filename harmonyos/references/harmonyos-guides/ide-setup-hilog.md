---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-setup-hilog
title: 日志分析
breadcrumb: 指南 > 编写与调试应用 > 日志与故障分析 > 日志分析
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:21e74f91556566609fd215341e96c3358817b3361e94cd652fc49e1d5fbd6fba
---

说明

打印日志请查看[使用HiLog打印日志](hilog-guidelines-arkts.md)。

DevEco Studio提供了“Log > HiLog”窗口查看设备当前所有应用实时打印的日志信息。HiLog默认显示的日志为以下6个部分。

| 第一列 | 第二列 | 第三列 | 第四列 | 第五列 | 第六列 |
| --- | --- | --- | --- | --- | --- |
| 时间戳 | 进程ID和线程ID | 日志标签 | 应用包名 | 日志级别 | 日志内容 |

开发者可通过设置包名、日志级别和搜索关键词来筛选日志信息，还可以使用自定义日志显示格式、日志导出、显示最新日志等功能。

HiLog窗口左侧各个按钮的作用为：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/k5CYnXhcRpG0CGyjCoNYsQ/zh-cn_image_0000002561833479.png?HW-CC-KV=V1&HW-CC-Date=20260427T235656Z&HW-CC-Expire=86400&HW-CC-Sign=6A70F72264934FFBAE6DCB79F2FE4EF91E4AABFAF9B941F896BE7938130C75D5)：单击该按钮可以向上翻页，日志窗口取消自动滚动。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/oymg6essQBemMsJ-F4GiPg/zh-cn_image_0000002530753502.png?HW-CC-KV=V1&HW-CC-Date=20260427T235656Z&HW-CC-Expire=86400&HW-CC-Sign=C2990A0456A039994F88AB2521D4365AF6C229AC92D9063EBB8B78F099B4FE1A)：单击该按钮可以向下翻页，日志窗口取消自动滚动。如果翻页已到底部，日志窗口自动滚动。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/iZlpYvNtSV-PGnwxnTFb3w/zh-cn_image_0000002561753505.png?HW-CC-KV=V1&HW-CC-Date=20260427T235656Z&HW-CC-Expire=86400&HW-CC-Sign=471D8EC9990EAC11F45F813A9B904A093452F37767DB1D133A09E22F0FAFEC29)：当该按钮处于选中状态时，日志自动换行显示，否则日志按行显示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/l8K0GwmEQYq_vAw5kF87eA/zh-cn_image_0000002530753540.png?HW-CC-KV=V1&HW-CC-Date=20260427T235656Z&HW-CC-Expire=86400&HW-CC-Sign=162F243D2CE6FE263F220AD7C79474231611D4BADCFF83B3C5D68BF93EB968D9)：当该按钮处于选中状态时，日志自动滚动到窗口底部，否则停留在当前日志显示处。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/eboqIh9hTyegP1nfzgwruA/zh-cn_image_0000002530753488.png?HW-CC-KV=V1&HW-CC-Date=20260427T235656Z&HW-CC-Expire=86400&HW-CC-Sign=0BC9A9A79351C69871E11A667ACA6FA8C5E1DD40E64CA04F943862488DA46F0A)：单击该按钮可以重新开启日志接收，会重新加载设备缓存日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/c0F7PZaJQDebS221qE1eUw/zh-cn_image_0000002530753504.png?HW-CC-KV=V1&HW-CC-Date=20260427T235656Z&HW-CC-Expire=86400&HW-CC-Sign=33308C114EB938B3AC3A9CBDECCAAAAC0FC9911DC787D8B5BBE3BB54E41827EB)：单击该按钮可以清空窗口日志和设备缓存。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/xyVWF3CCQSiCIiUSePdTcA/zh-cn_image_0000002530913472.png?HW-CC-KV=V1&HW-CC-Date=20260427T235656Z&HW-CC-Expire=86400&HW-CC-Sign=1623E2F65013D3FEBB80E427F3E72993AFC8213FEE4B732AF6051F5A691CAC2F): 单击该按钮可以对当前选择的设备屏幕进行截屏，并保存在本地。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/r3uVIJ5YRtm7YT6LvOmEag/zh-cn_image_0000002561833497.png?HW-CC-KV=V1&HW-CC-Date=20260427T235656Z&HW-CC-Expire=86400&HW-CC-Sign=46AC9CDAB0B0873CBCB6D051204F912D2E5BA38DD093F9D85EB2FCEAAEBA0922): 单击该按钮可以对当前选择的设备进行录屏，并保存在本地。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/QfUCKh3WTo6jGcsrIFDlBA/zh-cn_image_0000002561753515.png?HW-CC-KV=V1&HW-CC-Date=20260427T235656Z&HW-CC-Expire=86400&HW-CC-Sign=8011D99F37192DEFF77AAFE558CE4181BCB6D53BAABCB46C6E42CE4E2BDAB93F)：单击该按钮可以保存日志缓存到指定文件（在线日志）或保存离线日志文件（离线日志）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/QqUiu_gWSKGozajOAKBFkg/zh-cn_image_0000002530753468.png?HW-CC-KV=V1&HW-CC-Date=20260427T235656Z&HW-CC-Expire=86400&HW-CC-Sign=6992DAF98782A93BB20CB1B00FAF886639E415BACEB4941E17946EDCFFAD1AE8)：单击该按钮可以自动选择和切换已连接的设备。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/0G85op2xR8-hDaQHDvq5dQ/zh-cn_image_0000002561833487.png?HW-CC-KV=V1&HW-CC-Date=20260427T235656Z&HW-CC-Expire=86400&HW-CC-Sign=572D010CD48DE21263E8973D4E3CE90317C3BD38A3893332CFF0B5A75C3299D4)：单击该按钮可以切换日志视图以及自定义日志格式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/Uuqphr0SRdaM0Z9MRMcP7w/zh-cn_image_0000002530753506.png?HW-CC-KV=V1&HW-CC-Date=20260427T235656Z&HW-CC-Expire=86400&HW-CC-Sign=E5075CA459E6386CBD896A1FD041CC4A0D58EF0CC108983D1A1834B00A24BCC0)：单击该按钮可以关闭当前日志窗口。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/Pzyk-PLlQEeqI1xcN-fiZA/zh-cn_image_0000002530753508.png?HW-CC-KV=V1&HW-CC-Date=20260427T235656Z&HW-CC-Expire=86400&HW-CC-Sign=26A57EB7A69DF9C40BCB2ECDF489961DF5703A4AE296E9677FEB594ECCE9C795)：单击该按钮可以跳转到HiLog日志相关的在线帮助文档。

## 过滤日志

### 按关键字过滤日志

在HiLog搜索框中输入希望过滤的信息，即可过滤显示所有包含此信息的日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/7DVjE4aiSSmGeRz3OcpVSg/zh-cn_image_0000002561833393.png?HW-CC-KV=V1&HW-CC-Date=20260427T235656Z&HW-CC-Expire=86400&HW-CC-Sign=8184914DF275D878E56B4E28000983A163C3C7C102C38778C4092CA88E346753)按钮表示过滤是否区分大小写，![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/nWbQ4E7nQ9eyz7nVtwOtvQ/zh-cn_image_0000002561833477.png?HW-CC-KV=V1&HW-CC-Date=20260427T235656Z&HW-CC-Expire=86400&HW-CC-Sign=C6A6B4192E204EC52E8E603D6F6750715ECC909809149DEC29B20941E52A5862)按钮表示是否按照正则表达式匹配过滤。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/irH7NJgTTPugcIJwWxI4Ug/zh-cn_image_0000002530913574.png?HW-CC-KV=V1&HW-CC-Date=20260427T235656Z&HW-CC-Expire=86400&HW-CC-Sign=D9882444B041A004F79F78A347AB7EB7AC1D0694FB501E6DC44DAE4E0E32C91D)

从DevEco Studio 6.0.2 Beta1版本开始，支持使用逻辑运算符&拼接多个关键字，精准搜索日志，&字符前后要有空格。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/Um6izB_jSwG1_TGiZRExNQ/zh-cn_image_0000002530753472.png?HW-CC-KV=V1&HW-CC-Date=20260427T235656Z&HW-CC-Expire=86400&HW-CC-Sign=839BD4A5034DC959860815BF3783A8D6A57FA8B102E0ACDB84D19573C950884F "点击放大")

### 使用默认提供的过滤配置

HiLog提供多种默认的过滤模式，开发者不需要反复输入关键字过滤日志信息，只需要切换相应的过滤项，即可快速过滤所需的日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/roMc_eO4TDGScJ9n_9SDsA/zh-cn_image_0000002530913576.png?HW-CC-KV=V1&HW-CC-Date=20260427T235656Z&HW-CC-Expire=86400&HW-CC-Sign=7E275A02310B9D7EAA748C9D7CD2911B2C6E732F8CCF91A4A3D9A5A12AA9A911)

* All logs of selected app：按照应用进程过滤日志。
* User logs of selected app：按照应用进程过滤用户输出的日志。

当选择All logs of selected app或User logs of selected app时，进程过滤下拉框处于可选状态，可选择相应的选项过滤想查看的进程日志。

说明

由于设备启动时，USB调试开关没有开启，部分系统应用没注册上，HiLog进程列表无法显示未注册上的系统应用，如需查看此部分的日志，可以[按关键字过滤](ide-setup-hilog.md#section1264082914019)查看，或者保持USB调试开关打开的状态，重启设备。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/OnglzzXOTmuhfGPX9oD2tw/zh-cn_image_0000002530753494.png?HW-CC-KV=V1&HW-CC-Date=20260427T235656Z&HW-CC-Expire=86400&HW-CC-Sign=6D7C345DBEE5271A508FB7EC257E80B7CA8E37386388E7CFEFCFC8B3DD08C441)

进程选择窗口可输入PID或应用名的关键字搜索要过滤的进程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/RUyS_jzyR82fqKTJ5iI45g/zh-cn_image_0000002530913530.png?HW-CC-KV=V1&HW-CC-Date=20260427T235656Z&HW-CC-Expire=86400&HW-CC-Sign=472EEF9C1772D85B4E33887BC641FFA5A466B5B3FE5B314C89688EC2CE41DE19)

### 按日志级别过滤日志

HiLog提供日志级别过滤以过滤某一级别及以上的日志。日志级别分为Debug、Info、Warn、Error、Fatal五个级别。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/zjg2zsWIR5mhbu06RbdfCQ/zh-cn_image_0000002561833475.png?HW-CC-KV=V1&HW-CC-Date=20260427T235656Z&HW-CC-Expire=86400&HW-CC-Sign=4868EB24D310EECB26B88CDDDD09B608DE4F94B5D3A07E6799F788E05A39D402)

如选择Warn级别，则过滤展示Warn级别与Warn级别以上的日志信息，即展示Warn、Error、Fatal3个级别。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/w-KFAUVMRqiGiexLFjUNXw/zh-cn_image_0000002530753550.png?HW-CC-KV=V1&HW-CC-Date=20260427T235656Z&HW-CC-Expire=86400&HW-CC-Sign=349B18B0C1FC12FC0169D6242B9AF6E4681773B34695D0001E344F4A9C4CBE71)

### 按自定义过滤项过滤日志

除默认过滤项外，HiLog还提供配置自定义过滤项的途径以供开发者按照实际需求过滤日志，并保存此过滤配置以供重复使用。

点击**Config custom filter**时将弹出自定义过滤配置窗口。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/lNBfX8mNTRuM2ugBeGat1A/zh-cn_image_0000002530753496.png?HW-CC-KV=V1&HW-CC-Date=20260427T235656Z&HW-CC-Expire=86400&HW-CC-Sign=2390E37157E4ABD0553C96383288EF86B64DE84E5CCCF4C9AD74227A5082631C)

先前介绍的过滤选项此处均可配置，同时增加了Package name和Set to all projects配置项。

* Set to all projects：此配置当前工程及其他所有工程均可用。
* Package name：按应用包名过滤日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/J-xH9DS-SbiCcXfJXA3GdQ/zh-cn_image_0000002530753522.png?HW-CC-KV=V1&HW-CC-Date=20260427T235656Z&HW-CC-Expire=86400&HW-CC-Sign=5021F910808947B81321D90C11E526BC1679CF93C0AA55E01659049BCCCB0F92)

当配置完后将自动切换至此过滤配置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/iyYuZIxLQ5u88IPuqZKNEQ/zh-cn_image_0000002530753486.png?HW-CC-KV=V1&HW-CC-Date=20260427T235656Z&HW-CC-Expire=86400&HW-CC-Sign=A3474514BA6C9D08B3429B17000E2BA52C68D8A818C4178711CAED6387B521B7)

切换至此自定义配置时，日志级别过滤窗口和关键字过滤窗口将在此自定义配置过滤出的日志的基础上再进行过滤。

## 自定义日志显示格式

开发者可以通过配置自定义格式，限制每条日志只显示用户关注的信息。

点击左侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/sMgr2mf8TvevrQ5lEv8lCA/zh-cn_image_0000002530753524.png?HW-CC-KV=V1&HW-CC-Date=20260427T235656Z&HW-CC-Expire=86400&HW-CC-Sign=E383539F7D47E59DE60B09E6BC34DD60F99B68E913E0DBF64F1E9B7FD1A374BE)图标，将弹出自定义格式窗口。

* Standard Views：默认显示所有信息。
* Compact Views：默认显示日志级别与日志信息。
* Modify Views：进入“Hilog Format”窗口后，可以按照需要自定义日志格式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/a1WIsAC4SISIxsUGTVhubA/zh-cn_image_0000002561833469.png?HW-CC-KV=V1&HW-CC-Date=20260427T235656Z&HW-CC-Expire=86400&HW-CC-Sign=6B45D5206D47C152C89BFD7AA7BA73AEBC60C39A914597ED269CC6EDDC9D7BB8)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/epcO9VMxR5yJ1p1PY9zB6g/zh-cn_image_0000002530753516.png?HW-CC-KV=V1&HW-CC-Date=20260427T235656Z&HW-CC-Expire=86400&HW-CC-Sign=0542310D0F79BDCA36644B5C9E3B23DCDD98025EB08AA1EF0C449F4FF960E0F7)

## 超长日志自动换行

当日志的消息过长时，日志窗口可能不能完整显示日志消息，需要拖动滚动条查看信息。此时开发者可以点击**Soft-Wrap**按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/ZLjsLS7KRdS1OXWi5ew_fA/zh-cn_image_0000002561833481.png?HW-CC-KV=V1&HW-CC-Date=20260427T235656Z&HW-CC-Expire=86400&HW-CC-Sign=876F6CD97AC16A25083AF916D0E670CA6FCE4109212E63CBF0CA8A91486A8520)控制日志消息自动换行。

**图1** 未开启自动换行

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/AeQBkDKHRFKruAVhku4RbA/zh-cn_image_0000002561833505.png?HW-CC-KV=V1&HW-CC-Date=20260427T235656Z&HW-CC-Expire=86400&HW-CC-Sign=BBBB15DB8628F01B4138E5457F2337FDD4B50DE4516EBB553BF92D277C5DCADF)

**图2** 开启自动换行

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/_1tZCkt9SyuHOPMQL-p0Uw/zh-cn_image_0000002530753518.png?HW-CC-KV=V1&HW-CC-Date=20260427T235656Z&HW-CC-Expire=86400&HW-CC-Sign=38197BEA0E6AC8194890C5059D720227FCE51D912401E68D1C5E7935579A4BD0)

## 显示最新日志

设备输出的日志信息会实时刷新到HiLog窗口底部，用户可点击**Scroll to End**按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/dqmryn4yTo6EZCG7VjdrQQ/zh-cn_image_0000002561753415.png?HW-CC-KV=V1&HW-CC-Date=20260427T235656Z&HW-CC-Expire=86400&HW-CC-Sign=03B8DA41EE73658DF9823F92F43F4544CDCB5BD05F95E24EE8568A9FC7A5DC71)使HiLog一直显示底部的最新日志信息。当观察到需要的日志时，点击HiLog窗口，即可停止滚动，停留在当前行，以便查看日志信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/zDdMjlhfRzOWOwVHYSHx9Q/zh-cn_image_0000002561833451.gif?HW-CC-KV=V1&HW-CC-Date=20260427T235656Z&HW-CC-Expire=86400&HW-CC-Sign=64B3D138692F3473BFAB890B44AEDD2404BB3F0FDAF856CC384325837C3ABBAB)

## 导出日志信息

用户可将经上述步骤过滤后的关键日志信息保存到本地，以便后续的进一步分析。

点击**Export HiLog**按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/spMn10jJTMaWFDrf-cEAFg/zh-cn_image_0000002530753526.png?HW-CC-KV=V1&HW-CC-Date=20260427T235656Z&HW-CC-Expire=86400&HW-CC-Sign=F8F708D6B404B383416D4BB195D4DE533B0290F0FFC870321D2D07A0EDE258A3)，在弹出的Export HiLog To窗口中选择保存路径。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/RXFItC44RF6Rt1_etxvXjw/zh-cn_image_0000002561753473.png?HW-CC-KV=V1&HW-CC-Date=20260427T235656Z&HW-CC-Expire=86400&HW-CC-Sign=2F4F4BF16FFA1F0F2B2F2A32FD885451FD34670903DA36CA6170A925FBED9B48)

## 清除日志缓存

与日志相关的缓存有两个：设备端日志缓存、HiLog窗口缓存。

HiLog显示日志信息的流程为：

1. 应用输出日志信息至设备端日志缓存；
2. Log组件将设备端日志缓存取出，保存在HiLog窗口缓存中；
3. HiLog窗口根据过滤条件，将HiLog窗口缓存中的消息显示窗口在界面中。

点击**Clear All**按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/jZoH6HWzSOm_vUUVAaBpJA/zh-cn_image_0000002530753514.png?HW-CC-KV=V1&HW-CC-Date=20260427T235656Z&HW-CC-Expire=86400&HW-CC-Sign=AADDBC5A4B05DC5CF7D33CB5AB3FC5F09C6489684DC352919191CCC3096B7ABD)，将同时清除设备日志缓存和HiLog窗口日志缓存，以及当前已经打印的日志。HiLog窗口将显示执行清除操作后，新输出至设备端缓存的日志信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/Ki7JJns5Qki05sJMEdDzHQ/zh-cn_image_0000002561833493.png?HW-CC-KV=V1&HW-CC-Date=20260427T235656Z&HW-CC-Expire=86400&HW-CC-Sign=66E2EECF03C869FE278B2C7EBA55B7DBBEAEF686B87B6C11344DBCF21A070192)

## 设置HiLog窗口缓存

HiLog窗口显示的日志信息保存在此窗口的缓存中，缓存的大小决定了当前窗口能显示的日志信息的最大数量，当日志超出缓存上限时，窗口中最早的日志将会被清除，新日志在窗口底部输出。开发者可以自行设置窗口的缓存大小。

点击Settings > Buffer，进入缓存设置窗口。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/kp1Bk5A9SRmvk-LZcfWRvA/zh-cn_image_0000002561833471.png?HW-CC-KV=V1&HW-CC-Date=20260427T235656Z&HW-CC-Expire=86400&HW-CC-Sign=B880CA47DC8507D7B19B59EE9D7D41C52A62CF3A3654BF4F95AB4C442E8D026B)

默认缓存大小为4096K，变更缓存大小需重启HiLog窗口后生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/wwx6bqkrQFKqMugo6sNtTQ/zh-cn_image_0000002561833387.png?HW-CC-KV=V1&HW-CC-Date=20260427T235656Z&HW-CC-Expire=86400&HW-CC-Sign=59A4C145BD953F0EC50834E2A2A2995214044FCEAAA8B7722B29AD21B667B4CC)

重启HiLog窗口操作：先点击下方的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/P1XORut9SLGUg7qZPJpEVA/zh-cn_image_0000002530753542.png?HW-CC-KV=V1&HW-CC-Date=20260427T235656Z&HW-CC-Expire=86400&HW-CC-Sign=7A135234D9A0FCD8B135AA104B8BA8D46A7C6E877D9F018A2DF610997423F123)按钮，再点击上方的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/YO35IaJNTlipc_hKAqPIng/zh-cn_image_0000002530753544.png?HW-CC-KV=V1&HW-CC-Date=20260427T235656Z&HW-CC-Expire=86400&HW-CC-Sign=3989B2BD608BDDCA99E0C6559C8291E4911B8125D1E85AAB776ACE7BFBC8F230)按钮中的Online Log即可。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/Xg1QEJYXRV6W3LBOgHf0Qg/zh-cn_image_0000002530753512.png?HW-CC-KV=V1&HW-CC-Date=20260427T235656Z&HW-CC-Expire=86400&HW-CC-Sign=4F34FD5A15D810CF980175F1421149F99C55387AAC495128E2BDC7CF5C36F6FD)

当日志量超出缓存时，顶部的旧日志不断被清除，因而顶部日志信息处于不停滚动的状态。此时若想查看此处的日志信息，可在日志滚动时，点击右键，勾选**Pause Output**暂停窗口打印，查看完后再取消勾选，重新开始打印日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/wsDlCrAZRuO_PEsQu51oZQ/zh-cn_image_0000002561833489.png?HW-CC-KV=V1&HW-CC-Date=20260427T235656Z&HW-CC-Expire=86400&HW-CC-Sign=11EFD5A2DBFE009F89CDF83624DBE2ADFBCAA5972B01DA1C0E2C962AF7E6AE06)

## 设置设备端日志缓存

使用hdc shell hilog -g命令可查看当前设备端设置的日志缓存，默认为256K。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/9J2cpM6XRCmbeFYPh7UdZQ/zh-cn_image_0000002530753546.png?HW-CC-KV=V1&HW-CC-Date=20260427T235656Z&HW-CC-Expire=86400&HW-CC-Sign=9E247904176402760D38B6CF9AC6965FC5AE53B348EFC9B28571A3E291177440 "点击放大")

使用hdc shell hilog -G命令可更改设备端日志缓存大小。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/Za7c2AyaQHKegeu5uf8fZg/zh-cn_image_0000002530753530.png?HW-CC-KV=V1&HW-CC-Date=20260427T235656Z&HW-CC-Expire=86400&HW-CC-Sign=4D5326538FAD13ACE299CB6E1FA49E1C003243980B745E06D681AD8B06DD69D5 "点击放大")

配合-t参数可单独设置某一类型的日志缓存大小。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/FFFP6uqcRTOOiSAcFxY3Lg/zh-cn_image_0000002530913464.png?HW-CC-KV=V1&HW-CC-Date=20260427T235656Z&HW-CC-Expire=86400&HW-CC-Sign=222CDF28A10D43DE0B223BCED95DF756476192296C8323B42F1CAB4ED468EA87 "点击放大")

超出设备端缓存日志将被落盘于设备data/log/hilog路径下，开发者可在此目录下载历史hilog日志并查看。

## 查看/导出设备离线日志

DevEco Studio提供查看设备离线日志的功能，支持查看设备中/data/log/hilog路径中的日志，离线日志窗口中展示的是经过[解析](hilog-tool.md)和DevEco Studio格式化之后的日志。

点击HiLog窗口左上角New，随后点击Offline Log即可打开离线日志窗口。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/YLpBc4MkSWigEaMe7FI-YA/zh-cn_image_0000002530753528.png?HW-CC-KV=V1&HW-CC-Date=20260427T235656Z&HW-CC-Expire=86400&HW-CC-Sign=0981BAB6B49C325B4012A9278BD7B582BA5C4E2EC747E571D0FCE0E392C73D0E)

离线日志窗口左边工具栏中的按钮、日志级别下拉框和搜索框和在线日志的功能一致，设备下拉框仅支持选择真机和模拟器。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/slQyv8eySgqc5Wnhh8AjLg/zh-cn_image_0000002530913582.png?HW-CC-KV=V1&HW-CC-Date=20260427T235656Z&HW-CC-Expire=86400&HW-CC-Sign=7B02D62BDA99514AD94251D5221248E32F543EE5F2649C186DEA14AD6B27C020)

离线日志支持通过时间筛选设备上的日志文件，默认时间范围为打开窗口时的前三十分钟，除显示格式外，也支持通过键入yyyyMMddHHmm后回车进行时间输入。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/KvA4sbhOQIaeoUn1M7k4Aw/zh-cn_image_0000002530753490.png?HW-CC-KV=V1&HW-CC-Date=20260427T235656Z&HW-CC-Expire=86400&HW-CC-Sign=2930AD3DE1EC6000FDF43EE57A22A46C6C55CC5429C1F937E41D7FBB752DF5D0)

在输入时间之后，日志文件下拉框会进行刷新，点击文件会从设备端下载并自动解析后输出到离线日志窗口。

由于最新的日志文件内容还在更新中，在达到设定的大小前，内容会不断增多。如果重新打开离线日志窗口或者修改时间，日志文件列表都会刷新，会从设备端重新下载最新的日志文件，解析的内容会更多。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/UMASAQCfTKee2AISbSZFXQ/zh-cn_image_0000002530753480.png?HW-CC-KV=V1&HW-CC-Date=20260427T235656Z&HW-CC-Expire=86400&HW-CC-Sign=FCE6D79981E5D5D1DCA8FCCF84BC978643FD6651D9D3FA118E3487E56D49D938)离线日志窗口能输出的文本量可参考[设置HiLog窗口缓存](ide-setup-hilog.md#section106741332995)进行设置，设置较小可能无法显示选择文件的所有日志，推荐设置6M(6144K)。

通过设置窗口的缓存大小可能无法展示完整的日志，可点击左侧工具栏的保存按钮导出离线日志，支持导出解析后未经DevEco Studio格式化的原始日志文件，导出的文件可以看到完整日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/k8MDnVFIQSCO6IbnVKpoDQ/zh-cn_image_0000002530753590.png?HW-CC-KV=V1&HW-CC-Date=20260427T235656Z&HW-CC-Expire=86400&HW-CC-Sign=F60C09E68373772F7486BF6B72C96EB9EB096E2B3E55C857ACC3B0C1A38A0393)

## 终止应用

从DevEco Studio 6.0.0 Beta5版本开始，在日志窗口点击**右键 > Force Stop App**，可以终止该日志所属进程的应用，不支持系统应用和release签名的应用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/Hd3COJ4yThipK6HMsxTDhQ/zh-cn_image_0000002530753484.png?HW-CC-KV=V1&HW-CC-Date=20260427T235656Z&HW-CC-Expire=86400&HW-CC-Sign=56F59274E0272096483A12B444C9BAED6954F1EF4F374488A6D8C5792D76BC3A)
