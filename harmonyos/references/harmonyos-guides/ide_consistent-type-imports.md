---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_consistent-type-imports
title: @typescript-eslint/consistent-type-imports
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/consistent-type-imports
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:25+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:7eca539bcccfa2e0f1b06d4ba86eb016d58c4e16db44b103b5eb1090eda95b3d
---

强制使用一致的类型导入风格。

该规则仅支持对.js/.ts文件进行检查。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/consistent-type-imports": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/consistent-type-imports选项](https://typescript-eslint.nodejs.cn/rules/consistent-type-imports/#options)。

## 正例

```
1. // 默认推荐使用import type Foo from '...'
2. import type { Foo } from 'Foo';
3. import type Bar from 'Bar';
4. export type T = Foo;
5. export const x: Bar = 1;
```

## 反例

```
1. // 默认推荐使用import type Foo from '...'
2. import { Foo } from 'Foo';
3. import Bar from 'Bar';
4. export type T = Foo;
5. export const x: Bar = 1;
```

## 规则集

```
1. plugin:@typescript-eslint/recommended
2. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
