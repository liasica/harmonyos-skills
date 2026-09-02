---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1452
title: HarmonyOS多窗口截图合并方案
breadcrumb: FAQ > 应用框架开发 > UI框架 > 屏幕管理 > HarmonyOS多窗口截图合并方案
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:13+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ff22351db9eb521f08bbb6c387d220d2381ef65918ff7d57cecf804e4f728a45
---

## 问题现象

当前页面由两个窗口组成，截图时仅能获取其中一个窗口的内容，无法实现与用户手动截图一致的效果。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/lJgNXgTlTDa6BnCJzGGEuQ/zh-cn_image_0000002628604264.png "点击放大")

## 背景知识

* [Window](../harmonyos-references/js-apis-window.md)：窗口提供管理窗口的一些基础能力，包括对当前窗口的创建、销毁、各属性设置，以及对各窗口间的管理调度。用于生成子窗口。
* [snapshot](../harmonyos-references/arkts-apis-window-window.md#snapshot9)：获取窗口级别截图。
* [Canvas](../harmonyos-references/ts-components-canvas-canvas.md)：提供画布组件，用于自定义绘制图形。将图片在画布组件上进行合并实现与手动截图相同的效果。

## 解决方案

使用snapshot分别获取每个窗口的截图，再根据窗口的叠加顺序，将截图按照顺序使用drawImage绘制在Canvas上的同一位置，然后获取截图。

* 主要页面（截图以及绘制合并主要逻辑）。

  ```screen
  import { BusinessError } from '@kit.BasicServicesKit';
  import { window } from '@kit.ArkUI';
  import { image } from '@kit.ImageKit';
  import { common } from '@kit.AbilityKit';

  @Entry
  @Component
  struct Index {
    private context = this.getUIContext().getHostContext(); // 获取Context
    mainWindowClass: window.Window | undefined = undefined;
    private settings: RenderingContextSettings = new RenderingContextSettings(true);
    private canvasContext: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

    aboutToAppear(): void {
      // 获取主窗口
      window.getLastWindow(this.context).then((value) => {
        this.mainWindowClass = value;
      });
    }

    build() {
      Row() {
        Column() {
          TextInput({ placeholder: '输入文本后可复制，也可以粘贴到此处' })
            .width('90%')
            .margin(5);
          Button('弹出水印子窗口')
            .width('90%')
            .margin(20)
            .onClick(() => {
              try {
                let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
                context.windowStage.createSubWindow('subWindowTest')
                  .then((win: window.Window) => {
                    win.setUIContent('pages/Watermark');
                    win.setWindowFocusable(false);
                    win.setWindowTouchable(false);
                    win.showWindow().then(() => {
                      win.setWindowBackgroundColor('#00000000');
                    });
                  })
                  .catch((err: BusinessError) => {
                    console.info(`Failed to create the subwindow. Cause code: ${err.code}, message: ${err.message}`);
                  });
              } catch (exception) {
                console.info(`Failed to create the subwindow. Cause code: ${exception.code}, message: ${exception.message}`);
              }
            });
          Button("截图")
            .width('90%')
            .margin({ bottom: 20 })
            .onClick(async () => {
              // 清除画布内容
              this.canvasContext.clearRect(0, 0, 1000, 1000);
              // 主窗口截图
              this.mainWindowClass?.snapshot((err: BusinessError, pixelMap: image.PixelMap) => {
                const errCode: number = err.code;
                if (errCode) {
                  console.error(`Failed to snapshot window. Cause code: ${err.code}, message: ${err.message}`);
                  return;
                }
                // 绘制主窗口到画布
                this.canvasContext.drawImage(pixelMap, 90, 50, 200, 400);
              });
              window.getLastWindow(this.context, (err: BusinessError, topWindow) => {
                const errCode: number = err.code;
                if (errCode) {
                  return;
                }
                topWindow.snapshot((err: BusinessError, pixelMap: image.PixelMap) => {
                  const errCode: number = err.code;
                  if (errCode) {
                    console.error(`Failed to snapshot window. Cause code: ${err.code}, message: ${err.message}`);
                    return;
                  }
                  // 绘制子窗口到画布
                  this.canvasContext.drawImage(pixelMap, 90, 50, 200, 400);
                });
              });
            });
          Canvas(this.canvasContext)
            .width('100%')
            .height('100%')
            .backgroundColor('#ffdedbdb');
        }
        .width('100%');
      }
      .height('100%');
    }
  }
  ```

* 子窗口（示例窗口，无关键逻辑）。

  ```screen
  @Entry
  @Component
  struct Watermark {
    canvas: CanvasRenderingContext2D = new CanvasRenderingContext2D(new RenderingContextSettings(true));

    build() {
      Column() {
        Column() {
          Canvas(this.canvas)
            .width('100%')
            .height('100%')
            .hitTestBehavior(HitTestMode.Transparent)
            .onReady(() => {
              this.canvas.fillStyle = '#ff000000';
              this.canvas.font = '16vp';
              this.canvas.textAlign = 'center';
              this.canvas.textBaseline = 'middle';
              // 在这里绘制文字水印，也可以是图片水印
              for (let i = 0; i < this.canvas.width / 120; i++) {
                this.canvas.translate(120, 0);
                let j = 0;
                for (; j < this.canvas.height / 120; j++) {
                  this.canvas.rotate(-Math.PI / 180 * 30);
                  // 此处水印数据是写死的，具体请替换为自己的水印
                  this.canvas.fillText('test', -60, -60);
                  this.canvas.rotate(Math.PI / 180 * 30);
                  this.canvas.translate(0, 120);
                }
                this.canvas.translate(0, -120 * j);
              }
            })
        }
        .backgroundColor(Color.White)
        .borderRadius(20)
        .width('100%')
        .height('100%')
        .justifyContent(FlexAlign.Center)
      }
      .opacity(0.1)
      .justifyContent(FlexAlign.Center)
      .height('100%')
      .width('100%')
      .backgroundColor('#60000000')
      .transition(TransitionEffect.OPACITY.animation({ duration: 300 }))
    }
  }
  ```
