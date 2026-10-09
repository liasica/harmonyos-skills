---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-hp-arkui-avoid-empty-callback
title: "@performance/hp-arkui-avoid-empty-callback"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-avoid-empty-callback
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:31+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:58300f7ede075bbec5958b254f3282b8fd455c8896df2e11cceac423f376d796
---

避免设置空的系统回调监听。

根据ArkUI编程规范，建议修改。

## 规则配置

```json
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

```ts
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

```ts
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

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
