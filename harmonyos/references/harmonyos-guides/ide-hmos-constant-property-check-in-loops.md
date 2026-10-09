---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-constant-property-check-in-loops
title: "@performance/constant-property-referencing-check-in-loops"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/constant-property-referencing-check-in-loops
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:31+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:463b27e24dbfaacdb1cc6c646c157f9c0d9039326744c3ea8878f4d93f345a05
---

在循环如需频繁访问某个常量，且该属性引用常量在循环中不会改变，建议提取到循环外部，减少属性访问的次数。

根据[ArkTS高性能编程实践](arkts-high-performance-programming.md)，建议修改。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@performance/constant-property-referencing-check-in-loops": "suggestion",
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```ts
class Time {
  static start: number = 0;
  static info: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];
}
function getNum(num: number): number {
  /* Year has (12 * 29 =) 348 days at least */
  let total: number = 348;
  const info = Time.info[num- Time.start];  
  for (let index: number = 0x8000; index > 0x8; index >>= 1) {
    if ((info & index) != 0) {
      total++;
    }
  }
  return total;
}
```

## 反例

```ts
class Time {
  static start: number = 0;
  static info: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];
}
function getNum(num: number): number {
  /* Year has (12 * 29 =) 348 days at least */
  let total: number = 348;
  for (let index: number = 0x8000; index > 0x8; index >>= 1) {
    // warning
    total += ((Time.info[num - Time.start] & index) !== 0) ? 1 : 0;
  }
  return total;
}
```

## 规则集

```json
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
