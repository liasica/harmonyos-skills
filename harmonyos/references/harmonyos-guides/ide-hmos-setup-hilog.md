---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-setup-hilog
title: 日志分析
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 日志与故障分析 > 日志分析
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:46+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:c54a5c01e6071ba56e565c0f098fb7a7bcab5a3c07abe6ebd04d2e84e5a2bd49
---

鸿蒙电脑DevEco Studio提供了“**日志** **>** **HiLog**”窗口来查看设备当前所有应用实时打印的日志信息。点击DevEco Studio底部![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/ZfWC40pkRpigpEqyqyTB9g/zh-cn_image_0000002820720897.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=7365E9018C96BE7C6B614925C9337A30CCC706D8A0F30635C59EBA7F17B50295 "点击放大")图标打开日志面板并点击**HiLog**，进入HiLog日志面板。

HiLog默认显示的日志为以下6个部分：

| 第一列 | 第二列 | 第三列 | 第四列 | 第五列 | 第六列 |
| --- | --- | --- | --- | --- | --- |
| 时间戳 | 进程ID和线程ID | 日志标签 | 应用包名 | 日志级别 | 日志内容 |

开发者可通过设置包名、日志级别和搜索关键词来筛选日志信息，还可以使用自定义日志显示格式、日志导出、显示最新日志等功能。

HiLog窗口左侧各个按钮的作用为：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/p96P2YSqQbC5rDNgz4Oj_A/zh-cn_image_0000002792000928.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=B644AE115520C39B651E4A8555517F6AAE62D327C8174358C122531B59AE9100)：当该按钮处于选中状态时，日志自动换行显示，否则日志按行显示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/ZzF590UiSVGHRX-nVKUoxQ/zh-cn_image_0000002820720903.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=4D08ABCFDD971D63D24565D33193902CD01912E106AC1482F0ACEC19258EA6F1)：当该按钮处于选中状态时，日志自动滚动到窗口底部，否则停留在当前日志显示处。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/zvCAKoYkQsiwwxBvANyX0w/zh-cn_image_0000002820680887.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=A1DAC54363985BC13B7F6A6691105B8B3D1EA356CDC7562B919F825AA0A2571C)：单击该按钮可以清空窗口日志和设备缓存。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/INX6nycXQ72lxMSqKnuTGg/zh-cn_image_0000002820680889.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=67AE8DA3CC85F010A98253B56A5367B0BE4490A2ACEE75E0E32FD8476E431CCF)：单击该按钮可以对当前选择的设备屏幕进行截屏，并保存在本地。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/5P7Gzfs7RK6NU4fuwb1P1Q/zh-cn_image_0000002792000920.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=74867AE646299F8D71776AB87105EEE95C921A5EF6DFD031DB55DB41124AFCDE)：单击该按钮可以保存日志缓存到指定文件。

## 过滤日志

### 按关键字过滤日志

在HiLog搜索框中输入需要过滤的信息，即可过滤所有包含此信息的日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/ayj6sfMnQ-2y7wk7-IrPZw/zh-cn_image_0000002820720891.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=BE13A190AB242E1A8BA59952F440AAB3AC07A3C603350B0F577244372D1A54DD)按钮表示是否区分大小写，![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/ixW7fcWTQrKGKZoEZS-EXA/zh-cn_image_0000002820720895.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=5E4CEC507244C012860948EC26D6F18A9CEF10982A577583A0A78E8CB0553BB3)按钮表示是否按照正则表达式匹配过滤。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/PQ7y-ZSPTXa6oBKnaR_vkw/zh-cn_image_0000002791840954.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=533E3D5594244315E774ABFB974FB9528D786286715B329BCC83D23EB6C09FE2)

### 使用默认提供的过滤配置

HiLog提供多种默认的过滤模式，无需反复输入关键字过滤日志信息，只需要切换相应的过滤项，即可快速过滤所需的日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/HbKPVXfsQJmuZaJ2NsA5pg/zh-cn_image_0000002791840970.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=8ED81B9C115731ADDBA68BFE5AC41DAC6E87764DDF8B00FD43EF76D053FB77E6)

* 选中应用的所有日志：按照应用进程过滤日志。
* 选中应用的用户日志：按照应用进程过滤用户输出的日志。

