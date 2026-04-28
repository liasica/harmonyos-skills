---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-base-to-string
title: @typescript-eslint/no-base-to-string
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-base-to-string
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:29+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:5e9ea8d64e8ab78406a80847343d3dae1aa1f26b28c3e3f44da68ada6d4eb184
---

要求当一个对象在字符串化时提供了有用的信息，才能调用“toString()”方法。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/no-base-to-string": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/no-base-to-string选项](https://typescript-eslint.nodejs.cn/rules/no-base-to-string/#options)。

## 正例

```
1. // These types all have useful .toString()s
2. const num = 123;
3. export const v1 = 'Text' + true;
4. export const v2 = `Value: ${num}`;
5. (() => {
6. console.info('arrow function');
7. }).toString();
```

## 反例

```
1. interface MyType {
2. name: string;
3. }
4. // Passing an object or class instance to string concatenation:
5. const obj: MyType = {
6. name: 'object'
7. };
8. export const v1 = '' + obj;

10. class MyClass {}
11. const value = new MyClass();
12. export const v2 = value + '';

14. // Interpolation and manual .toString() calls too:
15. export const v3 = `Value: ${value}`;
16. export const v4 = obj.toString();
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
