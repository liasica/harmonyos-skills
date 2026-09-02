---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-empty-interface
title: "@typescript-eslint/no-empty-interface"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-empty-interface
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:a014c471bfbd9268579a725a2d0eaf24f86834d2f191727922b78c99daada222
---

不允许声明空接口。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-empty-interface": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/no-empty-interface选项](https://typescript-eslint.nodejs.cn/rules/no-empty-interface/#options)。

## 正例

```screen
// an interface with any number of members
interface Foo {
  name: string;
}

interface Bar {
  age: number;
}

// an interface with more than one supertype
// in this case the interface can be used as a replacement of an intersection type.
export interface Baz extends Foo, Bar {}
```

## 反例

```screen
// an empty interface
interface Foo {}

// an interface with only one supertype (Bar === Foo)
export interface Bar extends Foo {}

// an interface with an empty list of supertypes
export interface Baz {}
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
