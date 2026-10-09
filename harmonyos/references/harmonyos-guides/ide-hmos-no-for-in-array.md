---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-no-for-in-array
title: "@typescript-eslint/no-for-in-array"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-for-in-array
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:29+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:d840f8f48b68af993ba15f799d5d3e7a7a4f14e7aa6f6742d9d276f97f8cc111
---

禁止使用 for-in 循环来遍历数组元素。

该规则仅支持对.js/.ts文件进行检查。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-for-in-array": "error"
  }
}
```

## 选项

该规则无需配置额外选项。

## 正例

```ts
declare const array: string[];

for (const value of array) {
  console.log(value);
}

array.forEach((value) => {
  console.log(value);
});
```

## 反例

```ts
declare const array: string[];

for (const i in array) {
  console.log(array[i]);
}

for (const i in array) {
  console.log(i, array[i]);
}
```

## 规则集

```screen
plugin:@typescript-eslint/recommended
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
