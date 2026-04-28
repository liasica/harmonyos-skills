---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-76
title: 在使用UIAbilityContext时报401“The context must be a valid Context”的Context类型错误
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 在使用UIAbilityContext时报401“The context must be a valid Context”的Context类型错误
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:48+08:00
doc_updated_at: 2026-03-25
content_hash: sha256:3228f8822c93fe3013de886196ca64a3029d67077869df929cb3c5b7af984700
---

401错误表示提供的上下文类型不正确，需要使用UIAbility的上下文。获取[UIAbilityContext](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md)的方式如下：

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

3. export default class EntryAbility extends UIAbility {
4. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
5. let uiAbilityContext = this.context;
6. // ...
7. }
8. }
```

[GetUIAbilityContext.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/AbilityKit/entry/src/main/ets/pages/GetUIAbilityContext.ets#L21-L28)

**参考链接**

[应用上下文Context](../harmonyos-guides/application-context-stage.md)
