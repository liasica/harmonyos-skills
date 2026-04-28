---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-37
title: onUnhandledException与onException回调分别什么时候触发
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > onUnhandledException与onException回调分别什么时候触发
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:45+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:470ef0f68b8e30c1633c41278b6a0170a7a1b22673694635cc352187a12da5f6
---

* [onUnhandledException](../harmonyos-references/js-apis-inner-application-errorobserver.md#errorobserveronunhandledexception)：当异常未被任何try/catch或onException处理时触发，如用于记录崩溃日志或上报未知错误。
* [onException](../harmonyos-references/js-apis-inner-application-errorobserver.md#errorobserveronexception10)：在任务或异步操作中主动抛出异常时，系统会触发 onException 回调，例如网络请求失败、数据解析错误等。

  ```
  1. import { errorManager } from '@kit.AbilityKit';
  2. import { BusinessError } from '@kit.BasicServicesKit';

  4. let observer: errorManager.ErrorObserver = {
  5. onUnhandledException(errorMsg) {
  6. console.error('onUnhandledException, errorMsg: ', errorMsg);
  7. },
  8. onException(errorObj) {
  9. console.log('onException, name: ', errorObj.name);
  10. console.log('onException, message: ', errorObj.message);
  11. if (typeof (errorObj.stack) === 'string') {
  12. console.log('onException, stack: ', errorObj.stack);
  13. }
  14. }
  15. };

  17. try {
  18. errorManager.on('error', observer);
  19. } catch (error) {
  20. console.error(`registerErrorObserver failed, error.code: ${(error as BusinessError).code}, error.message: ${(error as BusinessError).message}`);
  21. }
  ```

  [Exceptionhandle.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/AbilityKit/entry/src/main/ets/pages/Exceptionhandle.ets#L21-L41)

区别在于，onUnhandledException仅返回异常信息，而onException返回完整的异常对象。
