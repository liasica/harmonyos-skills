---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-setup-hilog
title: 日志分析
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 日志与故障分析 > 日志分析
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:e6d4a75f6e4aa5fb6ccf01b0b7e022cfc8ea36ee65509417de0c6ceb7d46d098
---

鸿蒙电脑DevEco Studio提供了“**日志** **>** **HiLog**”窗口来查看设备当前所有应用实时打印的日志信息。点击DevEco Studio底部![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/xj2BQONaRUWb5Mh5wESDdA/zh-cn_image_0000002810750889.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=88485DCED9023F8972DCF6AED52FF3DCB0C774806E2E5024B02F32EF9BF79E78 "点击放大")图标打开日志面板并点击**HiLog**，进入HiLog日志面板。

HiLog默认显示的日志为以下6个部分：

| 第一列 | 第二列 | 第三列 | 第四列 | 第五列 | 第六列 |
| --- | --- | --- | --- | --- | --- |
| 时间戳 | 进程ID和线程ID | 日志标签 | 应用包名 | 日志级别 | 日志内容 |

开发者可通过设置包名、日志级别和搜索关键词来筛选日志信息，还可以使用自定义日志显示格式、日志导出、显示最新日志等功能。

HiLog窗口左侧各个按钮的作用为：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/C8aOHD1WQ6-pBujdlzOHcQ/zh-cn_image_0000002810750887.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=C396CC4E82836750CF1FC71404C170516391CC325205DD6B102CB9029FD7EE1F)：当该按钮处于选中状态时，日志自动换行显示，否则日志按行显示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/B3tI-VezQa6RCWGkp1X__Q/zh-cn_image_0000002810630793.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=4324EA81BD1085A32F2AF5C1939774F62753C4483D9056E24A0427BF86B009F9)：当该按钮处于选中状态时，日志自动滚动到窗口底部，否则停留在当前日志显示处。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/8rPlJPV3TFO4SWy0rfAxfw/zh-cn_image_0000002810630785.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=99CC599B2AEF7ACD76FE97E79D2E6039696D414B7161341386CE07A6149352D0)：单击该按钮可以清空窗口日志和设备缓存。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/wlsDZq7-QN-gDfnesbOCfA/zh-cn_image_0000002781471234.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=901EFCCB125125E88C495484251706CA86D6497F003262FEB35B58DE3136EC47)：单击该按钮可以对当前选择的设备屏幕进行截屏，并保存在本地。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/cpVTosqwRXyhE6cvs9O16g/zh-cn_image_0000002810630779.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=3E3F56C2DF6325918C668A8F96EF6BEB1BD4167BB1CCE10C92CD0055449FEB4E)：单击该按钮可以保存日志缓存到指定文件。

## 过滤日志

### 按关键字过滤日志

在HiLog搜索框中输入需要过滤的信息，即可过滤所有包含此信息的日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/JhI1eoEyS4OcvPRy_FRV8g/zh-cn_image_0000002781471230.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=61B3560EF7E8CA9BEE563305B6A56486DEF7823D9165B2872DDDB52685C359BE)按钮表示是否区分大小写，![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/fCsxfsc1RJqwOR7CE5cPTw/zh-cn_image_0000002810630781.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=8FCD160CEFFCBBDDD5435721B7235CE340C3D19EA6AD2597DFAEE2819A8462C8)按钮表示是否按照正则表达式匹配过滤。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/1y8rtjQFStCCbO_3LLtpLg/zh-cn_image_0000002810630783.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=DC0153D96698B5BE7694BF9152035724AFB5D8475E86D84F905BDFFC24F4421D)

### 使用默认提供的过滤配置

HiLog提供多种默认的过滤模式，无需反复输入关键字过滤日志信息，只需要切换相应的过滤项，即可快速过滤所需的日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/bl-3MlmqTgKTevs1FLFxIA/zh-cn_image_0000002781471248.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=856263156F073E2324169CB80A65C9D8DEC2E1182BA2CA1ACD714B65EFDB9168)

* 选中应用的所有日志：按照应用进程过滤日志。
* 选中应用的用户日志：按照应用进程过滤用户输出的日志。

