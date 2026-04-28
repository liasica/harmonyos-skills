---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-space-infix-ops-stylistic
title: @hw-stylistic/space-infix-ops
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:32+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:017860a7fa1fb441725fdd1c14c571fcbc43758e6053e613113f588762fc3425
---

强制运算符前后都加空格。该规则仅检查.ets文件类型。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@hw-stylistic/space-infix-ops": "error"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. export function test(size: number) {
2. for (let i = 0; i < size; i++) {
3. console.info(`${i}`);
4. }
5. }

7. export function test1(a: boolean, b: boolean, c: boolean) {
8. return a || (b && c);
9. }
```

## 反例

```
1. export function test(size: number) {
2. // Operator '=' must be spaced.
3. // Operator '<' must be spaced.
4. for (let i=0; i<size; i++) {
5. console.info(`${i}`);
6. }
7. }

9. export function test1(a: boolean, b: boolean, c: boolean) {
10. // Operator '||' must be spaced.
11. // Operator '&&' must be spaced.
12. return a||b&&c;
13. }
```

## 规则集

```
1. "plugin:@hw-stylistic/recommended"
2. "plugin:@hw-stylistic/all"
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
