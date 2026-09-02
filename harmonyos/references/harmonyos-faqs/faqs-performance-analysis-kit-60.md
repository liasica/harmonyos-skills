---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-60
title: 如何使用ErrorManager捕获异常
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 如何使用ErrorManager捕获异常
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:96e03253508c91bc5f82e17ee26392cfce3fee6fea31c87a9c23537bf12678db
---

ErrorManager提供错误观察器的注册和注销。

异常监听（ErrorObserver）接口功能介绍：

| 接口名称 | 说明 |
| --- | --- |
| onUnhandledException(errMsg: string): void | 系统回调接口，应用注册后，当应用产生未捕获的异常时的回调。 |
| onException?(errObject: Error): void | 系统回调接口，应用注册后，当应用产生异常上报JS层时的回调。 |

捕获异常代码参考：

Index.ets中：

```typescript
@Entry
@Component
struct ErrorManagerPage {
  @State message: string = 'Capture exceptions';

  build() {
    Row() {
      Column() {
        Button(this.message)
          .onClick(() => {
            let tempList = ['0', '1'];
            tempList[5].toString();
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

EntryAbility.ets中：

```typescript
import { AbilityConstant, errorManager, UIAbility, Want } from '@kit.AbilityKit';
import { ConfigurationConstant } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';

let callback: errorManager.ErrorObserver = {
  onUnhandledException: (errMsg) => {
    console.log('Callback when an uncaught exception occurs,onUnhandledException:', errMsg);
  },
  onException: (errorObj) => {
    console.log('The callback when an exception is reported to the JS layer,onException');
    console.log('onException, name: ', errorObj.name);
    console.log('onException, message: ', errorObj.message);
    if (typeof (errorObj.stack) === 'string') {
      console.log('onException, stack: ', errorObj.stack);
    }
  }
}

let abilityWant: Want;
let registerId = -1;
const DOMAIN = 0x0000;

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    try {
      this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
      console.log('[Demo] EntryAbility onCreate');
      registerId = errorManager.on('error', callback);
      abilityWant = want;
      console.log('registerId:', registerId);
    } catch (err) {
      hilog.error(DOMAIN, 'testTag', `setColorMode failed, code is ${err.code}, message is ${err.message}`);
    }
  }

  onDestroy(): void {
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
    console.log('[Demo] EntryAbility onDestroy');
    errorManager.off('error', registerId, (result) => {
      console.log(`[Demo] result:${result}`);
    });
  }

  // ...
}
```

**参考链接**

[@ohos.app.ability.errorManager](../harmonyos-references/js-apis-app-ability-errormanager.md)
