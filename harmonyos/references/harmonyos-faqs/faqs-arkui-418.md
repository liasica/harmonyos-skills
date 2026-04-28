---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-418
title: 使用Navigation，页面从A->B->C->D，D直接调用popToName到A，不会触发B、C的onPop是什么原因
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 使用Navigation，页面从A->B->C->D，D直接调用popToName到A，不会触发B、C的onPop是什么原因
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:50+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:f1f46123e10bddbf813f495935e4b7163b770213447e00fc922d6d97ec6341ab
---

**问题描述**

页面从A->B->C->D，D直接调用popToName到A，会不会触发B、C的onPop。

**解决措施**

* 仅按push的反序返回时会触发onPop。以A->B->C->D为例，仅如下的pop操作会触发对应页面的onPop回调：D->C，C->B，B->A，popToName属于跨级返回，会跳过中间页面栈而不触发其生命周期回调，这与逐级pop的机制不同。
* 自API15起，推荐开发者使用[onResult](../harmonyos-references/ts-basic-components-navdestination.md#onresult15)处理返回场景的路由参数。
