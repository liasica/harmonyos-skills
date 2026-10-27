---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-profiler-1
title: Profiler分析任务录制失败
breadcrumb: FAQ > DevEco Studio > 性能分析 > Profiler分析任务录制失败
category: harmonyos-faqs
scraped_at: 2026-10-28T07:49:00+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:868a5ce2595b8b03b84faa1593343bcf32de611bee94f1073cfba60b1163e130
---

**问题现象**

单击Profiler深度分析任务的启动录制按钮后，录制失败。

* DevEco Studio提示任务启动或录制失败。

* Session列表中任务显示异常图标。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/vFU7L0ciQzqDZhR3Snb7hg/zh-cn_image_0000002624638714.png)

**解决措施**

启动深度分析任务录制后，将经历初始化、录制和停止录制后分析及组装数据三个阶段。每个阶段都可能遇到任务录制失败的问题，具体原因包括连接断开、插件错误和设备状态异常。

请参考以下步骤进行操作。

1. 确保设备亮屏运行。

2. 尝试重新推送包到设备，或者重启应用和服务。
3. 重启设备。
4. 重启DevEco Studio。
