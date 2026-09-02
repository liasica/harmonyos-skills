---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-base-to-string
title: "@typescript-eslint/no-base-to-string"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-base-to-string
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:ce7a1617af977c48606e2c93f5bf14d252b042cd00ccac2015fec6074ffb355c
---

要求当一个对象在字符串化时提供了有用的信息，才能调用“toString()”方法。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-base-to-string": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/no-base-to-string选项](https://typescript-eslint.nodejs.cn/rules/no-base-to-string/#options)。

## 正例

```screen
// These types all have useful .toString()s
const num = 123;
export const v1 = 'Text' + true;
export const v2 = `Value: ${num}`;
(() => {
  console.info('arrow function');
}).toString();
```

## 反例

```screen
interface MyType {
  name: string;
}
// Passing an object or class instance to string concatenation:
const obj: MyType = {
  name: 'object'
};
export const v1 = '' + obj;

class MyClass {}
const value = new MyClass();
export const v2 = value + '';

// Interpolation and manual .toString() calls too:
export const v3 = `Value: ${value}`;
export const v4 = obj.toString();
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
