---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-setup-hilog
title: 日志分析
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 日志与故障分析 > 日志分析
category: harmonyos-guides
scraped_at: 2026-10-17T06:43:47+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:0d41cca95360399e7103b30186f78f48c52f3f55c5b670bc5233d77883143743
---

鸿蒙电脑DevEco Studio提供了“**日志** **>** **HiLog**”窗口来查看设备当前所有应用实时打印的日志信息。点击DevEco Studio底部![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/Z6xgg_7SQhuqgh-YDf6ZDg/zh-cn_image_0000002750169752.png "点击放大")图标打开日志面板并点击**HiLog**，进入HiLog日志面板。

HiLog默认显示的日志为以下6个部分：

| 第一列 | 第二列 | 第三列 | 第四列 | 第五列 | 第六列 |
| --- | --- | --- | --- | --- | --- |
| 时间戳 | 进程ID和线程ID | 日志标签 | 应用包名 | 日志级别 | 日志内容 |

开发者可通过设置包名、日志级别和搜索关键词来筛选日志信息，还可以使用自定义日志显示格式、日志导出、显示最新日志等功能。

HiLog窗口左侧各个按钮的作用为：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/V6V8lByoT-y-LlylmktAlw/zh-cn_image_0000002750169750.png)：当该按钮处于选中状态时，日志自动换行显示，否则日志按行显示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/8n2I9VCKRRGu8TJoWpFMew/zh-cn_image_0000002779608793.png)：当该按钮处于选中状态时，日志自动滚动到窗口底部，否则停留在当前日志显示处。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/YM8gOMwmQYaNXCsjDGuLww/zh-cn_image_0000002750009868.png)：单击该按钮可以清空窗口日志和设备缓存。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/293F4XkbTPqmWBo7NA4JiA/zh-cn_image_0000002779608783.png)：单击该按钮可以对当前选择的设备屏幕进行截屏，并保存在本地。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/1GS_owUHQ7WyuP53D0nPKw/zh-cn_image_0000002779728921.png)：单击该按钮可以保存日志缓存到指定文件。

## 过滤日志

### 按关键字过滤日志

在HiLog搜索框中输入需要过滤的信息，即可过滤所有包含此信息的日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/U9roFBQpTxurBWz6Em1lvA/zh-cn_image_0000002750009860.png)按钮表示是否区分大小写，![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/iZTOnvecTtq3wK8GZ2FW7A/zh-cn_image_0000002779728923.png)按钮表示是否按照正则表达式匹配过滤。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/ZA6ZhMYORfyKiSHuBUnBeQ/zh-cn_image_0000002750009864.png)

### 使用默认提供的过滤配置

HiLog提供多种默认的过滤模式，无需反复输入关键字过滤日志信息，只需要切换相应的过滤项，即可快速过滤所需的日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/MKnZRLxSSHm-4DoPFharkg/zh-cn_image_0000002779728947.png)

* 选中应用的所有日志：按照应用进程过滤日志。
* 选中应用的用户日志：按照应用进程过滤用户输出的日志。

当使用**选中应用的所有日志**或**选中应用的用户日志**时，进程过滤下拉框处于可选状态，可选择相应的选项过滤想查看的进程日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/TxvBtT5vToWBs6tHFVUi6A/zh-cn_image_0000002779608773.png)

### 按日志级别过滤日志

HiLog提供日志级别过滤，用来过滤一个或多个级别的日志。日志级别分为Debug、Info、Warn、Error、Fatal五个级别。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/2cOuULQXSDaQnxFtB6yrvw/zh-cn_image_0000002779608775.png)

### 按自定义过滤项过滤日志

除默认过滤项外，HiLog还提供配置自定义过滤项的途径以供开发者按照实际需求过滤日志，并保存此过滤配置以供重复使用。

点击**新建自定义过滤配置**时将弹出自定义过滤配置窗口。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/bkJ_RTfaT-e7iJmavASwZA/zh-cn_image_0000002779728925.png)

先前介绍的过滤选项此处均可配置，同时增加了**应用包名**和**同步至所有工程**配置项。

* 同步至所有工程：此配置当前工程及其他所有工程均可用。
* 应用包名：按应用包名过滤日志。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/mteH4rZQSY6ihQFcCFBuIQ/zh-cn_image_0000002750009870.png)

当配置完后将自动切换至此过滤配置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/6d10x-WwQgaRd4l2sm4TtQ/zh-cn_image_0000002779608795.png)

切换至此自定义配置时，日志级别过滤窗口和关键字过滤窗口将在此自定义配置过滤出的日志的基础上再进行过滤。

