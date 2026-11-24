---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-setup-hilog
title: 日志分析
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 日志与故障分析 > 日志分析
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:31+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:cc5058c5dedce42c733229d0ccb91d05352f86e98703233612a334cfe07c9f0b
---

**说明** 

打印日志请查看[使用HiLog打印日志](hilog-guidelines-arkts.md)。

DevEco Studio提供了“Log > HiLog”窗口查看设备当前所有应用实时打印的日志信息。HiLog默认显示的日志为以下6个部分。

| 第一列 | 第二列 | 第三列 | 第四列 | 第五列 | 第六列 |
| --- | --- | --- | --- | --- | --- |
| 时间戳 | 进程ID和线程ID | 日志标签 | 应用包名 | 日志级别 | 日志内容 |

开发者可通过设置包名、日志级别和搜索关键词来筛选日志信息，还可以使用自定义日志显示格式、日志导出、显示最新日志等功能。

HiLog窗口左侧各个按钮的作用为：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/7aCH8HRHR4-q_gnhwwTVRg/zh-cn_image_0000002779567490.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=F36604CABD4DF14CF892CFB4CB1BFB6D0338A0A97F1EBF8125905EDC3AEC3F1B)：单击该按钮可以向上翻页，日志窗口取消自动滚动。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/J-BAZnpeQSSvx3wJSez7qg/zh-cn_image_0000002808887127.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=2BD2A08E46687311464BC2E5DA6003296141149492A337A36F3D777DAE4B9574)：单击该按钮可以向下翻页，日志窗口取消自动滚动。如果翻页已到底部，日志窗口自动滚动。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/3CSZjLg_QYqbSBAQ3e1cwQ/zh-cn_image_0000002779567492.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=719DC55D90E017E48B93B1991E5FE6669D0D40FEBC2D6D96B9BF508C088FBB93)：当该按钮处于选中状态时，日志自动换行显示，否则日志按行显示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/4-rOXwklRICmiQavLwK-1g/zh-cn_image_0000002779407502.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=4D6237CEE9E66DD65A25884B3284B7ABEE5FD5E1EA8F6E2F54FE97148E6C8A77)：当该按钮处于选中状态时，日志自动滚动到窗口底部，否则停留在当前日志显示处。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/7XBR27KUTsqtNzhA_nfVbA/zh-cn_image_0000002779567462.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=7020A1800C9F4F6485896C6758AFD1FD1521D6370B80C5DC53D7CACAA6B76CCD)：单击该按钮可以重新开启日志接收，会重新加载设备缓存日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/Urob7j2RR_i89NJCZlgGVg/zh-cn_image_0000002779567466.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=9F94966193DDC4FF2CEA484D3896B76648EF456581845ACED2DB080C476557DF)：单击该按钮可以清空窗口日志和设备缓存。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/e8cHpIhDTIyFzfnwSIOE-g/zh-cn_image_0000002779567460.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=CB71868432EA1520AEAF9F520ADF7DF0D7EECF82C74D8710FC00EE07E342D00B)：单击该按钮可以对当前选择的设备屏幕进行截屏，并保存在本地。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/0kRDVw8lR02-dfBCxMZeuw/zh-cn_image_0000002808767075.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=05B10E7AB0834EBED75D4C482B6D8DA454ADAC8A4251E45F9CEAD8BA1C4ED6FD)：单击该按钮可以对当前选择的设备进行录屏，并保存在本地。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/xK1dOWXwSnCvZW2H5neFZQ/zh-cn_image_0000002779567496.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=57582447E772EBAA30C802FBD07F3BC140C69875072BB46F8499A76857E16984)：单击该按钮可以保存日志缓存到指定文件（在线日志）或保存离线日志文件（离线日志）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/j0x639RdReCKsZxLvkiWGg/zh-cn_image_0000002808887111.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=ADAE2E4E272796BBB1CA4C12D4F1B2F8E5C6C7A96EB12D9A1811F8CB4256EADE)：单击该按钮可以自动选择和切换已连接的设备。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/pagx2PGfRnu7DlQsv8Qr3A/zh-cn_image_0000002779407514.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=6EAC4D6F505DB14243BECD2BC862F8FB414D95848A2DC66A866ECC70ED9C3A17)：单击该按钮可以切换日志视图以及自定义日志格式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/n9UrAiI1Tyysx-yX4FHQ2Q/zh-cn_image_0000002808767045.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=041ECDAC886BB334DAA679133658EFE7BDF30ABFD5F8AEFBDF39162F18291E9B)：单击该按钮可以关闭当前日志窗口。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/oBXmk-kjTg2NS8COCBDO4Q/zh-cn_image_0000002779407490.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=A2627087DB109FF792D17D3B223EBC789F0C0DD5405AA74ED1E1A3F8002CCF53)：单击该按钮可以跳转到HiLog日志相关的在线帮助文档。

