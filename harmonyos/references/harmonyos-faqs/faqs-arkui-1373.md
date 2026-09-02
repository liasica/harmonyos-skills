---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1373
title: 如何在Native侧获取窗口ID
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 如何在Native侧获取窗口ID
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:14+08:00
doc_updated_at: 2026-07-02
content_hash: sha256:54c792d8b03ebb6683111b00a58c108f4b062626cbea3802a876a00beacee0ca
---

## 问题现象

在进行系统级功能开发、输入事件拦截、无障碍服务、屏幕录制、窗口管理时，如何在Native侧需要获取窗口的ID，以便后续的功能开发。

## 背景知识

HarmonyOS的窗口模块将窗口界面分为系统窗口、应用窗口两种基本类型。

* 系统窗口：系统窗口指完成系统特定功能的窗口。如音量条、壁纸、通知栏、状态栏、导航栏等。
* 应用窗口：应用窗口区别于系统窗口，指与应用显示相关的窗口。根据显示内容的不同，应用窗口又分为应用主窗口、应用子窗口两种类型。应用窗口开发可以参考[窗口类型开发概述](../harmonyos-guides/window-type-overview.md)。
  + 应用主窗口：应用主窗口用于显示应用界面，会在"任务管理界面"显示。
  + 应用子窗口：应用子窗口用于显示应用的弹窗、悬浮窗等辅助窗口，不会在"任务管理界面"显示。应用子窗口的生命周期跟随应用主窗口。设置方式参考[子窗口开发指导](../harmonyos-guides/subwindow-guide.md)。

ArkTS与Native跨语言交互开发详见[使用Node-API实现跨语言交互开发流程](../harmonyos-guides/use-napi-process.md)。

## 解决方案

实现Native侧获取窗口ID可参考如下步骤：

1. 由于在Native侧无法直接获取window实例，需要在ArkTS侧EntryAbility的onWindowStageCreate生命周期中获取。

   ```ts
   onWindowStageCreate(windowStage: window.WindowStage): void {
     // Main window is created,set main page for this ability
     hilog.info(0x0000, 'testTag', '%{public}s','Ability onWindowStageCreate');
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
       console.info(`Succeeded in obtaining the main window. Result:${data}`);
     });
     windowStage.loadContent('pages/Index', (err) => {
       if (err.code) {
         hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
         return;
       }
       hilog.info(0x0000, 'testTag', 'Succeeded in loading the content.');
     });
   }
   ```
2. 获取到windowID后，调用Native方法将windowID传入Native侧。

   ```ts
   import testNapi from 'libentry.so';

   @Entry
   @Component
   struct Index {
     @StorageLink('windowID') windowID: number = 0;
     build() {
       Row() {
         Column() {
           Text('setWindowID')
             .fontSize($r('app.float.page_text_font_size'))
             .fontWeight(FontWeight.Bold)
             .onClick(() => {
               testNapi.setWindowID(this.windowID);
             });
         }
         .width('100%');
       }
       .height('100%');
     }
   }
   ```
3. 在Native侧接收到windowID后，将windowID进行固化用于后续使用。

   ```
   int32_t g_WindowID;
   static napi_value setWindowID(napi_env env, napi_callback_info info)
   {
       size_t argc = 1;
       napi_value args[1] = {nullptr};
       napi_typedarray_type type_napi;

       napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

       napi_get_value_int32(env, args[0], &g_WindowID);

       OH_LOG_Print(LOG_APP, LOG_INFO, 0x0, "setWindowID", "get windowID %{public}d", g_WindowID);

       return nullptr;
   }
   ```

完整代码：

entry>src>main>ets>entryability>EntryAbility.ets:

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

  onDestroy(): void {
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
  }
  onWindowStageCreate(windowStage: window.WindowStage): void {
    // Main window is created,set main page for this ability
    hilog.info(0x0000, 'testTag', '%{public}s','Ability onWindowStageCreate');
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
      console.info(`Succeeded in obtaining the main window. Result:${data}`);
    });
    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
        return;
      }
      hilog.info(0x0000, 'testTag', 'Succeeded in loading the content.');
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

entry>src>main>ets>pages>Index.ets:

```ts
import testNapi from 'libentry.so';

@Entry
@Component
struct Index {
  @StorageLink('windowID') windowID: number = 0;
  build() {
    Row() {
      Column() {
        Text('setWindowID')
          .fontSize($r('app.float.page_text_font_size'))
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            testNapi.setWindowID(this.windowID);
          });
      }
      .width('100%');
    }
    .height('100%');
  }
}
```

entry>src>main>cpp>types>libentry>index.d.ts:

```ts
export const setWindowID: (windowID: number) => void;
```

entry>src>main>cpp>napi\_init.cpp:

```
/*
 * Copyright (c) Huawei Technologies Co., Ltd. 2025. All rights reserved.
 */
#include "napi/native_api.h"
#include "hilog/log.h"
int32_t g_WindowID;
static napi_value setWindowID(napi_env env, napi_callback_info info)
{
    size_t argc = 1;
    napi_value args[1] = {nullptr};
    napi_typedarray_type type_napi;

    napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

    napi_get_value_int32(env, args[0], &g_WindowID);

    OH_LOG_Print(LOG_APP, LOG_INFO, 0x0, "setWindowID", "get windowID %{public}d", g_WindowID);

    return nullptr;
}
EXTERN_C_START
static napi_value Init(napi_env env, napi_value exports)
{
    napi_property_descriptor desc[] = {
        { "setWindowID", nullptr, setWindowID, nullptr, nullptr, nullptr, napi_default, nullptr }
    };
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
    .nm_priv = ((void*)0),
    .reserved = { 0 },
};

extern "C" __attribute__((constructor)) void RegisterEntryModule(void)
{
    napi_module_register(&demoModule);
}
```

## 常见FAQ

Q：Native侧有办法对窗口进行管理和控制么？

A：可以通过[WindowManager](../harmonyos-references/capi-windowmanager.md)模块的C API对窗口进行控制，由于其接口均需要windowID作为入参，需要在调用前获取到windowID。

Q：如何传入多个windowID？

A：如果需要传入多个windowID可以通过构建Int32Array进行填充，在Native侧创建数组接收。
