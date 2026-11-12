---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-quotes-stylistic
title: "@hw-stylistic/quotes"
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > ArkTS代码风格规则@hw-stylistic > @hw-stylistic/quotes
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:59+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:ddb79bb5d1a4d401b25ab9f067dff1290ae0a6552b8c83ebb283dddaf4a5d478
---

强制字符串使用单引号。该规则仅检查.ets文件类型。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@hw-stylistic/quotes": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
export {a, b};

const a = 'hello';
const b = `hello`;
```

## 反例

```screen
// Strings must use single quotes.
export const a = "hello";
```

## 规则集

```screen
"plugin:@hw-stylistic/recommended"
"plugin:@hw-stylistic/all"
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查（ArkTS/TS）](ide-code-linter.md)。
