---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-progress-indicator
title: 进度条 (Progress)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 添加组件 > 进度条 (Progress)
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:53+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c59b5e6c20d2ba7fbc97591ccbc3682c798605dd440725f72cb82f9cc7449a36
---

Progress是进度条显示组件，显示内容通常为目标操作的当前进度。具体用法请参考[Progress](../harmonyos-references/ts-basic-components-progress.md)。

## 创建进度条

Progress通过调用接口来创建，接口调用方式如下：

```
1. Progress(options: {value: number, total?: number, type?: ProgressType})
```

其中，value用于设置初始进度值，total用于设置进度总长度，type用于设置Progress样式。

```
1. Progress({ value: 24, total: 100, type: ProgressType.Linear }) // 创建一个进度总长为100，初始进度值为24的线性进度条
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/eASdHqo0TIOwS2WO4OhXUw/zh-cn_image_0000002558764382.png?HW-CC-KV=V1&HW-CC-Date=20260429T052751Z&HW-CC-Expire=86400&HW-CC-Sign=9519819B94FEB764E81A2C9F1CE0511833CD431A003E20E88282BBC660DA2CEE)

## 设置进度条样式

Progress有5种可选类型，通过ProgressType可以设置进度条样式。ProgressType类型包括：ProgressType.Linear（线性样式）、 ProgressType.Ring（环形无刻度样式）、ProgressType.ScaleRing（环形有刻度样式）、ProgressType.Eclipse（圆形样式）和ProgressType.Capsule（胶囊样式）。

* 线性样式进度条（默认类型）

  说明

  从API version 9开始，组件高度大于宽度时，自适应垂直显示；组件高度等于宽度时，保持水平显示。

  ```
  1. Progress({ value: 20, total: 100, type: ProgressType.Linear }).width(200).height(50)
  2. Progress({ value: 20, total: 100, type: ProgressType.Linear }).width(50).height(200)
  ```

  [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/InfoComponent/ProgressProject/entry/src/main/ets/pages/Index.ets#L39-L42)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/4emqRrQJQoy_4u37rMBb6g/zh-cn_image_0000002558604726.png?HW-CC-KV=V1&HW-CC-Date=20260429T052751Z&HW-CC-Expire=86400&HW-CC-Sign=28EE6B8116239CAB7D4D6CAD2B97BAC9ADE2B574DE0B36EC04754980BC275F8D)
* 环形无刻度样式进度条

  ```
  1. // 从左往右，1号环形进度条，默认前景色为蓝色渐变，默认strokeWidth进度条宽度为2.0vp
  2. Progress({ value: 40, total: 150, type: ProgressType.Ring }).width(100).height(100)
  3. // 从左往右，2号环形进度条
  4. Progress({ value: 40, total: 150, type: ProgressType.Ring }).width(100).height(100)
  5. .color(Color.Grey)    // 进度条前景色为灰色
  6. .style({ strokeWidth: 15})    // 设置strokeWidth进度条宽度为15.0vp
  ```

  [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/InfoComponent/ProgressProject/entry/src/main/ets/pages/Index.ets#L47-L54)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/4Z53UJ3tR7KFqz4JWwDpIw/zh-cn_image_0000002589324251.png?HW-CC-KV=V1&HW-CC-Date=20260429T052751Z&HW-CC-Expire=86400&HW-CC-Sign=79B3E28DA3AD022536C8E02C5B55CFA83B557B5302A483DC1533C96CDA0126DA)
* 环形有刻度样式进度条

  ```
  1. Progress({ value: 20, total: 150, type: ProgressType.ScaleRing }).width(100).height(100)
  2. .backgroundColor(Color.Black)
  3. .style({ scaleCount: 20, scaleWidth: 5 })    // 设置环形有刻度进度条总刻度数为20，刻度宽度为5vp
  4. Progress({ value: 20, total: 150, type: ProgressType.ScaleRing }).width(100).height(100)
  5. .backgroundColor(Color.Black)
  6. .style({ strokeWidth: 15, scaleCount: 20, scaleWidth: 5 })    // 设置环形有刻度进度条宽度15，总刻度数为20，刻度宽度为5vp
  7. Progress({ value: 20, total: 150, type: ProgressType.ScaleRing }).width(100).height(100)
  8. .backgroundColor(Color.Black)
  9. .style({ strokeWidth: 15, scaleCount: 20, scaleWidth: 3 })    // 设置环形有刻度进度条宽度15，总刻度数为20，刻度宽度为3vp
  ```

  [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/InfoComponent/ProgressProject/entry/src/main/ets/pages/Index.ets#L60-L70)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/tH8NoguwRGGN4BLRctEFKw/zh-cn_image_0000002589244191.png?HW-CC-KV=V1&HW-CC-Date=20260429T052751Z&HW-CC-Expire=86400&HW-CC-Sign=919BAA8700BF580A36900C817CA31ED0B993E5A2B59A427C454ACEE850704582)
* 圆形样式进度条

  ```
  1. // 从左往右，1号圆形进度条，默认前景色为蓝色
  2. Progress({ value: 10, total: 150, type: ProgressType.Eclipse }).width(100).height(100)
  3. // 从左往右，2号圆形进度条，指定前景色为灰色
  4. Progress({ value: 20, total: 150, type: ProgressType.Eclipse }).color(Color.Grey).width(100).height(100)
  ```

  [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/InfoComponent/ProgressProject/entry/src/main/ets/pages/Index.ets#L76-L81)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/Gb5cv6YGRzyu-XnJ61uZcw/zh-cn_image_0000002558764384.png?HW-CC-KV=V1&HW-CC-Date=20260429T052751Z&HW-CC-Expire=86400&HW-CC-Sign=B5114AAB0673C07E01E0B6CEEA8E5D2C504B40AD04D20DF9BE499DBBD7D898B6)
* 胶囊样式进度条

  说明

  + 头尾两端圆弧处的进度展示效果与ProgressType.Eclipse样式一致。
  + 中段处的进度展示效果为矩形状长条，与ProgressType.Linear线性样式相似。
  + 组件高度大于宽度时，自适应垂直显示。

  ```
  1. Progress({ value: 10, total: 150, type: ProgressType.Capsule }).width(100).height(50)
  2. Progress({ value: 20, total: 150, type: ProgressType.Capsule }).width(50).height(100).color(Color.Grey)
  3. Progress({ value: 50, total: 150, type: ProgressType.Capsule }).width(50).height(100).color(Color.Blue).backgroundColor(Color.Black)
  ```

  [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/InfoComponent/ProgressProject/entry/src/main/ets/pages/Index.ets#L87-L91)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/vyeFOefbT6ervWzYAJzN-Q/zh-cn_image_0000002558604728.png?HW-CC-KV=V1&HW-CC-Date=20260429T052751Z&HW-CC-Expire=86400&HW-CC-Sign=235956C6A4AC8F64DCB43DACC74F8072B2FDCA3144BC1AE4A24981E6A72DDCF8)

## 场景示例

更新当前进度值，如应用安装进度条，可通过点击Button增加progressValue，value属性将progressValue设置给Progress组件，进度条组件即会触发刷新，更新当前进度。

```
1. @Entry
2. @Component
3. struct ProgressCase1 {
4. @State progressValue: number = 0;    // 设置进度条初始值为0
5. build() {
6. Column() {
7. Column() {
8. Progress({value:0, total:100, type:ProgressType.Capsule}).width(200).height(50).value(this.progressValue)
9. Row().width('100%').height(5)
10. // 请将$r('app.string.progress_add')替换为实际资源文件，在本示例中该资源文件的value值为"进度条+5"
11. Button($r('app.string.progress_add'))
12. .onClick(()=>{
13. this.progressValue += 5;
14. if (this.progressValue > 100){
15. this.progressValue = 0;
16. }
17. })
18. }
19. }.width('100%').height('100%')
20. }
21. }
```

[ProgressCase1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/InfoComponent/ProgressProject/entry/src/main/ets/pages/ProgressCase1.ets#L15-L37)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/ZldlOqbTSzaHNykh6NmkAg/zh-cn_image_0000002589324253.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052751Z&HW-CC-Expire=86400&HW-CC-Sign=8FD90F501ABEF8FA32ABAB28DE49B930030D26065C06D677179E2D991848048E)
