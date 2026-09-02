---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-830
title: 拉起软键盘时闪过黑色块
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 拉起软键盘时闪过黑色块
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:13+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a5c301ad6d937d3775da7ab47da9ccb60daef06b2165a41f8ff8275083729aa8
---

## 问题现象

拉起软键盘时，页面与键盘之间显示黑色块。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/7Tl_TbtETyOVr3s4j84FAQ/zh-cn_image_0000002658917667.png "点击放大")

## 背景知识

* 当用户在输入时，为了确保输入框不会被键盘遮挡，系统提供了避让模式来解决这一问题。开发者可以通过[setKeyboardAvoidMode](../harmonyos-references/ts-universal-attributes-expand-safe-area.md#setkeyboardavoidmode11)控制虚拟键盘抬起时页面的避让模式，避让模式有上抬模式和压缩模式两种，键盘抬起时默认页面避让模式为上抬模式。
* [resize](../harmonyos-references/arkts-apis-window-window.md#resize9)可用来改变当前应用窗口大小。
* [on('avoidAreaChange')](../harmonyos-references/arkts-apis-window-window.md#onavoidareachange9)用来开启当前应用窗口系统规避区变化的监听。

## 问题定位

1. EntryAbility文件中搜索avoidAreaChange，发现应用监听窗口系统规避区变化时使用了resize方法修改窗口尺寸，且该窗口并非应用主窗口。

   ```ts
   import { ConfigurationConstant, UIAbility } from '@kit.AbilityKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { KeyboardAvoidMode, window } from '@kit.ArkUI';
   import { BusinessError } from '@kit.BasicServicesKit';

   export default class EntryAbility extends UIAbility {
     onCreate(): void {
       this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
       hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
     }

     onDestroy(): void {
       hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDestroy');
     }

     onWindowStageCreate(windowStage: window.WindowStage): void {
       // Main window is created,set main page for this ability
       hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

       windowStage.loadContent('pages/Index', (err) => {
         windowStage.getMainWindowSync().getUIContext().setKeyboardAvoidMode(KeyboardAvoidMode.NONE);
         windowStage.getMainWindowSync().setWindowLayoutFullScreen(true);
         if (err.code) {
           hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
           return;
         }
       });

       let windowClass: window.Window | undefined = undefined;
       let config: window.Configuration = {
         name: 'test',
         windowType: window.WindowType.TYPE_DIALOG,
         decorEnabled: true,
         ctx: this.context
       };
       try {
         window.createWindow(config, (err: BusinessError, data) => {
           const errCode: number = err.code;
           if (errCode) {
             console.error(`Failed to create the system window. Cause code: ${err.code}, message: ${err.message}`);
             return;
           }
           windowClass = data;
           windowClass.setUIContent('pages/Main');
           windowClass.showWindow((err: BusinessError) => {
             const errCode: number = err.code;
             if (errCode) {
               console.error(`Failed to show the window. Error code: ${err.code}, message: ${err.message}`);
               return;
             }
             console.info('Succeeded in showing the window.');
           });
           // 监听屏幕避让区域变化
           windowClass.on('avoidAreaChange', (data) => {
             // 监听软键盘区域
             if (data.type === window.AvoidAreaType.TYPE_KEYBOARD) {
               console.info('Succeeded in showing the window.');
               // 软键盘拉起时改变窗口尺寸
               if (data.area.bottomRect.height > 0) {
                 windowClass?.resize(1270, 1800);
               } else {
                 windowClass?.resize(1270, 2740);
               }
             }
           });

         });
       } catch (exception) {
         console.error(`Failed to create the system window. Cause code: ${exception.code}, message: ${exception.message}`);
       }
     }
   };
   ```
2. 查看应用主窗口的设置，主窗口页面的背景色设置为黑色。窗口发生尺寸变化后软键盘才拉起，窗口与软键盘存在空隙显露出页面黑色背景。

   ```ts
   // 主窗口页面
   @Entry
   @Component
   struct Index {
     build() {
       Column()
       .height('100%')
       .width('100%')
       .backgroundColor(Color.Black)
     }
   }
   ```

## 分析结论

应用使用resize方法在软键盘拉起的瞬间就更改并固定了窗口的尺寸，软键盘拉起过程中窗口与软键盘存在空白部分，显露出页面背景黑色。

## 修改建议

该窗口使用setKeyboardAvoidMode(KeyboardAvoidMode.RESIZE)动态避让软键盘。

```ts
import { ConfigurationConstant, UIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(): void {
    this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
  }

  onDestroy(): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDestroy');
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    // Main window is created, set main page for this ability
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
    windowStage.loadContent('pages/Index', (err) => {
      windowStage.getMainWindowSync().setWindowLayoutFullScreen(true);
      if (err.code) {
        hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
        return;
      }
    });
    let windowClass: window.Window | undefined = undefined;
    // 设置窗口配置
    let config: window.Configuration = {
      name: 'test', // 设置窗口名称
      windowType: window.WindowType.TYPE_DIALOG, // 设置为模态窗口
      decorEnabled: true, // 设置显示窗口装饰
      ctx: this.context // 设置窗口上下文
    };
    try {
      // 创建窗口
      window.createWindow(config, (err: BusinessError, data) => {
        const errCode: number = err.code; // 获取错误码
        if (errCode) {
          console.error(`Failed to create the system window. Cause code: ${err.code}, message: ${err.message}`);
          return;
        }
        windowClass = data;
        windowClass.setUIContent('pages/Main'); // 设置窗口绑定的页面
        // 显示窗口
        windowClass.showWindow((err: BusinessError) => {
          const errCode: number = err.code;
          if (errCode) {
            console.error(`Failed to show the window. Error code: ${err.code}, message: ${err.message}`);
            return;
          }
          console.info('Succeeded in showing the window.');
        });
      });
    } catch (exception) {
      console.error(`Failed to create the system window. Cause code: ${exception.code}, message: ${exception.message}`);
    }
  }

  onWindowStageDestroy(): void {
    // Main window is destroyed, release UI related resources
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

```ts
@Entry
@Component
struct Index {
  build() {
    Stack()
      .height('100%')
      .width('100%')
      .backgroundColor(Color.Black);
  }
}
```

输入框所在窗口：

```ts
import { KeyboardAvoidMode } from '@kit.ArkUI';

@Entry
@Component
struct Main {
  aboutToAppear(): void {
    this.getUIContext().setKeyboardAvoidMode(KeyboardAvoidMode.RESIZE); // 该页面进行软键盘避让
  }

  build() {
    Stack() {
      TextInput({ placeholder: '请输入手机号' })
        .type(InputType.PhoneNumber)
        .fontSize(14)
        .fontWeight(FontWeight.Bold)
        .placeholderFont({
          size: 14,
          weight: 400
        })
        .caretColor('#000000')
        .height(40)
        .width('80%')
        .borderRadius(50);
    }
    .height('100%')
    .width('100%')
    .backgroundColor(Color.White);
  }
}
```

src/main/module.json5中需添加权限"ohos.permission.SYSTEM\_FLOAT\_WINDOW"。

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/Bk7dVnerQvKgwAB0wMOiZg/zh-cn_image_0000002628398444.png "点击放大")
