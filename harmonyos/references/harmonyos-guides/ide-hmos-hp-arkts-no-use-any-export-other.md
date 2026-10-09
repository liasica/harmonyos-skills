---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-hp-arkts-no-use-any-export-other
title: "@performance/hp-arkts-no-use-any-export-other"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkts-no-use-any-export-other
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:31+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:8ef31a8e26e620233daa1d084ef9bd7e5f5038ac1516fc760bbcefa3afe96266
---

避免使用export \* 导出其他模块中定义的类型和数据。

冷启动完成时延场景下，建议优先修改。

## 规则配置

```json
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

```ts
// 当前文件 User.ets
// 从 Product.ets 文件中导出Product成员
export { Product } from './Product';
class User {
  id?: number;
  name?: string;
}
```

## 反例

```ts
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
