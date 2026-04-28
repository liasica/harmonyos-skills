---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-39
title: 安装HAP时提示“error: unlock screen failed in developer mode”
breadcrumb: FAQ > DevEco Studio > 应用调试 > 安装HAP时提示“error: unlock screen failed in developer mode”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:06+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:ba56bc93c1857eed2ced05d7ab59e48a4d78e37c4ddb32f26e35ea69aff1eaf1
---

**问题现象**

在启动调试或运行应用/服务时，如果安装HAP失败并显示“error: failed to start ability. error: unlock screen failed in developer mode”错误信息，表示在开发者模式下未能成功解锁屏幕。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/AoXr95aaTlCekv_l0SKdyg/zh-cn_image_0000002194317996.png?HW-CC-KV=V1&HW-CC-Date=20260428T003005Z&HW-CC-Expire=86400&HW-CC-Sign=4C5B65FD3B58C199461CE2C25550130534A3549E12F967F344A8C4825C59A6BA "点击放大")

**解决措施**

该问题的原因是在锁屏状态下，设备设置了锁屏密码，导致应用无法正常启动。

* 方法一：通过设置显示和亮度中的屏幕休眠选项，延长自动休眠时间。
* 方法二：应用开发时，可不设置锁屏密码。应用启动时，设备将自动亮屏并启动应用。