## 过滤日志

### 按关键字过滤日志

在HiLog搜索框中输入希望过滤的信息，即可过滤显示所有包含此信息的日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/KmOiE-G1TGOnhDdb-P0Myg/zh-cn_image_0000002779567458.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=395E6CCA526D3508B8495245D439A3EE66B6B13A7962C961A3E3002D096FA198 "点击放大")按钮表示是否区分大小写，![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/zbY89DQvR_SdoLK1iS_eRA/zh-cn_image_0000002779407510.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=E564293ABFF6F6734DB5ECF5A0A63E1CB380B13188AADDAE8357929B0ED0B804 "点击放大")按钮表示是否按照正则表达式匹配过滤，![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/cdQEKCcoSq68Az9pnXbD1Q/zh-cn_image_0000002808767035.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=29E8BAAC6BE08DA1AAC45707E9ACE9A7BB7F5F91AD78BDE54B24066347BA8C28)按钮表示关键字是否高亮。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/xntUKONfTfGewHj_UBJQ7Q/zh-cn_image_0000002779567486.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=B425BD69752A1D69F7E0411E3FDFE89DCE16EF4A5ED965CC391B8D71A846CD60)

从DevEco Studio 6.0.2 Beta1版本开始，支持使用逻辑运算符&拼接多个关键字，精准搜索日志，&字符前后要有空格。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/uqVLNDGWR0yPbHedV4nN8w/zh-cn_image_0000002779567494.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=FE08A1AE5543E001575AFE57BCEC5D6CEAB2CBFA2C9A52682BB412F20654C728)

### 使用默认提供的过滤配置

HiLog提供多种默认的过滤模式，开发者不需要反复输入关键字过滤日志信息，只需要切换相应的过滤项，即可快速过滤所需的日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/BQ6ROTAzRyWjOOND0l-l3Q/zh-cn_image_0000002779567464.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=458950508589D88886FD6ABF2AA3C9D0089EA6F75FDAA9A4C492460C51DB3539)

* All logs of selected app：按照应用进程过滤日志。
* User logs of selected app：按照应用进程过滤用户输出的日志。

当选择All logs of selected app或User logs of selected app时，进程过滤下拉框处于可选状态，可选择相应的选项过滤想查看的进程日志。

**说明** 

由于设备启动时，USB调试开关没有开启，部分系统应用没注册上，HiLog进程列表无法显示未注册上的系统应用，如需查看此部分的日志，可以[按关键字过滤](ide-setup-hilog.md#section1264082914019)查看，或者保持USB调试开关打开的状态，重启设备。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/ry7QuhhQTdmV4CQ-bcTy7w/zh-cn_image_0000002779407486.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=296B8F67C079906D4EA6C5115DA90858B471318F4F882B411EAD51E590FCA124)

进程选择窗口可输入PID或应用名的关键字搜索要过滤的进程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/5VvbYby8S6CTeYT-LMnXUQ/zh-cn_image_0000002779407516.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=F474E7DF8F954589CEBAEEAD5E4F2AA26D7E178AC6BCFD1B1F0237144AD1449B)

### 按日志级别过滤日志

HiLog提供日志级别过滤，用来过滤某一级别及以上的日志。日志级别分为Debug、Info、Warn、Error、Fatal五个级别。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/134fiVSOR7qkKtZMQxLjzA/zh-cn_image_0000002808887129.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=1DEE66B97839AFE6BB3B6F2805DE56DF463AD503339A5F0E01890C2C07DF307A)

