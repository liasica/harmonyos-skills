---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-no-dynamic-delete
title: "@typescript-eslint/no-dynamic-delete"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-dynamic-delete
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:29+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:4b692f5a9a0b8aa02fabdf751978437c4f9c0cd55065b10c37d31c4bc86b4d70
---

不允许在computed key表达式上使用“delete”运算符。

该规则仅支持对.js/.ts文件进行检查。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-dynamic-delete": "error"
  }
}
```

## 选项

该规则无需配置额外选项。

## 正例

```ts
const container: Record<string, number> = {
  /* ... */
};

// Constant runtime lookups by string index
delete container.aaa;

// Constants that must be accessed by []
delete container['7'];
delete container['-Infinity'];
```

## 反例

```ts
const container: Record<string, number> = {
  /* ... */
};

// Can be replaced with the constant equivalents, such as container.aaa
delete container['aaa'];
delete container['Infinity'];

// Dynamic, difficult-to-reason-about lookups
const name = 'name';
delete container[name];
delete container[name.toUpperCase()];
```

## 规则集

```screen
plugin:@typescript-eslint/recommended
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
