---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hp-arkui-remove-redundant-state-var
title: "@performance/hp-arkui-remove-redundant-state-var"
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-remove-redundant-state-var
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:58+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:53842840aa3bf319569ec4f0c082632c1c45763737f8d4094cde57410aaf3e33
---

建议移除不关联UI组件的状态变量设置。

通用丢帧场景下，建议优先修改。

## 规则配置

```screen
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

```screen
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

```screen
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

```screen
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查（ArkTS/TS）](ide-code-linter.md)。
