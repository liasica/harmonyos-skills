---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-prefer-const
title: prefer-const
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > prefer-const
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:31+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:7819384e0311903ce65ea71a34de93d7d9845b1ce673c1bb4f4c6af5ed81327c
---

推荐声明后未修改值的变量用const关键字来声明。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "prefer-const": "error"
  }
}
```

## 选项

该规则无需配置额外选项。详情请参考[eslint/prefer-const选项](https://eslint.nodejs.cn/docs/latest/rules/prefer-const#选项)。

## 正例

```ts
const a = 'hello';
console.log(a);
```

## 反例

```ts
// 变量a声明以后未重新赋值，建议用const关键字来声明
let a = 'hello';
console.log(a);
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
