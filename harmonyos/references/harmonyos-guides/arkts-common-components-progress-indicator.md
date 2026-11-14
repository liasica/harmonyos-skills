---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-progress-indicator
title: 进度条 (Progress)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 添加组件 > 进度条 (Progress)
category: harmonyos-guides
scraped_at: 2026-11-14T08:47:04+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:45e6073affb22ec41717a8ad7f04826f421e3c68e776f8d4699e85b17e3a520c
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/5hx2oTucRp6eO3hdQi91WA/zh-cn_image_0000002817426139.png?HW-CC-KV=V1&HW-CC-Date=20261114T004526Z&HW-CC-Expire=31536000000&HW-CC-Sign=BCE62CB6F034E7EC38B18174A4727E7663176530EA6AE3CCA51709D4D13E374A)

## 设置进度条样式

Progress有5种可选类型，通过[ProgressType](../harmonyos-references/ts-basic-components-progress.md#progresstype8枚举说明)可以设置进度条样式。ProgressType类型包括：ProgressType.Linear（线性样式）、 ProgressType.Ring（环形无刻度样式）、ProgressType.ScaleRing（环形有刻度样式）、ProgressType.Eclipse（圆形样式）和ProgressType.Capsule（胶囊样式）。

* 线性样式进度条（默认类型）

  **说明** 

  从API version 9开始，组件高度大于宽度时，自适应垂直显示；组件高度等于宽度时，保持水平显示。

  ```typescript
  Progress({ value: 20, total: 100, type: ProgressType.Linear }).width(200).height(50)
  Progress({ value: 20, total: 100, type: ProgressType.Linear }).width(50).height(200)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/7w-yrEI-TTiIo4UbLvUXFw/zh-cn_image_0000002788466720.png?HW-CC-KV=V1&HW-CC-Date=20261114T004526Z&HW-CC-Expire=31536000000&HW-CC-Sign=EF384F98D295B8A342D7DCC0E01B55A585DBA56D1FEF63ABC8470DC4B50DC91B)
* 环形无刻度样式进度条

  ```typescript
  // 从左往右，1号环形进度条，默认前景色为蓝色渐变，默认strokeWidth进度条宽度为4.0vp
  Progress({ value: 40, total: 150, type: ProgressType.Ring }).width(100).height(100)
  // 从左往右，2号环形进度条
  Progress({ value: 40, total: 150, type: ProgressType.Ring }).width(100).height(100)
    .color(Color.Grey)    // 进度条前景色为灰色
    .style({ strokeWidth: 15})    // 设置strokeWidth进度条宽度为15vp
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/yiNeX3ZoT0uQwjxWlBg9Kw/zh-cn_image_0000002817506207.png?HW-CC-KV=V1&HW-CC-Date=20261114T004526Z&HW-CC-Expire=31536000000&HW-CC-Sign=FB11F714716E896BE3822944A2D5BA9479A67974F2D90482230AEF2097A18151)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/-XXIG3FvTmWL-hMZLPynAg/zh-cn_image_0000002788306778.png?HW-CC-KV=V1&HW-CC-Date=20261114T004526Z&HW-CC-Expire=31536000000&HW-CC-Sign=252186F33A35EF1D67AB538636F10937CBA23A71A8B03131969E8747FFE1E9F1)
* 圆形样式进度条

  ```typescript
  // 从左往右，1号圆形进度条，默认前景色为蓝色
  Progress({ value: 10, total: 150, type: ProgressType.Eclipse }).width(100).height(100)
  // 从左往右，2号圆形进度条，指定前景色为灰色
  Progress({ value: 20, total: 150, type: ProgressType.Eclipse }).color(Color.Grey).width(100).height(100)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/Ssar6EMUTUSrG6aWExZiDQ/zh-cn_image_0000002817426141.png?HW-CC-KV=V1&HW-CC-Date=20261114T004526Z&HW-CC-Expire=31536000000&HW-CC-Sign=B8BB6ECE4E4883B107353E62327CBF80B180B85677BA88B5BC806918163C8EB5)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/JM2DOGziSp-tEAM9ndcwDQ/zh-cn_image_0000002788466722.png?HW-CC-KV=V1&HW-CC-Date=20261114T004526Z&HW-CC-Expire=31536000000&HW-CC-Sign=822000C439ACBA332F99F2D0EC0E93F17E96E299ECCD8822B8CA2D7581EE1FE0)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/MRhONAUoTaOk_jxxKZto-w/zh-cn_image_0000002817506209.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004526Z&HW-CC-Expire=31536000000&HW-CC-Sign=9D472B165C9A316A91445BB49A1ADFAF19244F189D5E1CB7021A85AAC9E247B8)
