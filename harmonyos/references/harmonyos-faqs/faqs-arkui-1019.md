---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1019
title: 组件曲线移动动画
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 组件曲线移动动画
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:26+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:47797a5ac1fa1efa44064a3e62b98d08175342ac21018d0cdc991cd78c164754
---

## 问题现象

当前的路径动画方法实现组件位置变化时，仅支持在各个路径点中依次直线移动，实现曲线移动时动画不够平滑。

## 背景知识

* [UIContext.createAnimator](../harmonyos-references/arkts-apis-uicontext-uicontext.md#createanimator)：创建AnimatorResult动画类，通过设置动画帧回调时对组件属性修改来实现动画效果，可对组件动画做播放，暂停，重置，反向播放，取消等操作，可以设置对动画的完成，取消，重复状态回调。
* [keyframeAnimateTo](../harmonyos-references/ts-keyframeanimateto.md)：在UIContext中提供keyframeAnimateTo接口来指定若干个关键帧状态，实现分段的动画。同属性动画，布局类改变宽高的动画。
* 贝塞尔曲线原理：
  1. 如下图所示，P0为曲线的起始点，P1为曲线的终点，Pt为曲线中的各个坐标点，t为P0到P1的进度百分比。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/EhOSRJzbQt-q6sJmsK_-zg/zh-cn_image_0000002658804077.png "点击放大")

     Pt的坐标点可以通过起始点P0的坐标，加上(P1-P0)\*t + P0计算得出。

     计算公式：

     Pt = P0 + (P1 - P0)\*t = (1 - t)P0 + t\*P1
  2. 下图所示是二阶贝塞尔曲线，共有P0，P1，P2三个控制点，P0和P1构成一阶P11(t)，P1和P2构成一阶P12(t)，在由P11(t)和P12(t)的基础上，计算得出二阶贝塞尔点P2t。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/XK1ymegPQ1in1T1U7ayqkA/zh-cn_image_0000002628564714.png "点击放大")

     计算公式：

     P11 = (1 - t)P0 + t\*P1

     P12 = (1 - t)P1 + t\*P2

     P2t = (1 - t)P11 + t\*P12 = (1 - t)²P0 + 2t\*(1 - t)P1 + t²P2
  3. 下图所示是三阶贝塞尔曲线，共有P0，P1，P2，P3四个控制点，计算降阶得P11，P12，P13得到一阶贝塞尔点，再次计算降阶得P21，P22二阶贝塞尔点，最终计算得到三阶P3t贝塞尔点。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/uCCsIUZoR8CxSONGYqTi7g/zh-cn_image_0000002658924019.png "点击放大")

     计算公式：

     P11 = (1 - t)P0 + t\*P1

     P12 = (1 - t)P1 + t\*P2

     P13 = (1 - t)P2 + t\*P3

     P21 = (1 - t)P11 + t\*P12

     P22 = (1 - t)P12 + t\*P13

     P3t = (1 - t)P21 + t\*P22 = (1 - t)³

## 解决方案

