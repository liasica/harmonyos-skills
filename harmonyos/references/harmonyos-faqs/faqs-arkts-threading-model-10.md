---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-threading-model-10
title: 冷启动产生ArkCompiler错误日志
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > 冷启动产生ArkCompiler错误日志
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:54+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:35b0b1818e704c5f0b6372580c07f59d8c9c759e2bb822f6e443800359b0eb58
---

## 问题现象

应用冷启动会产生ArkCompiler错误日志，应用可以正常编译并运行，报错如下：

```shell
07-14 23:03:42.131   C03F00/com.example.demo/ArkCompiler  E     ReferenceError: Observed is not defined
                                                               at func_main_0 (phone|ui|1.0.0|src/main/ets/dialog/components/CommonDialogView.ts:31:2)
07-14 23:03:42.131   C03F00/com.example.demo/ArkCompiler  E     ReferenceError: Observed is not defined
                                                               at func_main_0 (phone|ui|1.0.0|src/main/ets/dialog/components/DialogView.ts:137:2)
07-14 23:03:42.131   C03F00/com.example.demo/ArkCompiler  E     ReferenceError: ViewV2 is not defined
                                                               at func_main_0 (phone|ui|1.0.0|src/main/ets/base/SectionCell.ts:28:40)
07-14 23:03:42.131   C03F00/com.example.demo/ArkCompiler  E     ReferenceError: Trace is not defined
                                                               at func_main_0 (phone|ui|1.0.0|src/main/ets/chart/beans/ChartBean.ts:37:6)
07-14 23:03:42.131   C03F00/com.example.demo/ArkCompiler  E     ReferenceError: Trace is not defined
                                                               at func_main_0 (phone|ui|1.0.0|src/main/ets/chart/model/core/Legend.ts:33:6)
07-14 23:03:42.131   C03F00/com.example.demo/ArkCompiler  E     ReferenceError: AppStorageV2Impl is not defined
                                                               at func_main_0 (../../../foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/engine/jsStateManagement.js:67:1)
07-14 23:03:42.131   C03F00/com.example.demo/ArkCompiler  E     ReferenceError: Trace is not defined
                                                               at func_main_0 (phone|ui|1.0.0|src/main/ets/chart/model/ChartController.ts:8:6)
07-14 23:03:42.131   C03F00/com.example.demo/ArkCompiler  E     ReferenceError: ViewV2 is not defined
                                                               at func_main_0 (phone|ui|1.0.0|src/main/ets/chart/components/ChartBaseView.ts:5:36)
07-14 23:03:42.131   C03F00/com.example.demo/ArkCompiler  E     ReferenceError: ViewV2 is not defined
                                                               at func_main_0 (phone|ui|1.0.0|src/main/ets/chart/components/BarChartView.ts:22:35)
07-14 23:03:42.131   C03F00/com.example.demo/ArkCompiler  E     ReferenceError: ViewV2 is not defined
                                                               at func_main_0 (phone|ui|1.0.0|src/main/ets/chart/components/LineChartView.ts:32:36)
07-14 23:03:42.131   C03F00/com.example.demo/ArkCompiler  E     ReferenceError: ViewV2 is not defined
                                                               at func_main_0 (phone|ui|1.0.0|src/main/ets/base/SegmentedButton.ts:12:38)
07-14 23:03:42.132   C03F00/com.example.demo/ArkCompiler  E     ReferenceError: ViewV2 is not defined
                                                               at func_main_0 (phone|phone|1.0.0|src/main/ets/base/audio/AudioStatusIndicator.ts:13:43)
07-14 23:03:42.133   C03F00/com.example.demo/ArkCompiler  E     ReferenceError: Observed is not defined
                                                               at func_main_0 (@hadss/hmrouter|@hadss/hmrouter|1.0.0-rc.11|src/main/ets/template/AnimatorModel.ts:15:2)
07-14 23:03:42.133   C03F00/com.example.demo/ArkCompiler  E     ReferenceError: Trace is not defined
                                                               at func_main_0 (phone|phone|1.0.0|src/main/ets/base/popup/basePopup/BasePopupController.ts:14:6)
07-14 23:03:42.133   C03F00/com.example.demo/ArkCompiler  E     ReferenceError: ObservedV2 is not defined
                                                               at func_main_0 (phone|phone|1.0.0|src/main/ets/base/popup/basePopup/BasePopupView.ts:17:2)
07-14 23:03:42.133   C03F00/com.example.demo/ArkCompiler  E     ReferenceError: Trace is not defined
                                                               at func_main_0 (phone|phone|1.0.0|src/main/ets/base/popup/dialog/DialogConstants.ts:33:6)
07-14 23:03:42.133   C03F00/com.example.demo/ArkCompiler  E     ReferenceError: ViewV2 is not defined
                                                               at func_main_0 (phone|phone|1.0.0|src/main/ets/base/popup/dialog/DialogContentView.ts:66:42)
07-14 23:03:42.133   C03F00/com.example.demo/ArkCompiler  E     ReferenceError: ViewV2 is not defined
                                                               at func_main_0 (phone|phone|1.0.0|src/main/ets/base/popup/dialog/MMDialogRouterView.ts:20:43)
07-14 23:03:42.133   C03F00/com.example.demo/ArkCompiler  E     ReferenceError: ViewV2 is not defined
                                                               at func_main_0 (phone|phone|1.0.0|src/main/ets/base/popup/dialog/DialogView.ts:56:35)
07-14 23:03:42.133   C03F00/com.example.demo/ArkCompiler  E     ReferenceError: ViewV2 is not defined
                                                               at func_main_0 (phone|phone|1.0.0|src/main/ets/base/popup/anchorPopup/AnchorPopupRouter.ts:23:44)
07-14 23:03:42.133   C03F00/com.example.demo/ArkCompiler  E     ReferenceError: ViewV2 is not defined
                                                               at func_main_0 (phone|phone|1.0.0|src/main/ets/base/popup/anchorPopup/AnchorPopup.ts:25:38)
07-14 23:03:42.133   C03F00/com.example.demo/ArkCompiler  E     ReferenceError: ViewV2 is not defined
                                                               at func_main_0 (phone|phone|1.0.0|src/main/ets/base/popup/centerPopup/CenterPopup.ts:82:38)
07-14 23:03:42.133   C03F00/com.example.demo/ArkCompiler  E     ReferenceError: ViewV2 is not defined
                                                               at func_main_0 (phone|phone|1.0.0|src/main/ets/base/popup/menu/MenuPopupRouter.ts:24:42)
07-14 23:03:42.133   C03F00/com.example.demo/ArkCompiler  E     ReferenceError: ViewV2 is not defined
                                                               at func_main_0 (phone|phone|1.0.0|src/main/ets/base/popup/menu/MenuPopup.ts:28:36)
07-14 23:03:42.134   C03F00/com.example.demo/ArkCompiler  E     ReferenceError: Trace is not defined
                                                               at func_main_0 (phone|phone|1.0.0|src/main/ets/base/popup/loading/LoadingPopup.ts:31:6)
07-14 23:03:42.134   C03F00/com.example.demo/ArkCompiler  E     ReferenceError: LoadingPopupBuilder is not initialized
                                                               at loading (phone|phone|1.0.0|src/main/ets/base/popup/MMPopup.ts:28:16)
                                                               at MMPopup (phone|phone|1.0.0|src/main/ets/base/popup/MMPopup.ts:12:27)
                                                               at func_main_0 (phone|phone|1.0.0|src/main/ets/base/popup/MMPopup.ts:1:1)
07-14 23:03:42.139   C03F00/com.example.demo/ArkCompiler  E     ReferenceError: ViewV2 is not defined
                                                               at func_main_0 (phone|phone|1.0.0|src/main/ets/base/components/NavigationBar.ts:34:36)
07-14 23:03:42.139   C03F00/com.example.demo/ArkCompiler  E     ReferenceError: ViewV2 is not defined
                                                               at func_main_0 (phone|phone|1.0.0|src/main/ets/user/profile/components/PrivilegeDialog.ts:66:45)
07-14 23:03:42.139   C03F00/com.example.demo/ArkCompiler  E     ReferenceError: ViewV2 is not defined
                                                               at func_main_0 (phone|phone|1.0.0|src/main/ets/base/components/SharedViews.ts:6:33)
07-14 23:03:42.139   C03F00/com.example.demo/ArkCompiler  E     ReferenceError: Trace is not defined
                                                               at func_main_0 (phone|phone|1.0.0|src/main/ets/payment/components/ThirdPartyPaymentOptionsView.ts:13:6)
07-14 23:03:42.139   C03F00/com.example.demo/ArkCompiler  E     ReferenceError: ViewV2 is not defined
                                                               at func_main_0 (phone|phone|1.0.0|src/main/ets/payment/components/PaymentComponent.ts:10:39)
```

