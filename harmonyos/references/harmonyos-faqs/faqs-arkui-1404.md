---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1404
title: 如何实现自定义indicator
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现自定义indicator
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:10+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3023c97515832a6bb7a70f6a556e826225029fe63d19acf29eabe9151925eb51
---

## 问题现象

在软件开发过程中，Swiper组件的indicator指示器仅提供导航点和数字两种默认形式，不支持样式自定义，比如自定义背景颜色，自定义动画效果等多种情况，同时在指示器位置的设置上也有较大的局限性。所以需要实现自定义indicator的功能。

## 背景知识

[Swiper组件](../harmonyos-references/ts-container-swiper.md)是一种滑块视图容器，提供了子组件轮播展示的能力，同时该组件的[indicator](../harmonyos-references/ts-container-swiper.md#indicator)属性可以设置导航点指示器样式，可选参数如下：

| 参数类型 | 说明 | 效果 |
| --- | --- | --- |
| [IndicatorComponentController](../harmonyos-references/ts-swiper-components-indicator.md#indicatorcomponentcontroller) | API15之后新增。 | 可以与外部单独导航点进行绑定。 |
| [DotIndicator](../harmonyos-references/ts-container-swiper.md#dotindicator10) | API10后可以使用。 | 圆点指示器样式：[示例1（设置导航点交互及翻页动效）](../harmonyos-references/ts-container-swiper.md#示例1设置导航点交互及翻页动效)。 |
| [DigitIndicator](../harmonyos-references/ts-container-swiper.md#digitindicator10) | API10后可以使用。 | 数字指示器样式：[示例2（设置数字指示器）](../harmonyos-references/ts-container-swiper.md#示例2设置数字指示器)。 |
| boolean | 是否启用导航点指示器。 | 设置为true启用，false不启用。默认值：true。 |

## 解决方案

实现思路：

1. 自定义indicator需要先不启用导航点指示器，即设置Swiper属性indicator(false)。
2. 然后根据需要实现的效果设置相应的布局。比如利用Stack布局把Swiper和自定义indicator堆叠显示。
3. 自定义设置indicator样式，并通过onChange等事件获取Swiper显示的页面索引，设置对应的indicator显示。

常见场景：

* **场景一**：自定义基础指示器。

  实现基础的导航指示器（圆点、长条、数字等）。

  ```ts
  @Entry
  @Component
  struct SceneOne {
    private swiperController: SwiperController = new SwiperController();
    @State arr: string[] = ['1', '2', '3', '4', '5', '6'];
    @State currentIndex: number = 0;

    build() {
      Column() {
        Stack({ alignContent: Alignment.Bottom }) {
          Swiper(this.swiperController) {
            ForEach(this.arr, (item: string) => {
              Text(item)
                .width('90%')
                .height(200)
                .backgroundColor(0xAFEEEE)
                .textAlign(TextAlign.Center)
                .fontSize(30)
            }, (item: string) => item)
          }
          .cachedCount(2)
          .index(0)
          .indicator(false)
          .onChange((index: number) => {
            this.currentIndex = index; // 控制指示器。
          })

          // 导航点指示器。
          Row({ space: 5 }) {
            ForEach(this.arr, (item: string, index: number) => {
              Column()
                .width(this.currentIndex === index ? 20 : 7) // 控制导航点样式。
                .height(7)
                .borderRadius(7)
                .backgroundColor(this.currentIndex === index ? Color.Gray : Color.White) // 控制导航点样式。
            }, (item: string) => item)
          }
          .margin({ bottom: 5 })
        }

        // 数字指示器。
        Row() {
          Text((this.currentIndex + 1).toString())
            .fontSize(20)
            .fontColor(Color.Black)
          Text('/')
            .fontSize(18)
            .fontColor(Color.Black)
          Text(this.arr.length.toString())
            .fontSize(20)
            .fontColor(Color.Black)
        }
        .alignItems(VerticalAlign.Bottom)
      }
      .width('100%')
      .height('100%')
    }
  }
  ```
* **场景二**：自定义指示器动效。
  1. 自定义导航点动效。

     第1步：设置一个指示器遮罩层，通过控制遮罩层的大小和位置变换实现动画效果。

     第2步：通过[keyframeAnimateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#keyframeanimateto11)关键帧动画实现遮罩层动效长度的变化。

     第3步：由于第二步中长度变化动画是默认左侧位置不变，右侧伸长与缩短实现。所以往右侧滑动时，动画效果与实际不符。需要通过[onAnimationStart](../harmonyos-references/ts-container-swiper.md#onanimationstart9)判断是往左或者往右滑动，再通过[animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)在第二步基础上长度变化时改变遮罩层位置，实现往左或往右滑动效果一致。

     ```ts
     import { UIContext } from '@kit.ArkUI';

     @Entry
     @Component
     struct DotIndicator {
       private swiperController: SwiperController = new SwiperController();
       @State arr: string[] = ['1', '2', '3', '4', '5', '6'];
       @State widthLength: number = 7; // 动效图案宽度。
       widthPoint: number = 7; // 导航点宽度。
       spacePoint: number = 5; // 导航点间距。
       positionArr: Array<Array<number>> = []; // 动效位置数组。
       positionX: number = 0;
       positionY: number = 0;
       @State currentX: number = 0; // 准确的动效位置。
       currentY: number = 0; // 准确的动效位置。
       uiContext: UIContext | undefined = undefined;
       @State toggle: boolean = true;

       aboutToAppear(): void {
         this.uiContext = this.getUIContext();
         // 动效图案位置储存。
         for (let i = 0; i < this.arr.length; i++) {
           this.positionArr.push([this.positionX, this.positionY]);
           this.positionX = this.positionX + this.widthPoint + this.spacePoint;
         }
       }

       build() {
         Column() {
           Stack({ alignContent: Alignment.Bottom }) {
             Swiper(this.swiperController) {
               ForEach(this.arr, (item: string) => {
                 Text(item)
                   .width('90%')
                   .height(200)
                   .backgroundColor(0xAFEEEE)
                   .textAlign(TextAlign.Center)
                   .fontSize(30)
               }, (item: string) => item)
             }
             .cachedCount(2)
             .index(0)
             .indicator(false)
             .onAnimationStart((index: number, targetIndex: number, extraInfo: SwiperAnimationEvent) => {
               // 判断是向前还是向后滑动。
               if (extraInfo.currentOffset > 0) {
                 this.toggle = true;
               } else {
                 this.toggle = false;
               }
               console.info(`onAnimationStart：划出页面${index}`);
               console.info(`onAnimationStart：目标页面${targetIndex}`);
             })
             .onChange((index: number) => {
               if (!this.uiContext) {
                 console.error('no uiContext, keyframe failed');
                 return;
               }
               // 设置关键帧动画整体播放1次，分前后动画样式。
               if (this.toggle && index !== this.arr.length - 1) {
                 this.widthLength = 19;
                 this.uiContext.keyframeAnimateTo({
                   iterations: 1
                 }, [
                   {
                     duration: 600,
                     event: () => {
                       this.widthLength = 7;
                     }
                   }
                 ]);
                 this.currentX = this.positionArr[index][0];
               } else {
                 this.widthLength = 19;
                 this.uiContext.keyframeAnimateTo({
                   iterations: 1
                 }, [
                   {
                     duration: 600,
                     event: () => {
                       this.widthLength = 7;
                     }
                   }
                 ]);
                 this.uiContext.animateTo({ duration: 600, curve: Curve.EaseInOut }, () => {
                   this.currentX = this.positionArr[index][0];
                 });
               }
             })

             // 导航点指示器。
             Stack() {
               Row({ space: this.spacePoint }) {
                 ForEach(this.arr, () => {
                   Column()
                     .width(this.widthPoint)
                     .height(7)
                     .borderRadius(7)
                     .backgroundColor(Color.White)
                 }, (item: string) => item)
               }

               // 动效的图案。
               Column()
                 .width(this.widthLength)
                 .height(7)
                 .borderRadius(7)
                 .backgroundColor(Color.Blue)
                 .position({ x: this.currentX, y: this.currentY })
             }
             .margin({ bottom: 5 })
           }
         }
         .width('100%')
         .height('100%')
       }
     }
     ```
  2. 数字指示器动效。

     相较于导航点指示器，数字指示器动效相对简单可以通过滚动与滑动组件实现翻页滚动动效。以下示例通过Swiper组件实现数字指示器滚动效果。

     ```ts
     import { display } from '@kit.ArkUI';

     @Entry
     @Component
     struct DigitIndicator {
       private swiperController: SwiperController = new SwiperController();
       private swiperControllerTwo: SwiperController = new SwiperController(); // 数字滚动控制器。
       @State arr: string[] = ['1', '2', '3', '4', '5', '6'];
       @State screenWidth: number = 0;

       aboutToAppear(): void {
         display.getAllDisplays((err, data) => {
           this.screenWidth = this.getUIContext().px2vp(data[0].width); // 获取屏幕宽度
           if (err) {
             console.info(JSON.stringify(err));
           }
         });
       }

       build() {
         Column() {
           Stack() {
             Swiper(this.swiperController) {
               ForEach(this.arr, (item: string) => {
                 Text(item)
                   .width('90%')
                   .height(200)
                   .backgroundColor(0xAFEEEE)
                   .textAlign(TextAlign.Center)
                   .fontSize(30);
               }, (item: string) => item);
             }
             .cachedCount(2)
             .index(0)
             .indicator(false)
             .onAnimationStart((index: number, targetIndex: number, extraInfo: SwiperAnimationEvent) => {
               // 判断是向前还是向后滑动。
               if (index === 0 && targetIndex === this.arr.length - 1) {
                 this.swiperControllerTwo.showPrevious();
               } else if (targetIndex === 0 && index === this.arr.length - 1) {
                 this.swiperControllerTwo.showNext();
               } else {
                 this.swiperControllerTwo.changeIndex(targetIndex, true);
               }
               console.info(`onAnimationStart：划出页面${index}`);
               console.info(`onAnimationStart：目标页面${targetIndex}`);
               console.info(`extraInfo：${JSON.stringify(extraInfo)}`);
             });

             // 数字指示器。
             Row() {
               Swiper(this.swiperControllerTwo) {
                 ForEach(this.arr, (item: string) => {
                   Text(item)
                     .fontColor(Color.Black)
                     .fontSize(16);
                 }, (item: string) => item);
               }
               .index(0)
               .vertical(true) // 纵向滚动。
               .indicator(false);

               Text('/')
                 .fontSize(18)
                 .fontColor(Color.Black);
               Text(this.arr.length.toString())
                 .fontSize(20)
                 .fontColor(Color.Black);
             }
             .alignItems(VerticalAlign.Bottom)
             .position({ x: this.screenWidth * 0.9 - 35, y: 175 });
           };
         }
         .width('100%')
         .height('100%');
       }
     }
     ```
* **场景三**：当Swiper同时显示多个卡片时，导航点也显示多个点高亮的效果。

  当Swiper需要同时展示两个卡片时，由于自带的默认指示器不支持两个导航点同时高亮的样式，所以需要采用自定义的方式实现两个导航点高亮的效果。

  实现步骤如下：

  第1步：实现场景二中的导航点指示器。

  第2步：修改遮罩层动效的起始和结束长度，使其结束的长度等于两个导航点宽度与间距之和。

  第3步：当Swiper展示的数量为单数时，需要通过this.currentIndex!==this.arr.length-1判定是否是最后一个导航点，最后一个导航点遮罩层动效宽度为导航点宽度即可。

  ```ts
  import { UIContext } from '@kit.ArkUI';

  @Entry
  @Component
  struct SceneThree {
    private swiperController: SwiperController = new SwiperController();
    @State arr: string[] = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'];
    widthPoint: number = 7; // 导航点宽度。
    spacePoint: number = 5; // 导航点间距。
    @State widthLength: number = this.widthPoint + this.spacePoint + this.widthPoint; // 动效图案宽度。
    positionArr: Array<Array<number>> = []; // 动效位置数组。
    positionX: number = 0;
    positionY: number = 0;
    @State currentX: number = 0; // 准确的动效位置。
    currentY: number = 0; // 准确的动效位置。
    currentIndex: number = 0;
    uiContext: UIContext | undefined = undefined;
    @State toggle: boolean = true;

    aboutToAppear(): void {
      this.uiContext = this.getUIContext();
      // 动效图案位置储存。
      for (let i = 0; i < this.arr.length; i++) {
        this.positionArr.push([this.positionX, this.positionY]);
        this.positionX = this.positionX + this.widthPoint + this.spacePoint;
      }
    }

    build() {
      Column() {
        Stack({ alignContent: Alignment.Bottom }) {
          Swiper(this.swiperController) {
            ForEach(this.arr, (item: string) => {
              Text(item)
                .width('90%')
                .height(200)
                .backgroundColor(0xAFEEEE)
                .textAlign(TextAlign.Center)
                .fontSize(30)
            }, (item: string) => item)
          }
          .cachedCount(2)
          .index(0)
          .displayCount(2, true)
          .indicator(false)
          .onAnimationStart((index: number, targetIndex: number, extraInfo: SwiperAnimationEvent) => {
            // 判断是向前还是向后滑动。
            if (extraInfo.currentOffset > 0) {
              this.toggle = true;
            } else {
              this.toggle = false;
            }
            console.info(`onAnimationStart：划出页面${index}`);
            console.info(`onAnimationStart：目标页面${targetIndex}`);
          })
          .onChange((index: number) => {
            if (!this.uiContext) {
              console.error('no uiContext, keyframe failed');
              return;
            }
            this.currentIndex = index; // 设置滑动位置。
            // 设置关键帧动画整体播放1次,分前后动画样式。
            if (this.toggle && index !== this.arr.length - 1) {
              // 根据滑动位置判断动效图案长度。
              if (this.currentIndex !== this.arr.length - 1) {
                this.widthLength =
                  this.widthPoint + this.spacePoint + this.widthPoint + this.spacePoint + this.widthPoint +
                  this.spacePoint + this.widthPoint;
              } else {
                this.widthLength =
                  this.widthPoint + this.spacePoint + this.widthPoint + this.spacePoint + this.widthPoint;
              }
              this.uiContext.keyframeAnimateTo({
                iterations: 1
              }, [
                {
                  duration: 600,
                  event: () => {
                    // 根据滑动位置判断动效图案长度。
                    if (this.currentIndex !== this.arr.length - 1) {
                      this.widthLength = this.widthPoint + this.spacePoint + this.widthPoint;
                    } else {
                      this.widthLength = this.widthPoint;
                    }
                  }
                }
              ]);
              this.currentX = this.positionArr[index][0];
            } else {
              // 根据滑动位置判断动效图案长度。
              if (this.currentIndex !== this.arr.length - 1) {
                this.widthLength =
                  this.widthPoint + this.spacePoint + this.widthPoint + this.spacePoint + this.widthPoint +
                  this.spacePoint + this.widthPoint;
              } else {
                this.widthLength =
                  this.widthPoint + this.spacePoint + this.widthPoint + this.spacePoint + this.widthPoint;
              }
              this.uiContext.keyframeAnimateTo({
                iterations: 1
              }, [
                {
                  duration: 600,
                  event: () => {
                    // 根据滑动位置判断动效图案长度。
                    if (this.currentIndex !== this.arr.length - 1) {
                      this.widthLength = this.widthPoint + this.spacePoint + this.widthPoint;
                    } else {
                      this.widthLength = this.widthPoint;
                    }
                  }
                }
              ]);
              this.uiContext.animateTo({ duration: 600, curve: Curve.EaseInOut }, () => {
                this.currentX = this.positionArr[index][0];
              });
            }
          })

          // 导航点指示器。
          Stack() {
            Row({ space: this.spacePoint }) {
              ForEach(this.arr, () => {
                Column()
                  .width(this.widthPoint)
                  .height(7)
                  .borderRadius(7)
                  .backgroundColor(Color.White)
              }, (item: string) => item)
            }

            // 动效的图案。
            Column()
              .width(this.widthLength)
              .height(9)
              .borderRadius(7)
              .opacity(0.6) // 透明度设置。
              .backgroundColor(Color.Blue)
              .position({ x: this.currentX, y: this.currentY }) // 动效位置。
          }
          .margin({ bottom: 5 })
        }
        .backgroundColor(Color.Gray)
      }
      .width('100%')
      .height('100%')
    }
  }
  ```
* **场景四**：如何实现折叠屏展开时Swiper展示两个卡片，导航点指示器展示两个高亮点，折叠时Swiper展示一个卡片，导航点指示器展示一个高亮点。

  设置判断变量，并且通过监听折叠屏折叠状态（[FoldStatus](../harmonyos-references/ts-appendix-enums.md#foldstatus11)）判断动效是执行场景三还是场景二的动画即可。在场景三基础上做出修改如下：

  ```ts
  import { display, UIContext } from '@kit.ArkUI';

  @Entry
  @Component
  struct SceneFour {
    private swiperController: SwiperController = new SwiperController();
    @State arr: string[] = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'];
    widthPoint: number = 7; // 导航点宽度。
    spacePoint: number = 5; // 导航点间距。
    @State widthLength: number = this.widthPoint + this.spacePoint + this.widthPoint; // 动效图案宽度。
    positionArr: Array<Array<number>> = []; // 动效位置数组。
    positionX: number = 0;
    positionY: number = 0;
    @State currentX: number = 0; // 准确的动效位置。
    currentY: number = 0; // 准确的动效位置。
    currentIndex: number = 0;
    uiContext: UIContext | undefined = undefined;
    @State toggle: boolean = true;
    @State @Watch('changeWidth') foldStatus: number = 1; // 判断折叠屏状态，并监听状态修改遮罩动效初始宽度。

    // 遮罩动效初始宽度的修改函数。通过Watch监听foldStatus值发生变化时，执行该函数。
    changeWidth() {
      if (this.foldStatus === 2) {
        this.widthLength = this.widthPoint;
      } else {
        this.widthLength = this.widthPoint + this.spacePoint + this.widthPoint;
      }
    }

    aboutToAppear(): void {
      this.uiContext = this.getUIContext();
      // 动效图案位置储存。
      for (let i = 0; i < this.arr.length; i++) {
        this.positionArr.push([this.positionX, this.positionY]);
        this.positionX = this.positionX + this.widthPoint + this.spacePoint;
      }
      // 折叠屏状态监听。
      let callback: Callback<display.FoldStatus> = (data: display.FoldStatus) => {
        this.foldStatus = data;
      };
      display.on('foldStatusChange', callback);
    }

    build() {
      Column() {
        Stack({ alignContent: Alignment.Bottom }) {
          Swiper(this.swiperController) {
            ForEach(this.arr, (item: string) => {
              Text(item)
                .width('90%')
                .height(200)
                .backgroundColor(0xAFEEEE)
                .textAlign(TextAlign.Center)
                .fontSize(30)
            }, (item: string) => item)
          }
          .displayCount(this.foldStatus === 2 ? 1 : 2, true) // 根据折叠状态判断展示几个卡片。
          .cachedCount(2)
          .index(0)
          .displayCount(2, true)
          .indicator(false)
          .onAnimationStart((index: number, targetIndex: number, extraInfo: SwiperAnimationEvent) => {
            // 判断是向前还是向后滑动。
            if (extraInfo.currentOffset > 0) {
              this.toggle = true;
            } else {
              this.toggle = false;
            }
            console.info(`onAnimationStart：划出页面${index}`);
            console.info(`onAnimationStart：目标页面${targetIndex}`);
          })
          .onChange((index: number) => {
            if (!this.uiContext) {
              console.error('no uiContext, keyframe failed');
              return;
            }
            // 根据屏幕宽度判断实现场景二或者场景三动效。
            if (this.foldStatus === 2) {
              // 场景二动画方案。
              // 设置关键帧动画整体播放1次，分前后动画样式。
              if (this.toggle && index !== this.arr.length - 1) {
                this.widthLength = 19;
                this.uiContext.keyframeAnimateTo({
                  iterations: 1
                }, [
                  {
                    duration: 600,
                    event: () => {
                      this.widthLength = 7;
                    }
                  }
                ]);
                this.currentX = this.positionArr[index][0];
              } else {
                this.widthLength = 19;
                this.uiContext.keyframeAnimateTo({
                  iterations: 1
                }, [
                  {
                    duration: 600,
                    event: () => {
                      this.widthLength = 7;
                    }
                  }
                ]);
                this.uiContext.animateTo({ duration: 600, curve: Curve.EaseInOut }, () => {
                  this.currentX = this.positionArr[index][0];
                });
              }
            } else {
              // 场景三动画方案。
              this.currentIndex = index; // 设置滑动位置。
              // 设置关键帧动画整体播放1次,分前后动画样式。
              if (this.toggle && index !== this.arr.length - 1) {
                // 根据滑动位置判断动效图案长度。
                if (this.currentIndex !== this.arr.length - 1) {
                  this.widthLength =
                    this.widthPoint + this.spacePoint + this.widthPoint + this.spacePoint + this.widthPoint +
                    this.spacePoint + this.widthPoint;
                } else {
                  this.widthLength =
                    this.widthPoint + this.spacePoint + this.widthPoint + this.spacePoint + this.widthPoint;
                }
                this.uiContext.keyframeAnimateTo({
                  iterations: 1
                }, [
                  {
                    duration: 600,
                    event: () => {
                      // 根据滑动位置判断动效图案长度。
                      if (this.currentIndex !== this.arr.length - 1) {
                        this.widthLength = this.widthPoint + this.spacePoint + this.widthPoint;
                      } else {
                        this.widthLength = this.widthPoint;
                      }
                    }
                  }
                ]);
                this.currentX = this.positionArr[index][0];
              } else {
                // 根据滑动位置判断动效图案长度。
                if (this.currentIndex !== this.arr.length - 1) {
                  this.widthLength =
                    this.widthPoint + this.spacePoint + this.widthPoint + this.spacePoint + this.widthPoint +
                    this.spacePoint + this.widthPoint;
                } else {
                  this.widthLength =
                    this.widthPoint + this.spacePoint + this.widthPoint + this.spacePoint + this.widthPoint;
                }
                this.uiContext.keyframeAnimateTo({
                  iterations: 1
                }, [
                  {
                    duration: 600,
                    event: () => {
                      // 根据滑动位置判断动效图案长度。
                      if (this.currentIndex !== this.arr.length - 1) {
                        this.widthLength = this.widthPoint + this.spacePoint + this.widthPoint;
                      } else {
                        this.widthLength = this.widthPoint;
                      }
                    }
                  }
                ]);
                this.uiContext.animateTo({ duration: 600, curve: Curve.EaseInOut }, () => {
                  this.currentX = this.positionArr[index][0];
                });
              }
            }
          })

          // 导航点指示器。
          Stack() {
            Row({ space: this.spacePoint }) {
              ForEach(this.arr, () => {
                Column()
                  .width(this.widthPoint)
                  .height(7)
                  .borderRadius(7)
                  .backgroundColor(Color.White)
              }, (item: string) => item)
            }

            // 动效的图案。
            Column()
              .width(this.widthLength)
              .height(9)
              .borderRadius(7)
              .opacity(0.6) // 透明度设置。
              .backgroundColor(Color.Blue)
              .position({ x: this.currentX, y: this.currentY }) // 动效位置。
          }
          .margin({ bottom: 5 })
        }
        .backgroundColor(Color.Gray)
      }
      .width('100%')
      .height('100%')
    }
  }
  ```

## 常见FAQ

Q：一多适配时如何实现Swiper指示器样式变化？

A：参考场景四，通过[display.getAllDisplays](../harmonyos-references/js-apis-display.md#displaygetalldisplays9)获取屏幕宽度或者通过设备信息[@ohos.deviceInfo](../harmonyos-references/js-apis-device-info.md)接口获取设备类型等方式，在aboutToAppear()内判断不同设备，从而执行不同的动画效果及UI布局。

Q：如何修改Swiper中indicator导航点的间距？

A：可以通过本文档中自定义的方式，修改指示器部分代码的{space:5}中的数值即可，或在API19中可以通过[space](../harmonyos-references/ts-container-swiper.md#space19)修改Swiper自带的指示器导航点间距。

Q：如何修改Swiper中indicator的背景颜色？

A：Swiper组件自带的指示器背景颜色不支持修改，可以通过以下两种方式实现：

1. 通过本文档实现自定义的指示器并修改颜色。参考场景一，可以在自定义导航点指示器的最外层Row({space: 5})组件通过修改[backgroundColor](../harmonyos-references/ts-universal-attributes-background.md#backgroundcolor)属性，实现导航点背景颜色的修改。
2. 在API15中，新增加[Indicator组件](../harmonyos-references/ts-swiper-components-indicator.md)，该组件可以绑定Swiper组件的indicator指示器，且支持部分[通用属性](../harmonyos-references/ts-component-general-attributes.md)设置。实现方式参考：[API示例](../harmonyos-references/ts-swiper-components-indicator.md#示例)。

Q：如何修改Swiper中indicator的高度？

A：Swiper中自带的indicator不支持直接修改高度。在API15中，当Indicator组件绑定Swiper组件时，也不支持宽高修改。

1. 通过设置itemHeight或itemWidth调整宽高达到类似效果。API19之前，存在默认间距和间距，在API19之后可以通过设置indicator忽略默认的32vp高度，以及设置space属性重新设置间距等效的宽高控制效果。
2. 通过本文档的自定义方式实现指示器的宽高控制。

Q：Swiper中indicator设置.bottom(-18)不生效？

A：由于[Indicator.bottom](../harmonyos-references/ts-container-swiper.md#bottom)的取值范围：[0,Swiper高度-导航点区域高度]，超出该范围时，取最近的边界值。所以Swiper中indicator设置.bottom(-18)和Swiper中indicator设置.bottom(0)效果是一样的。