## 修改日志显示格式

支持开发者修改日志显示的格式。点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/4BFLkLe0RXKaIjXTRfDOoQ/zh-cn_image_0000002750009858.png "点击放大")图标。

* 标准视图：默认显示所有信息。
* 紧凑视图：默认显示日志级别与日志信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/zPpdbrgzQHO2HAzqoTrpqQ/zh-cn_image_0000002750169766.png)

## 超长日志自动换行

当单行日志过长时，用户可点击自动换行来使日志信息自适应当前窗口宽度，在末尾自动换行，在当前窗口中完整显示。

当日志消息过长时，日志窗口可能不能完整显示，需要拖动滚动条查看信息。此时开发者可以点击按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/3B5Gq4gFQuKXAz9hAWhhsQ/zh-cn_image_0000002779608787.png)控制日志消息自动换行。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/_ZeqJhgSTBiCDAIuMK5Dsg/zh-cn_image_0000002779608789.png)

## 显示最新日志

设备输出的日志信息会实时刷新到HiLog窗口底部，用户可点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/bpNwuoaTSWuKuPMbO65YGQ/zh-cn_image_0000002779728943.png)按钮使HiLog一直显示底部的最新日志信息。当观察到需要的日志时，点击HiLog窗口，即可停止滚动，停留在当前行，以便查看日志信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/8Bc2bHP5TDegr2FBppat9A/zh-cn_image_0000002779608791.png)

## 导出日志信息

开发者可将经过过滤后的关键日志信息保存到本地，以便进一步分析。

点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/Y2wFIuf9Rie9Sk2pysmi4A/zh-cn_image_0000002779608781.png "点击放大")按钮，在弹出的窗口中选择保存路径。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/vhm7p-MVQ_WGaxvscipkiw/zh-cn_image_0000002750009862.png)

## 清除日志缓存

与日志相关的缓存有两个：设备端日志缓存、HiLog窗口缓存。

HiLog显示日志信息的流程为：

1. 应用输出日志信息至设备端日志缓存；
2. 日志组件将设备端日志缓存取出，保存在HiLog窗口缓存中；
3. HiLog窗口根据过滤条件，将HiLog窗口缓存中的消息显示在界面中。

点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/OVrrfcsnQuSKwJJtKMq6lA/zh-cn_image_0000002750009874.png)按钮，将弹出两个选项**：清除控制台日志**、**清除设备日志**。

* **清除控制台日志**：清除HiLog窗口日志缓存。日志组件将重新从设备端日志缓存读取日志消息，因而执行清除操作前已保存在设备端日志缓存的日志消息会显示到HiLog窗口中。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/-4Z80uXjSSG0Z0ZZxGCykw/zh-cn_image_0000002779608799.png)
* **清除设备日志**：清除设备端日志缓存。此操作将清除设备端日志缓存和HiLog窗口缓存。HiLog窗口将显示执行清除操作后，新输出至设备端缓存的日志信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/Q2qubUj8QHSb0e6ntLXzSw/zh-cn_image_0000002750009878.png)

## 设置HiLog窗口缓存

HiLog窗口显示的日志信息保存在此窗口的缓存中，缓存的大小决定了当前窗口能显示的日志信息的最大数量，当日志超出缓存上限时，窗口中最早的日志将会被清除，新日志在窗口底部输出。开发者可以自行设置窗口的缓存大小。

进入**文件 > 设置 > 扩展 > HiLog Console**面板，或点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/y-aJGos7SgCaPt7cBMM02A/zh-cn_image_0000002750009866.png "点击放大")图标，选择控制台设置 > 缓冲区，默认缓存大小为4096KB，变更缓存大小后实时生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/09Q14Ry2R0OD1r-zuvBgKg/zh-cn_image_0000002750169772.png)

## 设置设备端日志缓存

使用hdc shell hilog -g命令可查看当前设备端设置的日志缓存。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/y0F3UCLYQfycsdtU7_CcFg/zh-cn_image_0000002779608785.png)

使用hdc shell hilog -G命令可更改设备端日志缓存大小。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/z2WuwO8ATSaIqpZnLxUQ8g/zh-cn_image_0000002750009876.png)

配合-t参数可单独设置某一类型的日志缓存大小。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/ZBU8cbJ4Q0Cqdz9SY_wuCw/zh-cn_image_0000002750009872.png)

超出设备端缓存日志将被落盘于设备data/log/hilog路径下，开发者可在此目录下载历史hilog日志并查看。
