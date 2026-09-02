---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-34
title: 页面内容在加载过程中，卡死无响应
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 页面内容在加载过程中，卡死无响应
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f497d133e37482b4f0c814df07d96bc44e3698b7374df6b0e1b2b8720769c115
---

## 问题现象

应用页面在加载内容的过程中，长时间无响应。

## 背景知识

* 用户在使用应用时，如果出现点击无反应或应用无响应等情况，并且持续时间超过一定限制，就会被定义为应用无响应，详情参考[AppFreeze（应用冻屏）检测](../harmonyos-guides/appfreeze-guidelines.md)。
* AppFreeze日志规格说明可以参考[日志规格](../harmonyos-guides/appfreeze-guidelines.md#日志规格)。
* vSyncTask是每帧的刷新，这种任务一秒执行几十次，如果耗时过长，一般原因可能是组件太复杂，例如长列表。

## 问题定位

1. 从日志中看到，故障是APP\_INPUT\_BLOCK，上报的原因是：User input does not respond!用户输入事件没有响应。查看主线程的任务从10:46:31到Fault time:10:46:37都没执行完，没有反馈，导致超时。且当前执行的任务为vSyncTask，可能是组件渲染太复杂。

   ```shell
   EVENTNAME = APP_INPUT_BLOCK
   PID = 38709
   PACKAGE_NAME = com.hx.example
   MSG = Fault time:2025/07/03-10:46:37
   User input does not respond!
   mainHandler dump is:
    EventHandler dump begin curTime: 2025-07-03 10:46:38.178
    Event runner (Thread name = , Thread ID = 11839) is running
    Current Running: start at 2025-07-03 10:46:31.327, Event { send thread = 11839, send time = 2025-07-03 10:46:31.327, handle time = 2025-07-03 10:46:31.327, trigger time = 2025-07-03 10:46:31.327, task name = vSyncTask, caller = [event_queue.cpp(HandleFileDescriptorEvent:280)] }
   ```
2. 观察到堆栈中有ListItem字段，很可能是长列表的加载耗时过长，排查堆栈中调用的应用函数，检查是否存在长列表情况。

   ```shell
   Tid:11839, Name:com.hx.example
   #00 pc 00000000009c34d8 /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::NG::FrameNode::GetAncestorNodeOfFrame(bool) const+284)(2ce844c3afc83b8cbb8a679c99508b7c)
   #01 pc 0000000000dad750 /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::NG::WaterFlowItemNode::RequestParentDirty()+52)(2ce844c3afc83b8cbb8a679c99508b7c)
   #02 pc 000000000187ef00 /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::NG::FrameNode::MarkDirtyNode(bool, bool, unsigned int)+416)(2ce844c3afc83b8cbb8a679c99508b7c)
   #03 pc 0000000000d3bcc4 /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::NG::FrameNode::RequestParentDirty()+1100)(2ce844c3afc83b8cbb8a679c99508b7c)
   #04 pc 000000000187ef00 /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::NG::FrameNode::MarkDirtyNode(bool, bool, unsigned int)+416)(2ce844c3afc83b8cbb8a679c99508b7c)
   #05 pc 0000000000d3bcc4 /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::NG::FrameNode::RequestParentDirty()+1100)(2ce844c3afc83b8cbb8a679c99508b7c)
   #06 pc 000000000187ef00 /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::NG::FrameNode::MarkDirtyNode(bool, bool, unsigned int)+416)(2ce844c3afc83b8cbb8a679c99508b7c)
   #07 pc 0000000000d3bcc4 /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::NG::FrameNode::RequestParentDirty()+1100)(2ce844c3afc83b8cbb8a679c99508b7c)
   #08 pc 000000000187ef00 /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::NG::FrameNode::MarkDirtyNode(bool, bool, unsigned int)+416)(2ce844c3afc83b8cbb8a679c99508b7c)
   #09 pc 0000000000bd5dc8 /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::NG::ListItemPattern::SetEndNode(OHOS::Ace::RefPtr<OHOS::Ace::NG::UINode> const&)+456)(2ce844c3afc83b8cbb8a679c99508b7c)
   #10 pc 0000000000bd5288 /system/lib64/platformsdk/libace_compatible.z.so(2ce844c3afc83b8cbb8a679c99508b7c)
   #11 pc 0000000000c76f38 /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::Framework::JSListItem::ParseSwiperAction(OHOS::Ace::Framework::JsiRef<OHOS::Ace::Framework::JsiObject> const&, OHOS::Ace::Framework::JsiExecutionContext const&)+2784)(2ce844c3afc83b8cbb8a679c99508b7c)
   #12 pc 0000000000c76414 /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::Framework::JSListItem::SetSwiperAction(OHOS::Ace::Framework::JsiCallbackInfo const&)+164)(2ce844c3afc83b8cbb8a679c99508b7c)
   #13 pc 0000000000de7880 /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::Framework::JsiClass<OHOS::Ace::Framework::JSListItem>::JSStaticMethodCallback(panda::JsiRuntimeCallInfo*)+196)(2ce844c3afc83b8cbb8a679c99508b7c)
   #14 pc 0000000000589de8 /system/lib64/platformsdk/libark_jsruntime.so(panda::Callback::RegisterCallback(panda::ecmascript::EcmaRuntimeCallInfo*)+272)(0d69a79f2a5bf79a69fb024e1aa5e02f)
   #15 pc 0000000000445a2c /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+40)
   #16 at itemCreation2 (entry|entry|1.0.0|src/main/ets/pages/Index.ts:1814:1)
   #17 at itemCreation (entry|entry|1.0.0|src/main/ets/pages/Index.ts:1806:1)
   #18 at deepRenderFunction (entry|entry|1.0.0|src/main/ets/pages/Index.ts:1822:1)
   ```

## 分析结论

应用组件太复杂，渲染时间过长，vSyncTask任务超时，导致页面卡死。

## 修改建议

控制页面渲染的逻辑，考虑大量组件、频繁刷新等场景，简化布局、异步处理，避免组件渲染时间过长，参考文档[界面渲染性能优化](../best-practices/bpta-developing-high-performance-ui.md)。

还可以通过@kit.ArkUI.inspector(布局回调)接口获取绘制完成回调的通知，计算组件渲染耗时，参考[如何获取组件渲染完成时间](faqs-arkui-302.md)。
