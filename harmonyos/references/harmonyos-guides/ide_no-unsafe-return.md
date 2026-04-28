---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-return
title: @typescript-eslint/no-unsafe-return
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-unsafe-return
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:41+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:2f80155f86efff0fe7f7c79236f1e05d6659688bba5edee65991cf025a972f21
---

函数禁止返回类型为“any”的值。

该规则仅支持对.js/.ts文件进行检查。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/no-unsafe-return": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. export function foo1(): string {
2. return '1';
3. }

5. export function foo2(): object {
6. return Object.create(null) as Record<string, unknown>;
7. }

9. export const foo3 = (): object[] => [];
10. export const foo4 = (): string[] => ['a'];

12. export function assignability1(): Set<string> {
13. return new Set<string>(['foo']);
14. }
```

## 反例

```
1. export function foo1(): string {
2. return '1' as any;
3. }

5. export function foo2(): string {
6. return Object.create(null) as any;
7. }

9. export const foo3 = (): object[] => [] as any;
10. export const foo4 = (): string[] => ['a'] as any;

12. export function assignability1(): Set<string> {
13. return new Set<string>(['foo']) as any;
14. }
```

## 规则集

```
1. plugin:@typescript-eslint/recommended
2. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
