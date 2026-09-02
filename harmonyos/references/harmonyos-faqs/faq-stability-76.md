---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-76
title: ArkTS主线程执行高复杂度循环逻辑导致APP_INPUT_BLOCK卡顿
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > ArkTS主线程执行高复杂度循环逻辑导致APP_INPUT_BLOCK卡顿
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:50+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9d129389bb109c08c7c21c1d0b78c555137d647e8a1cc542c183fc9a0695a5d9
---

## 问题现象

应用在使用过程中出现界面无响应的情况，点击屏幕无法触发任何操作。

## 背景知识

在HarmonyOS应用开发中，主线程（UI线程）主要负责UI的构建、刷新以及响应用户的输入事件（如点击、滑动）。

1. **APP\_INPUT\_BLOCK**：当主线程被某个耗时任务长时间占用（通常超过5秒），导致输入事件（Input Event）积压在队列中无法被及时处理，系统会判定为输入阻塞故障。
2. **ArkTS容器性能**：ArkTS提供了丰富的数组操作方法（如forEach、findIndex等）。如果开发者在处理大量数据时，在主线程中使用嵌套循环（例如在forEach循环内部再次调用findIndex），会导致算法的时间复杂度呈指数级上升（O(N²)）。当数据量达到一定规模时，计算耗时会瞬间阻塞主线程。

## 问题定位

分析appfreeze日志可以按以下步骤进行：

1. **确认故障类型与时间**：

   在日志头部确认EVENTNAME为APP\_INPUT\_BLOCK，并记录TIMESTAMP（例如：2026/01/06-17:45:08）。

   ```text
   DOMAIN = AAFWK
   EVENTNAME = APP_INPUT_BLOCK
   TIMESTAMP = 2026/01/06-17:45:08:167
   PID = 20289
   UID = 20020212
   TID = 20289
   PACKAGE_NAME = com.jd.app.reader.hos
   PROCESS_NAME = com.jd.app.reader.hos
   ```
2. **检查主线程当前任务**：

   查找Main handler dump部分，观察Current Running的任务信息。
   * **输入**：查看start at时间与故障上报时间Fault time的差值。
   * **输出**：如果差值超过5秒，且task name为uv\_io\_cb（通常代表JS/ArkTS的回调任务），说明主线程正被该任务阻塞。

   ```text
   Current Running: start at 2026-01-06 17:44:59.785...
   Fault time: 2026-01-06 17:45:05...
   // 耗时约6秒
   Current Running: start at 2026-01-06 17:44:59.785, Event { send thread = 20580, send time = 2026-01-06 17:44:59.778, handle time = 2026-01-06 17:44:59.778, trigger time = 2026-01-06 17:44:59.785, task name = uv_io_cb, caller = [ohos_js_environment_impl.cpp(PostTaskToHandler:70)] }
   ```
3. **分析堆栈信息（关键步骤）**：

   查找Catche stack trace部分，重点关注主线程（Tid与Pid相同）的堆栈。

   例如日志中显示：

   ```text
   #01 at anonymous (bookshelf|src/main/ets/BookShelfModule.ts:766:1)
   #02 pc ... BuiltinStub_ArrayFindIndexStwCopy... // 正在执行查找
   #04 at anonymous (bookshelf|src/main/ets/BookShelfModule.ts:765:42)
   #05 pc ... BuiltinStub_ArrayForEachStwCopy...   // 正在执行遍历
   ```

   这表明在BookShelfModule.ts的第764-766行，存在forEach循环内部嵌套findIndex的操作。

## 分析结论

导致应用出现APP\_INPUT\_BLOCK的原因是主线程执行了高复杂度的ArkTS业务逻辑。

具体表现为：在数据库回调或数据同步过程中，代码对两个较大的数组进行了嵌套遍历（双重循环）。例如在外层使用forEach遍历数组A，在内层使用findIndex遍历数组B查找匹配项。这种操作的时间复杂度为O(N\*M)，当数据量较大时（例如数千条数据），计算量会造成主线程长时间卡死，无法响应后续的VIP输入事件（如MMI::OnPointerEvent），最终触发系统看门狗机制报错。

## 修改建议

建议通过优化算法降低时间复杂度，或者将耗时任务移至后台线程处理。
