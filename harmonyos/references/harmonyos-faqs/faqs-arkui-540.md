---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-540
title: 全屏播放视频时，页面布局发生短暂错位
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 全屏播放视频时，页面布局发生短暂错位
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:13+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8c042a6e845255aad60bc0580b7c6afd662ec304d9af8aa30b3cea9df9a71d5e
---

## 问题现象

视频切换至全屏播放时，页面出现短暂的布局错位的问题。

## 背景知识

* [setWindowLayoutFullScreen](../harmonyos-references/arkts-apis-window-window.md#setwindowlayoutfullscreen9)：设置主窗口或子窗口的布局是否为沉浸式布局，使用Promise异步回调。
* [setPreferredOrientation](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)：设置主窗口的显示方向属性，使用callback异步回调。
* [async/await](../harmonyos-guides/async-concurrency-overview.md#asyncawait)：async/await是一种用于处理异步操作的Promise语法糖，使得编写异步代码变得更加简单和易读。通过使用async关键字声明一个函数为异步函数，并使用await关键字等待Promise的解析（完成或拒绝），以同步的方式编写异步操作的代码。

## 问题定位

全局搜索setPreferredOrientation方法和setWindowLayoutFullScreen方法，发现设置了横竖屏后，又异步设置了沉浸式布局，这会导致WebView在横竖屏切换时未完成重绘，出现短暂布局错位。

```screen
async changeOrientation(orientation: window.Orientation) {
    if (!this.windowClass) {
      return;
    }
    this.windowClass.setPreferredOrientation(orientation); // 设置横竖屏
    if (orientation === window.Orientation.LANDSCAPE) {
       this.windowClass.setWindowLayoutFullScreen(true);
    } else {
       this.windowClass.setWindowLayoutFullScreen(false);
    }
  }
```

## 分析结论

setWindowLayoutFullScreen与setPreferredOrientation的异步执行存在时序冲突，造成布局短暂错位的问题。

## 修改建议

1. 在EntryAbility.ets中获取并保存windowClass。

   ```screen
   import { UIAbility } from '@kit.AbilityKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { window } from '@kit.ArkUI';

   const DOMAIN = 0x0000;

   export default class EntryAbility extends UIAbility {
     onDestroy(): void {
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
     }

     onWindowStageCreate(windowStage: window.WindowStage): void {
       // Main window is created, set main page for this ability
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
       windowStage.loadContent('pages/Index', (err) => {
         if (err.code) {
           return;
         }
         let windowClass: window.Window = windowStage.getMainWindowSync();
         AppStorage.setOrCreate('windowClass', windowClass);
         hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
       });
     }

     onWindowStageDestroy(): void {
       // Main window is destroyed, release UI related resources
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
     }

     onForeground(): void {
       // Ability has brought to foreground
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onForeground');
     }

     onBackground(): void {
       // Ability has back to background
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
     }
   };
   ```
2. 在Page1.ets中使用await优化执行时序，方向切换完成后再设置全屏，并通过给Web组件注入方法，把本地RawFile中的视频拷贝到沙箱播放。

   ```screen
   import { display, window } from '@kit.ArkUI';
   import { fileIo } from '@kit.CoreFileKit';
   import fs from '@ohos.file.fs';
   import { webview } from '@kit.ArkWeb';

   let context: Context | undefined = undefined;
   let uicontext: UIContext | undefined = undefined;

   class SourceUtil {
     screenWidth() {
       let dis = display.getDefaultDisplaySync();
       if (uicontext) {
         return uicontext?.px2vp(dis.width) * 0.85;
       }
       return 0;
     }

     chosePicture() {
       // 获取应用上下文和资源管理器
       if (!context) {
         return;
       }
       let resMgr = context.resourceManager;
       // 读取应用资源
       try {
         const resource = resMgr.getRawFileContentSync('video.mp4');
         // 获取沙箱路径
         const targetPath = context.filesDir + '/' + 'video.mp4';
         // 创建写入流
         const file = fs.openSync(targetPath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
         // 写入文件
         try {
           fileIo.writeSync(file.fd, resource.buffer);
         } finally {
           fileIo.closeSync(file);
         }
       } catch (error) {
         console.info('error==', error);
       }
       return context.filesDir + '/video.mp4';
     }
   }

   @Entry
   @Component
   struct Page1 {
     private windowClass: window.Window | undefined = AppStorage.get('windowClass');
     private cusAspectRatio: number = 0;
     webviewController: webview.WebviewController = new webview.WebviewController();
     @State sourceUtil: SourceUtil = new SourceUtil();
     @State webWidth: string = '85%';

     async changeOrientation(orientation: window.Orientation) {
       if (!this.windowClass) {
         return;
       }
       if (orientation === window.Orientation.LANDSCAPE) {
         this.webWidth = '100%';
         await this.windowClass.setWindowLayoutFullScreen(true);
       } else {
         this.webWidth = '85%';
         await this.windowClass.setWindowLayoutFullScreen(false);
       }
       this.windowClass.setPreferredOrientation(orientation);
     }

     aboutToAppear(): void {
       context = this.getUIContext().getHostContext();
       uicontext = this.getUIContext();
     }

     build() {
       RelativeContainer() {
         Web({ src: $rawfile('index.html'), controller: this.webviewController })
           .fileAccess(true)
           .geolocationAccess(false)
           .javaScriptProxy({
             object: this.sourceUtil,
             name: 'picture',
             methodList: ['chosePicture', 'screenWidth'],
             controller: this.webviewController
           })
           .alignRules({
             center: { anchor: '__container__', align: VerticalAlign.Center },
             middle: { anchor: '__container__', align: HorizontalAlign.Center }
           })
           .height('100%')
           .width(this.webWidth)
           .onFullScreenEnter(() => {
             this.changeOrientation(window.Orientation.LANDSCAPE);
           })
           .onFullScreenExit(() => {
             this.changeOrientation(window.Orientation.PORTRAIT);
           });
       }
       .aspectRatio(this.cusAspectRatio)
       .height('100%')
       .width('100%');
     }
   }
   ```
3. 在index.html中播放本地视频。

   ```screen
   <!DOCTYPE html>
   <html>
   <head>
       <meta charset="UTF-8"/>
       <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
   </head>
   <script>
       function takePicture() {
          let s = picture.chosePicture();
          document.getElementById('myImage').src = "file:///data/storage/el2/base/haps/entry/files/video.mp4";
           document.getElementById('myImage').width = picture.screenWidth()
       }

          document.addEventListener("DOMContentLoaded",takePicture)
   </script>
   <body>
   <video src="" id="myImage"  height="240" controls loop autoplay>
   </video>

   </body>
   </html>
   ```
