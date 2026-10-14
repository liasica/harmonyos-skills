---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-attribute-modifier-faq
title: 动态属性设置常见问题
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发调试调优 > UI开发常见问题 > 动态属性设置常见问题
category: harmonyos-guides
scraped_at: 2026-10-15T07:04:16+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0f18ccd324f7a357ff78ade3ac542fc836061eb163e133f5d3a213d05702e2e0
---

本文档介绍动态属性设置的常见问题并提供参考。

## 使用AttributeModifier设置组件动态属性，出现JS Crash

**问题现象**

使用AttributeModifier对组件进行[动态属性设置](../harmonyos-references/ts-universal-attributes-attribute-modifier.md)，设置某些属性后出现[JS Crash](jscrash-guidelines.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/aOf7YqGjRKGVLsXkiAeUDg/zh-cn_image_0000002791738671.png)

**解决措施**

根据提示跳转至报错日志，查看具体的报错原因，进行相应的修改，具体的跳转方法请参考下方示例代码。

**示例代码**

该示例通过Button绑定AttributeModifier，展示了AttributeModifier在设置不支持的属性时会抛出异常的场景，运行示例代码后会出现JS Crash报错，参考下方的动图，跳转至具体的报错场景。在本示例中，删除reuseId相关代码即可正常运行。

```ts
// xxx.ets
// 设置Button组件属性的自定义AttributeModifier
class MyButtonModifier implements AttributeModifier<ButtonAttribute> {

  applyNormalAttribute(instance: ButtonAttribute): void {
    instance.reuseId('String') // 删除本行可以让程序正常运行
    instance.backgroundColor(Color.Red)
  }
}

@Entry
@Component
struct attributeDemo {
  @State modifier: MyButtonModifier = new MyButtonModifier();

  build() {
    Row() {
      Column() {
        Button('Button')
          .attributeModifier(this.modifier)
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/_y3chHLhS0-XECWiAJcBcg/zh-cn_image_0000002762340090.gif)
