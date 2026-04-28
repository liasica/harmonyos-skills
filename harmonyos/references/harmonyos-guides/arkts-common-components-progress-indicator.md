---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-progress-indicator
title: 进度条 (Progress)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 添加组件 > 进度条 (Progress)
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5ea2071b77dfe35d15fe6270802079b8c2ffc255d2f0379bcce3206bc97cf7ef
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/bpb2O-WoQ7ijnHWBYB2j2w/zh-cn_image_0000002552798242.png?HW-CC-KV=V1&HW-CC-Date=20260427T233940Z&HW-CC-Expire=86400&HW-CC-Sign=199B2B4F55CA560378435141821F26B9BDCB2D72AA704AFB9ED9D927D7D4D946)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/dxBxfVTgT8SUiiLwTtZJoQ/zh-cn_image_0000002583437937.png?HW-CC-KV=V1&HW-CC-Date=20260427T233940Z&HW-CC-Expire=86400&HW-CC-Sign=F3E9257D4BE2E667C985426B25A258D3D6D5828035113792B74206F46BC2CFE3)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/ZPuk2vSCRk2mbLwAk1Dw-w/zh-cn_image_0000002552957892.png?HW-CC-KV=V1&HW-CC-Date=20260427T233940Z&HW-CC-Expire=86400&HW-CC-Sign=2A59B92851AFED0BE58BD751E81603C6FF67F2A3965517FC708B71D444BA80E7)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/vkuD0kqPRWGUuyf8IeceHA/zh-cn_image_0000002583477893.png?HW-CC-KV=V1&HW-CC-Date=20260427T233940Z&HW-CC-Expire=86400&HW-CC-Sign=7B23FE1C442B46150B5583E6A67A6D7A0931254BC0535D9ADA726C92DEC09690)
* 圆形样式进度条

  ```
  1. // 从左往右，1号圆形进度条，默认前景色为蓝色
  2. Progress({ value: 10, total: 150, type: ProgressType.Eclipse }).width(100).height(100)
  3. // 从左往右，2号圆形进度条，指定前景色为灰色
  4. Progress({ value: 20, total: 150, type: ProgressType.Eclipse }).color(Color.Grey).width(100).height(100)
  ```

  [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/InfoComponent/ProgressProject/entry/src/main/ets/pages/Index.ets#L76-L81)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/ukAcKzxfTRGTx2Jgueve1A/zh-cn_image_0000002552798244.png?HW-CC-KV=V1&HW-CC-Date=20260427T233940Z&HW-CC-Expire=86400&HW-CC-Sign=EF9ADD30BD58CB0EC9F3E8546D7BEE0719DBA37E5A092F9AE1870B50C1350818)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/vqk1XdAvSpimcTm9Aisq5g/zh-cn_image_0000002583437939.png?HW-CC-KV=V1&HW-CC-Date=20260427T233940Z&HW-CC-Expire=86400&HW-CC-Sign=A02BE73EA9839117EAD44D0B432494D9F175EBE4CB8F3DA83FB242E1A45DA1D0)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/-5EpKTxVT0CEHFeqU5zKaA/zh-cn_image_0000002552957894.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233940Z&HW-CC-Expire=86400&HW-CC-Sign=DBEE35E340DBB1E972484DD3C97486EC890B2097B4FC068142B8663657856EE6)
