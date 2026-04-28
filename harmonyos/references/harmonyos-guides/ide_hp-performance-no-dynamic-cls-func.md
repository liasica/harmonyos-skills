---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-performance-no-dynamic-cls-func
title: @performance/hp-performance-no-dynamic-cls-func
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-performance-no-dynamic-cls-func
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:12+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:810bdb7552110bd676d81b5a67bf8df6732012c4aa9770dd0824409335154309
---

避免动态声明function与class，仅适用于js/ts。

根据[ArkTS编程规范](arkts-high-performance-programming.md)，建议修改。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/hp-performance-no-dynamic-cls-func": "suggestion",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. function foo(f: boolean, a: number, b: number): number {
2. if (f) {
3. return add(a, b);
4. } else {
5. return sub(a, b);
6. }
7. }
8. function add(c: number, d: number): number {
9. return c + d;
10. }
11. function sub(e: number, g: number): number {
12. return e - g;
13. }
```

## 反例

```
1. function foo(f: boolean, a: number, b: number): number {
2. if (f) {
3. function add(c: number, d: number): number {
4. return c + d;
5. }
6. return add(a, b);
7. } else {
8. function sub(e: number, g: number): number {
9. return e - g;
10. }
11. return sub(a, b);
12. }
13. }
```

## 规则集

```
1. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
