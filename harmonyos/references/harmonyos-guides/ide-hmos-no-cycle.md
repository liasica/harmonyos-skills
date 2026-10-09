---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-no-cycle
title: "@security/no-cycle"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 安全规则@security > @security/no-cycle
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:31+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:ad5a16f1a1fe9f8af165192050dbd8106624e9288a7839ef4c034f3ecfed2a5e
---

该规则禁止使用循环依赖。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@security/no-cycle": "error"
  }
}
```

## 选项

该规则无需配置额外选项。

## 正例

```ts
// foo.ets
import {} from './bar';

// bar.ets
import {} from './index';
```

## 反例

```ts
// foo.ets
import {} from './bar';

// bar.ets
import {} from './foo';
```

**说明** 

反例中foo.ets文件依赖了bar.ets文件，bar.ets文件同时依赖了foo.ets文件，造成了循环依赖。

## 规则集

```screen
plugin:@security/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
