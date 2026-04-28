---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-form-1
title: 点击服务卡片如何跳转至指定的页面
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 卡片开发（Form） > 点击服务卡片如何跳转至指定的页面
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:57+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:ed8c19fe1395d439d638799f50f4c05d4ba4390c508a9851d9f01471318540e7
---

配置卡片事件，指定目标UIAbility进行跳转。

* 如果应用不在后台，可以在目标UIAbility的onWindowStageCreate()中调用loadContent加载指定的页面。
* 如果应用已在后台，可在目标UIAbility的onNewWant()中调用loadContent加载指定页面。

**参考链接**

[启动UIAbility的指定页面](../harmonyos-guides/uiability-intra-device-interaction.md#启动uiability的指定页面)
