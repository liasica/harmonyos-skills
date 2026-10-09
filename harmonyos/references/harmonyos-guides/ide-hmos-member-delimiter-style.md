---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-member-delimiter-style
title: "@typescript-eslint/member-delimiter-style"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/member-delimiter-style
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:29+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:3b58fa56f206d0264c870bdab21748c2b20b236617f20f2ebe48f2b2332b4b13
---

要求接口和类型别名中的成员之间使用特定的分隔符。

支持定义的分隔符有三种：分号、逗号、无分隔符。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/member-delimiter-style": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/member-delimiter-style选项](https://typescript-eslint.nodejs.cn/rules/member-delimiter-style/#options)。

## 正例

```ts
// 默认接口/类型别名定义为多行的场景下，每个成员应以分号 (;) 分隔。 最后一个成员必须有一个分隔符。
// 默认接口/类型别名定义为单行的场景下，每个成员应以分号 (;) 分隔。最后一个成员不能有分隔符。
// 接口/类型别名中的任何换行符都会使其成为多行。
export interface Foo1 {
  name: string;

  greet(): string;
}

export interface Foo2 { name: string }
```

## 反例

```ts
// missing semicolon delimiter
export interface Foo {
  name: string
  greet(): string
}

// using incorrect delimiter
export interface Bar {
  name: string,
  greet(): string,
}

// missing last member delimiter
export interface Baz {
  name: string;
  greet(): string
}
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
