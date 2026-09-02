---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-570
title: 如何实现同一行的ListItem文本高度不一致按最大高度展示
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现同一行的ListItem文本高度不一致按最大高度展示
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:01+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:299d52cf76d99459ccb50383908bc152603942e26bfbb988e7406da8651786bb
---

## 问题现象

在同一行中有多个ListItem时，ListItem中显示的文本高度不一致，导致各ListItem高度不一致，由于文本的长度不确定，无法通过设置height属性来固定ListItem的高度。

问题图预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/uIjKX91rRZOf6R2uDe8LVQ/zh-cn_image_0000002628392150.png "点击放大")

## 背景知识

* [List组件](../harmonyos-references/ts-container-list.md)为列表组件，包含相同宽度的列表项，适合连续、多行呈现同类数据，可通过属性设置为多列。可以通过[onAreaChange](../harmonyos-references/ts-universal-component-area-change-event.md#onareachange)获取各ListItem的组件区域变化前后的值，如组件高度。
* [Flex组件](../harmonyos-references/ts-container-flex.md)为弹性容器组件，可通过修改[FlexOptions](../harmonyos-references/ts-container-flex.md#flexoptions对象说明)的wrap和alignItems的参数，配合子组件的宽度，设置子组件多行多列显示，实现与List、Grid相似的布局。

## 解决方案

* **方案一**：使用Flex容器组件，修改FlexOptions的wrap和alignItems的参数，实现多行多列显示，且子组件在交叉轴方向拉伸填充。示例代码如下：

  ```ts
  import { LengthUnit } from '@kit.ArkUI';

  export class Area {
    name: string = '';
    heightSize: number = 0;

    constructor(name: string) {
      this.name = name;
    }
  }

  const ARR: Area[] = [
    new Area('铜梁区'), new Area('潼南区'), new Area('荣昌区'), new Area('开州区'), new Area('梁平区'),
    new Area('石柱土家族自治县'),
    new Area('秀山土家族苗族自治县kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk'),
    new Area('酉阳土家族苗族自治县'), new Area('彭水苗族土家族自治县'),
    new Area('铜梁区'), new Area('潼南区'), new Area('荣昌区'), new Area('开州区'), new Area('梁平区'),
    new Area('石柱土家族自治县'),
    new Area('秀山土家族苗族自治县kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk'),
    new Area('酉阳土家族苗族自治县'), new Area('彭水苗族土家族自治县'),
    new Area('铜梁区'), new Area('潼南区'), new Area('荣昌区'), new Area('开州区'), new Area('梁平区'),
    new Area('石柱土家族自治县'),
    new Area('秀山土家族苗族自治县kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk'),
    new Area('酉阳土家族苗族自治县'), new Area('彭水苗族土家族自治县'),
  ];

  // 元素子组件
  @Component
  struct TextComponentOne {
    content: string = '';

    build() {
      Column() {
        Text(this.content)
          .fontSize(14)
          .padding(9)
          .width(this.content.length >= 9 ? '100%' : null)
          .textAlign(this.content.length >= 9 ? TextAlign.Start : TextAlign.Center);
      };
    }
  }

  @Entry
  @Component
  struct Index {
    private arr: Area[] = ARR;

    build() {
      Scroll() {
        Flex({
          justifyContent: FlexAlign.Center,
          wrap: FlexWrap.Wrap, // Flex容器的元素多行/列排布
          alignItems: ItemAlign.Stretch, // 元素在Flex容器中，交叉轴方向拉伸填充
          space: {
            cross: { value: 0, unit: LengthUnit.VP }
          }
        }) {
          ForEach(this.arr, (item: Area) => {
            Column() {
              TextComponentOne({ content: item.name });
            }
            // 格式、宽度、圆角等属性需在Flex元素设置，若设置在元素子组件内，交叉轴防线拉伸填充可能不生效
            .justifyContent(item.name.length >= 9 ? FlexAlign.Start : FlexAlign.Center)
            .width('30%')
            .border({ width: 0, radius: 7 })
            .backgroundColor('#ffe5e5e5')
            .margin({
              bottom: 5,
              top: 5,
              right: 3,
              left: 3
            });
          });
        };
      }
      .width('100%');
    }
  }
  ```

  修正效果图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/mQr62QeMS0mLmPQLtmohnw/zh-cn_image_0000002658791433.png "点击放大")
* **方案二**：通过onAreaChange获取各ListItem高度并判断行内最大高度，通过状态变量变化和if/else条件语句，刷新页面布局，将组件高度设置为行内最大高度。
  1. 计算每个ListItem的高度，并判断同一行中所有ListItem的最大高度。

     ```ts
     // 判断行内高度的最大值，并将arr中的元素的高度设置为高度最大值
     reSetHeightSize() {
       for (let i = 0; i < this.arr.length; i += 3) {
         let arrTmp: number[] = [];
         arrTmp.push(this.arr[i].heightSize);
         arrTmp.push(this.arr[i + 1].heightSize);
         arrTmp.push(this.arr[i + 2].heightSize);
         arrTmp.sort((a, b) => a - b);
         let maxHeight = Math.max(...arrTmp);
         this.arr[i].heightSize = maxHeight;
         this.arr[i + 1].heightSize = maxHeight;
         this.arr[i + 2].heightSize = maxHeight;
       }
     }
     ```
  2. 首次布局时，通过onAreaChange收集并计算ListItem高度。

     ```ts
     @Builder
     ListItemChangeRegion() {
       List({ space: 8 }) {
         ForEach(this.arr, (item: RegionOne, index: number) => {
           ListItem() {
             TextComponentTwo({ content: item.name })
               .onAreaChange((oldValue: Area, newValue: Area) => {
                 // 遍历全部ListItem并收集高度后，调用reSetHeightSize方法计算各行的最大高度，并再完成遍历后改变状态变量isBoolean的值，UI渲染改变
                 this.arr[index].heightSize = newValue.height as number;
                 if (this.flags === this.arr.length - 1) {
                   this.isBoolean = false;
                   this.reSetHeightSize();
                 }
                 this.flags += 1;
                 console.info(`Ace: on area change, oldValue is ${JSON.stringify(oldValue)} value is ${JSON.stringify(newValue)}`);
               });
           };
         });
       }
       .lanes(3);
     }
     ```
  3. 二次布局时，设置组件高度为行内最大高度。

     ```ts
     @Builder
     ListItemSameHeight() {
       List({ space: 8 }) {
         ForEach(this.arr, (item: RegionOne, index: number) => {
           ListItem() {
             TextComponentTwo({ content: item.name, hgt: item.heightSize, index: index });
           };
         }, (item: RegionOne) => JSON.stringify(item));
       }
       .lanes(3);
     }
     ```
  4. 使用条件语句if和状态变量isBoolean，通过判断状态变量的值的变化，重新对布局进行刷新。

     ```ts
     if (this.isBoolean) {
       // 首次布局，组件区域变化触发onRegionOneChange回调，收集并计算ListItem高度
       this.ListItemChangeRegion();
     } else {
       // isBoolean值发生改变，重新布局进入else语句，此时，各ListItem的高度已是行内的最大高度值
       this.ListItemSameHeight();
     }
     ```

  完整示例参考如下：

  ```ts
  class RegionOne {
    name: string = '';
    heightSize: number = 0;

    constructor(name: string) {
      this.name = name;
    }
  }

  const ARR: RegionOne[] = [
    new RegionOne('铜梁区'), new RegionOne('潼南区'), new RegionOne('荣昌区'), new RegionOne('开州区'),
    new RegionOne('梁平区'),
    new RegionOne('石柱土家族自治县'),
    new RegionOne('秀山土家族苗族自治县kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk'),
    new RegionOne('酉阳土家族苗族自治县'), new RegionOne('彭水苗族土家族自治县'),
    new RegionOne('铜梁区'), new RegionOne('潼南区'), new RegionOne('荣昌区'), new RegionOne('开州区'),
    new RegionOne('梁平区'),
    new RegionOne('石柱土家族自治县'),
    new RegionOne('秀山土家族苗族自治县kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk'),
    new RegionOne('酉阳土家族苗族自治县'), new RegionOne('彭水苗族土家族自治县'),
    new RegionOne('铜梁区'), new RegionOne('潼南区'), new RegionOne('荣昌区'), new RegionOne('开州区'),
    new RegionOne('梁平区'),
    new RegionOne('石柱土家族自治县'),
    new RegionOne('秀山土家族苗族自治县kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk'),
    new RegionOne('酉阳土家族苗族自治县'), new RegionOne('彭水苗族土家族自治县'),
  ];

  // 元素子组件
  @Component
  struct TextComponentTwo {
    content: string = '';
    hgt: Length = 'auto';
    index: number = 0;

    build() {
      Column() {
        Text(this.content)
          .zIndex(this.index)
          .fontSize(14)
          .padding(9)
          .width(115)
          .textAlign(this.content.length >= 9 ? TextAlign.Start : TextAlign.Center);
      }
      .height(this.hgt)
      .backgroundColor('#ffe5e5e5')
      .justifyContent(this.content.length >= 9 ? FlexAlign.Start : FlexAlign.Center)
      .border({
        width: 0,
        radius: 7
      });
    }
  }

  @Entry
  @Component
  struct Page {
    private arr: RegionOne[] = ARR;
    private flags: number = 0;
    @State private isBoolean: boolean = true;

    // 判断行内高度的最大值，并将arr中的元素的高度设置为高度最大值
    reSetHeightSize() {
      for (let i = 0; i < this.arr.length; i += 3) {
        let arrTmp: number[] = [];
        arrTmp.push(this.arr[i].heightSize);
        arrTmp.push(this.arr[i + 1].heightSize);
        arrTmp.push(this.arr[i + 2].heightSize);
        arrTmp.sort((a, b) => a - b);
        let maxHeight = Math.max(...arrTmp);
        this.arr[i].heightSize = maxHeight;
        this.arr[i + 1].heightSize = maxHeight;
        this.arr[i + 2].heightSize = maxHeight;
      }
    }

    @Builder
    ListItemChangeRegion() {
      List({ space: 8 }) {
        ForEach(this.arr, (item: RegionOne, index: number) => {
          ListItem() {
            TextComponentTwo({ content: item.name })
              .onAreaChange((oldValue: Area, newValue: Area) => {
                // 遍历全部ListItem并收集高度后，调用reSetHeightSize方法计算各行的最大高度，并再完成遍历后改变状态变量isBoolean的值，UI渲染改变
                this.arr[index].heightSize = newValue.height as number;
                if (this.flags === this.arr.length - 1) {
                  this.isBoolean = false;
                  this.reSetHeightSize();
                }
                this.flags += 1;
                console.info(`Ace: on area change, oldValue is ${JSON.stringify(oldValue)} value is ${JSON.stringify(newValue)}`);
              });
          };
        });
      }
      .lanes(3);
    }

    @Builder
    ListItemSameHeight() {
      List({ space: 8 }) {
        ForEach(this.arr, (item: RegionOne, index: number) => {
          ListItem() {
            TextComponentTwo({ content: item.name, hgt: item.heightSize, index: index });
          };
        }, (item: RegionOne) => JSON.stringify(item));
      }
      .lanes(3);
    }

    build() {
      Column() {
        if (this.isBoolean) {
          // 首次布局，组件区域变化触发onRegionOneChange回调，收集并计算ListItem高度
          this.ListItemChangeRegion();
        } else {
          // isBoolean值发生改变，重新布局进入else语句，此时，各ListItem的高度已是行内的最大高度值
          this.ListItemSameHeight();
        }
      }
      .width('100%')
      .height('100%')
      .padding({ top: 5, left: 12, right: 6 });
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/mYNezj4ERNOZvcRnuZJ2wg/zh-cn_image_0000002628552046.png "点击放大")

## 总结

* 行内各元素高度不同，要使元素高度按行内最大高度展示，推荐使用Flex容器组件，通过改变wrap和alignItems的参数，配合设置元素宽度实现。
* 若场景需要使用List组件，则可以通过onAreaChange获取组件高度，自定义方法判断和记录行内组件最大高度，并改变状态变量的值触发UI渲染改变，将组件的高度设置为行内组件的最大高度。当元素数量较多时，此方案可能出现性能问题。
