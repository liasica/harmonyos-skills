---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-dark-color-mode-check
title: @performance/dark-color-mode-check
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:00+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f3d37d7844dd430182754741d6cff66c1169746f9fe4c7b36ebc9ffb7a24e3b0
---

通过启用深色模式，可以进一步实现能耗的降低。应用需要根据当前设备状态来适配深色模式。

说明

* 在检查整个工程时，该规则才生效。
* code-linter.json5配置文件中的[overrides](ide-code-linter.md#section19310459444)和[ignore](ide-code-linter.md#section19310459444)字段对该规则不生效。
* 若想关闭该规则检查，可将code-linter.json5配置文件中[rules](ide-code-linter.md#section19310459444)字段设置为off。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/dark-color-mode-check": "suggestion",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. src
2. ├── main
3. │   ├── ets
4. │   └── resources
5. │       └── dark
6. │           └── element
7. │               └── color.json
8. │
9. ├── mock
10. │   └── mock-config.json5
```

## 反例

```
1. src
2. ├── main
3. │   ├── ets
4. │   └── resources
5. │       └── dark
6. │           └── element
7. │
8. ├── mock
9. │   └── mock-config.json5
```

## 规则集

```
1. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
