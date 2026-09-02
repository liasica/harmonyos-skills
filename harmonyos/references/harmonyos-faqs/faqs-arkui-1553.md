---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1553
title: 如何实现滑动经过复选框时选中/取消的功能
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现滑动经过复选框时选中/取消的功能
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:11+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6aa72da91565389a1d07c6cc25d6e580fcbb5ad50515585afa51ed9f3cd752d8
---

## 问题现象

列表中的每一个Item都对应一个复选框。当前，CheckBox仅支持逐个选中/取消选中，如何实现手指滑动经过CheckBox的时候，CheckBox能完成选中/取消选中的功能，同时不影响列表滑动。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/hldUFmiMSwONg4wmdvNU3g/zh-cn_image_0000002658968445.gif "点击放大")

## 背景知识

* [CheckBox](../harmonyos-references/ts-basic-components-checkbox.md)：多选框组件，通常用于某选项的打开或关闭。
* [onAreaChange](../harmonyos-references/ts-universal-component-area-change-event.md#onareachange)：组件区域变化事件，组件区域变化时触发该回调。仅会响应由布局变化所导致的组件大小、位置发生变化时的回调。
* [onWillScroll](../harmonyos-references/ts-container-scrollable-common.md#onwillscroll12)：滚动事件回调，滚动组件滚动前触发。可以获取到相对于上一帧的偏移量、当前滑动状态、当前滑动操作的来源。
* [onTouch](../harmonyos-references/ts-universal-events-touch.md)：触摸事件，由手指在组件上按下、滑动或抬起时触发。回调中可以获取到触摸事件的类型。

## 解决方案

CheckBox本身不提供滑动多选的能力，需要自定义选中逻辑：手指在CheckBox选择框区域进行滑动时，完成选中操作；手指在文本区域进行滑动时，进行列表滚动。

1. 首先要明确组件的位置以及当前手指滑动的位置。对于组件的位置，自定义组件位置的数据类ComponentRect，记录当前组件四个边相对于父组件左上角的距离。通过onAreaChange事件，在组件位置发生变化时触发回调，重新计算位置并存储到map中。

   ```screen
   // 记录组件的位置
   interface ComponentRect {
     left: number;
     top: number;
     right: number;
     bottom: number;
   }
   ```

   ```screen
   // 判断手指当前在哪个组件的矩形区域内
   detectCurrentComponent(x: number, y: number) {
     let cur = '';
     this.componentRects.forEach((rect, id) => {
       if (x >= rect.left && x <= rect.right &&
         y >= rect.top && y <= rect.bottom) {
         cur = id;
       }
     });
     return cur;
   }
   ```

   ```screen
   // 组件发生变化时，刷新组件的位置信息
   .onAreaChange((oldVal, newVal) => {
     console.info(`${oldVal},${newVal}`);
     let area: ComponentRect = {
       left: Number(newVal.position.x),
       top: Number(newVal.position.y),
       right: Number(newVal.position.x) + Number(newVal.width),
       bottom: Number(newVal.position.y) + Number(newVal.height)
     };
     this.componentRects.set(item.id, area); // 记录组件位置
   })
   ```
2. ComponentRect数据类型记录的组件位置是包含了CheckBox和文本的，还需要再次根据组件位置比例判断手指是在CheckBox上还是在文本上，只有在CheckBox选择框上时才触发选中逻辑。

   ```screen
   // 获取手指处于组件上的横向比例
   getRateWidth(x: number, index: string) {
     let item = this.componentRects.get(index);
     if (!item) {
       return 0;
     }
     return (x - item.left) / (item.right - item.left);
   }
   ```
3. 获取到组件位置和手指位置之后，动态执行CheckBox选中操作，当检测到触摸类型为TouchType.Move且在组件范围，说明手指滑过了选中框，就将对应CheckBox的状态值置反，同时设置列表的friction和onWillScroll用于禁止列表滑动。

   ```screen
   .onTouch((event) => {
     // 获取当前手指的坐标（相对于父容器，与组件rect的坐标系一致）
     const fingerX = event.touches[0].x;
     const fingerY = event.touches[0].y;
     // 判断手指当前在哪个组件的矩形区域内
     let cur = this.detectCurrentComponent(fingerX, fingerY);
     // 获取手指处于组件上的横向比例
     let rate = this.getRateWidth(fingerX, cur);
     if (event.type === TouchType.Move && 0 < rate && rate < this.widthCheckRate) {
       this.isInCheckBox = true;
       // 更新CheckBox状态
       if (cur !== this.curId) {
         this.curId = cur;
         let item = this.itemsMap.get(cur);
         if (item !== undefined) {
           item.checked = !item.checked;
           this.itemsMap.set(cur, item);
         }
       }
     }
     if (event.type === TouchType.Up) {
       setTimeout(() => {
         this.isInCheckBox = false;
       }, 100);
       this.curId = '';
     }
   })
   ```

完整示例参考如下：

```screen
@Entry
@Component
struct CheckBoxTest {
  @State items: Array<CheckBoxStatus> = [];
  // 记录组件的位置信息
  @State itemsMap: Map<string, CheckBoxStatus> = new Map<string, CheckBoxStatus>();
  @State isInCheckBox: boolean = false;
  private componentRects: Map<string, ComponentRect> = new Map(); // 存储组件的位置信息
  private widthCheckRate: number = 0.2; // 选择框所占比例
  private curId: string = ''; // 当前手指所在的组件

  aboutToAppear(): void {
    for (let index = 0; index < 20; index++) {
      this.itemsMap.set(String(index), { id: String(index), name: '选项序号 - ' + index, checked: false });
    }
    this.items = Array.from(this.itemsMap.values());
  }

  build() {
    Column() {
      List({ space: 10 }) {
        ForEach(this.items, (item: CheckBoxStatus) => {
          ListItem() {
            Row() {
              Flex({ justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
                Checkbox()
                  .enabled(false)    // 禁用CheckBox自己的选中逻辑
                  .select(this.itemsMap.get(item.id)?.checked)
              }.width(`${100 * this.widthCheckRate}%`)
              .hitTestBehavior(HitTestMode.Transparent)

              Flex({ alignItems: ItemAlign.Center }) {
                Text(item.name)
                  .fontSize(18)
              }.width(`${100 - 100 * this.widthCheckRate}%`)
            }
            .width('100%')
            .height(50)
          }
          .backgroundColor('#fff1f3f5')
          .borderRadius(10)
          .margin({ left: 16, right: 16 })
          // 组件发生变化时，刷新组件的位置信息
          .onAreaChange((oldVal, newVal) => {
            console.info(`${oldVal},${newVal}`);
            let area: ComponentRect = {
              left: Number(newVal.position.x),
              top: Number(newVal.position.y),
              right: Number(newVal.position.x) + Number(newVal.width),
              bottom: Number(newVal.position.y) + Number(newVal.height)
            };
            this.componentRects.set(item.id, area); // 记录组件位置
          })
        })
      }
      .friction(this.isInCheckBox ? 1000 : 0)
      .onWillScroll(() => {
        // 手指不在CheckBox框位置时，禁止列表滑动
        if (this.isInCheckBox) {
          return { offsetRemain: 0 };
        }
        return;
      })
      .width('100%')
      .height('100%')
    }
    .padding({ top: 10 })
    .width('100%')
    .height('95%')
    .backgroundColor('#ffffffff')
    .onTouch((event) => {
      // 获取当前手指的坐标（相对于父容器，与组件rect的坐标系一致）
      const fingerX = event.touches[0].x;
      const fingerY = event.touches[0].y;
      // 判断手指当前在哪个组件的矩形区域内
      let cur = this.detectCurrentComponent(fingerX, fingerY);
      // 获取手指处于组件上的横向比例
      let rate = this.getRateWidth(fingerX, cur);
      if (event.type === TouchType.Move && 0 < rate && rate < this.widthCheckRate) {
        this.isInCheckBox = true;
        // 更新CheckBox状态
        if (cur !== this.curId) {
          this.curId = cur;
          let item = this.itemsMap.get(cur);
          if (item !== undefined) {
            item.checked = !item.checked;
            this.itemsMap.set(cur, item);
          }
        }
      }
      if (event.type === TouchType.Up) {
        setTimeout(() => {
          this.isInCheckBox = false;
        }, 100);
        this.curId = '';
      }
    })
  }

  // 判断手指当前在哪个组件的矩形区域内
  detectCurrentComponent(x: number, y: number) {
    let cur = '';
    this.componentRects.forEach((rect, id) => {
      if (x >= rect.left && x <= rect.right &&
        y >= rect.top && y <= rect.bottom) {
        cur = id;
      }
    });
    return cur;
  }

  // 获取手指处于组件上的横向比例
  getRateWidth(x: number, index: string) {
    let item = this.componentRects.get(index);
    if (!item) {
      return 0;
    }
    return (x - item.left) / (item.right - item.left);
  }
}

// 记录CheckBox的状态
interface CheckBoxStatus {
  id: string;
  name: string;
  checked: boolean;
}

// 记录组件的位置
interface ComponentRect {
  left: number;
  top: number;
  right: number;
  bottom: number;
}
```
