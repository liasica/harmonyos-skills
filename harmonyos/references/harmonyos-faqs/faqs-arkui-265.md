---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-265
title: 如何实现点击输入框时会拉起软键盘，点击Button时软键盘关闭
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现点击输入框时会拉起软键盘，点击Button时软键盘关闭
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:59+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:3be894a95bb65f72c7cf159e002fd4a03df113a5b85b4c0ff7461aebdf16c653
---

可以通过全局的焦点控制对象FocusController的[clearFocus()](../harmonyos-references/arkts-apis-uicontext-focuscontroller.md#clearfocus12)方法收起软键盘，示例代码如下：

```screen
@Entry
@Component
struct ClickBlankHideKeyboard {
  build() {
    Column({ space: 12 }) {
      TextInput({ placeholder: 'Please enter your account' })
        .height(40)
      TextInput({ placeholder: 'Please input a password' })
        .height(40)
      Button('log on').width('100%')
        .onClick(() => {
          this.getUIContext().getFocusController().clearFocus();
        })
    }
  }
}
```

参考链接：

[代码控制收起软键盘](../best-practices/bpta-keyboard-layout-adapt.md#section19809195110316)
