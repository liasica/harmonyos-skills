---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-5
title: HarmonyOS应用自动化签名时提示“Unsupported restricted ACL permission exist in the configuration”
breadcrumb: FAQ > DevEco Studio > 应用调试 > HarmonyOS应用自动化签名时提示“Unsupported restricted ACL permission exist in the configuration”
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:74b48141dc7f42703ea5d6592a765841cc9ce2210fd157eaaeb073169ea57d5e
---

**问题现象**

在对HarmonyOS应用工程中，勾选“Automatically generate signature”时，提示“Unsupported restricted ACL permission exist in the configuration”报错信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/sRGTYWYTSdaT9FtzoGQe7w/zh-cn_image_0000002624478778.png?HW-CC-KV=V1&HW-CC-Date=20261112T233144Z&HW-CC-Expire=31536000000&HW-CC-Sign=BDB0E84550CCB5EE9A6AF6F8464B7682F07411519BB742323AC3BFEAB46796C5)

**解决措施**

出现该问题的原因是当前DevEco Studio自动签名只支持部分的ACL权限，当前工程中使用了不在支持范围之内的ACL权限，建议尝试手动签名。

**参考链接**

[自动签名支持的ACL权限](../harmonyos-guides/ide-signing.md#section5301916183411)

[手动签名](../harmonyos-guides/ide-signing.md#section297715173233)
