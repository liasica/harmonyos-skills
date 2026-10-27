---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-uimana-faq-0026
title: 面包屑导航效果实现常见问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 常见问题 > 面包屑导航效果实现常见问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:47:32+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:b140bbd48f23e1f017944e7b24d920a9e0e2beeae0636ad5641a53cb623eb4f2
---

**Q：如何在HarmonyOS中实现面包屑导航的效果，具体演示如下：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/3LfwWFndRwm-GjVrwOK3SA/zh-cn_image_0000002772839722.png "点击放大")

**A**：实现面包屑导航效果的步骤如下：

1. 定义相关类以及数据源transformedData，其中ContentItem用于省市具体内容的展示，MyTabBean用于面包屑导航栏数据的展示。

   ```ts
   export class MyDataItem {
     id: number = 0;
     provinceId: string = '';
     provinceName: string = '';
     cityId: string = '';
     cityName: string = '';
     countyId: string = '';
     countyName: string = '';
   }

   export class ContentItem {
     name: string = '';
     idType: string | null = null;
     idContent: string | null = null;
   }

   export const transformedData: MyDataItem[] =
     [
       {
         'id': 1,
         'provinceId': '110000',
         'provinceName': '江苏省',
         'cityId': '110100000000',
         'cityName': '南京市',
         'countyId': '110101000000',
         'countyName': '江宁区'
       },
       {
         'id': 2,
         'provinceId': '120000',
         'provinceName': '浙江省',
         'cityId': '120100000000',
         'cityName': '杭州市',
         'countyId': '110201000000',
         'countyName': '西湖区'
       },
       {
         'id': 3,
         'provinceId': '130000',
         'provinceName': '河北省',
         'cityId': '130100000000',
         'cityName': '石家庄市',
         'countyId': '130102000000',
         'countyName': '新华区'
       }
     ];

   export class MyTabBean {
     name: string = '';
     idType: string | null = null;
     idContent: string | null = null;
     x: number = -1;
     width: number = -1;

     constructor(name: string) {
       this.name = name;
     }
   }
   ```
2. 添加getDataByIdType方法并绑定到Text组件的点击事件，该方法根据页面当前的情况为MyTabBean和ContentItem变量进行赋值。

   ```ts
   // contentItems为页面数据，titles为导航栏数据
     getDataByIdType(name: string, idType: string | null, idContent: string | null, index?: number) {
       let contentItems: ContentItem[] = [];
       // 获取页面初始数据
       if (idType == null) {
         const seenProvinces: object = Object();
         for (let i = 0; i < transformedData.length; i++) {
           const item = transformedData[i];
           const provinceKey = item.provinceName + item.provinceId;
           if (!seenProvinces[provinceKey]) {
             seenProvinces[provinceKey] = true;
             contentItems.push({
               name: item.provinceName,
               idType: 'province',
               idContent: item.provinceId
             });
           }
         }
       } else {
         // 获取页面当前数据
         for (let i = 0; i < transformedData.length; i++) {
           const item = transformedData[i];
           if (idType === 'province') {
             if (item.provinceId === idContent) {
               contentItems.push({
                 name: item.cityName,
                 idType: 'city',
                 idContent: item.cityId
               });
             }
           } else if (idType === 'city') {
             if (item.cityId === idContent) {
               contentItems.push({
                 name: item.countyName,
                 idType: 'county',
                 idContent: item.countyId
               });
             }
           }
         }
       }
       this.contentList = [...contentItems];

       // 获取导航数据
       if (!idType) {
         this.titles = [new MyTabBean(name)];
       } else {
         if (index) {
           this.titles.splice(index);
         }
         let myTabBean = new MyTabBean(name);
         myTabBean.idType = idType;
         myTabBean.idContent = idContent;
         this.titles.push(myTabBean);
       }
     }
   ```
3. 在根容器Column中使用[ForEach](../harmonyos-guides/arkts-rendering-control-foreach.md)循环渲染出导航栏数据MyTabBean以及省市具体内容ContentItem。

完整示例如下：

