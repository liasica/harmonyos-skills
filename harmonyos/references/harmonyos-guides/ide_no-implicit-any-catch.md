---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-implicit-any-catch
title: "@typescript-eslint/no-implicit-any-catch"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-implicit-any-catch
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:b0aa25c41f9b0aedc5d872ce8c0b62c761f60214d5a0c7d7a5511c4d07859b59
---

禁止在 catch 表达式中使用隐式“any”类型。

该规则仅支持对.js/.ts文件进行检查。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-implicit-any-catch": "error"
  }
}
```

## 选项

该规则默认不允许使用隐式any类型。但是可以接受{"allowExplicitAny": true}对象作为规则参数，以允许使用显式的any类型。

示例：

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-implicit-any-catch": ["error", {"allowExplicitAny": true}]
  }
}
```

在配置{"allowExplicitAny": true}的条件下，以下代码不会产生告警：

```screen
try {
  // ...
} catch (e: any) {
  // ...
}
```

## 正例

```screen
try {
  // ...
} catch (e: unknown) {
  // ...
}
```

## 反例

```screen
try {
  // ...
// 默认不允许使用隐式any类型
} catch (e) {
  // ...
}
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
