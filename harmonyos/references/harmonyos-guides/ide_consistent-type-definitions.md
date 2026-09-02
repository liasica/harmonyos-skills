---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_consistent-type-definitions
title: "@typescript-eslint/consistent-type-definitions"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/consistent-type-definitions
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:6e1344d070d79c3904eb4dfc403e06ebefe9f05587710e364af3b6a1598ea8a3
---

强制使用一致的类型声明样式，仅使用“interface”或者仅使用“type”。

该规则仅支持对.js/.ts文件进行检查。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/consistent-type-definitions": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/consistent-type-definitions选项](https://typescript-eslint.nodejs.cn/rules/consistent-type-definitions/#options)。

## 正例

```screen
// 基本类型的定义可以使用type
export type T1 = string;

// 默认推荐使用interface 进行对象类型定义
export interface T2 {
  x: number;
}

export type Foo = string | T2;
```

## 反例

```screen
// 默认推荐使用interface 进行对象类型定义
type T = { x: number };
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
