---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_prefer-for-of
title: "@typescript-eslint/prefer-for-of"
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/prefer-for-of
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:56+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:6affabd6c5ec33ced10bc282b22ad2b9bf2e5d15151107aa8dd9bf80246a0a35
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查（ArkTS/TS）](ide-code-linter.md)。
