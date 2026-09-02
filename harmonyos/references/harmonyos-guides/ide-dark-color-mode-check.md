---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-dark-color-mode-check
title: "@performance/dark-color-mode-check"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/dark-color-mode-check
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:22+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d33899eb0f1c0c9a26eaa41afd6a31f61b1f6d7af8f0919a6c5d61fe743a239b
---

通过启用深色模式，可以进一步降低能耗。应用需要根据当前设备状态来适配深色模式。

**说明** 

* 在检查整个工程时，该规则才生效。
* code-linter.json5配置文件中的[overrides](ide-code-linter.md#section19310459444)和[ignore](ide-code-linter.md#section19310459444)字段对该规则不生效。
* 若想关闭该规则检查，可将code-linter.json5配置文件中[rules](ide-code-linter.md#section19310459444)字段设置为off。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@performance/dark-color-mode-check": "suggestion",
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
src
├── main  
│   ├── ets    
│   └── resources
│       └── dark    
│           └── element
│               └── color.json     
│           
├── mock
│   └── mock-config.json5
```

## 反例

```screen
src
├── main  
│   ├── ets    
│   └── resources
│       └── dark    
│           └── element
│           
├── mock
│   └── mock-config.json5
```

## 规则集

```screen
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
