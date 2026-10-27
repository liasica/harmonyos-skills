---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-uimana-faq-0003
title: ArkUI动画效果实现与控制常见问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 常见问题 > ArkUI动画效果实现与控制常见问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:47:32+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:a1c460bdc9c1250041d1faedfe79dd42bd8abbca9784cc52dfeb6fb4738041a5
---

**Q：如何实现影视类app首页的内容推荐功能？具体演示如下：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/8pwcz4ikScmqFaDyfQFS8w/zh-cn_image_0000002793395103.png "点击放大")

**A**：实现方式如下：

1. 创建ZonesItem数组，用来存储影视的图片数据，自定义SegmentButton组件，用来存储并渲染影视的标题数据。
2. 在ForEach方法中对zonesList进行渲染，并根据当前显示页对图片进行动画效果处理。

完整示例参考如下：

```ts
class ZoneConst {
  static readonly ITEM_WIDTH: number = 70;
  static readonly SHOW_COUNT: number = 3;
  static readonly HALF_COUNT: number = Math.floor(ZoneConst.SHOW_COUNT / 2);
  static readonly OPACITY_COEFFICIENTS: number = 0.1;
  static readonly OFFSET_COEFFICIENTS: number = 10;
  static readonly MAX_OFFSET_X: number = 100;
  static readonly MAX_MOVE_OFFSET: number = 60;
  static readonly SWIPER_DURATION: number = 300;
  static readonly SHADOW_RADIUS: number = 50;
  static readonly SWIPER_ASPECT_RATIO: number = 6 / 4;
}

interface itemButton {
  text: string;
}

class ZonesItem {
  thumbnail: ResourceStr = '';
}

const defaultList: ZonesItem[] = [
  {
    thumbnail: $r('app.media.startIcon'), // 此处仅为样例，请开发者更换为可用图片
  },
  {
    thumbnail: $r('app.media.startIcon'),
  },
  {
    thumbnail: $r('app.media.startIcon'),
  },
];

@Component
struct SegmentButton {
  @Prop buttonOptions: itemButton[] = [{
    text: 'ljx'
  }, {
    text: 'byfx'
  }, {
    text: 'narm'
  }];
  @Link currentIndex: number;
  @State w: number = 0;
  @State h: number = 0;
  @State color: string | Resource = '#272727';
  @State selectColor: string | Resource = '#ffffff';
  @State backColor: string | Resource = '#e1dfe0';
  @Prop offsetX: number = 0;
  private buttonClick = (index: number) => {
    console.info('index:', index);
  };

  @Builder
  overItem() {
    Row()
      .zIndex(1)
      .width(this.w / this.buttonOptions.length)
      .backgroundColor(Color.Red)
      .height('100%')
      .borderRadius(this.h / 2)
      .backgroundColor(this.selectColor)
      .linearGradient({
        angle: 90,
        colors: [['#ff6c8e', 0.0], [' #ff2754', 1.0]]
      })
      .translate({
        x: this.currentIndex * this.w / this.buttonOptions.length + this.offsetX
      })
      .position({
        left: 0,
        top: 0
      });
  }

  // 构建项目
  build() {
    Row() {
      this.overItem();
      ForEach(this.buttonOptions, (item: itemButton, index) => {
        Row({
          space: 10
        }) {
          Text(item.text)
            .fontSize(15)
            .fontColor(this.currentIndex === index ? this.selectColor : this.color);
        }
        .justifyContent(FlexAlign.Center)
        .zIndex(2)
        .width(this.w / this.buttonOptions.length)
        .height('100%')
        .onClick(() => {
          this.buttonClick(index);
          this.getUIContext().animateTo({
            duration: 300
          }, () => {
            this.currentIndex = index;
          });
        });
      }, (item: itemButton) => JSON.stringify(item));
    }
    .onAreaChange((_old, n) => {
      this.w = n.width as number;
      this.h = n.height as number;
    })
    .zIndex(0)
    .borderRadius(30)
    .height(40)
    .width('100%')
    .backgroundColor(this.backColor)
    .clip(true);
  }
}

@Entry
@Component
struct RecommendApp {
  changedIndex: boolean = true;
  zonesList: ZonesItem[] = defaultList;
  @State aheadIndex: number = ZoneConst.HALF_COUNT;
  @State marginBottom: number = 0;
  uiContext: UIContext | undefined = undefined;

  aboutToAppear(): void {
    this.uiContext = this.getUIContext();
  }

  getImgCoefficients(index: number): number {
    let coefficient = this.aheadIndex - index;
    let tempCoefficient = Math.abs(coefficient);
    if (tempCoefficient <= ZoneConst.HALF_COUNT) {
      return coefficient;
    }
    let dataLength = this.zonesList.length;
    let tempOffset = dataLength - tempCoefficient;
    if (tempOffset <= ZoneConst.HALF_COUNT) {
      if (coefficient > 0) {
        return -tempOffset;
      }
      return tempOffset;
    }
    return 0;
  }

  getOffSetX(index: number): number {
    let offsetIndex = this.getImgCoefficients(index);
    let tempOffset = Math.abs(offsetIndex);
    let offsetX = this.marginBottom / (tempOffset + 1);
    if (tempOffset === 1) {
      offsetX += -offsetIndex * ZoneConst.MAX_OFFSET_X;
    } else if (tempOffset === ZoneConst.HALF_COUNT) {
      offsetX += -offsetIndex * (ZoneConst.MAX_OFFSET_X - ZoneConst.OFFSET_COEFFICIENTS);
    }
    return offsetX;
  }

  startAnimation(isUp: boolean): void {
    this.getUIContext().animateTo({
      duration: ZoneConst.SWIPER_DURATION,
    }, () => {
      let dataLength = this.zonesList.length;
      let tempIndex = isUp ? this.aheadIndex + 1 : dataLength + this.aheadIndex - 1;
      this.aheadIndex = tempIndex % dataLength;
      this.marginBottom = 0;
    });
  }

  handlePanGesture(offsetX: number): void {
    if (Math.abs(offsetX) < ZoneConst.MAX_MOVE_OFFSET) {
      this.marginBottom = offsetX;
    } else {
      if (this.changedIndex) {
        return;
      }
      this.changedIndex = true;
      this.startAnimation(offsetX < 0);
    }
  }

  build() {
    Column({
      space: 20
    }) {
      Stack() {
        ForEach(this.zonesList, (item: ZonesItem, index: number) => {
          Row() {
            Image(item.thumbnail)
              .objectFit(ImageFit.Cover)
              .borderRadius(16)
              .shadow({
                radius: 50,
                color: `rgba(0,0,0,0.3)`,
                offsetY: 1
              })
              .opacity(1 - Math.min(ZoneConst.HALF_COUNT,
                Math.abs(this.getImgCoefficients(index))) * ZoneConst.OPACITY_COEFFICIENTS);
          }
          .width(index !== this.aheadIndex && this.getImgCoefficients(index) === 0 ? '10%' : `${ZoneConst.ITEM_WIDTH - ZoneConst.OFFSET_COEFFICIENTS * Math.abs(this.getImgCoefficients(index))}%`)
          .aspectRatio(ZoneConst.SWIPER_ASPECT_RATIO)
          .borderRadius(16)
          .offset({ x: this.getOffSetX(index) })
          .zIndex(index !== this.aheadIndex && this.getImgCoefficients(index) === 0 ?
            0 : ZoneConst.HALF_COUNT - Math.abs(this.getImgCoefficients(index)));
        }, (item: ZonesItem) => JSON.stringify(item));
      }
      .width('100%')
      .alignContent(Alignment.Center)
      .gesture(
        PanGesture({ direction: PanDirection.Horizontal })
          .onActionStart((event: GestureEvent) => {
            this.changedIndex = false;
            this.handlePanGesture(event.offsetX);
          })
          .onActionUpdate((event: GestureEvent) => {
            this.handlePanGesture(event.offsetX);
          })
          .onActionEnd(() => {
            this.getUIContext().animateTo({
              duration: ZoneConst.SWIPER_DURATION,
            }, () => {
              this.marginBottom = 0;
            });
          })
      );

      SegmentButton({
        currentIndex: this.aheadIndex
      });
    }
    .justifyContent(FlexAlign.Start)
    .height('100%')
    .backgroundColor($r('sys.color.point_color_checked'));
  }
}
```

