---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_eqeqeq
title: eqeqeq
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > eqeqeq
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:53+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:8320b257bd6fc367ab074db8e4255d246a56fe2b29106f5cc0df485b5594c2d9
---

要求使用===和!==。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "eqeqeq": "error"
5. }
6. }
```

## 选项

详情请参考[eslint/eqeqeq选项](https://eslint.nodejs.cn/docs/latest/rules/eqeqeq#选项)。

## 正例

```
1. export function test(a: string, b: string) {
2. return a === b;
3. }
```

## 反例

```
1. export function test(a: string, b: string) {
2. // Expected '===' and instead saw '=='.
3. return a == b;
4. }
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
