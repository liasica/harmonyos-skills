---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-prefer-for-of
title: "@typescript-eslint/prefer-for-of"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/prefer-for-of
category: harmonyos-guides
scraped_at: 2026-10-11T07:23:18+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:3e7ed9c1f86892de78aaf8415e8faf05cd6452ec485ace5edccd482441539b2d
---

强制使用“for-of”循环而不是标准“for”循环。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/prefer-for-of": "error"
  }
}
```

## 选项

该规则无需配置额外选项。

## 正例

```ts
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

```ts
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
