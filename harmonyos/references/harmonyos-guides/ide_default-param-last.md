---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_default-param-last
title: @typescript-eslint/default-param-last
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/default-param-last
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:26+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:ea5744adde55f522803a6e52b0483fa581798032abf8bc99bfc698ee4a5e9ba2
---

强制默认参数位于参数列表的最后一个。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/default-param-last": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. const defaultValue = 0;
2. export function f1(a = defaultValue) {
3. return a;
4. }
5. export function f2(a: number, b = defaultValue) {
6. return a + b;
7. }
8. export function f3(a: number, b?: number) {
9. return b !== undefined ? a + b : a;
10. }
11. export function f4(a: number, b?: number, c = defaultValue) {
12. return b !== undefined ? a + b + c : a + c;
13. }
14. export function f5(a: number, b = defaultValue, c?: number) {
15. return c !== undefined ? a + c : a + b;
16. }
```

## 反例

```
1. const defaultValue = 0;
2. export function f2(b = defaultValue, a: number) {
3. return a + b;
4. }
5. export function f3(b?: number, a: number) {
6. return b !== undefined ? a + b : a;
7. }
8. export function f4(b?: number, a: number, c = defaultValue) {
9. return b !== undefined ? a + b + c : a + c;
10. }
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