**Q：如何实现图片在当前位置不停地转动，做出加载中的动态效果？**

**A**：通过条件渲染机制触发animateTo动画，实现显示状态的切换。在状态切换过程中，同步执行加载层的淡出动画与内容层的淡入动画，并结合旋转动画，从而实现从加载状态到正式内容展示的平滑过渡。

```ts
@Entry
@Component
struct RotatingLoadPage {
  @State imageAngle: number = 0;
  @State flag: boolean = false;
  @State opacityValue: number = 0;
  @State opacityValueNum: number = 1;

  // 通过生命周期模拟请求数据
  aboutToAppear(): void {
    setTimeout(() => {
      this.getUIContext()?.animateTo({ duration: 1000 }, () => {
        this.flag = true;
        this.opacityValueNum = 0;
        this.opacityValue = 1;
      });
    }, 3000);
  }

  build() {
    Column({ space: 20 }) {
      if (!this.flag) {
        Stack() {
          Image($r('app.media.startIcon')) // 此处'app.media.startIcon'等资源仅作示例，请开发者自行替换。
            .width(200)
            .height(200)
            .borderRadius(1000)
            .rotate({ z: 1, angle: this.imageAngle })
          Text('图片加载中...');
        }
        .opacity(this.opacityValueNum)
        .onAppear(() => {
          this.getUIContext()?.animateTo({ duration: 5000, iterations: -1 }, () => {
            this.imageAngle = 360;
            this.opacityValueNum = 0;
          });
        })
      } else {
        Image($r('app.media.startIcon'))  // 此处'app.media.startIcon'等资源仅作示例，请开发者自行替换。
          .width(200)
          .height(200)
          .borderRadius(1000) // 绑定透明度属性
          .opacity(this.opacityValue)
          .onAppear(() => {
            // 执行透明度渐变动画
            this.getUIContext()?.animateTo({
              duration: 5000, curve: Curve.EaseOut,
              iterations: 1
            }, () => {
              // 从0到1实现淡入效果
              this.opacityValue = 1;
            });
          })
      }
    }
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%')
  }
}
```

运行效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/LYCUtOFsREWNNAoVIhC4HA/zh-cn_image_0000002793395489.png "点击放大")

**Q：如何为组件添加180°镜面翻转的动画效果？**

**A**：实现方案如下：

1. 使用Stack组件进行布局，可以同时设置两个组件内容，但只有一个组件可见，可使页面翻转时交替出现。
2. 设置两个按钮分别用于显示正面和背面，给按钮添加点击事件，在点击事件中使用animateTo方法进行动画过渡。
3. 点击“切换背面”按钮设置rotate为180，zIndex属性值为-1，使其旋转到背面。点击“切换正面”按钮设置rotate为0，zIndex属性值为1，使其旋转到正面。页面旋转交替显示从而实现组件180°镜面翻转效果。

完整示例参考如下：

```ts
@Entry
@Component
struct ReversalIndex {
  @State angle: number = 0;
  @State zIndexNumber: number = 1;
  uiContext: UIContext | undefined = undefined;

  aboutToAppear() {
    this.uiContext = this.getUIContext();
    if (!this.uiContext) {
      console.warn('no uiContext');
      return;
    }
  }

  build() {
    Column({ space: 5 }) {
      Button('切换背面')
        .onClick(() => {
          this.uiContext?.animateTo({ duration: 1000 }, () => {
            // 当动画结束时，将角度设置为180度，并将层级号设置为-1切换到背面
            this.angle = 180;
            this.zIndexNumber = -1;
          });
        });

      Button('切换正面')
        .onClick(() => {
          this.uiContext?.animateTo({ duration: 1000 }, () => {
            // 当动画结束时，将角度设置为0度，并将层级号设置为1切换到正面
            this.angle = 0;
            this.zIndexNumber = 1;
          });
        });

      // 使用Stack布局，可以同时设置两个组件内容，但只有一个组件内容可见
      Stack() {
        Column() {
          Text('背面的内容')
            .fontSize(50);
        }
        .backgroundColor(Color.Pink)
        .width('100%')
        .height('100%')
        .rotate({ y: 2, angle: 180 }); // 设置组件旋转轴向量坐标和旋转角度

        Column() {
          Text('正面的内容')
            .fontSize(50);
        }
        .backgroundColor('#ff709df8')
        .width('100%')
        .height('100%')
        .zIndex(this.zIndexNumber); // 根据zIndexNumber设置层级
      }
      .layoutWeight(1) // 设置布局权重为1
      .rotate({ y: 2, angle: this.angle, perspective: 200 }); // 设置组件旋转轴向量坐标和旋转角度

    }
    .height('100%')
    .width('100%');
  }
}
```

