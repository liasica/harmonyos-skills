---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-layout-constraints
title: 布局约束
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 布局与边框 > 布局约束
category: harmonyos-references
scraped_at: 2026-04-28T08:01:05+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:a69a558317eafa14b7f8d68df220222252c47b8cebb8609b244043495eb8c1cc
---

通过组件的宽高比和显示优先级约束组件显示效果。

说明

从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## aspectRatio

PhonePC/2in1TabletTVWearable

aspectRatio(value: number): T

指定当前组件的宽高比，aspectRatio=width/height。

* 仅设置width、aspectRatio时，height=width/aspectRatio。
* 仅设置height、aspectRatio时，width=height\*aspectRatio。
* 同时设置width、height和aspectRatio时，height不生效，height=width/aspectRatio。

设置aspectRatio属性后，组件宽高会受父组件内容区大小限制，[constraintSize](ts-universal-attributes-size.md#constraintsize)的优先级高于aspectRatio。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 指定当前组件的宽高比。  API version 9及以前，默认值为：1.0。  API version 10：无默认值。  **说明：**  该属性在不设置值或者设置非法值(小于等于0)时不生效。  例如，Row只设置宽度且没有子组件，aspectRatio不设置值或者设置成负数时，此时Row高度为0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## displayPriority

PhonePC/2in1TabletTVWearable

displayPriority(value: number): T

设置当前组件在布局容器中显示的优先级。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 设置当前组件在布局容器中显示的优先级。  默认值：1  **说明：**  仅在[Row](ts-container-row.md)/[Column](ts-container-column.md)/[Flex(单行)](ts-container-flex.md)容器组件中生效。  小数点后的数字不作优先级区分，即区间为[x, x + 1)内的数字视为相同优先级。例如：1.0与1.9为同一优先级。  子组件的displayPriority均不大于1时，优先级没有区别。  当子组件的displayPriority大于1时，displayPriority数值越大，优先级越高。若父容器空间不足，隐藏低优先级子组件。若某一优先级的子组件被隐藏，则优先级更低的子组件也都被隐藏。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（设置组件宽高比）

通过aspectRatio设置不同的宽高比。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct AspectRatioExample {
5. private children: string[] = ['1', '2', '3', '4', '5', '6']

7. build() {
8. Column({ space: 20 }) {
9. Text('using container: row').fontSize(14).fontColor(0xCCCCCC).width('100%')
10. Row({ space: 10 }) {
11. ForEach(this.children, (item:string) => {
12. // 组件宽度 = 组件高度*1.5 = 90
13. Text(item)
14. .backgroundColor(0xbbb2cb)
15. .fontSize(20)
16. .aspectRatio(1.5)
17. .height(60)
18. // 组件高度 = 组件宽度/1.5 = 60/1.5 = 40
19. Text(item)
20. .backgroundColor(0xbbb2cb)
21. .fontSize(20)
22. .aspectRatio(1.5)
23. .width(60)
24. }, (item:string) => item)
25. }
26. .size({ width: "100%", height: 100 })
27. .backgroundColor(0xd2cab3)
28. .clip(true)

30. // grid子元素width/height=3/2
31. Text('using container: grid').fontSize(14).fontColor(0xCCCCCC).width('100%')
32. Grid() {
33. ForEach(this.children, (item:string) => {
34. GridItem() {
35. Text(item)
36. .backgroundColor(0xbbb2cb)
37. .fontSize(40)
38. .width('100%')
39. .aspectRatio(1.5)
40. }
41. }, (item:string) => item)
42. }
43. .columnsTemplate('1fr 1fr 1fr')
44. .columnsGap(10)
45. .rowsGap(10)
46. .size({ width: "100%", height: 165 })
47. .backgroundColor(0xd2cab3)
48. }.padding(10)
49. }
50. }
```

**图1** 竖屏显示

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/cV5G25iATEOdab2ReVlZiw/zh-cn_image_0000002552959494.png?HW-CC-KV=V1&HW-CC-Date=20260428T000102Z&HW-CC-Expire=86400&HW-CC-Sign=E6CFC81276F232858DF8B26F9DA2671BC8388476F4671E62D8EF255CF9D43DE2)

**图2** 横屏显示

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/sCO9Rp4zRwyK9pZRWvGZrw/zh-cn_image_0000002583479495.png?HW-CC-KV=V1&HW-CC-Date=20260428T000102Z&HW-CC-Expire=86400&HW-CC-Sign=0581E04BF58570B4F52CD6F5B24F92C3B221B8E9085956640211FE0FAB0BB7AC)

### 示例2（设置组件显示优先级）

使用displayPriority为子组件设置显示优先级。

```
1. class ContainerInfo {
2. label: string = '';
3. size: string = '';
4. }

6. class ChildInfo {
7. text: string = '';
8. priority: number = 0;
9. }

11. @Entry
12. @Component
13. struct DisplayPriorityExample {
14. // 显示容器大小
15. private container: ContainerInfo[] = [
16. { label: 'Big container', size: '90%' },
17. { label: 'Middle container', size: '50%' },
18. { label: 'Small container', size: '30%' }
19. ]
20. private children: ChildInfo[] = [
21. { text: '1\n(priority:2)', priority: 2 },
22. { text: '2\n(priority:1)', priority: 1 },
23. { text: '3\n(priority:3)', priority: 3 },
24. { text: '4\n(priority:1)', priority: 1 },
25. { text: '5\n(priority:2)', priority: 2 }
26. ]
27. @State currentIndex: number = 0;

29. build() {
30. Column({ space: 10 }) {
31. // 切换父级容器大小
32. Button(this.container[this.currentIndex].label).backgroundColor(0x317aff)
33. .onClick(() => {
34. this.currentIndex = (this.currentIndex + 1) % this.container.length;
35. })
36. // 通过变量设置Flex父容器宽度
37. Flex({ justifyContent: FlexAlign.SpaceBetween }) {
38. ForEach(this.children, (item:ChildInfo) => {
39. // 使用displayPriority给子组件绑定显示优先级
40. Text(item.text)
41. .width(120)
42. .height(60)
43. .fontSize(24)
44. .textAlign(TextAlign.Center)
45. .backgroundColor(0xbbb2cb)
46. .displayPriority(item.priority)
47. }, (item:ChildInfo) => item.text)
48. }
49. .width(this.container[this.currentIndex].size)
50. .backgroundColor(0xd2cab3)
51. }.width("100%").margin({ top: 50 })
52. }
53. }
```

横屏显示

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/vg_6-FyeQrSMiR6DE6xBjg/zh-cn_image_0000002552799846.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000102Z&HW-CC-Expire=86400&HW-CC-Sign=4E6EF0857EB7467A7BB54A0B72A3071FADBEAB242DA7B7F6C441042FA7CDA8F6)
