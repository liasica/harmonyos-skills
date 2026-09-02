---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_naming-convention
title: "@typescript-eslint/naming-convention"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/naming-convention
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:4b0184a3a53089243f8000c4392b70002e81c7d8c5b26ae1ef15007e5340877c
---

强制标识符使用一致的命名风格。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/naming-convention": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/naming-convention选项](https://typescript-eslint.nodejs.cn/rules/naming-convention/#options)。

## 正例

```screen
// 默认类名为大驼峰的命名风格，函数名为小驼峰的命名风格
export class Bar {
  public meth() {
    console.info('method');
  }
}

export function foo() {
  console.info('function');
}
```

## 反例

```screen
// 默认类名为大驼峰的命名风格，函数名为小驼峰的命名风格
export class bar {
  public Meth() {
    console.info('method');
  }
}

export function Foo() {
  console.info('function');
}
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