当使用**选中应用的所有日志**或**选中应用的用户日志**时，进程过滤下拉框处于可选状态，可选择相应的选项过滤想查看的进程日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/S3M1PTBJR26mN-MxPnyqDw/zh-cn_image_0000002781311294.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=108D971FFD1A01AD8E956367A960792967A9CAA6CCF6D0FD199DA806EA4357FC)

### 按日志级别过滤日志

HiLog提供日志级别过滤，用来过滤一个或多个级别的日志。日志级别分为Debug、Info、Warn、Error、Fatal五个级别。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/ycCSITc4Qgq_WlAjgCm54w/zh-cn_image_0000002781311296.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=14B7D114800F7D7E7D836AB69C6A0AF07B7BE6BA707E855946A844A52D410853)

### 按自定义过滤项过滤日志

除默认过滤项外，HiLog还提供配置自定义过滤项的途径以供开发者按照实际需求过滤日志，并保存此过滤配置以供重复使用。

点击**新建自定义过滤配置**时将弹出自定义过滤配置窗口。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/bWdl_MoDTdedNSwFcxCDJw/zh-cn_image_0000002781471232.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=126BEBD5E5217529283C5C515F005C2F1743562EBF2087A4E07E5CC4410FCDD7)

先前介绍的过滤选项此处均可配置，同时增加了**应用包名**和**同步至所有工程**配置项。

* 同步至所有工程：此配置当前工程及其他所有工程均可用。
* 应用包名：按应用包名过滤日志。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/Dgsq-g_GTdeSU4LJ7hhzJw/zh-cn_image_0000002810750895.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=1D10FD2B3E0797083BA108484097805FE101EE00D7277D6C94431FF425D37DB6)

当配置完后将自动切换至此过滤配置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/VAYkDjEbR32GbPuJRPdorA/zh-cn_image_0000002781471244.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=A9E10BEA601ADA320CDF21FDE00E2D401C8A8B560AE4EAC56E8A0634B4ECDEA7)

切换至此自定义配置时，日志级别过滤窗口和关键字过滤窗口将在此自定义配置过滤出的日志的基础上再进行过滤。

## 修改日志显示格式

支持开发者修改日志显示的格式。点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/NcRvsKFsQVe65IHDi0kvPw/zh-cn_image_0000002781471228.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=78D90E3FF6A7B730BBA83D114D26B9694759A81229DC85E1FC486C132BB98EF3 "点击放大")图标。

* 标准视图：默认显示所有信息。
* 紧凑视图：默认显示日志级别与日志信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/sX0IqrzQR7-pRUmh_6Ielg/zh-cn_image_0000002810630789.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=9A0E1A114B5AAE905C970D0293C6AF7784445DFF3C73A2F818D60F7592DB4D44)

## 超长日志自动换行

当单行日志过长时，用户可点击自动换行来使日志信息自适应当前窗口宽度，在末尾自动换行，在当前窗口中完整显示。

当日志消息过长时，日志窗口可能不能完整显示，需要拖动滚动条查看信息。此时开发者可以点击按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/cJM4BWFSRfyjrOkgtUGjiQ/zh-cn_image_0000002781471236.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=0E4BC7E8C99466EE82883203F5D52D3300A665D3A4CA8F7D24FC2D4BA497F819)控制日志消息自动换行。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/sAzBWYVNRj2i-boVDMCJCg/zh-cn_image_0000002810750897.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=AF01A3399F9A09F17A4C91A6FDE73713748A93A87FD44E7EA035D0A9BD3CE3C8)

## 显示最新日志

设备输出的日志信息会实时刷新到HiLog窗口底部，用户可点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/O5yTUzBjShm0nm12AqYvCg/zh-cn_image_0000002781471246.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=47A7DF1997566A9A9600F9C7EBEE04DABD7BA192E5C6D8145B25E22E97454618)按钮使HiLog一直显示底部的最新日志信息。当观察到需要的日志时，点击HiLog窗口，即可停止滚动，停留在当前行，以便查看日志信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/Hcg4NBWiQHO6UjMuE0fmbA/zh-cn_image_0000002810630791.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=459CE693A2D319662742B798F53DE8573F803B5C5ECFF739D1A3D20CB65C42AB)

## 导出日志信息

