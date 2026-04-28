---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-explicit-any
title: @typescript-eslint/no-explicit-any
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-explicit-any
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:31+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:4a083322b1c8a6be00b5f665e3ce4f5833b7eb61fe0dfec1ada0da2ebf9e8fc5
---

不允许使用“any”类型。

该规则仅支持对.js/.ts文件进行检查。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/no-explicit-any": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/no-explicit-any选项](https://typescript-eslint.nodejs.cn/rules/no-explicit-any#options)。

## 正例

```
1. export const age1 = 17;
2. export const age2 = [age1];
3. export const age3 = [age1];

5. export function greet1(): string {
6. return 'greet';
7. }

9. export function greet2(): string[] {
10. return ['greet'];
11. }

13. export function greet4(): string[][] {
14. return [['greet']];
15. }

17. export function greet5(param: readonly string[]): string {
18. return param[age1];
19. }

21. export function greet6(param: readonly string[]): string[] {
22. return [...param];
23. }
```

## 反例

```
1. export const age1: any = 17;
2. export const age2: any = [age1];
3. export const age3: any = [age1];

5. export function greet1(): any {
6. return 'greet';
7. }

9. export function greet2(): any[] {
10. return ['greet'];
11. }

13. export function greet4(): any[][] {
14. return [['greet']];
15. }

17. export function greet5(param: readonly any[]): any {
18. return param[age1];
19. }

21. export function greet6(param: readonly any[]): any[] {
22. return [...param];
23. }
```

## 规则集

```
1. plugin:@typescript-eslint/recommended
2. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
