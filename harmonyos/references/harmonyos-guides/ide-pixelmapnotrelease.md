---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-pixelmapnotrelease
title: PixelMapNotRelease
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Scanner代码检查规则 > ArkTS代码检查规则 > PixelMapNotRelease
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:00+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:6280a6adcc2fee10875479bc7375c2fd0cdbf921f4d82d15676928cc4cdeac8e
---

通过createPixelMap()、createPixelMapSync()、getEffectPixelMap()等接口创建的PixelMap对象，使用完毕后，需及时调用release()方法释放对象，避免图片占用过大内存。

## 规则配置

```json
// rules.json
{
  "rules": {
    "arkts": {
      "ResourceLeak": [
        {
          "ruleId": "PixelMapNotRelease",
          "severity": "error",
          "skip": false
        }
      ]
    }
  }
}
```

## 正例

```ts
import image from '@ohos.multimedia.image';
import { effectKit } from "@kit.ArkGraphics2D";
import UIAbility from '@ohos.app.ability.UIAbility';

/**
 * 正例：正确释放资源
 */
export class TestRelease extends UIAbility {
  private pixelMap1: image.PixelMap | null = null;
  private pixelMap2: image.PixelMap | null = null;
  private pixelMap3: image.PixelMap | null = null;
  async onCreate(): Promise<void> {
    // 测试 image.ImageSource.createPixelMap 创建接口
    const imageSource1 = image.createImageSource("file://test1.jpg");
    this.pixelMap1 = await imageSource1.createPixelMap();
    imageSource1.release();
    // 测试 image.ImageSource.createPixelMapSync 创建接口
    const imageSource2 = image.createImageSource("file://test2.jpg");
    this.pixelMap2 = imageSource2.createPixelMapSync();
    imageSource2.release();
    // 测试 effectKit.Filter.getEffectPixelMap 创建接口
    const color = new ArrayBuffer(96);
    let opts : image.InitializationOptions = {
      editable: true,
      pixelFormat: 3,
      size: {
        height: 4,
        width: 6
      }
    };
    image.createPixelMap(color, opts).then((pixelMap) => {
      effectKit.createEffect(pixelMap).grayscale().getEffectPixelMap().then(data => {
        this.pixelMap3 = data;
      })
    })
  }
  onDestroy(): void {
    this.pixelMap1?.release();
    this.pixelMap2?.release();
    this.pixelMap3?.release();
  }
}
```

## 反例

```screen
import image from '@ohos.multimedia.image';
import { effectKit } from "@kit.ArkGraphics2D";
import UIAbility from '@ohos.app.ability.UIAbility';

/**
 * 反例：未释放资源
 */
export class TestNotRelease extends UIAbility {
  private pixelMap1: image.PixelMap | null = null;
  private pixelMap2: image.PixelMap | null = null;
  private pixelMap3: image.PixelMap | null = null;
  async onCreate(): Promise<void> {
    // 测试 image.ImageSource.createPixelMap 资源创建接口
    const imageSource1 = image.createImageSource("file://test1.jpg");
    this.pixelMap1 = await imageSource1.createPixelMap(); // leak
    imageSource1.release();
    // 测试 image.ImageSource.createPixelMapSync 资源创建接口
    const imageSource2 = image.createImageSource("file://test2.jpg");
    this.pixelMap2 = imageSource2.createPixelMapSync(); // leak
    imageSource2.release();
    // 测试 effectKit.Filter.getEffectPixelMap 资源创建接口
    const color = new ArrayBuffer(96);
    let opts : image.InitializationOptions = {
      editable: true,
      pixelFormat: 3,
      size: {
        height: 4,
        width: 6
      }
    };
    image.createPixelMap(color, opts).then((pixelMap) => {
      effectKit.createEffect(pixelMap).grayscale().getEffectPixelMap().then(data => { // leak
        this.pixelMap3 = data;
      })
    })
  }
}
```

Code Scanner代码检查规则的配置指导请参考[1.6.3 代码检查工具（codescanner）](ide-command-line-codescanner.md)
