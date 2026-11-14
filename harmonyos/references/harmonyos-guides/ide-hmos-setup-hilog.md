---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-setup-hilog
title: 日志分析
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 日志与故障分析 > 日志分析
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:17+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:8150e2d7266bbe3e3e67ad3b486e7b11df0c620f7e23fd23d5a389249061e5c8
---

鸿蒙电脑DevEco Studio提供了“**日志** **>** **HiLog**”窗口来查看设备当前所有应用实时打印的日志信息。点击DevEco Studio底部![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/5FM5frHyTmmcg6lI0v3ODw/zh-cn_image_0000002810750889.png?HW-CC-KV=V1&HW-CC-Date=20261114T004917Z&HW-CC-Expire=31536000000&HW-CC-Sign=76D71FB0AE25C7FB621D2427DAA962EBFCB665933F255889EC53063AF65E38DD "点击放大")图标打开日志面板并点击**HiLog**，进入HiLog日志面板。

HiLog默认显示的日志为以下6个部分：

| 第一列 | 第二列 | 第三列 | 第四列 | 第五列 | 第六列 |
| --- | --- | --- | --- | --- | --- |
| 时间戳 | 进程ID和线程ID | 日志标签 | 应用包名 | 日志级别 | 日志内容 |

开发者可通过设置包名、日志级别和搜索关键词来筛选日志信息，还可以使用自定义日志显示格式、日志导出、显示最新日志等功能。

HiLog窗口左侧各个按钮的作用为：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/WEdbMmmESwGT6KMD-9nmLA/zh-cn_image_0000002810750887.png?HW-CC-KV=V1&HW-CC-Date=20261114T004917Z&HW-CC-Expire=31536000000&HW-CC-Sign=CB17FC470BB15FED37F24E321405E010DA58B4B03B9DC480256056992301AF7F)：当该按钮处于选中状态时，日志自动换行显示，否则日志按行显示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/MIIwGfSUQ_OA6oGgG2gfBQ/zh-cn_image_0000002810630793.png?HW-CC-KV=V1&HW-CC-Date=20261114T004917Z&HW-CC-Expire=31536000000&HW-CC-Sign=106B85ADEDC91801ABD3A70FACFAD0F405FAE352CEA61F761F4D0F8862ABAB21)：当该按钮处于选中状态时，日志自动滚动到窗口底部，否则停留在当前日志显示处。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/4Vkt7g2TR5Wct5hDTrBcLQ/zh-cn_image_0000002810630785.png?HW-CC-KV=V1&HW-CC-Date=20261114T004917Z&HW-CC-Expire=31536000000&HW-CC-Sign=4092D54CED9A09F6564888DB81707249A5C2CD4CCF32DA9817E9AAC3E4EBE7AE)：单击该按钮可以清空窗口日志和设备缓存。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/aUgtl8j9QHiAguBMPtkRfw/zh-cn_image_0000002781471234.png?HW-CC-KV=V1&HW-CC-Date=20261114T004917Z&HW-CC-Expire=31536000000&HW-CC-Sign=F52F290F0CB97594B04FE84A0E578C5D55E234A5347C1A2BD2793D38DE82651C)：单击该按钮可以对当前选择的设备屏幕进行截屏，并保存在本地。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/wPvfRN57SHixQw7igcHj_A/zh-cn_image_0000002810630779.png?HW-CC-KV=V1&HW-CC-Date=20261114T004917Z&HW-CC-Expire=31536000000&HW-CC-Sign=E521B73F32751B666EE222CBE2FB2399D6DA15FB978804C319D90FBF7359281D)：单击该按钮可以保存日志缓存到指定文件。

## 过滤日志

### 按关键字过滤日志

