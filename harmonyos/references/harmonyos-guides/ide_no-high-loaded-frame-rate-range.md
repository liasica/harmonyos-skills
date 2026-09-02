---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-high-loaded-frame-rate-range
title: "@performance/no-high-loaded-frame-rate-range"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/no-high-loaded-frame-rate-range
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:dce0f99362cc3459d44806213bbd1ea859ab60e1e042fc7ff70edc10db5f864f
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

```screen
import { displaySync } from '@kit.ArkGraphics2D';
let sync = displaySync.create();
sync.setExpectedFrameRateRange({
  expected: 60,
  min: 45,
  max: 60,
});
```

## 反例

```screen
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
