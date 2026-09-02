---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1049
title: 如何实现Canvas绘制刷新以及防止绘制丢失
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现Canvas绘制刷新以及防止绘制丢失
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:26+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:0e14b79b821b3952a12a2affb9a0b5750ee5f6ee7e92143131fc1a7bfc178625
---

## 问题现象

Canvas动态绘制时，如何实现内容实时刷新与防止绘制丢失是两大核心问题，如何有效解决？

## 背景知识

* [Canvas](../harmonyos-references/ts-components-canvas-canvas.md)：提供画布组件，用于自定义绘制图形。
* [onReady](../harmonyos-references/ts-components-canvas-canvas.md#onready)：Canvas组件初始化完成或者发生大小变化时的事件回调，当该事件被触发时画布被清空。
* [@Monitor](../harmonyos-guides/arkts-new-monitor.md)：@Monitor装饰器用于监听状态变量修改，使得状态变量具有深度监听的能力。

## 解决方案

* **场景一**：Canvas绘制如何刷新。

  Canvas无自动重绘机制，需要手动触发绘制刷新，共有4种实现方式，对比如下：

  | 实现方式 | 触发机制 | 适用场景 |
  | --- | --- | --- |
  | 利用clearRect方法清空画布。 | 开发者手动调用。 | 局部刷新场景（如擦除部分区域）。 |
  | 利用reset方法重置画布。 | 开发者手动调用。 | 全部重绘场景（如重置Canvas路径、样式）。 |
  | 利用@Watch装饰器监听变量，根据变量变化刷新。 | 数据变量变更时自动触发。 | 数据驱动的动态内容（如实时进度条、图表）、需要与UI状态强绑定的场景，用状态管理V1实现。 |
  | 利用@Monitor装饰器监听变量，根据变量变化刷新。 | 数据变量变更时自动触发。 | 数据驱动的动态内容（如实时进度条、图表）、需要与UI状态强绑定的场景，用状态管理V2实现。 |

  + **方式一**：利用[clearRect](../atomic-ascf/apis-canvas-rendering-context-2d.md#canvasrenderingcontext2dclearrect)方法清空画布，进而重新绘制，代码示例如下：

    ```ts
    @Entry
    @Component
    struct CanvasClearRect {
      private settings: RenderingContextSettings = new RenderingContextSettings(true);
      private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

      build() {
        Column() {
          Canvas(this.context)
            .width(300)
            .height(400)
            .onReady(() => {
              this.context.fillStyle = '#0097D4';
              this.context.fillRect(50, 100, 200, 100);
            })
            .backgroundColor('#f1f3f5');

          Button('Re Draw')
            .width('80%')
            .margin({ top: 20 })
            .onClick(() => {
              this.draw();
            });
        }
        .height('100%')
        .width('100%');
      }

      private draw() {
        // 用clearRect清除画布中内容
        this.context.clearRect(0, 0, 300, 400);
        this.context.fillStyle = '#0097D4';
        this.context.beginPath();
        this.context.arc(100, 100, 50, 0, 2 * Math.PI);
        this.context.fill();
      }
    }
    ```

    实现效果如下：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/nMEP6PLoTBGvJWOrt41tIg/zh-cn_image_0000002628565454.png "点击放大")
  + **方式二**：利用[reset](../harmonyos-references/ts-components-canvas-common-method.md#reset12)方法重置画布状态，清空绘制路径，代码示例如下：

    ```ts
    @Entry
    @Component
    struct CanvasReset {
      private settings: RenderingContextSettings = new RenderingContextSettings(true);
      private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
      // "common/images/example.png"需要替换为开发者所需的图像资源文件
      private img: ImageBitmap = new ImageBitmap('common/images/example.png');
      private angle: number = Math.PI * 5 / 4;

      build() {
        Column() {
          Canvas(this.context)
            .width(300)
            .height(300)
            .onReady(() => {
              this.draw();
            })
            .backgroundColor('#f1f3f5');

          Button('Re Draw')
            .width('80%')
            .margin({ top: 20 })
            .onClick(() => {
              this.angle += Math.PI / 4;
              this.draw();
            });
        }
        .height('100%')
        .width('100%');
      }

      private draw() {
        // 这里clearRect无法清除路径，需要用reset重置画布状态
        this.context.reset();
        let width = 300;
        this.context.beginPath();
        this.context.moveTo(width / 2, width / 2);
        this.context.arc(width / 2, width / 2, width / 2, Math.PI, this.angle);
        this.context.clip();
        this.context.drawImage(this.img, 0, 0, width, width);
      }
    }
    ```

    实现效果如下：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/Nd3YS6KXRbSYNpyVpa9kqQ/zh-cn_image_0000002658924761.png "点击放大")
  + **方式三**：利用[@Watch](../harmonyos-guides/arkts-watch.md)装饰器监听状态变量，当数据刷新时，触发重新绘制逻辑，示例参考：[Canvas绘制内容如何动态更新](faqs-arkui-225.md)。
  + **方式四**：利用@Monitor装饰器监听嵌套Class对象属性的变化，代码示例如下：

    ```ts
    @ObservedV2
    class User {
      @Trace name: string;
      @Trace age: number;

      constructor(name: string, age: number) {
        this.name = name;
        this.age = age;
      }
    }

    @Entry
    @ComponentV2
    struct CanvasMonitor {
      private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(new RenderingContextSettings(true));
      @Local userArr: Array<User> = [new User('Tom', 24), new User('Jerry', 18)];

      @Monitor('userArr.length')
      draw() {
        this.context.clearRect(0, 0, 200, 500);
        for (let i = 0; i < this.userArr.length; i++) {
          this.context.fillText(this.userArr[i].name, 50, i * 30 + 50);
          this.context.fillText(this.userArr[i].age.toString(), 100, i * 30 + 50);
        }
      }

      build() {
        Column() {
          Canvas(this.context)
            .width(300)
            .height(400)
            .onReady(() => {
              this.context.font = '60px';
              this.draw();
            })
            .height('25%')
            .width('100%')
            .backgroundColor('#f1f3f5');

          Button('Change info property')
            .width('80%')
            .margin({ top: 20 })
            .onClick(() => {
              this.userArr.push(new User('Kitty', 12));
            });
        }
        .width('100%')
        .height('100%');
      }
    }
    ```

    实现效果如下：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/078VejpcTIyo5mIpLhMDGw/zh-cn_image_0000002628405556.png "点击放大")
