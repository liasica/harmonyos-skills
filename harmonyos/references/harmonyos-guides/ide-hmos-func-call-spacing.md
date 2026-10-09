---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-func-call-spacing
title: "@typescript-eslint/func-call-spacing"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/func-call-spacing
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:29+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:ddd83b3bf3ce63c894e0e64ee139f9a0a9f1892c5d95f0e482c5a3e3ed190b8a
---

禁止或者要求函数名与函数名后面的括号之间加空格。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/func-call-spacing": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/func-call-spacing选项](https://eslint.nodejs.cn/docs/rules/func-call-spacing#选项)。

## 正例

```ts
function fn() {
  console.log('hello');
}

// 默认不允许函数名称和左括号之间有空格。
fn();
```

## 反例

```ts
function fn() {
  console.log('hello');
}

// 默认不允许函数名称和左括号之间有空格。
fn ();

fn
();
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
