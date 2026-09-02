---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-update-state-var-between-animatetos-check
title: "@performance/update-state-var-between-animatetos-check"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/update-state-var-between-animatetos-check
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d49f0f91bfe63019617e23b5c28867adac396fa70dc15df929ff277742943961
---

如果多个animateTo之间存在状态更新，会导致执行下一个animateTo之前又存在需要更新的脏节点，可能造成冗余更新。因此不建议在两次animateTo之间进行状态变量更新。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@performance/update-state-var-between-animatetos-check": "warn",
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
@Entry
@Component
struct UpdateMultipleProperties {
  @State w: number = 100
  @State h: number = 2
  @State color: Color = Color.Red
  build() {
    Column() {
      Column() {
        
        Button('Tap2')
          .width('100%')
          .margin({ top: 12 })
          .onClick(() => {
            let doTimes = 5;
            for (let i = 0; i < doTimes; i++) {
              setTimeout(() => {
                // Explicitly specify the initial values of all properties to be animated before the animation.
                this.w = 80
                this.color = Color.Yellow
                this.getUIContext().animateTo({ curve: Curve.Sharp, duration: 1000 }, () => {
                  this.w = (this.w === 80 ? 150 : 80);
                });
                this.getUIContext().animateTo({ curve: Curve.Linear, duration: 2000 }, () => {
                  this.color = (this.color === Color.Yellow ? Color.Red : Color.Yellow);
                });
                // Refresh non-animated properties after animation completes
                this.h = 5
              }, 2000 * i)
            }
          })
        Button('Tap3')
          .width('100%')
          .margin({ top: 12 })
          .onClick(() => {
            let doTimes = 5;
            for (let i = 0; i < doTimes; i++) {
              setTimeout(() => {
                this.getUIContext().animateTo({ curve: Curve.Sharp, duration: 1000 }, () => {
                  this.w = (this.w === 80 ? 150 : 80);
                });
                this.getUIContext().animateTo({ curve: Curve.Linear, duration: 2000 }, () => {
                  this.color = (this.color === Color.Yellow ? Color.Red : Color.Yellow);
                });
              }, 2000 * i)
            }
          })
      }
      .justifyContent(FlexAlign.End)
      .height('25%')
    }
    .padding({
      left: 16,
      right: 16,
      bottom: 16
    })
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Start)
  }
}
```

## 反例

```screen
@Entry
@Component
struct UpdateMultipleProperties {
  @State w: number = 100
  @State h: number = 2
  @State color: Color = Color.Red
  build() {
    Column() {
      Column() {
        Button('Tap1')
          .width('100%')
          .margin({ top: 12 })
          .onClick(() => {
            let doTimes = 5;
            for (let i = 0; i < doTimes; i++) {
              setTimeout(() => {
                this.w = 80
                this.h = 4
                this.getUIContext().animateTo({ curve: Curve.Sharp, duration: 1000 }, () => {
                  this.w = (this.w === 80 ? 150 : 80);
                });
                // Updating state variables between two animateTo calls
                this.color = Color.Yellow
                this.getUIContext().animateTo({ curve: Curve.Linear, duration: 2000 }, () => {
                  this.color = (this.color === Color.Yellow ? Color.Red : Color.Yellow);
                });
              }, 2000 * i)
            }
          })
      }
      .justifyContent(FlexAlign.End)
      .height('25%')
    }
    .padding({
      left: 16,
      right: 16,
      bottom: 16
    })
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Start)
  }
}
```

## 规则集

```screen
plugin:@performance/recommended
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
