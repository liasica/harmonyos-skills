---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1056
title: 多个滚动组件同步滚动实现方案及应用场景
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 多个滚动组件同步滚动实现方案及应用场景
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:04+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9f78935ec60727a5eaa576fe7949195e1dae8de169438aef4423ffb475366d5c
---

## 问题现象

滚动组件关联是软件中经常需要实现的效果，除了类似于滚动组件嵌套关联外，还有同级滚动组件的同步滚动关联，例如以下场景：

* 翻译类、文言文类软件翻译超长段文本。
* 购物软件进行参数对比。

以上场景，经常会需要多个滚动组件进行滚动关联，达到同步滚动的效果。

## 背景知识

同步滚动组件常用[Scroll组件](../harmonyos-references/ts-container-scroll.md)与[List组件](../harmonyos-references/ts-container-list.md)进行滚动，需要注意的是Scroll组件只能包含一个子组件。

常用控制滚动的事件有：

| 事件 | [scrollToIndex](../harmonyos-references/ts-container-scroll.md#scrolltoindex) | [scrollTo](../harmonyos-references/ts-container-scroll.md#scrollto) | [scrollBy](../harmonyos-references/ts-container-scroll.md#scrollby9) |
| --- | --- | --- | --- |
| 功能简介 | 通过监听索引值，支持滚动组件滑动到指定索引位置，且支持设置滑动额外偏移量。 | 通过监听位置偏移量，支持滑动指定的偏移量。 | 通过监听位置偏移量，支持滑动指定的偏移距离。 |
| 可支持回调方式简介 | [onScrollIndex](../harmonyos-references/ts-container-list.md#onscrollindex) | [onWillScroll](../harmonyos-references/ts-container-scrollable-common.md#onwillscroll12)、[onDidScroll](../harmonyos-references/ts-container-scrollable-common.md#ondidscroll12)、[onScrollFrameBegin](../harmonyos-references/ts-container-scroll.md#onscrollframebegin9) | 与scrollTo基本一致 |
| 可支持组件 | List等支持索引值监听的组件 | List/Scroll等支持位移监听的组件 | List/Scroll等支持位移监听的组件 |

**须知** 

onScroll事件从API version11开始使用，从API version12开始废弃不再使用。

## 解决方案

* **场景一：文本翻译实现同步跟随滚动查看。**

  该参考案例采用Scroll组件及scrollTo方式实现两个同级滚动组件的同步滚动：

  1. 由于翻译文本和原文本长度和高度不一致，可以通过[onSizeChange](../harmonyos-references/ts-universal-component-size-change-event.md#onsizechange)事件对被翻译文本和翻译完成的文本进行高度计算。
  2. 然后计算转换后的偏移量，通过scrollTo达成同步滚动的效果。

  ```ts
  @Entry
  @Component
  struct SceneOne {
    private contentTxt: string =
      '子曰：“学而时习之，不亦说乎？有朋自远方来，不亦乐乎？人不知而不愠，不亦君子乎？”\n' +
        '有子曰：“其为人也孝弟，而好犯上者，鲜矣；不好犯上而好作乱者，未之有也。君子务本，本立而道生。孝弟也者，其为仁之本与！”\n' +
        '子曰：“巧言令色，鲜矣仁！”\n' +
        '曾子曰：“吾日三省吾身：为人谋而不忠乎？与朋友交而不信乎？传不习乎？”\n' +
        '子曰：“道千乘之国，敬事而信，节用而爱人，使民以时。”\n' +
        '子曰：“弟子入则孝，出则弟，谨而信，泛爱众，而亲仁，行有余力，则以学文。”\n' +
        '子夏曰：“贤贤易色；事父母，能竭其力；事君，能致其身；与朋友交，言而有信。虽曰未学，吾必谓之学矣。”\n' +
        '子曰：“君子不重则不威，学则不固。主忠信，无友不如己者，过，则勿惮改。”\n' +
        '曾子曰：“慎终追远，民德归厚矣。”\n' +
        '子禽问于子贡曰：“夫子至于是邦也，必闻其政，求之与，抑与之与？”\n' +
        '子贡曰：“夫子温、良、恭、俭、让以得之。夫子之求之也，其诸异乎人之求之与？”\n' +
        '子曰：“父在，观其志；父没，观其行；三年无改于父之道，可谓孝矣。”\n' +
        '有子曰：“礼之用，和为贵。先王之道，斯为美。小大由之，有所不行。知和而和，不以礼节之，亦不可行也。”\n' +
        '有子曰：“信近于义，言可复也。恭近于礼，远耻辱也。因不失其亲，亦可宗也。”\n' +
        '子曰：“君子食无求饱，居无求安，敏于事而慎于言，就有道而正焉，可谓好学也已。”\n' +
        '子贡曰：“贫而无谄，富而无骄，何如？”\n' +
        '子曰：“可也。未若贫而乐，富而好礼者也。”\n' +
        '子贡曰：“《诗》云：‘如切如磋，如琢如磨’，其斯之谓与？”\n' +
        '子曰：“赐也，始可与言《诗》已矣，告诸往而知来者。”\n' +
        '子曰：“不患人之不己知，患不知人也。”\n';
    private contentTxt2: string =
      '孔子说：“学的道理在合适的时机去实践，不也是很快乐吗？有志同道合的人从远方来，不也是很快乐吗？人家不了解我，我也不生气，不也是品德上有修养的人吗？”\n' +
        '有子说：“一个人如果能够孝顺父母，友爱兄长，却喜欢犯上作乱，这是基本不可能。不喜欢犯上作乱，而喜欢造反的人是没有的。君子应该专心于根本的事务，' +
        '根本建立了，治国做人的原则也就有了。孝悌，这是仁爱的根本！”\n' +
        '孔子说：“花言巧语，满脸谄媚之色的人，很少会有仁爱之心。”\n' +
        '曾子说：“我每天多次地反省自己：替别人办事是不是尽心尽力呢 ？跟朋友交往是不是真诚，诚实呢？ 老师传授的知识是否复习过了呢？”\n' +
        '孔子说：“治理一个能出千辆兵车的大国，处理事务时应谨慎、恪守信用、诚实无欺，节约财政开支，爱惜百姓，征用民力时，要顾及他们的生产作息。”\n' +
        '孔子说：“弟子们在家里就要孝顺父母，出门在外，要顺从师长，言行要谨慎，要诚实可信，要博爱大众，亲近仁德的人。这样亲身实践之后，如果还有剩余的时间跟精力，' +
        '就再去学习文献知识。”\n' +
        '子夏说：“对妻子，看中品德，不看中姿色；侍奉父母，能够竭尽全力；服侍君主，能够献出自己的生命；跟朋友来往，能够说话诚实恪守信用。这样的人，' +
        '尽管他自己谦虚说没有学习，我也一定说他已经学习过了。”\n' +
        '孔子说：“君子举止不庄重，就没有威严，即使读书，学习的知识也不会牢固。做事应该以忠和信这两种道德为主，没有不如自己的朋友；犯了错，就不要怕改正。”\n' +
        '曾子说：“慎重办理父母的丧事，虔诚祭祀远代先祖，这样就能使百姓的德行趋归敦厚。”\n' +
        '子禽问子贡说：“老师去到一个国家，就会知道这个国家的政事。这种事情是他自己求得的呢？还是各个国家的国君主动以自己国家的政事咨询，亲口告诉他的呢？”\n' +
        '子贡说：“老师是靠温和、善良、恭敬、节俭、谦逊来取得他们的信任。他老人家获得的方法，和别人获得的方法，不相同吧？”\n' +
        '孔子说；“当他父亲还活着时，要观察他的志向；在他父亲去世以后，要观察他的行为；若是他能长久的坚持父亲生前正确的原则，这样的人就可以说是尽到孝了。”\n' +
        '有子说：“礼的作用，在于使人的关系变得更加和谐。古代君王治国的方法，宝贵的地方就在这里。但是不论大小事情一味按和谐的办法去做，有的时候又行不通。这是因' +
        '为为了和谐而和谐，不用礼来节制和谐，也是行不通的。”\n' +
        '有子说：“我们作出的承诺要合理，说过的话才能兑现。对人恭敬也要掌握好分寸，就不会招致屈辱。如果坚守着君子的底线，又能做到谦和恭顺，不至于让人难以亲近，' +
        '这样的人，着实值得尊敬。”\n' +
        '孔子说：“君子，不追求饮食的饱足，不追求居住的舒适，做事情勤劳敏捷，说话小心谨慎，亲近有德之人来匡正自己，这样就算得上好学了。”\n' +
        '子贡说：“贫穷却不巴结奉承，富有却不骄傲自大，怎么样？”孔子说：“这样可以算不错了。只是还不如虽贫穷却乐于道，虽然富裕却又好礼的人。”\n' +
        '子贡说：“《诗经》上说，‘要像骨、角、象牙、玉石等的加工一样，先开料，再粗锉，细刻，然后磨光’，就是讲的这个意思吧？”\n' +
        '孔子说：“子贡呀，你能从我已经讲过的话中领会到我还没有说到的意思，举一反三，我现在可以同你谈论《诗经》了。”\n' +
        '孔子说：“不要担心别人不了解自己，只需要担心自己不了解别人。”\n';
    // 文本高度变量
    @State contentTxtHeight2: number = 0;
    @State contentTxtHeight: number = 0;
    // 文本布局高度
    @State halfOfColumnHeight: number = 0;
    // 滑动偏移变量
    @State contentTxtOffsetY: number = 0;
    @State contentTxtOffsetY2: number = 0;
    scroller: Scroller = new Scroller();
    scroller2: Scroller = new Scroller();
    @State isScroll: boolean = true;

    build() {
      Column() {
        Scroll(this.scroller) {
          Text(this.contentTxt)
            .onSizeChange((oldValue: SizeOptions, newValue: SizeOptions) => {
              // 获取被翻译文本高度
              this.contentTxtHeight = newValue.height as number;
              console.info(`被翻译文本高度：${this.contentTxtHeight.toString()}，oldValue：${JSON.stringify(oldValue)}`);
            })
        }
        .onTouch(() => {
          // 第一个Scroll在用手指滑动
          this.isScroll = true;
        })
        .scrollBar(BarState.Off)
        .backgroundColor(Color.White)
        .width('90%')
        .height('50%')
        .onWillScroll(() => {
          // 判断当前Scroll是否是手指滑动，手指滑动才执行，避免scrollTo滑动时也执行该代码
          if (this.isScroll) {
            this.contentTxtOffsetY2 =
              this.scroller.currentOffset().yOffset * (this.contentTxtHeight2 - this.halfOfColumnHeight) /
                (this.contentTxtHeight - this.halfOfColumnHeight);
            console.info(`this.scroller.currentOffset().yOffset：${this.scroller.currentOffset()
              .yOffset}；this.contentTxtOffsetY2：${this.contentTxtOffsetY2.toString()}`);
            this.scroller2.scrollTo({ xOffset: 0, yOffset: this.contentTxtOffsetY2 });
          }
        });

        Scroll(this.scroller2) {
          Text(this.contentTxt2)
            .onSizeChange((oldValue: SizeOptions, newValue: SizeOptions) => {
              // 获取翻译后文本高度
              this.contentTxtHeight2 = newValue.height as number;
              console.info(`翻译后文本高度：${this.contentTxtHeight2.toString()}，oldValue：${JSON.stringify(oldValue)}`);
            })
        }
        .onTouch(() => {
          // 第二个Scroll在用手指滑动
          this.isScroll = false;
        })
        .scrollBar(BarState.Off)
        .backgroundColor('#0a59f7')
        .width('90%')
        .height('50%')
        .onWillScroll(() => {
          // 判断当前Scroll是否是手指滑动，手指滑动才执行，避免scrollTo滑动时也执行该代码
          if (!this.isScroll) {
            this.contentTxtOffsetY =
              this.scroller2.currentOffset().yOffset * (this.contentTxtHeight - this.halfOfColumnHeight) /
                (this.contentTxtHeight2 - this.halfOfColumnHeight);
            console.info(`this.scroller2.currentOffset().yOffset：${this.scroller2.currentOffset()
              .yOffset}；this.contentTxtOffsetY：${this.contentTxtOffsetY.toString()}`);
            this.scroller.scrollTo({ xOffset: 0, yOffset: this.contentTxtOffsetY });
          }
        });
      }
      .height('100%')
      .width('100%')
      .onSizeChange((oldValue: SizeOptions, newValue: SizeOptions) => {
        // 半屏高度
        this.halfOfColumnHeight = (newValue.height as number) / 2;
        console.info(`半屏高度：${this.halfOfColumnHeight.toString()}`);
        console.info(`oldColumnValue：${JSON.stringify(oldValue)}`);
      });
    }
  }
  ```

  实现效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/9p9W3YA2QPyWBDFDUJY-0g/zh-cn_image_0000002628405562.png "点击放大")

* **场景二：实现不同表格同步滚动。**

  该参考案例通过List组件与scrollTo的方式实现三个同级滚动组件的同步滚动：

  1. 先定义各个List的滚动控制器。
  2. 滚动开始执行时，onScrollFrameBegin回调方法触发，通过与期望同步的列表的控制器联动，同步X轴偏移量来实现左右两个滚动组件同步滑动，同步y轴偏移量来实现上下两个滚动组件同步滑动。

  右侧单行列表参考示例代码如下：

  ```ts
  const LeftItemWidth = 100;
  const RightItemWidth = 100;

  @Component
  struct ItemComponent {
    @Prop title: string = '';
    private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
    private scroller: Scroller = new Scroller();
    private static instance: ItemComponent;

    public static getContext(): ItemComponent {
      if (!ItemComponent.instance) {
        ItemComponent.instance = new ItemComponent();
      }
      return ItemComponent.instance;
    }

    @Builder
    RightSingleLineList() {
      List({ scroller: this.scroller }) {
        ForEach(this.arr, (item: string, index: number) => {
          ListItem() {
            Text('' + index)
              .height(100)
              .width(RightItemWidth)
              .fontSize(16)
              .textAlign(TextAlign.Start)
              .borderRadius(0)
              .padding(10)
              .backgroundColor(0xFFFFFF);
          };
        }, (item: string) => item);
      }
      .height('100%')
      .width('100%')
      .layoutWeight(1)
      .listDirection(Axis.Horizontal)
      .scrollBar(BarState.Off)
      .friction(0.6)
      .nestedScroll({
        scrollForward: NestedScrollMode.PARENT_FIRST,
        scrollBackward: NestedScrollMode.PARENT_FIRST
      })
      .divider({ strokeWidth: 0.5, color: 0xeeeeee })
      .edgeEffect(EdgeEffect.None);
    }

    build() {
      Column() {
        this.RightSingleLineList();
        Line().width('100%').height(0.5).backgroundColor(0xeeeeee);
      }.height(100);
    }
  }
  ```

  页面构建参考示例代码如下：

  ```ts
  @Entry
  @Component
  struct SceneTwo {
    private leftGroupArr: string[] = ['基本信息', '车身', '发动机'];
    private topRightArr: string[] =
      ['车型1', '车型2', '车型3', '车型4', '车型5', '车型6', '车型7', '车型8', '车型9', '车型10'];
    @State arr: string[] =
      ['车长', '车高', '内饰', '轮毂', '系统', '电机', '马力', '音响', '悬架', '座椅通风', '自动泊车', '后备箱容积',
        '座椅记忆'];
    @State rightHeaderOffset: number = 0;
    // 定义滚动控制器
    fullScroller: Scroller = new Scroller();
    hScroller: Scroller = new Scroller();
    tempScroller: Scroller = new Scroller();
    topRightScroller: Scroller = new Scroller();

    build() {
      Column() {
        this.contentBuilder();
      };
    }

    @Builder
    leftStickyHeader(title: string) {
      Column() {
        Text(title)
          .height('100%')
          .textAlign(TextAlign.Start)
          .padding(10)
          .width('100%')
          .fontSize(15)
          .fontWeight(FontWeight.Bolder);
      }.height(60).width('100%').backgroundColor(0xEEEEEE);
    }

    @Builder
    rightStickyHeader(index: number) {
      Column() {
        Text(index == 0 ? '官方配置>' : '●标配 ○选配 —无')
          .height('100%')
          .position({ x: 100 + this.rightHeaderOffset, y: 0 })
          .textAlign(TextAlign.End)
          .width(150);
      }.height(60).width('100%').backgroundColor(0xEEEEEE);
    }

    // 上侧滚动列表
    @Builder
    topFixed() {
      Row() {
        Column() {
          Text('共11款车').fontSize(15);
          Toggle({ type: ToggleType.Switch, isOn: false }).height(30).width(50);
          Text('只看差异').fontSize(15).fontWeight(FontWeight.Bolder);
        }
        .width(LeftItemWidth)
        .height(100)
        .backgroundColor(Color.White)
        .justifyContent(FlexAlign.Center)
        .alignItems(HorizontalAlign.Start)
        .padding(10);

        // 分割线
        Line().height(100).width(0.5).backgroundColor(0xeeeeee);
        // 对比列表
        List({ scroller: this.topRightScroller }) {
          ForEach(this.topRightArr, (item: string) => {
            ListItem() {
              Text(item)
                .height(100)
                .width(RightItemWidth)
                .fontSize(16)
                .textAlign(TextAlign.Start)
                .borderRadius(0)
                .padding(10)
                .backgroundColor(0xFFFFFF);
            };
          }, (item: string) => item);
        }.listDirection(Axis.Horizontal)
        .divider({ strokeWidth: 0.5, color: 0xeeeeee })
        .scrollBar(BarState.Off);
      }.height(100).width('100%').backgroundColor(Color.Pink);
    }

    // 左侧滚动列表
    @Builder
    leftList() {
      List({ scroller: this.tempScroller }) {
        ForEach(this.leftGroupArr, (item: string) => {
          ListItemGroup({ header: this.leftStickyHeader(item) }) {
            ForEach(this.arr, (item: string) => {
              ListItem() {
                Column() {
                  Text(item)
                    .width(LeftItemWidth)
                    .height('100%')
                    .fontSize(16)
                    .textAlign(TextAlign.Start)
                    .backgroundColor(0xFFFFFF)
                    .padding(10)
                    .layoutWeight(1);
                  Line().width('100%').height(0.5).backgroundColor(0xeeeeee);
                };
              }
              .height(100);
            }, (item: string) => item);
          };
        });
      }
      .sticky(StickyStyle.Header)
      .listDirection(Axis.Vertical)
      .scrollBar(BarState.Off)
      .friction(0.6)
      .divider({ strokeWidth: 0, color: 0xdddddd })
      .edgeEffect(EdgeEffect.None)
      .nestedScroll({ scrollForward: NestedScrollMode.PARENT_FIRST, scrollBackward: NestedScrollMode.PARENT_FIRST })
      .width(LeftItemWidth)
      .visibility(Visibility.Visible)
      // 滚动开始执行,与期望同步的列表的控制器联动，通过同步X轴或Y轴的偏移量来实现同步滑动
      .onScrollFrameBegin((offset: number, state: ScrollState) => {
        this.fullScroller.scrollTo({
          xOffset: 0,
          yOffset: this.tempScroller.currentOffset().yOffset + offset,
          animation: false
        });
        console.info(`liftState：${JSON.stringify(state)}`);
        return { offsetRemain: offset };
      });
    }

    // 右侧滚动列表
    @Builder
    rightScroll() {
      Scroll(this.hScroller) {
        List({ initialIndex: 0, scroller: this.fullScroller }) {
          ForEach(this.leftGroupArr, (item: string, index: number) => {
            ListItemGroup({ header: this.rightStickyHeader(index) }) {
              ForEach(this.arr, (item: string, index: number) => {
                ItemComponent({ title: this.arr[index] });
              }, (item: string) => item);
            };
          });
        }
        .sticky(StickyStyle.Header)
        .listDirection(Axis.Vertical)
        .scrollBar(BarState.Off)
        .friction(0.6)
        .edgeEffect(EdgeEffect.None)
        .width('100%')
        .nestedScroll({ scrollForward: NestedScrollMode.PARENT_FIRST, scrollBackward: NestedScrollMode.PARENT_FIRST })
        // 滚动开始执行,与期望同步的列表的控制器联动，通过同步X轴或Y轴的偏移量来实现同步滑动
        .onScrollFrameBegin((offset: number, state: ScrollState) => {
          this.tempScroller.scrollTo({
            xOffset: 0,
            yOffset: this.fullScroller.currentOffset().yOffset + offset,
            animation: false
          });
          console.info(`rightState：${JSON.stringify(state)}`);
          return { offsetRemain: offset };
        });
      }
      .position({ x: LeftItemWidth, y: 0 })
      .onWillScroll((xOffset: number, yOffset: number, scrollState: ScrollState, scrollSource: ScrollSource) => {
        console.info(`rightState：${JSON.stringify(scrollState)}，rightyOffset：${JSON.stringify(yOffset)}，rightyscrollSource：${JSON.stringify(scrollSource)}`);
        this.rightHeaderOffset = this.rightHeaderOffset + xOffset;
        this.topRightScroller.scrollTo({ xOffset: this.hScroller.currentOffset().xOffset, yOffset: 0 });
      })
      .edgeEffect(EdgeEffect.None)
      .nestedScroll({ scrollForward: NestedScrollMode.PARENT_FIRST, scrollBackward: NestedScrollMode.PARENT_FIRST })
      .width(RightItemWidth * 10 + 9 * 0.5)
      .scrollable(ScrollDirection.Horizontal)
      .backgroundColor(0xDCDCDC)
      .padding({ top: 0 });
    }

    @Builder
    contentBuilder() {
      Column() {
        this.topFixed();
        Row() {
          this.leftList();
          this.rightScroll();
          Line().height('100%').width(0.5).backgroundColor('#EEEEEE').position({ x: LeftItemWidth });
        }.justifyContent(FlexAlign.Start)
        .alignItems(VerticalAlign.Top);
      }.height('100%').justifyContent(FlexAlign.Start).alignItems(HorizontalAlign.Start);
    }
  }
  ```

  实现效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/vHos5VGDR96Lo62q_bXbIw/zh-cn_image_0000002658804835.png "点击放大")

## 常见FAQ

Q：如果滑动时卡顿掉帧可能是什么原因？

A：滑动时的回调函数如果使用onScroll()可能会导致卡顿，可以改成onScrollFrameBegin()。

## 总结

| 实现方式 | scrollToIndex | scrollTo/scrollBy |
| --- | --- | --- |
| 优点分析 | 将每一段文本分为一个ListItem，实现方式简单。 | 该方案可以将文本分段，也可以不分段整体滚动，则可以实现全文一次复制粘贴 |
| 缺点分析 | 该方式需要将文本分段切割为不同的ListItem，导致无法整体复制只能分段复制的情况。 | 该方案当文本长度不一致时需要自定义实现偏移逻辑，也就是假设文本长度比为1：2时，滚动偏移量也应符合相应的比例，否则被动滚动的组件如果长度较大将无法滚动到最底部。 |