## 背景知识

ArkTS提供了[TaskPool](../harmonyos-guides/taskpool-introduction.md)与[Worker](../harmonyos-guides/worker-introduction.md)两种多线程并发方案，TaskPool与Worker两种多线程并发能力均是基于Actor并发模型实现的。Worker主、子线程通过收发消息进行通信；TaskPool基于Worker做了更多场景化的功能封装，例如支持任务组TaskGroup、任务优先级设置、取消任务等功能，且可以根据任务数量进行自动的扩容与缩容，还可以根据任务优先级进行任务调度。

## 问题定位

排查是否在子线程中加载UI属性，导致UI装饰器或状态变量即使没有被显式调用也可能会被解析执行，访问时会抛出异常。

## 分析结论

在子线程中加载了UI属性，标记了Observed装饰器的类无法在子线程中初始化，会影响到同一个文件里的其他类的初始化，但是不影响正常编译。

## 修改建议

将[@Observed](../harmonyos-guides/arkts-observed-and-objectlink.md)、[AppStorage](../harmonyos-guides/arkts-appstorage.md)等UI装饰器或状态变量和其他的类分开，具体参考：[根据业务场景合理划分项目结构，避免在子线程中直接或间接引入UI](../harmonyos-guides/task-pool-usage-guidelines.md#根据业务场景合理划分项目结构避免在子线程中直接或间接引入ui)的正例部分。
