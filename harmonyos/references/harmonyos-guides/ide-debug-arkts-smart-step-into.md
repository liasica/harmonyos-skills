---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-smart-step-into
title: 智能步入
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > 智能步入
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:3decb14bef419f9fcfef4b3030f84db525e244c3e3af07df73301e85ffd165ca
---

当代码行存在多个函数嵌套或调用时，开发者可以通过Smart Step Into的能力来步入到想要调试的函数内，如果在调试时想跳过某些文件，也可以自定义需要跳过的文件列表。

## 智能步入

1. 启动调试，如果断点所在的一行内存在多个方法调用，可以通过点击调试窗口的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/pSkYgqB8QLuvBv44MQxtCg/zh-cn_image_0000002808887071.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=089DD677AE5A0FA210E54A0C963408E912937CA85A49013FAC4462E1BCB4539A)按钮或快捷键Shift + F7高亮展示可步入的函数。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/G104PTHZSDOt48X8jLSLYQ/zh-cn_image_0000002808766987.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=6D7D1621944D081B3EF2C050019DC26A9EDBBBF6C6834BFEFB759C8E4044DE85)
2. 点击其中一个函数即可步入。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/nns9yflQSMqtlG8xfpdZXQ/zh-cn_image_0000002808766993.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=485011B947511764A9C7A433593D9119DAE9E4F7068DB2B5490C865865BBA49E)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/uEmtF6kLTmquznVTaL7ULw/zh-cn_image_0000002779567408.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=344FEADCDE6654EF0BDABB54376411A7FB6C30580D11495A8E03E51559A76086)

## 过滤脚本文件

1. 点击**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **>** **Build, Execution, Deployment > Debugger > Stepping**，勾选**Do not step into ArkTS scripts**， 可在调试时禁止智能步入某些脚本。使用工具栏按钮管理要跳过的脚本列表。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/Nb5dZYEjTe2hYCnHqZairg/zh-cn_image_0000002779407434.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=F9C41E4775204703B57EBFF4F4E7E473D4233B30A0903454FD46040474606D54)
2. 单击 **+** 按钮可添加新的脚本过滤器。在打开的对话框中，输入要跳过的文件名称或使用通配符。例如，如果要始终跳过 JavaScript文件，请输入 \*.js。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/B-7q0hhvRX2zF78n-M_FgQ/zh-cn_image_0000002779567414.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=D45EF985DAB0E9B10195114838B08B7764341ED85C86CB03D5E91924300BD920)
