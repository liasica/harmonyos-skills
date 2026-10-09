---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-no-invalid-this
title: "@typescript-eslint/no-invalid-this"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-invalid-this
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:29+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:9da6231811c8a0d8f7506d698efb152a782897c84f802715fac556a36a826e14
---

禁止在this的值为undefined的上下文中使用this。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-invalid-this": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/no-invalid-this选项](https://eslint.nodejs.cn/docs/rules/no-invalid-this#选项)。

## 正例

```ts
// ts代码文件中需要添加"use strict"
function baz(arg0: () => object) {
  return arg0;
}

export class Bar {
  public a: number;

  public constructor() {
    this.a = 0;
    baz(() => this);
  }
}
```

## 反例

```ts
// ts代码文件中需要添加"use strict"
function baz(arg0: () => object) {
  return arg0;
}

export function foo1() {
  this.a = 0;
  baz(() => this);
}

export const foo2 = () => {
  this.a = 0;
  baz(() => this);
};
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
