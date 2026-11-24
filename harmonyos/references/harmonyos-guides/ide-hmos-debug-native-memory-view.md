---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-debug-native-memory-view
title: 查看内存信息
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 查看内存信息
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:46+08:00
doc_updated_at: 2026-11-06
content_hash: sha256:e129291a33366791fc9a2eec17222671c974afb683ae4f1bbeede064ce2d9370
---

在native调试窗口中，点击**内存**，打开内存查看窗口。

## 查看指定地址内存

在内存视图中，填写地址、数量、进制，点击地址旁的搜索按钮，或者按回车键，查看对应地址处的内存。

返回的数据显示在下面的数据表中，第一列显示地址，0-F每个方框显示一个字节内存数据的十六进制形式，一行显示16个字节的内存数据，最后一列显示每一个字节对应的ASCII值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/nDdn3ArWTTaGRMzLZy2SaA/zh-cn_image_0000002791841304.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=61C769E32EC34A3572308FF2F0EC85B192F43F5930BE78D0EEB6AFD8907ADBF4)

支持内存值以十六进制、十进制、二进制展示，下拉框选择**Hexadecimal、Decimal或Binary**，默认为**Hexadecimal**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/7M2mRHWoS9mnf-T3ISgLFw/zh-cn_image_0000002792001276.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=4747755CCEA1C6305AECF2A6E5A9711462C987AC2A1B25B96D5C7E17E10DDA54)

## 内存修改

可以在内存格上双击，输入想要修改的内存来修改对应地址处的内存值。十六进制可以输入1-2位，十进制可以输入1-3位，二进制可以输入1-8位，输入的值转换为十进制数值范围为0-255（一个字节8位）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/KXIB0XQiRy6sticLpP5SFg/zh-cn_image_0000002820721247.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=97C5B844C10405E8E6B0AEF7FE064E1E704D544264F836ABBD333853A1A617D0)

修改完之后，ASCII码也会同步刷新。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/hPzPbud4Tq-vyfJUdHKAEQ/zh-cn_image_0000002820681239.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=0D3CBAA713E4C090EDCF494F6A8D55A8E76A5097C6A20EE6812E46D4E110D3D0)
