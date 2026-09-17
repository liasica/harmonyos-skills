---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/speech-textreadericonv2
title: TextReaderIconV2（朗读听筒图标）
breadcrumb: API参考 > AI > Speech Kit（场景化语音服务） > ArkTS组件 > TextReaderIconV2（朗读听筒图标）
category: harmonyos-references
scraped_at: 2026-09-18T06:52:22+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:401f48ca0d7bd23167f3014440a0f4a126e1aa2fee3cc582cb0528afa877677c
---

朗读听筒图标，可以作为动态组件加载，并配置成为播放面板的主入口。

在应用使用ArkTS的[状态管理V1装饰器](../harmonyos-guides/arkts-state-management-v1.md)时，需要通过[TextReaderIcon](speech-textreadericon.md)组件接口拉起朗读听筒图标；在应用使用[状态管理V2装饰器](../harmonyos-guides/arkts-state-management-v2.md)时，需要通过TextReaderIconV2组件接口拉起朗读听筒图标。

**起始版本：** 6.1.1(24)

## 导入模块

```typescript
import { TextReaderIconV2, UpReadState } from '@kit.SpeechKit';
```

## UpReadState

type UpReadState = (readState:ReadStateCode)=>void

用于听筒图标组件触发父组件状态更新的回调函数。

**元服务API：** 从版本6.1.1(24)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 6.1.1(24)

**参数：**

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| readState | [ReadStateCode](speech-readstatecode.md) | 是 | 播报状态。 |

## TextReaderIconV2

朗读听筒图标，可以作为动态组件加载。设置onClick回调，在用户点击听筒图标时启动朗读控件。

**装饰器类型：** @ComponentV2

**元服务API：** 从版本6.1.1(24)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 6.1.1(24)

**参数：**

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| readState | [ReadStateCode](speech-readstatecode.md) | 是 | @Param | 播报状态。  **说明：**  readState使用[@Param装饰器：父子单向同步](../harmonyos-guides/arkts-new-param.md)。 |
| upReadState | [UpReadState](speech-textreadericonv2.md#upreadstate) | 是 | @Event | 回调函数，更新播报状态。  **说明：**  upReadState使用[@Event装饰器：子组件通过回调函数触发父组件状态更新](../harmonyos-guides/arkts-new-event.md)。 |

### build

build(): void

用于创建[TextReaderIconV2](speech-textreadericonv2.md#textreadericonv2)对象的构造函数。

**元服务API：** 从版本6.1.1(24)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.TextReader

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 6.1.1(24)

**示例：**

```typescript
import  {TextReader,ReadStateCode,TextReaderIconV2, UpReadState} from '@kit.SpeechKit'

@Entry
@ComponentV2
struct Index {

  /**
   * 待加载的文章
   */
  @Local readInfoList: TextReader.ReadInfo[] = [];
  @Local selectedReadInfo: TextReader.ReadInfo = this.readInfoList[0];

  /**
   * 播放状态
   */
  @Local readState: ReadStateCode = ReadStateCode.WAITING;

  /**
   * 初始化状态
   */
  @Local isInit: boolean = false;

  async aboutToAppear(){
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
    await this.init();
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
      let context: Context | undefined = this.getUIContext().getHostContext()
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
  
  updateReadState: UpReadState = (readState: ReadStateCode) => {
    this.readState = readState
    console.info(`TextReader new readState:${readState}`)
  }

  build() {
    Column() {
      TextReaderIconV2({ readState: this.readState,upReadState:this.updateReadState})
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
        })
    }
    .height('100%')
  }
}
```

组件如下图：

静止状态

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/9iHAnO4dTH2XWAUrWMwO9A/zh-cn_image_0000002757313499.png)

播放状态

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/BOKyFvfhSPSzbYDmmivUBg/zh-cn_image_0000002757233619.png)
