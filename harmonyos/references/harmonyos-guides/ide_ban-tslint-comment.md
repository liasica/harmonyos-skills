---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_ban-tslint-comment
title: "@typescript-eslint/ban-tslint-comment"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/ban-tslint-comment
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:50+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f1a15a4c5123c91ab8b153be036432897e7a4ed4502e91583cce3f947b8c8fd3
---

不允许使用`//tslint:<rule-flag>`格式的注释。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/ban-tslint-comment": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
// This is a comment that just happens to mention tslint
/* This is a multiline comment that just happens to mention tslint */
console.log('hello'); // This is a comment that just happens to mention tslint
```

## 反例

```screen
/* tslint:disable */
/* tslint:enable */
/* tslint:disable:rule1 rule2 rule3... */
/* tslint:enable:rule1 rule2 rule3... */
// tslint:disable-next-line
console.log('hello'); // tslint:disable-line
// tslint:disable-next-line:rule1 rule2 rule3...
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
