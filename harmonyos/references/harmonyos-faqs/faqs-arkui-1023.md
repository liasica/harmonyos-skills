---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1023
title: 如何获取窗口的尺寸及位置
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 如何获取窗口的尺寸及位置
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:14+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5123eea2ee0fd576d4f7fd92283f5f46dc06a93389da4b4bcdc7dcdec1944c3e
---

## 问题现象

应用开发过程中，窗口的尺寸及位置该如何获取？

## 背景知识

* [getWindowProperties](../harmonyos-references/arkts-apis-window-window.md#getwindowproperties9)接口可以获取当前窗口的属性，该接口返回的[WindowProperties](../harmonyos-references/arkts-apis-window-i.md#windowproperties)实例中的windowRect属性返回一个[Rect](../harmonyos-references/arkts-apis-window-i.md#rect7)类型的参数，该参数可获取到当前窗口的宽度（width）和高度（height）及窗口的左边界（left）和上边界（top）信息。
* [OH\_WindowManager\_GetWindowProperties](../harmonyos-references/capi-oh-window-h.md#oh_windowmanager_getwindowproperties)：HarmonyOS Next提供了Native侧获取窗口属性的napi，该接口返回的[WindowManager\_WindowProperties](../harmonyos-references/capi-windowmanager-windowproperties.md)实例中的windowRect属性返回一个[WindowManager\_Rect](https://lfwiseopertest04.hwcloudtest.cn/knowledge-admin/knowledgeDetail/(https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-windowmanager-rect))类型的参数，该参数可获取到当前窗口的宽度（width）和高度（height）及窗口的x轴（posX）和y轴（posY）的信息。

## 解决方案

方案一：使用窗口提供的getWindowProperties接口获取当前窗口的大小及位置信息。

```ts
import { window } from '@kit.ArkUI';

@Entry
@Component
struct WindowProp {
  @State windowRectRes: window.Rect = {
    left: 0,
    top: 0,
    width: 0,
    height: 0
  };

  onPageShow(): void {
    let windowClass: window.Window | undefined = undefined;
    try {
      // 获取需要查询信息的窗口实例
      let promise = window.getLastWindow(this.getUIContext().getHostContext());
      promise.then((data) => {
        windowClass = data;
        try {
          // 通过调用getWindowProperties接口返回一个类型为WindowProperties的属性，该属性中的windowRect属性返回一个Rect类型的参数，该参数可获取到当前窗口的宽度（width）和高度（height）及窗口的左边界（left）和上边界（top）信息。
          let properties = windowClass.getWindowProperties();
          this.windowRectRes = properties.windowRect;
        } catch (exception) {
          console.error(`窗口Failed to obtain the window properties. Cause: ${exception}`);
        }
        console.info(`窗口Succeeded in obtaining the top window. Data: ${data}`);
      }).catch((err: BusinessError<string>) => {
        console.error(`窗口Failed to obtain the top window. Cause: ${err}`);
      });
    } catch (exception) {
      console.error(`窗口Failed to obtain the top window. Cause: ${exception}`);
    }
  }

  build() {
    Column({ space: 20 }) {
      Row({ space: 20 }) {
        Row() {
          Text('窗口X轴坐标值：')
            .fontSize(15)
            .fontWeight(FontWeight.Bold);
          // 通过windowRectRes的left属性获取窗口的左边界（x轴坐标值）
          Text(this.windowRectRes.left.toString())
            .fontSize(15)
            .fontWeight(FontWeight.Bold);
        };

        Row() {
          Text('窗口Y轴坐标值：')
            .fontSize(15)
            .fontWeight(FontWeight.Bold);
          // 通过windowRectRes的top属性获取窗口的上边界（y轴坐标值）
          Text(this.windowRectRes.top.toString())
            .fontSize(15)
            .fontWeight(FontWeight.Bold);
        };
      };

      Row({ space: 20 }) {
        Row() {
          Text('窗口宽度：')
            .fontSize(15)
            .fontWeight(FontWeight.Bold);
          // 通过windowRectRes的width属性获取窗口的宽度
          Text(this.windowRectRes.width.toString())
            .fontSize(15)
            .fontWeight(FontWeight.Bold);
        };

        Row() {
          Text('窗口高度：')
            .fontSize(15)
            .fontWeight(FontWeight.Bold);
          // 通过windowRectRes的height属性获取窗口的高度
          Text(this.windowRectRes.height.toString())
            .fontSize(15)
            .fontWeight(FontWeight.Bold);
        };
      };
    }
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%');
  }
}
```

效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/X9uFYXlYQROqFWcskuCCaw/zh-cn_image_0000002658804079.png "点击放大")

方案二：通过OH\_WindowManager\_GetWindowProperties接口在Native侧获取窗口属性。

1. 创建NDK工程，详细步骤请参考以下文档：[创建NDK工程](../harmonyos-guides/create-with-ndk.md)。
2. 在napi\_init.cpp文件中定义获取窗口属性的方法getWindowPropertiesByID：

   ```
   /*
    * Copyright (c) Huawei Technologies Co., Ltd. 2026. All rights reserved.
    */
   #include "napi/native_api.h"
   #include "hilog/log.h"
   #include <window_manager/oh_window.h>
   int32_t g_WindowID;
   WindowManager_WindowProperties windowProperties;

   static napi_value getWindowPropertiesByID(napi_env env, napi_callback_info info)
   {
     size_t argc = 1;
     napi_value args[1] = {nullptr};
     napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
     napi_get_value_int32(env, args[0], &g_WindowID);
     OH_LOG_Print(LOG_APP, LOG_INFO, 0x0, "getWindowPropertiesByID", "get windowID %{public}d", g_WindowID);
     // 根据窗口id获取窗口信息，返回的windowProperties实例中的windowRect属性返回一个WindowManager_Rect类型的参数，该参数可获取到当前窗口的宽度（width）和高度（height）及窗口的x轴（posX）和y轴（posY）的信息
     int32_t re = OH_WindowManager_GetWindowProperties(g_WindowID, &windowProperties);
     OH_LOG_Print(LOG_APP, LOG_INFO, 0x0, "windowProperties",
                 "get windowProperties rect %{public}d %{public}d %{public}d %{public}d",
                 windowProperties.windowRect.posX, windowProperties.windowRect.posY, windowProperties.windowRect.width,
                 windowProperties.windowRect.height);
     return nullptr;
   }
   EXTERN_C_START
   static napi_value Init(napi_env env, napi_value exports)
   {
     napi_property_descriptor desc[] = {{"getWindowPropertiesByID", nullptr, getWindowPropertiesByID, nullptr, nullptr,
                                         nullptr, napi_default, nullptr}};
     napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
     return exports;
   }
   EXTERN_C_END
   static napi_module demoModule = {
     .nm_version = 1,
     .nm_flags = 0,
     .nm_filename = nullptr,
     .nm_register_func = Init,
     .nm_modname = "entry",
     .nm_priv = ((void *)0),
     .reserved = {0},
   };
   extern "C" __attribute__((constructor)) void RegisterEntryModule(void) { napi_module_register(&demoModule); }
   ```
3. 在cpp->types->libentry路径下的Index.d.ts文件中导出napi\_init.cpp文件中定义的getWindowPropertiesByID方法：

   ```ts
   export const getWindowPropertiesByID: (windowID: number) => void;
   ```
4. 在Entry主模块的oh-package.json5中添加依赖Native的声明文件路径：

   ```json
   "dependencies": {
     "libentry.so": "file:./src/main/cpp/types/libentry"
   },
   ```
5. 在EntryAbility.ets中获取并保存对应窗口的ID(本例以主窗口为例)。

   ```ts
   import { ConfigurationConstant, UIAbility } from '@kit.AbilityKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { window } from '@kit.ArkUI';
   import { BusinessError } from '@kit.BasicServicesKit';

   const DOMAIN = 0x0000;

   export default class EntryAbility extends UIAbility {
     windowID: number = 0;

     onCreate(): void {
       this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
     }

     onWindowStageCreate(windowStage: window.WindowStage): void {
       windowStage.loadContent('pages/WindowProp', (err) => {
         if (err.code) {
           return;
         }
         // 1.获取应用主窗口。
         let windowClass: window.Window | null = null;
         windowStage.getMainWindow((err: BusinessError, data) => {
           let errCode: number = err.code;
           if (errCode) {
             console.error(`Failed to obtain the main window. CCode:${err.code}, message:${err.message}`);
             return;
           }
           windowClass = data;
           // 通过windowClass的getWindowProperties方法获取id信息
           this.windowID = windowClass.getWindowProperties().id;
           AppStorage.setOrCreate<number>('windowID', this.windowID);
         });
         hilog.info(0x0000, 'testTag', 'Succeeded in loading the content.');
       });
     }
   };
   ```
6. ArkTS侧import引用oh-package.json5中声明的依赖名称([本例中为libentry.so](http://xn--libentry-kd0mgez4n6p2h.so/))，并调用so的getWindowPropertiesByID方法：

   ```ts
   import testNapi from 'libentry.so';

   @Entry
   @Component
   struct Index {
     private windowID: number | undefined = AppStorage.get('windowID');

     build() {
       Row() {
         Column() {
           Text('setWindowID')
             .fontSize($r('app.float.page_text_font_size'))
             .fontWeight(FontWeight.Bold)
             .onClick(() => {
               // 调用so中定义的方法,获取窗口的位置及大小。
               testNapi.getWindowPropertiesByID(this.windowID);
             });
         }
         .width('100%');
       }
       .height('100%');
     }
   }
   ```
