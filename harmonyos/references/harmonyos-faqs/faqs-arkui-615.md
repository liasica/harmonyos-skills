---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-615
title: 如何使bindPopup在组件上下区域不足时可以覆盖组件显示
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何使bindPopup在组件上下区域不足时可以覆盖组件显示
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:01+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:81818c1e9873f5484fdfa30f03ed75d4e59c8877e6f1f7b7e639f67535acee49
---

## 问题现象

使用bindPopup为组件A绑定Popup气泡时，当绑定的组件A上下方有区域使Popup显示时，Popup会自动优先显示在组件上方或者下方，当上下方没有区域使Popup显示时，Popup会自动显示在组件A左侧或右侧（下述示例中左侧有可用显示区域，因此Popup会自动寻找左侧空白区域显示）。希望的效果是：Popup会自动优先显示在组件A上方或者下方，当上下方无可用区域显示Popup时，Popup会覆盖在组件A上。

未实现时的效果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/ez4_hqZPTiKKcUNHOni1Qg/zh-cn_image_0000002658911943.png "点击放大")

## 背景知识

* [bindPopup](../harmonyos-references/ts-universal-attributes-popup.md#bindpopup)可以为组件绑定Popup弹窗，由自定义构建函数@Builder构建UI内容，弹出位置由系统决定，优先上下空白区域，其次左右空白区域。通过设置其参数offset可以改变Popup弹窗的偏移量并覆盖到其所绑定的组件上。
* 通过UIInspector的[createComponentObserver](../harmonyos-references/arkts-apis-uicontext-uiinspector.md#createcomponentobserver)方法可以绑定指定组件，并设置其[FrameNode](../harmonyos-references/js-apis-arkui-framenode.md)，进而获取该组件的布局信息，并通过[getPositionToWindow](../harmonyos-references/js-apis-arkui-framenode.md#getpositiontowindow12)比较Popup和组件A的布局位置。

## 解决方案

bindPopup可以使用offset参数实现偏离，当给x轴设置正数偏移量后，Popup会右移并能覆盖组件A。因此，整体思路是设置一个控制bindPopup是否使用offset的状态变量needToMove，当组件A上下方有区域供Popup显示时，needToMove为false，bindPopup不使用偏移量，当Popup只能在左侧显示时，needToMove为true，bindPopup使用偏移量向右移动覆盖组件A，同时根据点击位置调整y轴偏移量使Popup能够跟随点击位置。

偏移量示意图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/2yUp0XWxTQqzD9BypxF7Uw/zh-cn_image_0000002628392734.png "点击放大")

其中，nodeWidth为文本框宽度，popupWidth为气泡弹窗宽度，如果需要位移后的气泡弹窗能够在文本框中X方向居中，则X轴需要的偏移量为一半的气泡弹窗宽度+一半的文本框宽度；需要Y轴上出现在点击位置处，则Y轴需要的偏移量为点击处的Y坐标-气泡弹窗的Y坐标。

1. bindPopup通过needToMove决定是否使用偏移量：

   ```ts
   offset: this.needToMove ?
     { x: this.popupWidth / 2 + this.getUIContext().px2vp(this.node?.getMeasuredSize().width) / 2,
       y: this.onClick_y - this.popup_y } : { x: 0, y: 0 }
   ```
2. 获取组件A的FrameNode以便获取其布局位置信息。

   ```ts
   function once(type: 'layout', component: CustomComponent, componentId: string, callback: (node: FrameNode) => void) {
     let observer = component.getUIContext().getUIInspector().createComponentObserver(componentId);
     observer.on(type, () => {
       let node = component.getUIContext().getFrameNodeById(componentId);
       if (node) {
         callback(node);
         console.log(`componentId is`, `${componentId}`);
       }
     });
   }
   ```

   ```ts
   Row() {
     Text(this.message);
   }
   .id('text' + this.index)
   ```

   ```ts
   aboutToDisappear(): void {
     let observer = this.getUIContext().getUIInspector().createComponentObserver('text' + this.index,);
     observer.off('layout');
   }
   ```
3. 在bindPopup渲染完成并显示前，会先触发其UI内容的onAppear方法，并且在此方法中，可以通过getPositionToWindow方法获取到Popup节点和组件A节点的显示位置，如果Popup在组件A左侧，则将needToMove设为true，使得bindPopup可以通过offset使Popup覆盖在组件A上。

   这里的核心是，onAppear方法的触发时间在UI结点布局完成前，因此可以在onAppear方法使用getPositionToWindow得知Popup是否将显示在组件A左侧，getPositionToWindow方法的触发时机又在Popup真正渲染显示前，因此这时改变needToMove的值可以让Popup渲染完成时覆盖在组件A上。

   触发时机onAppear->getPositionToWindow->Popup真正渲染完成并显示。

   ```ts
   .id('popupContent')
   .constraintSize({ maxWidth: 300 })
   .onAppear(() => {
     let popupNode = this.getUIContext().getAttachedFrameNodeById('popupContent');
     if (popupNode && this.node) {
       if (popupNode.getPositionToWindow().x <= this.node.getPositionToWindow().x - this.popupWidth) {
         this.needToMove = true;
         this.popup_y = popupNode.getPositionToWindow().y;
       }
       console.info(`this.needToMove is`, `${this.needToMove}`);
     }
   })
   .onDisAppear(() => {
     this.needToMove = false;
   });
   ```

完整示例代码如下：

```ts
@Entry
@Component
struct SplitNav {
  @Provide stackPath: NavPathStack = new NavPathStack(); // 声明一个pathStack对象

  build() {
    Column() {
      Column()
        .height(1);
      // 绑定关系
      Navigation(this.stackPath) {
        Column() {
          Text('点击跳转')
            .fontSize(30)
            .fontColor(Color.Black)
            .onClick(() => {
              this.stackPath.pushPathByName('popup', null);
            });
        }
        .width('100%')
        .height('100%')
        .justifyContent(FlexAlign.Center)
        .alignItems(HorizontalAlign.Center);
      }
      .navDestination(this.getPageContent)
      .navBarWidth('50%')
      .mode(NavigationMode.Split);
    };
  }

  @Builder
  getPageContent(name: string) {
    if (name === 'popup') {
      // 渲染朋友圈组件
      Popup();
    }
  }
}

@Component
struct Popup {
  @Consume
  stackPath: NavPathStack;
  @State messageList: string[] = [
    '文本测试1',
    '文本测试2',
    '文本测试3',
    '文本测试4',
    '测试文本测试文本测试文本测试文本测试文本测试文本2222',
    '测试文本测试文本测试文本测试文本测试文本测试文本33333',
    '测试文本测试文本测试文本测试文本测试文本测试文本44444',
    '对于一个在北平住惯的人，像我，冬天要是不刮风，便觉得是奇迹;济南的冬天是没有风声的。对于一个刚由伦敦回来的人，像我，冬天要能看得见日光，便觉得是怪事;济南的冬天是响晴的。自然，在热带的地方，日光是那么毒，响亮的天气，反有点叫人害怕。可是，在北中国的冬天，而能有温晴的天气，济南真得算个宝地。\n' +
      '设假设单单是有阳光，那也算不了出奇。请闭上眼睛想:一个老城，有山有水，全在天底下晒着阳光，暖和安闲地睡着，只等春风来把它们唤醒，这是不是个理想的境界?小山整把济南围了个圈儿，只有北边缺着点口儿。这一圈小山在冬天特别可爱，好似是把济南放在一个小摇篮里，它们安静不动地低声地说:“你们放心吧，这儿准保暖和。”真的济南的人们在冬天是面上含笑的。他们一看那些小山，心中便觉得有了着落，有了依靠。他们由天上看到山上，便不知不觉地想起:“明天也许就是春天了吧?这样的温暖，今天夜里山草也许就绿起来了吧?”就是这点梦想不能一时实现，他们也并不着急，因为有这样慈善的冬天，干啥还希望别的呢!\n' +
      '最妙的是下点小雪呀看吧，山上的矮松越发的青黑，树尖上顶着一髻儿白花，好似日本看护妇。山尖全白了，给蓝天镶上一道银边。山坡上，有的地方雪厚点，有的地方草看吧，山上的矮松越发的青黑，树尖上顶着一髻儿白花，好似日本看护妇。山尖全白了，给蓝天镶上一道银边。山坡上，有的地方雪厚点，有的地方草看吧，山上的矮松越发的青黑，树尖上顶着一髻儿白花，好似日本看护妇。山尖全白了，给蓝天镶上一道银边。山坡上，有的地方雪厚点，有的地方草看吧，山上的矮松越发的青黑，树尖上顶着一髻儿白花，好似日本看护妇。山尖全白了，给蓝天镶上一道银边。山坡上，有的地方雪厚点，有的地方草看吧，山上的矮松越发的青黑，' +
      '树尖上顶着一髻儿白花，好似日本看护妇。山尖全白了，给蓝天镶上一道银边。山坡上，有的地方雪厚点，有的地方草。看吧，山上的矮松越发的青黑，树尖上顶着一髻儿白花，好似日本看护妇。山尖全白了，给蓝天镶上一道银边。山坡上，有的地方雪厚点，有的地方草色还露着;这样，一道儿白,一道儿暗黄,给山们穿上一件带水纹的花衣;看着看着，这件花衣好似被风儿吹动，叫你希望看见一点更美的山的肌肤。等到快日落的时候，微黄的阳光斜射在山腰上，那点薄雪好似突然害了羞，微微露出点粉色。就是下小雪吧，济南是受不住大雪的，那些小山太秀气!\n' +
      '古老的济南，城里那么狭窄，城外又那么宽敞，山坡上卧着些小村庄，小村庄的房顶上卧着点雪，对，这是张小水墨画，也许是唐代的名手画的吧。那水呢，不但不结冰，倒反在绿萍上冒着点热气，水藻真绿，把终年贮蓄的绿色全拿出来了。天儿越晴，水藻越绿，就凭这些绿的精神，水也不忍得冻上，况且那些长技的垂柳还要在水里照个影儿呢!看吧，由澄清的河水慢慢往上看吧，空中，半空中，天上，自上而下全是那么清亮，那么蓝汪汪的，整个的是块空灵的蓝水晶。这块水晶里，包着红屋顶，黄草山，像地毯上的小团花的小灰色树影;\n' +
      '这就是冬天的济南。',
    '测试文本测试文本测试文本测试文本测试文本测试文本1111',
    '测试文本测试文本测试文本测试文本测试文本测试文本2222',
    '测试文本测试文本测试文本测试文本测试文本测试文本33333',
    '测试文本测试文本测试文本测试文本测试文本测试文本44444',
  ];

  build() {
    NavDestination() {
      Column() {
        Scroll() {
          List({ space: 20 }) {
            ForEach(this.messageList, (item: string, index: number) => {
              ListItem() {
                MessageItem({ message: item, index: index });
              };

            }, (item: string) => JSON.stringify(item));
          };
        }
        .id('list')
        .height('100%')
        .width('100%');
      }
      .height('100%')
      .width('100%')
      .padding(20);
    };
  }
}

function once(type: 'layout', component: CustomComponent, componentId: string, callback: (node: FrameNode) => void) {
  let observer = component.getUIContext().getUIInspector().createComponentObserver(componentId);
  observer.on(type, () => {
    let node = component.getUIContext().getFrameNodeById(componentId);
    if (node) {
      callback(node);
      console.log(`componentId is`, `${componentId}`);
    }
  });
}

@Component
export struct MessageItem {
  @Prop message: string;
  @Prop index: number;
  @State popupFilterList: string[] = ['复制', '转发', '回复', '收藏', '撤回'];
  @State showPopup: boolean = false;
  private node: FrameNode | null = null;
  @State needToMove: boolean = false;
  popupWidth: number = 280;
  @State onClick_x: number = 0;
  @State popup_y: number = 0;
  @State onClick_y: number = 0;

  aboutToAppear(): void {
    once('layout', this, 'text' + this.index, (node) => {
      this.node = node;
    });
  }
  aboutToDisappear(): void {
    let observer = this.getUIContext().getUIInspector().createComponentObserver('text' + this.index,);
    observer.off('layout');
  }

  build() {
    Row() {
      Row() {
        Text(this.message);
      }
      .id('text' + this.index)
      .backgroundColor(Color.Pink)
      .bindPopup($$this.showPopup, {
        width: this.popupWidth,
        radius: 8,
        builder: this.getContent(),
        popupColor: Color.White,
        backgroundBlurStyle: BlurStyle.NONE,
        onStateChange: (event) => {
          this.showPopup = event.isVisible;
        },
        // 设置popup与目标的间隙
        targetSpace: '1vp',
        // 设置popup组件相对于目标的显示位置
        placement: Placement.Bottom,
        placementOnTop: true,
        arrowPointPosition: ArrowPointPosition.CENTER,
        keyboardAvoidMode: KeyboardAvoidMode.DEFAULT,
        offset: this.needToMove ?
          { x: this.popupWidth / 2 + this.getUIContext().px2vp(this.node?.getMeasuredSize().width) / 2,
            y: this.onClick_y - this.popup_y } : { x: 0, y: 0 }
      })

      .onClick((event) => {
        this.showPopup = true;
        this.onClick_y = event.displayY;
        this.onClick_x = event.displayX;
      });
    }
    .width('100%')
    .justifyContent(this.index % 2 === 0 ? FlexAlign.Start : FlexAlign.End);
  }

  @Builder
  getContent(): void {
    // 行：设置一行几列
    GridRow({ columns: 5, gutter: { x: 12, y: 20 } }) {
      // 列：根据一行几个进行排列位置
      ForEach(this.popupFilterList, (item: string) => {
        GridCol() {
          Column({ space: 4 }) {
            Row() {
              Text(item)
                .fontSize(15)
                .fontColor(Color.Black);
            }.width(48)
            .justifyContent(FlexAlign.Center)
            .alignItems(VerticalAlign.Center);

          }.justifyContent(FlexAlign.Center)
          .alignItems(HorizontalAlign.Center);
        }
        .onClick(() => {
        });
      }, (item: string) => JSON.stringify(item));
    }
    .id('popupContent')
    .constraintSize({ maxWidth: 300 })
    .onAppear(() => {
      let popupNode = this.getUIContext().getAttachedFrameNodeById('popupContent');
      if (popupNode && this.node) {
        if (popupNode.getPositionToWindow().x <= this.node.getPositionToWindow().x - this.popupWidth) {
          this.needToMove = true;
          this.popup_y = popupNode.getPositionToWindow().y;
        }
        console.info(`this.needToMove is`, `${this.needToMove}`);
      }
    })
    .onDisAppear(() => {
      this.needToMove = false;
    });
  }
}
```
