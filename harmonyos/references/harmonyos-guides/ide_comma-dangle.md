---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_comma-dangle
title: "@typescript-eslint/comma-dangle"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/comma-dangle
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:50+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:a5ed9237135e51cd6d1db80d641c8b0d10d45cc22c3e7881d6cdb829ee02cf16
---

允许或禁止使用尾随逗号。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/comma-dangle": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/comma-dangle选项](https://eslint.nodejs.cn/docs/rules/comma-dangle#选项)。

## 正例

```screen
// 默认不允许尾随逗号
interface MyType {
  bar: string;
  qux: string;
}

const foo: MyType = {
  bar: 'baz',
  qux: 'qux'
};

const arr = ['1', '2'];

export { foo, arr };
```

## 反例

```screen
interface MyType {
  bar: string;
  qux: string;
}

const foo: MyType = {
  bar: 'baz',
  qux: 'qux',
};

const arr = ['1', '2',];

export { foo, arr, };
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
