---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-commented-code
title: @security/no-commented-code
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 安全规则@security > @security/no-commented-code
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:53+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:a8c19a92e2dc428a4df0e8eb6b337b1f41584388746811f90fc4359171dd2961
---

不使用的代码段建议直接删除，不允许通过注释的方式保留。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@security/no-commented-code": "warn"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. // this is a comment
```

## 反例

```
1. // console.log('info')
```

## 规则集

```
1. plugin:@security/recommended
2. plugin:@security/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
