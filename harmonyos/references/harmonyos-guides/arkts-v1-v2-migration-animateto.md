---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-v1-v2-migration-animateto
title: AnimateTo使用迁移
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式状态管理 > 状态管理V1-V2迁移指导 > 状态管理V1向V2迁移场景 > AnimateTo使用迁移
category: harmonyos-guides
scraped_at: 2026-11-21T09:11:04+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:445cb1e1200dd5ffdce93380227554e337c50da18e739a466568b916ecb6083f
---

在状态管理从V1迁移至V2的过程中，[animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)执行动画前如需修改状态变量，可参考本文档的适配方案。

## 执行动画前重新定义初始态场景

**V1实现代码如下：**

```typescript
@Entry
@Component
struct Index {
  @State w: number = 50; // 宽度
  @State h: number = 50; // 高度
  @State message: string = 'Hello';

  build() {
    Column() {
      Button('change size')
        .margin(20)
        .onClick(() => {
          // 在执行动画前，存在额外的修改
          this.w = 100;
          this.h = 100;
          this.message = 'Hello World';
          this.getUIContext().animateTo({
            duration: 1000
          }, () => {
            this.w = 200;
            this.h = 200;
            this.message = 'Hello ArkUI';
          })
        })
      Column() {
        Text(`${this.message}`)
      }
      .backgroundColor('#ff17a98d')
      .width(this.w)
      .height(this.h)
    }
  }
}
```

预期动画效果：绿色矩形从长宽100变为200，字符串从Hello World变为Hello ArkUI。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/90lRONZhTmGdMY22F1jPBg/zh-cn_image_0000002821756231.gif?HW-CC-KV=V1&HW-CC-Date=20261121T010940Z&HW-CC-Expire=31536000000&HW-CC-Sign=379444FA42AD3D3F451B6F5ABEDE7F94FC2AD8677690AF8D65A8C62208435F47)

**V1迁移V2**

```typescript
@Entry
@ComponentV2
struct Index {
  @Local w: number = 50; // 宽度
  @Local h: number = 50; // 高度
  @Local message: string = 'Hello';

  build() {
    Column() {
      Button('change size')
        .margin(20)
        .onClick(() => {
          // 在执行动画前，存在额外的修改
          this.w = 100;
          this.h = 100;
          this.message = 'Hello World';
          this.getUIContext().animateTo({
            duration: 1000
          }, () => {
            this.w = 200;
            this.h = 200;
            this.message = 'Hello ArkUI';
          })
        })
      Column() {
        Text(`${this.message}`)
      }
      .backgroundColor('#ff17a98d')
      .width(this.w)
      .height(this.h)
    }
  }
}
```

由于当前animateTo与V2的刷新机制不兼容，执行动画前的额外修改未生效，实际显示的动画效果如下图所示：绿色矩形从长宽50变为200，字符串从Hello变为Hello ArkUI。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/sFpuOoVMT52LH2r1xE4ugg/zh-cn_image_0000002821836231.gif?HW-CC-KV=V1&HW-CC-Date=20261121T010940Z&HW-CC-Expire=31536000000&HW-CC-Sign=CFCA513CB62E399C392721332A3BF47C6F9A427B188E8E7D5120BB34F958CCED)

## 迁移方案

### API version 22之前的迁移方案

在API version 22之前，可以使用一个duration为0的[animateToImmediately](../harmonyos-references/ts-explicit-animatetoimmediately.md#animatetoimmediately)将额外的修改先刷新，再执行原来的动画达成预期的效果。

完整代码如下：

```typescript
@Entry
@ComponentV2
struct Index {
  @Local w: number = 50; // 宽度
  @Local h: number = 50; // 高度
  @Local message: string = 'Hello';

  build() {
    Column() {
      Button('change size')
        .margin(20)
        .onClick(() => {
          // 在执行动画前，存在额外的修改
          this.w = 100;
          this.h = 100;
          this.message = 'Hello World';
          animateToImmediately({
            duration: 0
          }, () => {
          })
          this.getUIContext().animateTo({
            duration: 1000
          }, () => {
            this.w = 200;
            this.h = 200;
            this.message = 'Hello ArkUI';
          })
        })
      Column() {
        Text(`${this.message}`)
      }
      .backgroundColor('#ff17a98d')
      .width(this.w)
      .height(this.h)
    }
  }
}
```

### API version 22及以后的迁移方案

从API version 22开始，可以使用[applySync接口](arkts-new-applysync-flushupdates-flushuiupdates.md)实现预期的显示效果。

原理为使用applySync接口同步刷新闭包函数内的状态变量变化，再执行原来的动画达成预期的效果。

```typescript
import { UIUtils } from '@kit.ArkUI';

@Entry
@ComponentV2
struct Index {
  @Local w: number = 50; // 宽度
  @Local h: number = 50; // 高度
  @Local message: string = 'Hello';

  build() {
    Column() {
      Button('change size')
        .margin(20)
        .onClick(() => {
          // 在执行动画前，存在额外的修改
          UIUtils.applySync(() => {
            this.w = 100;
            this.h = 100;
            this.message = 'Hello World';
          })
          this.getUIContext().animateTo({
            duration: 1000
          }, () => {
            this.w = 200;
            this.h = 200;
            this.message = 'Hello ArkUI';
          })
        })
      Column() {
        Text(`${this.message}`)
      }
      .backgroundColor('#ff17a98d')
      .width(this.w)
      .height(this.h)
    }
  }
}
```
