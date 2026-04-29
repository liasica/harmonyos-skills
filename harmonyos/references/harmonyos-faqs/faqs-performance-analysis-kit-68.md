---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-68
title: 安装VPN软件astrill后hdc访问不了设备
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 安装VPN软件astrill后hdc访问不了设备
category: harmonyos-faqs
scraped_at: 2026-04-29T14:14:38+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:d2b10569f97f33e7ca211236ef63debdea72684ccd13ddabcf95bcfca9f5db45
---

**问题现象**

hdc访问不了设备。hdc list targets -v出现unknown状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/lHPZgNnTTaevNg_Q6C5Pgg/zh-cn_image_0000002474863621.png?HW-CC-KV=V1&HW-CC-Date=20260429T061437Z&HW-CC-Expire=86400&HW-CC-Sign=B6F41C01523470339E13FADEFD2ABAB46E8C273F7D61CF09FBD304D226B6BD66)

查看hdc.log日志

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/d4r8fZ6YSg2pWsMGZtDIbw/zh-cn_image_0000002474943789.png?HW-CC-KV=V1&HW-CC-Date=20260429T061437Z&HW-CC-Expire=86400&HW-CC-Sign=C48C823CCBC75B4CCF6E16FD615B502DE99A6600FEC103C14EEAA77AC776C485)

**可能原因**

系统兼容问题。在win10上安装vpn工具astrill后，会导致出现这样问题。

**解决措施**

* 当前版本hdc建议卸载掉vpn软件，注意不是停掉vpn，而是卸载vpn。
* 参考[hdc版本配套表](../harmonyos-guides/hdc.md#hdc版本配套表)升级最新版本后重试。
