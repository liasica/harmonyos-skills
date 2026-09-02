---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-dynamic-delete
title: "@typescript-eslint/no-dynamic-delete"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-dynamic-delete
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:24198f34b54025270c7ca61e12d3aa61b0c9d5991ef2ef6b5cd1195b3f09b554
---

不允许在computed key表达式上使用“delete”运算符。

该规则仅支持对.js/.ts文件进行检查。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-dynamic-delete": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
const container: Record<string, number> = {
  /* ... */
};

// Constant runtime lookups by string index
delete container.aaa;

// Constants that must be accessed by []
delete container['7'];
// '-Infinity' is number.  
delete container['-Infinity'];
```

## 反例

```screen
const container: Record<string, number> = {
  /* ... */
};

// Can be replaced with the constant equivalents, such as container.aaa
delete container['aaa'];
// 'Infinity' may be a string constant
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
