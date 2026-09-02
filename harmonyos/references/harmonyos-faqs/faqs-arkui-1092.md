---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1092
title: 如何实现Flex分页展示的功能
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现Flex分页展示的功能
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:27+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:81363d71a2716e3c0a9ad774807617268e7dff6fecd93a189205e36128da1459
---

## 问题现象

如何实现Flex布局每超过两行自动分页，并能够像Swiper容器一样能左右滑动？

参考图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/Fh3wUeMkSSWWXKYvhb9cjg/zh-cn_image_0000002658926573.png "点击放大")

## 背景知识

* [Flex](../harmonyos-references/ts-container-flex.md)是以弹性方式布局子组件的容器组件，能够高效地排列、对齐子元素并分配剩余空间。
* [Swiper](../harmonyos-references/ts-container-swiper.md)滑块视图容器，提供子组件滑动轮播显示的能力。
* [Window](../harmonyos-references/arkts-apis-window-window.md)当前窗口实例，窗口管理器管理的基本单元。[getWindowProperties](../harmonyos-references/arkts-apis-window-window.md#getwindowproperties9)方法可以获取窗口属性，得到窗口宽度。
* [MeasureUtils对象](../harmonyos-references/arkts-apis-uicontext-measureutils.md)提供文本宽度、高度等相关计算。[measureText](../harmonyos-references/arkts-apis-uicontext-measureutils.md#measuretext12)计算指定文本单行布局下的宽度，得到的值单位为px，可以通过[px2vp](../harmonyos-references/arkts-apis-uicontext-uicontext.md#px2vp12)方法转化为vp单位。

## 解决方案

通过Swiper组件和Flex布局组件可以实现分页展示多个文本框的功能，步骤如下：

1. 获取当前窗口对象，得到窗口宽度。通过当前窗口宽度计算单行的可用宽度。
2. 遍历需要展示在文本框中的字符串数组，通过measureText方法和文本框属性计算文本框占用的宽度。
3. 根据当前每行可用宽度和文本框占用的宽度进行计算。当前行可用宽度-文本框占用宽度-Flex布局中的组件间距，如果小于0就进行换行，并记录每个文本框所在的行。
4. 由于当前每页需要展示两行，通过最大行数/2计算出需要的总页数。最后用记录的文本框所在行判断展示在对应的Swiper页。

实现代码如下：

```ts
import { LengthMetrics, MeasureUtils, UIContext, window } from '@kit.ArkUI';

class TextInfo {
  text: string = '';
  width: number = 0; // 文本框占用的宽
  line: number = 0; // 原本文本框所在行
  remainWidth: number = 0; // 添加文本框后本行剩下的宽

  constructor(text: string, width: number, line: number, remainWidth: number) {
    this.text = text;
    this.width = width;
    this.line = line;
    this.remainWidth = remainWidth;
  }
}

@Component
struct TextItem {
  @Prop text: string;

  build() {
    Text(this.text)
      .textAlign(TextAlign.Center)
      .maxLines(1)
      .padding({
        left: 4,
        right: 4,
        top: 5,
        bottom: 5
      })
      .constraintSize({ minWidth: 70 }) // 文本框的最小宽度
      .border({ width: 1, color: '#ffececec' })
      .borderRadius(5);
  }
}

@Entry
@Component
struct FlexPage {
  uiContext: UIContext = this.getUIContext();
  measureUtils: MeasureUtils = this.uiContext.getMeasureUtils();
  lineWidth: number = 0; // 每行的可用宽度，aboutToAppear中获取
  allData: string[] =
    ['1234567', '2222222', '333', '44444', '555555', '666', '7777', '88888888888', '99', '3434', '5656', '7878',
      '12131415', '68681', '7777', '8888888888888', '99', '3434', '5656', '7878', '141414141', '68681'];
  textInfos: TextInfo[] = []; // 文本框信息
  maxLine: number = 0; // 文本框原本能占用的最大行数
  @State swiperList: TextInfo[][] = []; // 轮播图数据

  getTextInfos() {
    let line = 1;
    let remainWidth = this.lineWidth + 5; // +5是因为首行添加第一个文本框不会出现间距，方便后面计算
    this.allData.forEach((str) => {
      // 文字占用的宽度，单位px
      let value = this.measureUtils.measureText({
        textContent: str,
        fontSize: '16fp'
      });
      // 文本框占用的宽度
      let width = this.uiContext.px2vp(value) + 10;
      if (width <= 70) {
        if (remainWidth - 70 - 5 >= 0) { // 本行是否能放下当前文本框
          remainWidth = remainWidth - 70 - 5; // 计算剩余宽度，减去文本框宽度和间距
          this.textInfos.push(new TextInfo(str, 70, line, remainWidth));
        } else {
          line++; // 换行
          remainWidth = this.lineWidth - 70;
          this.textInfos.push(new TextInfo(str, 70, line, remainWidth));
        }
      } else {
        if (remainWidth - width - 5 >= 0) {
          remainWidth = remainWidth - width - 5;
          this.textInfos.push(new TextInfo(str, width, line, remainWidth));
        } else {
          remainWidth = this.lineWidth - width;
          line++; // 换行
          this.textInfos.push(new TextInfo(str, width, line, remainWidth));
        }
      }
    });
    console.info(JSON.stringify(this.textInfos));
    this.maxLine = line; // 得到原本能占用的最大行数
  }

  getSwiperList() {
    let maxIndex = Math.ceil(this.maxLine / 2); // 轮播图需要的页数
    for (let index = 1; index <= maxIndex; index++) {
      this.swiperList[index - 1] = this.textInfos.filter((item: TextInfo) => {
        return item.line === index * 2 - 1 || item.line === index * 2;
      });
    }
    console.info(JSON.stringify(this.swiperList));
  }

  aboutToAppear(): void {
    window.getLastWindow(this.uiContext.getHostContext()).then((win) => {
      let winWidth = win.getWindowProperties().windowRect.width;
      // 计算行宽，40是因为左右内边距20
      this.lineWidth = this.uiContext.px2vp(winWidth) - 40 > 0 ? this.uiContext.px2vp(winWidth) - 40 : 320;
      console.info(`每行可用宽度：${this.lineWidth}`);
      this.getTextInfos(); // 获取文本框信息
      this.getSwiperList(); // 获取轮播图页数
    });
  }

  build() {
    Column() {
      Swiper() {
        ForEach(this.swiperList, (textItems: TextInfo[]) => {
          Flex({
            wrap: FlexWrap.Wrap,
            space: {
              main: LengthMetrics.vp(5),
              cross: LengthMetrics.vp(15)
            }
          }) {
            ForEach(textItems, (item: TextInfo) => {
              TextItem({ text: item.text });
            });
          }
          .height(120);
        });
      }
      .width('100%')
      .padding({ left: 20, right: 20 })
      .loop(false)
      .indicator(
        Indicator.dot()
          .selectedItemWidth(6)
      );
    }
    .width('100%')
    .height('100%');
  }
}
```

效果图展示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/aizTYZ-lTWSTO2TlA-oWfA/zh-cn_image_0000002658806631.png "点击放大")

## 常见FAQ

Q：如何获取Flex组件中元素的相关信息？

A：可以通过[getRectangleById](../harmonyos-references/arkts-apis-uicontext-componentutils.md#getrectanglebyid)方法获取组件大小、位置等属性信息。
