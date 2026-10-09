---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-no-high-loaded-frame-rate-range
title: "@performance/no-high-loaded-frame-rate-range"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/no-high-loaded-frame-rate-range
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:32+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:9126e8ccc18953f2fb0b26b6a125e9b5eeb47f5bc711438ce36e0f3ae919a5bc
---

不允许锁定最高帧率运行。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@performance/no-high-loaded-frame-rate-range": "warn",
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```ts
import { displaySync } from '@kit.ArkGraphics2D';
let sync = displaySync.create();
sync.setExpectedFrameRateRange({
  expected: 60,
  min: 45,
  max: 60,
});
```

## 反例

```ts
import { displaySync } from '@kit.ArkGraphics2D';
let sync = displaySync.create();
sync.setExpectedFrameRateRange({
  expected: 120,
  min: 120,
  max: 120,
});
```

## 规则集

```screen
plugin:@performance/all
plugin:@performance/recommended
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
