---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/multi-device-deployment-faqs-2
title: 折叠屏展开态直接打开应用与折叠后再打开应用字体大小不一致
breadcrumb: FAQ > 多设备场景 > 一次开发多端部署 > 折叠屏展开态直接打开应用与折叠后再打开应用字体大小不一致
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9234df66a8339943796697ca3bb1c989cc9b141b857b1192fa1a2712fbbfdc88
---

## 问题现象

折叠屏展开态打开应用和折叠态打开应用再展开，字体大小不一致。

## 背景知识

* [@State装饰器](../harmonyos-guides/arkts-state.md)：被@State装饰的变量称为状态变量，使普通变量具备状态属性。当状态变量改变时，会触发其直接绑定的UI组件渲染更新。
* [断点开发](../best-practices/bpta-multi-device-responsive-layout.md#section1532120147301)：可以将窗口宽度及窗口高宽比划分为不同的范围，称之为“断点”。当窗口宽度及窗口高宽比从一个断点变化到另一个断点时，改变页面布局（如将页面内容从单列排布调整为双列排布甚至三列排布等）以获得更好的显示效果。
* [on('windowSizeChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowsizechange7)：可监听窗口尺寸的变化，进行对应的回调操作。

## 问题定位

1. 排查页面代码中，文本字体大小是否是状态变量，以及初始化信息，例如下面代码。

   ```screen
   @State textFontSize: Resource | number | string = 15
   ```
2. 排查代码中，是否调用on('windowSizeChange')接口监听窗口的变化修改全局状态变量中的断点信息，例如下面代码。

   ```screen
   windowClass.on('windowSizeChange', (data) => {
     let uiContext: UIContext = windowClass.getUIContext()
     let widthBp: WidthBreakpoint = uiContext.getWindowWidthBreakpoint();
     AppStorage.setOrCreate('widthBp',widthBp)
   })
   ```
3. 排查代码中文本字体是否进行了断点适配，并判断md下的值与初始化的值是否相等，例如下面代码。

   ```screen
   // 三个值分别代表sm、md、lg下的值
   this.theFontSize = new BreakpointType('14fp', '16fp', '18fp').getValue(widthBp)
   ```

## 分析结论

应用在折叠屏展开态页面初始化时的字体大小与md断点下的值不一致，导致折叠屏展开态打开应用和折叠态打开应用再展开，字体大小不一致。

## 修改建议

修改代码中页面字体大小初始化逻辑，保证页面字体大小初始化时的值与对应断点下的值一致，这样就能保证折叠屏展开态打开应用和折叠态打开应用再展开，字体大小一致，代码样例如下。

```screen
import { window } from '@kit.ArkUI';
import { common } from '@kit.AbilityKit';

export class WidthBreakpointType<T> {
  sm: T;
  md: T;
  lg: T;

  constructor(sm: T, md: T, lg: T) {
    this.sm = sm;
    this.md = md;
    this.lg = lg;
  }

  getValue(widthBp: WidthBreakpoint): T {
    if (widthBp === WidthBreakpoint.WIDTH_XS || widthBp === WidthBreakpoint.WIDTH_SM) {
      return this.sm;
    }
    if (widthBp === WidthBreakpoint.WIDTH_MD) {
      return this.md;
    } else {
      return this.lg;
    }
  }
}

@Entry
@Component
struct TextSizePage {
  private message: string = 'Hello World';
  // 页面字体大小默认值
  @State theFontSize: Resource | number | string = 16;
  @StorageProp('widthBp') widthBp: WidthBreakpoint | undefined = AppStorage.get('widthBp');

  getWindow(): window.Window {
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    let windowStage = context.windowStage;
    let windowClass = windowStage.getMainWindowSync();
    return windowClass;
  }

  aboutToAppear(): void {
    // 按断点类型初始化页面字体大小
    if (this.widthBp) {
      this.theFontSize = new WidthBreakpointType('10fp', '16fp', '22fp').getValue(this.widthBp);
    }
    let windowClass: window.Window = this.getWindow();
    // 监听窗口尺寸的变化
    windowClass.on('windowSizeChange', () => {
      let uiContext: UIContext = windowClass.getUIContext();
      let widthBp: WidthBreakpoint = uiContext.getWindowWidthBreakpoint();
      // 改变应用全局状态变量中widthBp
      AppStorage.setOrCreate('widthBp', widthBp);
      // 根据窗口变化后的断点，改变页面字体大小
      if (this.widthBp) {
        this.theFontSize = new WidthBreakpointType('16fp', '22fp', '26fp').getValue(this.widthBp);
      }
    });
  }

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('TextSizePageHelloWorld')
        .fontSize(this.theFontSize)
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        });
    }
    .height('100%')
    .width('100%');
  }
}
```
