---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-no-inferrable-types
title: "@typescript-eslint/no-inferrable-types"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-inferrable-types
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:29+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:45011a9a51434ea690e5c907c484844e820e9aa3fa098abdfbd29a72ba524394
---

不允许对初始化为数字、字符串或布尔值的变量或参数进行显式类型声明。

变量或者参数如果在初始化时定义为布尔、数字或者字符串类型，TypeScript可以推断出其类型，不用显式声明其类型。

该规则仅支持对.js/.ts文件进行检查。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-inferrable-types": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/no-inferrable-types选项](https://typescript-eslint.io/rules/no-inferrable-types/#options)。

## 正例

```ts
const num = 10;
export const a1 = 10n;
export const a2 = BigInt(num);
export const a3 = !num;
export const a4 = Boolean(null);
export const a5 = true;
export const a6 = null;

export class Foo {
  public prop = num;
}

export function fn(a = num, b = true): void {
  console.info(`${a}${b}`);
}
```

## 反例

```ts
const num: number = 10;
export const a1: bigint = 10n;
export const a2: bigint = BigInt(num);
export const a3: boolean = !num;
export const a4: boolean = Boolean(null);
export const a5: boolean = true;
export const a6: null = null;

export class Foo {
  public prop: number = num;
}

export function fn(a: number = num, b: boolean = true): void {
  console.info(`${a}${b}`);
}
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
