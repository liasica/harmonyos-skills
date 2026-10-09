---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-no-namespace
title: "@typescript-eslint/no-namespace"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-namespace
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:29+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:a0b1703484c3b9700b8f454ce21d4c0ab61e9e428786a37526640e4039291821
---

禁止使用 TypeScript语法中的命名空间。

命名空间是一种过时的语法，推荐使用import/export。

该规则仅支持对.js/.ts文件进行检查。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-namespace": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/no-namespace选项](https://typescript-eslint.nodejs.cn/rules/no-namespace/#options)。

## 正例

```ts
// foo为模块名
declare module 'foo' {}
// anything inside a d.ts file
```

## 反例

```ts
module foo {}
namespace foo {}

declare module foo {}
declare namespace foo {}
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
