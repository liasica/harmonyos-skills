---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-lldb-client-alive
title: Native调试启动加速
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > Native调试启动加速
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:30+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:c01c9be7949dc8f770c71787d4a92204ec8193e1dc24ab74dd5f5803f274707d
---

在大型工程中，Native调试的启动耗时较长。为提升开发调试效率，从26.0.0版本开始，新增Native调试启动加速功能。开启该功能后，首次调试完成时，调试服务器会保持活跃状态，后续再次启动调试时，可以大幅减少调试连接的耗时。

## 使用约束

* 该配置是工程级配置，每个工程需要单独开启。
* 同一个工程中，同时创建多个Native调试会话，该加速功能只对第一个调试会话有效。

## 操作步骤

在**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> Build, Execution, Deployment > Debugger > C++ Debugger**中，勾选**Keep LLDB client alive**开启Native调试启动加速功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/TGbemIchSoSu5VVNtSMXVA/zh-cn_image_0000002808766573.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=B20BA957A6D2DF489586BAAEF24934A7635F05FFE45EABC38CC615CD9D0AD72C)

也可以通过调试窗口控制台的超链接跳转到设置中开启。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/BMwovyQzRyeA5I8q4scMGg/zh-cn_image_0000002779566992.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=ADE86D2926DD62A826D66E725958AC4ED39AFE7DC8D8DEB009327DCD5A99063B)

开启开关并启动调试后，DevEco Studio底部会有调试服务器图标，调试过程中不能关闭服务器。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/fQb4G9d6Q3qmNV4tX-WylQ/zh-cn_image_0000002779407014.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=04A43F151D919088AB7E342F66CD57AD72951CC3AD7D93DBC153771A8E1E64D3)

同时，开启开关后会占用内存和磁盘空间，在不调试时，可手动释放资源。

* 释放内存：点击DevEco Studio底部的调试服务器图标，关闭调试服务器释放内存。
* 释放磁盘空间：点击**File >** **Invalidate Caches**，勾选**Clear LLDB caches**，点击**Invalidate and Restart**重启DevEco Studio以清理缓存数据。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/e5xbLas9RUidKwNS5HqkBg/zh-cn_image_0000002808886653.png?HW-CC-KV=V1&HW-CC-Date=20261124T044230Z&HW-CC-Expire=31536000000&HW-CC-Sign=98E1CE5FCC95544134169BC1F6C0C5CB5DC994848D09815BBA6B531C852E094D)
