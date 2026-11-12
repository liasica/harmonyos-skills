---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-misused-new
title: "@typescript-eslint/no-misused-new"
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-misused-new
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:55+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:f6665771b0a00affda3b4a94c934e2be043336ba996d471ef53730d15d6b242e
---

要求正确地定义“new”和“constructor”。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-misused-new": "error"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
export declare class C {
  public name: string;

  public constructor();
}
```

## 反例

```screen
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查（ArkTS/TS）](ide-code-linter.md)。
