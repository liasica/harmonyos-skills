---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-profiler-1
title: Profiler分析任务录制失败
breadcrumb: FAQ > DevEco Studio > 性能分析 > Profiler分析任务录制失败
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:28+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:8d727438157f83b793c7a23201512fbe6eaaaa96d6f0813da66324e336f81558
---

**问题现象**

单击Profiler深度分析任务的启动录制按钮后，录制失败。

* DevEco Studio提示任务启动或录制失败。

* Session列表中任务显示异常图标。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/MsswAGj1Q8itdVWWrkO5vQ/zh-cn_image_0000002194318540.png)

**解决措施**

启动深度分析任务录制后，将经历初始化、录制和停止录制后分析及组装数据三个阶段。每个阶段都可能遇到任务录制失败的问题，具体原因包括连接断开、插件错误和设备状态异常。

请参考以下步骤进行操作。

1. 确保设备亮屏运行。

2. 尝试重新推送包到设备，或者重启应用和服务。
3. 重启设备。
4. 重启DevEco Studio。
