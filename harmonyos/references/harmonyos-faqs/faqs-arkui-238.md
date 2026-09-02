---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-238
title: 在屏幕底部的组件的响应区域是否存在遮挡
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 在屏幕底部的组件的响应区域是否存在遮挡
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1de8415f41b4ff4bab13ceab9462520894912c333e1fa3a290fe5d7356c6c31b
---

**问题现象**

创建窗口并加载自定义键盘后，发现底部按钮下半部分无法响应点击事件。

**解决措施**

底部遮挡区域的高度为20像素，可以通过on('avoidAreaChange')事件获取。开发者可以定义一个点击区域来测试点击事件是否能够触发。以下为代码示例：

```ts
@Entry
@Component
struct Index {
  build() {
    Column() {
      Column() {
      }
      .width('100%')
      .height(5) // 5px click range
      .backgroundColor(Color.Red)
      .onClick(() => {
        console.log("Trigger click event")
      })
    }
    .height('100%')
    .width('100%')
    .justifyContent(FlexAlign.End)
  }
}
```

**参考链接**

[on('avoidAreaChange')](../harmonyos-references/arkts-apis-window-window.md#onavoidareachange9)
