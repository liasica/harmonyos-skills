---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-551
title: 切换视频时都会短暂显示暂停按钮
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 切换视频时都会短暂显示暂停按钮
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4c4f90202d34b70297c98301f91da50661bf6b682b94a5d8a6efeba8d41ea4c5
---

## 问题现象

在线短视频播放场景，用户切换视频时会短暂显示暂停按钮，影响用户观看体验。

## 背景知识

* [visibility](../harmonyos-references/ts-universal-attributes-visibility.md#visibility)：控制组件的显示或隐藏。当未设置visibility时，组件默认为显示。
* [在线短视频流畅切换](../best-practices/bpta-smooth-switching.md)：使用LazyForEach进行数据懒加载，设置cachedCount属性指定缓存数量，搭配组件复用能力以提升性能。
* [controls](../harmonyos-references/ts-media-components-video.md#controls)：设置控制视频播放的控制栏是否显示。

## 问题定位

1. 通过UIViewer工具可以发现应用通过Video组件实现了视频播放，并通过Image组件作为暂停标志进行显示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/I8i9RUpQTIiPF8KfQ4LQUQ/zh-cn_image_0000002658790895.png "点击放大")
2. 在HiLog日志中通过搜索media\_service和pause关键字发现应用多次设置pause状态，即使当前已处于pause。

   ```txt
   07-23 14:21:20.244   1471-63179    C02B2B/media_se...PlayerServer  media_service         E     #611 Can not Pause, currentState is PLAYER_PAUSED
   07-23 14:21:20.824   1471-62900    C02B2B/media_se...PlayerServer  media_service         E     #611 Can not Pause, currentState is PLAYER_PAUSED
   07-23 14:21:20.824   1471-62954    C02B2B/media_se...PlayerServer  media_service         E     #611 Can not Pause, currentState is PLAYER_PAUSED
   07-23 14:21:20.825   1471-63057    C02B2B/media_se...PlayerServer  media_service         E     #611 Can not Pause, currentState is PLAYER_PAUSED
   07-23 14:21:20.825   1471-63120    C02B2B/media_se...PlayerServer  media_service         E     #611 Can not Pause, currentState is PLAYER_PAUSED
   07-23 14:21:20.825   1471-63234    C02B2B/media_se...PlayerServer  media_service         E     #611 Can not Pause, currentState is PLAYER_PAUSED
   ```
3. 每次通过Swiper切换视频时，Video组件都会短暂进入pause状态，之后通过DoStart恢复播放。

   ```txt
   07-23 15:48:25.302   1471-53328    C02B24/media_service/TaskInner  media_service         I     [Task]:player.videodecoder Pause
   07-23 15:48:25.302   1471-53328    C02B24/media_service/TaskInner  media_service         I     [Task]:player.videodecoder Pause done.
   07-23 15:48:25.302   1471-53328    C02B22/media_s...SurfaceFilter  media_service         I     (DoPause(), 281): Pause enter.
   07-23 15:48:25.302   1471-53328    C02B3A/media_se...MediaDemuxer  media_service         I     (Pause(), 1390): In
   07-23 15:48:25.302   1471-53328    C02B22/media_service/Source     media_service         I     (Pause(), 245): Pause entered.
   07-23 15:48:25.302   1471-53328    C02B23/media_s...ce/HiStreamer  media_service         I     (Pause(), 141): Pause enter.
   07-23 15:48:25.302   1471-53328    C02B24/media_service/TaskInner  media_service         I     [Task]:DemuxV PauseAsync
   07-23 15:48:25.302   1471-53328    C02B24/media_service/TaskInner  media_service         I     [Task]:DemuxV Pause
   07-23 15:48:25.307   1471-53354    C02B22/media_s...SurfaceFilter  media_service         I     (DoStart(), 267): DoStart after pause to execute resume.
   ```

## 分析结论

应用的暂停标志根据Video的播放状态进行显示，但是由于视频切换期间视频播放状态都会进入pause，导致了暂停标志的显示。

## 修改建议

Image组件默认可视状态设置为不可视，通过isPaused变量进行控制，当Video完成视频加载时，将isPaused置为false，实现切换视频时不显示暂停标志。

完整示例参考如下：

```ts
import { AVDataSource } from './AVDataSource';

@Entry
@Component
struct AudioDemoPage {
  private swiperController: SwiperController = new SwiperController();
  private videoController: VideoController = new VideoController();
  @State isPaused: boolean = false; // 默认为播放状态
  private data: AVDataSource = new AVDataSource();

  async aboutToAppear(): Promise<void> {
    for (let i = 0; i <= 20; i++) {
      this.data.pushData($rawfile('sample-5.mp4')); // 此处请填写实际的播放资源
    }
  }

  build() {
    // Swiper轮播视频
    Swiper(this.swiperController) {
      LazyForEach(this.data, (item: Resource) => {
        Stack() {
          Video({
            src: item,
            controller: this.videoController
          })
            // 在视频准备完成后将状态需修改为播放。
            .onPrepared(() => {
              console.info(`Video prepared.`);
              this.isPaused = false;
            })
            .autoPlay(true)
            .controls(false)
          Image($r('app.media.play')) // 此处请填写实际的按钮图标地址
            .width(60)
            .height(60)
            .visibility(this.isPaused ? Visibility.Visible : Visibility.None)
        }
      }, (item: string, index: number) => JSON.stringify(item) + index)
    }
    // 配置缓存使得视频提前缓存
    .cachedCount(2)
    .width('100%')
    .height('100%')
    .vertical(true)
    .loop(true)
    .curve(Curve.Ease)
    .duration(300)
    .indicator(false)
    .backgroundColor(Color.Black)
    .onClick(() => {
      this.isPaused = !this.isPaused;
      if (this.isPaused) {
        this.videoController.pause();
      } else {
        this.videoController.start();
      }
    })
  }
}
```

AVDataSource.ets文件如下所示，跟页面放在同级文件夹下即可。

```ts
class BasicDataSource implements IDataSource {
  private listeners: DataChangeListener[] = [];
  private originDataArray: Resource[] = [];

  public totalCount(): number {
    return this.originDataArray.length;
  }

  public getData(index: number): Resource {
    return this.originDataArray[index];
  }

  // 该方法为框架侧调用，为LazyForEach组件向其数据源处添加listener监听
  registerDataChangeListener(listener: DataChangeListener): void {
    if (this.listeners.indexOf(listener) < 0) {
      console.info('add listener');
      this.listeners.push(listener);
    }
  }

  // 该方法为框架侧调用，为对应的LazyForEach组件在数据源处去除listener监听
  unregisterDataChangeListener(listener: DataChangeListener): void {
    const pos = this.listeners.indexOf(listener);
    if (pos >= 0) {
      console.info('remove listener');
      this.listeners.splice(pos, 1);
    }
  }

  // 通知LazyForEach组件需要重载所有子组件
  notifyDataReload(): void {
    this.listeners.forEach(listener => {
      listener.onDataReloaded();
    });
  }

  // 通知LazyForEach组件需要在index对应索引处添加子组件
  notifyDataAdd(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataAdd(index);
      // 写法2：listener.onDatasetChange([{type: DataOperationType.ADD, index: index}]);
    });
  }

  // 通知LazyForEach组件在index对应索引处数据有变化，需要重建该子组件
  notifyDataChange(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataChange(index);
      // 写法2：listener.onDatasetChange([{type: DataOperationType.CHANGE, index: index}]);
    });
  }

  // 通知LazyForEach组件需要在index对应索引处删除该子组件
  notifyDataDelete(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataDelete(index);
      // 写法2：listener.onDatasetChange([{type: DataOperationType.DELETE, index: index}]);
    });
  }

  // 通知LazyForEach组件将from索引和to索引处的子组件进行交换
  notifyDataMove(from: number, to: number): void {
    this.listeners.forEach(listener => {
      listener.onDataMove(from, to);
      // 写法2：listener.onDatasetChange(
      //         [{type: DataOperationType.EXCHANGE, index: {start: from, end: to}}]);
    });
  }

  notifyDatasetChange(operations: DataOperation[]): void {
    this.listeners.forEach(listener => {
      listener.onDatasetChange(operations);
    });
  }
}

export class AVDataSource extends BasicDataSource {
  private dataArray: Resource[] = [];

  public totalCount(): number {
    return this.dataArray.length;
  }

  public getData(index: number): Resource {
    return this.dataArray[index];
  }

  public pushData(data: Resource): void {
    this.dataArray.push(data);
    this.notifyDataAdd(this.dataArray.length - 1);
  }
}
```