在HiLog搜索框中输入需要过滤的信息，即可过滤所有包含此信息的日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/gaPncbfBQbqI0J2C9fwI4w/zh-cn_image_0000002781471230.png?HW-CC-KV=V1&HW-CC-Date=20261114T004917Z&HW-CC-Expire=31536000000&HW-CC-Sign=8E21C7B10CA2566786971ED0ED41663324EFE3D0E2A0622318160D2CDEE2C7E0)按钮表示是否区分大小写，![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/BLHsVFzPQ0KUItMsRWkqqw/zh-cn_image_0000002810630781.png?HW-CC-KV=V1&HW-CC-Date=20261114T004917Z&HW-CC-Expire=31536000000&HW-CC-Sign=D5D682B571421E68B09757EFE25EC3DAEFEABA9497B72BC9D11C2F68851F6EFF)按钮表示是否按照正则表达式匹配过滤。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/jBawT9VzT1WsAFe3E4-Y_w/zh-cn_image_0000002810630783.png?HW-CC-KV=V1&HW-CC-Date=20261114T004917Z&HW-CC-Expire=31536000000&HW-CC-Sign=F7937351BC8DDCCB50B23A998208BA735974497FF14277CABADB297FEBB42650)

### 使用默认提供的过滤配置

HiLog提供多种默认的过滤模式，无需反复输入关键字过滤日志信息，只需要切换相应的过滤项，即可快速过滤所需的日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/s7zLtgOoS3ew0oN8MJCMeA/zh-cn_image_0000002781471248.png?HW-CC-KV=V1&HW-CC-Date=20261114T004917Z&HW-CC-Expire=31536000000&HW-CC-Sign=26686EF7426E7D8BD612EDBE9E00344C3EBE5D81F9F27557926B079EF920CAD3)

* 选中应用的所有日志：按照应用进程过滤日志。
* 选中应用的用户日志：按照应用进程过滤用户输出的日志。

当使用**选中应用的所有日志**或**选中应用的用户日志**时，进程过滤下拉框处于可选状态，可选择相应的选项过滤想查看的进程日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/i0yX4LhXRX-lcermdl9MyA/zh-cn_image_0000002781311294.png?HW-CC-KV=V1&HW-CC-Date=20261114T004917Z&HW-CC-Expire=31536000000&HW-CC-Sign=9F8AB74EC131D2332339D7B2F824E869CA1E1A68B21C4D7736AAD9A2D2C4A1E7)

### 按日志级别过滤日志

HiLog提供日志级别过滤，用来过滤一个或多个级别的日志。日志级别分为Debug、Info、Warn、Error、Fatal五个级别。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/BeUb6eCgTjWHwINO7tlY8w/zh-cn_image_0000002781311296.png?HW-CC-KV=V1&HW-CC-Date=20261114T004917Z&HW-CC-Expire=31536000000&HW-CC-Sign=36BBE1CD9B7F32AF6C6765632EE307C4C3D917F2E84A8428E73AA74FD16A5CCD)

### 按自定义过滤项过滤日志

除默认过滤项外，HiLog还提供配置自定义过滤项的途径以供开发者按照实际需求过滤日志，并保存此过滤配置以供重复使用。

点击**新建自定义过滤配置**时将弹出自定义过滤配置窗口。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/LccUGViHSbqXaVPvF4LDBQ/zh-cn_image_0000002781471232.png?HW-CC-KV=V1&HW-CC-Date=20261114T004917Z&HW-CC-Expire=31536000000&HW-CC-Sign=C81F430FBD9BD580A86BBDE7AB6EB06607E81DA85CDD1C30167FC018A9E8A03C)

先前介绍的过滤选项此处均可配置，同时增加了**应用包名**和**同步至所有工程**配置项。

* 同步至所有工程：此配置当前工程及其他所有工程均可用。
* 应用包名：按应用包名过滤日志。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/XzwMrsEeQg2Nekms-NI7GQ/zh-cn_image_0000002810750895.png?HW-CC-KV=V1&HW-CC-Date=20261114T004917Z&HW-CC-Expire=31536000000&HW-CC-Sign=4ADD7F9D3CD55DEB4660448685DCABA6DB86D19704EC1ADFF2743443F5BB46F4)

当配置完后将自动切换至此过滤配置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/zwoaKjRzSqCe_7JDGhVHnA/zh-cn_image_0000002781471244.png?HW-CC-KV=V1&HW-CC-Date=20261114T004917Z&HW-CC-Expire=31536000000&HW-CC-Sign=31FE6A4472642BB51D57852F3BEF8E06FD03D9DC61D9D76E1AACFE8D0C201AEE)

切换至此自定义配置时，日志级别过滤窗口和关键字过滤窗口将在此自定义配置过滤出的日志的基础上再进行过滤。

