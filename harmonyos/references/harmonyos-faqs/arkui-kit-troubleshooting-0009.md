---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-kit-troubleshooting-0009
title: Video组件播放与显示问题定位
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 故障排查 > Video组件播放与显示问题定位
category: harmonyos-faqs
scraped_at: 2026-10-21T07:10:33+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:865e113b5a2763d450ff1a43bb078084edc3a70874fa259b7b4fb2c7f9ffe78a
---

## 平板上视频显示不全

### 问题现象

当用户在平板等不同尺寸设备上播放视频时，出现视频显示不全、画面被截断的情况。

### 定位过程

1. 检查代码中Video组件objectFit属性的内容是否为ImageFit.Cover，例如下面代码。

   ```ts
   @Entry
   @Component
   struct VideoPage {
     @State curRate: PlaybackSpeed = PlaybackSpeed.Speed_Forward_1_00_X;
     controller: VideoController = new VideoController();

     build() {
       RelativeContainer() {
         Video({
           src: $rawfile('example.mp4'),
           currentProgressRate: this.curRate,
           controller: this.controller
         })
           .width('80%')
           .height('100%')
           // 检查objectFit设置值
           .objectFit(ImageFit.Cover)
       }
       .height('100%')
       .width('100%')
     }
   }
   ```
2. 检查视频区域是否使用了固定高度值（如.height(240)），而非layoutWeight自适应填充剩余空间。
3. 检查外层容器是否缺少layoutWeight属性，导致无法占满可用空间。

### 分析结论

1. 代码中Video组件objectFit属性配置成了ImageFit.Cover，随着设备的变化，屏幕宽高比发生变化，视频播放页面的组件宽高比也随之变化，导致视频宽高比与组件宽高比不一致时，播放的视频会出现显示不全或被截断的情况。
2. 视频区域使用了固定高度值，无法根据不同窗口尺寸自适应调整，导致在不同尺寸设备上视频区域空间不足或溢出。外层容器缺少layoutWeight属性时，无法占满可用空间，也会导致视频区域被压缩。

### 修改建议

1. 将代码中Video组件的objectFit属性设置为ImageFit.Contain，保证视频完全显示的情况下自动适配屏幕。
2. 将视频区域的固定高度替换为layoutWeight(1)，使其自适应填充剩余空间。
3. 为外层容器添加layoutWeight(1)，确保占满可用空间。

修改后的示例代码如下。

```ts
@Entry
@Component
struct VideoPageDemo {
  @State curRate: PlaybackSpeed = PlaybackSpeed.Speed_Forward_1_00_X;
  controller: VideoController = new VideoController();

  build() {
    Column() {
      // 导航栏
      Text('视频播放')
        .width('100%')
        .height(50)
        .textAlign(TextAlign.Center)

      // 视频外层容器：使用layoutWeight(1)占满剩余空间
      Stack() {
        Video({
          src: \$rawfile('example.mp4'), // 实际开发替换为实际资源
          currentProgressRate: this.curRate,
          controller: this.controller
        })
          .width('100%')
          .height('100%')
          .objectFit(ImageFit.Contain)
      }
      .width('100%')
      .layoutWeight(1)
    }
    .width('100%')
    .height('100%')
  }
}
```

## 视频预览图尺寸和视频的尺寸不一致

### 问题现象

视频预览图尺寸和视频内容尺寸不一致，应该如何解决该问题？

### 定位过程

使用DevEco Testing工具查看UI结构，发现预览图是一个Image组件，显示预览图时只有Image组件，视频播放时视频播放组件覆盖了Image组件。

* 排查预览图和视频使用的填充模式，如果预览图采用contain模式，这会保持原比例，显示黑边。播放器从封面切换到视频流时，视频切换为cover或fill模式来填充容器，这会导致视频预览图尺寸和视频内容尺寸不一致。
* 排查播放容器和预览图是否设置宽高比约束（是否使用aspectRatio属性），没有设置约束的话，会导致视频预览图尺寸和视频内容尺寸不一致。

### 分析结论

使用了自行封装的视频播放组件，使用Image组件覆盖住视频播放组件作为预览图。

* 预览图和视频使用的填充模式不一致，导致视频预览图尺寸和视频内容尺寸不一致。
* 播放容器和预览图未正确设置宽高比约束，导致视频预览图尺寸和视频内容尺寸不一致。

