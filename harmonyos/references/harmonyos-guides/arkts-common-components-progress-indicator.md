---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-progress-indicator
title: 进度条 (Progress)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 添加组件 > 进度条 (Progress)
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:7c8c7453c38e0efb44389ae253c05639d17e8db4d5b91e0c8ae5e9c7fcf3c7a1
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/PZ33VT8nTMaoBJpXxiIaMw/zh-cn_image_0000002786359044.png?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=D5037C5DC2FD124317C6F4E92C5298BA0E33FE8662FACE82917F27F20F75FC2E)

## 设置进度条样式

Progress有5种可选类型，通过[ProgressType](../harmonyos-references/ts-basic-components-progress.md#progresstype8枚举说明)可以设置进度条样式。ProgressType类型包括：ProgressType.Linear（线性样式）、 ProgressType.Ring（环形无刻度样式）、ProgressType.ScaleRing（环形有刻度样式）、ProgressType.Eclipse（圆形样式）和ProgressType.Capsule（胶囊样式）。

* 线性样式进度条（默认类型）

  **说明** 

  从API version 9开始，组件高度大于宽度时，自适应垂直显示；组件高度等于宽度时，保持水平显示。

  ```typescript
  Progress({ value: 20, total: 100, type: ProgressType.Linear }).width(200).height(50)
  Progress({ value: 20, total: 100, type: ProgressType.Linear }).width(50).height(200)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/CqTpWoGiSzi0azi-pkOAWg/zh-cn_image_0000002815558465.png?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=BEEF782B5F13D4F053FBE7B40FCA4070322B7E084B294B5A3DC02181D524E397)
* 环形无刻度样式进度条

  ```typescript
  // 从左往右，1号环形进度条，默认前景色为蓝色渐变，默认strokeWidth进度条宽度为4.0vp
  Progress({ value: 40, total: 150, type: ProgressType.Ring }).width(100).height(100)
  // 从左往右，2号环形进度条
  Progress({ value: 40, total: 150, type: ProgressType.Ring }).width(100).height(100)
    .color(Color.Grey)    // 进度条前景色为灰色
    .style({ strokeWidth: 15})    // 设置strokeWidth进度条宽度为15vp
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/tFeNx3cvTZK_Lf0D5BCYZA/zh-cn_image_0000002815398549.png?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=A7D5ECBA9C5184B926F28B73620BD5830BC579998EA5992A910D4D1D089A91D0)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/6b2lA4w2Q5aYAxLXQOb1oQ/zh-cn_image_0000002786518974.png?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=E1033DBF6781094EEEC2CC02A57BB639A0652CB2578725E5206B5BF0DDE0C4C2)
* 圆形样式进度条

  ```typescript
  // 从左往右，1号圆形进度条，默认前景色为蓝色
  Progress({ value: 10, total: 150, type: ProgressType.Eclipse }).width(100).height(100)
  // 从左往右，2号圆形进度条，指定前景色为灰色
  Progress({ value: 20, total: 150, type: ProgressType.Eclipse }).color(Color.Grey).width(100).height(100)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/86LvllSxTZq_3pQjlWtfAw/zh-cn_image_0000002786359046.png?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=0EC46674683EA6FFA8C1CF711759A2D16A1A308E97EE6B5C196E6013A9B51ED7)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/xaMb71e8RfeD4fIz8Q5Avg/zh-cn_image_0000002815558467.png?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=737D141AF75C130882D575818818679CE298DEAFBBC8D0296426883220FA9757)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/B8Qz3LytQUigp16_tXhwWw/zh-cn_image_0000002815398551.gif?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=F42AB5E4DD2B79B9AFD12D1582C207D8F50D1FCA323DCDBC056A679EA3755E33)
