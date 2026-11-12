---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-setup-hilog
title: 日志分析
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 日志与故障分析 > 日志分析
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:c96f5d9b3750c287e1a4d592d8d49989d04d285bebf5284046b09eb717652512
---

**说明** 

打印日志请查看[使用HiLog打印日志](hilog-guidelines-arkts.md)。

DevEco Studio提供了“Log > HiLog”窗口查看设备当前所有应用实时打印的日志信息。HiLog默认显示的日志为以下6个部分。

| 第一列 | 第二列 | 第三列 | 第四列 | 第五列 | 第六列 |
| --- | --- | --- | --- | --- | --- |
| 时间戳 | 进程ID和线程ID | 日志标签 | 应用包名 | 日志级别 | 日志内容 |

开发者可通过设置包名、日志级别和搜索关键词来筛选日志信息，还可以使用自定义日志显示格式、日志导出、显示最新日志等功能。

HiLog窗口左侧各个按钮的作用为：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/asY7LQeCSZaQlMZfCOSr_A/zh-cn_image_0000002779567490.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=2A084FD00ACE91F433785E04DB575D5B8EF6297471C88295DF0AF23CFBE69BA3)：单击该按钮可以向上翻页，日志窗口取消自动滚动。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/_I6FqHtBSsWBTUARFautnQ/zh-cn_image_0000002808887127.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=E1CE1F9CAF2201AC05CCA02C7487D8C028A2AB8401840F60E1BB7CE40CBE49BD)：单击该按钮可以向下翻页，日志窗口取消自动滚动。如果翻页已到底部，日志窗口自动滚动。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/akLrjx4cTwqxqAET2TEiDg/zh-cn_image_0000002779567492.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=C5134CF19D09D266A1464474C3F1AE32F60B9A5683E4377F2DEEA105AFA3D500)：当该按钮处于选中状态时，日志自动换行显示，否则日志按行显示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/Z5USFMaUT7ewr6cINM_v8w/zh-cn_image_0000002779407502.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=168844E3D5B4A5D5D483D5553AAD2811793B21CE63ACC001C437A13DD0384A66)：当该按钮处于选中状态时，日志自动滚动到窗口底部，否则停留在当前日志显示处。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/fFkyMSkrQtGrfVRPJBE53A/zh-cn_image_0000002779567462.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=5D2B13B891EFFDF5626D715AB7191DFC2DC0BCCB2AFA5F7AFA8DAE4C2E5B0BC9)：单击该按钮可以重新开启日志接收，会重新加载设备缓存日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/IuJmmrJeSXim5G3eqOky-w/zh-cn_image_0000002779567466.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=9588DD3D642474DC10D8247BFC1458DBE5DE1A475587B4D97E4E915B8C279FE6)：单击该按钮可以清空窗口日志和设备缓存。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/PCtVk11EQBiM3jfp1iLMYQ/zh-cn_image_0000002779567460.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=7DACF73F4310B0A92C597985DB98F2E8F049D51E5E174C890FB3FAA577D5381C)：单击该按钮可以对当前选择的设备屏幕进行截屏，并保存在本地。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/hF0apfBoR86Rc8pbmDHWbw/zh-cn_image_0000002808767075.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=CBCA22799FB9A6CEEDF570CE19E0A6F599584B6E0491FC9C48AEBBBD0E01C2CC)：单击该按钮可以对当前选择的设备进行录屏，并保存在本地。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/DzvdULgtRvKchIqdiATeZw/zh-cn_image_0000002779567496.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=7C386597B0DC2A00BF9A12B233B8B2CDD8617C40C0B6F99BCDB988840E15FBCF)：单击该按钮可以保存日志缓存到指定文件（在线日志）或保存离线日志文件（离线日志）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/3ibdUNaSQ-KqSyIHg9-GQQ/zh-cn_image_0000002808887111.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=BFDE4D5E43C72BA2BDFF7B90D9589A6FFB12DD2C18B3151101A8668B8A612D4B)：单击该按钮可以自动选择和切换已连接的设备。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/RG7WvsseQbK2xZxUO3iKJA/zh-cn_image_0000002779407514.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=E1406A1A2E30B059F780BE3A9383AE89AE92C84C13582C7923C794DDA07D4184)：单击该按钮可以切换日志视图以及自定义日志格式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/jQUpSknDQd-VXPdr5IJzuQ/zh-cn_image_0000002808767045.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=F9B5C594DFF1D585FB600ADA5A5D13859EDED77EA3EBA39220F84D92EE3DA39B)：单击该按钮可以关闭当前日志窗口。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/7Q189OymRsW9KtZldY33tA/zh-cn_image_0000002779407490.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=C4EA380C6A70B018B73803DF55E9C66F896F9C958FD78B4E07B3F4874846E062)：单击该按钮可以跳转到HiLog日志相关的在线帮助文档。