当使用**选中应用的所有日志**或**选中应用的用户日志**时，进程过滤下拉框处于可选状态，可选择相应的选项过滤想查看的进程日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/5Hu4yPbEQRKPb15Y0TdYVQ/zh-cn_image_0000002792000922.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=A8304005AA7FB9EE56F5085134E699D504BB48786D8EB4607E285062F8FC2326)

### 按日志级别过滤日志

HiLog提供日志级别过滤，用来过滤一个或多个级别的日志。日志级别分为Debug、Info、Warn、Error、Fatal五个级别。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/SoBu-wuORw-W_Wod2VAlFA/zh-cn_image_0000002820720889.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=58A305475298E09E64421D386262C3EEEFBA6184FB1D4E287141C22EF0868B06)

### 按自定义过滤项过滤日志

除默认过滤项外，HiLog还提供配置自定义过滤项的途径以供开发者按照实际需求过滤日志，并保存此过滤配置以供重复使用。

点击**新建自定义过滤配置**时将弹出自定义过滤配置窗口。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/qKA_paU3TquoQbW8dtoTRQ/zh-cn_image_0000002792000924.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=2E232483CC100E68EABA15AEACB66B26CDA20A715D96B9DA3C53B34485FE40E8)

先前介绍的过滤选项此处均可配置，同时增加了**应用包名**和**同步至所有工程**配置项。

* 同步至所有工程：此配置当前工程及其他所有工程均可用。
* 应用包名：按应用包名过滤日志。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/QfFLOTv0SR-ZYyOGgEXWew/zh-cn_image_0000002791840942.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=2A2539DA13FE02C4A381F25C97C498EE27BB70D5CAFB5E750728FACBC98EEBB0)

当配置完后将自动切换至此过滤配置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/H0bwrPKOQ_GOaZ81qfIg7w/zh-cn_image_0000002792000938.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=E1C2E7EB241028CA9D507700FC4A22881673B498F2BA974D85BFCE645C0961EC)

切换至此自定义配置时，日志级别过滤窗口和关键字过滤窗口将在此自定义配置过滤出的日志的基础上再进行过滤。

## 修改日志显示格式

支持开发者修改日志显示的格式。点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/HeQeAHNfQgC67ZCGwvfUQg/zh-cn_image_0000002792000916.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=CE2336429627D456964CDC5B0D59552C37DE1946845FDA320CA302831B6AD59D "点击放大")图标。

* 标准视图：默认显示所有信息。
* 紧凑视图：默认显示日志级别与日志信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/cpbnyHcjRtq4EIjDiuEIsQ/zh-cn_image_0000002820720901.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=7CCF8D5F623BD9470357EBB49BBB80A2D0CEBE3943F897C082AB7C2E974DFF8E)

## 超长日志自动换行

当单行日志过长时，用户可点击自动换行来使日志信息自适应当前窗口宽度，在末尾自动换行，在当前窗口中完整显示。

当日志消息过长时，日志窗口可能不能完整显示，需要拖动滚动条查看信息。此时开发者可以点击按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/ORwpuEP_SPm3cMls0n_oUQ/zh-cn_image_0000002791840956.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=F04F99718A89FD51040A56B99490EB7EDDEC2559DB76E94A452A98302B6B960D)控制日志消息自动换行。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/YplDEb9LTHCltcGnDj2EjA/zh-cn_image_0000002820680879.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=0525B6CB962BF2C3487C35DEEA915A1A2FC6F0E9868AA2E5426E70463858917B)

## 显示最新日志

设备输出的日志信息会实时刷新到HiLog窗口底部，用户可点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/QOD9Pnj8Th27sSGYKkMvbw/zh-cn_image_0000002820680903.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=6097724AD2909D99BF49475F3F1C850BBA84D73A618A14CF22186224293AF27F)按钮使HiLog一直显示底部的最新日志信息。当观察到需要的日志时，点击HiLog窗口，即可停止滚动，停留在当前行，以便查看日志信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/ugDbSRfhSMilrlWWdQuR7g/zh-cn_image_0000002820720907.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=4E521DB3563C417C81D5B4734F2BE1FCC004661A9BA2DCA76E2D316B74BFA56A)

