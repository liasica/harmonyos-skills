---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-location-16
title: 如何自定义公式计算两点位置坐标的距离
breadcrumb: FAQ > 应用服务开发 > 位置服务（Location Kit） > 如何自定义公式计算两点位置坐标的距离
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6b8a2883ef123de7db3d62facbc155dc8e42339a22d0091afb618f642506d00e
---

## 问题现象

华为地图在中国大陆使用GCJ-02坐标系，但有些服务使用的是WGS-84坐标系，可以通过坐标系切换到WGS-84坐标系来精确计算两个坐标之间的距离。GCJ-02实际上是WGS-84经过加密后的坐标，所以直接用WGS-84的计算方法可能不适用。[Map Kit](../harmonyos-guides/map-kit-guide.md)的距离计算只有一个接口，无法自定义计算公式。

## 背景知识

1. WGS-84坐标系是全球通用的坐标系，用于GPS定位，而GCJ-02坐标系是中国的坐标系，用于国内的电子地图。
2. Haversine公式专指数学领域用于描述球面几何计算的半正矢函数。该术语源于平面三角学中的正矢函数变体，主要应用于地理信息系统（GIS）、导航算法等领域，通过半正矢公式计算球体表面两点间的大圆距离。

## 解决方案

1. 确定坐标系：

   确定两个点的坐标系。假设点A在GCJ-02，点B在WGS-84。
2. 计算两个地理坐标之间的距离通常使用Haversine公式，这个公式适用于地球表面的大圆距离计算。但是这个公式是基于WGS-84坐标系的，GCJ-02是通过一定的偏移算法从WGS-84转换而来的，这个偏移不是简单的线性变换，而是更复杂的算法。所以，如果有一个GCJ-02的坐标，需要先把它转换回WGS-84，才能用Haversine公式计算距离。

   ```ts
   import { map, mapCommon } from '@kit.MapKit';

   let locations: Array<mapCommon.CoordinateLatLng> = [
     {
       // 输入香港坐标和WGS84坐标系，若当前地图站点使用GCJ02坐标系，返回GCJ02坐标系和转换后的香港坐标（输入的坐标转换为GCJ02坐标系）
       coordinateType: mapCommon.CoordinateType.WGS84,
       location: { latitude: 22.280556, longitude: 114.984000 }
     }
   ];

   // 包含await的外层方法需要添加async关键字
   async function rectifyCoordinate(context: Context | undefined): Promise<mapCommon.CoordinateLatLng[]> {
     let arr: Array<mapCommon.CoordinateLatLng> = await map.rectifyCoordinate(context, locations);
     return arr;
   }

   /*
   * 使用 Haversine 公式计算两个经纬度点之间的距离。
   * @param lon1 - 第一个点的经度
   * @param lat1 - 第一个点的纬度
   * @param lon2 - 第二个点的经度
   * @param lat2 - 第二个点的纬度
   * @returns 两点之间的距离（公里）
   */
   function haversine(lon1: number, lat1: number, lon2: number, lat2: number): number {
     const R = 6371; // 地球半径，单位为公里
     const radians = (degrees: number) => degrees * Math.PI / 180.0; // 将角度转换为弧度的函数

     const φ1 = radians(lat1); // 将第一个点的纬度转换为弧度
     const φ2 = radians(lat2); // 将第二个点的纬度转换为弧度
     const λ1 = radians(lon1); // 将第一个点的经度转换为弧度
     const λ2 = radians(lon2); // 将第二个点的经度转换为弧度

     const Δφ = φ2 - φ1; // 计算两个纬度的差值
     const Δλ = λ2 - λ1; // 计算两个经度的差值

     const a = Math.sin(Δφ / 2)**2 + Math.cos(φ1) * Math.cos(φ2) * Math.sin(Δλ / 2)**2; // 计算Haversine公式中的a值
     const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a)); // 计算Haversine公式中的c值（中心角）
     const distance = R * c; // 计算两点之间的距离

     return distance; // 返回计算的距离
   }

   @Entry
   @Component
   struct haversinePage {
     build() {
       Column() {
         Button('Calculate Distance')
           .onClick(() => {
             haversine(114.984000, 22.280556, 115.0, 22.3);
             rectifyCoordinate(this.getUIContext().getHostContext());
           });
       };
     }
   }
   ```

   上述示例给出的距离计算方法的关键应用场景示例可参考[根据实时定位获取经纬度计算距离](../architecture-guides/near_people-0000002237251858.md)。
