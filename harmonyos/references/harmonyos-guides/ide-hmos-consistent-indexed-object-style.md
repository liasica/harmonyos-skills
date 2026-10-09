---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-consistent-indexed-object-style
title: "@typescript-eslint/consistent-indexed-object-style"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/consistent-indexed-object-style
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:29+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:8b6db50433e0348132e6ef364b7275a1d81022c116c70c8cadcee6333c75e449
---

允许或禁止使用“Record”类型。

该规则仅支持对.js/.ts文件进行检查。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/consistent-indexed-object-style": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/consistent-indexed-object-style选项](https://typescript-eslint.nodejs.cn/rules/consistent-indexed-object-style/#options)。

## 正例

```ts
// 默认推荐使用Record 类型
export type Foo = Record<string, unknown>;
```

## 反例

```screen
export interface Foo1 {
  // 默认推荐使用Record 类型
  [key: string]: unknown;
}

export type Foo2 = {
  // 默认推荐使用Record 类型
  [key: string]: unknown;
};
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