## 修改日志显示格式

支持开发者修改日志显示的格式。点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/BYznvMozT6q7fMwxQZSgog/zh-cn_image_0000002781471228.png?HW-CC-KV=V1&HW-CC-Date=20261114T004917Z&HW-CC-Expire=31536000000&HW-CC-Sign=7EA5E000518AC38B4D587DFF6A6A9979B89937A016F1AB5A4BF555388AE470A8 "点击放大")图标。

* 标准视图：默认显示所有信息。
* 紧凑视图：默认显示日志级别与日志信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/kUr0NKEySeC-_evPZAm7Hg/zh-cn_image_0000002810630789.png?HW-CC-KV=V1&HW-CC-Date=20261114T004917Z&HW-CC-Expire=31536000000&HW-CC-Sign=1A700E0992403AE976929F93EC9A77740A3DD424B8C7AED688D9864E11CBB938)

## 超长日志自动换行

当单行日志过长时，用户可点击自动换行来使日志信息自适应当前窗口宽度，在末尾自动换行，在当前窗口中完整显示。

当日志消息过长时，日志窗口可能不能完整显示，需要拖动滚动条查看信息。此时开发者可以点击按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/FsUt9thdSlOQh6FtBJqobQ/zh-cn_image_0000002781471236.png?HW-CC-KV=V1&HW-CC-Date=20261114T004917Z&HW-CC-Expire=31536000000&HW-CC-Sign=6055E8F3B630C3D2856DDE902BA40DC6901F0484AB815A3A9C44783779EEF976)控制日志消息自动换行。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/WteQFFMXQdKUjpwqqldDQQ/zh-cn_image_0000002810750897.png?HW-CC-KV=V1&HW-CC-Date=20261114T004917Z&HW-CC-Expire=31536000000&HW-CC-Sign=40095584DF98E244A84D6656A672DE7DF218AEF4F20FA1005D5DF741111524FD)

## 显示最新日志

设备输出的日志信息会实时刷新到HiLog窗口底部，用户可点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/Bb3KvvL-R_uMt3fuW3TfBg/zh-cn_image_0000002781471246.png?HW-CC-KV=V1&HW-CC-Date=20261114T004917Z&HW-CC-Expire=31536000000&HW-CC-Sign=3876F6D913104804C2527841299EB6B9A937385F5B0B05E934FF157745BDD607)按钮使HiLog一直显示底部的最新日志信息。当观察到需要的日志时，点击HiLog窗口，即可停止滚动，停留在当前行，以便查看日志信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/axPGxV22QKCOAp1dnE_9ZQ/zh-cn_image_0000002810630791.png?HW-CC-KV=V1&HW-CC-Date=20261114T004917Z&HW-CC-Expire=31536000000&HW-CC-Sign=37B88891A9199D5E13CDBD86965815E2BCEA96813D5587D31E9CD9B0ED52D8F8)

## 导出日志信息

开发者可将经过过滤后的关键日志信息保存到本地，以便进一步分析。

点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/hb4a2BnBS-ucMa9785PxJA/zh-cn_image_0000002781311298.png?HW-CC-KV=V1&HW-CC-Date=20261114T004917Z&HW-CC-Expire=31536000000&HW-CC-Sign=C858F562952CFAF937D554B509EDE865E9619E5A9EABE0030D8BBD96C98732C7 "点击放大")按钮，在弹出的窗口中选择保存路径。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/uDt5BrKSSc-j73-vluy2kQ/zh-cn_image_0000002810750891.png?HW-CC-KV=V1&HW-CC-Date=20261114T004917Z&HW-CC-Expire=31536000000&HW-CC-Sign=45199C9A8956BDB8E8D0C68D0444700DF92869CB891B7450A7FE96DA4C932BD3)

## 清除日志缓存

与日志相关的缓存有两个：设备端日志缓存、HiLog窗口缓存。

HiLog显示日志信息的流程为：

1. 应用输出日志信息至设备端日志缓存；
2. 日志组件将设备端日志缓存取出，保存在HiLog窗口缓存中；
3. HiLog窗口根据过滤条件，将HiLog窗口缓存中的消息显示在界面中。

