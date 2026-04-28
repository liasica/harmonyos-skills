---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-259
title: 为什么vp2px、px2vp返回的结果不正确
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 为什么vp2px、px2vp返回的结果不正确
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:05+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:ac7dbceb53be73d6600bae15b4f32894d82a9ef4d4836bbcea65e13d49b065d7
---

1. [vp2px](../harmonyos-references/arkts-apis-uicontext-uicontext.md#vp2px12)、[px2vp](../harmonyos-references/arkts-apis-uicontext-uicontext.md#px2vp12)是ArkUI的全局接口，该接口已被标记为废弃，不推荐使用。在应用启动阶段或非UI线程调用时，UI实例不明确，使用默认屏幕的虚拟像素比进行转换，可能导致转换后结果与预期不一致的情况。
2. UIContext的[vp2px](../harmonyos-references/arkts-apis-uicontext-uicontext.md#vp2px12)、[px2vp](../harmonyos-references/arkts-apis-uicontext-uicontext.md#px2vp12)为推荐的替代接口，能保证调用时UI实例已经创建，并返回正确的结果。

**参考链接**

[像素单位](../harmonyos-references/ts-pixel-units.md)
