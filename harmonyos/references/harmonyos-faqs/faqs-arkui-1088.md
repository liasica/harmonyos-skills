---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1088
title: 半模态弹窗常见的开发问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 半模态弹窗常见的开发问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:06+08:00
doc_updated_at: 2026-08-27
content_hash: sha256:8adcca7ff90475b03fea63196deb8e5ac27248611a978e5e60c1c75022b9457c
---

## 问题现象

* 问题一：半模态弹框bindSheet在折叠屏展开状态和平板上没有半模态的效果。
* 问题二：半模态弹窗bindSheet如何固定内容高度，禁止跟手滑动。
* 问题三：半模态弹窗如何只支持侧滑关闭。
* 问题四：bindSheet弹出的半模态弹窗中内部为列表时，列表滑动到顶后无法连续下滑关闭弹窗。

## 背景知识

* [bindSheet](../harmonyos-references/ts-universal-attributes-sheet-transition.md#bindsheet)：给组件绑定半模态页面，点击后显示模态页面。
* [SheetType](../harmonyos-references/ts-universal-attributes-sheet-transition.md#sheettype11枚举说明)：设置半模态弹窗的样式。
* [Scroll](../harmonyos-references/ts-container-scroll.md)：可滚动的容器组件，当子组件的布局尺寸超过父组件的尺寸时，内容可以滚动。
* [SheetOptions](../harmonyos-references/ts-universal-attributes-sheet-transition.md#sheetoptions)：半模态页面内容选项，可通过实现onWillDismiss方法拦截半模态关闭的行为。
* [List](../harmonyos-references/ts-container-list.md)：可滚动的容器组件，用于呈现连续的数据列表。

## 解决方案

* **解决方案一：**

  通过手动设置preferType属性为SheetType.BOTTOM即可在平板上实现底部弹窗样式，具体代码如下：

  ```ts
  @Entry
  @Component
  struct SheetTransitionExample {
    @State isShow: boolean = false;

    @Builder
    myBuilder() {
      Column() {
        Text('豫章故郡，洪都新府。星分翼轸，地接衡庐。襟三江而带五湖，控蛮荆而引瓯越。物华天宝，龙光射牛斗之墟；人杰地灵，徐孺下陈蕃之榻。雄州雾列，俊采星驰。台隍枕夷夏之交，宾主尽东南之美。都督阎公之雅望，棨戟遥临；宇文新州之懿范，襜帷暂驻。十旬休假，胜友如云；千里逢迎，高朋满座。腾蛟起凤，孟学士之词宗；紫电青霜，王将军之武库。家君作宰，路出名区；童子何知，躬逢胜饯。\n' +
          '\n' +
          '时维九月，序属三秋。潦水尽而寒潭清，烟光凝而暮山紫。俨骖騑于上路，访风景于崇阿。临帝子之长洲，得天人之旧馆。层峦耸翠，上出重霄；飞阁流丹，下临无地。鹤汀凫渚，穷岛屿之萦回；桂殿兰宫，即冈峦之体势。\n' +
          '\n' +
          '披绣闼，俯雕甍，山原旷其盈视，川泽纡其骇瞩。闾阎扑地，钟鸣鼎食之家；舸舰弥津，青雀黄龙之轴。云销雨霁，彩彻区明。落霞与孤鹜齐飞，秋水共长天一色。渔舟唱晚，响穷彭蠡之滨；雁阵惊寒，声断衡阳之浦。\n' +
          '\n' +
          '遥襟甫畅，逸兴遄飞。爽籁发而清风生，纤歌凝而白云遏。睢园绿竹，气凌彭泽之樽；邺水朱华，光照临川之笔。四美具，二难并。穷睇眄于中天，极娱游于暇日。天高地迥，觉宇宙之无穷；兴尽悲来，识盈虚之有数。望长安于日下，目吴会于云间。地势极而南溟深，天柱高而北辰远。关山难越，谁悲失路之人；萍水相逢，尽是他乡之客。怀帝阍而不见，奉宣室以何年？\n' +
          '\n' +
          '嗟乎！时运不齐，命途多舛。冯唐易老，李广难封。屈贾谊于长沙，非无圣主；窜梁鸿于海曲，岂乏明时？所赖君子见机，达人知命。老当益壮，宁移白首之心？穷且益坚，不坠青云之志。酌贪泉而觉爽，处涸辙以犹欢。北海虽赊，扶摇可接；东隅已逝，桑榆非晚。孟尝高洁，空余报国之情；阮籍猖狂，岂效穷途之哭！\n' +
          '\n' +
          '勃，三尺微命，一介书生。无路请缨，等终军之弱冠；有怀投笔，慕宗悫之长风。舍簪笏于百龄，奉晨昏于万里。非谢家之宝树，接孟氏之芳邻。他日趋庭，叨陪鲤对；今兹捧袂，喜托龙门。杨意不逢，抚凌云而自惜；钟期既遇，奏流水以何惭？\n' +
          '\n' +
          '呜乎！胜地不常，盛筵难再；兰亭已矣，梓泽丘墟。临别赠言，幸承恩于伟饯；登高作赋，是所望于群公。敢竭鄙怀，恭疏短引；一言均赋，四韵俱成。请洒潘江，各倾陆海云尔。\n' +
          '\n' +
          '滕王高阁临江渚，佩玉鸣鸾罢歌舞。\n' +
          '画栋朝飞南浦云，朱帘暮卷西山雨。\n' +
          '闲云潭影日悠悠，物换星移几度秋。\n' +
          '阁中帝子今何在？槛外长江空自流。')
          .padding({ left: 15, right: 15 });
      }
      .width('100%');
    }

    build() {
      Column() {
        Button('transition modal 1')
          .onClick(() => {
            this.isShow = true;
          })
          .fontSize(20)
          .margin(10)
          .bindSheet($$this.isShow, this.myBuilder(), {
            detents: [SheetSize.MEDIUM, SheetSize.LARGE, 200],
            blurStyle: BlurStyle.Thick,
            showClose: true,
            title: { title: '滕王阁序', subtitle: '王勃' },
            preferType: SheetType.BOTTOM,
          });
      }
      .justifyContent(FlexAlign.Start)
      .width('100%')
      .height('100%');
    }
  }
  ```

  实现效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/XaBwEq2JT8uibxCd4L9t2A/zh-cn_image_0000002719023773.png "点击放大")
* **解决方案二：**

  在bindSheet的builder外层包裹Scroll容器，利用其手势拦截机制可有效屏蔽跟手滑动。但需特别注意的是，通过SheetOptions的title属性设置的标题区域与builder处于同级布局，该区域仍会独立消费手势事件，导致拖拽标题时触发跟手滑动。因此若要实现完全禁止跟手滑动的效果，应避免设置SheetOptions的title属性，具体代码如下：

  ```ts
  @Entry
  @Component
  struct Page1 {
    @State isShow: boolean = false;
    @State sheetHeight: number = 300;

    @Builder
    myBuilder() {
      // 在bindSheet布局外层用Scroll容器，即可实现禁止跟手滑动
      Scroll() {
        Button('改变高度')
          .margin(10)
          .backgroundColor('#0a59f7')
          .fontSize(20)
          .onClick(() => {
            this.sheetHeight = 500;
          });
      }
      .width('100%')
      .height('100%');
    }

    build() {
      Column() {
        Button('打开bindsheet')
          .onClick(() => {
            this.isShow = true;
          })
          .fontSize(20)
          .margin(10)
          .bindSheet($$this.isShow, this.myBuilder(), {
            height: this.sheetHeight,
  (backgroundColor: '#f1f3f5',
            showClose: true,
          });
      }
      .justifyContent(FlexAlign.Center)
      .width('100%')
      .height('100%');
    }
  }
  ```

  实现效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/GzuLjwz8QfuybFuxi_P87Q/zh-cn_image_0000002689344852.png "点击放大")
* **解决方案三：**

  通过bindSheet的SheetOptions提供的onWillDismiss方法，拦截bindSheet的关闭原因，从而可以控制bindSheet是否关闭，具体代码如下：

  ```ts
  @Entry
  @Component
  struct bindSheetDemo {
    @State isShow: boolean = false;
    @State sheetHeight: number = 300;

    @Builder
    myBuilder() {
      Column() {
        Button('改变高度')
          .margin(10)
          .backgroundColor('#0a59f7')
          .fontSize(20)
          .onClick(() => {
            this.sheetHeight = 500;
          });
      }
      .width('100%')
      .height('100%');
    }

    build() {
      Column() {
        Button('打开bindsheet')
          .onClick(() => {
            this.isShow = true;
          })
          .fontSize(20)
          .margin(10)
          .bindSheet($$this.isShow, this.myBuilder(), {
            height: this.sheetHeight,
            backgroundColor: '#f1f3f5',
            showClose: false,
            onWillDismiss: (dismissSheetAction: DismissSheetAction) => {
              // 侧拉关闭包含侧滑（左滑/右滑）、三键back、键盘ESC关闭时关闭弹窗：
              if (dismissSheetAction.reason === DismissReason.PRESS_BACK) {
                dismissSheetAction.dismiss();
              }
            }
          });
      }
      .justifyContent(FlexAlign.Center)
      .width('100%')
      .height('100%');
    }
  }
  ```

  实现效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/cOo5It4tTc2AFstwOf1_SQ/zh-cn_image_0000002689345618.png "点击放大")
