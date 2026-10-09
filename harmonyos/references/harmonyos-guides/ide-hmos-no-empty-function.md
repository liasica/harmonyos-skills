---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-no-empty-function
title: "@typescript-eslint/no-empty-function"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-empty-function
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:29+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:f97b64aef047f0edbbcd02c4ccca1d0adff31da2153227b8f6d812d0618ffaa0
---

不允许使用空函数。

## 规则配置

```json
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

```ts
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

```ts
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
