---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/ndk-development-faq-0006
title: Native与ArkTS跨语言交互与数据传递常见问题
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 常见问题 > Native与ArkTS跨语言交互与数据传递常见问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:46:55+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:8c2210f23aca3e1be4325d31242cc42f12243d9aa4d463d5a8c4a3766111e832
---

**Q：Native侧如何获取ArkTS侧Object对象及其成员变量？**

**A**：在ArkTS侧定义类，传递类到Native侧调用类函数。详情见示例代码。

ArkTS侧

```ts
// index.ets
import testNapi from 'libentry.so';
import { PromptAction } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

class A {
  name: string = 'username'

  onCall() {
    try {
      new PromptAction().showToast({
        message: 'Message Info',
        duration: 2000
      });
    } catch (err) {
      hilog.error(0x0000, 'testTag', `showToast undefined, code is ${err.code}, message is ${err.message}`);
    }
  }
}

@Entry
@Component
struct NativeGetArkTSObject {
  build() {
    Button()
      .onClick(() => {
        testNapi.callFunction(new A());
      })
  }
}
```

```ts
// index.d.ts
export const callFunction: (a:object) => void;
```

Native侧

```cpp
// Pass in an instance object and call functions in the object on the C++side 
#include "napi/native_api.h" 
static napi_value CallFunction(napi_env env, napi_callback_info info) { 
    // Get instance object 
    size_t argc = 1; 
    napi_value args[1] = {nullptr}; 
    napi_get_cb_info(env, info, &argc, args, NULL, NULL); 
    // Method for obtaining objects 
    napi_value onCall; 
    napi_get_named_property(env, args[0], "onCall", &onCall); 
    // Call functions in the object 
    napi_value res; 
    napi_call_function(env, args[0], onCall, 0, nullptr, &res); 
    return onCall; 
} 
EXTERN_C_START 
static napi_value Init(napi_env env, napi_value exports) { 
    napi_property_descriptor desc[] = { 
        {"callFunction", nullptr, CallFunction, nullptr, nullptr, nullptr, napi_default, nullptr}}; 
    napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc); 
    return exports; 
} 
EXTERN_C_END
```

**Q：Native侧如何通过char指针构造ArrayBuffer数组？**

**A**：可以通过napi\_create\_arraybuffer接口实现。

```
#include "CharToArrBuffer.h" 
napi_value CharToArrBuffer::TestCharBuf(napi_env env, napi_callback_info info) { 
    napi_value result = nullptr; 
    char *buf = nullptr; 
    // Create an Array buffer 
    napi_create_arraybuffer(env, 100, reinterpret_cast<void **>(&buf), &result); 
    // Assign an ArrayBuffer 
    for (int i = 0; i < 100; i++) { 
        buf[i] = i + 2; 
    } 
    return result; 
}
```

**Q：通过ArkTS侧向Native侧注册日志监听接口，当在Native侧任一业务中调用日志接口时，日志将通过回调上报给ArkTS侧。是否可以提供一个示例？**

**A**：解决措施如下：

