---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-5
title: HarmonyOS应用自动化签名时提示“Unsupported restricted ACL permission exist in the configuration”
breadcrumb: FAQ > DevEco Studio > 应用调试 > HarmonyOS应用自动化签名时提示“Unsupported restricted ACL permission exist in the configuration”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:22+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:5a461130e6a0042341ff2c0f3fff5e4c5ed53db302ffd13c18dfdc570ea79e20
---

**问题现象**

在对HarmonyOS应用工程中，勾选“Automatically generate signature”时，提示“Unsupported restricted ACL permission exist in the configuration”报错信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/xYnhr2ggQFO_FOE9gqW5Fw/zh-cn_image_0000002250504069.png?HW-CC-KV=V1&HW-CC-Date=20260429T062121Z&HW-CC-Expire=86400&HW-CC-Sign=3F960E7CFEC77B3E294D4968E4C5AEDB627F755D8C9D456CFB49D7DF71708643)

**解决措施**

出现该问题的原因是当前DevEco Studio自动签名只支持部分的ACL权限，当前工程中使用了不在支持范围之内的ACL权限，建议尝试手动签名。

**参考链接**

[自动签名支持的ACL权限](../harmonyos-guides/ide-signing.md#section5301916183411)

[手动签名](../harmonyos-guides/ide-signing.md#section297715173233)
