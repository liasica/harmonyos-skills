---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-displaynamespacelistenernotoff
title: DisplayNamespaceListenerNotOff
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Scanner代码检查规则 > ArkTS代码检查规则 > DisplayNamespaceListenerNotOff
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:00+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:068145bc6797041f3aceb3e7633c41aa33a58485af59cfd340227cd360735013
---

[@ohos.display (屏幕属性)](../doccenter-references/api/js-apis-display.md)提供管理显示设备的一些基础能力，在.on()方法使用完毕后，需及时调用对应的.off()方法注销监听，避免导致内存泄漏。

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
          "ruleId": "DisplayNamespaceListenerNotOff",
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
import { Callback } from '@kit.BasicServicesKit';
import display from '@ohos.display';
import Ability from '@ohos.app.ability.Ability';

/**
 * 正例：正确释放资源
 */
export class TestRelease extends Ability {
    private displayCallback: Callback<number> = (data: number) => {
        console.info(`Listening enabled. Data: ${data}`);
    };
    onCreate(): void {
        display.on('add', this.displayCallback);
        display.on('remove', this.displayCallback);
    }
    onDestroy(): void {
        display.off('add', this.displayCallback);
        display.off('remove', this.displayCallback);
    }
}
```

## 反例

```ts
import { Callback } from '@kit.BasicServicesKit';
import display from '@ohos.display';
import Ability from '@ohos.app.ability.Ability';

/**
 * 反例：未释放资源
 */
export class TestNotRelease extends Ability {
    private displayCallback: Callback<number> = (data: number) => {
        console.info(`Listening enabled. Data: ${data}`);
    };
    onCreate(): void {
        display.on('add', this.displayCallback); // leak
        display.on('remove', this.displayCallback); // leak
    }
}
```

Code Scanner代码检查规则的配置指导请参考[1.6.3 代码检查工具（codescanner）](ide-command-line-codescanner.md)
