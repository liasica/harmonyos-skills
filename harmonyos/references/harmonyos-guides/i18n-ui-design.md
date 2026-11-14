---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/i18n-ui-design
title: 国际化界面设计
breadcrumb: 指南 > 应用框架 > Localization Kit（本地化开发服务） > 应用国际化 > 国际化界面设计
category: harmonyos-guides
scraped_at: 2026-11-14T08:47:20+08:00
doc_updated_at: 2026-09-04
content_hash: sha256:c9f16853dea3d7bf5ddac0f4edce33ef77f6445bdb6ae03302d07510e36c814b
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/R4JHNyGvRMu8GrYmAQ8ttw/zh-cn_image_0000002788467266.png?HW-CC-KV=V1&HW-CC-Date=20261114T004541Z&HW-CC-Expire=31536000000&HW-CC-Sign=6F55E62A2FCA02CFF6A6C3A9D4CF1CCEBDDF071CF31CF8351F5134EE1543235B)

**图2** 镜像布局示例（阿拉伯文）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/GuUF1q2mTby-P_W_jFs8Yg/zh-cn_image_0000002817506755.png?HW-CC-KV=V1&HW-CC-Date=20261114T004541Z&HW-CC-Expire=31536000000&HW-CC-Sign=AF8823A1E5B46D027C27205DDCC2B871C4F5518C1F8A0C9F704BFF0B0A7704BA)

**图3** 一般图标资源

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/ZvW8rC83R-ilTWT2b-V3HQ/zh-cn_image_0000002788307324.png?HW-CC-KV=V1&HW-CC-Date=20261114T004541Z&HW-CC-Expire=31536000000&HW-CC-Sign=B1366A9FDF406012EF515B6AB9111490C6D834E078B83A2EF13C59460E0A47A8)

**图4** RTL语言系统下提供的图标资源

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/DhvWsPNzSpO9VuG8Gov3-w/zh-cn_image_0000002817426687.png?HW-CC-KV=V1&HW-CC-Date=20261114T004541Z&HW-CC-Expire=31536000000&HW-CC-Sign=EFD00264857A4195F66F65D5262DC54F09954E56942435D698511187EC714BDC)

**图5** RTL语言下提供的镜像控件

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/Hnj-KV8gTEmjETgpS8wuUg/zh-cn_image_0000002788467268.png?HW-CC-KV=V1&HW-CC-Date=20261114T004541Z&HW-CC-Expire=31536000000&HW-CC-Sign=0A272455334549E0257A857E1FDE739D3B9B49779A27A88CF1573CF15961FE73)
