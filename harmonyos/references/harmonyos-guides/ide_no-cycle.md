---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-cycle
title: "@security/no-cycle"
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 安全规则@security > @security/no-cycle
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:57+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:9ff854a8b1c582a394c56edf7053f8648a8987faec513e352e9742397b8109fc
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

该规则无需配置选项。

## 正例

```screen
// foo.ets
import {} from './bar';

// bar.ets
import {} from './index';
```

## 反例

```screen
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查（ArkTS/TS）](ide-code-linter.md)。
