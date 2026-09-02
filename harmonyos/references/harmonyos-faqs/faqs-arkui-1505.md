---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1505
title: Checkbox多选和反选功能实现
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Checkbox多选和反选功能实现
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:11+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a7fce2c7df4c52b8198964da2e747dc13bdb4fff759f6ff35bc4d582ff10db0b
---

## 问题现象

场景一：ArkUI中是否提供内置的一键反选功能的控件？

场景二：如何实现多选，并获取当前用户选择Checkbox的值？

## 背景知识

* [Checkbox](../harmonyos-references/ts-basic-components-checkbox.md)多选框组件，它允许用户从一系列选项中选择多个项。无论是电子商务网站上的商品筛选，还是在线表单的数据收集，Checkbox都发挥着重要作用。
* 反选是指将当前所有已选中的Checkbox变为未选中状态，同时将所有未选中的Checkbox变为选中状态。
* [CheckboxGroup](../harmonyos-references/ts-basic-components-checkboxgroup.md)：多选框群组，用于控制多选框全选或者不全选状态。

## 解决方案

* **场景一**：目前Checkbox暂无内置一键反选的能力，可通过反转每一项中绑定于Checkbox的select属性的参数的状态值，实现变更Checkbox的选中状态，并利用响应式数据绑定自动更新界面以实现一键反选功能。

  ```ts
  @ObservedV2
  class Person {
    // 控制Checkbox的选中状态
    @Trace public name: boolean;
    public value: number;

    constructor(name: boolean, value: number) {
      this.name = name;
      this.value = value;
    }
  }

  @ObservedV2
  class Info {
    personList: Person[] = [];

    constructor() {
      this.personList = [new Person(false, 0), new Person(false, 1), new Person(false, 2)];
    }
  }

  @Entry
  @Component
  struct CheckboxPage {
    info: Info = new Info();

    build() {
      Column() {
        Row() {
          Text('反选');
        }
        .onClick(() => {
          // 反转Checkbox的选中状态，实现反选
          for (let i = 0; i < this.info.personList.length; i++) {
            this.info.personList[i].name = !this.info.personList[i].name;
          }
        });

        List({ space: 0, initialIndex: 0 }) {
          ForEach(this.info.personList, (item: Person) => {
            ListItem() {
              Flex() {
                Checkbox({ name: item.value.toString() })
                  .selectedColor('#027cff')
                  .shape(CheckBoxShape.ROUNDED_SQUARE)
                  .unselectedColor('#027cff')
                  .select(item.name)
                  .onChange((value: boolean) => {
                    // 记录当前Checkbox的选中状态
                    item.name = value;
                  })
                  .width(18)
                  .height(18);
                Text(item.value.toString()).fontSize(15).margin({ top: 5 });
              };
            };
          }, (item: Person) => JSON.stringify(item));
        };
      }
      .width('100%')
      .height('100%')
      .margin({ top: 50 })
      .padding({ left: 24, right: 24 });
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/40M1HCKpR62bAtKYtrnPbg/zh-cn_image_0000002658965763.png "点击放大")

* **场景二**：通过Checkbox的onChange方法对选中数据进行处理。

  ```ts
  class CheckName {
    public id: string;
    public productName: string;

    constructor(id: string, productName: string) {
      this.id = id;
      this.productName = productName;
    }
  }

  @Entry
  @Component
  struct CheckboxExample {
    @State services: CheckName[] = [
      new CheckName('1', 'checkbox1'),
      new CheckName('2', 'checkbox2'),
      new CheckName('3', 'checkbox3'),
      new CheckName('4', 'checkbox4'),
    ];
    @State clickIndex: string = '';
    @State clickName: string = '';
    @State selectIndexList: Array<string> = [];

    build() {
      Scroll() {
        Column() {
          // 全选按钮
          Flex({ justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {
            CheckboxGroup({ group: 'checkboxGroup' })
              .selectedColor('#007DFF')
              .onChange((itemName: CheckboxGroupResult) => {
                console.info('checkbox group content' + JSON.stringify(itemName));
              });
            Text('Select All').fontSize(14).lineHeight(20).fontColor('#182431').fontWeight(500);
          }.width('auto');

          ForEach(this.services, (item: CheckName) => {
            Flex({ justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {
              Checkbox({ name: item.productName, group: 'checkboxGroup' })
                .selectedColor('#007DFF')
                .onChange((value: boolean) => {
                  this.clickIndex = item.id;
                  this.clickName = item.productName;
                  if (value == true) {
                    this.selectIndexList.push(item.productName);
                  } else {
                    this.selectIndexList = this.selectIndexList.filter((element) => {
                      return element !== item.productName;
                      // 返回不等于要删除元素的元素构成新数组
                    });
                  }
                });
              Text(item.productName).fontSize(14).lineHeight(20).fontColor('#182431').fontWeight(500);
            }.width('auto').margin({ left: 36 });
          }, (item: CheckName) => item.id);
          Text(this.selectIndexList.toString())
            .fontSize(14)
            .lineHeight(20)
            .fontColor('#182431')
            .fontWeight(500)
            .alignSelf(ItemAlign.Center);
        }
        .justifyContent(FlexAlign.Center)
        .width('100%')
        .height('100%');
      };
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/DypLTRtbRvmR1p0lQ_fWYQ/zh-cn_image_0000002628606552.png "点击放大")
