---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-sensor-service-11
title: 水平仪气泡移动方向错误
breadcrumb: FAQ > 系统开发 > 硬件 > 传感器（Sensor Service） > 水平仪气泡移动方向错误
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:40+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:45b05a99f8d206859feacee27bd8c6a679578c5de530bbd992f5b6e593ce0354
---

## 问题现象

当前水平仪气泡的实际移动方向与预期逻辑相反：当设备左高右低时，气泡向右移动；当左低右高时，气泡向左移动。按照预期，气泡应指向高处，即左高右低时气泡应向左移动，左低右高时应向右移动。

## 背景知识

* [@ohos.sensor](../harmonyos-references/js-apis-sensor.md)：sensor模块提供了获取传感器数据的能力，包括获取传感器属性列表，订阅传感器数据，以及一些通用的传感器算法。
  + [on(type: SensorId.ORIENTATION, callback: Callback<OrientationResponse>, options?: Options): void](../harmonyos-references/js-apis-sensor.md#sensoronsensoridorientation9)：订阅方向传感器数据。
  + [OrientationResponse](../harmonyos-references/js-apis-sensor.md#orientationresponse)：方向传感器数据，包含alpha、beta、gamma三个属性，分别表示设备围绕Z、X、Y轴的旋转角度（单位：度），取值范围分别为[0-360]、[0-±180]、[0-±90]度。
* [translate](../harmonyos-references/ts-universal-attributes-transformation.md#translate)：设置组件平移。可使组件在以组件左上角为坐标原点的坐标系中进行移动（坐标系如下图所示）。其中，x，y，z的值分别表示在对应轴移动的距离，值为正时表示向对应轴的正向移动，值为负时表示向对应轴的反向移动。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/L0eBBkMfR-Gem1MCWPo1nA/zh-cn_image_0000002658854361.png)
* [Canvas](../harmonyos-references/ts-components-canvas-canvas.md)：提供画布组件，用于自定义绘制图形。
  + [CanvasRenderingContext2D](../harmonyos-references/ts-canvasrenderingcontext2d.md)：使用RenderingContext在Canvas组件上进行绘制，绘制对象可以是矩形、文本、图片等。
  + Canvas2D的坐标系默认以Canvas的左上角为坐标原点，沿X轴向右为正值，沿Y轴向下为正值，如下图所示：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/yh1_NvB5StqOmWmn2QRBOw/zh-cn_image_0000002628615114.png)

## 问题定位

1. 查看水平仪气泡在水平、垂直方向的移动是否符合规律，即往更高处移动。当设备左高右低时，气泡应向左移动，反之向右移动；当设备上高下低时，气泡应向上移动，反之向下移动。
2. 水平仪气泡运动常见的实现方式有[Canvas](../harmonyos-references/ts-components-canvas-canvas.md)或设置[translate](../harmonyos-references/ts-universal-attributes-transformation.md#translate)属性，这两种方式的坐标系X轴、Y轴方向相同，当设备左高右低时，气泡应沿X轴逆向移动，反之沿X轴正向移动；当设备上高下低时，气泡应沿Y轴逆向移动，反之沿Y轴正向移动。可通过[DevEco Testing](https://developer.huawei.com/consumer/cn/deveco-testing/?ha_source=sousuo&ha_sourceId=89000251)的UIViewer功能查看是[Canvas](../harmonyos-references/ts-components-canvas-canvas.md)方案还是[translate](../harmonyos-references/ts-universal-attributes-transformation.md#translate)方案，如下图组件树中无[Canvas](../harmonyos-references/ts-components-canvas-canvas.md)，气泡是[Circle](../harmonyos-references/ts-drawing-components-circle.md)组件，可得知是利用[translate](../harmonyos-references/ts-universal-attributes-transformation.md#translate)属性实现气泡移动。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/vR0RrGQ8R1SKbvZoRFIgvA/zh-cn_image_0000002628775010.png "点击放大")
3. 设备旋转方向及角度的数据来源是方向传感器数据[OrientationResponse](../harmonyos-references/js-apis-sensor.md#orientationresponse)中的beta（设备围绕X轴的旋转角度）和gamma值（设备围绕Y轴的旋转角度），这两个值是有正负符号的，beta值为负表示设备上高下低，gamma值为负表示设备左高右低。在将设备旋转角度映射为水平仪气泡移动距离的处理代码中，需要根据旋转角度的正负符号确定气泡的移动方向。

## 分析结论

获取设备传感器数据转换为水平仪坐标时，水平仪气泡的X轴坐标符号与实际相反。

## 修改建议

* 检查对设备传感器数据的转换处理过程，确保水平仪气泡的移动方向与预期一致。以[translate](../harmonyos-references/ts-universal-attributes-transformation.md#translate)方案为例，完整示例代码：

  ```ts
  import { sensor } from '@kit.SensorServiceKit';

  const MAX_RADIUS = 150; // 水平仪最大半径
  const BUBBLE_RADIUS = 15; // 气泡半径
  const MAX_OFFSET = MAX_RADIUS - BUBBLE_RADIUS; // 气泡最大偏移距离

  @Entry
  @Component
  struct spiritPage {
    @State rotateX: number = 0; // 设备沿X轴旋转角度（垂直方向旋转角度）
    @State rotateY: number = 0; // 设备沿Y轴旋转角度（水平方向旋转角度）
    @State bubbleX: number = 0; // 气泡X坐标
    @State bubbleY: number = 0; // 气泡Y坐标
    topRectHeight: number = 30; // 状态栏高度
    bottomRectHeight: number = 10; // 导航条高度

    aboutToAppear(): void {
      // 注册方向传感器监听
      sensor.on(sensor.SensorId.ORIENTATION, (data) => {
        this.rotateY = this.getOrigin(data.gamma);
        this.rotateX = this.getOrigin(data.beta);
        // 计算气泡坐标（每个方向旋转90度时达到最大偏移量，根据旋转度数比例计算坐标）
        // 设备沿X轴旋转（垂直方向）角度映射为气泡的Y坐标，设备沿Y轴旋转（水平方向）角度映射为气泡的X坐标
        this.bubbleX = this.rotateY / 90 * MAX_OFFSET;
        this.bubbleY = this.rotateX / 90 * MAX_OFFSET;
        // 限制气泡在圆盘范围内
        this.bubbleX = Math.min(Math.max(this.bubbleX, -MAX_OFFSET), MAX_OFFSET);
        this.bubbleY = Math.min(Math.max(this.bubbleY, -MAX_OFFSET), MAX_OFFSET);
        let currentDistance = Math.sqrt(Math.pow(this.bubbleX, 2) + Math.pow(this.bubbleY, 2));
        // 如果超出圆形范围，按比例缩放坐标
        if (currentDistance > MAX_OFFSET) {
          let scale = MAX_OFFSET / currentDistance;
          this.bubbleX *= scale;
          this.bubbleY *= scale;
        }
      }, { interval: 1000000 });
    }

    build() {
      Column() {
        Row() {
          Text('测试')
            .fontSize(24)
            .fontWeight(FontWeight.Bold)
        }
        .width('100%')
        .padding(16)

        Stack() {
          // 水平仪背景图片，建议开发者自行替换为所需的图片资源
          Image($r('app.media.bg'))
            .width(MAX_RADIUS * 2)
            .height(MAX_RADIUS * 2)
          // 水平仪气泡
          Circle({ width: BUBBLE_RADIUS * 2, height: BUBBLE_RADIUS * 2 })
            .fill(Color.Blue)
            .translate({
              x: this.bubbleX,
              y: this.bubbleY,
            })
        }
        .width('100%')

        Text(`垂直:${this.rotateX.toFixed(1)}°     水平:${(this.rotateY).toFixed(1)}°`)
          .width(300)
          .height(68)
          .fontSize(20)
          .fontColor('#000000')
          .margin({ top: 44 })
      }
      .padding({
        top: this.topRectHeight,
        bottom: this.bottomRectHeight
      })
    }

    private getOrigin(data: number) {
      let absData = Math.abs(data);
      if (absData <= 90) {
        return data;
      }
      // 旋转角度为90度时水平仪气泡到达边界，当旋转角度的绝对值大于90度时应取补角，同时保留正负号
      return (180 - absData) * Math.sign(data);
    }
  }
  ```
* 水平仪开发指南及[Canvas](../harmonyos-references/ts-components-canvas-canvas.md)方案实现代码见官网文档——[水平仪](../architecture-guides/spirit_level-0000002362176089.md)。

## 总结

水平仪的实现依赖设备传感器数据，最终呈现的是水平仪气泡的位置变化。在数据转换处理过程中，应注意数据的正负符号，在坐标系中按正确的方向移动。对应关系总结如下：

| 方向传感器数据 | 值的范围 | 气泡移动方向 | 对应坐标轴及方向 |
| --- | --- | --- | --- |
| beta | (0,180) | 下 | Y轴正向 |
| beta | (-180,0) | 上 | Y轴逆向 |
| gamma | (0,90) | 右 | X轴正向 |
| gamma | (-90,0) | 左 | X轴逆向 |
