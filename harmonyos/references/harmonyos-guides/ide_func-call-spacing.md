---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_func-call-spacing
title: "@typescript-eslint/func-call-spacing"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/func-call-spacing
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:93eb716e4bc082c7ab0d9db8afc9a9892119882da7c660c9e0a0097b2b4f014c
---

禁止或者要求函数名与函数名后面的括号之间加空格。

## 规则配置

```screen
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

```screen
function fn() {
  console.log('hello');
}

// 默认不允许函数名称和左括号之间有空格。
fn();
```

## 反例

```screen
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
