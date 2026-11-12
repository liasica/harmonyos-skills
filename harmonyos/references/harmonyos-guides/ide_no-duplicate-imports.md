---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-duplicate-imports
title: "@typescript-eslint/no-duplicate-imports"
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 通用规则@typescript-eslint > @typescript-eslint/no-duplicate-imports
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:55+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:cc36a4efe651ff81657ffb2065d28c1be948f1a0655c3fdf24fa9581bcbeb87d
---

禁止重复的模块导入。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-duplicate-imports": "error"
  }
}
```

## 选项

详情请参考[eslint/no-duplicate-imports选项](https://eslint.nodejs.cn/docs/latest/rules/no-duplicate-imports#选项)。

## 正例

```screen
// foo和bar代表两个文件
import { foo } from './foo';
import bar from './bar';
```

## 反例

```screen
// foo代表文件
import { foo } from './foo';
import { bar } from './foo';
```

## 规则集

```screen
plugin:@typescript-eslint/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查（ArkTS/TS）](ide-code-linter.md)。
