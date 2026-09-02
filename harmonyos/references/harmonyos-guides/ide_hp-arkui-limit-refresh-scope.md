---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-limit-refresh-scope
title: "@performance/hp-arkui-limit-refresh-scope（已下线）"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-limit-refresh-scope（已下线）
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:85091c73f5eb62f0b835d73da2e2f3a427cf29d0ed68e3e658055039cd2d660b
---

建议减少组件刷新范围。该规则已于5.0.3.500版本下线。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@performance/hp-arkui-limit-refresh-scope": "suggestion",
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
@Entry
@Component
struct StackExample6 {
  @State isVisible : boolean = false;
  build() {
    Column() {
      Stack({alignContent: Alignment.Top}) {
        Text().width('100%').height('70%').backgroundColor(0xd2cab3)
          .align(Alignment.Center).textAlign(TextAlign.Center);
        // 此处省略100个相同的背景Text组件
        Stack() {
          if (this.isVisible) {
            Text('New Page').height("70%").backgroundColor(0xd2cab3)
              .align(Alignment.Center).textAlign(TextAlign.Center);
          }
        }.width('100%').height('70%')
      }
      Button("press").onClick(() => {
        this.isVisible = !(this.isVisible);
      })
    }
  }
}
```

## 反例

```screen
@Entry
@Component
struct StackExample5 {
  @State isVisible : boolean = false;
  build() {
    Column() {
      Stack({alignContent: Alignment.Top}) {
        Text().width('100%').height('70%').backgroundColor(0xd2cab3)
          .align(Alignment.Center).textAlign(TextAlign.Center);
        // 此处省略100个相同的背景Text组件
        if (this.isVisible) {
          Text('New Page').height("70%").backgroundColor(0xd2cab3)
            .align(Alignment.Center).textAlign(TextAlign.Center);
        }
      }
      Button("press").onClick(() => {
        this.isVisible = !(this.isVisible);
      })
    }
  }
}
```

## 规则集

```screen
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
