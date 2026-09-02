---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1243
title: 用户未登录时显示退出登录按钮
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 用户未登录时显示退出登录按钮
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c321ebe288daf9bde696b276faccaccc2ecae27996f8e7926c0903f2bcf94925
---

## 问题现象

在用户未登录某个应用时，应用却显示了“退出登录”的按钮。

## 背景知识

if/else条件渲染：ArkTS提供了渲染控制能力。条件渲染可根据应用状态，使用if、else和else if渲染相应的UI内容。

应用可以根据登录状态来控制“退出登录”按钮是否显示。

## 问题定位

排查应用代码，确认“退出登录”组件的条件渲染逻辑是否正确。

如果未使用条件渲染直接显示，则会出现问题现象中的问题：

```screen
Column() {
  Button("退出登录")
}
```

## 分析结论

* 若“退出登录”组件没有条件渲染控制或渲染控制里无登录状态相关的判断，则说明应用未通过登录状态控制“退出登录”组件的显示和隐藏。
* 若“退出登录”组件渲染控制里有登录状态相关的判断，则说明登录状态的判断有误。

## 修改建议

* 若“退出登录”组件没有条件渲染控制或渲染控制里无登录状态相关的判断，则需要应用根据登录状态对“退出登录”组件增加渲染控制。

  ```screen
  @Entry
  @Component
  struct VideoSavePage {
    @State isLogin: boolean = true; // 登录状态

    build() {
      Column() {
        if (this.isLogin) {
          Button("退出登录");
        }
      };
    }
  }
  ```
* 若“退出登录”组件渲染控制中有对登录状态的判断，则需要排查登录状态判断逻辑。
