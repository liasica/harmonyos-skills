---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hp-arkts-no-use-any-export-current
title: "@performance/hp-arkts-no-use-any-export-current"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkts-no-use-any-export-current
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:99b93f2c44cb4ca25494937f0ccc959de61f3641c463bbe36ac09b2a2ff82d26
---

避免使用export \* 导出当前module中定义的类型和数据。

冷启动完成时延场景下，建议优先修改。

## 规则配置

```screen
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

```screen
export class User {
  id?: number;
  name?: string;
}
```

## 反例

```screen
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

```screen
plugin:@performance/recommended
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