点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/5wYtihSDSo2fWIgeQ62b_g/zh-cn_image_0000002810750899.png?HW-CC-KV=V1&HW-CC-Date=20261114T004917Z&HW-CC-Expire=31536000000&HW-CC-Sign=D21788B5176BC7C3894E25684596FFBB6089295E6EC8F989341C01190E1F7150)按钮，将弹出两个选项**：清除控制台日志**、**清除设备日志**。

* **清除控制台日志**：清除HiLog窗口日志缓存。日志组件将重新从设备端日志缓存读取日志消息，因而执行清除操作前已保存在设备端日志缓存的日志消息会显示到HiLog窗口中。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/zRBBs_ETRnawfYzS3NoHog/zh-cn_image_0000002781311312.png?HW-CC-KV=V1&HW-CC-Date=20261114T004917Z&HW-CC-Expire=31536000000&HW-CC-Sign=EADCCA75381E8541988F52809DE984ABF3D856A3D1EEF3AC2B28590490128787)
* **清除设备日志**：清除设备端日志缓存。此操作将清除设备端日志缓存和HiLog窗口缓存。HiLog窗口将显示执行清除操作后，新输出至设备端缓存的日志信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/2lTpIYIiQ7iWNuLLWcO6jA/zh-cn_image_0000002810750903.png?HW-CC-KV=V1&HW-CC-Date=20261114T004917Z&HW-CC-Expire=31536000000&HW-CC-Sign=DB7CCA3431C97D54BACC3E4C48229408646142B9FBAD614AD47E2DB0629B0802)

## 设置HiLog窗口缓存

HiLog窗口显示的日志信息保存在此窗口的缓存中，缓存的大小决定了当前窗口能显示的日志信息的最大数量，当日志超出缓存上限时，窗口中最早的日志将会被清除，新日志在窗口底部输出。开发者可以自行设置窗口的缓存大小。

进入**文件 > 设置 > 扩展 > HiLog Console**面板，或点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/xBzyc39MTBalFfHztWIu_A/zh-cn_image_0000002810750893.png?HW-CC-KV=V1&HW-CC-Date=20261114T004917Z&HW-CC-Expire=31536000000&HW-CC-Sign=82A21A0AF1946EBBED09E7EF4DB0CCBB8C26ADF71A40C37DB015C452190FA9AE "点击放大")图标，选择控制台设置 > 缓冲区，默认缓存大小为4096KB，变更缓存大小后实时生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/xzlXllKwR3StPU8ga5g5Uw/zh-cn_image_0000002781311310.png?HW-CC-KV=V1&HW-CC-Date=20261114T004917Z&HW-CC-Expire=31536000000&HW-CC-Sign=AA7A7F89C6CF5877E6131B2AEFB15BFEAAA3B21100E7B7D11228C0183EF9F77C)

## 设置设备端日志缓存

使用hdc shell hilog -g命令可查看当前设备端设置的日志缓存。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/2zT9OyVbQqeOn0xD0uw2wQ/zh-cn_image_0000002781311300.png?HW-CC-KV=V1&HW-CC-Date=20261114T004917Z&HW-CC-Expire=31536000000&HW-CC-Sign=4409C1B918EDB42B316B948EDE92424309A7C8863C48B5083CA651ED0A53F1CD)

使用hdc shell hilog -G命令可更改设备端日志缓存大小。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/z1v4cStnRgSBU4XvEqH5gA/zh-cn_image_0000002810750901.png?HW-CC-KV=V1&HW-CC-Date=20261114T004917Z&HW-CC-Expire=31536000000&HW-CC-Sign=AD2388E759026E26065804CA25F986C87F5996E3735D3A8F21CD7F5BA8B8F96E)

配合-t参数可单独设置某一类型的日志缓存大小。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/9IixVEDXQkmluCufpzTTCw/zh-cn_image_0000002810630787.png?HW-CC-KV=V1&HW-CC-Date=20261114T004917Z&HW-CC-Expire=31536000000&HW-CC-Sign=C2E27C346308B3F575D1DF7DD5D2E04DE9DC01F4F25186E332B17A414FCB308D)

超出设备端缓存日志将被落盘于设备data/log/hilog路径下，开发者可在此目录下载历史hilog日志并查看。