如选择Warn级别，则过滤展示Warn级别与Warn级别以上的日志信息，即展示Warn、Error、Fatal三个级别。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/WAbmSMFAQSqFf8j0cEaAZA/zh-cn_image_0000002779407500.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=FF32F1CD31CD3FBA7F8ED58CAAA93B098D5EC1442D18BADBAC04FD4D97826922)

### 按日志标签过滤日志

从26.0.0版本开始，支持根据日志标签过滤日志，可输入多个标签，不同标签之间使用英文逗号分隔。如包含特殊字符，标签需要添加引号。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/pEStxwoETP6h_rkW69lKRg/zh-cn_image_0000002779407488.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=4C9FC0EC159BB77C648F2ADCD5A94573CBD91A9BAFED0FF573E4EA5D7D85D608)

### 按自定义过滤项过滤日志

除默认过滤项外，HiLog还提供配置自定义过滤项的途径以供开发者按照实际需求过滤日志，并保存此过滤配置以供重复使用。

点击**Config custom filter**时将弹出自定义过滤配置窗口。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/oQz4EtelQKuIW3BY10FsEQ/zh-cn_image_0000002808887117.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=807439A512DD28D36F12A8676F3F638CE7A70BB76D2C6B40D02862A25C494A9F)

先前介绍的过滤选项此处均可配置，同时增加了Package name和Set to all projects配置项。

* Set to all projects：此配置当前工程及其他所有工程均可用。
* Package name：按应用包名过滤日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/YUEwLNmsQGm421ip273Lqg/zh-cn_image_0000002779407494.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=CA464D9182EB0BEC410D4EBC25D370EFE3C0B35D4B92F71559F70F6364E7C2CE)

当配置完后将自动切换至此过滤配置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/w_RG3HV7RNS3l7pw1-R0GA/zh-cn_image_0000002779567474.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=5C42FC6547C7ADACFA8F4ADE03D3979285BEBE0A6A76E4C5F35B644D34115C3D)

切换至此自定义配置时，日志级别过滤窗口和关键字过滤窗口将在此自定义配置过滤出的日志的基础上再进行过滤。

## 自定义日志显示格式

开发者可以通过配置自定义格式，限制每条日志只显示用户关注的信息。

点击左侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/jMbtFk_gT-iwglzRKUm12Q/zh-cn_image_0000002779407496.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=24E9337DFD0FEF8F11ED101F11013681AFF084894995C12AA2C2B85D14B65616)图标，将弹出自定义格式窗口。

* Standard Views：默认显示所有信息。
* Compact Views：默认显示日志级别与日志信息。
* Modify Views：进入“Hilog Format”窗口后，可以按照需要自定义日志格式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/1_ZzMuSbQFeieS2bpt3kiA/zh-cn_image_0000002779567498.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=21352DF34E700541BE6D3A3B11ED9BE17865E69C1B554AE800E6902691F88F2B)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/TLBh-QBnRH-bFXicNXJk2Q/zh-cn_image_0000002779567472.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=7E70EA633ABCFF89A1C7490E4E6736121E66ED45A4348B6EA8554992E7E7F81E)

## 超长日志自动换行

当日志的消息过长时，日志窗口可能不能完整显示日志消息，需要拖动滚动条查看信息。此时开发者可以点击**Soft-Wrap**按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/ug9n8JspTU2UKG5ggdnjmQ/zh-cn_image_0000002779407512.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=B9D2BA427FD8BFFC976402821D8F687CFE7FB3F726C0F4CB31019AD20FFF7C55)控制日志消息自动换行。

**图1** 未开启自动换行  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/9VRmWHeOSXGYG416IqDjIg/zh-cn_image_0000002808767077.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=43CF17062B850B68059A8503CD2E316AABB3DF086BF1B666716C2FA50840E2E4)

**图2** 开启自动换行  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/oxnhTvhfTv-z_G9beGdgSQ/zh-cn_image_0000002779407478.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=E6A2A313946647DDDF5C18724407F603C1BBFED7F44FF87E226C563ED7D68D9C)

## 显示最新日志

