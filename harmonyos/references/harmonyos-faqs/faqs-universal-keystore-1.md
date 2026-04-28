---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-universal-keystore-1
title: HUKS生成的密钥在什么情况下会消失或被清理
breadcrumb: FAQ > 系统开发 > 安全 > 密钥管理（Universal Keystore） > HUKS生成的密钥在什么情况下会消失或被清理
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:01+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:6bb3083ad9f5dc6b6c893b563c0e4203318514dd0873483126bcb18ed0ac671b
---

应用中调用 `huks.deleteKeyItem` 接口可以删除指定别名的密钥。应用卸载后，存储在设备安全环境中的密钥将自动销毁。

**参考链接**

[huks.deleteKeyItem](../harmonyos-references/js-apis-huks.md#huksdeletekeyitem9)
