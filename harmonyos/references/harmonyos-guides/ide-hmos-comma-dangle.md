---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-comma-dangle
title: "@typescript-eslint/comma-dangle"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/comma-dangle
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:28+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:88671a1246594977da2c9ef5796658ac697c2a8efb8c16038247c3cce6dc7798
---

允许或禁止使用尾随逗号。

## 规则配置

```json
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

```ts
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

```ts
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
