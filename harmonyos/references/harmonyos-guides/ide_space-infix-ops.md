---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_space-infix-ops
title: @typescript-eslint/space-infix-ops
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/space-infix-ops
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:50+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:411d4d7e6b5acdfbbd090b7489a97ce8ce80a8da94cfc9a8d73dde5e510932c3
---

运算符前后要求有空格。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/space-infix-ops": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/space-infix-ops选项](https://eslint.nodejs.cn/docs/rules/space-infix-ops#选项)。

## 正例

```
1. declare const a: number;
2. declare const b: number;
3. export const c = a + b;
```

## 反例

```
1. declare const a: number;
2. declare const b: number;
3. export const c = a+b;
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
