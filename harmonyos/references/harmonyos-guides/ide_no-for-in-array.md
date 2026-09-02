---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-for-in-array
title: "@typescript-eslint/no-for-in-array"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-for-in-array
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8c1f6418c928bd501054840ed92324042d38ce86c30ede1c6d13b9d0c994f541
---

禁止使用 for-in 循环来遍历数组元素。

该规则仅支持对.js/.ts文件进行检查。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-for-in-array": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
declare const array: string[];

for (const value of array) {
  console.log(value);
}

array.forEach((value) => {
  console.log(value);
});
```

## 反例

```screen
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