## 过滤日志

### 按关键字过滤日志

在HiLog搜索框中输入希望过滤的信息，即可过滤显示所有包含此信息的日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/tKETaAQTTyi-VNSJORuv4Q/zh-cn_image_0000002779567458.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=D77B094CD550F405D72494860487AC62188B95C57F8859BF33042784E4BA621E "点击放大")按钮表示是否区分大小写，![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/Y28Lxr0hTg6uSju991cvqw/zh-cn_image_0000002779407510.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=1C75293E3620E72A22076A990C7C324F80779083A3733FE0ABDAFFD3235E3D28 "点击放大")按钮表示是否按照正则表达式匹配过滤，![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/HbfuYkS5QuSsz0X6GE8RiA/zh-cn_image_0000002808767035.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=DD5ED887A6C187943D72CB564CDE2498AA5402B9A2C83650A47F5A609CAC39C0)按钮表示关键字是否高亮。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/-2eqa7ILQzuYf-6thaLtmQ/zh-cn_image_0000002779567486.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=C3A59654E253DBD85C1EADFA79A65AE3EFD52B99B17463EF83FB9F88EF91EC70)

从DevEco Studio 6.0.2 Beta1版本开始，支持使用逻辑运算符&拼接多个关键字，精准搜索日志，&字符前后要有空格。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/HWz9Cvn5Ty2sR0ic_svCig/zh-cn_image_0000002779567494.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=A70919B04353EFF6E6237FED6BF7AA6E695089084A7E6070A97D5D9EA5933659)

### 使用默认提供的过滤配置

HiLog提供多种默认的过滤模式，开发者不需要反复输入关键字过滤日志信息，只需要切换相应的过滤项，即可快速过滤所需的日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/kuM_YbrfSbqC78A_EzTpaA/zh-cn_image_0000002779567464.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=6265158C0CE1254924D681B2605557D7FE8C8A9F8F44F0AE6D2FA2869E423CA6)

* All logs of selected app：按照应用进程过滤日志。
* User logs of selected app：按照应用进程过滤用户输出的日志。

当选择All logs of selected app或User logs of selected app时，进程过滤下拉框处于可选状态，可选择相应的选项过滤想查看的进程日志。

**说明** 

由于设备启动时，USB调试开关没有开启，部分系统应用没注册上，HiLog进程列表无法显示未注册上的系统应用，如需查看此部分的日志，可以[按关键字过滤](ide-setup-hilog.md#section1264082914019)查看，或者保持USB调试开关打开的状态，重启设备。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/tIRzDb2hTm6_2nJujYPVaw/zh-cn_image_0000002779407486.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=9DC8427F5CE04129D38FC485780EF99EB4EB44500E042C05B86DD4D456A0694E)

进程选择窗口可输入PID或应用名的关键字搜索要过滤的进程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/q2bEIKq6QYy6UqyDcjP4cw/zh-cn_image_0000002779407516.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=5B8D80FACB19A56CBDE98C2331B62D72F6364691FC13755E03B7B13E81EAECDD)

### 按日志级别过滤日志

HiLog提供日志级别过滤，用来过滤某一级别及以上的日志。日志级别分为Debug、Info、Warn、Error、Fatal五个级别。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/tHMUooC0TlmhOMgJnS_2qA/zh-cn_image_0000002808887129.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=4FF8FE1BAB8A1982383CE06776335816BD450D2C6E2DD21C990537D423F88776)

