---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-inferrable-types
title: @typescript-eslint/no-inferrable-types
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-inferrable-types
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:34+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:68590b208cabc223a573e35dcdbb74dbbc18c911f041cd529829ef0570ac22dd
---

不允许对初始化为数字、字符串或布尔值的变量或参数进行显式类型声明。

变量或者参数如果在初始化时定义为布尔、数字或者字符串类型，Typescript可以推断出其类型，不用显式声明其类型。

该规则仅支持对.js/.ts文件进行检查。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/no-inferrable-types": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/no-inferrable-types选项](https://typescript-eslint.io/rules/no-inferrable-types/#options)。

## 正例

```
1. const num = 10;
2. export const a1 = 10n;
3. export const a2 = BigInt(num);
4. export const a3 = !num;
5. export const a4 = Boolean(null);
6. export const a5 = true;
7. export const a6 = null;

9. export class Foo {
10. public prop = num;
11. }

13. export function fn(a = num, b = true): void {
14. console.info(`${a}${b}`);
15. }
```

## 反例

```
1. const num: number = 10;
2. export const a1: bigint = 10n;
3. export const a2: bigint = BigInt(num);
4. export const a3: boolean = !num;
5. export const a4: boolean = Boolean(null);
6. export const a5: boolean = true;
7. export const a6: null = null;

9. export class Foo {
10. public prop: number = num;
11. }

13. export function fn(a: number = num, b: boolean = true): void {
14. console.info(`${a}${b}`);
15. }
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
