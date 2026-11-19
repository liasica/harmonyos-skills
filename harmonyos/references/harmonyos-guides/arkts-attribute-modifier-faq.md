---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-attribute-modifier-faq
title: 动态属性设置常见问题
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发调试调优 > UI开发常见问题 > 动态属性设置常见问题
category: harmonyos-guides
scraped_at: 2026-11-19T09:47:49+08:00
doc_updated_at: 2026-11-03
content_hash: sha256:e6bd10b3ee11018c55891805afe93fd5769ad9e504681d795c7f5729469ad08a
---

本文档介绍动态属性设置的常见问题并提供参考。

## 使用AttributeModifier设置组件动态属性，出现JS Crash

**问题现象**

使用AttributeModifier对组件进行[动态属性设置](../harmonyos-references/ts-universal-attributes-attribute-modifier.md)，设置某些属性后出现[JS Crash](jscrash-guidelines.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/qF-mYeRGQjSqhtwmR0iGIw/zh-cn_image_0000002820525389.png?HW-CC-KV=V1&HW-CC-Date=20261119T014658Z&HW-CC-Expire=31536000000&HW-CC-Sign=B50458373A9BDF808D51EB01A1E027928EDD5B3A657E77F2494666B089BACAAD)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/SVLviteTRIqM8e-GqBARMA/zh-cn_image_0000002820405389.gif?HW-CC-KV=V1&HW-CC-Date=20261119T014658Z&HW-CC-Expire=31536000000&HW-CC-Sign=4D4FDADAE627C290FA36282FA5A67345C6B6FD6FB0CFE46F7F374AA9C2E3D2C8)
