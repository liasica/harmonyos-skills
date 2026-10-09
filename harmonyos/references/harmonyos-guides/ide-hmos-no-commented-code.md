---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-no-commented-code
title: "@security/no-commented-code"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 安全规则@security > @security/no-commented-code
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:31+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:ea2fec51918fc6fe4ba0c51113a5cf592d9f6da337eb1eb831a9191ac5bc964c
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

该规则无需配置额外选项。

## 正例

```ts
// this is a comment
```

## 反例

```ts
// console.log('info')
```

## 规则集

```screen
plugin:@security/recommended
plugin:@security/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
