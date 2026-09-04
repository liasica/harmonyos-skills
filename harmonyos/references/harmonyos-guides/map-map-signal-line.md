---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-map-signal-line
title: 信号路线
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 在地图上绘制 > 信号路线
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:12+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:3650b2f0b2dfa645499f3271efbdf41ef270b59dd7c872408ff604c20d245d59
---

## 场景介绍

从26.0.0开始，新增支持信号路线功能。

信号路线是一条能够动态反映地图上信号强度的彩色折线。信号路线可预测路线中的弱信号或无信号路段，提前提醒用户下载离线地图、提升户外安全性。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/zglFX4liQweOzobHYuilBQ/zh-cn_image_0000002742004247.jpg "点击放大")

## 约束与限制

* 该能力仅面向完成企业认证开发者开放，个人开发者不支持申请。
* 设备限制：信号路线功能仅适用于Phone、Tablet、PC/2in1和Wearable。
* 场景限制：

  1. 申请场景需与地图展示、路线规划、户外出行决策有明确关联，开发者申请该权益时，应基于Map Kit地图能力集成使用。常见的申请场景示例如下。

     + 专业户外徒步类应用：户外徒步路线循迹导航。
     + 专业户外骑行类应用：户外骑行路线循迹导航。
     + 专业户外跑步类应用：户外跑步路线循迹导航。
     + 专业道路救援类应用：规划可用救援路线。
  2. 申请场景需与网络质量信息存在明确关联，如自驾路线推荐、徒步路线规划、户外救援保障等。
  3. 以下场景不支持申请：

     + 用于运营商网络质量对比宣传。
     + 对信号图层进行批量下载、离线存储或二次分发。

## 接口说明

信号路线功能主要由[MapSignalParams](../harmonyos-references/map-common.md#mapsignalparams)、[addSignalLine](../harmonyos-references/map-map-mapcomponentcontroller.md#addsignalline)、[MapSignalLine](../harmonyos-references/map-map-mapsignalline.md)提供，更多接口及使用方法请参见[接口文档](../harmonyos-references/map-map-mapsignalline.md)。

| 接口名 | 描述 |
| --- | --- |
| [MapSignalParams](../harmonyos-references/map-common.md#mapsignalparams) | 信号路线的属性。 |
| [addSignalLine](../harmonyos-references/map-map-mapcomponentcontroller.md#addsignalline)(params: mapCommon.[MapSignalParams](../harmonyos-references/map-common.md#mapsignalparams)): Promise<[MapSignalLine](../harmonyos-references/map-map-mapsignalline.md)> | 新增信号路线。 |
| [MapSignalLine](../harmonyos-references/map-map-mapsignalline.md) | 信号路线管理对象。 |

## 开通信号预测能力

使用信号路线功能需要先开通信号预测能力。

**说明** 

权限申请入口目前仅针对企业开发者开放，个人开发者不可见。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，选择“开发与服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/BA3Vld2xQB2pmY253tDqpw/zh-cn_image_0000002712405258.jpg)
2. 在项目列表中找到需要开通“信号预测能力”的应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/yxg1IM5aStmefsQtxBv5Hw/zh-cn_image_0000002742124207.jpg)
3. 进入“开放能力管理”页签，找到“地图服务”开关下的“信号预测能力”，点击“申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/5F3334LiQTWl_NFra15hkQ/zh-cn_image_0000002712245300.jpg)
4. 确认您已满足开通信号预测能力的所有条件后，点击“下一步”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/ih9juAfDT22HehZAlgf2Ww/zh-cn_image_0000002742004249.jpg)
5. 填写申请原因。

   **说明** 

   申请原因填写模板：

   * **应用介绍**：说明应用类型，例如XXX应用属于XXX类型的应用。
   * **使用场景**：说明权限使用场景，例如在XXX场景下，需要使用XX能力。
   * **申请用途**：描述该权限的用途，例如用户使用XXX功能后，进行XXX操作，提供XXX服务。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/irMTkVozSR6f_-br73AiUQ/zh-cn_image_0000002712405260.jpg)
6. 系统将推送消息到互动中心，请等待审核。3个工作日内审核结果会通过站内消息的形式发送到[互动中心](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/interactive)，请注意查收。
7. 审核通过后，勾选“地图服务”和“信号预测能力”以完成配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/e3bmYLoeS1uptXGR2cny1w/zh-cn_image_0000002742124209.jpg)

## 开发步骤

### 添加信号路线

1. 导入相关模块。

   ```typescript
   import { MapComponent, mapCommon, map } from '@kit.MapKit';
   import { AsyncCallback } from '@kit.BasicServicesKit';
   ```
