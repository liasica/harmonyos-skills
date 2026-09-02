---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_consistent-type-imports
title: "@typescript-eslint/consistent-type-imports"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/consistent-type-imports
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:06738011eab7d9fe6fdf9e7685165d30436544e01a780dc5b4c98461a757f21b
---

强制使用一致的类型导入风格。

该规则仅支持对.js/.ts文件进行检查。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/consistent-type-imports": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/consistent-type-imports选项](https://typescript-eslint.nodejs.cn/rules/consistent-type-imports/#options)。

## 正例

```screen
// 默认推荐使用import type Foo from '...'
import type { Foo } from 'Foo';
import type Bar from 'Bar';
export type T = Foo;
export const x: Bar = 1;
```

## 反例

```screen
// 默认推荐使用import type Foo from '...'
import { Foo } from 'Foo';
import Bar from 'Bar';
export type T = Foo;
export const x: Bar = 1;
```

## 规则集

```screen
plugin:@typescript-eslint/recommended
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
