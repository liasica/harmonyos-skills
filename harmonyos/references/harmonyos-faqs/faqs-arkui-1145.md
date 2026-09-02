---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1145
title: 如何实现文字高亮滚动
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现文字高亮滚动
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:20+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0d51adfa8b3eebc229036036fc0c032a81e141e9d0af06aa7672b71c979755c8
---

## 问题现象

如何实现文字逐条高亮显示，且当高亮文本超过容器布局一半高度时自动逐行向上滚动到容器底部？

## 背景知识

* [RichEditor](../harmonyos-references/ts-basic-components-richeditor.md)：支持图文混排和文本交互式编辑的组件。
* [measureTextSize](../harmonyos-references/arkts-apis-uicontext-measureutils.md#measuretextsize12)：计算指定文本单行布局下的宽度。
* [scrollBy](../harmonyos-references/ts-container-scroll.md#scrollby9)：滑动指定距离。
* [onAreaChange](../harmonyos-references/ts-universal-component-area-change-event.md#onareachange)：组件区域变化时触发该回调。

## 解决方案

实现思路如下：

1. 利用定时器定时执行高亮数据项匹配，通过updateSpanStyle属性更新索引来变化高亮文字。
2. 利用measureText计算文字宽度，累加高亮过的文字宽度，超过一屏时减去一屏宽度，使得当前行数加1。
3. 利用onAreaChange计算布局容器高度，和布局容器内显示文字的总行数。
4. 利用Scroll滚动组件的scrollBy属性进行滚动，当前行数超过布局一半高度时开始进行滚动。

完整示例参考如下：

```ts
import { display } from '@kit.ArkUI';

export class CommonConstants {
  static readonly fontSize16 = 16;
  static readonly padding16 = 16;
  static readonly margin40 = 40;
  static readonly margin36 = 36;
  static readonly space16 = 16;
  static readonly FULL_WIDTH: string = '100%';
  static readonly FULL_HEIGHT: string = '100%';
  static readonly HALF_HEIGHT: string = '50%';
}

interface TextBean {
  label: string;
  startTime: number;
  endTime: number;
}

export class Bean {
  static readonly textArray: Array<TextBean> = [];

  static init() {
    for (let i = 0; i < 100; i++) {
      let text = `我是第 ${i} 句话,`;
      Bean.textArray.push({
        label: text,
        startTime: 1000 * i,
        endTime: 1000 * i + 1000
      });
    }
  }
}

export class Timer {
  paused: boolean = false;
  timeout: number = 0;
  duration: number = 99000; // 定时任务总时长
  currentTime: number = 0;
  callback: (time: number) => void = () => {
  };

  constructor(block: (time: number) => void) {
    this.callback = block;
  }

  setTimer(): void {
    let that = this;
    this.timeout = setInterval(() => {
      if (!this.paused) {
        if (that.currentTime <= this.duration) {
          that.currentTime += 800;
          this.callback(that.currentTime);
        } else {
          that.clearTimer();
        }
      }
    }, 300);
  }

  // 暂停定时任务
  pauseInterval() {
    this.paused = true;
  }

  // 恢复定时任务
  resumeInterval() {
    this.paused = false;
  }

  // 清除计时器
  clearTimer() {
    clearInterval(this.timeout);
  }
}

@Entry
@Component
struct main {
  scroller: Scroller = new Scroller();
  controller: RichEditorController = new RichEditorController();
  timer?: Timer; // 定时任务类
  textLineHeight: number = 20; // 单行文字行高
  lines: number = 0; // 组件显示范围内文本总行数
  widthComp: number = 0; // 屏幕宽度
  heightComp: number = 0; // 组件可视文本高度
  start: number = 0; // 高亮文本开始索引
  end: number = 0; // 高亮文本结束索引
  @State currentTime: number = 0; // 定时任务执行进度
  currentTabIndex: number = 0; // 当前展示高亮数据项索引

  aboutToAppear(): void {
    // 初始化数据
    Bean.init();
    // 获取屏幕宽度
    this.widthComp = this.getUIContext().px2vp(display.getDefaultDisplaySync().width);
  }

  onPageHide(): void {
    this.timer?.pauseInterval();
  }

  onPageShow(): void {
    if (this.timer?.paused) {
      this.timer.resumeInterval();
      return;
    }

    this.start = 0;
    this.end = 0;
    let line = 0;
    let w: number = 0;

    this.timer = new Timer((time: number) => {
      this.currentTime = time;
      // 找到当前时间匹配上文本的开始时间和结束时间的数据项进行高亮
      if ((Bean.textArray[this.currentTabIndex]) &&
        this.currentTime >= Bean.textArray[this.currentTabIndex].startTime &&
        this.currentTime < Bean.textArray[this.currentTabIndex].endTime) {
        // 取消上次高亮文本
        this.controller.updateSpanStyle({
          start: this.start,
          end: this.end,
          textStyle:
          {
            fontColor: Color.Black
          }
        });

        // 更新高亮部分文本索引位置
        this.start = this.end;
        this.end += Bean.textArray[this.currentTabIndex].label.length;
        let width: number = 0;

        // 更新高亮文本
        this.controller.updateSpanStyle({
          start: this.start,
          end: this.end,
          textStyle:
          {
            fontColor: '#317AF7'
          }
        });
        // 获取高亮部分文本宽度
        this.controller.getSpans({
          start: this.start,
          end: this.end
        }).forEach(item => {
          width = this.calcTextWidth((item as RichEditorTextSpanResult).value);
        });
        this.currentTabIndex += 1;

        w = w + width;
        if (w > this.widthComp) {
          // 多出的部分设为初始值
          w = w - this.widthComp;
          line += 1;

          // 大于一半就开始滚动
          if (line > Math.floor(this.lines / 2)) {
            // 滚动单行文本行高距离
            this.scroller.scrollBy(0, this.textLineHeight);
          }
        }
      }
    });
    this.timer.setTimer();
  }

  // 计算文本宽度
  calcTextWidth(text: string): number {
    let textWidth: number = this.getUIContext().getMeasureUtils().measureText({
      textContent: text,
      fontSize: 16
    });
    return this.getUIContext().px2vp(textWidth);
  }

  build() {
    Column() {
      Row() {
        Text('文字高亮滚动：')
          .fontColor(Color.White)
          .fontSize(CommonConstants.fontSize16);
      }
      .width(CommonConstants.FULL_WIDTH)
      .padding(CommonConstants.padding16)
      .backgroundColor('#317AF7');

      Scroll(this.scroller) {
        RichEditor({ controller: this.controller })
          .onReady(() => {
            for (let i = 0; i <= Bean.textArray.length; i++) {
              this.controller.addTextSpan(Bean.textArray[i]?.label || '', {
                style: {
                  fontSize: CommonConstants.fontSize16,
                  lineHeight: this.textLineHeight,
                }
              });
            }
          })
          .padding(0)
          .hitTestBehavior(HitTestMode.None)
          .width(CommonConstants.FULL_WIDTH);
      }
      .scrollBar(BarState.Off)
      .height(CommonConstants.HALF_HEIGHT)
      .onAreaChange((_oldValue: Area, newValue: Area) => {
        this.heightComp = Number(newValue.height);
        this.lines = this.heightComp / this.textLineHeight;
      });

      Slider({
        value: $$this.currentTime,
        min: 0,
        max: this.timer?.duration,
      })
        .selectedColor('#317AF7')
        .enabled(false)
        .onChange((value: number, mode: SliderChangeMode) => {
          if (mode === SliderChangeMode.Begin || mode === SliderChangeMode.Moving) {
          }
          if (mode === SliderChangeMode.End) {
            this.currentTime = value;
            this.timer?.clearTimer();
          }
        });
    };
  }
}
```
