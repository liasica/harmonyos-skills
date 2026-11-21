---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-progress-indicator
title: 进度条 (Progress)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 添加组件 > 进度条 (Progress)
category: harmonyos-guides
scraped_at: 2026-11-21T09:11:07+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:d6b0072d5dd77fdd73316fcab4701640302e882fd2ded3bbf6fdb8232d7ff3c6
---

Progress是进度条显示组件，显示内容通常为目标操作的当前进度。具体用法请参考[Progress](../harmonyos-references/ts-basic-components-progress.md)。

## 创建进度条

Progress通过调用接口来创建，接口调用方式如下：

```ts
Progress(options: {value: number, total?: number, type?: ProgressType})
```

其中，value用于设置当前进度值，total用于设置进度总长度，type用于设置Progress样式。

```typescript
Progress({ value: 24, total: 100, type: ProgressType.Linear }) // 创建一个进度总长为100，当前进度值为24的线性进度条
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/nLdJtKkHTAyftXboyo_WOg/zh-cn_image_0000002821836659.png?HW-CC-KV=V1&HW-CC-Date=20261121T010943Z&HW-CC-Expire=31536000000&HW-CC-Sign=4C28044F8DA3D8CA02B19371D78AF12F8ABF575880F450E1B7AB7F394F1A1193)

## 设置进度条样式

Progress有5种可选类型，通过[ProgressType](../harmonyos-references/ts-basic-components-progress.md#progresstype8枚举说明)可以设置进度条样式。ProgressType类型包括：ProgressType.Linear（线性样式）、 ProgressType.Ring（环形无刻度样式）、ProgressType.ScaleRing（环形有刻度样式）、ProgressType.Eclipse（圆形样式）和ProgressType.Capsule（胶囊样式）。

* 线性样式进度条（默认类型）

  **说明** 

  从API version 9开始，组件高度大于宽度时，自适应垂直显示；组件高度等于宽度时，保持水平显示。

  ```typescript
  Progress({ value: 20, total: 100, type: ProgressType.Linear }).width(200).height(50)
  Progress({ value: 20, total: 100, type: ProgressType.Linear }).width(50).height(200)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/vJvxV8R0Qi-J3qP8zjc-Fw/zh-cn_image_0000002821756661.png?HW-CC-KV=V1&HW-CC-Date=20261121T010943Z&HW-CC-Expire=31536000000&HW-CC-Sign=03C5D3526DF4E006B9EF2A3FE29753C384647DC71325A62E9E5BF2547B1E9737)
