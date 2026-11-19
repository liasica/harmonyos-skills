---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-z-order
title: Z序控制
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 基础属性 > Z序控制
category: harmonyos-references
scraped_at: 2026-11-19T09:50:50+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:213270b5bbd45e16a754da7e99c8f840709f6efe9492f01f393594d9e44f5379
---

组件的Z序，设置同一容器中兄弟组件的堆叠顺序。

**说明** 

从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## zIndex

zIndex(value: number): T

设置组件的堆叠顺序。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 同一容器中兄弟组件显示层级关系。zIndex值越大，显示层级越高，即zIndex值大的组件会覆盖在zIndex值小的组件上方；不同容器内的组件无法根据zIndex值改变跨容器显示层级。当不涉及新增或减少兄弟节点，动态改变zIndex时会在zIndex改变前层级顺序的基础上进行稳定排序；涉及新增或减少兄弟节点时，zIndex值越大，显示层级越高，zIndex值相等时将按声明顺序显示，即后声明的组件会覆盖在先声明的组件上方。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件，用于链式调用。 |

## 示例

### 示例1（设置组件堆叠顺序）

该示例通过zIndex设置组件堆叠顺序。

```ts
// xxx.ets
@Entry
@Component
struct ZIndexExample {
  build() {
    Column() {
      Stack() {
        // Stack会重叠组件，默认后定义的在最上面，具有较高zIndex值的元素在zIndex较小的元素前面
        // Text1设置zIndex值为2
        Text('1, zIndex(2)')
          .size({ width: '40%', height: '30%' }).backgroundColor(0xbbb2cb)
          .zIndex(2)
        // Text2设置zIndex值为1
        Text('2, zIndex(1)')
          .size({ width: '70%', height: '50%' }).backgroundColor(0xd2cab3).align(Alignment.TopStart)
          .zIndex(1)
        // Text3设置zIndex值为0
        Text('3, zIndex(0)')
          .size({ width: '90%', height: '80%' }).backgroundColor(0xc1cbac).align(Alignment.TopStart)
          .zIndex(0)
      }.width('100%').height(200)
    }.width('100%').height(200)
  }
}
```

Stack容器内子组件不设置zIndex时，默认按照声明顺序显示，后声明的组件会覆盖在先声明的组件上方。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/lzerXzFaRJ2JWoQEmG7wuA/zh-cn_image_0000002820406989.png?HW-CC-KV=V1&HW-CC-Date=20261119T015050Z&HW-CC-Expire=31536000000&HW-CC-Sign=A787D8E6FFB6D044D455642D00E853B94D6CAB42EC809CF03C74FB3779EF8B15)

Stack容器子组件设置zIndex后的效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/m0kbQPycSWmuqGhz2BkJPQ/zh-cn_image_0000002791727010.png?HW-CC-KV=V1&HW-CC-Date=20261119T015050Z&HW-CC-Expire=31536000000&HW-CC-Sign=ADB87B5DE6D24E65BF550F795A3D9802EF106BFD9873F72AA76080CC3DDFE1D5)

### 示例2（动态修改zIndex属性）

该示例使用Button组件动态修改zIndex属性。

```ts
// xxx.ets
@Entry
@Component
struct ZIndexExample {
  @State zIndex_: number = 0;

  build() {
    Column() {
      // 点击Button改变zIndex后，在点击Button前的层级顺序上根据zIndex进行稳定排序。
      Button('change Text2 zIndex')
        .onClick(() => {
          this.zIndex_ = (this.zIndex_ + 1) % 3;
        })
      Stack() {
        // Text1设置zIndex值为1
        Text('1, zIndex(1)')
          .size({ width: '70%', height: '50%' }).backgroundColor(0xd2cab3).align(Alignment.TopStart)
          .zIndex(1)
        // Text2设置zIndex默认值为0
        Text('2, default zIndex(0), now zIndex:' + this.zIndex_)
          .size({ width: '90%', height: '80%' }).backgroundColor(0xc1cbac).align(Alignment.TopStart)
          .zIndex(this.zIndex_)
      }.width('100%').height(200)
    }.width('100%').height(200)
  }
}
```

不点击Button修改zIndex值的效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/jLhXjXxUS9qNYJ36p_tG8g/zh-cn_image_0000002791567038.png?HW-CC-KV=V1&HW-CC-Date=20261119T015050Z&HW-CC-Expire=31536000000&HW-CC-Sign=CC0DB4EE413A6CE1DFCC008B6EEBB8F3B7CAA299D46B7B1B94FF945A43D685E0)

点击Button动态修改zIndex，使Text1和Text2的zIndex相等，因为在点击Button前的层级顺序上根据zIndex进行稳定排序，层级顺序不发生改变。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/WnXLJ3qHQAahH4re9FchOw/zh-cn_image_0000002820526991.png?HW-CC-KV=V1&HW-CC-Date=20261119T015050Z&HW-CC-Expire=31536000000&HW-CC-Sign=66DDAB2506B29C840957AE8D1A6990AB1E362C7E0EB7CB94E35B7413DD287F1A)

点击Button动态修改zIndex，使Text2的zIndex大于Text1，层级顺序发生改变。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/5wDekbRRTFqUTp5oeWo7xg/zh-cn_image_0000002820406991.png?HW-CC-KV=V1&HW-CC-Date=20261119T015050Z&HW-CC-Expire=31536000000&HW-CC-Sign=6D77550B46B54EC6B570E778E430E4EF5D0BF4F2041A7AA6A503109EDEE003D2)

### 示例3（设置不同容器内组件的zIndex属性）

该示例在不同容器内设置zIndex属性。其中，Text1、Text2在同一个Stack容器内，Text3在另一个Stack容器内。虽然Text3的zIndex值最小，但Text1、Text2仍无法根据zIndex值显示在Text3的上方。

```ts
// xxx.ets
@Entry
@Component
struct ZIndexExample {
  build() {
    Stack() {
      Stack() {
        // Text1设置zIndex值为2
        Text('1, zIndex(2)')
          .size({ width: '40%', height: '30%' }).backgroundColor(0xbbb2cb)
          .zIndex(2)
        // Text2设置zIndex值为1
        Text('2, zIndex(1)')
          .size({ width: '70%', height: '50%' }).backgroundColor(0xd2cab3).align(Alignment.TopStart)
          .zIndex(1)
      }.width('100%').height(200)

      Stack() {
        // zIndex在不同容器的组件中无法生效，Text3会显示在最上方
        // Text3设置zIndex值为0
        Text('3, zIndex(0)')
          .size({ width: '90%', height: '80%' }).backgroundColor(0xc1cbac).align(Alignment.TopStart)
          .zIndex(0)
      }.width('100%').height(200)
    }.width('100%').height(200)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/1s6qlxMVRumi7nEdWJ4Acw/zh-cn_image_0000002791727012.png?HW-CC-KV=V1&HW-CC-Date=20261119T015050Z&HW-CC-Expire=31536000000&HW-CC-Sign=6B625B983DFB469FDE8208FA58F4B240CAEDCFFC274C09089C1737DDAC2604E3)
