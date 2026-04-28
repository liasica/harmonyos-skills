---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_comma-spacing
title: @typescript-eslint/comma-spacing
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/comma-spacing
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:24+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:1499f4a3b77aa7b4a2e06307852d5af60e45dbe84c7a5c721cdb427499c410ca
---

强制逗号前后的空格风格保持一致。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/comma-spacing": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/comma-spacing选项](https://eslint.nodejs.cn/docs/rules/comma-spacing#选项)。

## 正例

```
1. // 默认不允许逗号前有空格，逗号后需要一个或多个空格
2. export const arr1 = ['1', '2'];
3. export const arr2 = ['1',, '3'];

5. function qur(a: string, b: string) {
6. return `${a}${b}`;
7. }
8. qur('1', '2');
```

## 反例

```
1. // 默认不允许逗号前有空格，逗号后需要一个或多个空格
2. export const arr = ['1' , '2'];

4. function qur(a: string ,b: string) {
5. return `${a}${b}`;
6. }
7. qur('1' ,'2');
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
