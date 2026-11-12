---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_prefer-literal-enum-member
title: "@typescript-eslint/prefer-literal-enum-member"
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/prefer-literal-enum-member
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:56+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:77bc313e02b62f2706083daa1213cada95846f0511c3514d2275100401ab826b
---

要求所有枚举成员都定义为字面量值。

该规则仅支持对.js/.ts文件进行检查。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/prefer-literal-enum-member": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/prefer-literal-enum-member选项](https://typescript-eslint.nodejs.cn/rules/prefer-literal-enum-member/#options)。

## 正例

```screen
export enum Valid {
  a = 'hello',
  b = 'TestStr' // A regular string
}
```

## 反例

```screen
const str = 'Test';
export enum Invalid {
  a = str, // Variable assignment
  b = {}, // Object assignment
  c = `A template literal string`, // Template literal
  d = new Set(1, 2, 3), // Constructor in assignment
  e = 2 + 2 // Expression assignment
}
```

## 规则集

```screen
plugin:@typescript-eslint/recommended
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查（ArkTS/TS）](ide-code-linter.md)。
