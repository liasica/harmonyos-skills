---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-650
title: 如何使用Canvas绘制饼状图
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何使用Canvas绘制饼状图
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:23+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7397aa801c007973754910c0206c08e978aba42b6555c175b78e12840cdfdf14
---

## 问题现象

如何使用Canvas绘制饼状图以展示不同类型的数据占比？问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/9Hi6rLyPSoa4qhkEAdXibg/zh-cn_image_0000002628554406.png "点击放大")

## 背景知识

* [Canvas](../harmonyos-references/ts-components-canvas-canvas.md)：是一种画布组件，用于自定义绘制图形，绘制对象可以是基础形状、文本、图片等。
* [CanvasRenderingContext2D](../harmonyos-references/ts-canvasrenderingcontext2d.md)：是Canvas组件的参数，可使用它在Canvas画布上进行绘制，绘制对象可以是矩形、文本、图片等。

## 解决方案

使用Canvas，根据各个分类对应的占比，绘制扇形，最后组成饼状图。具体步骤如下：

1. 根据指定数组填装数据，并且计算出总量。

   ```ts
   class SectorInfo {
     name: string = ''; // 名称
     data: number = 0; // 数据
     color: string = ''; // 颜色
     fontSize: number = 14; // 字体大小
     radius: number = 40; // 半径
   }
   ```

   ```ts
   aboutToAppear(): void {
     // 装载模拟数据
     const categories = ['视频广告', '搜索引擎', '直接访问', '邮件营销', '联盟广告'];
     const dataCount = [1, 2, 1, 3, 1];
     const colorArr =
     ['#4f81bd', '#c0504d', '#9bbb59', '#8064a2', '#4bacc6 '];
     for (let index = 0; index < categories.length; index++) {
       let sectorInfo = new SectorInfo();
       sectorInfo.name = categories[index];
       sectorInfo.data = dataCount[index];
       sectorInfo.color = colorArr[index];
       this.allData += dataCount[index];
       this.sectorInfoArr.push(sectorInfo);
       if (this.maxData < dataCount[index]) {
         this.maxData = dataCount[index];
       }
       if (this.minData > dataCount[index]) {
         this.minData = dataCount[index];
       }
     }
   }
   ```
2. 根据当前分类的数据和总数据占比，计算出扇形的起始角度和终点角度。

   ```ts
   drawChart() {
     this.context.clearRect(0, 0, this.centerX * 2, this.centerY * 2);
     // 上一个扇形的结束角度
     let lastEndAngle: number = -Math.PI / 2;
     for (let index = 0; index < this.sectorInfoArr.length; index++) {
       const element = this.sectorInfoArr[index];
       // 计算当前扇形的起始角度和终点角度
       let startAngle: number = lastEndAngle;
       let endAngle: number = lastEndAngle + element.data / this.allData * 2 * Math.PI;
       if (this.isTypeChange) {
         element.radius = this.radius * (0.5 + (element.data - this.minData) / this.maxData / 2);
       } else {
         element.radius = this.radius;
       }
       this.drawSector(startAngle, endAngle, element);
       this.drawBrokenLineAndText(startAngle, endAngle, element);
       lastEndAngle = endAngle;
     }
   }
   ```
3. 根据扇形的起始角度和终点角度，以及对应的数据信息绘制扇形。

   ```ts
   drawSector(startAngle: number, endAngle: number, sectorInfo: SectorInfo) {
     this.context.beginPath();
     this.context.arc(this.centerX, this.centerY, sectorInfo.radius, startAngle, endAngle);
     this.context.lineWidth = sectorInfo.radius * 2;
     this.context.strokeStyle = sectorInfo.color;
     this.context.stroke();
     this.context.restore();
   }
   ```
