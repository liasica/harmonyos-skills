---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-redundant-dependency-check
title: "@correctness/redundant-dependency-check"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 正确性规则@correctness > @correctness/redundant-dependency-check
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:70edfe65c0e7fd7274e76235723df9948bd7dcf0b9fc4034a6d04d671b536ee8
---

建议删除冗余的依赖配置。冗余依赖会增加加载和解析时间，影响代码质量。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@correctness/redundant-dependency-check": "suggestion"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

1. 在entry下的oh-package.json5文件中配置了a、b、c三个依赖，entry/src/main/ets中的文件中全部导入。

2. 在工程级的oh-package.json5文件中配置了a、b、c三个依赖，整个工程全部导入。

## 反例

1. 在entry下的oh-package.json5文件中配置了a、b、c三个依赖，但entry/src/main/ets中的文件中只导入了a和b两个依赖。

2. 在工程级的oh-package.json5文件中配置了a、b、c三个依赖，但整个工程只导入了a,b两个依赖。

## 规则集

```screen
plugin:@correctness/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
