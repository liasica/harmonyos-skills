---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-z-order
title: Z序控制
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 基础属性 > Z序控制
category: harmonyos-references
scraped_at: 2026-04-29T13:51:14+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c225bacc6be38babc0cb4a80dfb60fbe29f3e63f255e44613f7b6ee79e25876b
---

组件的Z序，设置同一容器中兄弟组件的堆叠顺序。

说明

从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## zIndex

PhonePC/2in1TabletTVWearable

zIndex(value: number): T

设置组件的堆叠顺序。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 同一容器中兄弟组件显示层级关系。zIndex值越大，显示层级越高，即zIndex值大的组件会覆盖在zIndex值小的组件上方。当不涉及新增或减少兄弟节点，动态改变zIndex时会在zIndex改变前层级顺序的基础上进行稳定排序。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（设置组件堆叠顺序）

该示例通过zIndex设置组件堆叠顺序。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ZIndexExample {
5. build() {
6. Column() {
7. Stack() {
8. // Stack会重叠组件，默认后定义的在最上面，具有较高zIndex值的元素在zIndex较小的元素前面
9. // Text1设置zIndex值为2
10. Text('1, zIndex(2)')
11. .size({ width: '40%', height: '30%' }).backgroundColor(0xbbb2cb)
12. .zIndex(2)
13. // Text2设置zIndex值为1
14. Text('2, default zIndex(1)')
15. .size({ width: '70%', height: '50%' }).backgroundColor(0xd2cab3).align(Alignment.TopStart)
16. .zIndex(1)
17. // Text3设置zIndex值为0
18. Text('3, zIndex(0)')
19. .size({ width: '90%', height: '80%' }).backgroundColor(0xc1cbac).align(Alignment.TopStart)
20. .zIndex(0)
21. }.width('100%').height(200)
22. }.width('100%').height(200)
23. }
24. }
```

Stack容器内子组件不设置zIndex的效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/LcO9ybjISBqMcT6B1UwCxg/zh-cn_image_0000002589245815.png?HW-CC-KV=V1&HW-CC-Date=20260429T055112Z&HW-CC-Expire=86400&HW-CC-Sign=9F89E3B835B3028548426942C08BACEEAB251547F3F031F801647320795D1D40)

Stack容器子组件设置zIndex后的效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/5qPcQFl-T9qjJTfna0SWUQ/zh-cn_image_0000002558766006.png?HW-CC-KV=V1&HW-CC-Date=20260429T055112Z&HW-CC-Expire=86400&HW-CC-Sign=5D210D1BBBA8CF7032E34A577578C0646305A8E58897C3AAB5FC9B3A83B1DCC4)

### 示例2（动态修改zIndex属性）

该示例使用Button组件动态修改zIndex属性。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ZIndexExample {
5. @State zIndex_: number = 0

7. build() {
8. Column() {
9. // 点击Button改变zIndex后，在点击Button前的层级顺序上根据zIndex进行稳定排序。
10. Button("change Text2 zIndex")
11. .onClick(() => {
12. this.zIndex_ = (this.zIndex_ + 1) % 3;
13. })
14. Stack() {
15. // Text1设置zIndex值为1
16. Text('1, zIndex(1)')
17. .size({ width: '70%', height: '50%' }).backgroundColor(0xd2cab3).align(Alignment.TopStart)
18. .zIndex(1)
19. // Text2设置zIndex默认值为0
20. Text('2, default zIndex(0), now zIndex:' + this.zIndex_)
21. .size({ width: '90%', height: '80%' }).backgroundColor(0xc1cbac).align(Alignment.TopStart)
22. .zIndex(this.zIndex_)
23. }.width('100%').height(200)
24. }.width('100%').height(200)
25. }
26. }
```

不点击Button修改zIndex值的效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/Mi0rVT4NTIuYnU96itdgWg/zh-cn_image_0000002558606348.png?HW-CC-KV=V1&HW-CC-Date=20260429T055112Z&HW-CC-Expire=86400&HW-CC-Sign=EA4EFB7E1FA4E2E9E0A31ADCEBE7C802589726378283E6F69832552B5E02C52C)

点击Button动态修改zIndex，使Text1和Text2的zIndex相等，因为在点击Button前的层级顺序上根据zIndex进行稳定排序，层级顺序不发生改变。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/YFRoTOGVT6W1GFa_43-mSA/zh-cn_image_0000002589325875.png?HW-CC-KV=V1&HW-CC-Date=20260429T055112Z&HW-CC-Expire=86400&HW-CC-Sign=F6788EF457A79B1023FF183B45DF2483C0A7A87187FE6E2084153D211179EE24)

点击Button动态修改zIndex，使Text2的zIndex大于Text1，层级顺序发生改变。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/YRvcavFmSE6fcSxbw7tPig/zh-cn_image_0000002589245817.png?HW-CC-KV=V1&HW-CC-Date=20260429T055112Z&HW-CC-Expire=86400&HW-CC-Sign=F0A8EF87620F98774251663F8F47212EE612620F1D9F7CAD758947FF3CC6D21B)

### 示例3（设置不同容器内组件的zIndex属性）

该示例在不同容器内设置zIndex属性。其中，Text1、Text2和Text3在不同的Stack容器内。虽然Text3的zIndex值最小，但Text1、Text2仍无法按照预期显示在Text3的上方。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ZIndexExample {
5. build() {
6. Stack() {
7. Stack() {
8. // Text1设置zIndex值为2
9. Text('1, zIndex(2)')
10. .size({ width: '40%', height: '30%' }).backgroundColor(0xbbb2cb)
11. .zIndex(2)
12. // Text2设置zIndex值为1
13. Text('2, default zIndex(1)')
14. .size({ width: '70%', height: '50%' }).backgroundColor(0xd2cab3).align(Alignment.TopStart)
15. .zIndex(1)
16. }.width('100%').height(200)

18. Stack() {
19. // zIndex在不同容器的组件中无法生效，Text3会显示在最上方
20. // Text3设置zIndex值为0
21. Text('3, zIndex(0)')
22. .size({ width: '90%', height: '80%' }).backgroundColor(0xc1cbac).align(Alignment.TopStart)
23. .zIndex(0)
24. }.width('100%').height(200)
25. }.width('100%').height(200)
26. }
27. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/qhVruAH-S0i68QJdQ8d8Ow/zh-cn_image_0000002558766008.png?HW-CC-KV=V1&HW-CC-Date=20260429T055112Z&HW-CC-Expire=86400&HW-CC-Sign=2947278A25430D1961499CAB09CF3F9DE512A2A5D6388FFB2AFECD5932C7DA85)