4. 根据扇形的起始角度和终点角度，以及对应的数据信息绘制折线和文字。

   ```ts
   drawBrokenLineAndText(startAngle: number, endAngle: number, sectorInfo: SectorInfo) {
     let angle = endAngle - startAngle;
     let brokenLineLength: number = 20;
     let brokenLineLengthTemp: number = 15;
     // 计算扇形中心角度
     let centerAngle = startAngle + angle / 2;
     let r = sectorInfo.radius * 2 + brokenLineLength / 2;
     // 计算折线起始点
     let startX = this.centerX + (r - brokenLineLength) * Math.cos(centerAngle);
     let startY = this.centerY + (r - brokenLineLength) * Math.sin(centerAngle);
     // 计算折线转折点
     let brokenX = this.centerX + r * Math.cos(centerAngle);
     let brokenY = this.centerY + r * Math.sin(centerAngle);
     let endX = brokenX;
     let endY = brokenY;
     // 添加文字属性
     this.context.textBaseline = 'middle';
     this.context.fillStyle = sectorInfo.color;
     this.context.font = this.getUIContext().fp2px(sectorInfo.fontSize) + 'px sans-serif';
     // 获取文本
     let textWidth = this.context.measureText(sectorInfo.name).width;
     let textHeight = this.context.measureText(sectorInfo.name).height;
     let textX = endX;
     let textY = endY - textHeight + 5;
     let lastX = 0;
     // 根据文字计算折线终点，根据角度单位判断折线左右方向，以及文字的起点
     if (centerAngle < Math.PI / 2) {
       this.context.textAlign = 'right';
       endX = brokenX + brokenLineLengthTemp + textWidth;
       textX = brokenX + brokenLineLengthTemp + textWidth;
       lastX = endX - 27;
     } else {
       this.context.textAlign = 'left';
       endX = brokenX - brokenLineLengthTemp - textWidth;
       textX = endX;
       lastX = endX + 27;
     }
     // 绘制折线
     this.context.beginPath();
     this.context.lineWidth = 2;
     this.context.strokeStyle = sectorInfo.color;
     this.context.moveTo(startX, startY);
     this.context.lineTo(brokenX, brokenY);
     this.context.lineTo(lastX, endY);
     // 填充文字
     this.context.fillText(sectorInfo.name, textX, textY);
     this.context.stroke();
   }
   ```
