---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-lldb-client-alive
title: Native调试启动加速
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > Native调试启动加速
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:00+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:8e74495a01899cd6da8004487f7e10aeae4de309a95cec574ca4319b8b1b94a6
---

在大型工程中，Native调试的启动耗时较长。为提升开发调试效率，从26.0.0版本开始，新增Native调试启动加速功能。开启该功能后，首次调试完成时，调试服务器会保持活跃状态，后续再次启动调试时，可以大幅减少调试连接的耗时。

## 使用约束

* 该配置是工程级配置，每个工程需要单独开启。
* 同一个工程中，同时创建多个Native调试会话，该加速功能只对第一个调试会话有效。

## 操作步骤

在**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> Build, Execution, Deployment > Debugger > C++ Debugger**中，勾选**Keep LLDB client alive**开启Native调试启动加速功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/IbWieQZOTjGgnb7vmk2qMg/zh-cn_image_0000002808766573.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=9C5804BE53CAA22102E33BCC14E83B1F582432340CD5BA6C06512A6603E4B3CB)

也可以通过调试窗口控制台的超链接跳转到设置中开启。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/T_TYTwa0Q92JXOYVBieRLA/zh-cn_image_0000002779566992.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=BAADA4ADE31C17E603621F67675D03CE84E3276C78A4A13A15AF685465784C61)

开启开关并启动调试后，DevEco Studio底部会有调试服务器图标，调试过程中不能关闭服务器。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/--rhZ4D2TxWz-FtxyLp-Jw/zh-cn_image_0000002779407014.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=A4C67DAF1F650E7C6BFF82185F87C17B465FCB50E716CFC132960EE24726F294)

同时，开启开关后会占用内存和磁盘空间，在不调试时，可手动释放资源。

* 释放内存：点击DevEco Studio底部的调试服务器图标，关闭调试服务器释放内存。
* 释放磁盘空间：点击**File >** **Invalidate Caches**，勾选**Clear LLDB caches**，点击**Invalidate and Restart**重启DevEco Studio以清理缓存数据。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/iB27nBA3SjmfIVEU_NpAwQ/zh-cn_image_0000002808886653.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=B435EEF0C634DC167670667032677F863A6F9F5F029E9A99DE86D6D593DD5D1F)
