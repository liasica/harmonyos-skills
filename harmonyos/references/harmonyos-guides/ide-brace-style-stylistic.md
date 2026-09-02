---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-brace-style-stylistic
title: "@hw-stylistic/brace-style"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > ArkTS代码风格规则@hw-stylistic > @hw-stylistic/brace-style
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c2cde9ad6a68534bcc946f195093fa0af2da8d45064098e0481581467aaf230d
---

强制大括号和语句位于同一行。该规则仅检查.ets文件类型。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@hw-stylistic/brace-style": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
try {
  // doSomething
} catch (e) {
  // doSomething
} finally {
  // doSomething
}
```

## 反例

```screen
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
