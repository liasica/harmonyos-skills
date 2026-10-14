---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-debug-native-variables
title: 检查变量
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 检查变量
category: harmonyos-guides
scraped_at: 2026-10-15T07:06:48+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:e0b01c9a5753839bf25e89323c2c8adb6798b50021e8b23bc85166fb81ea46e0
---

调试时，在“变量”页面查看变量，支持查看全局/静态变量、寄存器变量和局部变量。

## 查看全局/静态变量

点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/gJc49qNcSuiOneMsjO9gIg/zh-cn_image_0000002779608681.png "点击放大")按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/3pLubvmMRh6R6HwZbP1iHQ/zh-cn_image_0000002779728833.png)按钮打开配置界面。在**调试器**中勾选**在变量面板中显示静态/全局变量**，调试过程中变量列表会展示静态/全局变量。

## 变量监视/表达式求值

通过在变量页面的输入框输入需要监控的变量或变量表达式，在每次程序停住之后会计算表达式的值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/2Uwee4HIQUmxqqXbnOuVgQ/zh-cn_image_0000002750169656.png)

## 查看函数返回值

当使用“Step Out”从一个函数内步出后，变量列表中的“ReturnValues”会展示所步出函数的返回值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/UAtv5YCVSuCQ9_Cn_XZB8Q/zh-cn_image_0000002750009766.png)

**说明** 

* 不支持查看长度超过64位的数据结构；
* 不支持查看引用类型返回值。
