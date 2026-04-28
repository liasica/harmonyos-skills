---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-duplicate-imports
title: @typescript-eslint/no-duplicate-imports
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-duplicate-imports
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:30+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:cff2039dc89f737cb8868822bf4080354d7bf33b23393d910c471be2d6a2fc29
---

禁止重复的模块导入。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/no-duplicate-imports": "error"
5. }
6. }
```

## 选项

详情请参考[eslint/no-duplicate-imports选项](https://eslint.nodejs.cn/docs/latest/rules/no-duplicate-imports#选项)。

## 正例

```
1. // foo和bar代表两个文件
2. import { foo } from './foo';
3. import bar from './bar';
```

## 反例

```
1. // foo代表文件
2. import { foo } from './foo';
3. import { bar } from './foo';
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
