---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-787
title: 如何实现List联动滑动，子项点击弹出自定义气泡
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现List联动滑动，子项点击弹出自定义气泡
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:24+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b59079c4ca44739f3ffae73de95abc609b3cbe8f8f96de8ac86f25ebc55d4f84
---

## 问题现象

实现功能效果：页面左侧是数据列表，右侧有导航字母表，一一对应，点击导航字母表中字母，数据表滚动到对应的内容位置。

导航字母表数据样式较小，点击子项item时弹出自定义的气泡显示点击的字母内容。

## 背景知识

* [Popup](../harmonyos-guides/arkts-popup-and-menu-components-popup.md)属性可绑定在组件上显示气泡弹窗提示，设置弹窗内容、交互逻辑和显示状态。主要用于屏幕录制、信息弹出提醒等显示状态。
* [scrollToIndex](../harmonyos-references/ts-container-scroll.md#scrolltoindex)滑动到指定Index，支持设置滑动额外偏移量。
* [ListItemGroup](../harmonyos-references/ts-container-listitemgroup.md)用来展示列表item分组，宽度默认充满List组件，必须配合List组件来使用。

## 解决方案

可以通过双重List联动滑动实现导航表绑定数据列表的滑动，通过bindPopup绑定自定义气泡。

1. 通过List和ListItemGroup显示分类数据列表。

   ```ts
   List({ scroller: this.categoryScroller }) {
     ListItemGroup({ header: this.itemHead('当前') }) {
       ListItem() {
         Text(this.currentCategory)
           .width('100%')
           .height(45)
           .fontSize(16)
           .textAlign(TextAlign.Start)
           .backgroundColor(0xFFFFFF)
           .padding({ left: 10 });
       };
     };

     ListItemGroup({ header: this.itemHead('热门') }) {
       ForEach(this.hotCategories, (hotCategory: string) => {
         ListItem() {
           Text(hotCategory)
             .width('100%')
             .height(45)
             .fontSize(16)
             .textAlign(TextAlign.Start)
             .backgroundColor(0xFFFFFF)
             .padding({ left: 10 });
         };
       });
     };

     // A~L字母分组
     ForEach(this.groupNameList, (item: string) => {
       ListItemGroup({ header: this.itemHead(item) }) {
         ForEach(this.getCitiesWithGroupName(item), (item: Category) => {
           ListItem() {
             Text(item.category)
               .width('100%')
               .height(45)
               .fontSize(16)
               .textAlign(TextAlign.Start)
               .backgroundColor(0xFFFFFF)
               .padding({ left: 10 });
           };
         }, (item: Category) => item.category);
       };
     });
   }
   ```
2. 使用List组件显示导航字母表，点击时控制数据表scrollToIndex跳转到对应的位置。

   ```ts
   this.categoryScroller.scrollToIndex(index + 2, true, ScrollAlign.START);
   ```
3. 给导航字母表子项item绑定Popup气泡，设置气泡参数，传入自定义builder。

   ```ts
   .bindPopup(this.selectGroupIndex === index && this.handlePopup, {
     builder: this.popupBuilder(item),
     placement: Placement.Left,
     radius: '50%',
     mask: { color: '#33000000' },
     popupColor: Color.Transparent, // 设置气泡的背景色
     arrowHeight: 10, // 设置气泡箭头高度
     arrowWidth: 20, // 设置气泡箭头宽度
     offset: { x: -10 },
   });
   ```

完整示例如下：

```ts
interface CategoriesType {
  current: string[],
  hot: string[],
  categories: Map<string, Category[]>
}

interface Category {
  code: string;
  category: string;
}

@Entry
@Component
export default struct CityList {
  @State handlePopup: boolean = false;
  private currentCategory: string = '';
  private hotCategories: string[] = [];
  private groupCategories: Map<string, Category[]> = new Map;
  private groupNameList: string[] = ['A', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L'];
  @State private selectGroupIndex: number = -1;
  private categoryScroller: ListScroller = new ListScroller();
  private categoryScroller1: ListScroller = new ListScroller();
  private isClickScroll: boolean = false;

  aboutToAppear() {
    let jsonString: string =
      '{"current":["保健品种"],"hot":["险种转换","保单挂失","保单补发"],"categories":{"A":[{"code":"001","category":"新增附加险"},{"code":"002","category":"保险附加1"},{"code":"003","category":"保险附加2"},{"code":"004","category":"保险附加3"},{"code":"005","category":"保险附加4"},{"code":"006","category":"保险附加5"},{"code":"007","category":"保险附加6"}],"B":[{"code":"008","category":"保险附加1"},{"code":"009","category":"保险附加2"},{"code":"012","category":"保险附加3"}],"C":[{"code":"008","category":"保险附加1"},{"code":"009","category":"保险附加2"},{"code":"010","category":"保险附加3"},{"code":"011","category":"保险附加4"},{"code":"012","category":"保险附加5"}],"D":[{"code":"008","category":"保险附加1"},{"code":"009","category":"保险附加2"},{"code":"010","category":"保险附加3"},{"code":"011","category":"保险附加4"},{"code":"012","category":"保险附加5"}],"E":[{"code":"008","category":"保险附加1"},{"code":"009","category":"保险附加2"},{"code":"010","category":"保险附加3"},{"code":"011","category":"保险附加4"},{"code":"012","category":"保险附加5"}],"F":[{"code":"008","category":"保险附加1"},{"code":"009","category":"保险附加2"},{"code":"010","category":"保险附加3"},{"code":"011","category":"保险附加4"},{"code":"012","category":"保险附加5"}],"G":[{"code":"008","category":"保险附加1"},{"code":"009","category":"保险附加2"},{"code":"010","category":"保险附加3"},{"code":"011","category":"保险附加4"},{"code":"012","category":"保险附加5"}],"H":[{"code":"008","category":"保险附加1"},{"code":"009","category":"保险附加2"},{"code":"010","category":"保险附加3"},{"code":"011","category":"保险附加4"},{"code":"012","category":"保险附加5"}],"J":[{"code":"008","category":"保险附加1"},{"code":"009","category":"保险附加2"},{"code":"010","category":"保险附加3"},{"code":"011","category":"保险附加4"},{"code":"012","category":"保险附加5"}],"K":[{"code":"008","category":"保险附加1"},{"code":"009","category":"保险附加2"},{"code":"010","category":"保险附加3"},{"code":"011","category":"保险附加4"},{"code":"012","category":"保险附加5"}],"L":[{"code":"008","category":"保险附加1"},{"code":"009","category":"保险附加2"},{"code":"010","category":"保险附加3"},{"code":"011","category":"保险附加4"},{"code":"012","category":"保险附加5"}]}}';
    let data: CategoriesType = JSON.parse(jsonString) as CategoriesType;
    this.currentCategory = data.current[0];
    this.hotCategories = data.hot;
    this.groupCategories = data.categories;
  }

  build() {
    Stack() {
      Column() {
        this.categoryList();
      }
      .height('100%');

      Row() {
        this.navigationList();
      }
      .width(42)
      .height('100%')
      .margin({ left: 200 });

    };
  }

  getCitiesWithGroupName(name: string): Category[] {
    return this.groupCategories[name];
  }

  @Builder
  itemHead(text: string) {
    Text(text)
      .fontSize(16)
      .width('100%')
      .padding({ left: 10 })
      .height(45)
      .backgroundColor(0xEEEEEE);
  }

  @Builder
  categoryList() {
    List({ scroller: this.categoryScroller }) {
      ListItemGroup({ header: this.itemHead('当前') }) {
        ListItem() {
          Text(this.currentCategory)
            .width('100%')
            .height(45)
            .fontSize(16)
            .textAlign(TextAlign.Start)
            .backgroundColor(0xFFFFFF)
            .padding({ left: 10 });
        };
      };

      ListItemGroup({ header: this.itemHead('热门') }) {
        ForEach(this.hotCategories, (hotCategory: string) => {
          ListItem() {
            Text(hotCategory)
              .width('100%')
              .height(45)
              .fontSize(16)
              .textAlign(TextAlign.Start)
              .backgroundColor(0xFFFFFF)
              .padding({ left: 10 });
          };
        });
      };

      // A~L字母分组
      ForEach(this.groupNameList, (item: string) => {
        ListItemGroup({ header: this.itemHead(item) }) {
          ForEach(this.getCitiesWithGroupName(item), (item: Category) => {
            ListItem() {
              Text(item.category)
                .width('100%')
                .height(45)
                .fontSize(16)
                .textAlign(TextAlign.Start)
                .backgroundColor(0xFFFFFF)
                .padding({ left: 10 });
            };
          }, (item: Category) => item.category);
        };
      });
    }
    .width('100%')
    .height('100%')
    .scrollBar(BarState.Off)
    .sticky(StickyStyle.Header)
    .onTouch(() => {
      // 分列表触摸滚动，isClickScroll=false，防止滚动过程中与导航列表触发滚动冲突
      this.isClickScroll = false;
    })
    .onScrollIndex((start: number) => {
      // 通过selectGroupIndex状态变量与start联动控制导航列表选中状态
      if (!this.isClickScroll) {
        this.selectGroupIndex = start - 2;
      }
    });
  }

  @Builder
  popupBuilder(item: string) {
    Row({ space: 2 }) {
      Text(item);
    }.width(50).height(50).borderRadius('50%').justifyContent(FlexAlign.Center);
  }

  @Builder
  navigationList() {
    List({ scroller: this.categoryScroller1 }) {
      ForEach(this.groupNameList, (item: string, index: number) => {
        ListItem() {
          Column() {
            Text(item)
              .width(42)
              .height(30)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .backgroundColor(index === this.selectGroupIndex ? 0xCCCCCC : Color.Transparent)
              .borderRadius(15)
              .onClick(() => {
                // 导航列表选中isClickScroll=true，防止与分列表滚动过程中带动导航列表状态变化
                this.isClickScroll = true;
                this.selectGroupIndex = index;
                // 通过导航选中selectGroupIndex与Scroller控制分列表滚动到对应位置
                this.categoryScroller.scrollToIndex(index + 2, true, ScrollAlign.START);
                this.handlePopup = !this.handlePopup;
                setTimeout(() => {
                  this.handlePopup = !this.handlePopup;
                }, 1000);
              })
              .bindPopup(this.selectGroupIndex === index && this.handlePopup, {
                builder: this.popupBuilder(item),
                placement: Placement.Left,
                radius: '50%',
                mask: { color: '#33000000' },
                popupColor: Color.Transparent, // 设置气泡的背景色
                arrowHeight: 10, // 设置气泡箭头高度
                arrowWidth: 20, // 设置气泡箭头宽度
                offset: { x: -10 },
              });
          };
        };
      }, (item: string) => item);
    }
    .backgroundColor(Color.Transparent)
    .width('100%');
  }
}
```