* 环形无刻度样式进度条

  ```typescript
  // 从左往右，1号环形进度条，默认前景色为蓝色渐变，默认strokeWidth进度条宽度为4.0vp
  Progress({ value: 40, total: 150, type: ProgressType.Ring }).width(100).height(100)
  // 从左往右，2号环形进度条
  Progress({ value: 40, total: 150, type: ProgressType.Ring }).width(100).height(100)
    .color(Color.Grey)    // 进度条前景色为灰色
    .style({ strokeWidth: 15})    // 设置strokeWidth进度条宽度为15vp
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/KxRK9zh4TyarXSIAPjtbFQ/zh-cn_image_0000002793036724.png?HW-CC-KV=V1&HW-CC-Date=20261121T010943Z&HW-CC-Expire=31536000000&HW-CC-Sign=A6531627737B1AF1DC7FF3F664938DBFEF52552E46F4561BC7A5DA68A54A1DB8)
* 环形有刻度样式进度条

  ```typescript
  Progress({ value: 20, total: 150, type: ProgressType.ScaleRing }).width(100).height(100)
    .backgroundColor(Color.Black)
    .style({ scaleCount: 20, scaleWidth: 5 })    // 设置环形有刻度进度条总刻度数为20，刻度宽度为5vp
  Progress({ value: 20, total: 150, type: ProgressType.ScaleRing }).width(100).height(100)
    .backgroundColor(Color.Black)
    .style({ strokeWidth: 15, scaleCount: 20, scaleWidth: 5 })    // 设置环形有刻度进度条宽度15vp，总刻度数为20，刻度宽度为5vp
  Progress({ value: 20, total: 150, type: ProgressType.ScaleRing }).width(100).height(100)
    .backgroundColor(Color.Black)
    .style({ strokeWidth: 15, scaleCount: 20, scaleWidth: 3 })    // 设置环形有刻度进度条宽度15vp，总刻度数为20，刻度宽度为3vp
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/QTo4mr-5T9eqPFQjpM1SAg/zh-cn_image_0000002792876756.png?HW-CC-KV=V1&HW-CC-Date=20261121T010943Z&HW-CC-Expire=31536000000&HW-CC-Sign=C938A2E6FABEC9E9E8328156FC7B5D2E11B450320816018B2004F7F02009B806)
* 圆形样式进度条

  ```typescript
  // 从左往右，1号圆形进度条，默认前景色为蓝色
  Progress({ value: 10, total: 150, type: ProgressType.Eclipse }).width(100).height(100)
  // 从左往右，2号圆形进度条，指定前景色为灰色
  Progress({ value: 20, total: 150, type: ProgressType.Eclipse }).color(Color.Grey).width(100).height(100)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/hivPTEzwRIKHpT9E39li0A/zh-cn_image_0000002821836661.png?HW-CC-KV=V1&HW-CC-Date=20261121T010943Z&HW-CC-Expire=31536000000&HW-CC-Sign=B20E7A7D1FDEEBC5B0CAB343DCC875AD365DB6333A9117AF5D6DDEFC173C7216)
* 胶囊样式进度条

  **说明** 

  + 头尾两端圆弧处的进度展示效果与ProgressType.Eclipse样式一致。
  + 中段处的进度展示效果为矩形状长条，与ProgressType.Linear线性样式相似。
  + 组件高度大于宽度时，自适应垂直显示。

  ```typescript
  Progress({ value: 10, total: 150, type: ProgressType.Capsule }).width(100).height(50)
  Progress({ value: 20, total: 150, type: ProgressType.Capsule }).width(50).height(100).color(Color.Grey)
  Progress({ value: 50, total: 150, type: ProgressType.Capsule }).width(50).height(100).color(Color.Blue).backgroundColor(Color.Black)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/AEzrjXXsRLGhrMv6ToGC3Q/zh-cn_image_0000002821756663.png?HW-CC-KV=V1&HW-CC-Date=20261121T010943Z&HW-CC-Expire=31536000000&HW-CC-Sign=ECC4B37BE4A6FAF23FC4CA17471D3C6D9B79116D5B0769346E0F20CE76EFC15A)

## 场景示例

更新当前进度值，如应用安装进度条，可通过点击Button增加progressValue，value属性将progressValue设置给Progress组件，进度条组件即会触发刷新，更新当前进度。

```typescript
@Entry
@Component
struct ProgressCase1 {
  @State progressValue: number = 0;    // 设置进度条初始值为0
  build() {
    Column() {
      Column() {
        Progress({value:this.progressValue, total:100, type:ProgressType.Capsule}).width(200).height(50)
        Row().width('100%').height(5)
        // 请将$r('app.string.progress_add')替换为实际资源文件，在本示例中该资源文件的value值为"进度条+5"
        Button($r('app.string.progress_add'))
          .onClick(()=>{
            this.progressValue += 5;
            if (this.progressValue > 100){
              this.progressValue = 0;
            }
          })
      }
    }.width('100%').height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/HKhJ0C5iSoShgnUPgpB-8A/zh-cn_image_0000002793036726.gif?HW-CC-KV=V1&HW-CC-Date=20261121T010943Z&HW-CC-Expire=31536000000&HW-CC-Sign=9F69DCC6DB343828B477E5A36C20AD383E78CBB6098E35E9EE64E8E6A9AF43DE)
