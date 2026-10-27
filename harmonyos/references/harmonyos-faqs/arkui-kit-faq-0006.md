---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-kit-faq-0006
title: ArkUI-Swiper组件滑动与切换常见问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 常见问题 > ArkUI-Swiper组件滑动与切换常见问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:46:59+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:f04fefc8899494ff1479c2b68193479ccc9851503887f2771f3dd0d3754744d8
---

**Q：如何在Swiper最后一项的尾部设置一个添加按钮，并自定义按钮的大小？效果预览：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/sRAlt7wYTpu2o80gUhgrbg/zh-cn_image_0000002793586631.png "点击放大")

**A**：在外层使用Scroll组件，内部依次排列Swiper组件和添加按钮，设置Swiper优先滑动。当Swiper滑动到末尾时，继续滑动的为外层Scroll组件，显示出添加按钮。

* 在Scroll的滚动事件onDidScroll回调中，当Scroll的偏移量offset不为0时，设置Swiper不可滚动，当Scroll的偏移量为0时，重新设置Swiper可以滚动交互，以避免手指往回滑动Scroll时，Swiper也被滑动。
* 在Scroll的滚动停止onScrollStop回调中，根据手指滑动方向，设置Scroll滚动的边缘效果，以实现添加按钮跟随手指滑动的边缘对齐逻辑。

  ```ts
  @Entry
  @Component
  struct SwiperButtonDemo {
    private scroller: Scroller = new Scroller();
    @State currentIndex: number = 0;
    @State bgColors: string[] = ['#F1F3F5', '#F1F3F5', '#F1F3F5'];
    @State swiperEnable: boolean = true; // Swiper是否可交互
    @State directionRight: boolean = false; // 控制外层Scroll是否向右滑动

    build() {
      Scroll(this.scroller) {
        Row() {
          Swiper() {
            ForEach(this.bgColors, (item: string, index: number) => {
              Row() {
                Text(`${index}`).fontSize('24fp');
              }
              .justifyContent(FlexAlign.Center)
              .borderRadius('16')
              .backgroundColor(item);
            });
          }
          .index($$this.currentIndex)
          .enabled(this.swiperEnable)
          .loop(false)
          .width('100%')
          .height('25%')
          .nestedScroll(SwiperNestedScrollMode.SELF_FIRST) // Swiper优化Scroll滑动
          .indicator(
            Indicator.dot()
              .selectedItemWidth(10)
              .selectedItemHeight(5)
              .selectedColor('#FFFFFF')
              .color('#80ffffff')
          )
          .itemSpace(6)
          .nextMargin(10)
          .prevMargin(10)
          .effectMode(EdgeEffect.None);

          if (this.bgColors.length < 10) {
            Row() {
              Text(`添加`);
            }
            .onClick(() => {
              this.bgColors.push('#F1F3F5'); // 增加Swiper数据的数量
              this.currentIndex += 1;
            })
            .margin({ 'right': '10vp' })
            .justifyContent(FlexAlign.Center)
            .borderRadius('16')
            .width(100)
            .height(100)
            .backgroundColor('#F1F3F5');
          }
        }.margin({ top: '40vp' });
      }
      .width('100%')
      .scrollable(ScrollDirection.Horizontal)
      .scrollBar(BarState.Off)
      .onDidScroll((xOffset: number) => {
        if (xOffset > 0) {
          this.directionRight = true;
        } else if (xOffset < 0) {
          this.directionRight = false;
        }
        if (this.scroller.currentOffset().xOffset === 0) {
          this.swiperEnable = true;
        } else {
          this.swiperEnable = false;
        }
      })
      .onScrollStop(() => {
        this.scroller.scrollEdge(this.directionRight ? Edge.End : Edge.Top);
      });
    }
  }
  ```

**Q：如何实现一种舞台切换效果，具体要求如下：**

1. 页面可以左右滑动，初始时铺满屏幕，当移动距离大于屏幕一半会切换进入舞台效果。
2. 舞台效果：页面呈现三个内容，中间栏长宽略大于两侧。滑动切换页面，中间栏变小退到一侧，目标栏放大到中央。
3. 点击中间栏可退出舞台效果模式，此时原位于舞台中央的内容将重新恢复全屏显示，若点击两侧的目标栏，则将其直接切换到中央但不退出舞台效果。\*\*

