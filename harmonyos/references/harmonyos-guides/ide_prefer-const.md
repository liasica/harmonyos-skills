---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_prefer-const
title: prefer-const
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > prefer-const
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:52+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:f37f888da9c4765df4c71b83515cbde45e0e43d5a7b05159c83e4bcb9d3004fa
---

推荐声明后未修改值的变量用const关键字来声明。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "prefer-const": "error"
5. }
6. }
```

## 选项

详情请参考[eslint/prefer-const选项](https://eslint.nodejs.cn/docs/latest/rules/prefer-const#选项)。

## 正例

```
1. const a = 'hello';
2. console.log(a);
```

## 反例

```
1. // 变量a声明以后未重新赋值，建议用const关键字来声明
2. let a = 'hello';
3. console.log(a);
```

## 规则集

```
1. plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
