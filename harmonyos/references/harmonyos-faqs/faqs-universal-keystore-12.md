---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-universal-keystore-12
title: huks.isKeyItemExist和huks.hasKeyItem的区别
breadcrumb: FAQ > 系统开发 > 安全 > 密钥管理（Universal Keystore） > huks.isKeyItemExist和huks.hasKeyItem的区别
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:03+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:fbd3f6ee5f3bb8d0d21a12af1883fdc67b06e6ee7b959e73eb5eab0a0b0baed2
---

[huks.isKeyItemExist](../harmonyos-references/js-apis-huks.md#huksiskeyitemexist9)：若密钥存在，data为true，若密钥不存在，则error中会输出密钥不存在的error code。开发者需要通过错误码判断密钥不存在，不符合逻辑习惯。建议使用hasKeyItem接口。

[huks.hasKeyItem](../harmonyos-references/js-apis-huks.md#hukshaskeyitem11)：若密钥存在，返回值为true，若密钥不存在，返回值为false。
