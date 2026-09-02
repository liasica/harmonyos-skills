---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-redeclare
title: "@typescript-eslint/no-redeclare"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-redeclare
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:75b45cf476f236d7061555d789da85e0d03ce7fe3f98a69de933446f10933474
---

禁止变量重复声明。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-redeclare": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/no-redeclare选项](https://eslint.nodejs.cn/docs/rules/no-redeclare#选项)。

## 正例

```screen
let a = '3';
a = '10';
console.info(a);

export class C {
  static {
    let c = '3';
    c = '10';
    console.info(c);
  }

  public foo() {
    let b = '3';
    b = '10';
    console.info(b);
  }
}
```

## 反例

```screen
// 不允许重复声明变量a
const a = '3';
const a = '10';

export class C {
  static {
    // 不允许重复声明变量c
    const c = '3';
    const c = '10';
  }

  public foo() {
    // 不允许重复声明变量b
    const b = '3';
    const b = '10';
  }
}
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
