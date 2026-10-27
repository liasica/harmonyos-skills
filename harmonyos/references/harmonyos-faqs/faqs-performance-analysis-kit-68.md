---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-68
title: 安装VPN软件astrill后hdc访问不了设备
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 安装VPN软件astrill后hdc访问不了设备
category: harmonyos-faqs
scraped_at: 2026-10-28T07:46:45+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:0d79096001a77db7ed07091e0ccc198f3caa396e1fbed9632ba2428e58425c4a
---

**问题现象**

hdc访问不了设备。hdc list targets -v出现unknown状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/xZewRLYbQ_SFU2zl3-8YqQ/zh-cn_image_0000002624476474.png)

查看hdc.log日志

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/6AKBI2KNQDy2N-zOY5rxEA/zh-cn_image_0000002654795835.png)

**可能原因**

系统兼容问题。在win10上安装vpn工具astrill后，会导致出现这样问题。

**解决措施**

* 当前版本hdc建议卸载掉vpn软件，注意不是停掉vpn，而是卸载vpn。
* 参考[hdc版本配套表](../harmonyos-guides/hdc.md#hdc版本配套表)升级最新版本后重试。
