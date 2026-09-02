---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-use-transition-to-replace-animateto
title: "@performance/hp-arkui-use-transition-to-replace-animateto"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-use-transition-to-replace-animateto
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b7f7367a671b50b903f2d42627be2c509bb40bc8ab1f7ff97a127d6c0a67a6ba
---

建议组件转场动画使用transition。

动效丢帧场景下，建议优先修改。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@performance/hp-arkui-use-transition-to-replace-animateto": "warn",
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
  @State show: boolean = true;

  build() {
    Column() {
      Row() {
        if (this.show) {
          Text('value')
            // Set id to make transition interruptible
            .id('myText')
            .transition(TransitionEffect.OPACITY.animation({ duration: 1000 }))
        }
      }.width('100%')
      .height(100)
      .justifyContent(FlexAlign.Center)
      Text('toggle state')
        .onClick(() => {
          // Through transition, animates the appearance or disappearance of transparency.
          this.show = !this.show;
        })
    }
  }
}
```

## 反例

```screen
@Entry
@Component
struct MyComponent {
  @State mOpacity: number = 1;
  @State show: boolean = true;

  build() {
    Column() {
      Row() {
        if (this.show) {
          Text('value')
            .opacity(this.mOpacity)
        }
      }
      .width('100%')
      .height(100)
      .justifyContent(FlexAlign.Center)

      Text('toggle state')
        .onClick(() => {
          this.show = true;
          animateTo({
            duration: 1000, onFinish: () => {
              if (this.mOpacity === 0) {
                this.show = false;
              }
            }
          }, () => {
            this.mOpacity = this.mOpacity === 1 ? 0 : 1;
          })
        })
    }
  }
}
```

## 规则集

```screen
plugin:@performance/recommended
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
