---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_consistent-type-definitions
title: @typescript-eslint/consistent-type-definitions
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/consistent-type-definitions
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:25+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:eebd8d1e7be5d9728b7c931b258105d6cec6912807739f8a44635e72a7132a6a
---

强制使用一致的类型声明样式，仅使用“interface”或者仅使用“type”。

该规则仅支持对.js/.ts文件进行检查。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@typescript-eslint/consistent-type-definitions": "error"
5. }
6. }
```

## 选项

详情请参考[@typescript-eslint/consistent-type-definitions选项](https://typescript-eslint.nodejs.cn/rules/consistent-type-definitions/#options)。

## 正例

```
1. // 基本类型的定义可以使用type
2. export type T1 = string;

4. // 默认推荐使用interface 进行对象类型定义
5. export interface T2 {
6. x: number;
7. }

9. export type Foo = string | T2;
```

## 反例

```
1. // 默认推荐使用interface 进行对象类型定义
2. type T = { x: number };
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
