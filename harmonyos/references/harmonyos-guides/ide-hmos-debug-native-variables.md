---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-debug-native-variables
title: 检查变量
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 检查变量
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:46+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:1271872a2462f8a954979b1d1f5ed5db1d1c463cbeaa93418797cc4cb22ae9c2
---

调试时，在“变量”页面查看变量，支持查看全局/静态变量、寄存器变量和局部变量。

## 查看全局/静态变量

点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/EtXaCBFRRV2TvGh6llekgw/zh-cn_image_0000002820680871.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=E948EA2EF9E5A2F5AC440FCA7D5F03CC28185270BD62E37D9BAC9DFCDF8B5FDD "点击放大")按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/NvLGDeoAQzq86Kv_5g45sg/zh-cn_image_0000002791840940.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=987FC8FE0F3725F8AB63BD0550BC908592BB26B5A659EF0928C8D3F98C608A53)按钮打开配置界面。在**调试器**中勾选**在变量面板中显示静态/全局变量**，调试过程中变量列表会展示静态/全局变量。

## 变量监视/表达式求值

通过在变量页面的输入框输入需要监控的变量或变量表达式，在每次程序停住之后会计算表达式的值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/bmlk0_xdQGuwVTfrXL-R4A/zh-cn_image_0000002820680877.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=4AAA10A56FD7FB31C228DAFCBE0A89DAC4092141D2A7FCB4075CEDD8F0B5456E)

## 查看函数返回值

当使用“Step Out”从一个函数内步出后，变量列表中的“ReturnValues”会展示所步出函数的返回值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/IuhsZtgXTsew7YoZeHPcnQ/zh-cn_image_0000002792000912.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=CAC55F451626B14079EA2BC9D8FD65F9BD3B6797BC2B19CAE6495D9E156CA9C7)

**说明** 

* 不支持查看长度超过64位的数据结构；
* 不支持查看引用类型返回值。
