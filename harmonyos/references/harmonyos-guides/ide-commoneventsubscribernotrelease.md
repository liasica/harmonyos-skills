---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-commoneventsubscribernotrelease
title: CommonEventSubscriberNotRelease
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Scanner代码检查规则 > ArkTS代码检查规则 > CommonEventSubscriberNotRelease
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:00+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:59cfd8052efbcb86b71a9297394192fb713e3f2a8ecf71b243a168e8029805a4
---

通过commonEventManager.subscribe()方法注册的CommonEventSubscriber对象，使用完毕后，需及时调用commonEventManager.unsubscribe()方法取消订阅并释放资源，避免导致内存泄漏。

## 规则配置

```json
// rules.json
{
  "rules": {
    "arkts": {
      "ResourceLeak": [
        {
          "ruleId": "CommonEventSubscriberNotRelease",
          "severity": "error",
          "skip": false
        }
      ]
    }
  }
}
```

## 正例

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { commonEventManager } from '@kit.BasicServicesKit';
import UIAbility from '@ohos.app.ability.UIAbility';
import { window } from '@kit.ArkUI';

/**
 * 正例：正确释放资源
 */
export default class TestRelease extends UIAbility {
  private subscriber: commonEventManager.CommonEventSubscriber | null = null;
  private subscribeInfo: commonEventManager.CommonEventSubscribeInfo = { events: ['event'] };
  onWindowStageCreate(windowStage: window.WindowStage): void {
    try {
      commonEventManager.createSubscriber(this.subscribeInfo,
        (err: BusinessError, commonEventSubscriber: commonEventManager.CommonEventSubscriber) => {
          if(!err) {
            console.info(`Succeeded in creating subscriber.`);
            this.subscriber = commonEventSubscriber;
            try {
              commonEventManager.subscribe(commonEventSubscriber, (err: BusinessError, data: commonEventManager.CommonEventData) => {
                if (err) {
                  console.error(`Failed to subscribe. Code is ${err.code}, message is ${err.message}`);
                  return;
                }
                console.info(`Succeeded in subscribing, data is ${JSON.stringify(data)}`);
              });
            } catch (error) {
              let err: BusinessError = error as BusinessError;
              console.error(`Failed to subscribe. Code is ${err.code}, message is ${err.message}`);
            }
            return;
          }
          console.error(`Failed to create subscriber. Code is ${err.code}, message is ${err.message}`);
        });
    } catch (error) {
      let err: BusinessError = error as BusinessError;
      console.error(`Failed to create subscriber. Code is ${err.code}, message is ${err.message}`);
    }
  }
  onWindowStageDestroy(): void {
    setTimeout(() => {
      try {
        commonEventManager.unsubscribe(this.subscriber, (err: BusinessError) => {
          if (err) {
            console.error(`Failed to unsubscribe. Code is ${err.code}, message is ${err.message}`);
            return;
          }
          // subscriber不再使用时需要将其置为null，避免内存泄露
          this.subscriber = null;
          console.info(`Succeeded in unsubscribing.`);
        });
      } catch (error) {
        let err: BusinessError = error as BusinessError;
        console.error(`Failed to unsubscribe. Code is ${err.code}, message is ${err.message}`);
      }
    }, 500);
  }
}
```

## 反例

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { commonEventManager } from '@kit.BasicServicesKit';
import UIAbility from '@ohos.app.ability.UIAbility';
import { window } from '@kit.ArkUI';

/**
 * 反例：未释放资源
 */
export class TestNotRelease extends UIAbility {
  private subscriber: commonEventManager.CommonEventSubscriber | null = null;
  private subscribeInfo: commonEventManager.CommonEventSubscribeInfo = { events: ['event'] };
  onWindowStageCreate(windowStage: window.WindowStage): void {
    try {
      commonEventManager.createSubscriber(this.subscribeInfo,
        (err: BusinessError, commonEventSubscriber: commonEventManager.CommonEventSubscriber) => {
          if(!err) {
            console.info(`Succeeded in creating subscriber.`);
            this.subscriber = commonEventSubscriber;
            try {
              commonEventManager.subscribe(commonEventSubscriber, (err: BusinessError, data: commonEventManager.CommonEventData) => {
                if (err) {
                  console.error(`Failed to subscribe. Code is ${err.code}, message is ${err.message}`);
                  return;
                }
                console.info(`Succeeded in subscribing, data is ${JSON.stringify(data)}`);
              });
            } catch (error) {
              let err: BusinessError = error as BusinessError;
              console.error(`Failed to subscribe. Code is ${err.code}, message is ${err.message}`);
            }
            return;
          }
          console.error(`Failed to create subscriber. Code is ${err.code}, message is ${err.message}`);
        });
    } catch (error) {
      let err: BusinessError = error as BusinessError;
      console.error(`Failed to create subscriber. Code is ${err.code}, message is ${err.message}`);
    }
  }
}
```

Code Scanner代码检查规则的配置指导请参考[1.6.3 代码检查工具（codescanner）](ide-command-line-codescanner.md)
