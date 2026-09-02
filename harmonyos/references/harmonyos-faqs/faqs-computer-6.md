---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-computer-6
title: startAbility启动小窗口后requestFocus原页面组件报错
breadcrumb: FAQ > 多设备场景 > 电脑 > 常见问题 > startAbility启动小窗口后requestFocus原页面组件报错
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6645d08d7fb6f2437312f8d8ea082863f6599a0e44c7751f186380a720206132
---

## 问题现象

在2in1设备上启动小窗口，小窗口中调用requestFocus到原页面组件时报错150003。

```log
Error message:The component doesn't exist, is currently invisible, or has been disabled.
Error code:150003
```

## 背景知识

* [UIContext](../harmonyos-references/arkts-apis-uicontext-uicontext.md)：在Stage模型中，WindowStage/Window可以通过loadContent接口加载页面并创建UI的实例，并将页面内容渲染到关联的窗口中，所以UI实例和窗口是一一关联的。
* [requestFocus](../harmonyos-references/ts-universal-attributes-focus.md#requestfocus9)：通过组件的id将焦点转移到组件树对应的实体节点，当前帧生效。
* [AppStorage](../harmonyos-guides/arkts-appstorage.md)：AppStorage支持应用的主线程内多个UIAbility实例间的UI状态数据共享。
* [startAbility](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startability)：startAbility接口是将应用链接放入want中，通过调用[隐式want匹配](../harmonyos-guides/explicit-implicit-want-mappings.md#隐式want匹配原理)的方法触发应用跳转。通过startAbility接口启动时，还需要调用方传入待匹配的action和entity。

## 问题定位

错误码[150003](../harmonyos-references/errorcode-focus.md#section150003-节点不存在)表示requestFocus传入的id指向不存在、未挂树或者不可见节点。可以排查以下情况：

* 检查目标组件id同requestFocus请求参数是否一致。

  如下小窗口修改焦点方法requestFocus('TextInput')：

  ```ts
  Button('requestFocus')
    .margin(15)
    .onClick(() => {
      let context = this.getUIContext();
      context.getFocusController().requestFocus('TextInput');
    })
  ```

  主窗口获取焦点组件中.id('TextInput')，同小窗口请求的参数一致：

  ```screen
  TextInput({ text: this.text!!, placeholder: 'input your word...' })
    .placeholderColor(Color.Grey)
    .placeholderFont({ size: 14, weight: 400 })
    .caretColor(Color.Blue)
    .width('95%')
    .height(40)
    .margin(20)
    .fontSize(14)
    .fontColor(Color.Black)
    .id('TextInput')
  ```

* 组件id一致的情况下，需要检查小窗口启动方式，是否与主窗口之间有共享的UI实例，这样才能将焦点转移到主窗口组件树对应的实体节点。

  如下小窗口是由新的startAbility，通过loadContent接口加载页面新创建的UI实例，与主窗口没有关联，无法将焦点转移到主窗口组件树对应的实体节点。

  ```ts
  onWindowStageCreate(windowStage: window.WindowStage): void {
    let windowClass: window.Window | null = null;
    let calculation: number = 2;
    // 打开新UI实例
    let uiAbility: string = '@bundle:' + 'com.example.keyboard' + '/entry/ets/pages/KeyboardPage';

    hilog.info(0x0000, TAG, 'KeyboardAbility onWindowStageCreate');

    windowStage.loadContent(uiAbility, (err, data) => {
      if (err.code) {
        return;
      }
      hilog.info(0x0000, TAG, 'Succeeded in loading the content.');

      windowStage.getMainWindow((err: BusinessError, data) => {
        let errCode: number = err.code;
        if (errCode) {
          return;
        }
        windowClass = data;
      });
    }
  }
  ```

## 分析结论

小窗口自己的UIContext调用requestFocus无法使主窗口的组件获取焦点，需要先获取主窗口的UIContext，再使用主窗口的UIContext来调用requestFocus方法，使焦点转移到主窗口组件树对应的实体节点。

## 修改建议

在主窗口创建UI实例时，获取UIContext存到AppStorage应用全局的UI状态存储中，在小窗口将焦点转移到主窗口组件树对应的实体节点时，获取存储中的主窗口UIContext。示例代码如下：

1. 在EntryAbility内，主窗口获取并保存UIContext：

   ```ts
   import { UIAbility } from '@kit.AbilityKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { window } from '@kit.ArkUI';
   import { BusinessError } from '@kit.BasicServicesKit';

   const DOMAIN = 0x0000;

   export default class EntryAbility extends UIAbility {
     private uiContext: UIContext | undefined = undefined;

     onDestroy(): void {
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
     }

     onWindowStageCreate(windowStage: window.WindowStage): void {
       // Main window is created, set main page for this ability
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

       windowStage.loadContent('pages/Index', (err) => {
         if (err.code) {
           hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
           return;
         }
         windowStage.getMainWindow().then((data: window.Window) => {
           this.uiContext = data.getUIContext();
           AppStorage.setOrCreate("entryContext", this.uiContext);
         }).catch((err: BusinessError) => {
           console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
         });
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
2. Index.ets页面,使用startAbility唤起小窗口。

   ```ts
   import { componentUtils } from '@kit.ArkUI';
   import { common, StartOptions, Want } from '@kit.AbilityKit';
   import { BusinessError } from '@kit.BasicServicesKit';

   @Entry
   @Component
   struct Index {
     @State text: string = '';

     build() {
       Column() {
         TextInput({ text: this.text!!, placeholder: 'input your word...' })
           .placeholderColor(Color.Grey)
           .placeholderFont({ size: 15, weight: 400 })
           .caretColor(Color.Blue)
           .width('95%')
           .height(50)
           .margin(20)
           .fontSize(14)
           .fontColor(Color.Black)
           .id('TextInput');
         Button('openSoftKeyboard')
           .margin(15)
           .onClick(() => {
             this.openSoftKeyboard();
           });
       }
       .width('100%')
       .height('100%')
       .justifyContent(FlexAlign.Center);
     }

     openSoftKeyboard() {
       // 安全键盘输入框
       let modePosition: componentUtils.ComponentInfo = this.getUIContext().getComponentUtils().getRectangleById('TextInput');
       let layoutX = modePosition.screenOffset.x;
       let layoutY = modePosition.screenOffset.y;
       let inputH = modePosition.size.height;
       let inputW = modePosition.size.width;

       let want: Want = {
         bundleName: 'com.example.keyboard',
         abilityName: 'KeyboardAbility',
         moduleName: 'entry',
         parameters: {
           inputX: layoutX,
           inputY: layoutY,
           inputH: inputH,
           inputW: inputW
         }
       };
       let options: StartOptions = {
         supportWindowModes: [
           2
         ]
       };
       try {
         let uiAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
         uiAbilityContext?.startAbility(want, options, (err: BusinessError) => {
           if (err.code) {
             return;
           }
         });
       } catch (err) {
       }
     }
   }
   ```
3. 新建KeyboardPage.ets，通过StorageProp获取在主窗口保存的UIContext，可以通过该UIContext对TextInput获取焦点使能。

   ```ts
   @Entry
   @Component
   struct KeyboardPage {
     @State keyboardText: string = '';
     @StorageProp('entryContext') context: UIContext = this.getUIContext();

     build() {
       Column() {
         TextInput({ text: this.keyboardText!!, placeholder: 'input your word...' })
           .width('95%')
           .height(40)
           .margin(20)
           .fontSize(14)
           .fontColor(Color.Black)
           .placeholderColor(Color.Grey)
           .placeholderFont({ size: 14, weight: 100 })
           .caretColor(Color.Blue)
           .id('TextInput2');
         Button('requestFocus success')
           .margin(15)
           .onClick(() => {
             this.context.getFocusController().requestFocus('TextInput');
           });

         Button('requestFocus error')
           .margin(15)
           .onClick(() => {
             let context = this.getUIContext();
             context.getFocusController().requestFocus('TextInput');
           });
       }
       .width('100%')
       .height('100%')
       .justifyContent(FlexAlign.Center);
     }
   }
   ```
4. 新建小窗口的Ability命名为KeyboardAbility，并通过loadContent加载KeyboardPage页面，并且指定小窗口的大小和位置。

   ```ts
   import { UIAbility } from '@kit.AbilityKit';

   import { window } from '@kit.ArkUI';
   import { BusinessError } from '@kit.BasicServicesKit';

   export default class KeyboardAbility extends UIAbility {
     onWindowStageCreate(windowStage: window.WindowStage): void {
       let windowClass: window.Window | null = null;
       // 打开
       let uiAbility: string = '@bundle:' + 'com.example.keyboard' + '/entry/ets/pages/KeyboardPage';
       windowStage.loadContent(uiAbility, (err) => {
         if (err.code) {
           return;
         }
         windowStage.getMainWindow((err: BusinessError, data) => {
           let errCode: number = err.code;
           if (errCode) {
             return;
           }
           windowClass = data;
           // 获取应用启动时的窗口尺寸
           // 注册回调函数，监听窗口尺寸变化
           windowClass.resize(500, 300, (err: BusinessError) => {
             let errCode: number = err.code;
             if (errCode) {
               return;
             }
           });
           // 移动位置
           windowClass.moveWindowTo(500, 300);
           // 设置主窗口或子窗口的布局是否为沉浸式布局
           let isLayoutFullScreen = true;
           try {
             let promise = windowClass.setWindowLayoutFullScreen(isLayoutFullScreen);
             promise.then(() => {
             }).catch(() => {
             });
           } catch (exception) {
           }
           windowClass.setWindowSystemBarEnable([]);
           if (0) {
             try {
             } catch (exception) {
             }
             try {
               windowClass?.on('windowTitleButtonRectChange', () => {
               });
             } catch (exception) {
             }
           }
           if (canIUse('SystemCapability.Window.SessionManager')) {
             let isTouchable: boolean = false;
             windowClass?.setWindowDecorVisible(isTouchable);
           }
         });
       });
     }
   };
   ```
5. 将KeyboardAbility添加至模块配置的module.json5中abilities里。

   ```screen
   {
     "module": {
       "name": "entry",
       "type": "entry",
       "description": "$string:module_desc",
       "mainElement": "EntryAbility",
       "deviceTypes": [
         "phone"
       ],
       "deliveryWithInstall": true,
       "installationFree": false,
       "pages": "$profile:main_pages",
       "abilities": [
         {
           "name": "EntryAbility",
           "srcEntry": "./ets/entryability/EntryAbility.ets",
           "description": "$string:EntryAbility_desc",
           "icon": "$media:layered_image",
           "label": "$string:EntryAbility_label",
           "startWindowIcon": "$media:startIcon",
           "startWindowBackground": "$color:start_window_background",
           "exported": true,
           "skills": [
             {
               "entities": [
                 "entity.system.home"
               ],
               "actions": [
                 "ohos.want.action.home"
               ]
             }
           ]
         },
         {
           "name": "KeyboardAbility",
           "srcEntry": "./ets/keyboardability/KeyboardAbility.ets",
           "description": "$string:KeyboardAbility_desc",
           "icon": "$media:layered_image",
           "label": "$string:KeyboardAbility_label",
           "startWindowIcon": "$media:startIcon",
           "startWindowBackground": "$color:start_window_background"
         }
       ],
       "extensionAbilities": [
         {
           "name": "EntryBackupAbility",
           "srcEntry": "./ets/entrybackupability/EntryBackupAbility.ets",
           "type": "backup",
           "exported": false,
           "metadata": [
             {
               "name": "ohos.extension.backup",
               "resource": "$profile:backup_config"
             }
           ],
         }
       ]
     }
   }
   ```
