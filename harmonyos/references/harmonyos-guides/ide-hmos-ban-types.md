---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-ban-types
title: "@typescript-eslint/ban-types"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/ban-types
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:28+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:ee628c9f7d102268e7365b94b5f6798151b9e95cdf420dcfe0b64fc3c4f7203f
---

不允许使用某些类型。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/ban-types": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/ban-types选项](https://typescript-eslint.nodejs.cn/rules/ban-types/#options)。

## 正例

```ts
// 类型小写保持一致
const str: string = 'foo';
const bool: boolean = true;
const num: number = 1;
const bigInt: bigint = 1n;

// 使用正确的函数类型
const func: () => string = () => 'hello';

export { str, bool, num, bigInt, func };
```

## 反例

```ts
// 类型小写保持一致
const str: String = 'foo';
const bool: Boolean = true;
const num: Number = 1;
const bigInt: BigInt = 1n;

// 使用正确的函数类型
const func: Function = () => 'hello';

export { str, bool, num, bigInt, func };
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
