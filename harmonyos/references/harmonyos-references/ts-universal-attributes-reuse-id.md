---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-reuse-id
title: 复用标识
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 其他 > 复用标识
category: harmonyos-references
scraped_at: 2026-09-02T15:00:57+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8429f717a2bc9e0110bf9d213e0eaf8f02b4ac8f82f29b0bb61b25d4c14287be
---

reuseId用于标记自定义组件的复用组，当组件回收复用时，复用框架将根据组件的reuseId划分组件的复用组。通过为不同布局或类型的组件设置不同的reuseId，可避免组件被错误复用，实现更精准的复用匹配，提升复用效率，适用于同一自定义组件存在多种布局形态的场景。

**说明** 

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。

## reuseId

reuseId(id: string): T

复用标识，用于划分自定义组件的复用组。该接口仅可在Stage模型下使用。

**说明** 

* 根据组件的不同布局形态或类型设置对应的reuseId，以提升复用匹配的精确度。最佳实践请参考组件复用-[使用reuseId标记布局发生变化的组件](../harmonyos-guides/arkts-component_reuse.md#使用reuseid标记布局发生变化的组件)。
* 该接口不支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 复用标识，用于划分自定义组件的复用组。建议为不同布局或类型的组件设置不同的reuseId，以避免组件被错误复用，提升复用效率。仅在@Reusable装饰的自定义组件上生效。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## 示例

该示例通过reuseId标识自定义组件的复用组。

```ts
// xxx.ets
@Entry
@Component
struct MyComponent {
  @State isShow: boolean = true;
  private type: string = 'type1';

  build() {
    Column() {
      Button('ChangeType')
        .onClick(() => {
          this.type = 'type2';
        })
      Button('Switch')
        .onClick(() => {
          this.isShow = !this.isShow;
        })
      if (this.isShow) {
        ReusableChildComponent({ type: this.type })
          .reuseId(this.type)
      }
    }
    .width('100%')
    .height('100%')
  }
}

@Reusable
@Component
struct ReusableChildComponent {
  @State type: string = '';

  aboutToAppear() {
    console.info(`ReusableChildComponent Appear ${this.type}`);
  }

  aboutToReuse(params: ESObject) {
    console.info(`ReusableChildComponent Reuse ${this.type}`);
    this.type = params.type;
  }

  build() {
    Row() {
      Text(this.type)
        .fontSize(20)
        .margin({ left: 10 })
    }.margin({ left: 10, right: 10 })
  }
}
```
