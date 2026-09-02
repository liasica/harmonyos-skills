---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hp-arkts-no-use-any-export-other
title: "@performance/hp-arkts-no-use-any-export-other"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkts-no-use-any-export-other
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:042065b2d50592dabec7e61f88ae682cf8c2f270ab05e598fb8e3a28e370fbfa
---

避免使用export \* 导出其他模块中定义的类型和数据。

冷启动完成时延场景下，建议优先修改。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@performance/hp-arkts-no-use-any-export-other": "warn",
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
// 当前文件 User.ets
// 从 Product.ets 文件中导出Product成员
export { Product } from './Product';
class User {
  id?: number;
  name?: string;
}
```

## 反例

```screen
// 当前文件 User.ets
// 从 Product.ets 文件中导出所有可导出的成员
export * from './Product';
// 从 Product.ets 文件中导出所有可导出的成员
export * as XX from './Product';
class User {
  id?: number;
  name?: string;
}
```

## 规则集

```screen
plugin:@performance/recommended
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
