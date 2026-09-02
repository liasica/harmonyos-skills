---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-array-constructor
title: "@typescript-eslint/no-array-constructor"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-array-constructor
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:bf05d43342e641a2be8a5be91fbb29a3a9e2a6a490f4d2d797b42b6f12210237
---

不允许使用“Array”构造函数。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-array-constructor": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
const length = 500;
Array(length);

export const newArr: number[] = new Array(['1'].length);

export const arr = ['0', '1', '2'];

export const createArray = (array: string) => new Array(array.length);
```

## 反例

```screen
Array();

Array('0', '1', '2');

new Array('0', '1', '2');
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
