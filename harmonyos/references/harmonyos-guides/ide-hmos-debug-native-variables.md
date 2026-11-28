---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-debug-native-variables
title: 检查变量
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 检查变量
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:55+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:593d5ff9aafc84d87e76c5f01ca6383efb1c0188c6a0353e2a8d38d5ff72bb11
---

调试时，在“变量”页面查看变量，支持查看全局/静态变量、寄存器变量和局部变量。

## 查看全局/静态变量

点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/muffLJ6zQReC3OfsoCagaw/zh-cn_image_0000002820680871.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=2E67A46FB631A68683C4AB9AEB916EE71ED977F6AB6B97D127118E19E4F0E43C "点击放大")按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/kcdhLCHXTH6EWE8tuo5gmw/zh-cn_image_0000002791840940.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=48AB757F4C779973C7939FDA796EB01B1E4A715AC49999909BED8C3798172736)按钮打开配置界面。在**调试器**中勾选**在变量面板中显示静态/全局变量**，调试过程中变量列表会展示静态/全局变量。

## 变量监视/表达式求值

通过在变量页面的输入框输入需要监控的变量或变量表达式，在每次程序停住之后会计算表达式的值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/I2eOIDKgRGOdPJHKaOgAfA/zh-cn_image_0000002820680877.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=B406BCEDE2A41E2AFCF793D021099A289B71B1B1AC7F04D6A1DCCAFE1112FED6)

## 查看函数返回值

当使用“Step Out”从一个函数内步出后，变量列表中的“ReturnValues”会展示所步出函数的返回值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/EDTvPi0oTQm_gsKPlyXl3A/zh-cn_image_0000002792000912.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=39947C37F28ED47FDFFCB861C079D7270BCE2B20A4A57A81BA1652B3F010D536)

**说明** 

* 不支持查看长度超过64位的数据结构；
* 不支持查看引用类型返回值。