* **场景二**：Canvas绘制防止丢失。

  Canvas的onReady方法在Canvas组件初始化完成或者发生大小变化时会触发。比如折叠屏展开场景、横竖屏切换场景以及动态扩展Canvas组件宽高场景，可能会触发onReady方法，这时在onReady方法之外绘制的内容就会丢失，需要恢复绘制，共有2种实现方式，对比如下：

  | 实现方式 | 触发机制 | 适用场景 |
  | --- | --- | --- |
  | 在onReady中恢复绘制。 | Canvas初始化完成时或者发生大小变化时。 | 绘制内容较少时，不涉及监听尺寸变化场景。 |
  | 在onAreaChange事件恢复绘制。 | Canvas尺寸发生大小变化时。 | 需要精确根据尺寸变化进行绘制的场景。 |

  + **方式一**：在onReady方法中恢复画布绘制，示例参考：[横竖屏切换时，如何防止画布被清空](faqs-arkgraphics-2d-36.md)。
  + **方式二**：绑定[onAreaChange](../harmonyos-references/ts-universal-component-area-change-event.md#onareachange)方法，Canvas大小发生变化时同样会触发onAreaChange事件，这时可以在onAreaChange中恢复绘制逻辑，代码示例如下：

    ```ts
    @Entry
    @Component
    struct CanvasOnAreaChange {
      private settings: RenderingContextSettings = new RenderingContextSettings(true);
      private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
      @State myWidth: number = 300;

      build() {
        Column() {
          Canvas(this.context)
            .width(this.myWidth)
            .height(400)
            .onReady(() => {
              this.context.fillStyle = '#0097D4';
            })
            .onAreaChange(() => {
              // 监听尺寸变化事件，重新绘制，恢复画布
              this.draw();
            })
            .backgroundColor('#f1f3f5');

          Button('Change Size')
            .width('80%')
            .margin({ top: 20 })
            .onClick(() => {
              this.myWidth += 20;
            });
        }
        .height('100%')
        .width('100%');
      }

      private draw() {
        // 用clearRect清除画布中内容
        this.context.clearRect(0, 0, 300, 400);
        this.context.fillRect(50, 100, 200, 100);
      }
    }
    ```

    效果预览：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/8BOBoWreRQStM9WuM7yqKg/zh-cn_image_0000002658804829.png "点击放大")

## 常见FAQ

Q：在onReady方法中绘制了较多的内容，当Canvas尺寸变化时会触发重绘，引发闪烁如何解决？

A：这种情况可以避免在onReady方法中进行大量绘制，仅在其中设置Canvas属性，在外部方法中进行绘制；或者固定Canvas的宽高，防止触发onReady方法。
