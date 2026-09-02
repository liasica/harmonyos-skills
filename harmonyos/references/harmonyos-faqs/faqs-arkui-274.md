---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-274
title: 如何完成挖孔屏的适配
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何完成挖孔屏的适配
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:28+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:65b38c96538374acabf6279429373076c573a8fda5a0b538ecb1fd9d4254f2f9
---

1. 使用setWindowLayoutFullScreen和setWindowSystemBarEnable将窗口设置为全屏并隐藏顶部状态栏。

   ```ts
   onWindowStageCreate(windowStage: window.WindowStage): void {
     AppStorage.setOrCreate('context', this.context);
     windowStage.getMainWindow((err: BusinessError, window: window.Window) => {
       // The settings window is displayed in full screen
       window.setWindowLayoutFullScreen(true)
         .then(() => {
           console.info('Succeeded in setting the window layout to full-screen mode.');
         }).catch((err: BusinessError) => {
         console.error(`Failed to set the window layout to full-screen mode. Cause code: ${err.code}, message: ${err.message}`);
       });
       // Set the top status bar to be hidden
       let names: Array<'status' | 'navigation'> = [];
       window.setWindowSystemBarEnable(names)
         .then(() => {
           console.info('Succeeded in setting the system bar to be invisible.');
         }).catch((err: BusinessError) => {
         console.error(`Failed to set the system bar to be invisible. Cause code: ${err.code}, message: ${err.message}`);
       });
     })
     // ...
   }
   ```
2. 使用getDefaultDisplaySync获取同步display对象，再通过其异步方法getCutoutInfo回调获取挖孔区域信息，然后根据这些信息计算偏移量，实现对不可用区域的适配。

   ```ts
   import { display, window } from '@kit.ArkUI';
   import { common } from '@kit.AbilityKit';
   import { BusinessError, batteryInfo } from '@kit.BasicServicesKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';

   class TextMargin {
     left: number = 0; // Status bar left offset
     right: number = 0; // Status bar right offset
   }

   @Entry
   @Component
   struct Index {
     @State date: Date = new Date();
     @State currentTime: string = ''; // Top status bar time
     @State boundingRect: display.Rect[] = []; // Unavailable area data
     @State screenWidth: number = 0; // Screen width
     @State displayClass: display.Display | null = null;
     @State topTextMargin: TextMargin = { left: 0, right: 0 }; // Top status bar offset
     @StorageLink('context') context: common.UIAbilityContext | undefined = AppStorage.get('context'); // Get UIAbilityContext

     aboutToAppear(): void {
       try {
         this.displayClass = display.getDefaultDisplaySync();
         display.getDefaultDisplaySync().getCutoutInfo((err, data) => {
           if (err.code) {
             console.log('getCutoutInfo failed. error is:', JSON.stringify(err));
             return;
           }
           this.boundingRect = data.boundingRects;
           this.topTextMargin = this.getBoundingRectPosition();
         })
       } catch (error) {
         let err = error as BusinessError;
         hilog.error(0x000, 'testTag', `err.code=${err.code}, err.message=${err.message}`);
       }
       // Get hour
       let hours = this.date.getHours();
       // Get minute
       let minutes = this.date.getMinutes();
       // Add 0 before minute if less than 10
       this.currentTime = hours.toString() + ':' + (minutes < 10 ? '0' + minutes : minutes.toString());
     }

     // Reset window to initial state when leaving the page
     aboutToDisappear() {
       if (this.context !== undefined) {
         window.getLastWindow(this.context, async (err, data) => {
           if (err.code) {
             console.log('getLastWindow failed. error is:', JSON.stringify(err));
             return;
           }
           data.setWindowSystemBarEnable(['status', 'navigation'])
             .then(() => {
               hilog.info(0x000, 'testTag', `setWindowSystemBarEnable succeed.`);
             })
             .catch((err: BusinessError) => {
               hilog.error(0x000, 'testTag',
                 `setWindowSystemBarEnable failed. err.code=${err.code}, err.message=${err.message}`);
             })
           data.setWindowLayoutFullScreen(false)
             .then(() => {
               hilog.info(0x000, 'testTag', `setWindowLayoutFullScreen succeed.`);
             })
             .catch((err: BusinessError) => {
               hilog.error(0x000, 'testTag',
                 `setWindowLayoutFullScreen failed. err.code=${err.code}, err.message=${err.message}`);
             })
         })
       }
     }

     /**
      * Calculate the left and right margins of the unusable areas of the punch hole screen
      * @returns {TextMargin} Objects that include left/right offsets
      */
     getBoundingRectPosition(): TextMargin {
       if (this.boundingRect !== null && this.displayClass !== null && this.boundingRect[0] !== undefined) {
         // Distance from the right of the unavailable area to the right edge of the screen: screen width minus left width and unavailable area width
         let boundingRectRight: number =
           this.displayClass.width - (this.boundingRect[0].left + this.boundingRect[0].width);
         // Distance from the left of the unavailable area to the left edge of the screen: can be obtained directly by getCutoutInfo
         let boundingRectLeft: number = this.boundingRect[0].left;
         // For some devices, if the unavailable area is in the middle, the difference between the left and right distances is less than 10 pixels, treat it as being in the middle
         if (Math.abs(boundingRectLeft - boundingRectRight) <= 10) {
           return { left: 0, right: 0 };
         }
         if (boundingRectLeft > boundingRectRight) {
           // Unavailable area on the right
           return { left: 0, right: this.displayClass.width - boundingRectLeft };
         } else if (boundingRectLeft < boundingRectRight) {
           // Unavailable area on the left
           return { left: this.boundingRect[0].left + this.boundingRect[0].width, right: 0 };
         }
       }
       return { left: 0, right: 0 };
     }

     build() {
       Stack() {
         Image($r('app.media.digging_hole_screen_2048game'))
           .objectFit(ImageFit.Fill)
           .width('100%')
           .height('100%')
           .onClick(() => {
             try {
               this.getUIContext().getPromptAction().showToast({
                 message: 'This function is not yet developed',
                 duration: 2000
               })
             } catch (error) {
               let err = error as BusinessError;
               hilog.error(0x000, 'testTag', `showToast failed. err.code=${err.code}, err.message=${err.message}`);
             }
           })
         Column() {
           Flex({ direction: FlexDirection.Row, justifyContent: FlexAlign.SpaceBetween }) {
             Text(this.currentTime) // Time
               .fontSize(16)
               .fontColor(Color.Black)
               .fontWeight(FontWeight.Regular)
               .padding({ left: 12 })
               .margin({
                 left: this.getUIContext().px2vp(this.topTextMargin.left),
                 top: 14
               }) // The obtained offset is in px and needs to be converted
             Text(batteryInfo.batterySOC.toString() + '%')// Battery level
               .fontSize(16)
               .fontColor(Color.Black)
               .fontWeight(FontWeight.Regular)
               .padding({ right: 16 })
               .margin({
                 right: this.getUIContext().px2vp(this.topTextMargin.right),
                 top: 14
               }) // The obtained offset is in px and needs to be converted
           }
           .width('100%')
         }
         .width('100%')
       }
       .width('100%')
       .height('100%')
       .alignContent(Alignment.TopStart)
     }
   }
   ```
