---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-space-before-function-paren-stylistic
title: "@hw-stylistic/space-before-function-paren"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > ArkTS代码风格规则@hw-stylistic > @hw-stylistic/space-before-function-paren
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:33+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:1ced1dd6c9ded21d5b8a80439fa52add1e79b2a62e05d8594c21a179d6949a56
---

在函数名和“(”之间强制不加空格。该规则仅检查.ets文件类型。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@hw-stylistic/space-before-function-paren": "error"
  }
}
```

## 选项

该规则无需配置额外选项。

## 正例

```ts
function bar() {
  // doSomething
}
bar();
```

## 反例

```ts
// Unexpected space before function parentheses.
function bar () {
  // doSomething
}
// Unexpected space before function parentheses.
bar  ();
```

## 规则集

```screen
"plugin:@hw-stylistic/recommended"
"plugin:@hw-stylistic/all"
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