如选择Warn级别，则过滤展示Warn级别与Warn级别以上的日志信息，即展示Warn、Error、Fatal三个级别。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/V76V3Lk8TYyrbQkK7ABz2g/zh-cn_image_0000002779407500.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=0B2D6744FE1E48C76D3FD3377CECB5F3E1A2812E68AD69D27E0DDB2C24C7FAAC)

### 按日志标签过滤日志

从26.0.0版本开始，支持根据日志标签过滤日志，可输入多个标签，不同标签之间使用英文逗号分隔。如包含特殊字符，标签需要添加引号。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/GXvrGV7KQcGFd24ijd_BNg/zh-cn_image_0000002779407488.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=0836AC040C244CE4F7BCDEE108071C44A09F23DA8D760C46EDD50DCF22472599)

### 按自定义过滤项过滤日志

除默认过滤项外，HiLog还提供配置自定义过滤项的途径以供开发者按照实际需求过滤日志，并保存此过滤配置以供重复使用。

点击**Config custom filter**时将弹出自定义过滤配置窗口。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/fVMhadqmQmyo-YVJPh2-Rg/zh-cn_image_0000002808887117.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=E577E13F9803D57813A198F37A2089CC2A895AC25A0594A4C3896D241EC73351)

先前介绍的过滤选项此处均可配置，同时增加了Package name和Set to all projects配置项。

* Set to all projects：此配置当前工程及其他所有工程均可用。
* Package name：按应用包名过滤日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/PZqrSBrfSp6CbsA1RFdyfQ/zh-cn_image_0000002779407494.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=BCED7B8304AE827F67FB2A0B0A0B145764AF92276A74020A2D2BF8570711F344)

当配置完后将自动切换至此过滤配置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/5D6D24W1QsGZuOcbYLmL5g/zh-cn_image_0000002779567474.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=C8EA80A820E5175C00A9913DBA64A3E022B92DF557803CB95C3FE0311D3A80EB)

切换至此自定义配置时，日志级别过滤窗口和关键字过滤窗口将在此自定义配置过滤出的日志的基础上再进行过滤。

## 自定义日志显示格式

开发者可以通过配置自定义格式，限制每条日志只显示用户关注的信息。

点击左侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/DdRrjAmPRfab-tQpFKGg5A/zh-cn_image_0000002779407496.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=218D69812AD610941390662081E1F1B566A450C9FB969F20F047879FF51EB31C)图标，将弹出自定义格式窗口。

* Standard Views：默认显示所有信息。
* Compact Views：默认显示日志级别与日志信息。
* Modify Views：进入“Hilog Format”窗口后，可以按照需要自定义日志格式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/I8F4CushQxmhurVf6q_t5g/zh-cn_image_0000002779567498.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=46E144448F5A16E413FED261FB9C18CC063A02872F349CCF0C99062F651FCF97)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/PhMJFaRJT0CrsBz2pQH8xQ/zh-cn_image_0000002779567472.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=1EE5F1B976603833B2C1EF6BE8221D5DEFDDD4EF21A717CE061C89D775455153)

## 超长日志自动换行

当日志的消息过长时，日志窗口可能不能完整显示日志消息，需要拖动滚动条查看信息。此时开发者可以点击**Soft-Wrap**按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/aAqdNrh6ScuT1bj7wFQM-A/zh-cn_image_0000002779407512.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=7900A56917BF8B4F1B61E8D92651610DC369ADC0425856A565040A1CD57AB750)控制日志消息自动换行。

**图1** 未开启自动换行  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/n-qyZ7F7Q4Oha9B9dWllmw/zh-cn_image_0000002808767077.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=4F723AEEB65344D2F91380634C2BA2DAF1B9114174AA832973594303B1213B52)

**图2** 开启自动换行  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/gaNf5KkqS7ixoEy06mCuaQ/zh-cn_image_0000002779407478.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=CCF74A79FB2210E421588CA8B254E6AF794B326CFC03A4AA89121D152B1C19FB)

## 显示最新日志