2. 绘制信号路线。

   ```typescript
   @Entry
   @Component
   struct MapSignalLineDemo {
     // ...
     private mapOptions?: mapCommon.MapOptions;
     private mapController?: map.MapComponentController;
     private callback?: AsyncCallback<map.MapComponentController>;
     private mapSignalLine?: map.MapSignalLine;

     aboutToAppear(): void {
       this.mapOptions = {
         position: {
           target: {
             latitude: 32.055583099352,
             longitude: 118.540076398149
           },
           zoom: 14
         }
       };

       this.callback = async (err, mapController) => {
         if (!err) {
           this.mapController = mapController;
           let mapSignalParams: mapCommon.MapSignalParams = {
             signalId: 'signalId1'
           };
           mapSignalParams.points =
             [{ longitude: 118.553695, latitude: 32.050789 }, { longitude: 118.553738, latitude: 32.050884 },
               { longitude: 118.548506, latitude: 32.048543 }, { longitude: 118.548413, latitude: 32.048374 },
               { longitude: 118.547185, latitude: 32.048252 }, { longitude: 118.546939, latitude: 32.048296 },
               { longitude: 118.544343, latitude: 32.048765 }, { longitude: 118.544098, latitude: 32.048780 },
               { longitude: 118.538145, latitude: 32.048836 }, { longitude: 118.537896, latitude: 32.048846 },
               { longitude: 118.537654, latitude: 32.048818 }, { longitude: 118.537446, latitude: 32.048708 },
               { longitude: 118.532201, latitude: 32.049620 }, { longitude: 118.532076, latitude: 32.049583 },
               { longitude: 118.531726, latitude: 32.049490 }, { longitude: 118.531593, latitude: 32.049475 },
               { longitude: 118.531466, latitude: 32.049443 }, { longitude: 118.528349, latitude: 32.052531 },
               { longitude: 118.528298, latitude: 32.053657 }, { longitude: 118.528288, latitude: 32.053851 },
               { longitude: 118.527082, latitude: 32.054653 }, { longitude: 118.526755, latitude: 32.054781 },
               { longitude: 118.526755, latitude: 32.054857 }, { longitude: 118.526654, latitude: 32.055124 },
               { longitude: 118.529706, latitude: 32.057719 }, { longitude: 118.530101, latitude: 32.057906 },
               { longitude: 118.530211, latitude: 32.057911 }, { longitude: 118.532985, latitude: 32.058305 },
               { longitude: 118.538524, latitude: 32.057508 }, { longitude: 118.538571, latitude: 32.057418 },
               { longitude: 118.540255, latitude: 32.058049 }, { longitude: 118.540545, latitude: 32.058251 },
               { longitude: 118.540655, latitude: 32.058285 }, { longitude: 118.543645, latitude: 32.059025 },
               { longitude: 118.543763, latitude: 32.059010 }, { longitude: 118.545292, latitude: 32.059901 },
               { longitude: 118.545397, latitude: 32.059912 }, { longitude: 118.548790, latitude: 32.063339 },
               { longitude: 118.549064, latitude: 32.063531 }, { longitude: 118.550198, latitude: 32.064369 },
               { longitude: 118.552740, latitude: 32.059904 }, { longitude: 118.552866, latitude: 32.059620 },
               { longitude: 118.552929, latitude: 32.059516 }, { longitude: 118.553045, latitude: 32.059157 },
               { longitude: 118.553078, latitude: 32.059049 }, { longitude: 118.553186, latitude: 32.056241 },
               { longitude: 118.553204, latitude: 32.056126 }, { longitude: 118.553062, latitude: 32.053036 },
               { longitude: 118.553555, latitude: 32.051478 }, { longitude: 118.553626, latitude: 32.051203 },
               { longitude: 118.553650, latitude: 32.050680 }, { longitude: 118.553684, latitude: 32.050578 }];

           // 添加信号线
           try {
             this.mapSignalLine = await this.mapController.addSignalLine(mapSignalParams);
           } catch (e) {
             console.error(`Failed to create the signalLine, code is：${e.code}, message is ${e.message}`);
           }
         } else {
           // 地图初始化失败
           console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
         }
       };
     }

     build() {
       // ...
         Stack() {
           Column() {
             MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback });
           }.width('100%')
         }.height('100%')

         // ...
     }
   }
   ```

### 移除地图信号路线数据缓存

通过[removeSignalLineCache](../harmonyos-references/map-map-mapcomponentcontroller.md#removesignallinecache)，移除地图信号路线缓存，释放存储空间。

```typescript
// 删除信号路线ID为signalId1的缓存
let mapSignalParams: mapCommon.MapSignalParams = {
  signalId: 'signalId1'
};
mapSignalParams.points =
  [{ longitude: 118.553695, latitude: 32.050789 }, { longitude: 118.553738, latitude: 32.050884 },
    { longitude: 118.548506, latitude: 32.048543 }, { longitude: 118.548413, latitude: 32.048374 },
    { longitude: 118.547185, latitude: 32.048252 }, { longitude: 118.546939, latitude: 32.048296 }];
// 首次添加信号路线会自动缓存该路线信息
try {
  let mapSignalLine1 = await this.mapController.addSignalLine(mapSignalParams);
  // 删除后，以相同signalId（points不传值）添加路线时，会触发缓存
  mapSignalLine1.remove();
  let mapSignalLine2 = await this.mapController.addSignalLine({signalId: mapSignalParams.signalId});
  // 再次删除，且通过removeSignalLineCache，可以移除地图信号路线缓存。
  mapSignalLine2.remove();
  this.mapController?.removeSignalLineCache(mapSignalParams.signalId);
} catch (e) {
  console.error(`Operation failed, code is：${e.code}, message is ${e.message}`);
}
```
