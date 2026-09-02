---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-25
title: 侧滑退出应用响应慢
breadcrumb: FAQ > 应用质量 > 技术质量 > 性能 > 侧滑退出应用响应慢
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:023a1fcde865d65da4115c15317f22c2d1e036098bd67d60d190dded88fe4e8d
---

## 问题现象

侧滑屏幕退出应用时，需要等一段时间应用才退出，响应慢。

## 背景知识

* [killAllProcesses](../harmonyos-references/js-apis-inner-application-applicationcontext.md#applicationcontextkillallprocesses)：可实现关闭应用所有的进程，该接口用于应用异常场景中强制退出应用。如需正常退出应用，可以使用[terminateSelf()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#terminateself-1)接口。
* [onBackPress](../harmonyos-references/ts-custom-component-lifecycle.md#onbackpress)：点击返回按钮或侧滑时触发，返回true表示页面自己处理返回逻辑，不进行页面路由；返回false表示使用默认的路由返回逻辑，不设置返回值按照false处理。在日志中如果搜索到router user onBackPress return true则表示应用有重写onBackPress方法。

## 问题定位

1. 侧滑退出应用时如果采用默认的退出逻辑，响应时间会较短，出现响应慢现象则推测是应用实现了延时退出，可在日志中搜索onBackPress|KillApplicationSelf确认。

   如下图应用有重写onBackPress方法，同时在两次侧滑退出应用时有调用KillApplicationSelf方法关闭应用进程，第二次侧滑操作与关闭应用进程时间间隔1.2s，推测应用在侧滑响应处理时延迟退出应用进程。

   ```txt
   07-03 15:04:24.825   56626-56626  C03925/com.exa...ion/AceRouter com.examp...lication  I     [(100000:100000:scope)] router user onBackPress return true
   07-03 15:04:25.503   56626-56626  C03925/com.exa...ion/AceRouter com.examp...lication  I     [(100000:100000:scope)] router user onBackPress return true
   07-03 15:04:26.710   1458-2344    C01311/foundation/AppMS        foundation            W     [ams_mgr_stub.cpp:431]KillApplicationSelf,callingPid=56626
   ```
2. 可在代码中搜索killAllProcesses找到退出应用进程的相关代码，如下代码中可看到两次侧滑后有延迟1.2s关闭应用进程，会导致侧滑退出响应慢的问题。

   ```typescript
   onBackPress(): boolean | void {
     if (this.first) {
       this.first = false;
       // 延迟一段时间将this.first设置成true
     } else {
       setTimeout(() => {
         this.getUIContext().getHostContext()?.getApplicationContext().killAllProcesses().catch(() => {
            // TODO:Implement error handling.
         });
       }, 1200);
     }
     return true;
   }
   ```

## 分析结论

应用重写onBackPress方法，在侧滑时延迟退出应用进程，导致侧滑退出应用响应慢的问题。

## 修改建议

* 去掉延迟退出的代码逻辑。
* 增加退出提示，如下示例代码。

  ```typescript
  import { PromptAction } from '@ohos.arkui.UIContext';
  import { common } from '@kit.AbilityKit';
  import { BusinessError } from '@ohos.base';

  @Entry
  @Component
  struct ExitPromptDemoPage {
    message: string = 'Hello World';

    promptAction: PromptAction = this.getUIContext().getPromptAction();

    context = this.getUIContext().getHostContext() as common.UIAbilityContext;

    private first: boolean = true;

    firstBackPress(): void {
      this.first = false;
      this.showToast('再次侧滑退出', 1500);
      setTimeout(() => {
        this.first = true;
      }, 1500);
    }

    showToast(message: string, duration: number) {
      try {
        this.promptAction.showToast({
          message: message,
          duration: duration
        });
      } catch (error) {
        console.error('error: ', error);
      }
    }

    terminate() {
      this.context?.terminateSelf((err: BusinessError) => {
        if (err.code) {
          console.error(`terminateSelf failed, code is ${err.code}, message is ${err.message}`);
        }
        console.info('terminateSelf succeed');
      });
    }

    onBackPress(): boolean | void {
      if (this.first) {
        // 第一次侧滑处理
        this.firstBackPress();
      } else {
        // 第二次侧滑处理
        this.showToast('应用退出中', 3000);
        setTimeout(() => {
          this.terminate();
        }, 3000);
      }
      return true;
    }

    build() {
      RelativeContainer() {
        Text(this.message)
          .id('ExitPromptDemoPageHelloWorld')
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
      }
      .height('100%')
      .width('100%')
    }
  }
  ```
