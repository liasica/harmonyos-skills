---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-computer-11
title: 如何实现多个独立窗口
breadcrumb: FAQ > 多设备场景 > 电脑 > 常见问题 > 如何实现多个独立窗口
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:cdb8dd47f26d60d231bdfd40497b4087bc1e1d76149d6842c287e38488e4c153
---

## 问题现象

如何实现一个应用的窗口多开功能，点击按钮可以打开一个独立的窗口，每个窗口都互不干扰，可以单独的打开与关闭？

## 背景知识

* [UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)是包含UI界面的应用组件，继承自Ability，提供UIAbility组件创建、销毁、前后台切换等生命周期回调，同时也具备后台通信能力。
* [startAbility](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startability)启动一个Ability。
* UIAbility实例通过WindowStage持有了一个主窗口，详见：[主窗口的生命周期](../harmonyos-guides/window-type-overview.md#主窗口)，该主窗口为ArkUI提供了绘制区域，可以加载不同的ArkUI页面。

## 解决方案

打开多个互不干扰的独立窗口，可以通过startAbility打开多个UIAbility实例实现，每个UIAbility实例通过WindowStage持有一个主窗口，各个主窗口可以实现独立的功能。参考示例如下：

1. DocumentListPage.ets：通过EntryAbility加载该页面，该页面通过startAbility打开DocumentAbility加载DocumentPage页面。

   ```screen
   import { common, Want } from '@kit.AbilityKit';

   @Entry
   @Component
   struct DocumentListPage {
     private index: number = 1;
     @State docs: number[] = [];
     private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

     build() {
       Row() {
         Column({ space: 10 }) {
           Button('新建文档')
             .onClick(() => {
               // 添加文档
               this.docs.push(this.index);
               // 跳转的目的地want,参数须根据实际情况替换
               let want: Want = {
                 deviceId: '',
                 bundleName: 'com.example.myapplication',
                 moduleName: 'entry',
                 abilityName: 'DocumentAbility',
                 parameters: {
                   instanceKey: 'idx_' + this.index++
                 }
               };
               // 跳转
               this.context.startAbility(want);
             });

           ForEach(this.docs, (idx: number) => {
             Row({ space: 10 }) {
               Image('')
                 .width(20)
                 .aspectRatio(1)
                 .backgroundColor(Color.Blue);

               Text(`文档${idx}`)
                 .fontSize(18)
                 .onClick(() => {
                   // 跳转的目的地want,参数须根据实际情况替换
                   let want: Want = {
                     deviceId: '',
                     bundleName: 'com.example.myapplication',
                     moduleName: 'entry',
                     abilityName: 'DocumentAbility',
                     parameters: {
                       instanceKey: 'idx_' + idx
                     }
                   };
                   // 跳转
                   this.context.startAbility(want);
                 });
             }.width('100%');
           });
         }
         .width('100%')
         .height('100%')
         .padding(20);
       };
     }
   }
   ```
2. DocumentAbility.ets：提供DocumentPage页面的UIAbility组件创建、销毁、前后台切换等生命周期回调。

   ```screen
   import { UIAbility } from '@kit.AbilityKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { window } from '@kit.ArkUI';

   export default class DocumentAbility extends UIAbility {
     onCreate(): void {
       hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
     }

     onDestroy(): void {
       hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDestroy');
     }

     onWindowStageCreate(windowStage: window.WindowStage): void {
       hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

       windowStage.loadContent('pages/DocumentPage', (err) => {
         if (err.code) {
           hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
           return;
         }
         hilog.info(0x0000, 'testTag', 'Succeeded in loading the content.');
       });
     }

     onWindowStageDestroy(): void {
       hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
     }

     onForeground(): void {
       // Ability has brought to foreground
       hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onForeground');
     }

     onBackground(): void {
       // Ability has back to background
       hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onBackground');
     }
   };
   ```
3. DocumentPage.ets：DocumentAbility拉起的页面详情，支持跳转回DocumentListPage页面。

   ```screen
   import { common, Want } from '@kit.AbilityKit';

   @Entry
   @Component
   struct DocumentPage {
     private context = this.getUIContext().getHostContext() as common.UIAbilityContext;
     @State content: string = '';

     build() {
       Row() {
         Column({ space: 10 }) {
           Row({ space: 10 }) {
             SymbolGlyph($r('sys.symbol.arrow_left_circle'))
               .fontSize(50)
               .onClick(() => {
                 // 跳转的目的地want,参数须根据实际情况替换
                 let want: Want = {
                   deviceId: '',
                   bundleName: 'com.example.myapplication',
                   moduleName: 'entry',
                   abilityName: 'EntryAbility',
                 };
                 // 跳转
                 this.context.startAbility(want);
               });
             Text('这里是标题，点前面符号跳转')
               .fontSize(30)
               .fontWeight(FontWeight.Bold);
           }
           .width('100%');

           Divider();
           TextArea({
             placeholder: '请输入文档内容',
             text: this.content
           })
             .layoutWeight(1)
             .onChange(val => this.content = val);
         }
         .width('100%')
         .height('100%')
         .padding(10);
       };
     }
   }
   ```
4. module.json5：abilities增加DocumentAbility配置。

   ```screen
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
       "name": "DocumentAbility",
       "srcEntry": "./ets/entryability/DocumentAbility.ets",
       "description": "$string:DocumentAbility_desc",
       "icon": "$media:layered_image",
       "label": "$string:DocumentAbility_label",
       "launchType": "specified",
       "startWindowIcon": "$media:startIcon",
       "startWindowBackground": "$color:start_window_background"
     }
   ],
   ```

## 常见FAQ

Q：如何确认当前打开的UIAbility的数量？

A：可以在[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md#uiability)的生命周期中记录当前已打开的UIAbility数量，示例代码如下：

```screen
import { ConfigurationConstant, UIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';

const DOMAIN = 0x0000;
// 已打开的UIAbility数量
let uiAbilityNum = 0;

export default class WindowsNumAbility extends UIAbility {
  onCreate(): void {
    try {
      this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
    } catch (err) {
      hilog.error(DOMAIN, 'testTag', 'Failed to set colorMode. Cause: %{public}s', JSON.stringify(err));
    }
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
  }

  onDestroy(): void {
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
    // 销毁一个UIAbility时，UIAbility数量减少1，并存入AppStorage
    uiAbilityNum -= 1;
    AppStorage.setOrCreate('uiAbilityNum', uiAbilityNum);
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    // Main window is created, set main page for this ability
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
    // 每次完成WindowStage创建，UIAbility数量增加1，并存入AppStorage
    uiAbilityNum += 1;
    AppStorage.setOrCreate('uiAbilityNum', uiAbilityNum);

    // 第一个窗口加载Index页面，后续新创建的窗口加载NewIndex页面
    if (uiAbilityNum === 1) {
      windowStage.loadContent('pages/Index', (err) => {
        if (err.code) {
          hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
          return;
        }
        hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
      });
    } else {
      windowStage.loadContent('pages/NewIndex', (err) => {
        if (err.code) {
          hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
          return;
        }
        hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
      });
    }
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
