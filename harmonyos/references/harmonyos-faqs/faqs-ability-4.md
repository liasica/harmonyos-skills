---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-4
title: 如何在UIAbility调用terminateSelf()后设置不保留最近任务列表中的快照
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 如何在UIAbility调用terminateSelf()后设置不保留最近任务列表中的快照
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:32+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:bcf6710d5120afe00d44831200b16c44881a7f1719904ac7f0333db86109238b
---

在HarmonyOS应用开发中，UIAbilityContext的[terminateSelf()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#terminateself-1)方法被用来结束当前的UIAbility实例。

如果希望在调用terminateSelf()后，让应用在最近任务列表中不保留快照，可以通过在[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)中配置removeMissionAfterTerminate为true来实现。

```json
{
  "module": {
    // ...
    "abilities": [
      {
        // ...
        "removeMissionAfterTerminate": true,
      }
    ],
    // ...
  }
}
```

**说明** 

* removeMissionAfterTerminate字段的默认值为false，表示默认情况下应用会在最近任务列表中保留快照。

* 仅当removeMissionAfterTerminate设置为true时，调用terminateSelf()后应用不会在最近任务列表中保留快照。
