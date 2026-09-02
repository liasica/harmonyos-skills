---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_prefer-const
title: prefer-const
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > prefer-const
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:52+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:fd5abe2cfa7afaa75edf42148ae15b2dce0695427b437f6fa0ac2b3f46d394a7
---

推荐声明后未修改值的变量用const关键字来声明。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "prefer-const": "error"
  }
}
```

## 选项

详情请参考[eslint/prefer-const选项](https://eslint.nodejs.cn/docs/latest/rules/prefer-const#选项)。

## 正例

```screen
const a = 'hello';
console.log(a);
```

## 反例

```screen
// 变量a声明以后未重新赋值，建议用const关键字来声明
let a = 'hello';
console.log(a);
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
