---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-99
title: 如何判断App的启动来源
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 如何判断App的启动来源
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:bdc846e696b52bcd060327ccc0c94fb287f9ebb9aa5a3de7a00d77bb670146cf
---

通过startAbility()启动应用时，want参数中的parameters属性可以携带拉起方的信息。系统在parameters中提供了一些预置的key，例如，可以通过ohos.aafwk.param.callerBundleName获取拉起方的BundleName。

示例如下：

拉起端：

```typescript
import { common, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index {
  context = this.getUIContext();

  build() {
    Row() {
      Column() {
        Button('open app')
          .onClick(() => {
            let want: Want = {
              action: 'ohos.want.action.viewData',
              entities: ['entity.system.home']
            }
            let context = this.context.getHostContext() as common.UIAbilityContext;
            context.startAbility(want, (err: BusinessError) => {
              if (err.code) {
                // 处理业务逻辑错误
                hilog.error(0x0000, 'testTag', `startAbility failed, code is ${err.code}, message is ${err.message}`);
                return;
              }
              // 执行正常业务
              hilog.info(0x0000, 'testTag', 'startAbility succeed');
            });
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

接收端：

```typescript
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(0x0000, 'testTag', `app resource is:${want.parameters?.['ohos.aafwk.param.callerBundleName']}`);
    // ...
  }

  // ...
}
```

**参考链接**

[Want](../harmonyos-references/js-apis-app-ability-want.md#want)
