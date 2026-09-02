---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-speech-3
title: 如何修改TextReader控件在屏幕纵向的起始位置
breadcrumb: FAQ > AI功能开发 > 机器学习 > 场景化语音（Speech） > 如何修改TextReader控件在屏幕纵向的起始位置
category: harmonyos-faqs
scraped_at: 2026-09-02T14:55:00+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:cadbd643cd94a3a5a5da11080f34f65ad391d653608cae2f9c0ad7712b6a26d7
---

## 问题现象

[TextReader（朗读控件）](../harmonyos-references/speech-textreader-api.md)在屏幕垂直方向的位置固定，可以左右拖动，如何修改其在屏幕纵向的起始位置？

## 背景知识

TextReader：朗读控件使用AI能力将文本实时转化成语音并进行朗读，适用于一些新闻类文本内容浏览类APP，帮助用户在一些无法直接浏览文本内容的场景下，通过文本朗读来高效获取信息。

[MinibarParams](../harmonyos-references/speech-textreader-api.md#minibarparams)：用来设置Minibar初始化位置，以及与底部边框的距离。

## 解决方案

可以通过设置参数MinibarParams中的bottom的值调整朗读控件离底部边缘的距离，从而达到修改控件在屏幕纵向的起始位置的效果，示例代码如下：

```ts
import { TextReader, TextReaderIcon, ReadStateCode } from '@kit.SpeechKit';

@Entry
@Component
struct Index {

  /**
   * 待加载的文章
   */
  @State readInfoList: TextReader.ReadInfo[] = [];
  @State selectedReadInfo: TextReader.ReadInfo = this.readInfoList[0];

  /**
   * 播放状态
   */
  @State readState: ReadStateCode = ReadStateCode.WAITING;

  /**
   * 用于显示当前页的按钮状态
   */
  private isInit: boolean = false;

  async aboutToAppear() {
    /**
     * 加载数据
     */
    let readInfoList: TextReader.ReadInfo[] = [{
      id: '001',
      title: {
        text:'水调歌头.明月几时有',
        isClickable:true
      },
      author:{
        text:'宋.苏轼',
        isClickable:true
      },
      date: {
        text:'2024/01/01',
        isClickable:false
      },
      bodyInfo: '明月几时有？把酒问青天。'
    }];
    this.readInfoList = readInfoList;
    this.selectedReadInfo = this.readInfoList[0];
    this.init();
  }

  /**
   * 初始化
   */

  async init() {
    const readerParam: TextReader.ReaderParam = {
      isVoiceBrandVisible: true,
      businessBrandInfo: {
        panelName: '小艺朗读',
        panelIcon: $r('app.media.startIcon')
      },
      minibarParams:{
        defaultAlignment: 1,
        bottom: 70
      }
    };
    try {
      let context: Context | undefined = this.getUIContext().getHostContext();
      if (context) {
        await TextReader.init(context, readerParam);
        this.isInit = true;
        this.setActionListener();
      }
    } catch (err) {
      console.error(`TextReader failed to init. Code: ${err.code}, message: ${err.message}`);
    }
  }

  // 设置操作监听
  setActionListener() {
    TextReader.on('stateChange', (state: TextReader.ReadState) => {
      this.onStateChanged(state);
    });

    TextReader.on('requestMore', () => {
      TextReader.loadMore([], true);
    });
  }

  onStateChanged = (state: TextReader.ReadState) => {
    if (this.selectedReadInfo?.id === state.id) {
      this.readState = state.state;
    } else {
      this.readState = ReadStateCode.WAITING;
    }
  };

  build() {
    Column() {
      TextReaderIcon({ readState: this.readState })
        .margin({ right: 20 })
        .width(32)
        .height(32)
        .onClick(async () => {
          try {
            await TextReader.start(this.readInfoList, this.selectedReadInfo?.id);
          } catch (err) {
            console.error(`TextReader failed to start. Code: ${err.code}, message: ${err.message}`);
          }
        });
    }
    .height('100%')
  }
}
```
