---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1267
title: 动态生成多个CheckboxGroup并设置全选
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 动态生成多个CheckboxGroup并设置全选
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:08+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e7ebbefb2e3f45310569fd2514d12d6183bc68a10ed8e015fc72a78601713112
---

## 问题现象

如何动态生成多个CheckboxGroup并设置其全选？

## 背景知识

[Checkbox](../harmonyos-references/ts-basic-components-checkbox.md)多选框组件，通常用于某选项的打开或关闭。[CheckboxGroup](../harmonyos-references/ts-basic-components-checkboxgroup.md)多选框群组，用于控制多选框全选或者不全选状态。多组CheckboxGroup要设置不同的群组名称，多个相同群组名称的CheckboxGroup，仅第一个CheckboxGroup生效。

## 解决方案

* 可以将需要展示的数据源整理成类似格式，根据数据源动态生成多组CheckboxGroup，用boolean类型的数组保存每个CheckboxGroup的状态，用来刷新选择框的选择状态，参考示例代码如下：

  ```ts
  interface DataModel {
    groupName: string;
    items: string[];
    selectAll: boolean;
  }

  @Entry
  @Component
  struct CheckboxGroupExample {
    // 数据源
    groups: Array<DataModel> = [
      { groupName: '第一章', items: ['1.1', '1.2', '1.3', '1.4'], selectAll: false },
      { groupName: '第二章', items: ['2.1', '2.2', '2.3'], selectAll: false }
    ];
    @State groupSelect: boolean[] = [false, false]; // 每个CheckBoxGroup选择状态
    @State selectAll: boolean = false; // 全选按钮的状态
    @State selectItem: Array<Array<string>> = [[], []]; // 保存已选的数据

    @Builder
    createGroup(data: DataModel, index: number) {
      Flex({ justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {
        CheckboxGroup({ group: data.groupName })
          .checkboxShape(CheckBoxShape.ROUNDED_SQUARE)
          .selectedColor('#007DFF')
          .selectAll(this.groupSelect[index])
          .onChange((event: CheckboxGroupResult) => {
            this.groups[index].selectAll = (event.status === SelectStatus.All);

            this.selectAll = true;
            for (let item of this.groups) {
              this.selectAll = (this.selectAll && item.selectAll);
            }
            // 保存当前分组所选数据
            this.selectItem[index] = event.name;
          });
        Text(data.groupName).fontSize(14).lineHeight(20).fontColor('#182431').fontWeight(500);
      };

      ForEach(data.items, (item: string) => {
        Flex({ justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {
          Checkbox({ name: item, group: data.groupName })
            .selectedColor('#007DFF')
            .shape(CheckBoxShape.ROUNDED_SQUARE)
            .onChange((value: boolean) => {
              console.info(`Checkbox1 change is ${value}`);
            });
          Text(item).fontSize(14).lineHeight(20).fontColor('#182431').fontWeight(500);
        }.margin({ left: 36 });
      }, (item: string) => item);
    }

    build() {
      Column() {
        ForEach(this.groups, (item: DataModel, index: number) => {
          this.createGroup(item, index);
        }, (item: DataModel) => JSON.stringify(item));
        Flex({ alignItems: ItemAlign.Center }) {
          Checkbox({ name: '全选' })
            .select(this.selectAll)
            .selectedColor('#007DFF')
            .shape(CheckBoxShape.ROUNDED_SQUARE)
            .onClick(() => {
              // 点击全选按钮，改变每个CheckBoxGroup选择状态
              this.selectAll = !this.selectAll;
              for (let i = 0; i < this.groupSelect.length; i++) {
                this.groupSelect[i] = !this.groupSelect[i];
                this.groupSelect[i] = this.selectAll;
              }
            });
          Text('全选');
        };

        Text(`当前所选数据${this.selectItem}`);
      }
      .padding(16);
    }
  }
  ```

  效果图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/_c3D34FrTMeOGOgDAkp3AQ/zh-cn_image_0000002658955329.gif "点击放大")
* CheckboxGroup还可以和List组件组合使用，点击“全选”后实现全部选中，参考示例代码如下：

  ```screen
  @Entry
  @Component
  struct Index {
    @State dataList: string[] = [];
    @State selectedItemInGroup: boolean = false; // group是否存在被选中item
    @State notSelectedItemInGroup: boolean = true; // group是否存在未被选中item

    aboutToAppear(): void {
      for (let i = 0; i < 300; i++) {
        this.dataList.push(i + '');
      }
    }

    build() {
      Row() {
        Column({ space: 20 }) {
          Row() {
            CheckboxGroup({ group: 'checkboxGroup' })
              .checkboxShape(CheckBoxShape.ROUNDED_SQUARE)
              .selectedColor(Color.Orange)
              .onChange((itemName: CheckboxGroupResult) => {
                console.info(`checkbox itemName.status:${itemName.status}`);
                // 关键代码
                if (itemName.status === SelectStatus.All) {
                  this.selectedItemInGroup = true;
                  this.notSelectedItemInGroup = false;
                } else if (itemName.status === SelectStatus.None) {
                  this.notSelectedItemInGroup = true;
                  this.selectedItemInGroup = false;
                }
                console.info(`checkbox group content: ${itemName}`);
              })
              .mark({
                strokeColor: Color.Black,
                size: 40,
                strokeWidth: 5
              })
              .unselectedColor('#39a2db')
              .width(30)
              .height(30);
            Text('Select All').fontSize(20);
          };

          List({ space: 20 }) {
            ForEach(this.dataList,
              (item: string, index: number) => {
                ListItem() {
                  Row() {
                    Checkbox({ name: 'checkbox' + index, group: 'checkboxGroup' })
                      .selectedColor('#39a2db')
                      .select(this.selectedItemInGroup)
                      .shape(CheckBoxShape.ROUNDED_SQUARE)
                      .onChange((value: boolean) => {
                        console.info(`Checkbox ${index} change is ${value}`);
                      })
                      .mark({
                        strokeColor: Color.Black,
                        size: 50,
                        strokeWidth: 5
                      })
                      .unselectedColor('#ffbebebe')
                      .width(30)
                      .height(30);
                    Text('Checkbox' + index).fontSize(20);
                  };
                }
                .backgroundColor(Color.White);
              }
            );
          }
          .cachedCount(100)
          .layoutWeight(1);
        }
        .padding(16)
        .height('100%')
        .alignItems(HorizontalAlign.Start);
      }
      .height('100%');
    }
  }
  ```

  效果图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/8XZNk6XdTwu-3T66IJWHRg/zh-cn_image_0000002628596112.gif "点击放大")
