---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-avoid-empty-callback
title: "@performance/hp-arkui-avoid-empty-callback"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-avoid-empty-callback
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5d1841f1a7fd4ae4e746760c5c453dc29e926f98472ec0a31a33e34296886265
---

避免设置空的系统回调监听。

根据ArkUI编程规范，建议修改。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@performance/hp-arkui-avoid-empty-callback": "suggestion",
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
@Component
struct MyComponent {
  doSomething() {
    //业务逻辑
  }

  build() {
    Button('Click', { type: ButtonType.Normal, stateEffect: true })
      .onClick(() => {
        this.doSomething()
      })
  }
}
```

## 反例

```screen
@Component
struct MyComponent {
  build() {
    Button('Click', { type: ButtonType.Normal, stateEffect: true })
      .onClick(() => {
        // 无业务逻辑
      })
  }
}
```

## 规则集

```screen
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
