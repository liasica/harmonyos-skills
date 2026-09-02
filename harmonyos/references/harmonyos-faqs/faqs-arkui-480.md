---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-480
title: 如何实现护眼模式
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现护眼模式
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:28+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:62409403e8a20cd2e372be3e9a68644f2d99037228ab1c8ae2813a80dbb2efdf
---

**解决措施**

当前实现护眼模式可以采用下面两种方式：

方案一：可通过深色模式的方式，进行应用适配；深色模式的开发可以参考：[深色模式适配](../best-practices/bpta-dark-mode-adaptation.md)。

方案二：可通过系统设置全局开启护眼模式，通过应用内指引用户跳转设置页面手动打开护眼模式。

```typescript
import { common } from "@kit.AbilityKit";
import { BusinessError } from "@kit.BasicServicesKit";

@Entry
@Component
export struct ImplementEyeProtectionMode {
  build() {
    Row() {
      Button('跳转显示设置页面')
        .onClick(() => {
          let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
          context.startAbility({
            bundleName: 'com.huawei.hmos.settings',
            abilityName: 'com.huawei.hmos.settings.MainAbility',
            uri: 'display_settings'
          }).catch((err: BusinessError) => {
            console.error(`startAbility failed, code is ${err.code}, message is ${err.message}`);
          })
        })
    }
    .width('100%')
    .height('100%')
    .alignItems(VerticalAlign.Center)
    .justifyContent(FlexAlign.Center)
  }
}
```
