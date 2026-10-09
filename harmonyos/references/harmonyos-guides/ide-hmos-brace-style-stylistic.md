---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-brace-style-stylistic
title: "@hw-stylistic/brace-style"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > ArkTS代码风格规则@hw-stylistic > @hw-stylistic/brace-style
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:32+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:163d2a36dcb3607b0fd9d4560cfaf50ae678ff99bf20d5c093208aa7dfe15327
---

强制大括号和语句位于同一行。该规则仅检查.ets文件类型。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@hw-stylistic/brace-style": "error"
  }
}
```

## 选项

该规则无需配置额外选项。

## 正例

```ts
try {
  // doSomething
} catch (e) {
  // doSomething
} finally {
  // doSomething
}
```

## 反例

```ts
try
// Opening curly brace does not appear on the same line as statement before.
{

// Closing curly brace does not appear on the same line as statement after.
}
catch (e)
// Opening curly brace does not appear on the same line as statement before.
{

// Closing curly brace does not appear on the same line as statement after.
}
finally
// Opening curly brace does not appear on the same line as statement before.
{

}
```

## 规则集

```screen
"plugin:@hw-stylistic/recommended"
"plugin:@hw-stylistic/all"
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
