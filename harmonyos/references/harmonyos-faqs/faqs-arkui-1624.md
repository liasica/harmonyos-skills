---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1624
title: 如何实现随机生成数字图形验证码
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现随机生成数字图形验证码
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:24+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:c8c342100765b9c19b8e2d28dd3aabb5803a8723d2e01136d8e6d4b417820c44
---

## 问题现象

如何实现下图的验证码功能？

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/UhOpxEHbQxabBviY56ABoQ/zh-cn_image_0000002658976785.png "点击放大")

## 背景知识

* [CanvasRenderingContext2D](../harmonyos-references/ts-canvasrenderingcontext2d.md)：使用RenderingContext在Canvas组件上进行绘制，绘制对象可以是矩形、文本、图片等。
* [translate](../harmonyos-references/ts-components-canvas-common-method.md#translate)：移动当前坐标系的原点。
* [rotate](../harmonyos-references/ts-components-canvas-common-method.md#rotate)：针对当前坐标轴进行顺时针旋转。
* [fillText](../atomic-ascf/apis-canvas-rendering-context-2d.md#canvasrenderingcontext2dfilltext)：绘制填充类文本。
* [moveTo](../harmonyos-references/ts-components-canvas-common-method.md#moveto)：路径从当前点移动到指定点。
* [lineTo](../harmonyos-references/ts-components-canvas-common-method.md#lineto)：从当前点到指定点进行路径连接。

## 解决方案

实现思路如下：

1. 创建一个自定义的画图形验证码的方法drawImgCode。图形分为3部分：随机数字、随机颜色的线条、随机颜色的点。
2. 封装一个自定义组件ImageCode实现图形验证码。onReady回调里初始化图形验证码，onClick事件刷新图形验证码。
3. 使用TextInput和ImageCode实现图中功能。

完整示例参考如下：

```ts
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

@Entry
@Component
struct ValidationCodeL {
  @State showCode: string = '';

  build() {
    Row() {
      TextInput({ placeholder: '请输入验证码' })
        .layoutWeight(1);
      ImageCode({ showCode: this.showCode, controller: childRef })
        .width(140)
        .height(40);

      Text('刷新').onClick(() => {
        childRef.changeText('');
      });
    }
    .height('100%')
    .width('100%')
    .padding({ left: 30, right: 30 });
  }
}

export class CommonUtil {
  // 随机生成文本内容时使用的值
  sCode: string = '1,2,3,4,5,6,7,8,9,0';
  aCode: string[] = this.sCode.split(',');
  aLength: number = this.aCode.length; // 获取到数组的长度

  static getRandomNumber() {

    let rand = cryptoFramework.createRandom();
    // 设置生成随机数的字节长度为1
    let randData = rand.generateRandomSync(1);
    // 自定义范围(0-10之内)
    let numRan: number = Math.fround(randData.data[0] * 10 / 2550);

    return numRan;
  }

  // 绘制图形验证码
  drawImgCode(context: CanvasRenderingContext2D, canvasWidth: number = 100, canvasHeight: number = 40): string {
    // 用于保存验证码
    let showCode: string = '';
    // 清除当前画布内容，用作刷新画布
    context.clearRect(0, 0, canvasWidth, canvasHeight);

    for (let i = 0; i < 4; i++) { // 这里的for循环可以控制验证码位数
      const j = Math.floor(CommonUtil.getRandomNumber() * this.aLength); // 获取到随机的索引值
      const deg = CommonUtil.getRandomNumber() - 0.5; // 产生一个随机弧度
      const txt = this.aCode[j]; // 得到随机的一个内容
      showCode += txt.toLowerCase(); // 转小写
      const x = 10 + i * 20; // 文字在canvas上的x坐标
      const y = canvasHeight / 2 + CommonUtil.getRandomNumber() * 8; // 文字在canvas上的y坐标
      context.font = '20vp sans-serif';
      context.translate(x, y);
      context.rotate(deg);
      context.fillStyle = this.getColor();
      context.fillText(txt, 0, 0);
      context.rotate(-deg);
      context.translate(-x, -y);
    }
    for (let i = 0; i <= 5; i++) { // 验证码上显示线条
      context.strokeStyle = this.getColor();
      context.beginPath();
      context.moveTo(CommonUtil.getRandomNumber() * canvasWidth, CommonUtil.getRandomNumber() * canvasHeight);
      context.lineTo(CommonUtil.getRandomNumber() * canvasWidth, CommonUtil.getRandomNumber() * canvasHeight);
      context.stroke();
    }
    for (let i = 0; i <= 20; i++) { // 验证码上的小点
      context.strokeStyle = this.getColor(); // 随机生成
      context.beginPath();
      const x = CommonUtil.getRandomNumber() * canvasWidth;
      const y = CommonUtil.getRandomNumber() * canvasHeight;
      context.moveTo(x, y);
      context.lineTo(x + 1, y + 1);
      context.stroke();
    }
    return showCode;
  }

  // 获取随机颜色rgb
  getColor() {
    const r = Math.floor(CommonUtil.getRandomNumber() * 256);
    const g = Math.floor(CommonUtil.getRandomNumber() * 256);
    const b = Math.floor(CommonUtil.getRandomNumber() * 256);
    return 'rgb(' + r + ',' + g + ',' + b + ')';
  }
}

@Component
export default struct ImageCode {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  @State canvasWidth: number = 100;
  @State canvasHeight: number = 40;
  @Link showCode: string;
  private controller: ImageCodeController = new ImageCodeController();

  aboutToAppear(): void {
    if (this.controller) {
      this.controller.changeText = this.changeText;
    }
  }

  private changeText = () => {
    return new CommonUtil().drawImgCode(this.context, this.canvasWidth, this.canvasHeight);
  };

  build() {
    Row() {
      // 在canvas中调用CanvasRenderingContext2D对象。
      Canvas(this.context)
        .width(this.canvasWidth)
        .height(this.canvasHeight)
        .backgroundColor('#CCC')
        .onReady(() => {
          // 在这里绘制图形
          this.showCode = new CommonUtil().drawImgCode(this.context, this.canvasWidth, this.canvasHeight);
        })
        .onClick(() => {
          new CommonUtil().drawImgCode(this.context, this.canvasWidth, this.canvasHeight);
        });
    }
    .width('100%')
    .height('100%');
  }
}

class ImageCodeController {
  changeText = (value: string) => {
    return value;
  };
}

let childRef = new ImageCodeController();
```
