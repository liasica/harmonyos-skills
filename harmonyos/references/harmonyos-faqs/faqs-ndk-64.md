---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-64
title: 如何在ArkTS侧监听Native侧日志信息
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 如何在ArkTS侧监听Native侧日志信息
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5263b27339ea08e9fad2de98499de0ea317d68dd789d699bb7eefb6d8c556421
---

**问题现象**

通过ArkTS侧向Native侧注册日志监听接口，当在Native侧任一业务中调用日志接口时，日志将通过回调上报给ArkTS侧。是否可以提供一个示例？

**解决措施**

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

   ```cpp
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
