---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-imagesourcenotrelease
title: ImageSourceNotRelease
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Scanner代码检查规则 > ArkTS代码检查规则 > ImageSourceNotRelease
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:00+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:0ba65bd6e6712c21339fa62354235e0399e440ea6ae616496fceda7d3d75d8dc
---

通过image.createImageSource()方法创建的ImageSource对象，使用完毕后，需及时调用release()方法释放对象，避免图片占用过大内存。

## 规则配置

```json
// rules.json
{
  "rules": {
    "arkts": {
      "ResourceLeak": [
        {
          "ruleId": "ImageSourceNotRelease",
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
import UIAbility from '@ohos.app.ability.UIAbility';

/**
 * 正例：正确释放资源
 */
export class TestRelease extends UIAbility {
    onCreate() {
        this.createAndUseImageSource();
    }
    createAndUseImageSource(): void {
        let imageSource: image.ImageSource = image.createImageSource("file://test.jpg");
        let alias = imageSource;
        let imageSource2: image.ImageSource = image.createImageSource("file://test.jpg");
        let alias2 = imageSource2;
        alias.release();
        alias2.release();
    }
}
```

## 反例

```ts
import image from '@ohos.multimedia.image';
import UIAbility from '@ohos.app.ability.UIAbility';

/**
 * 反例：未释放资源
 */
export class TestNotRelease extends UIAbility {
    onCreate() {
        this.createAndUseImageSource();
    }
    createAndUseImageSource(): void {
        let imageSource: image.ImageSource = image.createImageSource("file://test.jpg");
        let alias = imageSource;
        let imageSource2: image.ImageSource = image.createImageSource("file://test.jpg"); // leak
        let alias2 = imageSource2;
        alias.release();
    }
}
```

Code Scanner代码检查规则的配置指导请参考[1.6.3 代码检查工具（codescanner）](ide-command-line-codescanner.md)