### 修改建议

方案一：使用aspectRatio属性强制锁定图片和视频的宽高比。

```ts
@Entry
@Component
struct OptionOne {
  @State ShowVideo: boolean = false;
  ratio: number = 16 / 9; // 根据需要调整宽高比
  controller: VideoController = new VideoController();

  build() {
    Stack() {
      Image($r('app.media.preview')) // 图片
        .width('100%')
        .aspectRatio(this.ratio)
        .onClick(() => {
          this.controller.start();
        });
      Video({
        controller: this.controller,
        src: $rawfile('videoTest.mp4')
      })
        .width('100%')
        .aspectRatio(this.ratio)
        .visibility(this.ShowVideo ? Visibility.Visible : Visibility.Hidden)
        .onStart(() => {
          // 开始播放视频时显示视频组件，覆盖预览图
          this.ShowVideo = true;
        });
    };
  }
}
```

方案二：预览图推荐使用Video组件的previewUri配置项。

```ts
@Entry
@Component
struct OptionTwo {
  ratio: number = 16 / 9; // 根据需要调整宽高比
  controller: VideoController = new VideoController();

  build() {
    Stack() {
      Video({
        previewUri: $r('app.media.preview'),
        controller: this.controller,
        src: $rawfile('videoTest.mp4')
      })
        .width('100%')
        .aspectRatio(this.ratio);
    };
  }
}
```

## 折叠屏横屏观看视频画面拉伸

### 问题现象

折叠屏折叠态下，应用横屏观看视频，视频画面发生拉伸现象。

### 定位过程

目前系统提供了Video和AVPlayer两种视频播放组件。可以通过DevEco Testing或代码检查来确认使用的是哪种组件。

* Video视频组件，建议检查代码中是否设置objectFit视频显示模式为Fill模式，该模式下视频不保持宽高比，会导致画面出现拉伸。
* 若使用的是AVPlayer视频组件，此时建议检查代码VideoScaleType视频缩放模式属性的设置值，该属性设置成VIDEO\_SCALE\_TYPE\_FIT时，会将视频拉伸至与窗口等大，导致画面拉伸。
* 通常AVPlayer会搭配XComponent使用，此时建议检查代码中视频的宽高比与XComponent持有Surface的显示区域的宽高比是否一致，如果宽高比不一致，会导致画面拉伸。

### 分析结论

* Video组件视频显示模式设置不正确导致视频画面发生拉伸现象。
* AVPlayer组件视频缩放模式设置不正确导致视频画面发生拉伸现象。
* AVPlayer组件中视频的宽高比跟XComponent持有Surface的显示区域的宽高比不一致，导致画面拉伸。

### 修改建议

