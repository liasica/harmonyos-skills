---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_prefer-nullish-coalescing
title: @typescript-eslint/prefer-nullish-coalescing
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/prefer-nullish-coalescing
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:45+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:769f05a33e913e87697af4ae1dc2a24250b24a953cb184b67af50dd2f996e0c3
---

强制使用空值合并运算符（??）而不是逻辑运算符。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/prefer-nullish-coalescing": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/prefer-nullish-coalescing选项](https://typescript-eslint.nodejs.cn/rules/prefer-nullish-coalescing/#options)。

## 正例

```
1. function getText1(): string | undefined {
2. return 'bar';
3. }

5. function getText2(): string | null {
6. return 'bar';
7. }

9. const foo1: string | undefined = getText1();
10. export const v1 = foo1 ?? 'a string';

12. const foo2: string | null = getText2();
13. export const v2 = foo2 ?? 'a string';
```

## 反例

```
1. declare const a: string | null;
2. declare const b: string | null;

4. export const c = a || b;
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
