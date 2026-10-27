---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-5
title: HarmonyOS应用自动化签名时提示“Unsupported restricted ACL permission exist in the configuration”
breadcrumb: FAQ > DevEco Studio > 应用调试 > HarmonyOS应用自动化签名时提示“Unsupported restricted ACL permission exist in the configuration”
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:59+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:488a887ad566e5b92db44593700b245b86f5a17a249f7e2dad456218187bf396
---

**问题现象**

在对HarmonyOS应用工程中，勾选“Automatically generate signature”时，提示“Unsupported restricted ACL permission exist in the configuration”报错信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/YWGWCUNOS5Ocbe0cVeg3oA/zh-cn_image_0000002624478778.png)

**解决措施**

出现该问题的原因是当前DevEco Studio自动签名只支持部分的ACL权限，当前工程中使用了不在支持范围之内的ACL权限，建议尝试手动签名。

**参考链接**

[自动签名支持的ACL权限](../harmonyos-guides/ide-signing.md#section5301916183411)

[手动签名](../harmonyos-guides/ide-signing.md#section297715173233)
