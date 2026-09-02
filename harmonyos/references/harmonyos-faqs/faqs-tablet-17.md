---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-tablet-17
title: 平板全屏播放视频时下方标题仍然显示
breadcrumb: FAQ > 多设备场景 > 平板 > 常见问题 > 平板全屏播放视频时下方标题仍然显示
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:48+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a0cb8e369867b3443c5d6460ff8166f604f60b49239084fae93b05842f21ae1b
---

## 问题现象

平板上播放视频时，点击全屏播放后，视频下方仍然显示视频标题，视频未真正全屏播放。

## 背景知识

* 使用[Window.setWindowLayoutFullScreen()](../harmonyos-references/arkts-apis-window-window.md#setwindowlayoutfullscreen9)设置窗口为全屏模式，应用页面会延伸到状态栏和导航栏。
* 使用[Window.setWindowSystemBarEnable()](../harmonyos-references/arkts-apis-window-window.md#setwindowsystembarenable9)或[Window.setSpecificSystemBarEnabled()](../harmonyos-references/arkts-apis-window-window.md#setspecificsystembarenabled11)方法设置状态栏和导航栏的显隐。
* 使用setWindowLayoutFullScreen(true)方法设置窗口为全屏模式，页面布局会拓展到顶部状态栏及底部导航栏，此时部分布局会被遮挡。通过[getWindowAvoidArea()](../harmonyos-references/arkts-apis-window-window.md#getwindowavoidarea9)接口以及[on('avoidAreaChange')](../harmonyos-references/arkts-apis-window-window.md#onavoidareachange9)接口获取到系统避让区高度，据此在页面顶部及底部使用padding属性避让状态栏和导航栏。

## 问题定位

1. 根据问题现象，页面内容拓展到了底部导航栏，标题被导航栏遮挡，判断应用使用了setWindowLayoutFullScreen(true)方法设置窗口为沉浸式，可以应用中全局搜索该方法进行确认。
2. 视频全屏播放时，导航栏还存在，可以尝试在视频播放页面搜索setWindowSystemBarEnable和setSpecificSystemBarEnabled方法，确认有无设置导航栏为隐藏状态。
3. 视频全屏播放时，避让了下方部分区域，判断视频组件中设置了避让属性导致了这一现象，可以尝试在视频播放页面搜索避让属性padding进行确认。

## 分析结论

应用在全屏播放视频时设置了沉浸式，同时设置了播放组件避让导航栏安全区域，并且没有设置导航栏的显隐状态为隐藏，导致了如上问题的发生。

## 修改建议

1. 在全屏播放页面查找避让导航栏安全区域的padding属性并去除。
2. 在全屏播放页面显示或隐藏时，设置导航栏状态显示或隐藏。

   ```screen
   import { BusinessError } from '@kit.BasicServicesKit';
   import { window } from '@kit.ArkUI';

   @Entry
   @Component
   struct Index {
     isFullScreen: boolean = false;
     private context = this.getUIContext().getHostContext();
     windowClass: window.Window | undefined = undefined;
     @State ButtonMsg: string = '沉浸式全屏';

     aboutToAppear(): void {
       window.getLastWindow(this.context, (err: BusinessError, window) => {
         this.windowClass = window;
         console.error(`failed to getLastWindow successfully errCode is: ${err.code}, ${err.message}`);
       });
     }

     // 进入全屏
     enterFullscreen() {
       if (this.windowClass != undefined) {
         this.windowClass.setWindowLayoutFullScreen(!this.isFullScreen);
         this.windowClass.setWindowSystemBarEnable([]);
         this.isFullScreen = !this.isFullScreen;
       }
     }

     // 退出全屏
     exitFullscreen() {
       if (this.windowClass != undefined) {
         this.windowClass.setWindowLayoutFullScreen(!this.isFullScreen);
         this.windowClass.setWindowSystemBarEnable(['status', 'navigation']);
         this.isFullScreen = !this.isFullScreen;
       }
     }

     build() {
       Column() {
         Stack({ alignContent: Alignment.Center }) {
           Text('Window show')
             .backgroundColor(Color.Black)
             .fontColor(Color.White)
             .textAlign(TextAlign.Center)
             .height('100%')
             .width('100%');
           Button(this.ButtonMsg)
             .onClick(() => {
               if (this.isFullScreen) {
                 this.exitFullscreen();
                 this.ButtonMsg = '进入沉浸式';
               } else {
                 this.enterFullscreen();
                 this.ButtonMsg = '退出沉浸式';
               }
             });
         }
         .height('100%')
         .width('100%');
       }
       .width('100%')
       .height('100%');
     }
   }
   ```
