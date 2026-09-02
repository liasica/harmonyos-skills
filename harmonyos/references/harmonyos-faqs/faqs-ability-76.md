---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-76
title: 在使用UIAbilityContext时报401“The context must be a valid Context”的Context类型错误
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 在使用UIAbilityContext时报401“The context must be a valid Context”的Context类型错误
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d3c8311470b6991e9b3edf8044feefe33e426e302f9bc941590289bbf85afa6f
---

401错误表示提供的上下文类型不正确，需要使用UIAbility的上下文。获取[UIAbilityContext](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md)的方式如下：

```typescript
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    let uiAbilityContext = this.context;
    // ...
  }
}
```

**参考链接**

[应用上下文Context](../harmonyos-guides/application-context-stage.md)
