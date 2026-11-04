---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-lldb-client-alive
title: Native调试启动加速
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > Native调试启动加速
category: harmonyos-guides
scraped_at: 2026-11-04T08:31:28+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:639b64b919437c27fc5fdb930f980e7981526659bb19d61284c93d9870e916ed
---

在大型工程中，Native调试的启动耗时较长。为提升开发调试效率，从26.0.0版本开始，新增Native调试启动加速功能。开启该功能后，首次调试完成时，调试服务器会保持活跃状态，后续再次启动调试时，可以大幅减少调试连接的耗时。

## 使用约束

* 该配置是工程级配置，每个工程需要单独开启。
* 同一个工程中，同时创建多个Native调试会话，该加速功能只对第一个调试会话有效。

## 操作步骤

在**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> Build, Execution, Deployment > Debugger > C++ Debugger**中，勾选**Keep LLDB client alive**开启Native调试启动加速功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/z-a7dTqlRTqgyQxCg_VA-g/zh-cn_image_0000002731382321.png)

也可以通过调试窗口控制台的超链接跳转到设置中开启。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/LWIsE2FDTAWkU4ewk1Db2g/zh-cn_image_0000002731542293.png)

开启开关并启动调试后，DevEco Studio底部会有调试服务器图标，调试过程中不能关闭服务器。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/UPFYSD3PSUmTj8DWwFx0Kw/zh-cn_image_0000002701663098.png)

同时，开启开关后会占用内存和磁盘空间，在不调试时，可手动释放资源。

* 释放内存：点击DevEco Studio底部的调试服务器图标，关闭调试服务器释放内存。
* 释放磁盘空间：点击**File >** **Invalidate Caches**，勾选**Clear LLDB caches**，点击**Invalidate and Restart**重启DevEco Studio以清理缓存数据。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/5lk2Jep2Tx2uIw1lzq4VRA/zh-cn_image_0000002701823020.png)
