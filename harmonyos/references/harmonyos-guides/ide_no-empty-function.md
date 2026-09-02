---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-empty-function
title: "@typescript-eslint/no-empty-function"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-empty-function
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:051787fbf316f2725e8e3c5e344e38f50293b1ed678c4fa6049027851d994729
---

不允许使用空函数。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-empty-function": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/no-empty-function选项](https://eslint.nodejs.cn/docs/rules/no-empty-function#选项)。

## 正例

该规则旨在消除空函数。如果函数包含注释，则不会将其视为问题。

```screen
/*eslint no-empty-function: "error"*/
function foo() {
  // do nothing.
}

const baz = () => {
  foo();
};

export class Bar {
  public meth1() {
    // do something
  }

  public meth2() {
    baz();
  }
}
```

## 反例

```screen
/*eslint no-empty-function: "error"*/
function foo() {

}

const baz = () => {

};

export class Bar {
  public meth1() {

  }

  public meth2() {

  }
}
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
