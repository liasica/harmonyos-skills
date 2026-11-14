---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-debug-native-variables
title: 检查变量
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 检查变量
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:16+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:6726781852bc845f1d0ad3bc17a016183be103ee30c2cad2a39faa27ebe111f7
---

调试时，在“变量”页面查看变量，支持查看全局/静态变量、寄存器变量和局部变量。

## 查看全局/静态变量

点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/nhXn4iPAQlitBthwryCisw/zh-cn_image_0000002781311206.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=35E50433110BD0B2CA38CE13F87E3C5DEF7D71D80DFDB6EC8A03B7B4C52EE140 "点击放大")按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/_6IUbaKbSS6CwGoOQG-rIQ/zh-cn_image_0000002810630693.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=D51806338E32AA8D27F465F16EAE243EAE6CBADFE3B8C8B881DCE04415043513)按钮打开配置界面。在**调试器**中勾选**在变量面板中显示静态/全局变量**，调试过程中变量列表会展示静态/全局变量。

## 变量监视/表达式求值

通过在变量页面的输入框输入需要监控的变量或变量表达式，在每次程序停住之后会计算表达式的值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/Hn8lbCtQR_y61sDgpiTDAA/zh-cn_image_0000002781471138.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=932A4CD82645F210DBB9BB2AD04ABF642BD3B2D645DA0182A504171152D53A5C)

## 查看函数返回值

当使用“Step Out”从一个函数内步出后，变量列表中的“ReturnValues”会展示所步出函数的返回值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/exbQ7seYRs2zNkMyT4G3qw/zh-cn_image_0000002781311204.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=E5FECEAB699BF3EB748B705506B5E97B51225E5F739D3D10CAC71C7E55B91AFD)

**说明** 

* 不支持查看长度超过64位的数据结构；
* 不支持查看引用类型返回值。