1. 在ArkTS侧新建Log.ts文件（注意文件扩展名为ts，而非ets），并使用单例模式封装日志监听接口。

   ```ts
   import { hilog } from '@kit.PerformanceAnalysisKit';

   export class GlobalThisAdapter {
     private constructor() {
     }

     private static instance: GlobalThisAdapter;
     private _logListener: LogsListener = new LogsListener();

     public static getInstance(): GlobalThisAdapter {
       if (!GlobalThisAdapter.instance) {
         GlobalThisAdapter.instance = new GlobalThisAdapter();
       }
       return GlobalThisAdapter.instance;
     }

     getLogsListener(): LogsListener | undefined {
       return this._logListener;
     }

     setLogsListener(value: LogsListener): void {
       this._logListener = value;
     }
   }

   export class LogsListener implements OnLogsListener {
     public constructor() {
     }

     onLogs(level: LogLevel, message: string): void {
       switch (level) {
         case LogLevel.DEBUG:
           hilog.debug(0x0000, 'debug', 'debug message is %{public}s', message);
           break;
         case LogLevel.INFO:
           hilog.info(0x0000, 'info', 'info message is %{public}s', message);
           break;
         case LogLevel.WARN:
           hilog.warn(0x0000, 'warn', 'warn message is %{public}s', message)
           break;
         case LogLevel.ERROR:
           hilog.error(0x0000, 'error', 'error message is %{public}s', message);
           break;
         case LogLevel.FATAL:
           hilog.fatal(0x0000, 'fatal', 'fatal message is %{public}s', message);
           break;
         default:
           hilog.info(0x0000, 'info', 'info message is %{public}s', message);
       }
     }
   }

   enum LogLevel {
     DEBUG = 3,
     INFO,
     WARN,
     ERROR,
     FATAL
   }

   export default interface OnLogsListener {
     onLogs(level: number, message: string): void;
   }
   ```
2. 在Native侧代码中添加接口实现。注意，napi\_create\_reference用于创建引用，napi\_ref由开发者管理对象的生命周期，不受NativeScope影响。通过napi\_get\_named\_property和napi\_call\_function获取OnLogsListener和onLogs，实现与 ArkTS 侧的绑定。

   ```ts
   #include "napi/native_api.h"
   #include <bits/alltypes.h>
   #include <cstring>
   #include <hilog/log.h>

   napi_ref logListenerRef = nullptr;
   napi_ref onLogsFuncRef = nullptr;
   static napi_value RegisterLogListener(napi_env env, napi_callback_info info) {
       size_t argc = 1;
       napi_value globalThisAdapter = nullptr;
       napi_get_cb_info(env, info, &argc, &globalThisAdapter, nullptr, nullptr);

       napi_value getLogListenerFunc = nullptr;
       napi_get_named_property(env, globalThisAdapter, "getLogsListener", &getLogListenerFunc);

       napi_value logListener = nullptr;
       napi_call_function(env, globalThisAdapter, getLogListenerFunc, 0, nullptr, &logListener);

       napi_value onLogsFunc = nullptr;
       napi_get_named_property(env, logListener, "onLogs", &onLogsFunc);

       napi_create_reference(env, logListener, 1, &logListenerRef);
       napi_create_reference(env, onLogsFunc, 1, &onLogsFuncRef);

       return nullptr;
   }
   ```
3. 在Native侧添加接口映射，以实现功能。

   ```cpp
   EXTERN_C_START
   static napi_value Init(napi_env env, napi_value exports) {
       napi_property_descriptor desc[] = {
           {"add", nullptr, Add, nullptr, nullptr, nullptr, napi_default, nullptr},
           {"registerLogListener", nullptr, RegisterLogListener, nullptr, nullptr, nullptr, napi_default, nullptr}};
       napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
       return exports;
   }
   EXTERN_C_END
   ```
4. 在index.t.ets中导出相关接口。

   ```ts
   import { GlobalThisAdapter } from '../../../ets/interface/Log'
   export const add: () => void;
   export const registerLogListener: (a: GlobalThisAdapter) => void;
   ```
5. 注册日志接口，调用registerLogListener将ArkTS侧的日志实现注册到Native侧。此处选择在EntryAbility.ets文件的onCreate方法中进行注册。

   ```ts
   onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
     let globalThisAdapter: GlobalThisAdapter = GlobalThisAdapter.getInstance();
     testNapi.registerLogListener(globalThisAdapter);
     hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
   }
   ```
