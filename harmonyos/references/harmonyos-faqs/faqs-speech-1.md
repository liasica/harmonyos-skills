---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-speech-1
title: 如何解决朗读控件TextReader的跳跃播放问题
breadcrumb: FAQ > AI功能开发 > 机器学习 > 场景化语音（Speech） > 如何解决朗读控件TextReader的跳跃播放问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:55:00+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:2482fb43ec7fac8ecd29044bf4a1508769dde7b9c0700d02c8214528ab947445
---

## 问题现象

朗读控件TextReader在朗读过程中，调用TextReader.setArticle()或TextReader.setArticleContent()修改列表其他数据内容，TextReader会直接跳转到最后一条数据播放。

## 背景知识

朗读控件应用广泛，例如在用户不方便或者无法查看屏幕文字的时候，为用户朗读新闻，提供资讯。

朗读控件TextReader设置内容的相关API有[TextReader.setArticle()](../harmonyos-references/speech-textreader-api.md#setarticle)和[TextReader.setArticleContent()](../harmonyos-references/speech-textreader-api.md#setarticlecontent)。

## 解决方案

根据问题的描述，由于朗读控件TextReader在修改列表其他内容时出现了，"播放内容"跳跃到最后一条数据播放的问题，推测问题与"播放内容"或"判断播放内容"的相关代码有关。需要修改相关代码，将播放内容引导回正常的播放顺序。第一步先将与"播放内容"相关的数组中最后一个对象的**bodyInfo**字段，修改为**undefined**，示例代码如下：

```ts
let readInfoList: TextReader.ReadInfo[] = [{
  id: '001',
  title: {
    text: '水调歌头 明月几时有',
    isClickable: true
  },
  author: {
    text: '苏轼',
    isClickable: true
  },
  date: {
    text: '2023/12/12',
    isClickable: false
  },
  bodyInfo: '明月几时有？把酒问青天。不知天上宫阙，今夕是何年。我欲乘风归去，又恐琼楼玉宇，高处不胜寒。起舞弄清影，何似在人间。'
}, {
  id: '002',
  title: {
    text: '水调歌头 游泳',
    isClickable: true
  },
  author: {
    text: '作者',
    isClickable: true
  },
  date: {
    text: '2023/12/12',
    isClickable: false
  },
  // 修改前：
  // bodyInfo:'水调歌头，游泳。才饮长沙水，又食武昌鱼，万里长江横渡，极目楚天舒'
  // 注意：bodyInfo修改成undefined或null
  bodyInfo: undefined
}];
```

当将bodyInfo字段设置为undefined或null时，播放到bodyInfo=undefined的TextReader.ReadInfo()时，控件会等待，同时触发TextReader.on('setArticle', (id: string) => {})回调。第二步在该回调中调用setArticle()或setArticleContent()设置bodyInfo内容，设置好就会自动播放，相关示例代码如下：

```ts
TextReader.on('setArticle', (id: string) => {
  console.info(`set article，id = ${id}`);
  setTimeout(() => {
    TextReader.setArticle({
      id: '002',
      title: {
        text: '水调歌头 游泳',
        isClickable: true
      },
      author: {
        text: '作者',
        isClickable: true
      },
      date: {
        text: '2023/12/12',
        isClickable: false
      },
      bodyInfo: '水调歌头，游泳。才饮长沙水，又食武昌鱼，万里长江横渡，极目楚天舒'
    });
  }, 1000);
});
```

连接设备后可朗读文字，完整代码如下：

```ts
import { TextReader, TextReaderIcon, ReadStateCode } from '@kit.SpeechKit';

@Entry
@Component
struct ReadText {
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
        text: '水调歌头 明月几时有',
        isClickable: true
      },
      author: {
        text: '苏轼',
        isClickable: true
      },
      date: {
        text: '2023/12/12',
        isClickable: false
      },
      bodyInfo: '明月几时有？把酒问青天。不知天上宫阙，今夕是何年。我欲乘风归去，又恐琼楼玉宇，高处不胜寒。起舞弄清影，何似在人间。'
    }, {
      id: '002',
      title: {
        text: '水调歌头 游泳',
        isClickable: true
      },
      author: {
        text: '作者',
        isClickable: true
      },
      date: {
        text: '2023/12/12',
        isClickable: false
      },
      // 修改前：
      // bodyInfo:'水调歌头，游泳。才饮长沙水，又食武昌鱼，万里长江横渡，极目楚天舒'
      // 注意：bodyInfo修改成undefined或null
      bodyInfo: undefined
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
    TextReader.on('setArticle', (id: string) => {
      console.info(`set article，id = ${id}`);
      setTimeout(() => {
        TextReader.setArticle({
          id: '002',
          title: {
            text: '水调歌头 游泳',
            isClickable: true
          },
          author: {
            text: '作者',
            isClickable: true
          },
          date: {
            text: '2023/12/12',
            isClickable: false
          },
          bodyInfo: '水调歌头，游泳。才饮长沙水，又食武昌鱼，万里长江横渡，极目楚天舒'
        });
      }, 1000);
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
            console.info(`开始朗读: ${this.readInfoList[0].bodyInfo}`);
          } catch (err) {
            console.error(`TextReader failed to start. Code: ${err.code}, message: ${err.message}`);
          }
        });
    }
    .height('100%');
  }
}
```
