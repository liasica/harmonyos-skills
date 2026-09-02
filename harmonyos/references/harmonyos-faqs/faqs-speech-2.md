---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-speech-2
title: 如何解决朗读控件播放列表中加载失败的问题
breadcrumb: FAQ > AI功能开发 > 机器学习 > 场景化语音（Speech） > 如何解决朗读控件播放列表中加载失败的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:55:00+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:257585c62a3017b58195026edac19171d95497a93272b2889565dad686b5863a
---

## 问题现象

参考[官网](../harmonyos-guides/speech-textreader-guide.md)示例，实际运行时，点击朗读控件的播放列表时，会展示“加载失败”字样，如何解决该问题？

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/3I5jhM2rQYaC9BIXV7LteQ/zh-cn_image_0000002658794093.gif "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/BTWb3nfzQWyyxNY_U2CZrA/zh-cn_image_0000002628394830.gif "点击放大")

## 背景知识

* [朗读控件](../harmonyos-guides/speech-textreader-guide.md)应用广泛，例如在用户不方便或者无法查看屏幕文字的时候，为用户朗读新闻，提供资讯。
* 该控件提供[on(type: 'requestMore')](../harmonyos-references/speech-textreader-api.md#onrequestmore)请求更多文章回调函数，拉到播放列表底端或播放到文章最后一篇，触发该回调执行。

## 解决方案

案例中展示“加载失败”是由于未自定义设置请求更多文章回调函数导致的，需要补充请求更多文章回调函数，并添加空列表项即可。

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
  @State isInit: boolean = false;

  async aboutToAppear() {
    /**
     * 加载数据
     */
    let readInfoList: TextReader.ReadInfo[] = [{
      id: '001',
      title: {
        text: '水调歌头.明月几时有',
        isClickable: true
      },
      author: {
        text: '宋.苏轼',
        isClickable: true
      },
      date: {
        text: '2024/01/01',
        isClickable: false
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
      }
    };
    try {
      let context: Context | undefined = this.getUIContext().getHostContext();
      if (context) {
        await TextReader.init(context, readerParam);
        this.isInit = true;
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

    // 添加请求更多文章回调函数，并在回调函数中新增空列表项
    TextReader.on('requestMore', () => {
      console.info(`requestMore`);
      try {
        console.info(`loadMore`);
        TextReader.loadMore([], true);
      } catch (e) {
        console.error(`TextReader failed to loadMore. Code: ${e.code}, message: ${e.message}`);
      }
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
            this.setActionListener();
            await TextReader.start(this.readInfoList, this.selectedReadInfo?.id);
          } catch (err) {
            console.error(`TextReader failed to start. Code: ${err.code}, message: ${err.message}`);
          }
        });
    }
    .height('100%');
  }
}
```
