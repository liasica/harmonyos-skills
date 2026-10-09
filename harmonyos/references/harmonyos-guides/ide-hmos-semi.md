---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-semi
title: "@typescript-eslint/semi"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/semi
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:30+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:eaf147eb2760f34b6aee5afe89f6fe5e4eb44d23af148d8d0572230b06469743
---

要求或不允许使用分号。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/semi": "error"
  }
}
```

## 选项

详情请参考[@typescript-eslint/semi选项](https://eslint.nodejs.cn/docs/rules/semi#选项)。

## 正例

```ts
export const name = 'ESLint';

export class Foo {
  public bar = '1';
}
```

## 反例

```ts
// 默认在语句末尾需要加分号
export const name = 'ESLint'

export class Foo {
  // 默认在语句末尾需要加分号
  public bar = '1'
}
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
