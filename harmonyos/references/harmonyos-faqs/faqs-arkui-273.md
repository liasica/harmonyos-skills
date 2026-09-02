---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-273
title: 如何在Navigation页面中实现侧滑事件拦截
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何在Navigation页面中实现侧滑事件拦截
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:28+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a46713801ba3d04ba6663635d38759ef0e13a933ba4f075abbec94685b3e44c2
---

1. 因为功能以har形式集成在主工程中，没有@Entry修饰的组件，无法作为入口组件，也不能使用onBackPress生命周期函数。
2. 在使用onBackPressed时，它是NavDestination的事件，需要与NavDestination组件配合使用。组件本身用于显示导航内容区，作为子页面的根容器。因此，若需拦截子页面的返回事件，可以使用onBackPressed回调。
3. 在使用onBackPress时， 生命周期函数onBackPress只能在 @Entry 组件中使用，因此可以使用该函数拦截入口组件的返回事件。
4. 开发者可通过NavDestination组件onBackPressed回调拦截返回事件。

参考代码如下：

```ts
import { ShowDialogSuccessResponse } from '@kit.ArkUI';

@Entry
@Component
struct SideslipIntercept {
  controller: TextAreaController = new TextAreaController();
  @State text: string = '';
  @Provide pageStack: NavPathStack = new NavPathStack();

  build() {
    // Main page uses NavDestination as carrier to display Navigation content area
    Navigation(this.pageStack) {
    }
    .onAppear(() => {
      this.pageStack.pushPathByName('MainPage', null, false);
    })
    // Create NavDestination component, use its onBackPressed callback to intercept back event
    .navDestination(this.textArea)
  }

  @Builder
  textArea(name: string) {
    NavDestination() {
      Column() {
        TextArea({
          text: this.text,
          placeholder: 'input your word...',
          controller: this.controller
        })
          .onChange((value: string) => {
            this.text = value;
          })
      }
      .justifyContent(FlexAlign.Start)
      .width('100%')
      .height('100%')
    }
    .onBackPressed(() => {
      // Interception logic can be added here, then return true to proceed
      this.getUIContext().getPromptAction().showDialog({
        message: 'Save?',
        alignment: DialogAlignment.Center,
        buttons: [
          {
            text: "Don't Save",
            color: '#0000FF'
          },
          {
            text: 'Save',
            color: '#0000FF'
          }
        ]
      }).then((data: ShowDialogSuccessResponse) => {
        // When selecting button index in buttons array, starting from 0, second index is 1
        // Click Don't Save button
        if (data.index === 0) {
          console.info('Not saving')
        }
        // Click Save button
        if (data.index === 1) {
          console.info('Saving')
        }
      })
      return true;
    })
  }
}
```

**参考链接**

[侧滑返回事件拦截案例](https://gitcode.com/HarmonyOS-Cases/cases/tree/master/CommonAppDevelopment/feature/sideslipintercept)
