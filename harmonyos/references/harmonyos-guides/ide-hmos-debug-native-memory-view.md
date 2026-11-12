---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-debug-native-memory-view
title: 查看内存信息
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 查看内存信息
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-06
content_hash: sha256:ce2dee4fc69c15e42eacb02908898b19247cd382742458e9813e40950499221d
---

在native调试窗口中，点击**内存**，打开内存查看窗口。

## 查看指定地址内存

在内存视图中，填写地址、数量、进制，点击地址旁的搜索按钮，或者按回车键，查看对应地址处的内存。

返回的数据显示在下面的数据表中，第一列显示地址，0-F每个方框显示一个字节内存数据的十六进制形式，一行显示16个字节的内存数据，最后一列显示每一个字节对应的ASCII值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/RE4BTzdRSYK6YlBdplNHXA/zh-cn_image_0000002781311274.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=8944AD0DF498016E145A54FECB708636148610C8D9C2CF59C1A5A3DA35E31652)

支持内存值以十六进制、十进制、二进制展示，下拉框选择**Hexadecimal、Decimal或Binary**，默认为**Hexadecimal**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/HkmDfEhbSkm5b5v2MZKphg/zh-cn_image_0000002781471210.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=757104E305ABBC1531A9121AD3EBD3E3E7C840926E379862F66E2F7F86EC7D9F)

## 内存修改

可以在内存格上双击，输入想要修改的内存来修改对应地址处的内存值。十六进制可以输入1-2位，十进制可以输入1-3位，二进制可以输入1-8位，输入的值转换为十进制数值范围为0-255（一个字节8位）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/pH1XqSg9ShqKslHOHYevtg/zh-cn_image_0000002781471208.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=0290ABD9B65682F2DF309EB61A8DD17922F74492099374022585210C7E9E97E2)

修改完之后，ASCII码也会同步刷新。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/jGRSj8RlS_aXGcUkz5jEpw/zh-cn_image_0000002781311276.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=EBB73053AAF379A45E16E06CA683D9C70CB3164B820154089CD70C8D2C7158A6)
