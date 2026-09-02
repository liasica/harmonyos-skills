---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1421
title: 实现子组件适应最高子组件的高度
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 实现子组件适应最高子组件的高度
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:10+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8452ed2536ea31bc47ef5ae2756507f173534a577d8b5067c90ed06be722da79
---

## 问题现象

父组件中有多个不同高度的子组件，如何让所有子组件的高度和最高子组件高度保持一致？

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/KFaHFEnRQbWfZnraw-ugmA/zh-cn_image_0000002658843009.png "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/6lUWQwhDSbSKylDaCN3Jiw/zh-cn_image_0000002628763644.png "点击放大")

## 背景知识

* [Row组件](../harmonyos-references/ts-container-row.md)是沿水平方向布局的容器。Row未设置宽度或高度时，在主轴或交叉轴方向上自适应子组件大小。
* [onAreaChange](../harmonyos-references/ts-universal-component-area-change-event.md#onareachange)事件在组件区域变化时触发该回调。仅会响应由布局变化所导致的组件大小、位置发生变化时的回调。可以使用该组件获取组件的高度。使用方式详见：[onAreaChange示例](../harmonyos-references/ts-universal-component-area-change-event.md#示例)。
* [onSizeChange](../harmonyos-references/ts-universal-component-size-change-event.md#onsizechange)事件在组件区域变化时触发该回调。仅会响应由布局变化所导致的组件尺寸发生变化时的回调。由绘制变化所导致的渲染属性变化不会响应回调，如translate、offset。使用方式详见：[onSizeChange示例](../harmonyos-references/ts-universal-component-size-change-event.md#示例)。

## 解决方案

可以通过获取最高子组件的高度并赋予其它子组件相应的高度，实现所有子组件高度和最高子组件一致：

* 采用onAreaChange事件：
  + 方案一：通过onAreaChange的回调获取newValue的height，直接赋值。

    ```screen
    @Entry
    @Component
    struct Index {
      @State subHeight: Length = 0;

      build() {
        Column() {
          Row() {
            Column() {
              Text('我是文本1');
              Text('我是文本2');
            }
            .backgroundColor('#ff0a59f7')
            .height(this.subHeight == 0 ? 'auto' : this.subHeight);

            Column() {
              Text('我是文本1');
              Text('我是文本2');
              Text('我是文本3');
            }
            .backgroundColor('#ff96bcff')
            .height(this.subHeight == 0 ? 'auto' : this.subHeight);

            Column() {
              Text('我是文本1');
              Text('我是文本2');
              Text('我是文本3');
              Text('我是文本4');
            }
            .backgroundColor('#ffd1d1d6')
            .height(this.subHeight === 0 ? 'auto' : this.subHeight);
          }
          .backgroundColor('#ff5b5b5b')
          .onAreaChange((oldValue: Area, newValue: Area) => {
            this.subHeight = newValue.height;
          });
        }
        .width('100%')
        .padding({ top: 20 });
      }
    }
    ```
  + **方案二**：采用ForEach循环渲染，该方案将每个子组件抽象为一个类，通过优化aboutToAppear中的输入方式，方便后期开发维护。

    ```screen
    class TextClass {
      name: string[] = [];
      color: string = '';
      index: number = 0;

      constructor(name: string[], color: string, index: number) {
        this.name = name;
        this.color = color;
        this.index = index;
      }
    }

    @Entry
    @Component
    struct Index2 {
      @State textList: TextClass[] = [];
      @State subHeight: Length = 0;

      aboutToAppear(): void {
        this.textList.push(new TextClass(['我是文本1', '我是文本2'], '#ff0a59f7', 0));
        this.textList.push(new TextClass(['我是文本1', '我是文本2', '我是文本3'], '#ff96bcff', 1));
        this.textList.push(new TextClass(['我是文本1', '我是文本2', '我是文本3', '我是文本4'], '#ffd1d1d6', 2));
      }

      build() {
        Column() {
          Row() {
            ForEach(this.textList, (item: TextClass) => {
              Column() {
                ForEach(item.name, (text: string) => {
                  Text(text)
                    .fontSize('16fp');
                });
              }
              .backgroundColor(item.color)
              .height(this.subHeight === 0 ? 'auto' : this.subHeight);
            });
          }
          .backgroundColor('#ff5b5b5b')
          .onAreaChange((oldValue: Area, newValue: Area) => {
            this.subHeight = newValue.height;
          });
        }
        .width('100%')
        .padding({ top: 20 });
      }
    }
    ```

* 采用onSizeChange事件：与onAreaChange用法一致，将onAreaChange事件改为onSizeChange事件获取高度。

## 常见FAQ

Q：Flex不设置宽高，子组件会撑满Flex组件？

A：在Flex布局中，主轴方向不设置高度，默认撑满。可以设置主轴方向的高度或宽度为'auto'，Flex组件自适应子组件的高度或宽度。

## 总结

* 上面的方案适用于所有支持onAreaChange和onSizeChange通用事件的容器组件，如Column、Row、Flex等。
* onAreaChange事件与onSizeChange事件在获取组件宽高上并没有差异，onAreaChange除了能获取组件宽高外还能获取组件坐标等信息。