设备输出的日志信息会实时刷新到HiLog窗口底部，用户可点击**Scroll to End**按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/dzNoZy8wQy2mB3n2TwgEfg/zh-cn_image_0000002779407480.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=32B05EC5A7352B04964A2A0958ACB299D861AA23090E63F8A3C6908609811941)使HiLog一直显示底部的最新日志信息。当观察到需要的日志时，点击HiLog窗口，即可停止滚动，停留在当前行，以便查看日志信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/fmzjZ_7PT-qfX7sSRUI-Cw/zh-cn_image_0000002779567488.gif?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=ADB6ABD713AD3BB248B3DEB1031962CD8B67BBACBA1CBB2B1935B94F78EED174)

## 导出日志信息

用户可将经上述步骤过滤后的关键日志信息保存到本地，以便进一步分析。

点击**Export HiLog**按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/_EUIZnmxRwyvHfknlGmCcg/zh-cn_image_0000002779567476.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=DC33D945B2AEABC2C75685DF080EAF41F8C4A1B71BB2490A2667C78599CFE005)，在弹出的Export HiLog To窗口中选择保存路径。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/IKb09oLXS-So8jCth3xR8w/zh-cn_image_0000002779567468.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=049A91D71710F70CA1491234F9F974CF505FFA30320F30C85CC40CD99C4BEB80)

## 清除日志缓存

与日志相关的缓存有两个：设备端日志缓存、HiLog窗口缓存。

HiLog显示日志信息的流程为：

1. 应用输出日志信息至设备端日志缓存；
2. Log组件将设备端日志缓存取出，保存在HiLog窗口缓存中；
3. HiLog窗口根据过滤条件，将HiLog窗口缓存中的消息显示在界面中。

点击**Clear All**按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/hpNaXq1yRiK2seBuX31BSg/zh-cn_image_0000002779407492.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=FDC854069B2ABAF7F4E5ABB6EB616216D0E2A0EDCE1F09443E292541507D1BBA)，将同时清除设备日志缓存和HiLog窗口日志缓存，以及当前已经打印的日志。HiLog窗口将显示执行清除操作后，新输出至设备端缓存的日志信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/jsyLw-4oTmeSgjSh3f6eHw/zh-cn_image_0000002779407508.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=E645166505A6668A7D674BA2E07A47DC28009A688F1556F9775D1550A96A671D)

## 设置HiLog窗口缓存

HiLog窗口显示的日志信息保存在此窗口的缓存中，缓存的大小决定了当前窗口能显示的日志信息的最大数量，当日志超出缓存上限时，窗口中最早的日志将会被清除，新日志在窗口底部输出。开发者可以自行设置窗口的缓存大小。

点击**Settings > Buffer**，进入缓存设置窗口。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/xmPIwEc7TAaLbRz3ifM8vw/zh-cn_image_0000002779567480.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=E678C7E999930A9E4B5620C8BC73BD066B158B31F0121B9FB84AAD77ACE19DE1)

默认缓存大小为4096K，变更缓存大小需重启HiLog窗口后生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/jmet8LXZScqv84b3qm9W0Q/zh-cn_image_0000002808767031.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=223C38B50D1F49445448EDD8834A77E2523FE288442E280A1DDA2B89EF79D42B)

重启HiLog窗口操作：先点击下方的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/ChxzXS8nSOaYg0PQxFnRsg/zh-cn_image_0000002779567482.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=00B7578420515B0BCD0846125BCF8AF235268FCE07F4EB4D7265CA2B41A86B1B)按钮，再点击上方的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/jns_X11FTMGVyzc_AYtlUg/zh-cn_image_0000002779407504.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=3CE4AAED27F30547CBB992E62E5EF9F077D37FAE73B7BF095097DFFECE2606FA)按钮中的Online Log即可。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/VFfZHVgaTg-g6NZbs5WHxA/zh-cn_image_0000002779567470.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=28D7EDF0EBECE6C60DA43EE1E7947BC03E96957A1C9D45E05F105A1D3E9D7194)

当日志量超出缓存时，顶部的旧日志不断被清除，因而顶部日志信息处于不停滚动的状态。此时若想查看此处的日志信息，可在日志滚动时，点击右键，勾选**Pause Output**暂停窗口打印，查看完后再取消勾选，重新开始打印日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/KCC66rf2QzWXoQMts8Mbjg/zh-cn_image_0000002779407506.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=49E7B0352F948F31865F87C19A5A63A4D1AB036675B7ACB76CDEF63AAEF157D1)

