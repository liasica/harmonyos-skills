---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-eqeqeq
title: eqeqeq
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > eqeqeq
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:31+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:6768819dd934ca8e95e6a3b3ac8391da06781dcecbc04bf183200a8d1a0c5601
---

要求使用===和!==。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "eqeqeq": "error"
  }
}
```

## 选项

该规则无需配置额外选项。详情请参考[eslint/eqeqeq选项](https://eslint.nodejs.cn/docs/latest/rules/eqeqeq#选项)。

## 正例

```ts
export function test(a: string, b: string) {
  return a === b;
}
```

## 反例

```ts
export function test(a: string, b: string) {
  // Expected '===' and instead saw '=='.
  return a == b;
}
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