5. 完整示例参考如下：

   ```ts
   class SectorInfo {
     name: string = ''; // 名称
     data: number = 0; // 数据
     color: string = ''; // 颜色
     fontSize: number = 14; // 字体大小
     radius: number = 40; // 半径
   }

   @Entry
   @Component
   struct drawPieChart {
     @State sectorInfoArr: Array<SectorInfo> = [];
     @State @Watch('drawChart') isTypeChange: boolean = false;
     // 用来配置CanvasRenderingContext2D对象的参数，包括是否开启抗锯齿，true表明开启抗锯齿。
     private settings: RenderingContextSettings = new RenderingContextSettings(true);
     // 用来创建CanvasRenderingContext2D对象，通过在canvas中调用CanvasRenderingContext2D对象来绘制。
     private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
     private centerX: number = 0;
     private centerY: number = 0;
     private radius: number = 40;
     private allData: number = 0; // 总数
     private maxData: number = 40; // 最大值
     private minData: number = 20; // 最小值

     // 绘制扇形
     drawSector(startAngle: number, endAngle: number, sectorInfo: SectorInfo) {
       this.context.beginPath();
       this.context.arc(this.centerX, this.centerY, sectorInfo.radius, startAngle, endAngle);
       this.context.lineWidth = sectorInfo.radius * 2;
       this.context.strokeStyle = sectorInfo.color;
       this.context.stroke();
       this.context.restore();
     }

     // 绘制折线和文字
     drawBrokenLineAndText(startAngle: number, endAngle: number, sectorInfo: SectorInfo) {
       let angle = endAngle - startAngle;
       let brokenLineLength: number = 20;
       let brokenLineLengthTemp: number = 15;
       // 计算扇形中心角度
       let centerAngle = startAngle + angle / 2;
       let r = sectorInfo.radius * 2 + brokenLineLength / 2;
       // 计算折线起始点
       let startX = this.centerX + (r - brokenLineLength) * Math.cos(centerAngle);
       let startY = this.centerY + (r - brokenLineLength) * Math.sin(centerAngle);
       // 计算折线转折点
       let brokenX = this.centerX + r * Math.cos(centerAngle);
       let brokenY = this.centerY + r * Math.sin(centerAngle);
       let endX = brokenX;
       let endY = brokenY;
       // 添加文字属性
       this.context.textBaseline = 'middle';
       this.context.fillStyle = sectorInfo.color;
       this.context.font = this.getUIContext().fp2px(sectorInfo.fontSize) + 'px sans-serif';
       // 获取文本
       let textWidth = this.context.measureText(sectorInfo.name).width;
       let textHeight = this.context.measureText(sectorInfo.name).height;
       let textX = endX;
       let textY = endY - textHeight + 5;
       let lastX = 0;
       // 根据文字计算折线终点，根据角度单位判断折线左右方向，以及文字的起点
       if (centerAngle < Math.PI / 2) {
         this.context.textAlign = 'right';
         endX = brokenX + brokenLineLengthTemp + textWidth;
         textX = brokenX + brokenLineLengthTemp + textWidth;
         lastX = endX - 27;
       } else {
         this.context.textAlign = 'left';
         endX = brokenX - brokenLineLengthTemp - textWidth;
         textX = endX;
         lastX = endX + 27;
       }
       // 绘制折线
       this.context.beginPath();
       this.context.lineWidth = 2;
       this.context.strokeStyle = sectorInfo.color;
       this.context.moveTo(startX, startY);
       this.context.lineTo(brokenX, brokenY);
       this.context.lineTo(lastX, endY);
       // 填充文字
       this.context.fillText(sectorInfo.name, textX, textY);
       this.context.stroke();
     }

     aboutToAppear(): void {
       // 装载模拟数据
       const categories = ['视频广告', '搜索引擎', '直接访问', '邮件营销', '联盟广告'];
       const dataCount = [1, 2, 1, 3, 1];
       const colorArr =
         ['#4f81bd', '#c0504d', '#9bbb59', '#8064a2', '#4bacc6 '];
       for (let index = 0; index < categories.length; index++) {
         let sectorInfo = new SectorInfo();
         sectorInfo.name = categories[index];
         sectorInfo.data = dataCount[index];
         sectorInfo.color = colorArr[index];
         this.allData += dataCount[index];
         this.sectorInfoArr.push(sectorInfo);
         if (this.maxData < dataCount[index]) {
           this.maxData = dataCount[index];
         }
         if (this.minData > dataCount[index]) {
           this.minData = dataCount[index];
         }
       }
     }

     drawChart() {
       this.context.clearRect(0, 0, this.centerX * 2, this.centerY * 2);
       // 上一个扇形的结束角度
       let lastEndAngle: number = -Math.PI / 2;
       for (let index = 0; index < this.sectorInfoArr.length; index++) {
         const element = this.sectorInfoArr[index];
         // 计算当前扇形的起始角度和终点角度
         let startAngle: number = lastEndAngle;
         let endAngle: number = lastEndAngle + element.data / this.allData * 2 * Math.PI;
         if (this.isTypeChange) {
           element.radius = this.radius * (0.5 + (element.data - this.minData) / this.maxData / 2);
         } else {
           element.radius = this.radius;
         }
         this.drawSector(startAngle, endAngle, element);
         this.drawBrokenLineAndText(startAngle, endAngle, element);
         lastEndAngle = endAngle;
       }
     }

     build() {
       Column() {
         Canvas(this.context)
           .width('90%')
           .height('40%')
           .backgroundColor('#fff5f5f1')
           .onAreaChange((oldArea: Area, newArea: Area) => {
             // 计算饼图的中心点
             this.centerX = Number(newArea.width) / 2;
             this.centerY = Number(newArea.height) / 2;
             this.drawChart();
           })
           .onReady(() => {
             console.info('onReady');
           })
         Button('切换状态')
           .onClick(() => {
             this.isTypeChange = !this.isTypeChange;
           })
       }
       .height('100%')
       .width('100%')
     }
   }
   ```
