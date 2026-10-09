---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-no-restricted-syntax
title: "@typescript-eslint/no-restricted-syntax"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-restricted-syntax
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:30+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:eafe907425d2eb397a30a6f931b6b0879d9cbdbbcaec2fa7c55aae03f0c4ea32
---

不允许使用指定的（即用户在规则中定义的）语法。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
      "@typescript-eslint/no-restricted-syntax": [
         "error",
         {
             "selector": "FunctionExpression",
             "message": "Function expressions are not allowed."
         },
         {
             "selector": "CallExpression[callee.name='setTimeout'][arguments.length!=2]",
             "message": "setTimeout must always be invoked with two arguments."
         }
     ]
  }
}
```

## 选项

详情请参考[@typescript-eslint/no-restricted-syntax选项](https://eslint.nodejs.cn/docs/latest/rules/no-restricted-syntax#选项)。

## 正例

```screen
/* eslint no-restricted-syntax: ["error", "ClassDeclaration"] */
export function doSomething() {
  console.info('doSomething');
}
```

## 反例

```ts
/* eslint no-restricted-syntax: ["error", "ClassDeclaration"] */
export class CC {
  public name: string;

  public constructor(name: string) {
    this.name = name;
  }
}
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
