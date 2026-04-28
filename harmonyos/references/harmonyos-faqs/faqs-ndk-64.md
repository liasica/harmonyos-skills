---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-64
title: 如何在ArkTS侧监听Native侧日志信息
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 如何在ArkTS侧监听Native侧日志信息
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:41+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:581b2868039e55ab5a5c2161cdfb5cb4c331d74a66810406aebf1b4340a8194b
---

**问题现象**

通过ArkTS侧向Native侧注册日志监听接口，当在Native侧任一业务中调用日志接口时，日志将通过回调上报给ArkTS侧。是否可以提供一个示例？

**解决措施**

1. 在ArkTS侧新建Log.ts文件（注意文件扩展名为ts，而非ets），并使用单例模式封装日志监听接口。

   ```
   1. import { hilog } from '@kit.PerformanceAnalysisKit';

   4. export class GlobalThisAdapter {
   5. private constructor() {
   6. }

   9. private static instance: GlobalThisAdapter;
   10. private _logListener: LogsListener = new LogsListener();

   13. public static getInstance(): GlobalThisAdapter {
   14. if (!GlobalThisAdapter.instance) {
   15. GlobalThisAdapter.instance = new GlobalThisAdapter();
   16. }
   17. return GlobalThisAdapter.instance;
   18. }

   21. getLogsListener(): LogsListener | undefined {
   22. return this._logListener;
   23. }

   26. setLogsListener(value: LogsListener): void {
   27. this._logListener = value;
   28. }
   29. }

   32. export class LogsListener implements OnLogsListener {
   33. public constructor() {
   34. }

   37. onLogs(level: LogLevel, message: string): void {
   38. switch (level) {
   39. case LogLevel.DEBUG:
   40. hilog.debug(0x0000, 'debug', 'debug message is %{public}s', message);
   41. break;
   42. case LogLevel.INFO:
   43. hilog.info(0x0000, 'info', 'info message is %{public}s', message);
   44. break;
   45. case LogLevel.WARN:
   46. hilog.warn(0x0000, 'warn', 'warn message is %{public}s', message)
   47. break;
   48. case LogLevel.ERROR:
   49. hilog.error(0x0000, 'error', 'error message is %{public}s', message);
   50. break;
   51. case LogLevel.FATAL:
   52. hilog.fatal(0x0000, 'fatal', 'fatal message is %{public}s', message);
   53. break;
   54. default:
   55. hilog.info(0x0000, 'info', 'info message is %{public}s', message);
   56. }
   57. }
   58. }

   61. enum LogLevel {
   62. DEBUG = 3,
   63. INFO,
   64. WARN,
   65. ERROR,
   66. FATAL
   67. }

   70. export default interface OnLogsListener {
   71. onLogs(level: number, message: string): void;
   72. }
   ```

   [Log.ts](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/LogListener/src/main/ets/interface/Log.ts#L20-L91)
2. 在Native侧代码中添加接口实现。注意，napi\_create\_reference用于创建引用，napi\_ref由开发者管理对象的生命周期，不受NativeScope影响。通过napi\_get\_named\_property和napi\_call\_function获取OnLogsListener和onLogs，实现与 ArkTS 侧的绑定。

   ```
   1. #include "napi/native_api.h"
   2. #include <bits/alltypes.h>
   3. #include <cstring>
   4. #include <hilog/log.h>

   7. napi_ref logListenerRef = nullptr;
   8. napi_ref onLogsFuncRef = nullptr;
   9. static napi_value RegisterLogListener(napi_env env, napi_callback_info info) {
   10. size_t argc = 1;
   11. napi_value globalThisAdapter = nullptr;
   12. napi_get_cb_info(env, info, &argc, &globalThisAdapter, nullptr, nullptr);

   15. napi_value getLogListenerFunc = nullptr;
   16. napi_get_named_property(env, globalThisAdapter, "getLogsListener", &getLogListenerFunc);

   19. napi_value logListener = nullptr;
   20. napi_call_function(env, globalThisAdapter, getLogListenerFunc, 0, nullptr, &logListener);

   23. napi_value onLogsFunc = nullptr;
   24. napi_get_named_property(env, logListener, "onLogs", &onLogsFunc);

   27. napi_create_reference(env, logListener, 1, &logListenerRef);
   28. napi_create_reference(env, onLogsFunc, 1, &onLogsFuncRef);

   31. return nullptr;
   32. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/LogListener/src/main/cpp/napi_init.cpp#L19-L50)
3. 在Native侧添加接口映射，以实现功能。

   ```
   1. EXTERN_C_START
   2. static napi_value Init(napi_env env, napi_value exports) {
   3. napi_property_descriptor desc[] = {
   4. {"add", nullptr, Add, nullptr, nullptr, nullptr, napi_default, nullptr},
   5. {"registerLogListener", nullptr, RegisterLogListener, nullptr, nullptr, nullptr, napi_default, nullptr}};
   6. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
   7. return exports;
   8. }
   9. EXTERN_C_END
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/LogListener/src/main/cpp/napi_init.cpp#L82-L90)
4. 在index.t.ets中导出相关接口。

   ```
   1. import { GlobalThisAdapter } from '../../../ets/interface/Log'
   2. export const add: () => void;
   3. export const registerLogListener: (a: GlobalThisAdapter) => void;
   ```

   [Index.d.ts](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/LogListener/src/main/cpp/types/libloglistener/Index.d.ts#L20-L22)
5. 注册日志接口，调用registerLogListener将ArkTS侧的日志实现注册到Native侧。此处选择在EntryAbility.ets文件的onCreate方法中进行注册。

   ```
   1. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
   2. let globalThisAdapter: GlobalThisAdapter = GlobalThisAdapter.getInstance();
   3. testNapi.registerLogListener(globalThisAdapter);
   4. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
   5. }
   ```

   [LogListenerAbility.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/LogListener/src/main/ets/loglistenerability/LogListenerAbility.ets#L29-L33)
6. 添加调用接口时的回调方法。在Native侧调用该方法即可实现ArkTS侧onLogs方法的回调。

   ```
   1. static void callOnLogs(napi_env env, LogLevel level, const char *message) {

   4. size_t argc = 2;
   5. napi_value argv[2] = {nullptr};

   8. int32_t tem = level;
   9. napi_create_int32(env, tem, &argv[0]);
   10. napi_create_string_utf8(env, message, strlen(message) + 1, &argv[1]);
   11. napi_value logListener = nullptr;
   12. napi_value onLogsFunc = nullptr;
   13. napi_get_reference_value(env, logListenerRef, &logListener);
   14. napi_get_reference_value(env, onLogsFuncRef, &onLogsFunc);

   17. napi_call_function(env, logListener, onLogsFunc, argc, argv, nullptr);
   18. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/LogListener/src/main/cpp/napi_init.cpp#L54-L71)
7. 调用其他业务代码。此处以Add方法为例，在该方法中调用callOnLogs方法，即可实现对ArkTS侧onLogs方法的回调。

   ```
   1. static napi_value Add(napi_env env, napi_callback_info info) {
   2. callOnLogs(env, LogLevel::LOG_INFO, "execute native Add function success");
   3. return nullptr;
   4. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/LogListener/src/main/cpp/napi_init.cpp#L75-L78)
