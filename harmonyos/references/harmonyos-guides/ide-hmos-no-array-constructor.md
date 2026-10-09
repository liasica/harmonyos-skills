---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-no-array-constructor
title: "@typescript-eslint/no-array-constructor"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-array-constructor
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:29+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:0791c7cc64d9185efc3983c3d6e9fa4b2192907a18e1860d82cae870aaf6d0dc
---

不允许使用“Array”构造函数。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-array-constructor": "error"
  }
}
```

## 选项

该规则无需配置额外选项。

## 正例

```ts
const length = 500;
Array(length);

export const newArr: number[] = new Array(['1'].length);

export const arr = ['0', '1', '2'];

export const createArray = (array: string) => new Array(array.length);
```

## 反例

```ts
Array();

Array('0', '1', '2');

new Array('0', '1', '2');
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
