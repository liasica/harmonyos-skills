---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-no-use-any-import
title: "@performance/no-use-any-import"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/no-use-any-import
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a0947f4f5a49538f6ba1cfd1cba4348619d3321cf658ab026585cf8557b9b570
---

使用import的方式引入对应的模块时，建议按需引用变量代替“import \*”的方式，以减少.ets文件的执行耗时和文件中所有export变量的初始化过程。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@performance/no-use-any-import": "warn",
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
// Index.ets
import { hilog } from '@kit.PerformanceAnalysisKit';
import { One } from '../utils/Numbers'; // It is recommended to reference variables on demand
hilog.info(0x0000, 'testTag', '%{public}d', One); // Only the variable One is used here
// Numbers.ets
export const One: number = 1;
export const Two: number = 2;
```

## 反例

```screen
// Index.ets
import { hilog } from '@kit.PerformanceAnalysisKit';
import * as nm from '../utils/Numbers'; // The import * method is not recommended
hilog.info(0x0000, 'testTag', '%{public}d', nm.One); // Only the variable One is used here
// Numbers.ets
export const One: number = 1;
export const Two: number = 2;
```

## 规则集

```screen
plugin:@performance/recommended
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