```ts
export class MyDataItem {
  id: number = 0;
  provinceId: string = '';
  provinceName: string = '';
  cityId: string = '';
  cityName: string = '';
  countyId: string = '';
  countyName: string = '';
}

export class ContentItem {
  name: string = '';
  idType: string | null = null;
  idContent: string | null = null;
}

export const transformedData: MyDataItem[] =
  [
    {
      'id': 1,
      'provinceId': '110000',
      'provinceName': '江苏省',
      'cityId': '110100000000',
      'cityName': '南京市',
      'countyId': '110101000000',
      'countyName': '江宁区'
    },
    {
      'id': 2,
      'provinceId': '120000',
      'provinceName': '浙江省',
      'cityId': '120100000000',
      'cityName': '杭州市',
      'countyId': '110201000000',
      'countyName': '西湖区'
    },
    {
      'id': 3,
      'provinceId': '130000',
      'provinceName': '河北省',
      'cityId': '130100000000',
      'cityName': '石家庄市',
      'countyId': '130102000000',
      'countyName': '新华区'
    }
  ];

export class MyTabBean {
  name: string = '';
  idType: string | null = null;
  idContent: string | null = null;
  x: number = -1;
  width: number = -1;

  constructor(name: string) {
    this.name = name;
  }
}

@Entry
@Component
struct BreadcrumbTab {
  @State titles: MyTabBean[] = [];
  @State contentList: ContentItem[] = [];

  // contentItems为页面数据，titles为导航栏数据
  getDataByIdType(name: string, idType: string | null, idContent: string | null, index?: number) {
    let contentItems: ContentItem[] = [];
    // 获取页面初始数据
    if (idType == null) {
      const seenProvinces: object = Object();
      for (let i = 0; i < transformedData.length; i++) {
        const item = transformedData[i];
        const provinceKey = item.provinceName + item.provinceId;
        if (!seenProvinces[provinceKey]) {
          seenProvinces[provinceKey] = true;
          contentItems.push({
            name: item.provinceName,
            idType: 'province',
            idContent: item.provinceId
          });
        }
      }
    } else {
      // 获取页面当前数据
      for (let i = 0; i < transformedData.length; i++) {
        const item = transformedData[i];
        if (idType === 'province') {
          if (item.provinceId === idContent) {
            contentItems.push({
              name: item.cityName,
              idType: 'city',
              idContent: item.cityId
            });
          }
        } else if (idType === 'city') {
          if (item.cityId === idContent) {
            contentItems.push({
              name: item.countyName,
              idType: 'county',
              idContent: item.countyId
            });
          }
        }
      }
    }
    this.contentList = [...contentItems];

    // 获取导航数据
    if (!idType) {
      this.titles = [new MyTabBean(name)];
    } else {
      if (index) {
        this.titles.splice(index);
      }
      let myTabBean = new MyTabBean(name);
      myTabBean.idType = idType;
      myTabBean.idContent = idContent;
      this.titles.push(myTabBean);
    }
  }

  aboutToAppear(): void {
    this.getDataByIdType('全部', null, null);
  }

  build() {
    Column() {
      Row() {
        ForEach(this.titles, (item: MyTabBean, index: number) => {
          Row() {
            Text('>').width('44lpx').height('44lpx')
              .textAlign(TextAlign.Start);
            Text(item.name)
              .fontColor(index === this.titles.length - 1 ? '#0A59F7' : '#2E2E2E')
              .fontSize('30lpx');
          }
          .padding({ right: '16lpx', top: '5lpx', bottom: '5lpx' })
          .onClick(() => {
            this.getDataByIdType(item.name, item.idType, item.idContent, index);
          });
        });
      }
      .height('95lpx')
      .align(Alignment.Start)
      .width('100%');

      Column() {
        ForEach(this.contentList, (item: ContentItem) => {
          Column() {
            Text(item.name).fontSize('30lpx').fontColor('#4B4B4B');
          }
          .padding({ top: '20lpx', bottom: '20lpx' })
          .onClick(() => {
            this.getDataByIdType(item.name, item.idType, item.idContent);
          });
        });
      };
    }
    .height('100%')
    .width('100%');
  }
}
```

运行效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/nP1w2jYCTUiuCsj5DIOPBA/zh-cn_image_0000002772679748.png "点击放大")
