---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-tablet-2
title: 平板设备上打开应用时，不显示状态栏
breadcrumb: FAQ > 多设备场景 > 平板 > 常见问题 > 平板设备上打开应用时，不显示状态栏
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:48+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c8c0d541f1411043632c8573cd6da095b2727e3251b62343b8b57bcf3812e46d
---

## 问题现象

当用户在平板设备上打开应用时，状态栏会不显示。

## 背景知识

* [setWindowSystemBarEnable](../harmonyos-references/arkts-apis-window-window.md#setwindowsystembarenable9)：设置主窗口状态栏、底部导航（根据用户设置，可表现为导航条或三键导航栏）的可见性模式，只有进入全屏主窗口才会生效。
* [setSpecificSystemBarEnabled](../harmonyos-references/arkts-apis-window-window.md#setspecificsystembarenabled11)：设置主窗口状态栏、底部导航区域的显示和隐藏，只有进入全屏主窗口才会生效。
* [setWindowLayoutFullScreen](../harmonyos-references/arkts-apis-window-window.md#setwindowlayoutfullscreen9)：设置主窗口或子窗口的布局是否为沉浸式布局，沉浸式布局生效时，布局不避让状态栏与底部导航区域，组件可能产生与其重叠的情况。

## 问题定位

1. 检查代码中，是否通过setWindowLayoutFullScreen设置了沉浸式布局。
2. 检查代码中，是否通过setWindowSystemBarEnable或者setSpecificSystemBarEnabled设置了状态栏不可见。

## 分析结论

应用开启沉浸式布局后，设置了状态栏的可见性模式为隐藏模式，导致在平板上应用状态栏不可见。

## 修改建议

目前系统提供了两种API，都可以控制状态栏的显示与隐藏。其中setWindowSystemBarEnable批量设置窗口所有系统栏的可见性，无法单独控制某个栏。setSpecificSystemBarEnabled支持精准控制单个系统栏的显隐状态（如只隐藏状态栏或导航条）。需要注意的是两种方式都需要在窗口为全屏模式才会生效，以下是setWindowSystemBarEnable的使用示例：

```ts
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct StatusExampleDemo {
  @State message: string = '测试状态栏的显示与隐藏';

  onPageShow(): void {
    try {
      let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      let windowStage = context.windowStage;
      let windowClass = windowStage.getMainWindowSync();
      let names: Array<'status' | 'navigation'> = ['status', 'navigation'];
      try {
        let promise = windowClass.setWindowSystemBarEnable(names);
        promise.then(() => {
          console.info('Succeeded in setting the system bar to be invisible.');
        }).catch((err: BusinessError) => {
          console.error(`Failed to set the system bar to be invisible. Cause code: ${err.code}, message: ${err.message}`);
        });
      } catch (exception) {
        console.error(`Failed to set the system bar to be invisible. Cause code: ${exception.code}, message: ${exception.message}`);
      }
    } catch (error) {
      // 异常处理逻辑
      console.error(`Get main window failed: ${error}`);
    }
  }

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('S2CFK20250616105528658955HelloWorld')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          this.message = 'Welcome';
        });
    }
    .height('100%')
    .width('100%');
  }
}
```
