---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-805
title: 如何解决动态修改TextArea数量时光标跳转的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何解决动态修改TextArea数量时光标跳转的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:04+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7217b4fb6a5c5e91744e256eb88ec7574dbd578a67487001bb2cef4c68aa0c4b
---

## 问题现象

当通过动态增删操作修改TextArea输入框数量时，光标会自动聚焦到默认输入框，当前输入的光标位置丢失。代码如下：

```ts
@Entry
@Component
struct SaveImagePage1 {
  message: string = 'Hello World';
  @State willGetList: AcquireModel[] = [new AcquireModel()];

  build() {
    Row() {
      this.edit();
    };
  }

  @Builder
  edit() {
    Column({ space: 10 }) {
      Text(this.message)
        .fontSize(50)
        .fontWeight(FontWeight.Bold);
      TextArea({ placeholder: '荐语' })
        .width('100%')
        .height(100);
      Text('你将获得');
      ForEach(this.willGetList, (e: AcquireModel, i) => {
        Row({ space: 10 }) {
          TextArea({ text: e.acquire })
            .layoutWeight(1)
            .height(30)
            .onChange((v) => {
              this.willGetList[i].acquire = v;
            });
          Button('-')
            .onClick(() => {
              this.willGetList.splice(i, 1);
            });
        }
        .width('100%');
      });
      Button('+')
        .onClick(() => {
          this.willGetList.push(new AcquireModel());
        });
    }
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%')
    .id('card')
    .padding(10);
  }
}

class AcquireModel {
  acquire: string = '';
}
```

效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/yqjjzJQzQdW7H0fQbIg2jQ/zh-cn_image_0000002658917111.png "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/F_FbmY4OSs2kJKc2w2fidw/zh-cn_image_0000002628397890.gif "点击放大")

## 背景知识

* [TextArea](../harmonyos-references/ts-basic-components-textarea.md)为多行文本输入框组件，当输入的文本内容超过组件宽度时会自动换行显示。
* [ForEach](../harmonyos-references/ts-rendering-control-foreach.md)接口基于数组类型数据来进行循环渲染。
* [requestFocus](../harmonyos-references/ts-universal-attributes-focus.md#requestfocus9)方法语句中可使用的全局接口，调用此接口可以主动让焦点在下一帧渲染时转移至参数指定的组件上。

## 解决方案

当数组通过push/splice修改时，ForEach会重新渲染UI。由于TextArea是动态生成的，框架无法正确追踪每个输入框的生命周期，导致焦点丢失或默认聚焦到默认输入框。可通过以下方法避免光标跳转：

1. 通过focusId明确跟踪当前聚焦的输入框。
2. 在删除操作后，通过deleteChange方法延迟恢复焦点。
3. 为每个输入框生成唯一ID，避免因DOM重排导致焦点错位。
4. 通过requestFocus精准定位光标，不依赖框架的自动分配。

```ts
import { util } from '@kit.ArkTS';

@Observed
class AcquireModel {
  public acquire: string = '';
  public id: string;

  constructor(acquire: string) {
    this.acquire = acquire;
    this.id = util.generateRandomUUID(true);
  }
}

@Entry
@Component
struct SaveImagePage2 {
  message: string = 'Hello World';
  @State willGetList: AcquireModel[] = [new AcquireModel('')];
  @State focusId: string = '';
  @State isDel: boolean = false;
  @State deleteId: string = '';

  build() {
    Row() {
      Column({ space: 10 }) {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold);
        TextArea({ placeholder: '荐语' })
          .width('100%')
          .height(100);
        Text('你将获得');
        ForEach(this.willGetList, (e: AcquireModel) => {
          Column({ space: 10 }) {
            Row({ space: 10 }) {
              Child({ e: e, focusId: this.focusId, delId: this.deleteId });
              Button('-')
                .onClick(() => {
                  this.isDel = true;
                  this.deleteId = e.id;
                  const index = this.willGetList.findIndex((item) => item.id === e.id);
                  this.willGetList.splice(index, 1);
                });
            };
          };
        }, (e: AcquireModel) => e.id);
        Button('+')
          .onClick(() => {
            this.willGetList.push(new AcquireModel(''));
          });
      }
      .justifyContent(FlexAlign.Center)
      .height('100%')
      .width('100%')
      .id('card')
      .padding(10);
    };
  }
}

@Component
struct Child {
  @ObjectLink e: AcquireModel;
  @Link focusId: string;
  @Link @Watch('deleteChange') delId: string;

  deleteChange() {
    if (!this.delId) {
      return;
    }
    if (this.focusId === this.e.id && this.delId !== this.focusId) {
      setTimeout(() => {
        this.getUIContext().getFocusController().requestFocus(this.focusId);
        this.delId = '';
      }, 50);
    }
  }

  build() {
    TextArea({ text: this.e.acquire })
      .layoutWeight(1)
      .onChange((v) => {
        this.e.acquire = v;
      })
      .onFocus(() => {
        this.focusId = this.e.id;
      })
      .id(this.e.id);
  }
}
```
