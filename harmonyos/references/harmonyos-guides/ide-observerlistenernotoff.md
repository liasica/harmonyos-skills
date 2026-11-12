---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-observerlistenernotoff
title: ObserverListenerNotOff
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Scanner代码检查规则 > ArkTS代码检查规则 > ObserverListenerNotOff
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:00+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:866043a5d6406a2ca82ce780c7a613c5ec1862cbf4129125e4eec7c792fe29d4
---

[@ohos.telephony.observer](../doccenter-references/api/js-apis-observer.md)电话服务状态监听提供订阅管理功能，可订阅网络状态、信号状态、通话状态等变化事件，在.on()方法使用完毕后，需及时调用对应的.off()方法注销监听，避免导致内存泄漏。

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
          "ruleId": "ObserverListenerNotOff",
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
import { observer } from '@kit.TelephonyKit';
import Ability from '@ohos.app.ability.Ability';

/**
 * 正例：正确释放资源
 */
export class TestRelease extends Ability {
  private observerCB1 = (data: observer.NetworkState) => {
    console.info("on networkStateChange, data:" + JSON.stringify(data));
  }
  private observerCB2 = (data: observer.DataFlowType) => {
    console.info("on networkStateChange, data:" + JSON.stringify(data));
  }
  onCreate(): void {
    observer.on('networkStateChange', this.observerCB1);
    observer.on('cellularDataFlowChange', this.observerCB2);
  }
  onDestroy(): void {
    observer.off('networkStateChange', this.observerCB1);
    observer.off('cellularDataFlowChange', this.observerCB2);
  }
}
```

## 反例

```ts
import { observer } from '@kit.TelephonyKit';
import Ability from '@ohos.app.ability.Ability';

/**
 * 反例：未释放资源
 */
export class TestNotRelease extends Ability {
  private observerCB1 = (data: observer.NetworkState) => {
    console.info("on networkStateChange, data:" + JSON.stringify(data));
  }
  private observerCB2 = (data: observer.DataFlowType) => {
    console.info("on networkStateChange, data:" + JSON.stringify(data));
  }
  onCreate(): void {
    observer.on('networkStateChange', this.observerCB1); // leak
    observer.on('cellularDataFlowChange', this.observerCB2);
  }
  onDestroy(): void {
    observer.off('cellularDataFlowChange', this.observerCB2);
  }
}
```

Code Scanner代码检查规则的配置指导请参考[1.6.3 代码检查工具（codescanner）](ide-command-line-codescanner.md)
