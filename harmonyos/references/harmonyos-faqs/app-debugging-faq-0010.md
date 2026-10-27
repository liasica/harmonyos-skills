---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/app-debugging-faq-0010
title: DevEco Studio安装HAP报错unlock screen failed问题排查
breadcrumb: FAQ > DevEco Studio > 应用调试 > 常见问题 > DevEco Studio安装HAP报错unlock screen failed问题排查
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:59+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:fbf6f7a897f06e0e796f99875b183e2efd506a8dd3ac89f9b5a88fbab397ac12
---

**Q：在启动调试或运行应用/服务时，如果安装HAP失败并显示“error: failed to start ability. error: unlock screen failed in developer mode”错误信息，表示在开发者模式下未能成功解锁屏幕，该如何解决？**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/7_wkGEnZR7amh1v7RcPsDg/zh-cn_image_0000002773062660.png "点击放大")

**A**：该问题的原因是在锁屏状态下，设备设置了锁屏密码，导致应用无法正常启动。

* 方法一：通过设置显示和亮度中的屏幕休眠选项，延长自动休眠时间。
* 方法二：应用开发时，可不设置锁屏密码。应用启动时，设备将自动亮屏并启动应用。
