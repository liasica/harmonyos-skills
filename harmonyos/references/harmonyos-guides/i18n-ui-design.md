---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/i18n-ui-design
title: 国际化界面设计
breadcrumb: 指南 > 应用框架 > Localization Kit（本地化开发服务） > 应用国际化 > 国际化界面设计
category: harmonyos-guides
scraped_at: 2026-11-21T09:11:24+08:00
doc_updated_at: 2026-09-04
content_hash: sha256:2d8444ca9aa4c861763d2cbce53dc0de33acc2743c390eae8607eb72a907506b
---

一套有效的国际化界面布局设计规则，既可以树立产品在国际化设计中产品调性，还可以保证操作的一致性，遵循以下设计规则可有效提升应用全球化质量。

## 界面空间预留与灵活布局

不同语言的译文长度存在较大差异，翻译可能造成界面文本长度增加。为了确保界面字符串翻译成其他语言后不被截断，最佳做法是使用灵活的动态布局，即UI控件根据文本内容长度动态调整，重新排版。若无法保证灵活布局，则应预留足够的文本空间。以英文为基础，相对于原始英语字符串，翻译需要预留的空间参考如表1。

**表1** 界面预留空间参考表

| 英文字符数量（个） | 预留的空间比率 |
| --- | --- |
| 小于等于10 | 100%～200% |
| 大于等于11，小于等于20 | 80%～100% |
| 大于等于21，小于等于30 | 60%～80% |
| 大于等于31，小于等于50 | 40%～60% |
| 大于等于51，小于等于70 | 30%～40% |
| 大于等于71 | 30% |

## 界面镜像

不同国家对文本对齐方式和读取顺序有所不同，例如英语采用从左到右的顺序，阿拉伯语则采用从右到左（RTL）的顺序。为了使界面显示的内容符合当地用户语言习惯，需确保UI元素布局支持界面镜像，如图1和图2。UI元素界面镜像的设计要点如下：

* 用户界面（UI）布局镜像。用户界面排列允许从右到左的内容按其原始布局显示，满足双向市场体验。如“ABC”，按照从左到右的顺序应显示“ABC”，按照从右向左的顺序应显示为“CBA”。
* UI元素镜像。带有方向性的UI元素控件和图标，遵循镜像规则。如图3、图4、图5。某些图标没有方向性或者与现实中的物体相关，不需要镜像，例如时钟表盘。
* 触控与操作。界面各元素触控或操作符合从右至左的阅读顺序。例如，对于多页签，一般情况下往左划表示往后，而在RTL语言下，往右划表示往后。
* 支持混合文本。文本方向支持可实现出色的混合文本呈现（双向版本中有英语文本，反之亦然）。

**图1** 一般布局示例（英文）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/DpHygpCmSHecDR82AFekuA/zh-cn_image_0000002821757211.png?HW-CC-KV=V1&HW-CC-Date=20261121T010959Z&HW-CC-Expire=31536000000&HW-CC-Sign=0BBEB69DB9797DB17B302F735F0702576672DBFE9C06527D9D51BC2567A56671)

**图2** 镜像布局示例（阿拉伯文）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/eVOeQ8sHTWSObYFAU4rzXQ/zh-cn_image_0000002793037274.png?HW-CC-KV=V1&HW-CC-Date=20261121T010959Z&HW-CC-Expire=31536000000&HW-CC-Sign=720800CF713C885E67DDE271B41C7F5F123CFD4200109EC59C0CAA36A29E179E)

**图3** 一般图标资源

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/Zey3upm9R2aQQXquRHq4MQ/zh-cn_image_0000002792877304.png?HW-CC-KV=V1&HW-CC-Date=20261121T010959Z&HW-CC-Expire=31536000000&HW-CC-Sign=F486885283520AB582EA08327466194472C52FF28C858E73601110EA67AA93A2)

**图4** RTL语言系统下提供的图标资源

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/tFWkYRiASFmCVYDKvauWLg/zh-cn_image_0000002821837211.png?HW-CC-KV=V1&HW-CC-Date=20261121T010959Z&HW-CC-Expire=31536000000&HW-CC-Sign=A87AA2455D06DAB19E358C1DE21E9801943F9C7CA1FA25DDCF3861A92C7F1F8B)

**图5** RTL语言下提供的镜像控件

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/FKGbcz9aR9uLKY4EalXT3g/zh-cn_image_0000002821757213.png?HW-CC-KV=V1&HW-CC-Date=20261121T010959Z&HW-CC-Expire=31536000000&HW-CC-Sign=8C4B94C406467C2660DA0F987931A148F20780C05B104D7FA7D89CEBA798D40C)