效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/WrHGyJK7SHykfxNaEgwq0Q/zh-cn_image_0000002763997146.png "点击放大")

**Q：图片可以进行镜面翻转吗？**

**A**：请参考[使用PixelMap完成图像变换](../harmonyos-guides/image-transformation.md#示例代码)。

**Q：如何给点击事件添加动画效果，以提升用户的使用体验？**

**A**：实现步骤如下：

1. 创建Stack父组件，在其中定义Text文本和Progress进度条组件，实现基本样式效果。
2. 在Progress组件中实现onTouch方法，根据事件类型（Down或Up）调整文本字体大小、按钮尺寸和进度条长度等样式属性，并通过keyframeAnimateTo定义相应的关键帧动画。

   ```ts
   @Entry
   @Component
   struct ClickAnimationPage {
     length: number = 60;
     @State nLength: number = 60;
     @State fontSizeInfoClick: number = 10;
     @State fontSizeInfoPerformance: number = 15;
     @State valueInfo: number = 0;
     @State count: number = 1;
     @State fontSizeInfoProgress: number = 18;
     uiContext: UIContext | undefined = undefined;

     aboutToAppear(): void {
       this.uiContext = this.getUIContext?.();
     }

     onPageShow(): void {
       this.length = 60;
       setTimeout(() => {
         this.length = 70;
       }, 50);
     }

     build() {
       Column() {
         Row() {
           Text('X')
             .fontColor(Color.Black).fontWeight(700).fontSize(13);
           Text(this.count.toString())
             .fontColor(Color.Black).fontWeight(700).fontSize(this.fontSizeInfoProgress);
         };
         Stack() {
           Column() {
             Text('点击').fontSize(this.fontSizeInfoPerformance).fontColor(Color.White);
           }
           .opacity(0.8)
           .width(this.nLength)
           .height(this.nLength)
           .borderRadius(this.nLength / 2)
           .backgroundColor(Color.Orange)
           .justifyContent(FlexAlign.Center);
           Column() {
             Progress({ value: this.valueInfo, total: 100, type: ProgressType.Ring })
               .width(this.nLength)
               .height(this.nLength)
               .color(Color.Blue)
               .style({ strokeWidth: 5 })
               .onTouch((event: TouchEvent) => {
                 if (TouchType.Up === event.type) {
                   // 用户可在这自定义实现动画效果
                   this.nLength = 60;
                   this.fontSizeInfoClick = 10;
                   this.fontSizeInfoPerformance = 15;
                   this.fontSizeInfoProgress = 15;
                   this.valueInfo = 0;
                   if (!this.uiContext) {
                     return;
                   }
                   this.uiContext.keyframeAnimateTo({ iterations: 3 }, [
                     {
                       duration: 100, event: () => {
                       this.valueInfo = 0;
                     }
                     },
                     {
                       duration: 100, event: () => {
                       this.valueInfo = 100;
                     }
                     }
                   ]);
                 }
                 if (TouchType.Down === event.type) {
                   // 用户可在这自定义实现动画效果
                   this.nLength = 50;
                   this.fontSizeInfoClick = 7;
                   this.fontSizeInfoPerformance = 10;
                   this.fontSizeInfoProgress = 18;
                   this.valueInfo = 0;
                   ++this.count;
                   if (!this.uiContext) {
                     return;
                   }
                   this.uiContext.keyframeAnimateTo({ iterations: 3 }, [
                     {
                       duration: 100, event: () => {
                       this.valueInfo = 0;
                     }
                     },
                     {
                       duration: 100, event: () => {
                       this.valueInfo = 100;
                     }
                     }
                   ]);
                 }
               });
           }
           .width(60)
           .height(60)
           .justifyContent(FlexAlign.Center);
         };
       }
       .justifyContent(FlexAlign.Center)
       .alignItems(HorizontalAlign.Center)
       .width('100%')
       .height('100%');
     }
   }
   ```

**Q：当组件在动画执行过程中，对组件当前显示位置进行点击操作，无法触发onClick事件，唯有当动画结束、组件停止在最终位置后，该组件的点击操作才可正常响应。如何在动画执行过程中使组件能正确响应onClick事件？**

```ts
@Entry
@Component
struct Problem {
  @State title: string = '点击更新时间参数：';
  @State x: number = 0;

  startAnimation() {
    this.getUIContext().animateTo({ duration: 5000, playMode: PlayMode.Normal }, () => {
      this.x = 100;
    });
  }

  build() {
    Stack() {
      Text(this.title)
        .fontSize(18)
        .position({ x: this.x, y: 40 })
        .animation({
          duration: 5000,
          curve: Curve.Linear,
          playMode: PlayMode.Normal
        })
        .onClick(() => {
          this.title = '点击更新时间参数：' + new Date().getTime();
        })
        .onAppear(() => {
          this.startAnimation();
        });
    }
    .height(100)
    .width('100%');
  }
}
```

**A**：解决方法如下：

1. 由于显式动画的特性，目标对象在动画执行期间所处的位置仅在动画结束时被识别和记录。当用户在动画播放过程中尝试点击该对象时，点击事件无法被正确识别和响应。
2. 为了解决这一问题，可以采用帧动画的方式来实现，帧动画通过逐帧定义对象的状态，系统会在每一帧更新对象的位置和状态，并据此响应用户交互事件。完整示例代码参考如下：

   ```ts
   import { AnimatorResult } from '@kit.ArkUI';

   @Entry
   @Component
   struct SolutionOne {
     @State title: string = '点击更新时间参数：';
     @State x: number = 0;
     private backAnimator: AnimatorResult = this.getUIContext().createAnimator({
       duration: 5000,
       easing: 'ease',
       delay: 0,
       fill: 'forwards',
       direction: 'normal',
       iterations: -1,
       begin: 0,
       end: 100
     });

     build() {
       Stack() {
         Text(this.title)
           .fontSize(18)
           .position({ x: this.x, y: 40 })
           .onClick(() => {
             this.title = '点击更新时间参数：' + new Date().getTime();
           })
           .onAppear(() => {
             this.backAnimator.play();
             this.backAnimator.onFrame = (value: number) => {
               this.x = value;
             };
           });
       }
       .height(100)
       .width('100%');
     }
   }
   ```

**Q：动画可以使应用界面过渡自然流畅，并且增强用户从界面获得的反馈感和互动感。如何实现组件的水波纹效果？**

**A**：实现组件的水波纹效果有以下两种方案：

* 方案一：点击后实现波纹动效。通过onClick回调获取手指点击的位置用于为圆形组件的位置赋值，然后通过组件内转场实现圆形出现并逐渐透明的效果。

  ```ts
  @Entry
  @Component
  struct WaterPageDemo {
    @State flag: boolean = false;
    @State ballX: number = 0;
    @State ballY: number = 0;
    build() {
      Column() {
        Column() {
        }.layoutWeight(1).backgroundColor(Color.Pink).width('100%');

        Stack() {
          // 根据flag判断是否显示动画效果
          if (this.flag) {
            Row()
              .width(5)
              .height(5)
              .position({
                x: this.ballX,
                y: this.ballY
              })
              .backgroundColor('rgba(0,0,0,0.7)')
              // 组件转场动画
              .transition(TransitionEffect.asymmetric(
                TransitionEffect.IDENTITY,
                TransitionEffect.OPACITY.animation({ duration: 1000, curve: Curve.EaseInOut }).combine(
                  TransitionEffect.scale({ x: 100, y: 100 })
                )
              ))
              .borderRadius(15)
          }
        }.width('100%').height('100%').clip(true)
        .onClick((e) => {
          this.ballX = e.x - 3;
          this.ballY = e.y - 3;
          this.flag = !this.flag;
          // 延时改变状态变量
          setTimeout(() => {
            this.flag = !this.flag;
          }, 100);
        });
      }
      .width('100%')
      .height('100%')
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/7WMgi4x0Qf6nBnjJWVtOEg/zh-cn_image_0000002793480175.png "点击放大")
* 方案二：控件自主产生动效。

  ```ts
  @Entry
  @Component
  struct WaterPageDemo2 {
    private settings: RenderingContextSettings = new RenderingContextSettings(true);
    private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
    waveSpeed: number = 0.03;
    phase: number = 0;
    // 绘制波纹动效
    drawWave() {
      this.context?.clearRect(0, 0, this.context.width, this.context.height); // 清除画布上在该矩形区域内的内容
      this.context?.beginPath();  // 开始创建路径
      for (let x = 0; x <= this.context.width; x += 10) {
        const y = this.context.height / 2 + Math.sin(x * 0.01 + this.phase) * 20;
        this.context?.lineTo(x, y); // 连接路径点
      }
      this.context?.lineTo(this.context.width, this.context.height);
      this.context?.lineTo(0, this.context.height);
      this.context?.closePath();    // 关闭一个路径
      this.context.fillStyle = '#30007bff'; // 设置填充色
      this.context?.fill();
      this.context?.beginPath();
      for (let x = 0; x <= this.context.width; x += 10) {
        const y = this.context.height / 2 + Math.sin(x * 0.02 + this.phase) * 10;
        this.context?.lineTo(x, y);
      }
      this.context?.lineTo(this.context.width, this.context.height);
      this.context?.lineTo(0, this.context.height);
      this.context?.closePath();
      this.context.fillStyle = '#50007bff';
      this.context?.fill();
      this.context?.beginPath();
      for (let x = 0; x <= this.context.width; x += 10) {
        const y = this.context.height / 2 + Math.sin(x * 0.015 + this.phase) * 30;
        this.context?.lineTo(x, y);
      }
      this.context?.lineTo(this.context.width, this.context.height);
      this.context?.lineTo(0, this.context.height);
      this.context?.closePath();
      this.context.fillStyle = '#20007bff';
      this.context?.fill();
      this.phase += this.waveSpeed;
    }

    build() {
      Column() {
        Canvas(this.context)
          .width(200)
          .height(100)
          .backgroundColor(Color.Pink)
          // Canvas初始化完成回调
          .onReady(() => {
            setInterval(this.drawWave.bind(this), 20);
          })
      }.width('100%').height('100%').justifyContent(FlexAlign.Center)
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/4_7zxSIJSY-2HAUDu4snKA/zh-cn_image_0000002793480829.png "点击放大")

**Q：在HarmonyOS系统中，如何实现红包雨的动画效果呢？**

**A**：实现红包雨动画效果的步骤如下：

1. 创建RedPacketModel类，添加属性用于设置红包的位置，添加getRandomNumber方法用于设置红包出现的间隔。

   ```ts
   @Observed
   class RedPacketModel {
     x: number = 0;
     y: number = -90;
     imageWidth: number = 0;
     delay: number = 0;

     constructor(index: number, imageWidth: number, delay?: number,) {
       this.x = 10 + (imageWidth) * (index - 1) + 10 * index;
       if (delay) {
         this.delay = delay * 1000;
       }
     }

     static getRandomNumber(min: number, max: number) {
       let rand = cryptoFramework.createRandom();
       // 设置生成随机数的字节长度为1
       let randData = rand.generateRandomSync(1);
       // 自定义范围(0-10之内)
       let numRan: number = Math.fround(randData.data[0] * 10 / 2550);
       let num = Math.floor(numRan * (max - min + 1)) + min;
       return num;
     }
   }
   ```
2. 定义RedPacket组件，使用AnimatorOptions设置动画的参数，并通过create方法创建动画，并在animatorResult的onFrame回调方法中设置红包的纵坐标。

   ```ts
   // 创建一个帧动画
       this.animatorResult = this.getUIContext().createAnimator(animatorOption);
       // 接收帧回调，并设置红包的纵坐标
       this.animatorResult.onFrame = (progress: number) => {
         this.model.y = progress;
       };
   ```
3. 在父组件RedPacketRain中创建RedPacketModel并通过ForEach循环渲染即可。

   ```ts
   ForEach(this.redPacketModels, (model: RedPacketModel) => {
           RedPacket({
             model: model,
             imageWidth: this.imageWidth
           });
         });
   ```

   完整示例参考如下：

   ```ts
   import { AnimatorOptions } from '@ohos.animator';
   import { AnimatorResult, window } from '@kit.ArkUI';
   import cryptoFramework from '@ohos.security.cryptoFramework';
   @Observed
   class RedPacketModel {
     x: number = 0;
     y: number = -90;
     imageWidth: number = 0;
     delay: number = 0;

     constructor(index: number, imageWidth: number, delay?: number,) {
       this.x = 10 + (imageWidth) * (index - 1) + 10 * index;
       if (delay) {
         this.delay = delay * 1000;
       }
     }

     static getRandomNumber(min: number, max: number) {
       let rand = cryptoFramework.createRandom();
       // 设置生成随机数的字节长度为1
       let randData = rand.generateRandomSync(1);
       // 自定义范围(0-10之内)
       let numRan: number = Math.fround(randData.data[0] * 10 / 2550);
       let num = Math.floor(numRan * (max - min + 1)) + min;
       return num;
     }
   }
   @Component
   struct RedPacket {
     @ObjectLink model: RedPacketModel;
     @Link imageWidth: number;
     animatorResult: AnimatorResult | undefined = undefined;

     aboutToAppear(): void {

       let animatorOption: AnimatorOptions = {
         duration: 2000 + (RedPacketModel.getRandomNumber(0, 255) % 250 / 100) * 1000,
         delay: this.model.delay,
         easing: 'linear',
         iterations: 1,
         fill: 'forwards',
         direction: 'normal',
         begin: -90,
         end: 840
       };
       // 创建一个帧动画
       this.animatorResult = this.getUIContext().createAnimator(animatorOption);
       // 接收帧回调，并设置红包的纵坐标
       this.animatorResult.onFrame = (progress: number) => {
         this.model.y = progress;
       };
     }

     build() {
       Stack() {
         Image($r('app.media.startIcon')); // 此处仅为样例，请开发者更换为可用图片
       }
       .width(this.imageWidth)
       .height(this.imageWidth)
       .position({ x: this.model.x, y: this.model.y })
       .onAppear(() => {
         this.animatorResult?.play();
       });
     }
   }

   @Entry
   @Component
   struct RedPacketRain {
     @State redPacketModels: RedPacketModel[] = [];
     @State imageWidth: number = 0;

     aboutToAppear(): void {
       window.getLastWindow(this.getUIContext().getHostContext()).then((data) => {
         let properties = data?.getWindowProperties();
         let w = this.getUIContext().px2vp(properties.windowRect.width);
         this.imageWidth = (w - 12 * 4) / 4.0;
         for (let index = 0; index < 30; index++) {
           this.redPacketModels.push(new RedPacketModel(1, this.imageWidth, index));
           this.redPacketModels.push(new RedPacketModel(2, this.imageWidth, index));
           this.redPacketModels.push(new RedPacketModel(3, this.imageWidth, index));
           this.redPacketModels.push(new RedPacketModel(4, this.imageWidth, index));
         }
       });
     }

     build() {
       Stack() {
         ForEach(this.redPacketModels, (model: RedPacketModel) => {
           RedPacket({
             model: model,
             imageWidth: this.imageWidth
           });
         });
       }
       .height('100%')
       .width('100%')
       .clip(true);
     }
   }
   ```

**Q：如何实现多张图片组成动画组，并实现其向右循环移动的效果？**

**A**：实现方式如下：

1. 使用Repeat组件对图片进行循环渲染，构建统一的排列结构，以便集中控制布局与动画。
2. 借助Animator逐步更新offsetX属性，以此驱动图片产生横向位移的动画效果。
3. 将offsetX的变化值绑定至translate属性，最终呈现多图片向右循环移动的视觉效果。

   ```ts
   import { AnimatorResult } from '@kit.ArkUI';

   @Entry
   @ComponentV2
   export struct MovingAnimationDemo {
     // 循环播放图片资源
     @Local playAnimation: Resource[][] = [
       [
         $r('app.media.startIcon'), // 此处仅为示例，请开发者自行替换为可用图片
         $r('app.media.startIcon'),
         $r('app.media.startIcon'),
         $r('app.media.startIcon')
       ],
       [
         $r('app.media.startIcon'),
         $r('app.media.startIcon'),
         $r('app.media.startIcon'),
         $r('app.media.startIcon')
       ],
       [
         $r('app.media.startIcon'),
         $r('app.media.startIcon'),
         $r('app.media.startIcon'),
         $r('app.media.startIcon')
       ]
     ];
     backAnimator?: AnimatorResult;
     // 动画偏移量
     @Local offsetX: number = -120;
     @Local isPlaying: boolean = false;

     @Monitor('isPlaying')
     onChangeIsPlaying(monitor: IMonitor) {
       monitor.dirty.forEach((path: string) => {
         if (path === 'isPlaying') {
           if (this.isPlaying) {
             this.backAnimator?.play();
           } else {
             this.backAnimator?.pause();
           }
         }
       });
     }

     aboutToAppear() {
       this.backAnimator = this.getUIContext().createAnimator({
         duration: 5000,
         easing: 'liner',
         delay: 0,
         fill: 'both',
         direction: 'normal',
         iterations: -1,
         begin: 0,
         end: 120
       });
       // 在5s内，逐步改变offsetX的值
       this.backAnimator.onFrame = (value: number) => {
         this.offsetX = -120 + value;
       };
     }

     build() {
       Column({ space: 15 }) {
         Text('实现向右循环移动动画效果');
         Row() {
           Row({ space: 5 }) {
             Repeat(this.playAnimation).each(ri => {
               Row({ space: 5 }) {
                 Repeat(ri.item).each(ri2 => {
                   Image(ri2.item)
                     .height(25)
                     .width(25);
                 });
               };
             });
           }
           .translate({ x: this.offsetX })
           .layoutWeight(1);
         }
         .backgroundColor(Color.Gray)
         .width(160)
         .clip(true);

         Button(this.isPlaying ? '暂停' : '播放')
           .width(60)
           .height(40)
           .onClick(() => {
             this.isPlaying = !this.isPlaying;
           });
       }
       .width('100%');
     }
   }
   ```

**Q：如何实现直播间欢迎词的进场动画，使其从左至右移动并逐渐淡出？**

**A**：实现方式如下：

1. 定义变量op以管理欢迎词的显示状态。监听按钮的点击事件，触发animateTo动画，实现欢迎词的入场效果。
2. 利用onFinish回调函数，在入场动画结束后调用animateTo方法，执行隐藏动画，从而实现欢迎词的自动消失效果。

   ```ts
   @Entry
   @Component
   struct LiveBroadcastDemo {
     message: string = 'xxx进入了直播间';
     @State markX: number | string = '100%';
     @State op: number = 1; // 显示状态

     build() {
       Column() {
         Button('点击进入直播间')
           .margin({ top: 60 })
           .onClick(() => {
             this.getUIContext().animateTo({
               delay: 0,
               duration: 500,
               onFinish: () => {
                 this.getUIContext().animateTo({
                   delay: 3000,
                   duration: 800
                 }, () => {
                   this.op = 0;
                 });
               }
             }, () => {
               this.markX = 0;
             });
           });
         if (this.op !== 0) {
           Text(this.message)
             .fontSize(30)
             .fontWeight(FontWeight.Bold)
             .backgroundColor(Color.Pink)
             .borderRadius(3)
             .markAnchor({ x: this.markX })
             .position({ x: 0 })
             .opacity(this.op);
         }
       }
       .width('100%')
       .height('100%');
     }
   }
   ```

**Q：组件当前绑定了一个转场动画transitionEffect，能否在运行时动态切换为另一种转场动画？**

**A**：实现方式如下：

1. 自定义两种不同的transitionEffect转场效果。
2. 声明并初始化transitionEffect实例，通过transition接口将其应用到目标组件。
3. 在组件的动态添加或移除过程中，通过animation接口配置动画参数，从而为组件应用不同的转场动画效果。

   ```ts
   import { curves } from '@kit.ArkUI';

   @Entry
   @Component
   struct TransitionEffectDemo {
     @State isPresent: boolean = false;
     // 创建transitionEffect
     private effect1: TransitionEffect =
       // 创建默认透明度转场效果，并指定了springMotion(0.6, 0.8)曲线
       TransitionEffect.OPACITY.animation({
         curve: curves.springMotion(0.6, 0.8)
       })
         .combine(TransitionEffect.scale({
           x: 0,
           y: 0
         }))// 添加旋转转场效果，这里的动画参数会跟随上面带animation的TransitionEffect，也就是springMotion(0.6, 0.8)
         .combine(TransitionEffect.rotate({ angle: -90 }))// 添加平移转场效果，这里的动画参数使用指定的springMotion()
         .combine(TransitionEffect.translate({ y: 150 })
           .animation({ curve: curves.springMotion() }))// 添加move转场效果，这里的动画参数会跟随上面的TransitionEffect，也就是springMotion()
         .combine(TransitionEffect.move(TransitionEdge.START));
     private effect2: TransitionEffect =
       TransitionEffect.OPACITY.animation({
         curve: curves.springMotion(0.6, 0.8)
       })
         .combine(TransitionEffect.scale({
           x: 0,
           y: 0
         }))
         .combine(TransitionEffect.rotate({ angle: 90 }))
         .combine(TransitionEffect.translate({ y: 150 })
           .animation({ curve: curves.springMotion() }))
         .combine(TransitionEffect.move(TransitionEdge.END));
     effect: TransitionEffect | null = null;

     build() {
       Stack() {
         if (this.isPresent) {
           Column() {
             Text('ArkUI')
               .fontWeight(FontWeight.Bold)
               .fontSize(20)
               .fontColor(Color.White);
           }
           .justifyContent(FlexAlign.Center)
           .width(150)
           .height(150)
           .borderRadius(10)
           .backgroundColor(0xf56c6c)
           // 将转场效果通过transition接口设置到组件
           .transition(this.effect);
         }
         Column()
           .width(155)
           .height(155)
           .border({
             width: 5,
             radius: 10,
             color: Color.Black
           });
         // 触发转场
         Column({ space: 10 }) {
           Button('从左侧入场')
             .onClick(() => {
               this.effect = this.effect1;
               this.isPresent = !this.isPresent;
             });
           Button('从右侧入场')
             .onClick(() => {
               this.effect = this.effect2;
               this.isPresent = !this.isPresent;
             });
         }
         .margin({ top: 320 });
       }
       .width('100%')
       .height('60%');
     }
   }
   ```

**Q：如何实现下图的点击'+'号展示导航栏，点击'X'号关闭导航栏的效果？**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/IFdofBhITKictz2KR61jyw/zh-cn_image_0000002793403439.png)

**A**：通过animateTo方法实现全局的显示动画效果，结合其他属性实现动画过程中水滴融合、组件位移以及透明度变化等视觉效果。

1. 采用Stack布局方式，利用Column组件创建四个圆形元素，并通过Image组件创建四张图片，将每对圆形和图片进行组合。
2. 使用@State装饰器定义状态变量，以动态追踪并响应组件尺寸、透明度以及沿Y轴的位移translate等属性的变化。
3. 在onClick方法中，通过设置并判断flag标记的布尔值，调用animateTo方法设置组件的动画属性。当flag为true时，所有组件沿Y轴方向根据各自的移动距离进行位置缩减，并以层叠的方式完成动画；当flag为false时，所有组件沿Y轴方向以固定的位移距离向外分散，形成扩散的动画效果。通过该逻辑切换两种状态，最终实现类似水滴融合与分离的动态交互效果。

   ```ts
   import { uiEffect } from '@kit.ArkGraphics2D';

   @Entry
   @Component
   struct HoverButtonExample {
     @State flag: boolean = true;
     @State opacityValue: number = 0;
     @State BY1: number = 0;
     @State BY2: number = 0;
     @State BY3: number = 0;
     @State BY4: number = 0;
     @State angle: number = 0;
     @State widthBottom: number = 80;
     @State backMove: number = 0;
     @State backHeight: number = 50;
     @State backWidth: number = 60;
     distance: number = 70;
     private filterTest1: uiEffect.Filter = uiEffect.createFilter().blur(20);

     build() {
       Column() {
         Stack() {
           Column() {
           }
           .width(this.widthBottom)
           .height(this.widthBottom)
           .borderRadius(this.widthBottom / 2)
           .backgroundColor('#000')
           .foregroundFilter(this.filterTest1)
           .translate({ y: this.BY1 });

           Column() {
           }
           .width(60)
           .height(60)
           .translate({ y: this.BY2 })
           .foregroundFilter(this.filterTest1)
           .backgroundColor('#000')
           .borderRadius(30);

           Column() {
           }
           .width(60)
           .height(60)
           .translate({ y: this.BY3 })
           .foregroundFilter(this.filterTest1)
           .backgroundColor('#000')
           .borderRadius(30);

           Column() {
           }
           .width(60)
           .height(60)
           .translate({ y: this.BY4 })
           .foregroundFilter(this.filterTest1)
           .backgroundColor('#000')
           .borderRadius(30);

           Image($r('app.media.add')) // 此处'app.media.add'仅作示例，请开发者自行替换，否则image创建失败会导致后续无法正常执行
             .width(20)
             .height(20)
             .rotate({ angle: this.angle })
             .zIndex(7);
           Image($r('app.media.pan')) // 此处'app.media.pan'仅作示例，请开发者自行替换，否则image创建失败会导致后续无法正常执行
             .width(20)
             .height(20)
             .opacity(this.opacityValue)
             .zIndex(8)
             .translate({ y: this.BY2 });
           Image($r('app.media.local')) // 此处'app.media.local'仅作示例，请开发者自行替换，否则image创建失败会导致后续无法正常执行
             .width(20)
             .height(20)
             .opacity(this.opacityValue)
             .zIndex(9)
             .translate({ y: this.BY3 });
           Image($r('app.media.trash')) // 此处'app.media.trash'仅作示例，请开发者自行替换，否则image创建失败会导致后续无法正常执行
             .width(20)
             .height(20)
             .opacity(this.opacityValue)
             .zIndex(10)
             .translate({ y: this.BY4 });
         }
         .width(100)
         .height('100%')
         .contrast(20)
         .padding(16)
         .onClick(() => {
           if (this.flag) {
             this.getUIContext()?.animateTo({ curve: Curve.Friction, duration: 2000 }, () => {
               this.backMove = this.distance * 3 / 2;
               this.backHeight += this.distance * 3;
               this.backWidth = 0;
               this.widthBottom = 60;
               this.angle = 45;
               this.BY2 = this.BY2 - this.distance;
               this.BY3 = this.BY3 - this.distance * 2;
               this.BY4 = this.BY4 - this.distance * 3;
               this.flag = !this.flag;
               this.opacityValue = 1;
             });
           } else {
             this.getUIContext()?.animateTo({ curve: Curve.Friction, duration: 2000 }, () => {
               this.backMove = this.backMove - this.distance * 3 / 2;
               this.backHeight -= this.distance * 3;
               this.backWidth = 60;
               this.widthBottom = 80;
               this.angle = 0;
               this.BY2 = this.BY2 + this.distance;
               this.BY3 = this.BY3 + this.distance * 2;
               this.BY4 = this.BY4 + this.distance * 3;
               this.flag = !this.flag;
               this.opacityValue = 0;
             });
             setTimeout(() => {
               this.getUIContext()?.animateTo({ curve: Curve.Friction, duration: 1000 }, () => {
                 this.BY1 = 10;
               });
             }, 1000);
             setTimeout(() => {
               this.getUIContext()?.animateTo({ curve: Curve.Friction, duration: 1000 }, () => {
                 this.BY1 = 0;
               });
             }, 1500);
           }
         });
       }
       .justifyContent(FlexAlign.Center)
       .width('100%')
       .height('100%');
     }
   }
   ```

   效果图：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/IHDXRZnATnqKVkDVH8IqUg/zh-cn_image_0000002793406387.png "点击放大")。