## 设置设备端日志缓存

使用hdc shell hilog -g命令可查看当前设备端设置的日志缓存，默认为256K。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/jbfpLRzITFqRxrczxcj9Gg/zh-cn_image_0000002779567484.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=BE3DDBD7D95C293BA378D07A208DE8F11EA9AA1CD603AE66FF744FE1A3F00D53 "点击放大")

使用hdc shell hilog -G命令可更改设备端日志缓存大小。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/z5tXiOdbSJmB5xbrF8CbxA/zh-cn_image_0000002779567478.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=FCB582D147B294F0AAF30A116D1FDC11C85B6AEBDDA68343EB9795309D40869F "点击放大")

配合-t参数可单独设置某一类型的日志缓存大小。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/mmmKu_RNSyWpYTmxH0eLrA/zh-cn_image_0000002808887115.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=0BB4A2628CA6AD2A1D8CF71572DDFC21DEF7B38CEB6D328051A17694BED524A0 "点击放大")

超出设备端缓存日志将被落盘于设备data/log/hilog路径下，开发者可在此目录下载历史hilog日志并查看。

## 查看/导出设备离线日志

DevEco Studio提供查看设备离线日志的功能，支持查看设备中/data/log/hilog路径中的日志，离线日志窗口中展示的是经过解析和DevEco Studio格式化之后的日志。

点击HiLog窗口左上角New，随后点击Offline Log即可打开离线日志窗口。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/dnJ6xqxLRNitgpFQskVDKw/zh-cn_image_0000002779407498.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=C44DDE9E5D236130301DBE475E022EE7F0E1885A1445BB4215976AA858DCFCCE)

离线日志窗口左边工具栏中的按钮、日志级别下拉框和搜索框和在线日志的功能一致，设备下拉框仅支持选择真机和模拟器。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/eJZUJpKMRweGwKzqQ8fkOQ/zh-cn_image_0000002779407518.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=5F9518B9D86A3ADDA9F4E64726A652AEB1C17025FB82A585068386651C70D53B)

离线日志支持通过时间筛选设备上的日志文件，默认时间范围为打开窗口时的前三十分钟，除显示格式外，也支持通过键入yyyyMMddHHmm后回车进行时间输入。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/c02gk6a3R6K9ilda3dnj_w/zh-cn_image_0000002779407484.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=0530877773A90158F074F7C130ED2E9BF3C57DA9F627C0E18494EC1080AA180B)

在输入时间之后，日志文件下拉框会进行刷新，点击文件会从设备端下载并自动解析后输出到离线日志窗口。

由于最新的日志文件内容还在更新中，在达到设定的大小前，内容会不断增多。如果重新打开离线日志窗口或者修改时间，日志文件列表都会刷新，会从设备端重新下载最新的日志文件，解析的内容会更多。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/T8vHcyYtSGaUHMD5gSM-jA/zh-cn_image_0000002779407482.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=39B150D126BF55DEB6F7B8A33AE4C39DC4DE0513EAD2EFB79C9BBC5FDD821744)离线日志窗口能输出的文本量可参考[设置HiLog窗口缓存](ide-setup-hilog.md#section106741332995)进行设置，设置较小可能无法显示选择文件的所有日志，推荐设置6M(6144K)。

通过设置窗口的缓存大小可能无法展示完整的日志，可点击左侧工具栏的保存按钮导出离线日志，支持导出解析后未经DevEco Studio格式化的原始日志文件，导出的文件可以看到完整日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/ysEXhqRRRPWD8o3Bc1I4XA/zh-cn_image_0000002808887159.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=544C7B2A91C8CDC0FF2D51F3FED7CE9DBB9733314366830333C06B130942C05E)

## 终止应用

从DevEco Studio 6.0.0 Beta5版本开始，在日志窗口点击**右键 > Force Stop App**，可以终止该日志所属进程的应用，不支持系统应用和release签名的应用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/Xpl6-zVxRpqO6jZ_gvc2fA/zh-cn_image_0000002779567452.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=8B8EC87D1C44BFC70DB93CA02DE2F1994DC28C35F2CF9AB3B06F0CE634FDC8BE)
