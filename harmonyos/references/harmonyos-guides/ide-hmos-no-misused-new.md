---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-no-misused-new
title: "@typescript-eslint/no-misused-new"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-misused-new
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:29+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:dce103a30cf4356da22b8af23c73bc4f0c3e9014fffe476b155693d50b426656
---

要求正确地定义“new”和“constructor”。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-misused-new": "error"
  }
}
```

## 选项

该规则无需配置额外选项。

## 正例

```ts
export declare class C {
  public name: string;

  public constructor();
}
```

## 反例

```ts
export declare class C {
  // 应该定义为constructor(): C
  public new(): C;
}

export interface I {
  // 不应该定义constructor
  constructor(): void;
}
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
