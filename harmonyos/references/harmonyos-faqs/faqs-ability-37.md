---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-37
title: onUnhandledException与onException回调分别什么时候触发
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > onUnhandledException与onException回调分别什么时候触发
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:caab81576850275eeafb00123825ce2a340de66bd5543cfa60713f15ef380e50
---

* [onUnhandledException](../harmonyos-references/js-apis-inner-application-errorobserver.md#errorobserveronunhandledexception)：当异常未被任何try/catch或onException处理时触发，如用于记录崩溃日志或上报未知错误。
* [onException](../harmonyos-references/js-apis-inner-application-errorobserver.md#errorobserveronexception10)：在任务或异步操作中主动抛出异常时，系统会触发 onException 回调，例如网络请求失败、数据解析错误等。

  ```typescript
  import { errorManager } from '@kit.AbilityKit';
  import { BusinessError } from '@kit.BasicServicesKit';

  let observer: errorManager.ErrorObserver = {
    onUnhandledException(errorMsg) {
      console.error('onUnhandledException, errorMsg: ', errorMsg);
    },
    onException(errorObj) {
      console.log('onException, name: ', errorObj.name);
      console.log('onException, message: ', errorObj.message);
      if (typeof (errorObj.stack) === 'string') {
        console.log('onException, stack: ', errorObj.stack);
      }
    }
  };

  try {
    errorManager.on('error', observer);
  } catch (error) {
    console.error(`registerErrorObserver failed, error.code: ${(error as BusinessError).code}, error.message: ${(error as BusinessError).message}`);
  }
  ```

区别在于，onUnhandledException仅返回异常信息，而onException返回完整的异常对象。
