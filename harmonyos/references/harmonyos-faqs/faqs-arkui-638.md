---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-638
title: 实现游戏摇杆控制角色移动的动画效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 实现游戏摇杆控制角色移动的动画效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:21+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:754bcaf95f2876d06c2bc8342feea045eb98b588786c6c10d2a83c9d3407de56
---

## 问题现象

在使用ArkTS开发的游戏页面中，希望实现一个游戏摇杆（虚拟摇杆），通过摇杆控制物体的移动。当按下摇杆滑动时，物体应该按照摇杆方向开始移动；当松开摇杆时，角色停止移动，并且摇杆小球恢复原位，此场景应如何实现？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/k5z-XVtrRv-YaXCMTz6Zrg/zh-cn_image_0000002658793777.gif "点击放大")

## 背景知识

* UIContext提供[animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)接口来指定由于闭包代码导致的状态变化插入过渡动效，可在其中设置动画效果相关参数。
* [transition](../harmonyos-references/ts-transition-animation-component.md#transition)用于设置组件插入显示和删除隐藏的过渡效果。

## 解决方案

1. 定义虚拟摇杆。
   * 由两个Circle组成，设置大小圆半径以及摇杆中心区域小球位置以及初始位置。

     ```ts
     Row() {
       Circle({ width: this.maxRadius * 2, height: this.maxRadius * 2 })
         .fill('#20101010')
         .position({ x: this.centerX - this.maxRadius, y: this.centerY - this.maxRadius })
       Circle({ width: this.radius * 2, height: this.radius * 2 })
         .fill('#403A3A3A')
         .position({ x: this.positionX - this.radius, y: this.positionY - this.radius })
     }
     .height(240)
     .width(240)
     .justifyContent(FlexAlign.Center)
     .position({ x: 0, y: 120 })
     .onTouch(this.handleTouchEvent.bind(this))
     ```
   * 通过[onTouch](../harmonyos-references/ts-universal-events-touch.md#ontouch)事件处理触摸操作。TouchType.Move事件中，计算手指相对于摇杆中心的位置，并更新小圆圈的位置。同时，计算出手指与中心点连线的角度和距离，用于控制物体的移动方向和速度。TouchType.Up事件中，停止物体的移动，并将小圆圈复位到摇杆的中心。

     ```ts
     // 处理手指移动的事件
     handleTouchEvent(event: TouchEvent) {
       switch (event.type) {
         case TouchType.Down:
           // 开始定时任务
           this.taskId = setInterval(() => {
             this.personX += this.speed * this.cos;
             this.personY += this.speed * this.sin;
           }, 40);
           break;
         case TouchType.Move:
           // 获取手指位置坐标
           let x = event.touches[0].x;
           let y = event.touches[0].y;
           // 计算手指与中心点的坐标差值
           let vx = x - this.centerX;
           let vy = y - this.centerY;
           // 计算手指与中心点连线和x轴正半轴的夹角，单位是弧度
           let angle = Math.atan2(vy, vx);
           this.sin = Math.sin(angle);
           this.cos = Math.cos(angle);
           // 计算手指与中心点的距离
           let distance = this.getDistance(vx, vy);
           this.getUIContext()?.animateTo(
             { curve: curves.responsiveSpringMotion() },
             () => {
               // 计算摇杆小球的坐标
               this.positionX = this.centerX + distance * this.cos;
               this.positionY = this.centerY + distance * this.sin;
               // 弧度换算角度
               this.angle = angle * 180 / Math.PI;
               this.speed = 5;
             }
           );
           break;
         case TouchType.Up:
           // 还原物体速度
           this.speed = 0;
           // 取消定时任务
           clearInterval(this.taskId);
           // 还原摇杆小球的坐标
           this.getUIContext()?.animateTo(
             { curve: curves.springMotion() },
             () => {
               this.positionX = this.centerX;
               this.positionY = this.centerY;
             }
           );
           break;
       }
     }
     ```
2. 设置动画效果。
   * 通过animateTo方法来平滑地改变物体的位置和摇杆小圆圈的位置。使用responsiveSpringMotion和springMotion方法来实现弹簧动画效果，使移动更加自然。

     ```ts
     this.getUIContext()?.animateTo(
       { curve: curves.responsiveSpringMotion() },
       () => {
         // 计算摇杆小球的坐标
         this.positionX = this.centerX + distance * this.cos;
         this.positionY = this.centerY + distance * this.sin;
         // 弧度换算角度
         this.angle = angle * 180 / Math.PI;
         this.speed = 5;
       }
     );
     ```

     ```ts
     // 还原摇杆小球的坐标
     this.getUIContext()?.animateTo(
       { curve: curves.springMotion() },
       () => {
         this.positionX = this.centerX;
         this.positionY = this.centerY;
       }
     );
     ```
   * 通过[TransitionEffect](../harmonyos-references/ts-transition-animation-component.md#transitioneffect10对象说明)中的combine和animation方法来实现组合动画。

     ```ts
     // 物体图片
     Image(this.src)
       .position({ x: this.personX - 20, y: this.personY - 20 })
       .rotate({ angle: this.angle })
       .transition(TransitionEffect.OPACITY.animation({ duration: 1000 }).combine(
         TransitionEffect.translate({ x: -240 })
       ))
       .width(40)
       .height(40)
     ```
3. 完整示例参考如下：

   ```ts
   import curves from '@ohos.curves';

   @Entry
   @Component
   struct AnimationPageDemo {
     // 物体坐标
     @State personX: number = 200;
     @State personY: number = 120;
     // 物体角度
     @State angle: number = 0;
     // 物体图片
     @State src: Resource = $r('app.media.startIcon');
     // 是否开始游戏
     @State isBegin: boolean = false;
     // 角度正弦和余弦
     sin: number = 0;
     cos: number = 0;
     // 物体移动速度
     speed: number = 0;
     // 任务id
     taskId: number = -1;
     // 摇杆中心区域坐标
     private centerX: number = 120;
     // 摇杆小圆球初始位置
     @State positionX: number = this.centerX;
     private centerY: number = 120;
     @State positionY: number = this.centerY;
     // 大、小圆半径
     private maxRadius: number = 100;
     private radius: number = 20;

     build() {
       Row() {
         Stack() {
           // 开始按钮和物体
           if (!this.isBegin) {
             // 开始按钮
             Button('开始游戏')
               .onClick(() => {
                 this.getUIContext()?.animateTo(
                   { duration: 1000 },
                   () => {
                     // 点击后显示物体
                     this.isBegin = true;
                   }
                 );
               });
           } else {
             // 物体图片
             Image(this.src)
               .position({ x: this.personX - 20, y: this.personY - 20 })
               .rotate({ angle: this.angle })
               .transition(TransitionEffect.OPACITY.animation({ duration: 1000 }).combine(
                 TransitionEffect.translate({ x: -240 })
               ))
               .width(40)
               .height(40)
           }
           // 摇杆
           Row() {
             Circle({ width: this.maxRadius * 2, height: this.maxRadius * 2 })
               .fill('#20101010')
               .position({ x: this.centerX - this.maxRadius, y: this.centerY - this.maxRadius })
             Circle({ width: this.radius * 2, height: this.radius * 2 })
               .fill('#403A3A3A')
               .position({ x: this.positionX - this.radius, y: this.positionY - this.radius })
           }
           .height(240)
           .width(240)
           .justifyContent(FlexAlign.Center)
           .position({ x: 0, y: 120 })
           .onTouch(this.handleTouchEvent.bind(this))
         }
         .height('100%').width('100%')
       }
       .height('100%')
       .width('100%')
     }
     // 处理手指移动的事件
     handleTouchEvent(event: TouchEvent) {
       switch (event.type) {
         case TouchType.Down:
           // 开始定时任务
           this.taskId = setInterval(() => {
             this.personX += this.speed * this.cos;
             this.personY += this.speed * this.sin;
           }, 40);
           break;
         case TouchType.Move:
           // 获取手指位置坐标
           let x = event.touches[0].x;
           let y = event.touches[0].y;
           // 计算手指与中心点的坐标差值
           let vx = x - this.centerX;
           let vy = y - this.centerY;
           // 计算手指与中心点连线和x轴正半轴的夹角，单位是弧度
           let angle = Math.atan2(vy, vx);
           this.sin = Math.sin(angle);
           this.cos = Math.cos(angle);
           // 计算手指与中心点的距离
           let distance = this.getDistance(vx, vy);
           this.getUIContext()?.animateTo(
             { curve: curves.responsiveSpringMotion() },
             () => {
               // 计算摇杆小球的坐标
               this.positionX = this.centerX + distance * this.cos;
               this.positionY = this.centerY + distance * this.sin;
               // 弧度换算角度
               this.angle = angle * 180 / Math.PI;
               this.speed = 5;
             }
           );
           break;
         case TouchType.Up:
           // 还原物体速度
           this.speed = 0;
           // 取消定时任务
           clearInterval(this.taskId);
           // 还原摇杆小球的坐标
           this.getUIContext()?.animateTo(
             { curve: curves.springMotion() },
             () => {
               this.positionX = this.centerX;
               this.positionY = this.centerY;
             }
           );
           break;
       }
     }
     getDistance(x: number, y: number) {
       let d = Math.sqrt(x * x + y * y);
       return Math.min(d, this.maxRadius);
     }
   }
   ```