**Q：如何实现播放中的动画暂停的功能？**

**A**：方案一：通过[lottie](https://gitcode.com/openharmony-tpc/lottieArkTS)动画三方库来实现动画播放暂停，详情参考：lottie[使用示例](https://gitcode.com/openharmony-tpc/lottieArkTS#使用示例)。

方案二：可以使用[@ohos.animator(动画)](../harmonyos-references/js-apis-animator.md)的[play](../harmonyos-references/js-apis-animator.md#play)，[pause](../harmonyos-references/js-apis-animator.md#pause)等相关方法来实现动画播放和暂停。具体代码见官网示例：[基于ArkTS扩展的声明式开发范式](../harmonyos-references/js-apis-animator.md#基于arkts扩展的声明式开发范式)。

方案三：API20提供了属性动画启停功能，详情请参考：[动画创建与取消示例](../harmonyos-references/js-apis-arkui-framenode.md#动画创建与取消示例)。

方案四：使用setInterval结合显式动画实现。

1. 设置状态变量angle用于控制图像的旋转角度。
2. 设置状态变量displaying用于控制动画的播放与暂停。
3. 使用setInterval和clearInterval来控制动画的播放。当点击播放按钮时，执行animateTo动画，修改图片的旋转角度。设置定时器延迟间隔和动画时长相同，实现平滑过渡。点击停止播放按钮时，关闭定时器，保持当前的旋转角度。

完整示例参考如下：

```ts
@Entry
@Component
struct PageOne {
  @State angle: number = 0;
  @State displaying: boolean = false;
  timer: number | null = null;
  duration: number = 400;
  uiContext: UIContext | undefined = undefined;

  aboutToAppear() {
    this.uiContext = this.getUIContext();
  }

  build() {
    Stack() {
      Image($r('app.media.ship'))
        .width(200)
        .height(200)
        .borderRadius(100)
        .backgroundColor(Color.Blue)
        .rotate({ angle: this.angle });

      Text(this.displaying ? '❚❚' : '▶')
        .fontColor(Color.White)
        .fontSize(30)
        .onClick(() => {
          this.displaying = !this.displaying;
          if (this.displaying) {
            this.timer = setInterval(() => {
              this.uiContext?.animateTo({
                duration: this.duration,
                iterations: 1,
                curve: Curve.Linear
              }, () => {
                this.angle += 50;
              });
            }, this.duration);
          } else {
            clearInterval(this.timer);
          }
        });
    }
    .alignContent(Alignment.Center)
    .width('100%')
    .height('100%');
  }
}
```

注意：此方案点击暂停时动画不会立即停止，而会等当前的动画执行完毕，可能会存在体验问题。

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/G1A98RZtQICYgiQPO1pZWQ/zh-cn_image_0000002793407685.png "点击放大")

方案五：控制多个动画的播放和暂停。实现方法与方案三类似，区别在于当使用setInterval方法播放一个动画时，用clearInterval方法清除掉另外一个动画。

具体代码如下：

```ts
@Entry
@Component
struct PageTwo {
  @State angleOne: number = 0;
  @State angleTwo: number = 0;
  timerOne: number | null = null;
  timerTwo: number | null = null;
  duration: number = 400;
  uiContext: UIContext | undefined = undefined;

  aboutToAppear() {
    this.uiContext = this.getUIContext();
  }

  build() {
    Column({ space: 20 }) {
      Text('动画A：');
      Image($r('app.media.ship')) // 根据具体情况引用资源
        .width(200)
        .height(200)
        .borderRadius(100)
        .backgroundColor(Color.Blue)
        .rotate({ angle: this.angleOne });
      Text('动画B：');
      Image($r('app.media.ship')) // 根据具体情况引用资源
        .width(200)
        .height(200)
        .borderRadius(100)
        .backgroundColor(Color.Blue)
        .rotate({ angle: this.angleTwo });

      Button('播放A，暂停B')
        .fontColor(Color.White)
        .backgroundColor('0A59F7')
        .onClick(() => {
          clearInterval(this.timerOne);
          clearInterval(this.timerTwo);
          this.timerOne = setInterval(() => {
            this.uiContext?.animateTo({
              duration: this.duration,
              iterations: 1,
              curve: Curve.Linear
            }, () => {
              this.angleOne += 50;
            });
          }, this.duration);
        });

      Button('播放B，暂停A')
        .fontColor(Color.White)
        .backgroundColor('0A59F7')
        .onClick(() => {
          clearInterval(this.timerTwo);
          clearInterval(this.timerOne);
          this.timerTwo = setInterval(() => {
            this.uiContext?.animateTo({
              duration: this.duration,
              iterations: 1,
              curve: Curve.Linear
            }, () => {
              this.angleTwo += 50;
            });
          }, this.duration);
        });
    }
    .position({
      left: 90
    });
  }
}
```

具体演示如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/TvpGQ7n6T3eyG_mPFuW-iw/zh-cn_image_0000002764009188.png "点击放大")

方案六：在显式动画、关键帧动画中新增一个duration为0的动画，即可停止该状态变量所关联**属性的**之前的所有动画，并停止在最终设置的状态变量所对应的状态上。

具体代码如下：

```ts
@Entry
@Component
struct PageThree {
  @State angle: number = 0;
  @State displaying: boolean = false;
  timer: number | null = null;
  duration: number = 4000;
  uiContext: UIContext | undefined = undefined;

  aboutToAppear() {
    this.uiContext = this.getUIContext();
  }

  build() {
    Stack() {
      Image($r('app.media.ship'))
        .width(200)
        .height(200)
        .borderRadius(100)
        .backgroundColor(Color.Blue)
        .rotate({ angle: this.angle });

      Text(this.displaying ? '❚❚' : '▶')
        .fontColor(Color.White)
        .fontSize(30)
        .onClick(() => {
          this.displaying = !this.displaying;
          if (this.displaying) {
            this.uiContext?.animateTo({
              duration: this.duration,
              iterations: 1,
              curve: Curve.Linear,
            }, () => {
              this.angle += 360;
            });
          } else {
            // 启动一个duration为0的动画
            this.uiContext?.animateTo({
              duration: 0,
              iterations: 1,
              curve: Curve.Linear,
            }, () => {
              this.angle = 0;
            });
          }
        });
    }
    .alignContent(Alignment.Center)
    .width('100%')
    .height('100%');
  }
}
```

**Q：能否在组件的aboutToAppear中调用animateTo动画？**

**A**：不建议在aboutToAppear中调用动画，自定义组件内的build还未执行，内部组件还未创建，动画时机过早，动画属性没有初值无法对组件产生动画。

**Q：为何有些场景动画设置的duration参数并不生效？**

**A**：弹性动画曲线为物理曲线，animation、animateTo、pageTransition中的duration参数不生效，动画持续时间取决于interpolatingSpring动画曲线参数，具体可见[curves.interpolatingSpring](../harmonyos-references/js-apis-curve.md#curvesinterpolatingspring10)。

**Q：animation属性生效，是否有特殊要求？**

**A**：属性动画只对写在[animation](../harmonyos-references/ts-animatorproperty.md#animation)前面的属性生效，且对组件构造器的属性不生效。