## 导出日志信息

开发者可将经过过滤后的关键日志信息保存到本地，以便进一步分析。

点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/ulYEigtSSjWdmcJnillywA/zh-cn_image_0000002820720885.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=3C97A5A7AF941463BCF84C76C48F297E93FB193ADA7816E7131798EA5B98920C "点击放大")按钮，在弹出的窗口中选择保存路径。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/h8LB164nR-CaeJQGTsg-bg/zh-cn_image_0000002792000940.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=E619C88CB46CFD82FE53AD19402F36B50339619BD97749CEEBAC35FCDFAAA3E4)

## 清除日志缓存

与日志相关的缓存有两个：设备端日志缓存、HiLog窗口缓存。

HiLog显示日志信息的流程为：

1. 应用输出日志信息至设备端日志缓存；
2. 日志组件将设备端日志缓存取出，保存在HiLog窗口缓存中；
3. HiLog窗口根据过滤条件，将HiLog窗口缓存中的消息显示在界面中。

点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/TkLFMhBIRG-un-PoD8PVGQ/zh-cn_image_0000002820720883.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=4EAC9066DEE69D044AA76CD1DD3FDEAEB21CDF42F5AB074455BBB1F2916C9D14)按钮，将弹出两个选项**：清除控制台日志**、**清除设备日志**。

* **清除控制台日志**：清除HiLog窗口日志缓存。日志组件将重新从设备端日志缓存读取日志消息，因而执行清除操作前已保存在设备端日志缓存的日志消息会显示到HiLog窗口中。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/YfyuQyyyQ4amtPTj4Vhr2A/zh-cn_image_0000002791840948.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=44143EA8A863A93D5A0F139D120D4940AE3CB4493F1218E25F18454F3D9DF52D)
* **清除设备日志**：清除设备端日志缓存。此操作将清除设备端日志缓存和HiLog窗口缓存。HiLog窗口将显示执行清除操作后，新输出至设备端缓存的日志信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/i2jFcirKS6uAiwWy9BArJg/zh-cn_image_0000002820720899.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=8C814DA84669FDA7EE3A516E37CDD265AC032C1453AF879CCBAEDE3A71D4DDC9)

## 设置HiLog窗口缓存

HiLog窗口显示的日志信息保存在此窗口的缓存中，缓存的大小决定了当前窗口能显示的日志信息的最大数量，当日志超出缓存上限时，窗口中最早的日志将会被清除，新日志在窗口底部输出。开发者可以自行设置窗口的缓存大小。

进入**文件 > 设置 > 扩展 > HiLog Console**面板，或点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/ejk54v3TQOud7y2yP_jDkA/zh-cn_image_0000002820680905.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=187BBB43090AFC123B998B93200EA21D9CFEDA00840964B69E23B02A5F1FE374 "点击放大")图标，选择控制台设置 > 缓冲区，默认缓存大小为4096KB，变更缓存大小后实时生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/vbD2XcUtQvOm_INZrxs0UA/zh-cn_image_0000002820680881.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=85783065CD16203B34965DA7452F47EF5C6D69D381329F13683105D847C0DFD8)

## 设置设备端日志缓存

使用hdc shell hilog -g命令可查看当前设备端设置的日志缓存。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/JteLU9ZlSJ-ToZsJKlQM9A/zh-cn_image_0000002792000934.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=649BE45FA1C3D8D7DDB1AADF54FAAF39FC3705B734A61A7511ED88EE5B23729B)

使用hdc shell hilog -G命令可更改设备端日志缓存大小。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/ZxZ_ulkSRLGAD07IOZYG4Q/zh-cn_image_0000002792000930.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=B9FC9F46F8E2A55ED59112C44A3234B01BDAEA80141C71C78530D655B2A82928)

配合-t参数可单独设置某一类型的日志缓存大小。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/GwWyXW6IS_SL3zRH_oQuCw/zh-cn_image_0000002792000936.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=28118506A19454C0BB59DD5C5CBCA5DCD6151246DCD57FA55598DE48D270B3D8)

超出设备端缓存日志将被落盘于设备data/log/hilog路径下，开发者可在此目录下载历史hilog日志并查看。
