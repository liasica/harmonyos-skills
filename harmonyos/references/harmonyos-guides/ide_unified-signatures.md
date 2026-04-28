---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_unified-signatures
title: @typescript-eslint/unified-signatures
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/unified-signatures
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:52+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:ef1b3a7fb01125d24d3418d0f972f220ead0c70c85a22d5802ab38f97a3160dc
---

如果两个重载函数可以用联合类型参数（|）、可选参数（?）或者剩余参数（...）来重构为一个函数，不允许使用重载。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/unified-signatures": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/unified-signatures选项](https://typescript-eslint.nodejs.cn/rules/unified-signatures/#options)。

## 正例

```
1. export declare function x(a: number | string): void;
2. export declare function y(...a: readonly number[]): void;
```

## 反例

```
1. export declare function x(a: number): void;
2. export declare function x(a: string): void;

4. export declare function y(): void;
5. export declare function y(...a: readonly number[]): void;
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
