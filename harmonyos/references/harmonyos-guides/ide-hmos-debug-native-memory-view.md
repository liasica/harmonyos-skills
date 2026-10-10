---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-debug-native-memory-view
title: 查看内存信息
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 查看内存信息
category: harmonyos-guides
scraped_at: 2026-10-11T07:23:21+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:0e573b5e41eeffab4a56d64fdaa5c63fb8b821e575c7cdf6d2ef32342a17a6ca
---

在native调试窗口中，点击**内存**，打开内存查看窗口。

## 查看指定地址内存

在内存视图中，填写地址、数量、进制，点击地址旁的搜索按钮，或者按回车键，查看对应地址处的内存。

返回的数据显示在下面的数据表中，第一列显示地址，0-F每个方框显示一个字节内存数据的16进制形式，一行显示16个字节的内存数据，最后一列显示每一个字节对应的ASCII值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/tSPNBzFqTNuKPvIDIlb2Ug/zh-cn_image_0000002750009844.png)

支持内存值以十六进制、十进制、二进制展示，下拉框选择**Hexadecimal、Decimal或Binary**，默认为**Hexadecimal**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/5AtGFW0vTzeWfqulkSsE3w/zh-cn_image_0000002750169738.png)

## 内存修改

可以在内存格上双击，输入想要修改的内存来修改对应地址处的内存值。十六进制可以输入1-2位，十进制可以输入1-3位，二进制可以输入1-8位，输入的值转换为十进制数值范围为0-255（一个字节8位）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/Aj4Up4dCTGyMigvDm7mP8A/zh-cn_image_0000002779608759.png)

修改完之后，ASCII码也会同步刷新。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/O7lpsFd_RDuM-gKXcQiLvg/zh-cn_image_0000002779728909.png)