* **方案一：**

  用UIContext.createAnimator创建帧动画，在onFrame帧回调中，使用预设的控制点和当前动画进度，计算动画贝塞尔曲线路径坐标点。

  1. 配置AnimatorOptions动画选项定义Animator类：

     ```ts
     let animatorOption: AnimatorOptions = {
       duration: 1000,
       delay: 0,
       easing: 'linear',
       iterations: 1,
       fill: 'forwards',
       direction: 'normal',
       begin: 0,
       end: 1
     };
     ```
  2. 参考贝塞尔曲线计算原理，计算组件动画过程中的坐标点：

     ```ts
     getCurve(progress: number): Translate {
       let translates: Translate[] = this.translates;
       while (translates.length > 1) {
         let translate2: Translate[] = [];
         for (let i = 0; i < translates.length - 1; i++) {
           let translate: Translate = {
             x: (1 - progress) * translates[i].x + progress * translates[i + 1].x,
             y: (1 - progress) * translates[i].y + progress * translates[i + 1].y
           };
           translate2.push(translate);
         }
         translates = translate2;
       }
       return translates[0];
     }
     ```
  3. 配置定义Animator类接收到帧时回调，入参动画的当前值，取值范围为AnimatorOptions定义的[begin, end]，默认取值范围为[0,1]。

     ```ts
     this.animatorOptions.onFrame = (progress: number) => {
       let translate: Translate = this.getCurve(progress);
       this.markAnchorX = translate.x;
       this.markAnchorY = translate.y;
     };
     ```

     ```ts
     Column() {
       Image($rawfile('AddShoppingCart.png')) // 需要替换为开发者所需的图像资源文件
         .width(25)
         .height(25)
         .objectFit(ImageFit.Auto);
     }
     .justifyContent(FlexAlign.Center)
     .alignItems(HorizontalAlign.Center)
     .width(30)
     .height(30)
     .borderRadius(15)
     .backgroundColor($r('app.color.start_window_background')) // 需要替换为开发者所需的颜色资源文件
     .visibility(this.vis)
     .markAnchor({ x: this.markAnchorX, y: this.markAnchorY + 40 })
     .transition({ scale: { x: this.imgScale, y: this.imgScale, z: 0 } })
     .margin({ top: this.marginBottom - this.topRectHeight, left: this.marginLeft });
     ```

  完整示例代码参考如下：

  ```ts
  import { AnimatorOptions, AnimatorResult, ComponentUtils, componentUtils, window } from '@kit.ArkUI';
  import { common } from '@kit.AbilityKit';
  import { hilog } from '@kit.PerformanceAnalysisKit';

  interface Translate {
    x: number,
    y: number
  }

  const TAG = 'CurveAnimatorPage';

  @Entry
  @Component
  struct CurveAnimatorPage {
    lists: string[] = [];
    shoppingCart: number[] = [];
    imgs: string[] = ['welfare_product_1.png', 'welfare_product_2.png', 'welfare_product_3.png', 'welfare_product_4.png',
      'welfare_product_5.png',
      'welfare_product_6.png', 'welfare_product_7.png', 'welfare_product_8.png']; // 需要替换为开发者所需的图像资源文件
    topRectHeight: number = 0;
    @State endPosition: Translate | undefined = undefined;
    @State vis: Visibility = Visibility.Hidden;
    @State markAnchorY: number = 0;
    @State markAnchorX: number = 0;
    @State marginBottom: number = 0;
    @State marginLeft: number = 0;
    @State imgScale: number = 1.0;
    @State sum: number = 0;

    // 初始化数据
    aboutToAppear(): void {
      for (let index = 0; index < 8; index++) {
        const element = `第${index}个商品`;
        this.lists.push(element);
        this.shoppingCart.push(0);
      }
      this.getWindowAvoidArea(this.getUIContext().getHostContext() as common.UIAbilityContext);
    }

    build() {
      Column() {
        Column() {
          Text(`商品目录`)
            .width(140)
            .height(40)
            .borderRadius(5)
            .textAlign(TextAlign.Center);
        }
        .width('100%')
        .height(40)
        .backgroundColor($r('app.color.list_window_background')) // 需要替换为开发者所需的颜色资源文件
        .margin({ bottom: 5 });

        Stack() {
          Stack({ alignContent: Alignment.Top }) {
            List({ space: 10 }) {
              ForEach(this.lists, (item: string, index: number) => {
                ListItem() {
                  ObjectBuild({
                    endPosition: this.endPosition,
                    vis: this.vis,
                    item: item,
                    sum: this.sum,
                    img: this.imgs[index],
                    markAnchorY: this.markAnchorY,
                    markAnchorX: this.markAnchorX,
                    imgScale: this.imgScale,
                    marginLeft: this.marginLeft,
                    marginBottom: this.marginBottom
                  });
                };
              }, (item: number) => item.toString());
            }
            .alignListItem(ListItemAlign.Center)
            .width('100%')
            .height('100%');

            Column() {
              Image($rawfile('AddShoppingCart.png')) // 需要替换为开发者所需的图像资源文件
                .width(25)
                .height(25)
                .objectFit(ImageFit.Auto);
            }
            .justifyContent(FlexAlign.Center)
            .alignItems(HorizontalAlign.Center)
            .width(30)
            .height(30)
            .borderRadius(15)
            .backgroundColor($r('app.color.start_window_background')) // 需要替换为开发者所需的颜色资源文件
            .visibility(this.vis)
            .markAnchor({ x: this.markAnchorX, y: this.markAnchorY + 40 })
            .transition({ scale: { x: this.imgScale, y: this.imgScale, z: 0 } })
            .margin({ top: this.marginBottom - this.topRectHeight, left: this.marginLeft });

            Text(`购物车商品数：${this.sum}`)
              .width(140)
              .height(30)
              .borderRadius(5)
              .backgroundColor($r('app.color.start_window_background')) // 需要替换为开发者所需的颜色资源文件
              .margin({ top: 640 })
              .textAlign(TextAlign.Center)
              .id('shoppingCar')
              .onAreaChange((oldValue: Area, newValue: Area) => {
                this.endPosition = {
                  x: Number(newValue.position.x),
                  y: Number(newValue.position.y) + 30
                };
                hilog.info(0x0000, TAG, '结束位置 = ' + JSON.stringify(this.endPosition));
              })
              .shadow({
                radius: 20,
                color: Color.Black,
                offsetX: 0,
                offsetY: 0
              });
          };

        };
      }
      .backgroundColor($r('app.color.start_window_background')) // 需要替换为开发者所需的颜色资源文件
      .height('100%')
      .width('100%');
    }

    async getWindowAvoidArea(context: common.UIAbilityContext): Promise<window.AvoidArea | null> {
      try {
        // The default area of the system includes the status bar and navigation bar
        const mainWindow = await window.getLastWindow(context);
        const avoidAreaType = window.AvoidAreaType.TYPE_SYSTEM;
        const avoidArea = mainWindow.getWindowAvoidArea(avoidAreaType);
        this.topRectHeight = this.getUIContext().px2vp(avoidArea.topRect.height);
        return avoidArea;
      } catch (e) {
        hilog.info(0x0000, TAG, 'getWindowAvoidArea fail');
        return null;
      }
    }
  }

  @Component
  struct ObjectBuild {
    uiContext: UIContext = this.getUIContext?.();
    img: string = '';
    item: string = '';
    @Prop endPosition: Translate;
    @Link vis: Visibility;
    @State isAdd: boolean = false;
    @Link sum: number;
    @Link markAnchorY: number;
    @Link markAnchorX: number;
    objectOffset: componentUtils.Offset = { x: 0, y: 0 };
    @Link imgScale: number;
    @Link marginBottom: number;
    @Link marginLeft: number;
    translates: Translate[] = [];
    @State animatorOptions: AnimatorResult | undefined = undefined;

    // 设置坐标点
    initAnimatorOption() {
      this.translates = [];
      this.translates.push({ x: 0, y: 0 });
      this.translates.push({ x: 0, y: 50 });
      this.translates.push({ x: this.getUIContext().px2vp(this.objectOffset.x) - this.endPosition.x, y: 50 });
      this.translates.push({
        x: this.getUIContext().px2vp(this.objectOffset.x) -
        this.endPosition.x, y: this.getUIContext().px2vp(this.objectOffset.y) - this.endPosition.y - 40
      });
      this.initAnimator();
    }

    build() {
      Row() {
        Stack({ alignContent: Alignment.TopEnd }) {
          Row() {
            Image($rawfile(this.img)) // 需要替换为开发者所需的图像资源文件
              .width(140)
              .height(140)
              .objectFit(ImageFit.Auto)
              .margin({
                top: 10,
                bottom: 10,
                left: 10,
                right: 10
              });
            Column() {
              Text('XXXXXXXXXXXXX')
                .backgroundColor($r('app.color.start_window_background')) // 需要替换为开发者所需的颜色资源文件
                .borderRadius(3)
                .fontSize(16)
                .fontColor('#d9000000')
                .margin({
                  top: 10,
                  bottom: 10,
                  left: 10,
                  right: 10
                });
              Text('XXXX')
                .backgroundColor($r('app.color.start_window_background')) // 需要替换为开发者所需的颜色资源文件
                .borderRadius(3)
                .fontSize(16)
                .fontColor('#d9000000')
                .margin({
                  top: 10,
                  bottom: 10,
                  left: 10,
                  right: 10
                });
              Text('￥：XXXX')
                .fontSize(16)
                .fontColor('#d9000000')
                .margin({
                  top: 0,
                  bottom: 10,
                  left: 90,
                  right: 10
                });
            }
            .justifyContent(FlexAlign.Start)
            .alignItems(HorizontalAlign.Start)
            .height(160)
            .margin({
              top: 10,
              bottom: 10,
              left: 10,
              right: 10
            });
          }.width('100%');

          Stack() {
            Text(this.isAdd ? '已添加购物车' : '添加购物车')
              .height(40)
              .id(this.item);
          }
          .width(120)
          .backgroundColor($r('app.color.start_window_background')) // 需要替换为开发者所需的颜色资源文件
          .borderRadius(10)
          .onClick(() => {
            if (this.isAdd) {
              this.isAdd = false;
              this.sum--;
            } else {
              let componentUtils: ComponentUtils = this.getUIContext().getComponentUtils();
              this.objectOffset = componentUtils.getRectangleById(this.item).screenOffset;
              // 开始动画
              this.vis = Visibility.Visible;
              this.marginBottom = this.getUIContext().px2vp(this.objectOffset.y);
              this.marginLeft = this.getUIContext().px2vp(this.objectOffset.x);
              this.initAnimatorOption();
              this.animatorOptions?.play();
              this.isAdd = true;
              this.sum++;
            }
          })
          .margin({ top: 120, right: 10 });
        };
      }
      .width('95%')
      .backgroundColor($r('app.color.list_window_background')) // 需要替换为开发者所需的颜色资源文件
      .borderRadius(10)
      .justifyContent(FlexAlign.Center)
      .alignItems(VerticalAlign.Center);
    }

    // 初始化动画参数
    initAnimator(): void {
      let animatorOption: AnimatorOptions = {
        duration: 1000,
        delay: 0,
        easing: 'linear',
        iterations: 1,
        fill: 'forwards',
        direction: 'normal',
        begin: 0,
        end: 1
      };
      this.animatorOptions = this.getUIContext().createAnimator(animatorOption);
      this.animatorOptions.onFrame = (progress: number) => {
        let translate: Translate = this.getCurve(progress);
        this.markAnchorX = translate.x;
        this.markAnchorY = translate.y;
      };
      this.animatorOptions.onCancel = () => {
      };
      this.animatorOptions.onFinish = () => {
        this.markAnchorX = 0;
        this.markAnchorY = 0;
        this.imgScale = 1.0;
        this.vis = Visibility.Hidden;
      };
      this.animatorOptions.onRepeat = () => {
        hilog.info(0x0000, TAG, '动画重复播放');
      };
    }

    getCurve(progress: number): Translate {
      let translates: Translate[] = this.translates;
      while (translates.length > 1) {
        let translate2: Translate[] = [];
        for (let i = 0; i < translates.length - 1; i++) {
          let translate: Translate = {
            x: (1 - progress) * translates[i].x + progress * translates[i + 1].x,
            y: (1 - progress) * translates[i].y + progress * translates[i + 1].y
          };
          translate2.push(translate);
        }
        translates = translate2;
      }
      return translates[0];
    }

    onPageHide(): void {
      this.animatorOptions = undefined;
    }
  }
  ```
