---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-124
title: TextInput按压态背景色如何修改
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > TextInput按压态背景色如何修改
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:58+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:2f927bba205976e8a4a812746a78b58bc1208894a53ffbf54a2e8c2a85d01f67
---

可以使用动态属性进行设置。自定义class实现AttributeModifier接口，并给组件设置.attributeModifier()进行绑定即可。参考代码如下：

```typescript
@Entry
@Component
struct Index {
  @State modifier: MyTextInputModifier = new MyTextInputModifier();

  build() {
    Row() {
      Column() {
        TextInput({ placeholder: 'test' })
          .width('80%')
          .height(100)
          .attributeModifier(this.modifier)
      }
      .width('100%')
    }
    .height('100%')
  }
}

class MyTextInputModifier implements AttributeModifier<TextInputAttribute> {
  applyNormalAttribute(instance: TextInputAttribute): void {
    instance.backgroundColor(Color.Grey);
  }

  applyPressedAttribute(instance: TextInputAttribute): void {
    instance.backgroundColor(Color.Blue);
  }
}
```

**参考链接**

[动态属性设置](../harmonyos-references/ts-universal-attributes-attribute-modifier.md)
