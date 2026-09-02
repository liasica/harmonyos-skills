---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-no-state-var-access-in-loop
title: "@performance/hp-arkui-no-state-var-access-in-loop"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-no-state-var-access-in-loop
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:71b7deae74b7648ecf5b06753021c8ad78982017b9030488b247c84d6cdf5e09
---

避免在for、while等循环逻辑中频繁读取状态变量。

通用丢帧场景下，建议优先修改。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@performance/hp-arkui-no-state-var-access-in-loop": "warn",
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
import hilog from '@ohos.hilog'

@Entry
@Component
struct MyComponent{
  @State message: string = '';
  build() {
    Column() {
      Button('点击打印日志')
        .onClick(() => {
          this.message = 'click';
          let logMessage: string = this.message;
          for (let i = 0; i < 10; i++) {
            hilog.info(0x0000, 'TAG', '%{public}s', logMessage);
          }
        })
        .width('90%')
        .backgroundColor(Color.Blue)
        .fontColor(Color.White)
        .margin({
          top: 10
        })
    }
    .justifyContent(FlexAlign.Start)
    .alignItems(HorizontalAlign.Center)
    .margin({
      top: 15
    })
  }
}
```

## 反例

```screen
import hilog from '@ohos.hilog'
@Entry
@Component
struct MyComponent{
  @State message: string = '';
  build() {
    Column() {
      Button('点击打印日志')
        .onClick(() => {
          this.message = 'click';
          for (let i = 0; i < 10; i++) {
            hilog.info(0x0000, 'TAG', '%{public}s', this.message);
          }
        })
        .width('90%')
        .backgroundColor(Color.Blue)
        .fontColor(Color.White)
        .margin({
          top: 10
        })
    }
    .justifyContent(FlexAlign.Start)
    .alignItems(HorizontalAlign.Center)
    .margin({
      top: 15
    })
  }
}
```

## 规则集

```screen
plugin:@performance/recommended
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
