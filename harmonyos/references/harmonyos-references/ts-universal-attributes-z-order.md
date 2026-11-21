---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-z-order
title: Z序控制
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 基础属性 > Z序控制
category: harmonyos-references
scraped_at: 2026-11-21T09:14:01+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5befbf97fc32b618c03938d58f95c31846157e0453a020b1928b45b6ad98db00
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/l09d3K_gT6amiqCgieDudQ/zh-cn_image_0000002821758599.png?HW-CC-KV=V1&HW-CC-Date=20261121T011401Z&HW-CC-Expire=31536000000&HW-CC-Sign=C9B570DC2592EEE369CB80931B206CE3913BC42CDC93ED3C34EEDAC5C520E43A)

Stack容器子组件设置zIndex后的效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/SrCnR79PQeyWz3IalK53dA/zh-cn_image_0000002793038662.png?HW-CC-KV=V1&HW-CC-Date=20261121T011401Z&HW-CC-Expire=31536000000&HW-CC-Sign=4C618156FCB3A96634979AC24ED341F157943717FF05B9B0C32605A0E5E0395C)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/COax79SGR2aMqsuUfI2PUw/zh-cn_image_0000002792878692.png?HW-CC-KV=V1&HW-CC-Date=20261121T011401Z&HW-CC-Expire=31536000000&HW-CC-Sign=E24F86E8501B1E25D31EB5464D9640A8999A2A8CFB311F6693E99BF7B2B562B5)

点击Button动态修改zIndex，使Text1和Text2的zIndex相等，因为在点击Button前的层级顺序上根据zIndex进行稳定排序，层级顺序不发生改变。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/RgFD-gckT9OiU3kh2v_q9Q/zh-cn_image_0000002821838599.png?HW-CC-KV=V1&HW-CC-Date=20261121T011401Z&HW-CC-Expire=31536000000&HW-CC-Sign=FDCF2097545EFD6EB42509F836525A3E5BC43F6D9ABD20FBCEA93C6F45F5D895)

点击Button动态修改zIndex，使Text2的zIndex大于Text1，层级顺序发生改变。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/D8lLJbk9TW-t4Bm5xSdOZw/zh-cn_image_0000002821758601.png?HW-CC-KV=V1&HW-CC-Date=20261121T011401Z&HW-CC-Expire=31536000000&HW-CC-Sign=6F1965437065AD2BE39953EB39A01F72491F2FE4B88A7170D88AED613B90825C)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/f3XhdpI5Rw2582JIi7glvA/zh-cn_image_0000002793038664.png?HW-CC-KV=V1&HW-CC-Date=20261121T011401Z&HW-CC-Expire=31536000000&HW-CC-Sign=8CE12AFA8746DF0EA7F5E506204C093666C0858F095A542A058F26A762530388)
