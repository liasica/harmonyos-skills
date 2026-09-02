---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-655
title: 进入/退出全屏时，弹幕字体大小变化后才旋转屏幕
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 进入/退出全屏时，弹幕字体大小变化后才旋转屏幕
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:02+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:bb785fa5d1b958eda7c333ccb9db0ec4193c75ec9248256f06207c7ee5ac0def
---

## 问题现象

播放视频时，进入横向全屏前弹幕字体会突然变大，退出横向全屏前弹幕字体会突然变小。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/kCBFcS-LQ6q1FWSoETMBGA/zh-cn_image_0000002658913731.png "点击放大")

## 背景知识

* [setPreferredOrientation](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)可设置主窗口的显示方向属性，使用callback异步回调。
* 基于[setInterval](../harmonyos-references/js-apis-timer.md#setinterval)函数和[translate](../harmonyos-references/ts-page-transition-animation.md#translate)属性可实现弹幕移动动画。
* 设置[onAreaChange](../harmonyos-references/ts-universal-component-area-change-event.md#onareachange)，组件区域变化时触发该回调。仅会响应由布局变化所导致的组件大小、位置发生变化时的回调。

## 问题定位

全局搜索setPreferredOrientation，查看进入和退出横向全屏时的设置，应用在更改屏幕方向时更改了弹幕的字号。setPreferredOrientation更改屏幕方向时有延迟，导致出现弹幕字体大小变化后才旋转屏幕的现象。

```typescript
import { common } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

@Entry
@Component
struct VideoPlayer {
  @State @Watch('changeOrientation') isFull: boolean = false; // 是否全屏
  @Provide('commentFontSize') myFontSize: number = 14; // 设置弹幕字体大小

  changeOrientation() {
    let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
    window.getLastWindow(context).then((lastWindow) => {
      // 设置横/竖屏
      lastWindow.setPreferredOrientation(this.isFull ? window.Orientation.LANDSCAPE :
        window.Orientation.PORTRAIT);
      this.myFontSize = this.isFull ? 22 : 14; // 进入/退出全屏时更改字体大小
    });
  }
}

// 弹幕组件
@Component
export struct BulletCommentView {
  @Consume('commentFontSize') myFontSize: number; // 设置弹幕字体大小

  build() {
    Stack() {
      if (this.showBulletComment) {
        ForEach(this.bulletComments, (item: BulletCommentItem) => {
          if (item.isUserBulletComment) {
            Text(item.content)
              .fontSize(this.myFontSize);

          } else {
            Text(item.content)
              .fontSize(this.myFontSize);
          }
        });
      }
    }
    .width('100%')
    .height('100%');
  }
}
```

## 分析结论

应用在更改屏幕方向时更改了弹幕的字号，而且setPreferredOrientation更改屏幕方向时有延迟，导致出现弹幕字体大小变化后才旋转屏幕的现象。

## 修改建议

对视频组件添加onAreaChange，在横竖屏切换组件区域变化时更改弹幕字体大小。

关键部分：

```typescript
Video({
  src: this.videoSrc,
  controller: this.controller
})
// 横竖屏切换组件区域变化时更改弹幕字体大小
  .onAreaChange((oldValue, newValue) => {
    console.info(oldValue.width.toString());
    if (newValue.width > newValue.height) {
      this.myFontSize = 22;
    } else {
      this.myFontSize = 14;
    }
  })
```

完整示例：

```typescript
import { util } from '@kit.ArkTS';
import { common } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

interface VideoPreparedEvent {
  duration: number;
}

interface VideoUpdateEvent {
  time: number;
}

@Component
export struct BulletCommentView {
  @State forceUpdate: boolean = false; // 强制刷新用
  @Link bulletComments: BulletCommentItem[];
  @Link isPlaying: boolean;
  @Link showBulletComment: boolean;
  private timerId: number = 0;
  @Consume('commentFontSize') myFontSize: number;

  aboutToAppear() {
    this.startAnimation();
  }

  aboutToDisappear() {
    clearInterval(this.timerId);
  }

  build() {
    Stack() {
      if (this.showBulletComment) {
        ForEach(this.bulletComments, (item: BulletCommentItem) => {
          if (item.isUserBulletComment) {
            Text(item.content)
              .fontSize(this.myFontSize)
              .fontColor(item.color)
              .translate({ x: `${item.translateX}vp`, y: 0 })
              .position({ y: `${item.positionY}%` })
              .backgroundColor('rgba(0, 0, 0, 0.4)')// 半透明背景
              .borderRadius(999)
              .padding({
                top: 4,
                left: 8,
                bottom: 4,
                right: 8
              })
              .borderWidth(1)
              .borderColor('rgba(255, 255, 255, 0.6)')
              .key(item.id.toString());
          } else {
            Text(item.content)
              .fontSize(this.myFontSize)
              .fontColor(item.color)
              .translate({ x: `${item.translateX}vp`, y: 0 })
              .position({ y: `${item.positionY}%` })
              .backgroundColor('rgba(0, 0, 0, 0.4)')
              .borderRadius(999)
              .padding({
                top: 4,
                left: 8,
                bottom: 4,
                right: 8
              })
              .key(item.id.toString());
          }
        });
      }
      // 隐藏的刷新触发器
      Text(this.forceUpdate ? ' ' : '  ')
        .size({ width: 0, height: 0 });
    }
    .width('100%')
    .height('100%');
  }

  // 启动弹幕动画
  private startAnimation() {
    // 清除已有定时器
    if (this.timerId) {
      clearInterval(this.timerId);
    }
    // 使用setInterval实现动画
    this.timerId = setInterval(() => {
      if (!this.isPlaying) {
        return;
      }
      let needsUpdate = false;
      // 更新所有弹幕位置
      this.bulletComments.forEach(item => {
        const NEWX = item.translateX - item.speed;
        if (NEWX !== item.translateX) {
          item.translateX = NEWX;
          needsUpdate = true;
        }
      });
      // 移除超出屏幕的弹幕并触发更新
      const BEFORELENGTH = this.bulletComments.length;
      this.bulletComments = this.bulletComments.filter(item => item.translateX > -20);
      if (needsUpdate || this.bulletComments.length !== BEFORELENGTH) {
        this.forceUpdate = !this.forceUpdate; // 触发视图更新
      }
    }, 16); // 60fps
  }
}

class BulletCommentItem {
  private static trackIndex: number = 0;
  id: number;
  content: Resource | string;
  color: string;
  positionY: number;
  translateX: number = 1000; // 初始位置(右侧)
  speed: number; // 移动速度
  isUserBulletComment: boolean = false; // 标记是否用户发送

  constructor(content: Resource | string, isUserBulletComment: boolean = false) {
    this.id = new Date().getTime();
    this.content = content;
    this.color = '#FFFFFF';
    BulletCommentItem.trackIndex = (BulletCommentItem.trackIndex + 1) % 4;
    this.positionY = BulletCommentItem.trackIndex * 33; // 计算Y位置
    this.speed = 2;
    this.isUserBulletComment = isUserBulletComment;
  }
}

@Entry
@Component
struct BulletCommentFont {
  @State isPlaying: boolean = false;
  @State @Watch('changeOrientation') isFull: boolean = false; // 是否全屏
  @Provide('commentFontSize') myFontSize: number = 14; // 设置弹幕字体大小
  @State currentTime: number = 0; // 当前播放进度
  @State duration: number = 0; // 总时长
  @State showControls: boolean = true; // 是否显示控制栏
  @State showBulletComment: boolean = true; // 是否显示弹幕
  @State bulletComments: BulletCommentItem[] = [];
  private videoSrc: Resource = $rawfile('video.mov'); // $rawfile('video.mov')需要替换为开发者需要的视频资源文件
  private controller: VideoController = new VideoController();
  private bulletCommentIndex: number = 0;
  private presetBulletComments = [
    '很好看', '支持', '再来一个', '爱了爱了', '厉害', '哈哈哈', '太棒了', '666', '精彩！', '好看！', '泪目',
    '针不戳', '好耶', '哈哈哈有趣', '绝了', '妙啊', '点赞', '关注了', '笑死我了', '收藏了', '点我发弹幕吧'
  ];
  private bulletCommentInterval: number = 0;

  aboutToAppear() {
    this.startBulletCommentGenerator();
    let initBulletComments = [
      '很好看', '支持',
    ];
    this.bulletComments = initBulletComments.map(text => new BulletCommentItem(text));
    let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
    window.getLastWindow(context).then((lastWindow) => {
      // 设置沉浸式
      lastWindow.setWindowLayoutFullScreen(true);
      let systemBarProperties: window.SystemBarProperties = {
        statusBarColor: '#00000000',
        statusBarContentColor: '#ffffff'
      };
      lastWindow.setWindowSystemBarProperties(systemBarProperties);
    });
  }

  // 横竖屏切换
  changeOrientation() {
    let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
    window.getLastWindow(context).then((lastWindow) => {
      lastWindow.setPreferredOrientation(this.isFull ? window.Orientation.AUTO_ROTATION_LANDSCAPE :
        window.Orientation.PORTRAIT);
      lastWindow.setWindowSystemBarEnable(this.isFull ? [] : ['status', 'navigation']);
    });
  }

  aboutToDisappear() {
    clearInterval(this.bulletCommentInterval);
  }

  // 切换播放状态
  private togglePlay() {
    this.isPlaying = !this.isPlaying;
    if (this.isPlaying) {
      this.controller.start();
    } else {
      this.controller.pause();
    }
  }

  // 根据播放时间均匀生成弹幕
  private startBulletCommentGenerator() {
    // 每3秒生成一条
    this.bulletCommentInterval = setInterval(() => {
      if (!this.isPlaying) {
        return;
      }
      let randomText = this.presetBulletComments[this.bulletCommentIndex];
      this.bulletCommentIndex = (this.bulletCommentIndex + 1) % this.presetBulletComments.length;
      this.bulletComments = [...this.bulletComments, new BulletCommentItem(randomText)];
    }, 1000);
  }

  // 格式化时间
  private formatTime(seconds: number): string {
    let mins = Math.floor(seconds / 60);
    let secs = Math.floor(seconds % 60);
    return util.format('%s:%s', mins.toString().padStart(2, '0'), secs.toString().padStart(2, '0'));
  }

  build() {
    Column() {
      Column() {
        // 视频播放区域
        Stack() {
          Video({
            src: this.videoSrc,
            controller: this.controller
          })
          // 横竖屏切换组件区域变化时更改弹幕字体大小
            .onAreaChange((oldValue, newValue) => {
              console.info(oldValue.width.toString());
              if (newValue.width > newValue.height) {
                this.myFontSize = 22;
              } else {
                this.myFontSize = 14;
              }
            })
            .size({ width: '100%', height: '100%' })
            .autoPlay(false)
            .controls(false)
            .onPrepared((event: VideoPreparedEvent) => { // 使用定义好的接口类型
              this.controller.start();
              this.duration = event.duration;
            })
            .objectFit(ImageFit.Contain)
            .onUpdate((event: VideoUpdateEvent) => {
              this.currentTime = event.time;
              // 同步播放状态到弹幕
              if (event.time > 0 && !this.isPlaying) {
                this.isPlaying = true;
              }
            })
            .onFinish(() => {
              this.isPlaying = false;
            })
            .onClick(() => {
              this.showControls = !this.showControls;
            });
          // 弹幕组件
          BulletCommentView({
            bulletComments: $bulletComments,
            isPlaying: $isPlaying,
            showBulletComment: $showBulletComment,
          })
            .width('100%')
            .height(100)
            .position({ x: '0%', y: '40%' })
            .onClick(() => {
              this.showControls = !this.showControls;
            });

          // 控制栏
          if (this.showControls) {
            Column() {
              // 进度条
              Row() {
                Slider({
                  value: this.currentTime,
                  min: 0,
                  max: this.duration,
                  step: 1,
                  style: SliderStyle.OutSet
                })
                  .trackThickness(6)
                  .blockSize({
                    width: 16,
                    height: 16
                  })
                  .height(60)
                  .trackColor('rgba(255, 255, 255, 0.4)')
                  .onChange((value: number, mode: SliderChangeMode) => {
                    if (mode === SliderChangeMode.Begin) {
                      this.controller.pause();
                    } else if (mode === SliderChangeMode.End) {
                      this.controller.start();
                    }
                    this.controller.setCurrentTime(value);
                  });
              }
              .height(30)
              .margin({ left: 8, right: 8 });

              // 控制按钮
              Row() {
                Button() {
                  Image(this.isPlaying ? $r('app.media.pause') :
                    $r('app.media.play')) // $r('app.media.pause')和$r('app.media.play')需要替换为开发者需要的图片资源文件
                    .width(24)
                    .height(24);
                }
                .onClick(() => this.togglePlay())
                .margin({ right: 8 })
                .backgroundColor(Color.Transparent);

                Button() {
                  Image($r('app.media.next')) // $r('app.media.next')需要替换为开发者需要的图片资源文件
                    .width(24)
                    .height(24);
                }
                .backgroundColor(Color.Transparent)
                .margin({ left: 8, right: 8 });

                // 控制弹幕显隐
                Button() {
                  Image(this.showBulletComment ? $r('app.media.bulletComment_hide') :
                    $r('app.media.bulletComment_show')) // $r('app.media.bulletComment_hide')和$r('app.media.bulletComment_show')需要替换为开发者需要的图片资源文件
                    .width(24)
                    .height(24);
                }
                .backgroundColor(Color.Transparent)
                .margin({ left: 8, right: 8 })
                .onClick(() => {
                  this.showBulletComment = !this.showBulletComment;
                });

                Text('  点击发送弹幕')
                  .backgroundColor('rgba(255, 255, 255, 0.3)')
                  .fontSize(14)
                  .padding({ top: 0, bottom: 0 })
                  .fontColor(Color.White)
                  .width(118)
                  .height(24)
                  .margin({ left: 8 })
                  .borderRadius(20);
                Blank();

                Text(this.formatTime(this.currentTime) + '/' + this.formatTime(this.duration))
                  .fontColor(Color.White)
                  .fontSize(14)
                  .margin({ right: 8 });

                // $r('app.media.out')和$r('app.media.full')需要替换为开发者需要的图片资源文件
                Image(this.isFull ? $r('app.media.out') : $r('app.media.full'))
                  .width(20)
                  .height(20)
                  .objectFit(ImageFit.Contain)
                  .onClick(() => {
                    this.isFull = !this.isFull;
                  })
                  .margin({ left: 5 });
              }
              .height('20%')
              .width('100%')
              .padding({ left: 12, right: 12 });
            }
            .backgroundColor('rgba(0, 0, 0, 0.5)')
            .height('40%')
            .width('100%')
            .position({ y: this.isFull ? '75%' : '78%' });
          }
        }
        .height('100%');
      }
      .width('100%')
      .height('100%')
      .expandSafeArea([SafeAreaType.SYSTEM, SafeAreaType.KEYBOARD], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
    }
    .width('100%')
    .height('108%');
  }
}
```

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/v7LK94PhSNGFbgVoIKJi6A/zh-cn_image_0000002628394518.png "点击放大")
