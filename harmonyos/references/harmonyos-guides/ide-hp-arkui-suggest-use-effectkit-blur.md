---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hp-arkui-suggest-use-effectkit-blur
title: "@performance/hp-arkui-suggest-use-effectkit-blur"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-suggest-use-effectkit-blur
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a81639927669703dbdaf5313da4849df09e60ac095e1c46969b6160826e1524b
---

建议使用effectKit.createEffect实现模糊效果。

通用丢帧场景下，建议优先修改。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@performance/hp-arkui-suggest-use-effectkit-blur": "suggestion",
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
// 导入图片处理模块
import image from '@ohos.multimedia.image';
// 导入图像效果模块
import effectKit from '@ohos.effectKit';

@Entry
@Component
struct MyComponent {
  // 是否显示全屏模态页面。静态模糊用
  @State isShowStaticBlur: boolean = false;
  // PixelMap实例
  @State pixelMap: image.PixelMap | undefined = undefined;
  // ImageSource实例
  imgSource: image.ImageSource | undefined = undefined;

  // 静态模糊
  async staticBlur() {
    // 获取resourceManager对象
    let resourceMgr = this.getUIContext()?.getHostContext()?.resourceManager;
    // 获rawfile目录下的图片
    const fileData = await resourceMgr?.getRawFileContent('startIcon.png');
    // 创建实例
    let buffer = fileData?.buffer.slice(0);
    if (buffer) {
      // 创建图片源实例
      this.imgSource = image.createImageSource(buffer);
    }
    // 创建像素的属性
    let opts: image.InitializationOptions = {
      // 是否可编辑
      editable: true,
      // 像素格式。3表示RGBA_8888
      pixelFormat: 3,
      // 创建图片大小
      size: {
        height: 4,
        width: 6
      }
    };
    // 创建PixelMap
    await this.imgSource?.createPixelMap(opts).then((pixelMap: image.PixelMap) => {
      // 模糊半径
      const blurRadius = 1;
      // 创建Filter实例
      let headFilter = effectKit.createEffect(pixelMap);
      if (headFilter != null) {
        // 设置静态模糊。将模糊效果添加到效果链表中
        headFilter.blur(blurRadius);
        // 获取已添加链表效果的源图像的image.PixelMap
        headFilter.getEffectPixelMap().then((pixelMap: image.PixelMap) => {
          this.pixelMap = pixelMap;
        });
      }
    })
  }

  // 图片设置静态模糊的模态页面
  @Builder
  staticBlurBuilder() {
    Stack() {
      Image(this.pixelMap)
        .width('100%')
        .height('100%')
        .objectFit(ImageFit.Fill)
      Button('close')
        .fontSize(20)
        .onClick(() => {
          this.isShowStaticBlur = false;
        })
    }
    .width('100%')
    .height('100%')
  }

  build() {
    Column({ space: 10 }) {
      Button('静态模糊')
        .onClick(() => {
          this.isShowStaticBlur = true;
          // 设置静态模糊
          this.staticBlur();
        })
        .bindContentCover(this.isShowStaticBlur, this.staticBlurBuilder(), {
          // 全屏模态转场类型。上下切换动画
          modalTransition: ModalTransition.DEFAULT
        })
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```

## 反例

```screen
@Entry
@Component
struct MyComponent {
  build() {
    Column({ space: 10 }) {
      // 对image进行模糊，未使用effectKit.createEffect
      Text('Image blur').fontSize(15).fontColor(0xCCCCCC).width('90%')
      Image('resources/base/media/sss001.jpg')
        .blur(1)
        .border({ width: 1 })
        .borderStyle(BorderStyle.Dashed)
        .aspectRatio(1)
        .width('90%')
        .height(40)

      // 对背景进行模糊，未使用effectKit.createEffect
      Text('backdropBlur').fontSize(15).fontColor(0xCCCCCC).width('90%')
      Text()
        .width('90%')
        .height(40)
        .fontSize(16)
        .backdropBlur(3)
        .backgroundImage('/pages/attrs/image/image.jpg')
        .backgroundImageSize({ width: 1200, height: 160 })
    }.width('100%').margin({ top: 5 })
  }
}
```

## 规则集

```screen
plugin:@performance/recommended
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
