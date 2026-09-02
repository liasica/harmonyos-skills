---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-cycle
title: "@security/no-cycle"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 安全规则@security > @security/no-cycle
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:22+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4dfa9dac28b8d905ca73effd0b7d31265be024e0d6e65259963249f4f22d03c5
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