设备输出的日志信息会实时刷新到HiLog窗口底部，用户可点击**Scroll to End**按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/AwxODqN7RVWtaPQTR4tf_w/zh-cn_image_0000002779407480.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=012C583F4916720EA8E2D0CF36D1C9E3FB0BAA9DA83FB0B581936FBA9A15DE62)使HiLog一直显示底部的最新日志信息。当观察到需要的日志时，点击HiLog窗口，即可停止滚动，停留在当前行，以便查看日志信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/n9jbqeiGRJ2qDCg2kEvheA/zh-cn_image_0000002779567488.gif?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=8A77950CF08CA262A7A5775079BF02547603D4EEB7973503C67EAE9E094C302C)

## 导出日志信息

用户可将经上述步骤过滤后的关键日志信息保存到本地，以便进一步分析。

点击**Export HiLog**按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/2XvgUcXqQpG4Z9U5ZryAfA/zh-cn_image_0000002779567476.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=70C3FC7618B96401B92DFFFE26B6917B7D9820201B2D9D4AF959DB3867F4B891)，在弹出的Export HiLog To窗口中选择保存路径。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/7gwf5eFgSw687RTPpURSNQ/zh-cn_image_0000002779567468.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=3972E23A42E41066D7FBED7D5B2C8083518ABAD01D84FB03FE572DD992B4EEBC)

## 清除日志缓存

与日志相关的缓存有两个：设备端日志缓存、HiLog窗口缓存。

HiLog显示日志信息的流程为：

1. 应用输出日志信息至设备端日志缓存；
2. Log组件将设备端日志缓存取出，保存在HiLog窗口缓存中；
3. HiLog窗口根据过滤条件，将HiLog窗口缓存中的消息显示在界面中。

点击**Clear All**按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/_woHCIAtRZiDUaSMx-K9hg/zh-cn_image_0000002779407492.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=7FCDE7933AFA688CCA5921B9CCF4D68D2BE12484C12293BE37DE24FDBCC2EA59)，将同时清除设备日志缓存和HiLog窗口日志缓存，以及当前已经打印的日志。HiLog窗口将显示执行清除操作后，新输出至设备端缓存的日志信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/bryzBM1ESgetsBofRndaeg/zh-cn_image_0000002779407508.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=E13FEDAE897455F26D9C8DF03286215EBF70EFF80750CCF6F8CA26B12E607DA9)

## 设置HiLog窗口缓存

HiLog窗口显示的日志信息保存在此窗口的缓存中，缓存的大小决定了当前窗口能显示的日志信息的最大数量，当日志超出缓存上限时，窗口中最早的日志将会被清除，新日志在窗口底部输出。开发者可以自行设置窗口的缓存大小。

点击**Settings > Buffer**，进入缓存设置窗口。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/w4m5r7oKQ2OMQRFE_wxjFQ/zh-cn_image_0000002779567480.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=EB8DC599EE9993E64A0E87E474377AABC2EFA2E5545E4F55F3C2B98595BCA884)

默认缓存大小为4096K，变更缓存大小需重启HiLog窗口后生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/fYrwotZDS5CDChzOLC6ZBA/zh-cn_image_0000002808767031.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=27D8974CBA1AEB80ECC359E351AD1A9871FCCF908A7621622AFE8B43F33FB31C)

重启HiLog窗口操作：先点击下方的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/haNeiiSzQH-nNS3PxFjxUA/zh-cn_image_0000002779567482.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=7ECDD04B8A71BEBDE2EB80E57280886A75F66E72242C19327BA8B8AF8B30E3F5)按钮，再点击上方的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/iGVGcXBATROEfn5aBtp-9A/zh-cn_image_0000002779407504.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=942C361A39B5EB7B00CA0E4C36002603F9EFE1262FD893014346B82586D35A12)按钮中的Online Log即可。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/rb_B24ujQmqmidk865YwLA/zh-cn_image_0000002779567470.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=A199E709A886E82E72FE40A57B97DF9C1925115D3F677021547808B5DC9ED20D)

当日志量超出缓存时，顶部的旧日志不断被清除，因而顶部日志信息处于不停滚动的状态。此时若想查看此处的日志信息，可在日志滚动时，点击右键，勾选**Pause Output**暂停窗口打印，查看完后再取消勾选，重新开始打印日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/Cea5tHIzRfSBOK9a8kQRYA/zh-cn_image_0000002779407506.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=A3CF639D14107DFA61D61EE70CE2E1F14BE230AEB44520EB2445F6BA3302B1D1)

