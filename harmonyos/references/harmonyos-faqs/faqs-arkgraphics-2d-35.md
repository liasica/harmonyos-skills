---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkgraphics-2d-35
title: Canvas绘制图形拖动卡顿
breadcrumb: FAQ > 图形开发 > 2D图形（ArkGraphics 2D） > Canvas绘制图形拖动卡顿
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:46+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3a5e32d2a91150c141769da1740cbf769b00d6d16c470f0f8651ebeb1ccb8149
---

## 问题现象

* 使用OffscreenCanvas绘制一张超出屏幕尺寸的PixelMap，监听手势移动事件，跟随手势不间断地重绘，实际视觉呈现效果会出现明显的卡顿现象。
* 问题代码如下：

  ```screen
  // 调整前 isValidate属性在@watch监听方法，第一次加载拖动时会存在卡顿
  redraw() {
    this.renderContext.reset();
    let t1 = Date.now();
    this.startRenderTestDrawImage(this.renderContext);
    let t2 = Date.now();
    console.debug(`canvas 绘制时间=${(t2 - t1)}ms`);
  }
  ```

## 背景知识

* [OffscreenCanvas](../harmonyos-references/ts-components-offscreencanvas.md)提供了一个可以在屏幕外渲染的画布用于绘制自定义图形，这样可以在单独的线程中运行一些任务，从而避免影响应用程序主线程性能。
* [CanvasRenderingContext2D](../harmonyos-references/ts-canvasrenderingcontext2d.md)在Canvas组件上进行绘制，绘制对象可以是矩形、文本、图片等。

## 问题定位

* 初步怀疑超出屏幕或组件区域的图形部分导致拖动卡顿现象。验证措施：裁剪屏幕外图形，使用drawImage接口裁剪显示区域，结果仍然卡顿。
* 进一步猜想是由于绘制的原始图形太大导致拖动卡顿现象。验证措施：传入getPixelMap的尺寸固定到屏幕尺寸，拖动效果没问题；使用当前超出屏幕尺寸的值，拖动卡顿。可以确认卡顿现象与原始图形尺寸有直接关联，实际业务原始图也是很大，需要解决大图情况下拖动卡顿问题。
* 在录屏记录现象时发现针对大图拖动并不存在卡顿，怀疑是绘制操作过于频繁导致卡顿现象。验证措施：由于录屏时屏幕刷新帧率固定为60，设置显示屏幕刷新帧率为60，绘制拖动无卡顿；设置显示屏幕刷新帧率为120，绘制拖动存在明显卡顿。怀疑手势响应事件过于频繁，渲染速度低于事件响应频率，需要想办法降低事件响应或考虑多线程。

## 分析结论

渲染速度低于事件响应频率，比如一秒内不停拖动，手势事件会触发120次，GPU需要执行120次绘制操作。

## 修改建议

