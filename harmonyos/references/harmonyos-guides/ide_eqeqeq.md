---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_eqeqeq
title: eqeqeq
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > eqeqeq
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:56+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:e7d8a6fba3bc1b683bd8df8cb60b1ddec5693b88b001f4d27b9c39b9ffcf7dd1
---

要求使用===和!==。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "eqeqeq": "error"
  }
}
```

## 选项

详情请参考[eslint/eqeqeq选项](https://eslint.nodejs.cn/docs/latest/rules/eqeqeq#选项)。

## 正例

```screen
export function test(a: string, b: string) {
  return a === b;
}
```

## 反例

```screen
export function test(a: string, b: string) {
  // Expected '===' and instead saw '=='.
  return a == b;
}
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查（ArkTS/TS）](ide-code-linter.md)。