## 设置设备端日志缓存

使用hdc shell hilog -g命令可查看当前设备端设置的日志缓存，默认为256K。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/Nl82SAvpTZqsIaAU8LHyvg/zh-cn_image_0000002779567484.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=7307AC4755791C2E882D9632CFF3BDE8A3EB6504ADD092B9B8E0FFB600FC0507 "点击放大")

使用hdc shell hilog -G命令可更改设备端日志缓存大小。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/jaza485vRD24UwS9Dlb99g/zh-cn_image_0000002779567478.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=021B5A97D595F4D4CB0CA20807B536444C2F1BEE2BA69DEADA6311F883D67E22 "点击放大")

配合-t参数可单独设置某一类型的日志缓存大小。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/cEonnmoTQEejhK88W2XYAw/zh-cn_image_0000002808887115.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=01F9A2F83C82F2F27003D063EEDE2A29BB6C03F04FF6BEEAF2A627BDE226940C "点击放大")

超出设备端缓存日志将被落盘于设备data/log/hilog路径下，开发者可在此目录下载历史hilog日志并查看。

## 查看/导出设备离线日志

DevEco Studio提供查看设备离线日志的功能，支持查看设备中/data/log/hilog路径中的日志，离线日志窗口中展示的是经过解析和DevEco Studio格式化之后的日志。

点击HiLog窗口左上角New，随后点击Offline Log即可打开离线日志窗口。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/STVIUUPxTvOZBIqPXw_oSQ/zh-cn_image_0000002779407498.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=08EDFAC15AD22FA68A79B3B304EA5DBF31B6125BE5FE8C90F30FEA4906488D52)

离线日志窗口左边工具栏中的按钮、日志级别下拉框和搜索框和在线日志的功能一致，设备下拉框仅支持选择真机和模拟器。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/7WXi12CCT36JngJyuhKB7g/zh-cn_image_0000002779407518.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=7C8685F783E60F69892153CBD7AC5157703B2785F0B9A724D775820C856472E6)

离线日志支持通过时间筛选设备上的日志文件，默认时间范围为打开窗口时的前三十分钟，除显示格式外，也支持通过键入yyyyMMddHHmm后回车进行时间输入。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/B2_BNiFpQP2ZMnSSGZo_xw/zh-cn_image_0000002779407484.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=7EF58DCD531E7D01CD7D83E84AF3939CD6A31B6914C82BD86915CD194DCF1F01)

在输入时间之后，日志文件下拉框会进行刷新，点击文件会从设备端下载并自动解析后输出到离线日志窗口。

由于最新的日志文件内容还在更新中，在达到设定的大小前，内容会不断增多。如果重新打开离线日志窗口或者修改时间，日志文件列表都会刷新，会从设备端重新下载最新的日志文件，解析的内容会更多。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/T1Q9Zl5PQimQl79M14piJA/zh-cn_image_0000002779407482.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=102B42CE1E5984F609B704287EFF1471F50C8123671DD7ED8002C5B652C165D1)离线日志窗口能输出的文本量可参考[设置HiLog窗口缓存](ide-setup-hilog.md#section106741332995)进行设置，设置较小可能无法显示选择文件的所有日志，推荐设置6M(6144K)。

通过设置窗口的缓存大小可能无法展示完整的日志，可点击左侧工具栏的保存按钮导出离线日志，支持导出解析后未经DevEco Studio格式化的原始日志文件，导出的文件可以看到完整日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/bnh_LAxbSm6j2twNVSmXNw/zh-cn_image_0000002808887159.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=DCC6046090CA1D0C91D8E9DD315E68E5F8171B3801460B221035E98DE269EA49)

## 终止应用

从DevEco Studio 6.0.0 Beta5版本开始，在日志窗口点击**右键 > Force Stop App**，可以终止该日志所属进程的应用，不支持系统应用和release签名的应用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/_W0eGf8xTRmzEW8Hs9hN0Q/zh-cn_image_0000002779567452.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=235B911B4B31139ED5A656B630FA94E0DFC17B2C6A4A4A2FD9BF2CD3B7BDCF53)
