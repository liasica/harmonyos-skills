---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-invalid-this
title: "@typescript-eslint/no-invalid-this"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-invalid-this
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:b9c99adc3d43e104ac8ce30f86802f4e1b11a9b24f0dca0fb67a74f689033285
---

禁止在this值为undefined的上下文中使用this。

## 规则配置

```screen
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

```screen
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

```screen
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
