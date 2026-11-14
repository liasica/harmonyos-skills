---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-attribute-modifier-faq
title: 动态属性设置常见问题
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发调试调优 > UI开发常见问题 > 动态属性设置常见问题
category: harmonyos-guides
scraped_at: 2026-11-14T08:47:12+08:00
doc_updated_at: 2026-11-03
content_hash: sha256:78cfe58af7d9b6d6f7c31565e702a21e6b1ba9d98fd50c87d36bee456fd94115
---

本文档介绍动态属性设置的常见问题并提供参考。

## 使用AttributeModifier设置组件动态属性，出现JS Crash

**问题现象**

使用AttributeModifier对组件进行[动态属性设置](../harmonyos-references/ts-universal-attributes-attribute-modifier.md)，设置某些属性后出现[JS Crash](jscrash-guidelines.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/SFbRRm0iSyG17-hUi47naQ/zh-cn_image_0000002817506539.png?HW-CC-KV=V1&HW-CC-Date=20261114T004711Z&HW-CC-Expire=31536000000&HW-CC-Sign=1ECC8A92C0C02605C543D8B0D6E0E5E54791EFDA08445B89BBDF203F8D73BC0B)

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
struct AttributeDemo {
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/lfhEMQeXRICZ8yNsi4E-wg/zh-cn_image_0000002788307110.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004711Z&HW-CC-Expire=31536000000&HW-CC-Sign=F759526985A49AC2A96CC481F97C7DD7171CAECDD9A9572F7C2D53B94914F38B)