开发者可将经过过滤后的关键日志信息保存到本地，以便进一步分析。

点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/6XXqgNWyQEiAW8I5-nTn9w/zh-cn_image_0000002781311298.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=B85EDDD62B9BC03F250234FD9A8BCF1632A4FFC5E01A2C4628714A3800425A4D "点击放大")按钮，在弹出的窗口中选择保存路径。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/lMzCaQg5QkCaOMvpjOhzLQ/zh-cn_image_0000002810750891.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=33A242A867FD6D74C3E32C4031196CDC220D5FBCFE54C51C25196BCDE9CFBA90)

## 清除日志缓存

与日志相关的缓存有两个：设备端日志缓存、HiLog窗口缓存。

HiLog显示日志信息的流程为：

1. 应用输出日志信息至设备端日志缓存；
2. 日志组件将设备端日志缓存取出，保存在HiLog窗口缓存中；
3. HiLog窗口根据过滤条件，将HiLog窗口缓存中的消息显示在界面中。

点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/WXAEmj21TGGzicqJY-DCEA/zh-cn_image_0000002810750899.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=D58838B48EB6BE19DD04BEAC868EC0DDBCA57AD3233E2C5E4B047B5DBE8D5305)按钮，将弹出两个选项**：清除控制台日志**、**清除设备日志**。

* **清除控制台日志**：清除HiLog窗口日志缓存。日志组件将重新从设备端日志缓存读取日志消息，因而执行清除操作前已保存在设备端日志缓存的日志消息会显示到HiLog窗口中。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/Lrpaa7RER1ag3dQbFRMVBQ/zh-cn_image_0000002781311312.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=6286D152182803C7E2E5FB8EE9C57E5167F5A50B73A2BA3120DD579A4B3ECF4F)
* **清除设备日志**：清除设备端日志缓存。此操作将清除设备端日志缓存和HiLog窗口缓存。HiLog窗口将显示执行清除操作后，新输出至设备端缓存的日志信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/-2k9k0fPSMqiqnMcR4iVVg/zh-cn_image_0000002810750903.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=21D0D2B57CA69E354D4C61AE0D26D40E9B27FB5EC0204549E777BA0B7F80A210)

## 设置HiLog窗口缓存

HiLog窗口显示的日志信息保存在此窗口的缓存中，缓存的大小决定了当前窗口能显示的日志信息的最大数量，当日志超出缓存上限时，窗口中最早的日志将会被清除，新日志在窗口底部输出。开发者可以自行设置窗口的缓存大小。

进入**文件 > 设置 > 扩展 > HiLog Console**面板，或点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/eEfF3PRrRL2lLsIZBi4s5w/zh-cn_image_0000002810750893.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=2A3D1486CBAADE80DBF433B1EC8DBF5917A73B2371F792CA4733587C7FAF6015 "点击放大")图标，选择控制台设置 > 缓冲区，默认缓存大小为4096KB，变更缓存大小后实时生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/Vzk43rfUTwCwUtoyc_2-xQ/zh-cn_image_0000002781311310.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=48389A9CC1E008BC42C30C2A8ACF61E9F0499EDEB57A5D39D635828F71CCD9BA)

## 设置设备端日志缓存

使用hdc shell hilog -g命令可查看当前设备端设置的日志缓存。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/gbeTjU4hS8eGt3G8ZaeXaA/zh-cn_image_0000002781311300.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=2BD585BC927125812491C7B2CCC6CF5BE3F72AA8A2B331A5413D9992C28FAA06)

使用hdc shell hilog -G命令可更改设备端日志缓存大小。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/ExclUtFeSS2fVHDRlxu6bA/zh-cn_image_0000002810750901.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=41A744F68C24D8F579189D2ABDC21226A97352F4CB234EB76DAAAD7F722B4A5E)

配合-t参数可单独设置某一类型的日志缓存大小。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/0hi7czocRlSLm0nixcAZTQ/zh-cn_image_0000002810630787.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=FEBB115654992EE8FE28E6950CF8631273E540E0DFF20B5473E289047186BFB1)

超出设备端缓存日志将被落盘于设备data/log/hilog路径下，开发者可在此目录下载历史hilog日志并查看。