* **方案二：**

  将组件移动的X轴和Y轴拆分，通过设置不同的动画曲线，来实现整体动画效果上的曲线移动。

  ```ts
  // 设置X方向动画
  generatePositionX(): Array<KeyframeState> {
    let result: Array<KeyframeState> = [];
    result.push({
      duration: 1000,
      curve: Curve.EaseInOut,
      event: () => {
        this.imgScale = 0.8;
        this.markAnchorX = this.getUIContext().px2vp(this.objectOffset.x) - this.endPosition.x;
        hilog.info(0x0000, TAG, 'X');
      }
    });
    return result;
  }

  // 设置Y方向动画
  generatePositionY(): Array<KeyframeState> {
    let result: Array<KeyframeState> = [];
    result.push({
      duration: 10,
      curve: Curve.FastOutLinearIn,
      event: () => {
        hilog.info(0x0000, TAG, ' Y - 1');
      }
    });
    result.push({
      duration: 300,
      curve: Curve.FastOutLinearIn,
      event: () => {
        this.markAnchorY = 50;
        this.imgScale = 0.5;
        hilog.info(0x0000, TAG, ' Y - 1');
      }
    });
    result.push({
      duration: 700,
      curve: Curve.FastOutLinearIn,
      event: () => {
        this.markAnchorY = this.getUIContext().px2vp(this.objectOffset.y) - this.endPosition.y - 40;
        hilog.info(0x0000, TAG, 'Y - 2');
        this.imgScale = 0.1;
      }
    });
    return result;
  }
  ```

  使用两套动画参数同时生成动画。

  ```ts
  let rs = this.generatePositionX();
  let rs2 = this.generatePositionY();
  // 只循环1次,每次的坐标变换由position决定
  this.uiContext.keyframeAnimateTo({ iterations: 1 }, rs);
  this.uiContext.keyframeAnimateTo({
    iterations: 1, onFinish: () => {
      this.markAnchorX = 0;
      this.markAnchorY = 0;
      this.imgScale = 1.0;
      this.vis = Visibility.Hidden;
    }
  }, rs2);
  ```

  完整示例参考如下：

  ```ts
  import { ComponentUtils, componentUtils, window } from '@kit.ArkUI';
  import { common } from '@kit.AbilityKit';
  import { hilog } from '@kit.PerformanceAnalysisKit';

  interface T {
    x: number,
    y: number
  }

  const TAG = 'KeyframeAnimatePage';

  @Entry
  @Component
  struct KeyframeAnimatePage {
    lists: string[] = [];
    shoppingCart: number[] = [];
    imgs: string[] = ['welfare_product_1.png', 'welfare_product_2.png', 'welfare_product_3.png', 'welfare_product_4.png',
      'welfare_product_5.png',
      'welfare_product_6.png', 'welfare_product_7.png', 'welfare_product_8.png']; // 需要替换为开发者所需的图像资源文件
    topRectHeight: number = 0;
    @State endPosition: T | undefined = undefined;
    @State vis: Visibility = Visibility.Hidden;
    @State markAnchorY: number = 0;
    @State markAnchorX: number = 0;
    @State marginBottom: number = 0;
    @State marginLeft: number = 0;
    @State imgScale: number = 1.0;
    @State sum: number = 0;

    // 初始化数据
    aboutToAppear(): void {
      for (let index = 0; index < 8; index++) {
        const element = `第${index}个商品`;
        this.lists.push(element);
        this.shoppingCart.push(0);
      }
      this.getWindowAvoidArea(this.getUIContext().getHostContext() as common.UIAbilityContext);
    }

    build() {
      Column() {
        Column() {
          Text(`商品目录`)
            .width(140)
            .height(40)
            .borderRadius(5)
            .textAlign(TextAlign.Center);
        }
        .width('100%')
        .height(40)
        .backgroundColor($r('app.color.list_window_background')) // 需要替换为开发者所需的颜色资源文件
        .margin({ bottom: 5 });

        Stack() {
          Stack({ alignContent: Alignment.Top }) {
            List({ space: 10 }) {
              ForEach(this.lists, (item: string, index: number) => {
                ListItem() {
                  ObjectBuild({
                    endPosition: this.endPosition,
                    item: item,
                    vis: this.vis,
                    sum: this.sum,
                    img: this.imgs[index],
                    markAnchorY: this.markAnchorY,
                    markAnchorX: this.markAnchorX,
                    imgScale: this.imgScale,
                    marginLeft: this.marginLeft,
                    marginBottom: this.marginBottom
                  });
                };
              }, (item: number) => item.toString());
            }
            .alignListItem(ListItemAlign.Center)
            .width('100%')
            .height('100%');

            Column() {
              Image($rawfile('AddShoppingCart.png')) // 需要替换为开发者所需的图像资源文件
                .width(25)
                .height(25)
                .objectFit(ImageFit.Auto);
            }
            .justifyContent(FlexAlign.Center)
            .alignItems(HorizontalAlign.Center)
            .width(30)
            .height(30)
            .borderRadius(15)
            .backgroundColor($r('app.color.start_window_background')) // 需要替换为开发者所需的颜色资源文件
            .visibility(this.vis)
            .markAnchor({ x: this.markAnchorX, y: this.markAnchorY + 40 })
            .transition({ scale: { x: this.imgScale, y: this.imgScale, z: 0 } })
            .margin({ top: this.marginBottom - this.topRectHeight, left: this.marginLeft });

            Text(`购物车商品数：${this.sum}`)
              .width(140)
              .height(30)
              .borderRadius(5)
              .backgroundColor($r('app.color.start_window_background')) // 需要替换为开发者所需的颜色资源文件
              .margin({ top: 640 })
              .textAlign(TextAlign.Center)
              .id('shoppingCar')
              .onAreaChange((oldValue: Area, newValue: Area) => {
                this.endPosition = {
                  x: Number(newValue.position.x),
                  y: Number(newValue.position.y) + 30
                };
                hilog.info(0x0000, TAG, '结束位置 = ' + JSON.stringify(this.endPosition));
              })
              .shadow({
                radius: 20,
                color: Color.Black,
                offsetX: 0,
                offsetY: 0
              });
          };
        };
      }
      .backgroundColor($r('app.color.start_window_background')) // 需要替换为开发者所需的颜色资源文件
      .height('100%')
      .width('100%');
    }

    async getWindowAvoidArea(context: common.UIAbilityContext): Promise<window.AvoidArea | null> {
      try {
        // The default area of the system includes the status bar and navigation bar
        const mainWindow = await window.getLastWindow(context);
        const avoidAreaType = window.AvoidAreaType.TYPE_SYSTEM;
        const avoidArea = mainWindow.getWindowAvoidArea(avoidAreaType);
        this.topRectHeight = this.getUIContext().px2vp(avoidArea.topRect.height);
        return avoidArea;
      } catch (e) {
        hilog.info(0x0000, TAG, 'getWindowAvoidArea fail');
        return null;
      }
    }
  }

  @Component
  struct ObjectBuild {
    uiContext: UIContext = this.getUIContext?.();
    img: string = '';
    item: string = '';
    @Prop endPosition: T;
    @Link vis: Visibility;
    @State isAdd: boolean = false;
    @Link sum: number;
    @Link markAnchorY: number;
    @Link markAnchorX: number;
    objectOffset: componentUtils.Offset = { x: 0, y: 0 };
    @Link imgScale: number;
    @Link marginBottom: number;
    @Link marginLeft: number;

    build() {
      Row() {
        Stack({ alignContent: Alignment.TopEnd }) {
          Row() {
            Image($rawfile(this.img)) // 需要替换为开发者所需的图像资源文件
              .width(140)
              .height(140)
              .objectFit(ImageFit.Auto)
              .margin({
                top: 10,
                bottom: 10,
                left: 10,
                right: 10
              });
            Column() {
              Text('XXXXXXXXXXXXX')
                .backgroundColor($r('app.color.start_window_background')) // 需要替换为开发者所需的颜色资源文件
                .borderRadius(3)
                .fontSize(16)
                .fontColor('#d9000000')
                .margin({
                  top: 10,
                  bottom: 10,
                  left: 10,
                  right: 10
                });
              Text('XXXX')
                .backgroundColor($r('app.color.start_window_background')) // 需要替换为开发者所需的颜色资源文件
                .borderRadius(3)
                .fontSize(16)
                .fontColor('#d9000000')
                .margin({
                  top: 10,
                  bottom: 10,
                  left: 10,
                  right: 10
                });
              Text('￥：XXXX')
                .fontSize(16)
                .fontColor('#d9000000')
                .margin({
                  top: 0,
                  bottom: 10,
                  left: 90,
                  right: 10
                });
            }
            .justifyContent(FlexAlign.Start)
            .alignItems(HorizontalAlign.Start)
            .height(160)
            .margin({
              top: 10,
              bottom: 10,
              left: 10,
              right: 10
            });
          }.width('100%');

          Stack() {
            Text(this.isAdd ? '已添加购物车' : '添加购物车')
              .height(40)
              .id(this.item);
          }
          .width(120)
          .backgroundColor($r('app.color.start_window_background')) // 需要替换为开发者所需的颜色资源文件
          .borderRadius(10)
          .onClick(() => {
            if (this.isAdd) {
              this.isAdd = false;
              this.sum--;
            } else {
              let componentUtils: ComponentUtils = this.getUIContext().getComponentUtils();
              this.objectOffset = componentUtils.getRectangleById(this.item).screenOffset;
              // 开始动画
              this.vis = Visibility.Visible;
              this.marginBottom = this.getUIContext().px2vp(this.objectOffset.y);
              this.marginLeft = this.getUIContext().px2vp(this.objectOffset.x);
              let rs = this.generatePositionX();
              let rs2 = this.generatePositionY();
              // 只循环1次,每次的坐标变换由position决定
              this.uiContext.keyframeAnimateTo({ iterations: 1 }, rs);
              this.uiContext.keyframeAnimateTo({
                iterations: 1, onFinish: () => {
                  this.markAnchorX = 0;
                  this.markAnchorY = 0;
                  this.imgScale = 1.0;
                  this.vis = Visibility.Hidden;
                }
              }, rs2);
              this.isAdd = true;
              this.sum++;
            }
          })
          .margin({ top: 120, right: 10 });
        };
      }
      .width('95%')
      .backgroundColor($r('app.color.list_window_background')) // 需要替换为开发者所需的颜色资源文件
      .borderRadius(10)
      .justifyContent(FlexAlign.Center)
      .alignItems(VerticalAlign.Center);
    }

    // 设置X方向动画
    generatePositionX(): Array<KeyframeState> {
      let result: Array<KeyframeState> = [];
      result.push({
        duration: 1000,
        curve: Curve.EaseInOut,
        event: () => {
          this.imgScale = 0.8;
          this.markAnchorX = this.getUIContext().px2vp(this.objectOffset.x) - this.endPosition.x;
          hilog.info(0x0000, TAG, 'X');
        }
      });
      return result;
    }

    // 设置Y方向动画
    generatePositionY(): Array<KeyframeState> {
      let result: Array<KeyframeState> = [];
      result.push({
        duration: 10,
        curve: Curve.FastOutLinearIn,
        event: () => {
          hilog.info(0x0000, TAG, ' Y - 1');
        }
      });
      result.push({
        duration: 300,
        curve: Curve.FastOutLinearIn,
        event: () => {
          this.markAnchorY = 50;
          this.imgScale = 0.5;
          hilog.info(0x0000, TAG, ' Y - 1');
        }
      });
      result.push({
        duration: 700,
        curve: Curve.FastOutLinearIn,
        event: () => {
          this.markAnchorY = this.getUIContext().px2vp(this.objectOffset.y) - this.endPosition.y - 40;
          hilog.info(0x0000, TAG, 'Y - 2');
          this.imgScale = 0.1;
        }
      });
      return result;
    }
  }
  ```

方案一和方案二对比：

| 名称 | 实现方式 | 事件响应方式 | 可暂停 | 性能 |
| --- | --- | --- | --- | --- |
| 方案一：帧动画（ohos.animator） | 开发者可每帧修改UI侧属性值，UI侧属性实时更新。 | 实时响应 | 是 | 较差 |
| 方案二：关键帧动画 | UI侧只计算动画最终状态，动画过程中渲染值在改变，UI侧一直为动画最终状态，不感知实时渲染值。 | 按最终状态响应 | 否 | 较好 |
