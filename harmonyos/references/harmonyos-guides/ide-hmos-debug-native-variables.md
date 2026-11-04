---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-debug-native-variables
title: 检查变量
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 检查变量
category: harmonyos-guides
scraped_at: 2026-11-04T08:31:48+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:34dc68cf8a893b0c7a422c8e4b9962b7e1dd4ceb4f12a5fefd85314b10cfc91f
---

调试时，在“变量”页面查看变量，支持查看全局/静态变量、寄存器变量和局部变量。

## 查看全局/静态变量

点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/z2J6XrT2RBSZk8BiBZypcA/zh-cn_image_0000002779608681.png "点击放大")按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/yEtkc68sSQGgRiTxFeUKuA/zh-cn_image_0000002779728833.png)按钮打开配置界面。在**调试器**中勾选**在变量面板中显示静态/全局变量**，调试过程中变量列表会展示静态/全局变量。

## 变量监视/表达式求值

通过在变量页面的输入框输入需要监控的变量或变量表达式，在每次程序停住之后会计算表达式的值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/jxC5b4r9RvK5Xuswx29s3Q/zh-cn_image_0000002750169656.png)

## 查看函数返回值

当使用“Step Out”从一个函数内步出后，变量列表中的“ReturnValues”会展示所步出函数的返回值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/9J0lDiVBT8u79YpqKwd1sQ/zh-cn_image_0000002750009766.png)

**说明** 

* 不支持查看长度超过64位的数据结构；
* 不支持查看引用类型返回值。