**A**：舞台切换效果可以分割成以下几个点分别实现后再组合：

1. 拖拽滑动距离大于父组件一半时切换页面是Swiper组件自带的属性，所有页面主体选择使用Swiper组件构成。
2. 舞台由三个子组件构成，其中两侧子组件只展示部分，Swiper组件的[nextMargin](../harmonyos-references/ts-container-swiper.md#nextmargin10)和[prevMargin](../harmonyos-references/ts-container-swiper.md#prevmargin10)属性可以很好地契合这一点，通过传入数值设置前后边距，只露出前后项的一小部分。
3. 全屏铺满和舞台效果的切换以及舞台状态下滑动组件的大小变化，均可通过设置scale属性来控制Swiper子组件的缩放比例实现，通过Swiper组件的[customContentTransition事件](../harmonyos-references/ts-container-swiper.md#customcontenttransition12)自定义Swiper页面切换动画，根据滑动的状态变化调整组件的缩放比例。
4. 点击将两侧目标栏直接切换到中央，可以通过给Swiper组件绑定[SwiperController](../harmonyos-references/ts-container-swiper.md#swipercontroller)以及[onClick事件](../harmonyos-references/ts-universal-events-click.md#onclick12)，当检测到点击事件触发时，调用控制器的[changeIndex](../harmonyos-references/ts-container-swiper.md#changeindex15)方法，将目标元素直接切换到中间位置。

完整示例代码如下：

```ts
@Entry
@Component
struct StageDemo {
  private swiperController: SwiperController = new SwiperController();
  @State showList: Array<string> = []; // 内容列表
  @State nowShow: number = 0; // 当前页
  @State isScroll: boolean = false; // 是否滑动状态

  aboutToAppear(): void {
    for (let index = 0; index < 10; index++) {
      this.showList.push(index.toString());
    }
  }

  build() {
    Column() {
      Swiper(this.swiperController) { // 绑定控制器
        ForEach(this.showList, (item: string, index: number) => {
          Column() {
            Text(item)
              .width(100)
              .border({
                width: 1,
                color: Color.White
              })
          }
          .border({
            radius: 20
          })
          .backgroundColor(Color.Pink)
          .width('100%')
          .height('100%')
          .justifyContent(FlexAlign.Center)
          .scale(this.nowShow === index ? (this.isScroll ? { x: 1, y: 0.5 } : { x: 1, y: 1 }) :
            (this.isScroll ? { x: 0.9, y: 0.4 } : { x: 1, y: 1 }))
          .animation({
            duration: 200,
            curve: Curve.Linear
          })
          .onClick(() => {
            if (this.nowShow === index) {
              this.isScroll = false;
            } else {
              this.swiperController.changeIndex(index); // 小屏（舞台）状态下，将点击的内容切换到中央显示
              this.nowShow = index;
            }
          })
        })
      }
      .prevMargin(this.isScroll ? 100 : 0) // 当处于小屏滑动状态时设置前后边距
      .nextMargin(this.isScroll ? 100 : 0)
      .loop(false) // 不能循环
      .indicator(false) // 不显示导航点
      .itemSpace(24) // 设置子组件间隔
      .duration(400) // 动画时间
      .curve(Curve.Linear)
      .onAnimationEnd((index) => {
        if (this.nowShow !== index) { // 滑动结束时，如果展示页面发生了变化，则将视图转化为小屏滑动
          this.nowShow = index;
          this.isScroll = true;
        }
      })
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
    .backgroundColor(Color.Yellow)
  }
}
```

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/Q0Zmqc7TTi-WGjykqPIYjg/zh-cn_image_0000002793507491.png "点击放大")

**Q：Swiper里嵌套不同的视频，滑动Swiper时（比如从第一个Item滑动到第二个Item），如何让之前的Item暂停视频播放？**

**A**：Swiper滑动时触发onChange事件，在onChange方法里调用VideoController的pause方法即可实现滑动过程控制视频暂停播放，代码示例如下：

```ts
@Entry
@Component
struct demoExample {
  private controllerList: VideoController[] =
    [new VideoController(), new VideoController(), new VideoController(), new VideoController()];
  @State swiperIndex: number = 0;

  build() {
    Swiper() {
      ForEach([0, 1, 2, 3], (item: number) => {
        Column() {
          Text(`第 ${item + 1} 个组件页`)
            .width('100%')
            .backgroundColor(Color.White)
            .textAlign(TextAlign.Center)
            .fontSize(20);
          Video({
            // 此处'www.xxx.com/yyy.mp4'仅作为示例
            src: 'www.xxx.com/yyy.mp4',
            controller: this.controllerList[item]
          })
            .objectFit(ImageFit.Contain)
            .controls(true)
            .autoPlay(false)
            .loop(true)
            .height(200);
        };
      });
    }
    .loop(true)
    .backgroundColor(Color.Black)
    .onChange((index: number) => {
      const preIndex = index > 0 ? index - 1 : 3;
      const nextIndex = index < 3 ? index + 1 : 0;
      this.controllerList[preIndex].pause();
      this.controllerList[nextIndex].pause();
      this.swiperIndex = index;
    });
  }
}
```

**Q：如果要视频切回来之后重新播放，应该如何设置？**

**A**：只需将上述样例代码中onChange方法里调用的pause()方法换成stop()即可。需要注意的是，这里切回来之后显示的还是暂停时的那一帧内容，在点击播放时会重新播放。

**Q：如果Video组件设置了预览图和视频路径，如何在视频播放暂停时如何由当前帧重置到预览图？**

**A**：可使用Stack堆叠Image和Video，通过状态控制Image的显示/隐藏，实现暂停时展示预览图、播放时隐藏的效果。

**Q：使用Swiper组件的DotIndicator构建导航指示器，并将导航点底部相对于Swiper的位置属性bottom设置为0，该指示器无法完全贴底，具体演示如下：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/B_0wsaC0RjeUCYg4ZeYryw/zh-cn_image_0000002764029006.png "点击放大")

**上下左右存在留白，如何实现可以去除内边距的导航指示器效果？**

**A**：解决方案如下：

* 方案一：采用API19的bottom接口。

  通过bottom接口，可以实现指示器与底部间距为0。实现方式详见：[示例9](../harmonyos-references/ts-container-swiper.md#示例9演示导航点space与bottom)。
* 方案二：自定义Indicator。

  当前DotIndicator的规格固定存在内边距，无法满足问题需求。可以通过以下步骤实现无内边距的导航指示器效果：

  1. 在Stack组件中创建Swiper轮播组件与导航点Column组件。
  2. 使用[LazyForEach](../harmonyos-references/ts-rendering-control-lazyforeach.md)循环渲染Column组件，并设置合适的高度和外边距，例如在Stack组件内设置[alignContent](../harmonyos-references/ts-container-stack.md#aligncontent)参数为[Alignment](../harmonyos-references/ts-appendix-enums.md#alignment).Bottom，表示底部对齐，也可以采用[位置设置](../harmonyos-references/ts-universal-attributes-location.md)的方式，直接指定指示器位置。
  3. 将index的值与currentIndex作比较，当两者相同时，改变Column的宽度与颜色，以此实现导航点效果。

  具体参考代码如下所示：

  ```ts
  @Entry
  @Component
  struct SwiperExample {
    private swiperController: SwiperController = new SwiperController();
    @State arr: string[] = ['1', '2', '3', '4', '5', '6'];
    @State currentIndex: number = 0;

    build() {
      Column({ space: 5 }) {
        Stack({ alignContent: Alignment.Bottom }) {
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
          .onChange((index: number) => {
            this.currentIndex = index;
          });

          Row() {
            ForEach(this.arr, (item: string, index: number) => {
              Column()
                .width(this.currentIndex === index ? 15 : 5)
                .height(5)
                .margin(5)
                .backgroundColor(this.currentIndex === index ? Color.Gray : Color.White);
            }, (item: string) => item);
          };
        };
      }
      .width('100%')
      .height('100%');
    }
  }
  ```

  方案二运行效果图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/hKwEB2pqSuy8IBZR9FxgdA/zh-cn_image_0000002793588067.png "点击放大")

* 方案三：采用API15中Indicator组件。Indicator组件采用的依旧是Swiper中的默认指示器样式，一样有32vp的交互高度限制，不过该组件将Swiper与指示器单独分割，可以通过Column组件单独封装指示器，再通过clip属性裁剪，控制Indicator组件高度，其它的与方案二类似采用Stack组件封装。

  具体参考代码如下所示：

  ```screen
  @Entry
  @Component
  struct DotIndicatorDemo {
    private indicatorController: IndicatorComponentController = new IndicatorComponentController();
    private swiperController: SwiperController = new SwiperController();
    @State list: string[] = ['1', '2', '3', '4', '5', '6'];

    build() {
      Stack({ alignContent: Alignment.Bottom }) {
        Swiper(this.swiperController) {
          ForEach(this.list, (item: string) => {
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
        .indicator(this.indicatorController);

        Column() {
          IndicatorComponent(this.indicatorController)
            .style(
              new DotIndicator()
                .itemWidth(10)
                .itemHeight(10)
                .selectedItemWidth(20)
                .selectedItemHeight(10)
                .color(Color.White)
                .selectedColor(Color.Gray)
            );
        }
        .height(25)
        .clip(true);
      }
      .width('100%');
    }
  }
  ```

  方案三运行效果图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/jbXXHJTeQXieAShseiaUzg/zh-cn_image_0000002764190976.png "点击放大")

  **须知** 

  若方案三指示器背景为透明，不使用clip裁剪也可。同时若背景颜色为透明，也可采用margin属性，设置底部为负值达成类似消除内边距的效果。

**Q：如何实现Swiper指示器居左下角显示？**

**A**：可以直接方案二采用位置设置的方式对自定义指示器位置进行定位，或采用自带指示器通过方案一，方案三消除内边距再进行左下角对齐。

**Q：如何修改Swiper指示器自带样式圆点的颜色？**

**A**：DotIndicator中.color设置未选中的圆点颜色，.selectedColor属性设置选中的圆点颜色。

**Q：如何实现Swiper指示器显示在Swiper外侧？**

**A**：方案二、方案三去掉Stack层叠组件替换为Column组件，默认从上往下排列即可。

**Q：使用Swiper组件，期望初始化显示时即加载最后一个位置的内容，应该如何实现？**

**A**：通过$$将index属性与@State装饰的变量双向绑定。

* 手指滑动Swiper切换页面，index变化会同步至@State变量，可实现获取当前显示页面下标的效果。
* 通过修改@State变量可以改变Swiper显示的页面，可实现显示指定index页面的效果。

  示例代码如下：将@State变量showIndex与Swiper的index双向绑定。

  ```ts
  @Entry
  @Component
  struct SwiperIndexDemo {
    private swiperNumber: number[] = [0, 1, 2, 3, 4, 5, 6, 7];
    @State showIndex: number = this.swiperNumber.length - 1;
    private swiperController: SwiperController = new SwiperController();

    build() {
      Column({ space: 16 }) {
        Swiper(this.swiperController) {
          ForEach(this.swiperNumber, (item: number) => {
            Text(item.toString())
              .width(250)
              .height(250)
              .backgroundColor(Color.Gray)
              .textAlign(TextAlign.Center)
              .fontSize(30);
          });
        }.index($$this.showIndex); // 与showIndex变量双向绑定
        Text(`当前showIndex: ${this.showIndex}`);
        Button(`showIndex+1`)
          .onClick(() => {
            this.showIndex = (this.showIndex + 1) % this.swiperNumber.length;
          });
      }.width('100%').margin({ top: 5 });
    }
  }
  ```

  效果如下：Swiper初始化显示最后一页内容，滑动Swiper会改变showIndex，改变showIndex也能滑动Swiper。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/w5MbMXBQRxu5iM_-AL5SNw/zh-cn_image_0000002764196330.png "点击放大")

**Q：Swiper的index方法显示指定位置无滑动动画，期望和手动滑动动画一致。**

**A**：可以使用SwiperController的[changeIndex](../harmonyos-references/ts-container-swiper.md#changeindex15)方法来指定显示位置，通过入参可以指定切换的动画效果。

**Q：ArcSwiper没有changeIndex方法，如何跳转到指定页面？**

**A**：可以通过设置[index](../harmonyos-references/ts-container-arcswiper.md#index)属性跳转到指定页面。
