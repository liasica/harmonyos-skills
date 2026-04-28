---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-9
title: 文件分享能否使用Want配置打开具体应用，而不是显示选择窗口
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 文件分享能否使用Want配置打开具体应用，而不是显示选择窗口
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:22+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:470df485be8e42bd208b6b96b503d56fa44bdf5ea8b1e3dd542311d6585f0504
---

目前不支持使用Want配置打开具体应用。当前拉起的打开方式是通过设备内应用配置action: "ohos.want.action.sendData"来识别的，不能由业务自行指定。

**参考链接**

[应用文件分享](../harmonyos-guides/share-app-file.md)
