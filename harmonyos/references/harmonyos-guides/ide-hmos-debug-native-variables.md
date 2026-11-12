---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-debug-native-variables
title: 检查变量
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 检查变量
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:896687389fc5d320db73b4e451068c5a54e936e2a40c171fe9c9c4adec1f4bc5
---

调试时，在“变量”页面查看变量，支持查看全局/静态变量、寄存器变量和局部变量。

## 查看全局/静态变量

点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/SGxxozT9SC28EuPXa5NiqQ/zh-cn_image_0000002781311206.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=532595C9A2A9E3C09EB55E4CA4837F42CE8904250D0FA11434E64C796E1531C5 "点击放大")按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/2cNAocXCStaJaH_jkCz53w/zh-cn_image_0000002810630693.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=CDA929E0D19C02F9C9728DAE44C8A96A8291BF2D6C2F0E9C6CD3A741849C5F00)按钮打开配置界面。在**调试器**中勾选**在变量面板中显示静态/全局变量**，调试过程中变量列表会展示静态/全局变量。

## 变量监视/表达式求值

通过在变量页面的输入框输入需要监控的变量或变量表达式，在每次程序停住之后会计算表达式的值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/fpvm0mhLSmucJlXCkJwKDw/zh-cn_image_0000002781471138.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=12FA0C1ED6135550A1C6DE94A8ED87BB45E9666EB793F20BA0DC16C3404638D8)

## 查看函数返回值

当使用“Step Out”从一个函数内步出后，变量列表中的“ReturnValues”会展示所步出函数的返回值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/A2ezCI-ATJqXbJucYCqVPw/zh-cn_image_0000002781311204.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=711708FB9A3F78DCE85CA20200FC8B521AA68EC1A142309F7A3B872EE1FEEF78)

**说明** 

* 不支持查看长度超过64位的数据结构；
* 不支持查看引用类型返回值。
