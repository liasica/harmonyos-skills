---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-44
title: 当跳转到新页面时提示登录超时，随后应用闪退
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 当跳转到新页面时提示登录超时，随后应用闪退
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:50+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:95c7c9d8a64054b018d8b747fde6a9c09375b14e2bb81e5955817dc13265442d
---

## 问题现象

应用加载新页面时，出现登录超时的弹窗，随后闪退。

## 背景知识

* JS Crash异常根据不同的异常场景，在Reason字段进行了分类，分为Error、TypeError、SyntaxError、ReferenceError、RangeError等错误类型。参考文档[JS Crash（进程崩溃）检测](../harmonyos-guides/jscrash-guidelines.md)。
* JS Crash日志规格说明可以参考[日志规格](../harmonyos-guides/jscrash-guidelines.md#日志规格)。
* 错误码[100001 接口调用异常错误码](../harmonyos-references/errorcode-internal.md#section100001-接口调用异常错误码)表示router内部错误，当出现了开发者解决不了的内部异常错误，系统会产生此错误码，并描述具体是哪种内部错误。

## 问题定位

1. 从faultlogger目录下获取到应用的JS Crash故障日志，故障原因是自定义错误类Error，故障信息为Internal error. UI execution context not found，错误码为100001。

   ```screen
   Reason:Error
   Error name:Error
   Error message:Internal error. UI execution context not found.
   Error code:100001
   Stacktrace:
   Cannot get SourceMap info, dump raw stack:
       at gotoLoginPage (entry|entry|1.0.0|src/main/ets/viewmodel/login/QuickLoginManager.ts:474:1)
       at anonymous (entry|entry|1.0.0|src/main/ets/h5common/plugin/JXPluginAlertInfo.ts:94:1)
       at anonymous (entry|entry|1.0.0|src/main/ets/widget/dialog/CustomWindowDialog.ts:67:1)
       at anonymous (entry|entry|1.0.0|src/main/ets/widget/dialog/CustomWindowDialog.ts:89:1)
       at (entry/src/main/ets/h5common/page/H5Page.ets:227:11)
   ```
2. 异常信息UI execution context not found表示没有获取到UI的执行上下文。排查栈顶函数gotoLoginPage是否直接使用了router跳转页面，此情况可能导致[UI上下文不明确](../harmonyos-guides/arkts-global-interface.md#ui上下文不明确)的问题。

## 分析结论

router没有获取到UI的执行上下文，导致页面闪退。

## 修改建议

* 方式一：

  通过使用[Class (UIContext)](../harmonyos-references/arkts-apis-uicontext-uicontext.md)中的[getRouter](../harmonyos-references/arkts-apis-uicontext-uicontext.md#getrouter)方法获取当前UI上下文关联的[Class (Router)](../harmonyos-references/arkts-apis-uicontext-router.md)对象，再通过该对象调用对应方法。可参考[pushUrl](../harmonyos-references/arkts-apis-uicontext-router.md#pushurl)中的示例，此页面路由方式不推荐，建议使用方式二。
* 方式二：

  [组件导航（Navigation）](../harmonyos-guides/arkts-navigation-navigation.md)具有更强的功能和自定义能力，推荐使用该组件作为应用的路由框架。Navigation和Router的差异可参考[Router切换Navigation](../harmonyos-guides/arkts-router-to-navigation.md)指导。
