---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-debug-native-memory-view
title: 查看内存信息
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 查看内存信息
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:16+08:00
doc_updated_at: 2026-11-06
content_hash: sha256:aba987965aca3e459d3ce49626336926721288d8d86f3e84572cf8442a2968a2
---

在native调试窗口中，点击**内存**，打开内存查看窗口。

## 查看指定地址内存

在内存视图中，填写地址、数量、进制，点击地址旁的搜索按钮，或者按回车键，查看对应地址处的内存。

返回的数据显示在下面的数据表中，第一列显示地址，0-F每个方框显示一个字节内存数据的十六进制形式，一行显示16个字节的内存数据，最后一列显示每一个字节对应的ASCII值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/VSOk0yhURyyL6p_bVL9ZSg/zh-cn_image_0000002781311274.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=7D9D405E7DF1BD78A9E24162C3A1111F9FDEAD69D63189A996AC0B0D0C4B037A)

支持内存值以十六进制、十进制、二进制展示，下拉框选择**Hexadecimal、Decimal或Binary**，默认为**Hexadecimal**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/2qMiayfFTrC4sY-SqO8Wbw/zh-cn_image_0000002781471210.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=2B68E2FAD7D1F5B91B26B53A41A6224E0C46CE5C8C31FCF8A63E3ABA805EF0F4)

## 内存修改

可以在内存格上双击，输入想要修改的内存来修改对应地址处的内存值。十六进制可以输入1-2位，十进制可以输入1-3位，二进制可以输入1-8位，输入的值转换为十进制数值范围为0-255（一个字节8位）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/zEdLrVQETBGuuE3fcRfy8g/zh-cn_image_0000002781471208.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=5C8FBBCF87AAA5117E635550BACC6B310327FEF7AF4B61B75B9A8A1E71E81987)

修改完之后，ASCII码也会同步刷新。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/-wo1mhZiSmWwa9AiI78rsQ/zh-cn_image_0000002781311276.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=5ACA4C2C50C993FB1EE66C66FCB91E77B62924BDF82FF1B6A1BCE235644EF4B9)
