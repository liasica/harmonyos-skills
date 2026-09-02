---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-45
title: 应用在背单词过程中出现闪退
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 应用在背单词过程中出现闪退
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:50+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8a13d7206be24dad9caf7e79eeea35049374c59d95c29340e0a35ae128d4f28f
---

## 问题现象

应用在使用背单词功能时，发生闪退。

## 背景知识

* JsCrash异常根据不同的异常场景，在Reason字段进行了分类，分为Error、TypeError、SyntaxError、ReferenceError、RangeError等错误类型。参考文档[JS Crash（进程崩溃）检测](../harmonyos-guides/jscrash-guidelines.md)。
* JsCrash日志规格说明可以参考[日志规格](../harmonyos-guides/jscrash-guidelines.md#日志规格)。
* process.ProcessManager().exit()：[exit](../harmonyos-references/js-apis-process.md#exit9)接口用于终止当前进程，请谨慎使用此接口，此接口调用后应用会退出，如果入参非0会产生数据丢失或者异常情况。

## 问题定位

1. 从faultlogger目录下未能获取到应用相关故障日志。
2. 在hilog日志中搜索关键字exit with code，退出码为1，应用很可能调用了process.ProcessManager().exit(1)接口主动退出了程序。

   ```shell
   07-21 13:16:57.700   655   655 W C02C11/appspawn/APPSPAWN: [appspawn_service.c:139]com.hx.example with pid 37605 exit with code:1
   ```
3. 向前排查退出原因，发现应用打印了Error自定义错误，异常信息是level config not found not matched to current user未找到与当前用户匹配的级别配置。

   ```shell
   07-21 13:16:57.524 37605 37605 E A03D00/com.hx.example/JSAPP: onRejection, name:  Error
   07-21 13:16:57.524 37605 37605 E A03D00/com.hx.example/JSAPP: onRejection, message:  level config not found not matched to current user
   07-21 13:16:57.524 37605 37605 E A03D00/com.hx.example/JSAPP: onRejection, stack:  Cannot get SourceMap info, dump raw stack:
   07-21 13:16:57.524 37605 37605 E A03D00/com.hx.example/JSAPP:     at loadLevelConfig (phone|phone|1.0.0|src/main/ets/l2/v3/w3.ts:143:1)
   ```
4. 排查堆栈中的相关代码，应用是否在打印异常后，主动调用了[process.ProcessManager().exit()](../harmonyos-references/js-apis-process.md#exit9)退出了进程。

## 分析结论

应用捕获并打印异常后，主动调用了[process.ProcessManager().exit()](../harmonyos-references/js-apis-process.md#exit9)接口退出了程序，导致闪退现象。

## 修改建议

尽量避免出现异常场景或者使用try-catch捕获并处理异常。

谨慎使用[process.ProcessManager().exit()](../harmonyos-references/js-apis-process.md#exit9)接口，如果入参非0会产生数据丢失或者异常情况。可以尝试使用[terminateSelf](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#terminateself-1)或[ApplicationContext.killAllProcesses](../harmonyos-references/js-apis-inner-application-applicationcontext.md#applicationcontextkillallprocesses)代替。
