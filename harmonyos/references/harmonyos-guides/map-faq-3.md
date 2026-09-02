---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-faq-3
title: 手势卡顿或者不生效
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > Map Kit常见问题 > 手势卡顿或者不生效
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:29+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:b4215b7e9a434417965c85001bc614ce7d40de2de056b2d973d9151c2fb5eaec
---

**现象描述**

地图页面操作手势卡顿或者不生效。

**可能原因**

1. 手势遮盖或者手势冲突。

   * 手势遮盖：地图组件的上层存在没有做手势穿透的组件。
   * 手势冲突：以Swiper容器组件中使用地图组件为例，Swiper容器组件和地图组件手势会存在冲突。
2. 主线程阻塞。

   应用主线程处理大批量逻辑时，存在主线程阻塞，此时进行地图手势操作，手势应答会变慢甚至手势响应失败。

**处理步骤**

1. 手势遮盖或者手势冲突。

   * 手势遮盖：参考[触摸测试控制](../harmonyos-references/ts-universal-attributes-hit-test-behavior.md)做手势穿透。
   * 手势冲突：以Swiper容器组件和地图组件手势存在冲突为例，解决方案参考如下代码：

     ```typescript
     import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
     import { map, mapCommon, MapComponent } from '@kit.MapKit';

     class MyDataSource implements IDataSource {
       private list: number[] = [];

       constructor(list: number[]) {
         this.list = list;
       }

       // 获取数组长度
       totalCount(): number {
         return this.list.length;
       }

       // 根据索引获取数据
       getData(index: number): number {
         return this.list[index];
       }

       // 注册数据变化监听器
       registerDataChangeListener(listener: DataChangeListener): void {
       }

       // 取消注册数据变化监听器
       unregisterDataChangeListener(listener: DataChangeListener): void {
       }
     }

     @Entry
     @Component
     struct SwiperExample {
       private swiperController: SwiperController = new SwiperController();
       private data: MyDataSource = new MyDataSource([]);
       private mapOptions?: mapCommon.MapOptions;
       private callback?: AsyncCallback<map.MapComponentController>;
       private mapController?: map.MapComponentController;
       private mapEventManager?: map.MapEventManager;
       @State mapPositionX: number = 0;
       @State mapPositionY: number = 0;
       @State mapHeight: number = 0;
       @State mapWidth: number = 0;
       @State index: number = 0;

       // 判断坐标是否在地图矩形内
       isMap(event: TouchEvent) {
         if (event.changedTouches[0].displayX > this.mapPositionX
           && event.changedTouches[0].displayX < this.mapPositionX + this.mapWidth
           && event.changedTouches[0].displayY > this.mapPositionY
           && event.changedTouches[0].displayY < this.mapPositionY + this.mapHeight) {
           return true;
         }
         return false;
       }

       aboutToAppear(): void {
         let list: number[] = [];
         for (let i = 1; i <= 10; i++) {
           list.push(i);
         }
         this.data = new MyDataSource(list);

         this.mapOptions = {
           position: {
             target: {
               latitude: 31.98441025,
               longitude: 118.766253
             },
             zoom: 10,
             tilt: 10,
             bearing: 90
           },
           scaleControlsEnabled: true
         }

         this.callback = async (err, mapController) => {
           if (!err) {
             this.mapController = mapController;
             this.mapEventManager = this.mapController.getEventManager();
             let callback = () => {
               console.info(`on-mapLoad`);
             };
             this.mapEventManager.on("mapLoad", callback);
           } else {
             console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
           }
         }
       }

       build() {
         Column({ space: 5 }) {
           Swiper(this.swiperController) {
             LazyForEach(this.data, (item: string) => {
               if (item == "3") {
                 Column() {
                   Text(item.toString())
                     .width('90%')
                     .height(160)
                     .backgroundColor(0xAFEEEE)
                     .textAlign(TextAlign.Center)
                     .fontSize(30)
                   MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback })
                     // 获取MapComponent的位置和长宽
                     .width('100%')
                     .height('65%')
                     .onAreaChange((_oldValue: Area, newValue: Area) => {
                       try {
                         if (newValue.globalPosition.x !== undefined && newValue.globalPosition.y !== undefined) {
                           this.mapPositionX = Number(newValue.globalPosition.x);
                           this.mapPositionY = Number(newValue.globalPosition.y);
                           this.mapHeight = Number(newValue.height);
                           this.mapWidth = Number(newValue.width);
                         }
                       } catch (error) {
                         let e: BusinessError = error as BusinessError;
                         console.error("onAreaChange error code:" + e.code + "message:" + e.message);
                       }
                     })
                 }.height("100%")
               } else {
                 Text(item.toString())
                   .width('90%')
                   .height(160)
                   .backgroundColor(0xAFEEEE)
                   .textAlign(TextAlign.Center)
                   .fontSize(30)
               }
             }, (item: string) => item)
           }
           // 手势判断 当index为存在地图页面且点击在地图矩形内时为HitTestMode.None（不响应Swiper手势，响应子组件手势）
           .onTouchIntercept((event: TouchEvent) => {
             if (this.index === 2 && this.isMap(event)) {
               return HitTestMode.None;
             }
             return HitTestMode.Transparent;
           })
           .cachedCount(2)
           .index(1)
           .loop(true)
           .itemSpace(0)
           // 设置圆点导航点样式
           .indicator(
             new DotIndicator()
               .itemWidth(15)
               .itemHeight(15)
               .selectedItemWidth(15)
               .selectedItemHeight(15)
               .color(Color.Gray)
               .selectedColor(Color.Blue))
           .displayArrow({
             // 设置导航点箭头样式
             showBackground: true,
             isSidebarMiddle: true,
             backgroundSize: 24,
             backgroundColor: Color.White,
             arrowSize: 18,
             arrowColor: Color.Blue
           }, false)
           .curve(Curve.Linear)
           .onChange((index: number) => {
             this.index = index;
           })
           .onGestureSwipe((index: number, extraInfo: SwiperAnimationEvent) => {
             console.info("index: " + index);
             console.info("current offset: " + extraInfo.currentOffset);
           })

           Row({ space: 12 }) {
             Button('showNext')
               .onClick(() => {
                 this.swiperController.showNext();
               })
             Button('showPrevious')
               .onClick(() => {
                 this.swiperController.showPrevious();
               })
           }.margin(5)
         }.width('100%')
         .margin({ top: 5 })
       }
     }
     ```
2. 主线程阻塞。

   请分析应用的业务逻辑，将复杂逻辑放到子线程中处理。
