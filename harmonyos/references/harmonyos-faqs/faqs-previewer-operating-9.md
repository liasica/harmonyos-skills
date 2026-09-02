---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-previewer-operating-9
title: previewer显示的UX效果和真机的显示实际不一致
breadcrumb: FAQ > DevEco Studio > 界面预览 > previewer显示的UX效果和真机的显示实际不一致
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:54+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9787e5111a4b040b4457081ec8468f9636fb3a3bfcc330d063b8a03dc6ae415d
---

## 问题现象

有如下代码，Flex布局，用previewer查看时，两侧占满屏幕；但是真机查看，两侧会有留白。

```screen
@Entry
@Component
struct Index {
  build() {
    Column() {
      Flex({ direction: FlexDirection.Row, justifyContent: FlexAlign.SpaceBetween }) { // 子组件在容器主轴上行布局
        Text('约伴召集')
          .width(180)
          .height(38)
          .backgroundColor('#ff1a9191')

        Text('我的活动')
          .width(180)
          .height(38)
          .backgroundColor('#ff6868d0')
      }
      .width(360)
      .height(58)
    }
    .height('100%')
    .width('100%')
  }
}
```

previewer效果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/okIkJapyQ6Wt9SNJCGTMTg/zh-cn_image_0000002658807357.png "点击放大")

真机效果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/d5edHIUERhy2VV96nt6-CA/zh-cn_image_0000002628408096.png "点击放大")

可以发现真机的Text组件两侧留有空白。

## 背景知识

* previewer可以看到previewer设备的屏幕尺寸：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/cNl-DI-1QNyz55-QDy317w/zh-cn_image_0000002628567996.png "点击放大")

  1080px换算成vp是360vp。
* 屏幕管理API @ohos.display可以参考[如何获取手机屏幕信息](faqs-arkui-242.md)。

## 问题定位

引入display工具，添加如下代码，获取真机屏幕尺寸。

```screen
try {
  this.screenWidth = display.getDefaultDisplaySync().width;
  this.screenHeight = display.getDefaultDisplaySync().height;
} catch (e) {
  console.error('Fail with code: ' + JSON.stringify(e));
}
console.info(`width = ${this.getUIContext().px2vp(this.screenWidth)} , height = ${this.getUIContext()
  .px2vp(this.screenHeight)}`);
```

查看日志，可以看到获取到真机屏幕的尺寸是374vp，大于360vp，所以真机两侧存在空白。

## 分析结论

代码中固定了组件的宽度尺寸是360vp，previewer设备的宽度尺寸设置的也是360vp，所以组件横向充满了previewer；但是真机的宽度尺寸是374vp，所以会留下空白。

## 修改建议

将Flex宽度设置为'100%'，子元素Text的宽度分别设置为'50%'，即可自适应设备宽度。

```screen
import { display } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  private screenWidth: number = 0;
  private screenHeight: number = 0;

  build() {
    Column() {
      Flex({ direction: FlexDirection.Row, justifyContent: FlexAlign.SpaceBetween }) { // 子组件在容器主轴上行布局
        Text('约伴召集')
          .width('50%')
          .height(38)
          .backgroundColor('#ff1a9191');

        Text('我的活动')
          .width('50%')
          .height(38)
          .backgroundColor('#ff6868d0');
      }
      .width('100%')
      .height(58);
    }
    .height('100%')
    .width('100%')
    .onClick(() => {
      try {
        this.screenWidth = display.getDefaultDisplaySync().width;
        this.screenHeight = display.getDefaultDisplaySync().height;
      } catch (e) {
        console.error('Fail with code: ' + JSON.stringify(e));
      }
      console.info(`width = ${this.getUIContext().px2vp(this.screenWidth)} , height = ${this.getUIContext()
        .px2vp(this.screenHeight)}`);
    });
  }
}
```
