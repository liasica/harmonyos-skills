---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-hp-arkts-no-use-any-export-current
title: "@performance/hp-arkts-no-use-any-export-current"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkts-no-use-any-export-current
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:31+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:210a60b6abdba4b2132cb409e212a3ec52413111d315a9bec20214905146d2d3
---

避免使用export \* 导出当前module中定义的类型和数据。

冷启动完成时延场景下，建议优先修改。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@performance/hp-arkts-no-use-any-export-current": "warn",
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```ts
export class User {
  id?: number;
  name?: string;
}
```

## 反例

```ts
class User {
  id?: number;
  name?: string;
}
// 当前文件 User.ets
export * from './User';
// 当前文件 User.ets
export * as XX from './User';
```

## 规则集

```json
plugin:@performance/recommended
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
