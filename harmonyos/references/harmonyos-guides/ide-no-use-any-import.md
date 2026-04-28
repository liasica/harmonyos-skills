---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-no-use-any-import
title: @performance/no-use-any-import
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/no-use-any-import
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:15+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:844118f5927af050487666813738491c4bd6cd085512ae0956b5411babafd044
---

使用import的方式引入对应的模块时，建议按需引用使用到的变量代替“import \*”的方式，以减少.ets文件的执行耗时和文件中所有export变量的初始化过程。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/no-use-any-import": "warn",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. // Index.ets
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { One } from '../utils/Numbers'; // It is recommended to reference variables on demand
4. hilog.info(0x0000, 'testTag', '%{public}d', One); // Only the variable One is used here
5. // Numbers.ets
6. export const One: number = 1;
7. export const Two: number = 2;
```

## 反例

```
1. // Index.ets
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import * as nm from '../utils/Numbers'; // The import * method is not recommended
4. hilog.info(0x0000, 'testTag', '%{public}d', nm.One); // Only the variable One is used here
5. // Numbers.ets
6. export const One: number = 1;
7. export const Two: number = 2;
```

## 规则集

```
1. plugin:@performance/recommended
2. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