* 修改Video视频显示模式[objectFit](../harmonyos-references/ts-basic-components-image.md#objectfit)属性为Auto或者Contain，确保视频保持宽高比缩放。
* 在横竖屏切换时或在切换到分栏模式时，可以先用avPlayer.on('stateChange')监听视频状态变化，在监听到状态prepared时，获取视频的宽和高，并动态更改XComponent的Surface显示区域的宽高。

  ```ts
  import { media } from '@kit.MediaKit';
  import { display } from '@kit.ArkUI';

  // 1.创建视频播放器组件
  @Entry
  @Component
  struct VideoPlayerDemo {
    private avPlayer: media.AVPlayer | null = null; // AVPlayer实例
    private surfaceId: string = ''; // 播放窗口SurfaceID
    private xComponentController: XComponentController = new XComponentController();
    private videoWidth: number | undefined = 0;
    private videoHeight: number | undefined = 0;

    // 2.构建UI布局
    build() {
      Column() {
        // 视频播放窗口组件
        XComponent({
          id: "XComponent",
          type: XComponentType.SURFACE,
          controller: this.xComponentController
        })
          .onLoad(() => {
            // 获取SurfaceID并初始化播放器
            this.surfaceId = this.xComponentController.getXComponentSurfaceId();
            this.initAVPlayer();
          })
          .width('100%')
          .height('100%');
      }
      .width('100%')
      .height('100%');
    }

    // 3.初始化播放器
    async initAVPlayer() {
      try {
        // 创建AVPlayer实例
        this.avPlayer = await media.createAVPlayer();
        // 设置监听事件
        this.avPlayer.on('stateChange', async (state: string) => {
          if (state === 'initialized') {
            // 设置播放窗口
            this.avPlayer!.surfaceId = this.surfaceId;
            await this.avPlayer!.prepare();
          } else if (state === 'prepared') {
            await this.avPlayer!.play(); // 自动开始播放
            // 获取视频原始宽高
            this.videoWidth = this.avPlayer?.width;
            this.videoHeight = this.avPlayer?.height;
            this.adjustSurfaceSize();
          }
        });
        // 监听屏幕旋转
        display.on('change', () => {
          this.adjustSurfaceSize();
        });
        // 设置播放源（本地文件或网络地址）
        this.avPlayer.url = 'https://xxx.mp4'; // 替换为实际地址
      } catch (error) {
        console.error(`Player initialization failed: ${error}`);
      }
    }

    private adjustSurfaceSize() {
      if (!this.videoWidth || !this.videoHeight) {
        return;
      }
      // 获取当前屏幕方向
      const displayInfo = display.getDefaultDisplaySync();
      const isPortrait = displayInfo.width < displayInfo.height;
      // 计算保持原始比例的显示尺寸
      let displayWidth = 0;
      let displayHeight = 0;
      if (isPortrait) {
        // 竖屏模式下保持视频宽度，高度按比例计算
        displayWidth = displayInfo.width;
        displayHeight = displayWidth * this.videoHeight / this.videoWidth;
      } else {
        // 横屏模式下保持视频高度，宽度按比例计算
        displayHeight = displayInfo.height;
        displayWidth = displayHeight * this.videoWidth / this.videoHeight;
      }
      // 更新XComponent尺寸
      this.xComponentController.setXComponentSurfaceRect({
        surfaceWidth: displayWidth,
        surfaceHeight: displayHeight
      });
    }

    // 4.组件销毁时释放资源
    aboutToDisappear() {
      if (this.avPlayer) {
        this.avPlayer.release();
        this.avPlayer = null;
      }
    }
  }
  ```

## 分栏模式下观看视频画面拉伸

### 问题现象

分栏模式下，应用观看视频，视频画面发生拉伸现象。

### 定位过程

目前系统提供了Video和AVPlayer两种视频播放组件。可以通过DevEco Testing或代码检查来确认使用的是哪种组件。

* Video视频组件，建议检查代码中是否设置objectFit视频显示模式为Fill模式，该模式下视频不保持宽高比，会导致画面出现拉伸。
* 若使用的是AVPlayer视频组件，此时建议检查代码VideoScaleType视频缩放模式属性的设置值，该属性设置成VIDEO\_SCALE\_TYPE\_FIT时，会将视频拉伸至与窗口等大，导致画面拉伸。
* 通常AVPlayer会搭配XComponent使用，此时建议检查代码中视频的宽高比与XComponent持有Surface的显示区域的宽高比是否一致，如果宽高比不一致，会导致画面拉伸。

### 分析结论

* Video组件视频显示模式设置不正确导致视频画面发生拉伸现象。
* AVPlayer组件视频缩放模式设置不正确导致视频画面发生拉伸现象。
* AVPlayer组件中视频的宽高比跟XComponent持有Surface的显示区域的宽高比不一致，导致画面拉伸。

### 修改建议

* 修改Video视频显示模式[objectFit](../harmonyos-references/ts-basic-components-image.md#objectfit)属性为Auto或者Contain，确保视频保持宽高比缩放。
* 在横竖屏切换时或在切换到分栏模式时，可以先用avPlayer.on('stateChange')监听视频状态变化，在监听到状态prepared时，获取视频的宽和高，并动态更改XComponent的Surface显示区域的宽高。

  ```ts
  import { media } from '@kit.MediaKit';
  import { display } from '@kit.ArkUI';

  // 1.创建视频播放器组件
  @Entry
  @Component
  struct VideoPlayerDemo {
    private avPlayer: media.AVPlayer | null = null; // AVPlayer实例
    private surfaceId: string = ''; // 播放窗口SurfaceID
    private xComponentController: XComponentController = new XComponentController();
    private videoWidth: number | undefined = 0;
    private videoHeight: number | undefined = 0;

    // 2.构建UI布局
    build() {
      Column() {
        // 视频播放窗口组件
        XComponent({
          id: "XComponent",
          type: XComponentType.SURFACE,
          controller: this.xComponentController
        })
          .onLoad(() => {
            // 获取SurfaceID并初始化播放器
            this.surfaceId = this.xComponentController.getXComponentSurfaceId();
            this.initAVPlayer();
          })
          .width('100%')
          .height('100%');
      }
      .width('100%')
      .height('100%');
    }

    // 3.初始化播放器
    async initAVPlayer() {
      try {
        // 创建AVPlayer实例
        this.avPlayer = await media.createAVPlayer();
        // 设置监听事件
        this.avPlayer.on('stateChange', async (state: string) => {
          if (state === 'initialized') {
            // 设置播放窗口
            this.avPlayer!.surfaceId = this.surfaceId;
            await this.avPlayer!.prepare();
          } else if (state === 'prepared') {
            await this.avPlayer!.play(); // 自动开始播放
            // 获取视频原始宽高
            this.videoWidth = this.avPlayer?.width;
            this.videoHeight = this.avPlayer?.height;
            this.adjustSurfaceSize();
          }
        });
        // 监听屏幕旋转
        display.on('change', () => {
          this.adjustSurfaceSize();
        });
        // 设置播放源（本地文件或网络地址）
        this.avPlayer.url = 'https://xxx.mp4'; // 替换为实际地址
      } catch (error) {
        console.error(`Player initialization failed: ${error}`);
      }
    }

    private adjustSurfaceSize() {
      if (!this.videoWidth || !this.videoHeight) {
        return;
      }
      // 获取当前屏幕方向
      const displayInfo = display.getDefaultDisplaySync();
      const isPortrait = displayInfo.width < displayInfo.height;
      // 计算保持原始比例的显示尺寸
      let displayWidth = 0;
      let displayHeight = 0;
      if (isPortrait) {
        // 竖屏模式下保持视频宽度，高度按比例计算
        displayWidth = displayInfo.width;
        displayHeight = displayWidth * this.videoHeight / this.videoWidth;
      } else {
        // 横屏模式下保持视频高度，宽度按比例计算
        displayHeight = displayInfo.height;
        displayWidth = displayHeight * this.videoWidth / this.videoHeight;
      }
      // 更新XComponent尺寸
      this.xComponentController.setXComponentSurfaceRect({
        surfaceWidth: displayWidth,
        surfaceHeight: displayHeight
      });
    }

    // 4.组件销毁时释放资源
    aboutToDisappear() {
      if (this.avPlayer) {
        this.avPlayer.release();
        this.avPlayer = null;
      }
    }
  }
  ```

## 应用前后台切换时，如何解决Video组件播放发生中断的问题

### 问题现象

自定义的组件嵌入到主页面，在页面播放视频被切换到后台，再返回到前台时，视频播放状态异常。

### 期待效果

视频播放状态应保持连续性，即切换到后台后，视频暂停；返回前台后，视频自动恢复播放。

### 实际效果

当前视频播放状态未保持连续性，切换到后台后视频停止播放，返回前台后需要手动刷新页面才能恢复播放。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/iV3aFQD1Q3u_XtQ_Cw-ENg/zh-cn_image_0000002768130662.png "点击放大")

### 定位过程

视频播放功能需要通过VideoController的start()方法启动。因此可以排查应用在前后台切换时controller.start()方法是否被调用。

### 分析结论

播放视频需要调用controller.start()，如下代码。虽然首次进入页面时，可以通过视频准备回调**onPrepared**调用controller.start()，但是前后台切换的时候，该回调不会被触发，因此controller.start()不会被调用，所以会出现视频无法继续播放的情况。

```ts
.onPrepared(()=>{
          this.controller.start()
        })
```

### 修改建议

为了实现前后台切换能够继续播放的效果，结合UIAbility组件生命周期和@Watch和自定义组件更新，考虑在前后台切换时，对APP全局变量的值进行修改，然后通过监听APP全局变量值，以及对其进行判断，来控制视频的停止和播放。

1. 在前后台切换时，对APP里的全局变量isForeGround进行赋值或者修改。

   **代码示例如下：**

   ```ts
   onForeground():void {
       // 切到前台，设置isForeGround值为true
       console.info('onForeground-切换到前台了');
       AppStorage.setOrCreate('isForeGround', true);
     }

     onBackground():void {
       // 切到后台，设置isForeGround值为false
       console.info('onBackground-切换到后台了');
       AppStorage.setOrCreate('isForeGround', false);
     }
   ```
2. 在当前组件用Watch来监听APP全局变量。

   **代码示例如下：**

   ```ts
   //设置变量控制播控图标变化
   @State isplay: boolean = true;
   //设置变量记录播放状态
   state: boolean = true;
   //监听前后台变化
   @Watch('network') @StorageLink('isForeGround') isForeGround: boolean = false;

   network() {
     if (this.isForeGround && this.state) {
       // 切换到前台了且视频播放状态为true，视频继续播放
       this.isplay = true;
       this.controller.start();
     } else {
       // 切换到后台了，视频暂停播放
       this.state = this.isplay;
       this.isplay = false;
       this.controller.pause();
     }
   }
   ```

**完整代码示例：**

```ts
import { window } from '@kit.ArkUI';

@Entry
@Component
struct VideoControlPage {
  @State private isFullScreen: boolean = false;
  @State videoSrc: Resource = $rawfile('videoTest.mp4');
  private controller = new VideoController();
  @State currentTime: number = 0;
  @State durationTime: number = 100;
  //设置变量控制播控图标变化
  @State isplay: boolean = true;
  //设置变量记录播放状态
  state: boolean = true;
  //监听前后台变化
  @Watch('network') @StorageLink('isForeGround') isForeGround: boolean = false;

  network() {
    if (this.isForeGround && this.state) {
      // 切换到前台了且视频播放状态为true，视频继续播放
      this.isplay = true;
      this.controller.start();
    } else {
      // 切换到后台了，视频暂停播放
      this.state = this.isplay;
      this.isplay = false;
      this.controller.pause();
    }
  }

  build() {
    Stack() {
      Video({
        src: this.videoSrc,
        controller: this.controller
      })
        .width('100%')
        .height('100%')
        .loop(false)
        .controls(false)
        .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
        .onFullscreenChange((event) => {
          this.isFullScreen = event.fullscreen;
          this.changeOrientation(this.isFullScreen);
        })
        .objectFit(ImageFit.Auto)
        .onPrepared((event) => {
          this.controller.start();
          if (event) {
            this.durationTime = event.duration;
          }
        })
        .onUpdate((event) => {
          if (event) {
            this.currentTime = event.time;
          }
        });

      // 自定义的控制器
      Row() {
        Image(this.isplay ? $r('app.media.pause') : $r('app.media.play_fill'))
          .onClick(() => {
            this.isplay = !this.isplay;
            console.info('==', this.isplay);
            if (this.isplay) {
              this.controller.start();
            } else {
              this.controller.pause();
            }
          })
          .width(25)
        Row() {
          Slider({
            value: this.currentTime,
            min: 0,
            max: this.durationTime
          })
            .selectedColor('#fff')
            .trackColor('#7ff1f3f5')
            .width('100%')
            .onChange((value: number) => {
              this.controller.setCurrentTime(value); // 设置视频播放的进度跳转到value处
            })
        }
        .width(this.isFullScreen ? '80%' : '68%');

        // 展示剩余时长
        Text(`${String(Math.floor((this.currentTime / 60))).padStart(2, '0')}` + `:` +
          `${String(this.currentTime % 60).padStart(2, '0')}`)
          .textAlign(TextAlign.Center)
          .fontColor(Color.White);
        // 修改全屏控制方法，同时删除原问题代码中Video组件的onFullscreenChange判断条件
        Image(this.isFullScreen ? $r('app.media.left') : $r('app.media.right'))
          .onClick(() => {
            this.isFullScreen = !this.isFullScreen;
            this.changeOrientation(this.isFullScreen);
          })
          .width(25)
      }
      .offset({ x: 0, y: this.isFullScreen ? 170 : 100 })
      .justifyContent(FlexAlign.SpaceAround)
      .alignItems(VerticalAlign.Center)
      .width('100%')
      .padding(12)
      .zIndex(2);

    }
    .width('100%')
    .height('100%')
  }

  // 更改屏幕方向landscape为true横屏，false竖屏
  changeOrientation(landscape: boolean) {
    window.getLastWindow(this.getUIContext().getHostContext()).then((lastWindow) => {
      lastWindow.setPreferredOrientation(landscape ? window.Orientation.LANDSCAPE : window.Orientation.PORTRAIT);
    });
  }
}
```

**效果预览图：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/rGy_ewyjSrm-Q_RLWtQfog/zh-cn_image_0000002768292190.png "点击放大")
