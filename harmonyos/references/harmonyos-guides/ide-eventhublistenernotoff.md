---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-eventhublistenernotoff
title: EventHubListenerNotOff
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Scanner代码检查规则 > ArkTS代码检查规则 > EventHubListenerNotOff
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:00+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:496db03c5b3f3dbbbadbcad841a1a774657d1e87a72496631d99bf9bcfd18c68
---

[EventHub](../doccenter-references/api/js-apis-inner-application-eventhub.md)是基于发布-订阅模式的事件通信机制，主要用于UIAbility组件与UI的数据通信，在.on()方法使用完毕后，需及时调用对应的.off()方法注销监听，避免导致内存泄漏。

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
          "ruleId": "EventHubListenerNotOff",
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

/**
 * 正例：正确释放资源
 */
@Component
struct TestRelease {
  eventFunc1() {
    console.info('eventFunc1 is called');
  }
  eventFunc2() {
    console.info('eventFunc2 is called');
  }
  eventFunc3() {
    console.info('eventFunc3 is called');
  }
  aboutToAppear() {
    getContext(this).eventHub.on('myEvent1', this.eventFunc1);
    this.getUIContext().getHostContext()?.eventHub.on('myEvent2', this.eventFunc2);
    this.getUIContext().getHostContext()?.eventHub.on('myEvent3', this.eventFunc3);
  }
  build() {
    Text('EventHubComponent')
  }
  aboutToDisappear() {
    getContext(this).eventHub.off('myEvent1', this.eventFunc1);
    this.getUIContext().getHostContext()?.eventHub.off('myEvent2', this.eventFunc2);
    getContext(this).eventHub.off('myEvent3');
  }
}
```

## 反例

```ts
import { Callback, emitter } from '@kit.BasicServicesKit';
import UIAbility from '@ohos.app.ability.UIAbility';

/**
 * 反例：未释放资源
 */
@Component
struct TestNotRelease {
  eventFunc1() {
    console.info('eventFunc1 is called');
  }
  eventFunc2() {
    console.info('eventFunc2 is called');
  }
  eventFunc3() {
    console.info('eventFunc3 is called');
  }
  aboutToAppear() {
    getContext(this).eventHub.on('myEvent1', this.eventFunc1); // leak
    this.getUIContext().getHostContext()?.eventHub.on('myEvent2', this.eventFunc2); // leak
    this.getUIContext().getHostContext()?.eventHub.on('myEvent3', this.eventFunc3); // leak
  }
  build() {
    Text('EventHubComponent')
  }
}
```

Code Scanner代码检查规则的配置指导请参考[1.6.3 代码检查工具（codescanner）](ide-command-line-codescanner.md)
