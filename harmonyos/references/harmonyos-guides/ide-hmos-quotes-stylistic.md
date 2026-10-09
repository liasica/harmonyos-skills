---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-quotes-stylistic
title: "@hw-stylistic/quotes"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > ArkTS代码风格规则@hw-stylistic > @hw-stylistic/quotes
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:33+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:718ceec5c73072bf77d4c145dd692935c8fa9a33264c18a2b9dc440770e93858
---

强制字符串使用单引号。该规则仅检查.ets文件类型。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@hw-stylistic/quotes": "error"
  }
}
```

## 选项

该规则无需配置额外选项。

## 正例

```ts
export {a, b};

const a = 'hello';
const b = `hello`;
```

## 反例

```ts
// Strings must use single quotes.
export const a = "hello";
```

## 规则集

```screen
"plugin:@hw-stylistic/recommended"
"plugin:@hw-stylistic/all"
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
