---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-emitterlistenernotoff
title: EmitterListenerNotOff
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Scanner代码检查规则 > ArkTS代码检查规则 > EmitterListenerNotOff
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:00+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:4132deb92ca171e19357ef661cc3b5e7cd7d23da2fd3bc77a92f3b0dd3086fc1
---

[@ohos.events.emitter (Emitter)](../doccenter-references/api/js-apis-emitter.md)提供同一进程不同线程间或同一线程内发送和处理事件的能力，在.on()方法使用完毕后，需及时调用对应的.off()方法注销监听，避免导致内存泄漏。

**说明** 

调用.on()监听接口后，只要存在对应的.off()调用（即取消全部或部分监听），不产生告警；仅当代码中不存在任何.off()调用时，才产生告警。

## 规则配置

```json
// rules.json
{
  "rules": {
    "arkts": {
      "ResourceLeak": [
        {
          "ruleId": "EmitterListenerNotOff",
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
import { Callback, emitter } from '@kit.BasicServicesKit';
import UIAbility from '@ohos.app.ability.UIAbility';
@Sendable
class Sample {
  constructor() {
    this.count = 100;
  }
  printCount() {
    console.info('Print count : ' + this.count);
  }
  count: number;
}

/**
 * 正例：正确释放资源
 */
export default class TestRelease extends UIAbility {
  private eventIdInstanceField = 'eventIdInstanceField';
  private emitterIdCallBack: Callback<emitter.GenericEventData<Sample>> = (eventData: emitter.GenericEventData<Sample>): void => {
    console.info(`eventData: ${JSON.stringify(eventData?.data)}`);
    if (eventData?.data instanceof Sample) {
      eventData?.data?.printCount();
    }
  }
  onCreate(): void {
    emitter.on(this.eventIdInstanceField, this.emitterIdCallBack);
    emitter.on({ eventId: 2 }, () => {});
    this.registerWithId('eventIdParam');
  }
  onDestroy(): void {
    emitter.off(this.eventIdInstanceField, this.emitterIdCallBack);
    emitter.off(2);
    this.unregisterWithId('eventIdParam');
  }
  registerWithId(eventId: string) {
    emitter.on(eventId, this.emitterIdCallBack);
  }
  unregisterWithId(eventId: string) {
    emitter.off(eventId, this.emitterIdCallBack);
  }
}
```

## 反例

```ts
import { Callback, emitter } from '@kit.BasicServicesKit';
import UIAbility from '@ohos.app.ability.UIAbility';
@Sendable
class Sample {
  constructor() {
    this.count = 100;
  }
  printCount() {
    console.info('Print count : ' + this.count);
  }
  count: number;
}

/**
 * 反例：未释放资源
 */
export class TestNotRelease extends UIAbility {
  private eventIdInstanceField = 'eventIdInstanceField';
  private emitterIdCallBack: Callback<emitter.GenericEventData<Sample>> = (eventData: emitter.GenericEventData<Sample>): void => {
    console.info(`eventData: ${JSON.stringify(eventData?.data)}`);
    if (eventData?.data instanceof Sample) {
      eventData?.data?.printCount();
    }
  }
  onCreate(): void {
    emitter.on(this.eventIdInstanceField, this.emitterIdCallBack); // leak
    emitter.on({ eventId: 4 }, () => {}); // leak
    this.registerWithId('eventIdParam');
  }
  registerWithId(eventId: string) {
    emitter.on(eventId, this.emitterIdCallBack); // leak
  }
  unregisterWithId(eventId: string) {
    emitter.off(eventId, this.emitterIdCallBack);
  }
}
```

Code Scanner代码检查规则的配置指导请参考[1.6.3 代码检查工具（codescanner）](ide-command-line-codescanner.md)
