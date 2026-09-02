---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-use-onanimationstart-in-swiper
title: "@performance/hp-arkui-use-onAnimationStart-for-swiper-preload"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-use-onAnimationStart-for-swiper-preload
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8d76d15299c0faa95b51616ec1b1f7583aa8b15c1bd4a96415b794e6901dfb21
---

建议Swiper预加载机制搭配 OnAnimationStart 接口回调使用。

滑动丢帧场景下，建议优先修改。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@performance/hp-arkui-use-onAnimationStart-for-swiper-preload": "warn",
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
import image from '@ohos.multimedia.image';
// 源码文件，请以工程实际为准
import { MyDataSource } from './MyDataSource';
import { PhotoItem } from './component/ChildComponent';
import { MyObject } from './data/DataEntry';

@Entry
@Component
struct MyComponent {
  cacheCount: number = 1;
  swiperController: SwiperController = new SwiperController();
  private data: MyDataSource = new MyDataSource([]);

  build() {
    Swiper(this.swiperController) {
      LazyForEach(this.data, (item: MyObject, index?: number) => {
        // 源码文件，请以工程实际为准
        PhotoItem({ myIndex: index, dataSource: this.data })
      }, (item: MyObject) => item.id) // item唯一id
    }
    .cachedCount(this.cacheCount)
    .indicator(true)
    .loop(false)
    // 在OnAnimationStart接口回调中进行预加载资源的操作
    .onAnimationStart((index: number, targetIndex: number) => {
      if (targetIndex !== index) {
        try {
          // 获取resourceManager资源管理器
          const resourceMgr = this.getUIContext().getHostContext()?.resourceManager;
          // 获取rawfile文件夹下icon.png的ArrayBuffer
          let str = "item" + (targetIndex + this.cacheCount + 2) + ".jpg";
          resourceMgr?.getRawFileContent(str).then((value) => {
            // 创建imageSource
            const imageSource = image.createImageSource(value.buffer);
            imageSource.createPixelMap().then((value) => {
              this.data.addData(targetIndex + this.cacheCount + 1, {
                description: "" + (targetIndex + this.cacheCount + 1),
                image: value
              })
            })
          })
        } catch (err) {
          console.log("error code" + err);
        }
      }
    })
    .width('100%')
    .height('100%')
  }
}
```

## 反例

```screen
// 源码文件，请以工程实际为准
import { MyDataSource } from './MyDataSource';
import { PhotoItem } from './component/ChildComponent';
import { MyObject } from './data/DataEntry';

@Entry
@Component
struct MyComponent {
  cacheCount: number = 1;
  swiperController: SwiperController = new SwiperController();
  private data: MyDataSource = new MyDataSource([]);
  context = getContext(this);

  build() {
    // Swiper组件没有使用OnAnimationStart进行预加载
    Swiper(this.swiperController) {
      LazyForEach(this.data, (item: MyObject, index?: number) => {
        // 源码文件，请以工程实际为准
        PhotoItem({ myIndex: index, dataSource: this.data })
      }, (item: MyObject) => item.id)
    }
    .cachedCount(this.cacheCount)
    .indicator(true)
    .loop(false)
    .width('100%')
    .height('100%')
  }
}
```

## 规则集

```screen
plugin:@performance/recommended
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
