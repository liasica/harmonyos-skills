---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-address-sanitizer-events-arkts
title: 订阅地址越界事件（ArkTS）
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 事件订阅 > 使用HiAppEvent订阅事件 > 系统事件 > 地址越界事件 > 订阅地址越界事件（ArkTS）
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:06+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:efa278967d4237bbf766a8da86a6738c8ed7c1e5908ff7ecc47c2f1e21431c10
---

## 接口说明

API接口的具体使用说明（参数使用限制、具体取值范围等）请参考[@ohos.hiviewdfx.hiAppEvent](../harmonyos-references/js-apis-hiviewdfx-hiappevent.md)。

| 接口名 | 描述 |
| --- | --- |
| addWatcher(watcher: Watcher): AppEventPackageHolder | 添加应用事件观察者，以添加对应用事件的订阅。 |
| removeWatcher(watcher: Watcher): void | 移除应用事件观察者，以移除对应用事件的订阅。 |

## 开发步骤

以实现对写数组越界场景生成的地址越界事件订阅为例，说明开发步骤。

### 步骤一：新建工程

1. 新建Native C++工程，目录结构如下：

   ```
   1. entry:
   2. src:
   3. main:
   4. cpp:
   5. - types:
   6. libentry:
   7. - index.d.ts
   8. - CMakeLists.txt
   9. - napi_init.cpp
   10. ets:
   11. - entryability:
   12. - EntryAbility.ets
   13. - pages:
   14. - Index.ets
   ```
2. 编辑工程中的“entry > src > main > ets > entryability > EntryAbility.ets”文件，导入依赖模块：

   ```
   1. import { hiAppEvent, hilog } from '@kit.PerformanceAnalysisKit';
   ```

### 步骤二：订阅地址越界事件

1. 编辑工程中的“entry > src > main > ets > entryability > EntryAbility.ets”文件，在onCreate函数中添加系统事件的订阅，示例代码如下

   ```
   1. hiAppEvent.addWatcher({
   2. // 开发者可以自定义观察者名称，系统会使用名称来标识不同的观察者
   3. name: "watcher",
   4. // 开发者可以订阅感兴趣的系统事件，此处是订阅了地址越界事件
   5. appEventFilters: [
   6. {
   7. domain: hiAppEvent.domain.OS,
   8. names: [hiAppEvent.event.ADDRESS_SANITIZER]
   9. }
   10. ],
   11. // 开发者可以自行实现订阅系统事件回调函数，以便对订阅获取到的事件数据进行自定义处理
   12. onReceive: (domain: string, appEventGroups: Array<hiAppEvent.AppEventGroup>) => {
   13. hilog.info(0x0000, 'testTag', `HiAppEvent onReceive: domain=${domain}`);
   14. for (const eventGroup of appEventGroups) {
   15. // 开发者可以根据事件集合中的事件名称区分不同的系统事件
   16. hilog.info(0x0000, 'testTag', `HiAppEvent eventName=${eventGroup.name}`);
   17. for (const eventInfo of eventGroup.appEventInfos) {
   18. // 开发者可以对事件集合中的事件数据进行自定义处理，此处是将事件数据打印在日志中
   19. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.domain=${eventInfo.domain}`);
   20. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.name=${eventInfo.name}`);
   21. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.eventType=${eventInfo.eventType}`);
   22. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.time=${eventInfo.params['time']}`);
   23. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.bundle_version=${eventInfo.params['bundle_version']}`);
   24. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.bundle_name=${eventInfo.params['bundle_name']}`);
   25. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.pid=${eventInfo.params['pid']}`);
   26. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.uid=${eventInfo.params['uid']}`);
   27. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.type=${eventInfo.params['type']}`);
   28. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.external_log=${JSON.stringify(eventInfo.params['external_log'])}`);
   29. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.log_over_limit=${eventInfo.params['log_over_limit']}`);
   30. }
   31. }
   32. }
   33. });
   ```

### 步骤三：构造地址越界错误

1. 编辑“entry > src > main > cpp > napi\_init.cpp”文件，该文件实现地址越界场景，并提供NAPI接口给应用层代码调用，完整示例代码如下：

   ```
   1. #include "napi/native_api.h"

   3. static napi_value Test(napi_env env, napi_callback_info info)
   4. {
   5. int a[10];
   6. // 构造数组越界写入
   7. a[10] = 1;
   8. return {};
   9. }

   11. EXTERN_C_START
   12. static napi_value Init(napi_env env, napi_value exports)
   13. {
   14. napi_property_descriptor desc[] = {
   15. { "test", nullptr, Test, nullptr, nullptr, nullptr, napi_default, nullptr }
   16. };
   17. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
   18. return exports;
   19. }
   20. EXTERN_C_END

   22. static napi_module demoModule = {
   23. .nm_version = 1,
   24. .nm_flags = 0,
   25. .nm_filename = nullptr,
   26. .nm_register_func = Init,
   27. .nm_modname = "entry",
   28. .nm_priv = ((void*)0),
   29. .reserved = { 0 }
   30. };

   32. extern "C" __attribute__((constructor)) void RegisterEntryModule(void)
   33. {
   34. napi_module_register(&demoModule);
   35. }
   ```
2. 编辑“entry > src > main > cpp > types > libentry > index.d.ts”文件，完整示例代码如下：

   ```
   1. export const test: () => void;
   ```
3. 编辑工程中的“entry > src > main > ets > pages > Index.ets”文件，新增按钮触发地址越界事件：

   ```
   1. import testNapi from 'libentry.so';

   3. @Entry
   4. @Component
   5. struct Index {
   6. build() {
   7. Row() {
   8. Column() {
   9. Button("address-sanitizer").onClick(() => {
   10. testNapi.test();
   11. })
   12. }
   13. .width('100%')
   14. }
   15. .height('100%')
   16. }
   17. }
   ```
4. 点击DevEco Studio界面中的“entry”，点击“Edit Configurations”，点击“Diagnostics”，勾选“Address Sanitizer”，保存设置。点击DevEco Studio界面中的运行按钮，运行应用工程，然后在应用界面中点击按钮“address-sanitizer”，触发一次地址越界事件。应用崩溃后重新进入应用，可以在Log窗口看到对系统事件数据的处理日志：

   ```
   1. HiAppEvent onReceive: domain=OS
   2. HiAppEvent eventName=ADDRESS_SANITIZER
   3. HiAppEvent eventInfo.domain=OS
   4. HiAppEvent eventInfo.name=ADDRESS_SANITIZER
   5. HiAppEvent eventInfo.eventType=1
   6. HiAppEvent eventInfo.time=1713161197957
   7. HiAppEvent eventInfo.bundle_version=1.0.0
   8. HiAppEvent eventInfo.bundle_name=com.example.myapplication
   9. HiAppEvent eventInfo.pid=12889
   10. HiAppEvent eventInfo.uid=20020140
   11. HiAppEvent eventInfo.type=stack-buffer-overflow
   12. HiAppEvent eventInfo.external_log=["/data/storage/el2/log/hiappevent/ADDRESS_SANITIZER_1713161197960_12889.log"]
   13. HiAppEvent eventInfo.log_over_limit=false
   ```