* **解决方案四：**

  列表滑动到顶后不能紧接着连续滑动关闭弹窗，是由于列表存在惯性滚动，当惯性滚动进行时，滑动手势无法交接给父组件bindSheet，因此无法连续滑动，必须等待惯性滚动消失后，bindSheet才能响应滑动。

  方式一：通过给List组件设置[nestedScroll](../harmonyos-references/ts-container-list.md#nestedscroll10)属性，开启嵌套滚动交互，使列表滑动到顶后可以连续下滑关闭弹窗，具体请参考[使用嵌套滚动交互](../harmonyos-guides/arkts-sheet-page.md#使用嵌套滚动交互)，示例代码如下：

  ```ts
  @Entry
  @Component
  struct bindSheetListDemo {
    @State isShow: boolean = false;
    @State arr: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

    @Builder
    myBuilder() {
      List() {
        ForEach(this.arr, (item: number) => {
          ListItem() {
            Text(`Item ${item}`)
              .fontSize(20)
              .margin(10);
          }
        }, (item: number) => item.toString());
      }
      .nestedScroll({
        scrollForward: NestedScrollMode.SELF_FIRST,
        scrollBackward: NestedScrollMode.SELF_FIRST
      })
      .width('100%')
      .height('100%');
    }

    build() {
      Column() {
        Button('打开bindsheet')
          .onClick(() => {
            this.isShow = true;
          })
          .fontSize(20)
          .margin(10)
          .bindSheet($$this.isShow, this.myBuilder(), {
            detents: [SheetSize.MEDIUM, SheetSize.LARGE],
            backgroundColor: '#f1f3f5',
            showClose: true,
          });
      }
      .justifyContent(FlexAlign.Center)
      .width('100%')
      .height('100%');
    }
  }
  ```

  方式二：通过禁用bindSheet的边缘回弹效果，设置effectEdge为EffectEdge.START和EffectEdge.END，也可达到目的，具体代码如下：

  ```ts
  @Entry
  @Component
  struct bindSheetListDemo2 {
    @State isShow: boolean = false;
    @State arr: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

    @Builder
    myBuilder() {
      List() {
        ForEach(this.arr, (item: number) => {
          ListItem() {
            Text(`Item ${item}`)
              .fontSize(20)
              .margin(10);
          }
        }, (item: number) => item.toString());
      }
      .width('100%')
      .height('100%');
    }

    build() {
      Column() {
        Button('打开bindsheet')
          .onClick(() => {
            this.isShow = true;
          })
          .fontSize(20)
          .margin(10)
          .bindSheet($$this.isShow, this.myBuilder(), {
            detents: [SheetSize.MEDIUM, SheetSize.LARGE],
            backgroundColor: '#f1f3f5',
            showClose: true,
            effectEdge: EffectEdge.START | EffectEdge.END,
          });
      }
      .justifyContent(FlexAlign.Center)
      .width('100%')
      .height('100%');
    }
  }
  ```

## 常见FAQ

Q：如何在bindSheet滑动改变高度的过程中刷新可视区域？

A：[ScrollSizeMode](../harmonyos-references/ts-universal-attributes-sheet-transition.md#scrollsizemode12枚举说明)是半模态面板上下滑动时的内容更新方式，给bindSheet添加ScrollSizeMode.CONTINUOUS属性即可。

Q：bindSheet设置mode为EMBEDDED时背景如何才能覆盖状态栏？

A：目前bindSheet无法做到，可以参考NavDestination的dialog模式，具体请参考[NavDestinationMode枚举说明](../harmonyos-references/ts-basic-components-navdestination.md#navdestinationmode枚举说明11)。

Q：是否可以将两个半模态绑定在同一个组件上面？

A：bindSheet给组件绑定半模态页面，点击后显示模态页面。同一个组件不能绑定两个bindSheet，需将bindSheet绑定到不同的组件上。
