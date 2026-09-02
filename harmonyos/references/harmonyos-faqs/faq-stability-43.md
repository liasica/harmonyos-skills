---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-43
title: 跳转到新页面时，应用闪退
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 跳转到新页面时，应用闪退
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:50+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:c058315b29efc5389b01dd6fb10e3cb99fad07ea450f5242584b89c4318db00f
---

## 问题现象

跳转到新页面时，应用出现闪退现象。

## 背景知识

1. [JsCrash异常](../best-practices/bpta-quality-overview.md#section19523112309)根据不同的异常场景，在Reason字段进行了分类，分为Error、TypeError、SyntaxError、ReferenceError、RangeError等错误类型。
2. TypeError（类型错误）：运行时最常见的异常，表示变量或参数不是预期类型。
3. [getParams](../harmonyos-references/arkts-apis-uicontext-router.md#getparams)：获取发起跳转的页面往当前页传入的参数。

## 问题定位

1. 查看faultlogger下的故障日志，故障原因是TypeError类型错误，异常信息是Cannot load property of null or undefined，无法加载空值或未定义的属性。

   ```txt
   Reason:TypeError
   Error name:TypeError
   Error message:Cannot load property of null or undefined
   Stacktrace:
       at anonymous entry (entry/src/main/ets/pages/TestLoadThirdPage.ets:17:25)
       at initialRender entry (entry/src/main/ets/pages/TestLoadThirdPage.ets:27:18)
       at pushUrl (.../foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/jsUIContext_ohos.js:1167:1)
       at anonymous entry (entry/src/main/ets/pages/TestLoadPage.ets:11:43)
   ```
2. 从故障堆栈中可以看到应用在执行pushUrl跳转到新的页面时出现了空值或未定义的属性。
3. 排查应用是否使用router.getParams()获取上一个页面传递过来的参数，但实际页面跳转时传递的参数为空。

   ```typescript
   class ParamInfo {
     name: string = '';

     constructor(name: string) {
       this.name = name;
     }
   }

   @Entry
   @Component
   struct TestLoadSecondPage {
     @State message: ParamInfo = this.getUIContext().getRouter().getParams() as ParamInfo;

     build() {
       RelativeContainer() {
         Text(this.message.name)
           .id('LoadUndefinedSecondPageHelloWorld')
           .fontSize($r('app.float.page_text_font_size'))
           .fontWeight(FontWeight.Bold)
           .alignRules({
             center: { anchor: '__container__', align: VerticalAlign.Center },
             middle: { anchor: '__container__', align: HorizontalAlign.Center }
           });
       }
       .height('100%')
       .width('100%');
     };
   }
   ```

## 分析结论

传递的参数为空导致应用闪退。

## 修改建议

在使用[getParams](../harmonyos-references/arkts-apis-uicontext-router.md#getparams)获取传递的参数时需要校验是否为空。

```ts
class ParamInfo {
  name: string = '';

  constructor(name: string) {
    this.name = name;
  }
}

@Entry
@Component
struct TestLoadThirdPage {
  @State message: ParamInfo = this.getUIContext().getRouter().getParams() as ParamInfo ?
    (this.getUIContext().getRouter().getParams() as ParamInfo) : new ParamInfo('Two2');

  build() {
    RelativeContainer() {
      Text(this.message.name)
        .id('LoadUndefinedThirdPageHelloWorld')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        });
    }
    .height('100%')
    .width('100%');
  }
}
```