6. 添加调用接口时的回调方法。在Native侧调用该方法即可实现ArkTS侧onLogs方法的回调。

   ```cpp
   static void callOnLogs(napi_env env, LogLevel level, const char *message) {

       size_t argc = 2;
       napi_value argv[2] = {nullptr};

       int32_t tem = level;
       napi_create_int32(env, tem, &argv[0]);
       napi_create_string_utf8(env, message, strlen(message) + 1, &argv[1]);
       napi_value logListener = nullptr;
       napi_value onLogsFunc = nullptr;
       napi_get_reference_value(env, logListenerRef, &logListener);
       napi_get_reference_value(env, onLogsFuncRef, &onLogsFunc);

       napi_call_function(env, logListener, onLogsFunc, argc, argv, nullptr);
   }
   ```
7. 调用其他业务代码。此处以Add方法为例，在该方法中调用callOnLogs方法，即可实现对ArkTS侧onLogs方法的回调。

   ```cpp
   static napi_value Add(napi_env env, napi_callback_info info) {
       callOnLogs(env, LogLevel::LOG_INFO, "execute native Add function success");
       return nullptr;
   }
   ```

**Q：如何在Native侧获取APP版本信息？**

**A**：Native侧目前没有获取APP版本信息的接口。如需获取APP版本信息，可以在ArkTS侧获取，然后传递到Native侧。

通过@kit.AbilityKit模块中的bundleManager查询bundleInfo。bundleInfo包含App版本号和版本名。

ArkTS侧传递数据到Native侧可参考链接：

```ts
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            bundleManager.getBundleInfoForSelf(bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION).then((bundleInfo)=>{
              let versionName = bundleInfo.versionName;//Application version name
              let versionNo = bundleInfo.versionCode;//Application version number
            }).catch((error : BusinessError)=>{
              console.error("get bundleInfo failed,error is "+error)})
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

ArkTS侧传递数据到Native侧可参考链接：[使用Node-API实现跨语言交互开发流程](../harmonyos-guides/use-napi-process.md)。

获取模块相关信息参考链接：[bundleInfo](../harmonyos-references/js-apis-bundlemanager-bundleinfo.md#bundleinfo-1)、[@ohos.bundle.bundleManager (应用程序包管理模块)](../harmonyos-references/js-apis-bundlemanager.md)。

**Q：如何在C++调用从ArkTS传递过来的function？**

**A**：具体步骤如下：

1. 在index.d.ts文件中，提供ArkTS侧的接口方法。

   ```ts
   export const nativeCallArkTS: (a: object) => number;
   ```
2. 实现Native侧的NativeCallArkTS接口，具体代码如下：

   ```cpp
   static napi_value NativeCallArkTS(napi_env env, napi_callback_info info) 
   {     
       size_t argc = 1; 
       // Declare parameter array 
       napi_value args[1] = {nullptr}; 

       // Retrieve the incoming parameters and sequentially place them into the parameter array 
       napi_get_cb_info(env, info, &argc, args , nullptr, nullptr); 

       // Create an int as a parameter for ArkTS
       napi_value argv = nullptr;     
       napi_create_int32(env, 2, &argv ); 

       // Call the incoming callback and return its result
       napi_value result = nullptr; 
       napi_call_function(env, nullptr, args[0], 1, &argv, &result); 
       return result; 
   }
   ```
3. 在ArkTS侧，通过nativeModule.nativeCallArkTS()方法传入回调函数。

   ```ts
   // entry/src/main/ets/pages/Index.ets
   // Introduce native capabilities through import.
   import nativeModule from 'libentry.so'

   @Entry
   @Component
   struct Index {
     @State message: string = 'Test Node-API nativeCallArkTS result: ';
     build() {
       Row() {
         Column() {
           // Call the nativeCallArkTS method, corresponding to the Native NativeCallArkTS, and call the ArkTS function in Native.
           Text(this.message)
             .fontSize(50)
             .fontWeight(FontWeight.Bold)
             .onClick(() => {
               this.message += nativeModule.nativeCallArkTS((a: number)=> {
                 return a * 2;
               });
             })
         }
         .width('100%')
       }
       .height('100%')
     }
   }
   ```

   参考链接：[Native侧方法的实现](../harmonyos-guides/use-napi-process.md#native侧方法的实现)。
