---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unnecessary-qualifier
title: @typescript-eslint/no-unnecessary-qualifier
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-unnecessary-qualifier
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:39+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:0f2923ab6d2319e69d6e4c5d674a6096b78ccbadbd0f0c3fb569366ad61562ad
---

禁止不必要的命名空间限定符。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/no-unnecessary-qualifier": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. export enum A {
2. b = 'x',
3. c = b
4. }

6. export namespace B {
7. export type C = number;
8. export const x: C = 3;
9. }
```

## 反例

```
1. export enum A {
2. b = 'x',
3. c = A.b
4. }

6. export namespace B {
7. export type C = number;
8. export const x: B.C = 3;
9. }
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
