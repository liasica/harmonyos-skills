---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_ban-types
title: @typescript-eslint/ban-types
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/ban-types
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:23+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:451d6f18988a782d5aea406e69524dc2f87474b8839878bc61a2b9840f807e37
---

不允许使用某些类型。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/ban-types": "error"
5. }
6. }
```

## 选项

支持配置以下选项：

```
1. type Options = {
2. types: {
3. [key: string]: boolean | string | { message: string, fixWith: string } | null;
4. };
5. extendDefaults: boolean;
6. }
```

* types：对象类型，配置需要检查的类型信息。属性名是一个字符串，表示要检查的类型名称，属性值支持配置为以下类型：
  + boolean：布尔值，配置为true时，表示禁用该类型，告警信息使用默认配置；配置为false时，表示不禁用该类型，通常和{ extendDefaults: true }搭配使用，表示不检查某些预置类型。
  + string：自定义告警信息。
  + { message: string, fixWith: string } ：对象，message表示自定义的告警信息，fixWith表示自动修复时将禁用类型替换为新类型。
  + null：使用默认的告警信息。

* extendDefaults：布尔类型，默认为true，表示需要检查ts语法中内置的原始类包装器，包括String、Boolean、Number、Symbol、BigInt、Function和Object；配置为false时，表示不需要检查。

示例：

```
1. "@typescript-eslint/ban-types": [
2. "error",
3. {
4. "types": {
5. "String": true,
6. "Number": false,
7. "MyType": "Do not use 'MyType'",
8. "MyTypeWithFix": {
9. "message": "Do not use 'MyTypeWithFix', use 'MyType' instead",
10. "fixWith": "MyType"
11. }
12. },
13. "extendDefaults": true
14. },
15. ]
```

## 正例

```
1. // 类型小写保持一致
2. const str: string = 'foo';
3. const bool: boolean = true;
4. const num: number = 1;
5. const bigInt: bigint = 1n;

7. // 使用正确的函数类型
8. const func: () => string = () => 'hello';

10. export { str, bool, num, bigInt, func };
```

## 反例

```
1. // 类型小写保持一致
2. const str: String = 'foo';
3. const bool: Boolean = true;
4. const num: Number = 1;
5. const bigInt: BigInt = 1n;

7. // 使用正确的函数类型
8. const func: Function = () => 'hello';

10. export { str, bool, num, bigInt, func };
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
