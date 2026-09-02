---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-tri-fold-1
title: 折叠屏折叠态，应用页面底部未避让导航栏
breadcrumb: FAQ > 多设备场景 > 手机 > 三折叠常见问题 > 折叠屏折叠态，应用页面底部未避让导航栏
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:48+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8a8ea43663bdc089fab99170f4d07cd653ebbcce115dfd5d5e05c92709ad52a1
---

## 问题现象

折叠屏折叠态时，应用页面底部按钮与导航栏重叠，导致无法点击该按钮。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/KD_s6N_UQvOHnh7i1NxWDA/zh-cn_image_0000002658910819.png "点击放大")

## 背景知识

* 使用[setWindowLayoutFullScreen](../harmonyos-references/arkts-apis-window-window.md#setwindowlayoutfullscreen9)方法可设置窗口为全屏模式，让页面的状态栏和导航栏区域背景可自定义，不为系统的默认底色。
* [getWindowAvoidArea](../harmonyos-references/js-apis-arkui-uiextension.md#getwindowavoidarea)可获取应用内容规避区域，如系统栏区域、刘海屏区域、手势区域、软键盘区域等与宿主窗口内容重叠时，需要宿主窗口内容避让的区域。

## 问题定位

全局检索setWindowLayoutFullScreen，应用通过setWindowLayoutFullScreen配置了全屏模式，且未设置padding避让导航栏和状态栏。

```screen
@Entry
@Component
struct WebComponent {

  aboutToAppear(): void {
    let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
    window.getLastWindow(context).then((lastWindow) => {
      lastWindow.setWindowLayoutFullScreen(true); // 设置全屏
    });
  }

  build() {
    Column() {
      // 页面内容
    }
    // 未设置padding避让导航栏和状态栏
  }
}
```

## 分析结论

为了实现沉浸式效果，应用开启了全屏模式，但是未动态避让状态栏和导航栏，导致内容与导航栏重叠，无法点击到页面上的点击按钮。

## 修改建议

在开启全屏模式后，通过padding避让状态栏和导航栏。

```screen
import { TipsDialog, window } from '@kit.ArkUI';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct AvoidArea {
  dialogController: CustomDialogController = new CustomDialogController({
    builder: TipsDialog({
      content: '是否确认无误',
      primaryButton: {
        value: '取消',
        action: () => {
          this.dialogController.close();
        },
      },
      secondaryButton: {
        value: '确定',
        role: ButtonRole.ERROR,
        action: () => {
          this.dialogController.close();
        }
      }
    }),
  });
  @State statusHeight: number = 0;
  @State navigationHeight: number = 0;

  aboutToAppear(): void {
    let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
    window.getLastWindow(context).then((lastWindow) => {
      lastWindow.setWindowLayoutFullScreen(true); // 设置全屏
      this.statusHeight = lastWindow.getWindowAvoidArea(window.AvoidAreaType.TYPE_SYSTEM).topRect.height; // 获取状态栏高度
      this.navigationHeight =
        lastWindow.getWindowAvoidArea(window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR).bottomRect.height; // 获取导航栏高度
    });
  }

  build() {
    Column() {
      TextInput({ placeholder: '请输入内容' })
        .width('80%')
        .height(40)
        .borderRadius('50%')
        .margin({ bottom: 350 });

      Button('确认')
        .height(30)
        .width(90)
        .borderRadius('50%')
        .backgroundColor('#0A59F7')
        .margin({ bottom: 2 })
        .onClick(() => {
          this.dialogController.open();
        });
    }
    .height('100%')
    .width('100%')
    .justifyContent(FlexAlign.End)
    .padding({ top: this.statusHeight + 'px', bottom: this.navigationHeight + 'px' }); // 设置padding避让导航栏和状态栏
  }
}
```

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/-su2obBcQb2XG-JPIWgRew/zh-cn_image_0000002628391610.png "点击放大")
