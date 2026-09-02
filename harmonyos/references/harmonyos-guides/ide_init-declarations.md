---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_init-declarations
title: "@typescript-eslint/init-declarations"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/init-declarations
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:51+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:11725b35129249d8cce07c70629cfe89ad4a88f14e8e310259438f104d622054
---

禁止或者要求在变量声明中进行初始化。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/init-declarations": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/init-declarations选项](https://eslint.nodejs.cn/docs/rules/init-declarations#选项)。

## 正例

```screen
// 默认变量必须在声明时初始化
export function foo() {
  console.info('hello');
}

export const bar = 1;
export const qux = 3;
```

## 反例

```screen
// 默认变量必须在声明时初始化
export function foo() {
  console.info('hello');
}

export let bar: string;
export let qux: number;
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