* 针对图形裁剪与控制响应手势事件混合的场景，在响应事件绘制函数中添加延时判断，确保一定时间段内（比如：15ms）内只响应一次事件并重绘。
* 按照修改建议调整后代码如下：

  ```screen
  import { display } from '@kit.ArkUI';
  import { displaySync } from '@kit.ArkGraphics2D';

  @Entry
  @Component
  export struct CanvasFix {
    private settings: RenderingContextSettings = new RenderingContextSettings(true);
    private renderContext: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
    private panOption: PanGestureOptions = new PanGestureOptions({ direction: PanDirection.All });
    // 如果需要复现问题请把代码修改为注释行代码
    // @StorageLink('validateCanvas') @Watch('redraw')
    @StorageLink('validateCanvas') @Watch('redrawWithStep')
    private isValidate: boolean = true;
    canvasHeight: Length = '50%';
    private screenWidth: number = 0;
    private screenHeight: number = 0;
    private scrollX = 0;
    private scrollY = 0;
    private curTime = 0;

    aboutToAppear() {
      this.isValidate = true;
      let displayClass: display.Display | null = null;
      try {
        displayClass = display.getDefaultDisplaySync();
        this.screenHeight = this.getUIContext().px2vp(displayClass.height);
        this.canvasHeight = this.screenHeight;
        this.screenWidth = this.getUIContext().px2vp(displayClass.width);
      } catch (exception) {
        console.error('Failed to obtain the default display object. Code: ' + JSON.stringify(exception));
      }

      let range: ExpectedFrameRateRange = {
        // 创建和配置帧率参数
        expected: 30, // 设置期望绘制帧率为30hz
        min: 0, // 配置帧率范围
        max: 60 // 配置帧率范围
      };
      let backDisplaySyncSlow: displaySync.DisplaySync = displaySync.create(); // 创建DisplaySync实例
      backDisplaySyncSlow.setExpectedFrameRateRange(range); // 设置帧率
      if (backDisplaySyncSlow) {
        backDisplaySyncSlow.start();
      }
    }

    // 自定义组件析构销毁之前执行，不允许在aboutToDisappear函数中改变状态变量，特别是@Link变量的修改可能会导致应用程序行为不稳定
    aboutToDisappear(): void {
      console.debug("CanvasView 销毁了");
    }

    cacheBitmap: PixelMap | undefined = undefined;

    getPixelMap(w: number, h: number): PixelMap {
      if (this.cacheBitmap) {
        return this.cacheBitmap;
      }
      let offset = 0;
      let _settings = new RenderingContextSettings(true);
      let offCanvas = new OffscreenCanvas(w, h);
      let offContext = offCanvas.getContext("2d", _settings);

      let grad = offContext.createLinearGradient(50, 0, 300, 100);

      offContext.save();
      offContext.translate(-offset, -offset);
      offContext.fillStyle = "#ffa7a9a9";
      offContext.fillRect(offset, offset, w, h);

      grad.addColorStop(0.0, 'rgba(250, 151, 215, 1.00)');
      grad.addColorStop(0.7, 'rgba(230, 197, 210, 1.00)');
      grad.addColorStop(0.8, 'rgba(126, 202, 254, 1.00)');
      grad.addColorStop(1.0, 'rgba(151, 209, 160, 1.00)');
      offContext.fillStyle = grad;
      offContext.fillRect(offset, offset, w, h);

      offContext.fillStyle = "#fffdd378";
      offContext.font = "24vp";
      offContext.fillText('测试文本', offset + 220, offset + 375);
      offContext.translate(offset, offset);
      offContext.restore();
      this.cacheBitmap = offContext.getPixelMap(0, 0, w, h);
      return this.cacheBitmap;
    }

    startRenderTestDrawImage(renderContext: CanvasRenderer) {
      let canvasW = Math.ceil(this.renderContext.width);
      let canvasH = Math.ceil(this.screenHeight > 0 ? this.screenHeight : this.renderContext.height);

      let cacheW = Math.round(canvasW * 1.5);
      let cacheH = Math.round(canvasH * 1.5);

      let cacheXpos = Math.round((cacheW - canvasW) * 0.5 + this.scrollX);
      let cacheYpos = Math.round((cacheH - canvasH) * 0.5 + this.scrollY);

      renderContext.save();
      renderContext.translate(-cacheXpos, -cacheYpos);
      renderContext.drawImage(this.getPixelMap(cacheW, cacheH), 0, 0);
      renderContext.translate(cacheXpos, cacheYpos);
      renderContext.restore();
    }
    // 调整前 isValidate属性在@watch监听方法，第一次加载拖动时会存在卡顿
    redraw() {
      this.renderContext.reset();
      let t1 = Date.now();
      this.startRenderTestDrawImage(this.renderContext);
      let t2 = Date.now();
      console.debug(`canvas 绘制时间=${(t2 - t1)}ms`);
    }
    // 调整后 isValidate属性在@watch监听方法，在redraw前添加了15ms延时
    redrawWithStep() {
      if ((Date.now() - this.curTime) < 15) {
        return;
      }
      this.curTime = Date.now();
      this.redraw();
    }

    build() {
      Column({ space: FlexAlign.SpaceBetween }) {
        Row() {
          Canvas(this.renderContext)
            .width('100%')
            .height('50%')
            .backgroundColor(Color.White)
            .onReady(() => {
              console.debug("Canvas onReady");
              this.redraw();
            })
            .gesture(GestureGroup(GestureMode.Exclusive,
              PanGesture(this.panOption)
                .onActionUpdate((event: GestureEvent) => {
                  this.scrollX = -event.offsetX;
                  this.scrollY = -event.offsetY;
                  let value = AppStorage.get<boolean>('validateCanvas');
                  AppStorage.setOrCreate<boolean>('validateCanvas', !value);
                  console.debug(`偏移x1=${this.scrollX},y1=${this.scrollY}`);
                })
                .onActionEnd((event: GestureEvent) => {
                  console.debug(`偏移x2=${event.offsetX},y2=${event.offsetY}`);
                  this.scrollX = 0;
                  this.scrollY = 0;
                  this.redraw();
                })
            ));
        }
        .margin(10)
        .clip(true)
        .border({
          color: Color.Gray,
          width: 1,
          radius: 24
        });
      };
    }
  }
  ```
