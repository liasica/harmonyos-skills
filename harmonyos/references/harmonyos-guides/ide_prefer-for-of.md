---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_prefer-for-of
title: "@typescript-eslint/prefer-for-of"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/prefer-for-of
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3083d9ae03e24c58b87fc6e85ce95fe8cd58fa24f2b4062342b5e22ce7d51724
---

强制使用“for-of”循环而不是标准“for”循环。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/prefer-for-of": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
declare const array: string[];

for (const x of array) {
  console.log(x);
}

for (let i = 0; i < array.length; i++) {
  // i is used, so for-of could not be used.
  console.log(`${i}-${array[i]}`);
}
```

## 反例

```screen
declare const array: string[];

for (const x of array) {
  console.log(x);
}

for (let i = 0; i < array.length; i++) {
  console.log(array[i]);
}
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
