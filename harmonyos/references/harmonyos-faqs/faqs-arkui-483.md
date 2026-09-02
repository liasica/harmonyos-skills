---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-483
title: 设置了动态的visibility属性，切换组件的显示隐藏，使用requestFocus让组件获取焦点报错150003：the component is not on tree or does not exist.
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 设置了动态的visibility属性，切换组件的显示隐藏，使用requestFocus让组件获取焦点报错150003：the component is not on tree or does not exist.
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:00+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6d37759ab4ed899c591c4e313308c6d78cf983036a93e01f9dbc603f2b5f8510
---

根据焦点错误码[150003 节点不存在](../harmonyos-references/errorcode-focus.md#section150003-节点不存在)表明传入的id指向不存在、未挂树或者不可见节点。requestFocus前需要确保节点已经可见。

如以下代码的实现，在切换可见性时，并不能保证获取焦点时组件已经可见：

```typescript
@Entry
struct Index {
  @State isEdit: boolean = true;

  build() {
    Column() {
      TextInput().id('input')
        .visibility(this.isEdit ? Visibility.Visible : Visibility.None)
      Button('change visibility')
        .onClick(() => {
          this.isEdit = !this.isEdit;
          if (this.isEdit) {
            try {
              this.getUIContext().getFocusController().requestFocus('input');
            } catch (e) {
              console.error("requestFocus error: " + e);
            }
          }
        })
    }
  }
}
```

推荐在[onVisibleAreaChange](../harmonyos-references/ts-universal-component-visible-area-change-event.md#onvisibleareachange)回调中进行焦点获取，参考示例代码如下：

```typescript
@Entry
@Component
struct GetFocusByOnVisibleAreaChange {
  @State isEdit: boolean = true;

  build() {
    Column() {
      TextInput().id('input')
        .visibility(this.isEdit ? Visibility.Visible : Visibility.None)
        .onVisibleAreaChange([1.0], () => {
          if (this.isEdit) {
            try {
              this.getUIContext().getFocusController().requestFocus('input');
            } catch (e) {
              console.error('requestFocus error:' + e);
            }
          }
        })
      Button('change visibility')
        .onClick(() => {
          this.isEdit = !this.isEdit;
        })
    }
  }
}
```
