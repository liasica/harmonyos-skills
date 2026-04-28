---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-5
title: HarmonyOS应用自动化签名时提示“Unsupported restricted ACL permission exist in the configuration”
breadcrumb: FAQ > DevEco Studio > 应用调试 > HarmonyOS应用自动化签名时提示“Unsupported restricted ACL permission exist in the configuration”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:05+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:51609ac7b719c2c0160c1a5b4baa3fa0bddb35fa7cccc4189a8013e96581ea75
---

**问题现象**

在对HarmonyOS应用工程中，勾选“Automatically generate signature”时，提示“Unsupported restricted ACL permission exist in the configuration”报错信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/xYnhr2ggQFO_FOE9gqW5Fw/zh-cn_image_0000002250504069.png?HW-CC-KV=V1&HW-CC-Date=20260428T003004Z&HW-CC-Expire=86400&HW-CC-Sign=8721F3F42C4D1B4BFB050150F703C4C6B382AACE36DD519E531A843AE930759D)

**解决措施**

出现该问题的原因是当前DevEco Studio自动签名只支持部分的ACL权限，当前工程中使用了不在支持范围之内的ACL权限，建议尝试手动签名。

**参考链接**

[自动签名支持的ACL权限](../harmonyos-guides/ide-signing.md#section5301916183411)

[手动签名](../harmonyos-guides/ide-signing.md#section297715173233)
