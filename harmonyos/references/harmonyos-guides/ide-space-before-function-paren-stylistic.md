---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-space-before-function-paren-stylistic
title: "@hw-stylistic/space-before-function-paren"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > ArkTS代码风格规则@hw-stylistic > @hw-stylistic/space-before-function-paren
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:324f3959282d4c5cce80dee232c9e0024fdfaa90a3103c95010299b31cae04e9
---

在函数名和“(”之间强制不加空格。该规则仅检查.ets文件类型。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@hw-stylistic/space-before-function-paren": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
function bar() {
  // doSomething
}
bar();
```

## 反例

```screen
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
