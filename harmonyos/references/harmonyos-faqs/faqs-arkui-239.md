---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-239
title: 如何获取设备屏幕横竖屏状态
breadcrumb: FAQ > 应用框架开发 > UI框架 > 屏幕管理 > 如何获取设备屏幕横竖屏状态
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:13+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b4f6f48ff439769cbbf068f0c389c18345837569abedb7e03ab2f7f1abbf5543
---

方法一：利用媒体查询

```screen
import { mediaquery, UIContext } from '@kit.ArkUI';

// Store context in EntryAbility
const context = AppStorage.get("context") as UIContext;
let listener = context.getMediaQuery().matchMediaSync('(orientation: landscape)'); // Listen to landscape events
function onPortrait(mediaQueryResult: mediaquery.MediaQueryResult) {
  console.info('mediaQueryResult.matches:' + mediaQueryResult.matches)
  if (mediaQueryResult.matches) {
    // do something here
  } else {
    // do something here
  }
}
listener.on('change', onPortrait) // Register callback
listener.off('change', onPortrait) // Unregister callback

@Entry
@Component
struct Index {
  build() {
    Column() {
      Column() {
        Text('test')
      }
      .width('100%')
    }
    .height('100%')
    .width('100%')
    .justifyContent(FlexAlign.End)
  }
}
```

方法二：

可通过[display.getDefaultDisplaySync](../harmonyos-references/js-apis-display.md#displaygetdefaultdisplaysync9)方法获取到[Display](../harmonyos-references/js-apis-display.md#display)实例，再通过此实例获取其rotation属性即可获取屏幕横竖屏状态。

```ts
import { display, window } from '@kit.ArkUI';

@Entry
@Component
struct WindowRotation {
  build() {
    Text("Scroll Area")
      .width("100%")
      .height("100%")
      .backgroundColor(0X330000FF)
      .fontSize(16)
      .textAlign(TextAlign.Center)
      .onClick(() => {
        window.getLastWindow(this.getUIContext().getHostContext(), (err, win) => {
          let cutOutInfo = win.getWindowAvoidArea(window.AvoidAreaType.TYPE_SYSTEM_GESTURE)
          console.log(JSON.stringify(cutOutInfo))
          if (window.Orientation.AUTO_ROTATION) {
            let rotation: number = display.getDefaultDisplaySync().orientation // Get current screen orientation enum value
            console.log('' + rotation);
            if (rotation == 0) {
              console.log("CutOutInfo Portrait data: " + JSON.stringify(cutOutInfo));
            } else if (rotation == 1) {
              console.log("CutOutInfo Landscape data: " + JSON.stringify(cutOutInfo));
            } else if (rotation == 2) {
              console.log("CutOutInfo Reverse portrait data: " + JSON.stringify(cutOutInfo));
            } else {
              console.log("CutOutInfo Reverse landscape data: " + JSON.stringify(cutOutInfo));
            }
          }
        })
      })
  }
}
```
