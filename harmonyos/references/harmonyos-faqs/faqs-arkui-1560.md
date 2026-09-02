---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1560
title: 应用启动后为横屏展示，发生页面跳转后转为竖屏
breadcrumb: FAQ > 应用框架开发 > UI框架 > 屏幕管理 > 应用启动后为横屏展示，发生页面跳转后转为竖屏
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:13+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a2561d8b2b7a11547d58f5ed5cb8735c3ebe40e8a97af2b3847eb431d40fa98d
---

## 问题现象

应用刚启动时横屏展示，页面跳转后，应用窗口变成竖屏展示，即使退出这个页面后，应用窗口仍然保持竖屏状态。

## 背景知识

设置窗口旋转策略的方式有以下两种：

1. 通过module.json5文件中“[orientation](../harmonyos-references/arkts-apis-window-e.md#orientation9)”字段进行设置。
2. 在代码中通过调用窗口window的setPreferredOrientation方法进行设置。

这两种方式触发设置旋转的时机不同，module.json5文件中的字段在窗口启动时就会生效，对于应用启动时就需要设置横屏或者竖屏的应用，需要进行配置。而[setPreferredOrientation](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)是在调用该方法时进行窗口方向的设置，用于在应用启动之后，还需要改变显示方向的场景。

## 问题定位

1. 查阅module.json5文件中“orientation”配置项是否配置为landscape。
2. 查阅页面跳转处代码，是否调用setPreferredOrientation方法，将窗口方向配置成了window.Orientation.PORTRAIT。

## 分析结论

应用module.json5配置文件中“orientation”配置项是否配置为landscape，因此应用在启动时处于横屏状态，页面跳转时，代码中调用了setPreferredOrientation(window.Orientation.PORTRAIT)接口，将窗口方向设置成竖屏。

## 修改建议

应用对该跳转页面有竖屏显示需求，可以在进入页面通过[setPreferredOrientation](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)进行相应的竖屏方向设置，退出页面需要通过setPreferredOrientation恢复横屏设置，完整示例可参考如下代码：

1. 涉及的两个页面需在路由配置main\_pages.json页面中配置。

   ```ts
   {
     "src": [
       "pages/Index",
       "pages/Second"
     ]
   }
   ```
2. 首页Index因module.json5中“orientation”配置项为landscape，初始化时会横屏显示，点击按钮可跳转Second页面。

   ```ts
   import { BusinessError } from '@kit.BasicServicesKit';

   @Entry
   @Component
   struct Index {
     private  message: string = '首页横屏展示';

     build() {
       Row() {
         Column() {
           Text(this.message)
             .fontSize(50)
             .fontWeight(FontWeight.Bold)
           // 添加按钮，以响应用户onClick事件
           Button() {
             Text('Next')
               .fontSize(30)
               .fontWeight(FontWeight.Bold)
           }
           .type(ButtonType.Capsule)
           .margin({
             top: 20
           })
           .backgroundColor('#0D9FFB')
           .width('40%')
           .height('5%')
           // 跳转按钮绑定onClick事件，单击时跳转到第二页
           .onClick(() => {
             console.info(`Succeeded in clicking the 'Next' button.`);
             // 获取UIContext
             let uiContext: UIContext = this.getUIContext();
             let router = uiContext.getRouter();
             // 跳转到第二页
             router.pushUrl({ url: 'pages/Second' }).then(() => {
               console.info('Succeeded in jumping to the second page.');

             }).catch((err: BusinessError) => {
               console.error(`Failed to jump to the second page. Code is ${err.code}, message is ${err.message}`);
             });
           })
         }
         .width('100%')
       }
       .height('100%')
     }
   }
   ```
3. Second页面初始化时通过setPreferredOrientation设置竖屏，在页面退出时恢复横屏设置。

   ```ts
   import { BusinessError } from '@kit.BasicServicesKit';
   import { common } from '@kit.AbilityKit';
   import { window } from '@kit.ArkUI';

   @Entry
   @Component
   struct Second {
     private  message: string = '业务需要竖屏展示';
     context = this.getUIContext().getHostContext() as common.UIAbilityContext;
     windowClass: window.Window = this.context.windowStage.getMainWindowSync();

     aboutToAppear(): void {
       this.windowClass.setPreferredOrientation(window.Orientation.PORTRAIT);
     }

     aboutToDisappear(): void {
       this.windowClass.setPreferredOrientation(window.Orientation.LANDSCAPE);
     }

     build() {
       Row() {
         Column() {
           Text(this.message)
             .fontSize(50)
             .fontWeight(FontWeight.Bold)
           Button() {
             Text('返回首页')
               .fontSize(30)
               .fontWeight(FontWeight.Bold)
           }
           .type(ButtonType.Capsule)
           .margin({
             top: 20
           })
           .backgroundColor('#0D9FFB')
           .width('40%')
           .height('5%')
           // 返回按钮绑定onClick事件，单击按钮时返回到第一页
           .onClick(() => {
             console.info(`Succeeded in clicking the 'Back' button.`);
             // 获取UIContext
             let uiContext: UIContext = this.getUIContext();
             let router = uiContext.getRouter();
             try {
               // 返回第一页
               router.back();
               console.info('Succeeded in returning to the first page.');
             } catch (err) {
               let code = (err as BusinessError).code;
               let message = (err as BusinessError).message;
               console.error(`Failed to return to the first page. Code is ${code}, message is ${message}`);
             }
           })
         }
         .width('100%')
       }
       .height('100%')
     }
   }
   ```
