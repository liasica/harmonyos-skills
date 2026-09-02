---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-start-window-icon-check
title: "@performance/start-window-icon-check"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/start-window-icon-check
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:23+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:cf449bd5c2340876bb85d4aca293eb44e506c56bf018fe3bc59902ae5aea4c71
---

启动页图标分辨率建议不超过256 \* 256，[冷启动响应时延场景](../best-practices/bpta-application-cold-start-optimization.md#section5953164714132)下，建议优先修改。

**说明** 

* 在检查整个工程时，该规则才生效。
* code-linter.json5配置文件中的[overrides](ide-code-linter.md#section19310459444)和[ignore](ide-code-linter.md#section19310459444)字段对该规则不生效。
* 若想关闭该规则检查，可将code-linter.json5配置文件中[rules](ide-code-linter.md#section19310459444)字段设置为off。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@performance/start-window-icon-check": "suggestion",
  }
}
```

## 选项

该规则无需配置选项。

## 正例

1、entry/src/main/module.json5中的mainElement对应的ability中配置了startWindowIcon

2、entry/src/main/resources/base/media目录下对应的图片文件分辨率小于等于256\*256

## 反例

1、entry/src/main/module.json5中的mainElement对应的ability中配置了startWindowIcon

2、entry/src/main/resources/base/media目录下对应的图片文件分辨率大于256\*256

## 规则集

```screen
plugin:@performance/recommended
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
