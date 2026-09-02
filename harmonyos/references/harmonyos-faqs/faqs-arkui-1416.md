---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1416
title: router使用pushUrl回调崩溃
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > router使用pushUrl回调崩溃
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:10+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:de1eb8d4c04c5949c4f49d2ac015cf7d9f558bbb711586b7d47b2e0e13ea5f74
---

## 问题现象

在router.pushUrl的回调中执行router.clear会崩溃。

```ts
router.pushUrl({
  url: "login/UserNameLoginPage"
}, () => {
  router.clear()
})
```

报错Log信息如下：

```log
Error name:Error
Error message:Internal error. UI execution context not found.
Error code:100001
```

## 背景知识

全局的UI接口是和具体UI实例的执行上下文相关的，在当前接口调用时，通过追溯调用链跟踪到UI的上下文，来确定具体的UI实例。若在非UI页面中或者一些异步回调中调用这类接口，可能无法跟踪到当前UI的上下文，导致接口执行失败。和上下文相关的全局接口请查阅[@ohos.arkui.UIContext](../harmonyos-references/arkts-apis-uicontext.md)模块。

## 问题定位

报错日志提示未找到UI执行的上下文信息"UI execution context not found"，即执行router相关接口时未追踪到当前UI上下文。

## 分析结论

在异步回调时使用router.clear，未追踪到当前UI的上下文，接口执行失败，程序崩溃。

## 修改建议

* 方法一：使用Navigation组件替代router作为应用路由框架，可参考[Router切换Navigation](../harmonyos-guides/arkts-router-to-navigation.md)。
* 方法二：通过使用UIContext中的[getRouter](../harmonyos-references/arkts-apis-uicontext-uicontext.md#getrouter)方法获取当前UI上下文关联的router对象，再通过该对象调用对应方法。可参考官网文档中关于[pushUrl](../harmonyos-references/arkts-apis-uicontext-router.md#pushurl)等API的用法说明和示例。

  如果在非UI页面类中调用router时，由于无法直接获取UIContext实例，需在页面初始化后将UIContext存入AppStorage，后续通过AppStorage获取该实例并调用其getRouter()方法获取router对象。如下示例：

  ```ts
  @Entry
  @Component
  struct RouterDemo {
    aboutToAppear(): void {
      // 获取UIContext，保存在AppStorage中
      // 也可以在EntryAbility.ets的onWindowStageCreate方法中保存UIContext
      AppStorage.setOrCreate('UIContext', this.getUIContext());
    }

    build() {
      Column() {
        Button('跳转页面')
          .onClick(() => {
            Auth.gotoLoginPage();
          });
      }.height('100%').width('100%');
    }
  }

  class Auth {
    // 跳转到登录页
    static gotoLoginPage() {
      // 通过AppStorage获取UIContext
      const uiContext = AppStorage.get<UIContext>('UIContext');
      if (uiContext) {
        uiContext.getRouter().pushUrl({
          url: 'pages/Index' // 需自行创建一个Index页面
        });
      }
    }
  }
  ```
