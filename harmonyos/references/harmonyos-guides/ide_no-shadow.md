---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-shadow
title: @typescript-eslint/no-shadow
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-shadow
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:38+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:ac08e09adc2aa6753b65c56d79f8f2fbb4a29567d6f819a4d673810e9fc85c6a
---

禁止声明与外部作用域变量同名的变量。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/no-shadow": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/no-shadow选项](https://typescript-eslint.nodejs.cn/rules/no-shadow/#options)。

## 正例

```
1. /*eslint no-shadow: "error"*/
2. const a = '1';
3. export function b() {
4. const a1 = '10';
5. console.info(a1);
6. }

8. export const c = () => {
9. const a1 = '10';
10. console.info(a1);
11. };

13. console.info(a);
```

## 反例

```
1. /*eslint no-shadow: "error"*/
2. const a = '3';
3. export function b() {
4. const a = '10';
5. console.info(a);
6. }

8. export const c = () => {
9. const a = '10';
10. console.info(a);
11. };

13. console.info(a);
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
