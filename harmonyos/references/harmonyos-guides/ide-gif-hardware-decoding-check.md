---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-gif-hardware-decoding-check
title: "@performance/gif-hardware-decoding-check"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/gif-hardware-decoding-check
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e7f66222a27e6181fc0121b9620265dd1860bcf312a6832a59fa32fe266fd1f1
---

在使用@ohos/gif-drawable库解码gif图片时，建议开启硬解码，提升gif加载性能。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@performance/gif-hardware-decoding-check": "warn",
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
// @ohos/gif-drawable依赖可以通过'ohpm install @ohos/gif-drawable@2.1.0'下载安装
import { GIFComponentV2, ResourceLoader } from '@ohos/gif-drawable'

@Entry
@ComponentV2
struct GifDrawableNoReport0 {
  @Local model2:GIFComponentV2.ControllerOptions = new GIFComponentV2.ControllerOptions();
  @Local gifAutoPlay:boolean = false;
  @Local gifReset:boolean = false;

  aboutToAppear(): void {
    this.model2.destroy();
    let model22:GIFComponentV2.ControllerOptions = new GIFComponentV2.ControllerOptions();
    // 调用setOpenHardware接口且值为true，开启硬解码
    model22.setOpenHardware(true);
    model22.setSpeedFactor(1);
    ResourceLoader.downloadDataWithContext(this.getUIContext().getHostContext(), {
      url: 'https://example.com/test.gif'
    }, (sucBuffer: ArrayBuffer) => {
      model22.loadBuffer(sucBuffer, () => {
        console.log('网络加载解析成功回调绘制！')
        this.gifAutoPlay = true;
        // 给组件数据赋新的用户配置参数，达到后续gif动画效果
        this.model2 = model22;
      })
    }, (err: string) => {
      // 用户根据返回的错误信息，进行业务处理(展示一张失败占位图、再次加载一次、加载其它图片等)
    })
  }
  build() {
    Row() {
      GIFComponentV2({model:this.model2!!, autoPlay:this.gifAutoPlay!!, resetGif: this.gifReset!!})
    }
  }
}
```

## 反例

```screen
// @ohos/gif-drawable依赖可以通过'ohpm install @ohos/gif-drawable@2.1.0'下载安装
import { GIFComponentV2, ResourceLoader } from '@ohos/gif-drawable'

@Entry
@ComponentV2
struct GifDrawableReport0 {
  // 调用setOpenHardware接口且值为true，开启硬解码
  // model0未调用setOpenHardware接口，告警
  @Local model0: GIFComponentV2.ControllerOptions = new GIFComponentV2.ControllerOptions();
  @Local gifAutoPlay:boolean = false;
  @Local gifReset:boolean = false;

  aboutToAppear(): void {
    this.model0.destroy();
    // model00未调用setOpenHardware接口，告警
    let model00: GIFComponentV2.ControllerOptions = new GIFComponentV2.ControllerOptions();
    model00.setSpeedFactor(1);
    ResourceLoader.downloadDataWithContext(this.getUIContext().getHostContext(), {
      url: 'https://example.com/test.gif'
    }, (sucBuffer: ArrayBuffer) => {
      model00.loadBuffer(sucBuffer, () => {
        console.log('网络加载解析成功回调绘制！')
        this.gifAutoPlay = true;
        // 给组件数据赋新的用户配置参数，达到后续gif动画效果
        this.model0 = model00;
      })
    }, (err: string) => {
      // 用户根据返回的错误信息，进行业务处理(展示一张失败占位图、再次加载一次、加载其它图片等)
    })
  }
  build() {
    Row() {
      GIFComponentV2({model:this.model0!!, autoPlay:this.gifAutoPlay!!, resetGif: this.gifReset!!})
    }
  }
}
```

## 规则集

```screen
plugin:@performance/recommended
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
