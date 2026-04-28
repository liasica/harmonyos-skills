---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-extra-non-null-assertion
title: @typescript-eslint/no-extra-non-null-assertion
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-extra-non-null-assertion
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:34+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:61af9d0a69290fa12f36d2d3d028a9de7fdc8b8110df94913585f899c7a5aa82
---

不允许多余的非空断言。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/no-extra-non-null-assertion": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. interface BarType1 {
2. bar: number;
3. }

5. function getFoo(): BarType1 | null {
6. return null;
7. }
8. const foo: BarType1 | null = getFoo();
9. export const bar1: number | undefined = foo?.bar;

11. export function foo1(bar: number | undefined): void {
12. const newBar: number = bar ?? Number.MAX_VALUE;
13. console.info(`${newBar}`);
14. }
```

## 反例

```
1. interface BarType1 {
2. bar: number;
3. }

5. const foo1: BarType1 | null = null;
6. export const bar1 = foo1!!!.bar;

8. export function foo2(bar: number | undefined) {
9. const newBar: number = bar!!!;
10. console.info(`${newBar}`);
11. }

13. interface BarType2 {
14. n: number;
15. }

17. export function foo(bar?: BarType2) {
18. return bar!?.n;
19. }
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
