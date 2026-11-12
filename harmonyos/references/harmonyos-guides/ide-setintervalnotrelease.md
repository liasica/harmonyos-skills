---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-setintervalnotrelease
title: SetIntervalNotRelease
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Scanner代码检查规则 > ArkTS代码检查规则 > SetIntervalNotRelease
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:00+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:5e9098bfb47d0f568292d07444ccfa1bc41046b6e845c0ab771bbd671598ec73
---

通过setInterval创建的定时器，使用完毕后，需及时调用clearInterval()释放，避免导致内存泄漏。

## 规则配置

```json
// rules.json
{
  "rules": {
    "arkts": {
      "ResourceLeak": [
        {
          "ruleId": "SetIntervalNotRelease",
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
import UIAbility from '@ohos.app.ability.UIAbility';

/**
 * 正例：正确释放资源
 */
export class TestRelease extends UIAbility {
  onCreate(): void {
    let intervalID = setInterval(() => {
      console.log('do every 1s');
    }, 1000);
    clearInterval(intervalID);
  }
}
```

## 反例

```ts
import UIAbility from '@ohos.app.ability.UIAbility';

/**
 * 反例：未释放资源
 */
export class TestNotRelease extends UIAbility {
  onCreate(): void {
    let intervalID = setInterval(() => { // leak
      console.log('do every 1s');
    }, 1000);
    clearInterval();
  }
  onDestroy(): void {
    let intervalID = setInterval(() => { // leak
      console.log('do every 1s');
    }, 1000);
  }
}
```

Code Scanner代码检查规则的配置指导请参考[1.6.3 代码检查工具（codescanner）](ide-command-line-codescanner.md)
