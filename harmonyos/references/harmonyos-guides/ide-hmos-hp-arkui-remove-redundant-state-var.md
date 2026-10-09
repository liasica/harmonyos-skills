---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-hp-arkui-remove-redundant-state-var
title: "@performance/hp-arkui-remove-redundant-state-var"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-remove-redundant-state-var
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:31+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:b5556c8f65b1dfcd4f86795756e768ef3d68f1aa048c9b777b98381bef450d7f
---

建议移除不关联UI组件的状态变量设置。

通用丢帧场景下，建议优先修改。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@performance/hp-arkui-remove-redundant-state-var": "suggestion",
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```ts
@Entry
@Component
struct MyComponent {
  @State message: string = "";

  appendMsg(newMsg: string): string {
    this.message += newMsg;
    return this.message;
  }

  build() {
    Column() {
      Stack() {
        Text(this.message)
      }
      .backgroundColor("black")
      .width(200)
      .height(400)

      Button("move")
    }
  }
}
```

## 反例

```ts
@Entry
@Component
struct MyComponent {
  @State message: string = "";

  appendMsg(newMsg: string): string {
    this.message += newMsg;
    return this.message;
  }

  build() {
    Column() {
      Stack() {
      }
      .backgroundColor("black")
      .width(200)
      .height(400)

      Button("move")
    }
  }
}
```

## 规则集

```json
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
