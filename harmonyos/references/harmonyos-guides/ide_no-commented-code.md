---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-commented-code
title: "@security/no-commented-code"
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 安全规则@security > @security/no-commented-code
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:56+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:fe5708639450d40d698120084a1d307eecf831d77680de4ed6acb9ecb39198dc
---

不使用的代码段建议直接删除，不允许通过注释的方式保留。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@security/no-commented-code": "warn"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
// this is a comment
```

## 反例

```screen
// console.log('info')
```

## 规则集

```screen
plugin:@security/recommended
plugin:@security/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查（ArkTS/TS）](ide-code-linter.md)。
