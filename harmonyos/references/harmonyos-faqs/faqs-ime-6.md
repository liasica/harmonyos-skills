---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ime-6
title: 如何实现悬浮键盘的拖动效果
breadcrumb: FAQ > 应用框架开发 > 输入法框架 > 输入法开发（IME） > 如何实现悬浮键盘的拖动效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:28+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:195fe0a00d95953da662c1518625ef41d89c120be1b11d5b1833e37f080dc9a4
---

## 问题现象

如何实现输入法的悬浮键盘自由拖动的效果？

## 背景知识

* 实现一个输入法应用流程请参考：[实现输入法应用](../harmonyos-guides/inputmethod-application-guide.md)。
* [Panel](../harmonyos-references/js-apis-inputmethod-panel.md)：输入法面板，当PanelFlag值为FLAG\_FLOATING时处于悬浮态（即悬浮键盘），而执行[moveTo](../harmonyos-references/js-apis-inputmethodengine.md#moveto10)操作时可以实现移动面板位置，若面板状态为固定态，则不会产生实际移动效果。
* [InputMethodExtensionAbility](../harmonyos-references/js-apis-inputmethod-extension-ability.md)：提供了onCreate()和onDestroy()生命周期回调，可以根据需要重写对应的回调方法。

## 解决方案

1. 对悬浮键盘的显示样式进行自定义，并在其对应的悬浮组件的onTouch事件中实现对移动操作的监听。每当悬浮键盘发生拖动时，实时记录其当前的坐标位置，以便后续进行位置更新与布局调整。
2. 当用户在触摸屏或触控设备上进行TouchType.Move滑动操作时，将当前的坐标信息通过emitter即时发送出去，供其他模块订阅和处理。

   ```ts
   import { FrameNode, NodeController, Position } from '@kit.ArkUI';
   import { emitter } from '@kit.BasicServicesKit';
   import { KeyboardController } from '../model/KeyboardController';

   class MyNodeController extends NodeController {
     private rootNode: FrameNode | null = null;
     message: string = "Node";
     left: FrameNode | null = null;

     constructor(message: string) {
       super();
       this.message = message;
     }
     context?: UIContext;
     makeNode(context: UIContext): FrameNode | null {
       let rootNode = new FrameNode(context);
       this.rootNode = rootNode;
       this.context = context;
       return this.rootNode;
     }
   }

   @Entry
   @Component
   struct Index {
     adjustSizeX: number = 0;
     adjustSizeY: number = 0;
     adjustSizeWidth: number = 0;
     adjustSizeHeight: number = 0;
     adjustSizeMoveStartPos: Position = { x: -1, y: -1 };
     private myNodeController: MyNodeController = new MyNodeController("D");

     build() {
       RelativeContainer() {
         Stack() {
           NodeContainer(this.myNodeController)
             .width('100%')
             .height(300)
             .backgroundColor('#e2e2e2');
           Text('拖动悬浮键盘区域');
         };
       }
       .width('100%')
       .height('100%')
       .onTouch((event) => {
         this.adjustSize(event);
       });
     }
     // 键盘拖动时判断大小位置信息
     adjustSize(event: TouchEvent) {
       if (!event) {
         return;
       }
       const firstTouch = event.touches[0];
       let displayX = Math.round(firstTouch.displayX);
       let displayY = Math.round(firstTouch.displayY);
       switch (event.type) {
         // 按下状态
         case TouchType.Down:
           this.adjustSizeMoveStartPos.x = displayX;
           this.adjustSizeMoveStartPos.y = displayY;
           this.adjustSizeX = KeyboardController.floatWindowRect.left;
           this.adjustSizeY = KeyboardController.floatWindowRect.top;
           this.adjustSizeWidth = KeyboardController.floatWindowRect.right - KeyboardController.floatWindowRect.left;
           this.adjustSizeHeight = KeyboardController.floatWindowRect.bottom - KeyboardController.floatWindowRect.top;
           break;
         case TouchType.Move:
           let offsetX = displayX - this.adjustSizeMoveStartPos.x;
           let offsetY = displayY - this.adjustSizeMoveStartPos.y;
           this.adjustSizeX = this.adjustSizeX + this.getUIContext().vp2px(offsetX);
           this.adjustSizeY = this.adjustSizeY + this.getUIContext().vp2px(offsetY);
           this.adjustSizeWidth = 650;
           this.adjustSizeHeight = 650;
           if (this.adjustSizeX < 0) {
             this.adjustSizeX = 0;
           }
           if (this.adjustSizeY < 0) {
             this.adjustSizeY = 0;
           }
           // 悬浮键盘被拖动时，记录拖动的坐标位置
           let eventData: emitter.EventData = {
             data: {
               "x": this.adjustSizeX,
               "y": this.adjustSizeY,
               "width": this.adjustSizeWidth,
               "height": this.adjustSizeHeight
             }
           };
           KeyboardController.floatWindowRect.left = this.adjustSizeX;
           KeyboardController.floatWindowRect.top = this.adjustSizeY;
           KeyboardController.floatWindowRect.right = this.adjustSizeX + this.adjustSizeWidth;
           KeyboardController.floatWindowRect.bottom = this.adjustSizeY + this.adjustSizeHeight;
           // 使用emitter传递键盘位置信息
           emitter.emit('onResize', eventData);
           this.adjustSizeMoveStartPos.x = displayX;
           this.adjustSizeMoveStartPos.y = displayY;
           break;
         case TouchType.Cancel:
         case TouchType.Up:
           break;
       }
     }
   }
   ```
3. 在onCreate方法中完成对输入法框架事件监听的注册后，即可实现对该组件所关联的键盘通用事件进行监听，从而确保相关事件能够被正确捕获与响应。
4. 在KeyboardController页面中，当接收到由拖动行为所产生的位置信息时，页面将执行相应的逻辑处理。具体而言，页面会调用this.panel?.moveTo(x, y)方法，通过传入当前获取到的坐标值x与y，将悬浮键盘的面板移动至指定的新位置，实现其在屏幕上的动态定位与调整。

   ```ts
   import { Rect } from '@kit.ArkUI';
   import { inputMethodEngine, InputMethodExtensionContext } from '@kit.IMEKit';
   import { emitter } from '@kit.BasicServicesKit';

   // 调用输入法框架的getInputMethodAbility方法获取实例，并由此实例调用输入法框架功能接口
   const inputMethodAbility: inputMethodEngine.InputMethodAbility = inputMethodEngine.getInputMethodAbility();

   export class KeyboardController {
     private mContext: InputMethodExtensionContext | undefined = undefined;
     private panel: inputMethodEngine.Panel | undefined = undefined;

     public onCreate(context: InputMethodExtensionContext): void {
       this.mContext = context;
       this.initWindow(); // 初始化窗口
       this.registerListener(); // 注册对输入法框架的事件监听
     }
     // 应用生命周期销毁
     public onDestroy(): void {
       this.unRegisterListener(); // 取消事件监听
       if (this.panel) {
         this.panel.hide(); // 销毁窗口
         inputMethodAbility.destroyPanel(this.panel);
       }
       if (this.mContext) {
         this.mContext.destroy();
       }
     }
     // 初始化窗口
     private initWindow(): void {
       if (this.mContext === undefined) {
         return;
       }
       let panelInfo: inputMethodEngine.PanelInfo = {
         type: inputMethodEngine.PanelType.SOFT_KEYBOARD,
         flag: inputMethodEngine.PanelFlag.FLG_FLOATING
       };

       inputMethodAbility.createPanel(this.mContext, panelInfo).then(async (inputPanel: inputMethodEngine.Panel) => {
         this.panel = inputPanel;
         if (this.panel) {
           await this.adjustSize();
           await this.panel.setUiContent('InputMethodExtensionAbility/pages/Index');
         }
       });
     }

     async adjustSize() {
       let x = KeyboardController.floatWindowRect.left;
       let y = KeyboardController.floatWindowRect.top;
       let w = KeyboardController.floatWindowRect.right - KeyboardController.floatWindowRect.left;
       let h = KeyboardController.floatWindowRect.bottom - KeyboardController.floatWindowRect.top;
       // 设置输入法应用横竖屏大小
       this.panel?.adjustPanelRect(inputMethodEngine.PanelFlag.FLG_FLOATING, {
         landscapeRect: {
           left: x,
           top: y,
           width: w,
           height: h
         },
         portraitRect: {
           left: x,
           top: y,
           width: w,
           height: h
         }
       });
     }
     public static floatWindowRect: Rect = {
       left: 325,
       top: 1300,
       right: 975,
       bottom: 1950
     };
     private registerListener(): void {
       this.registerInputListener(); // 注册对输入法框架服务的监听
       // 注册隐藏键盘事件监听等
     }
     // 注册对输入法框架服务的开启及停止事件监听
     private registerInputListener(): void {
       emitter.on('onResize', async (data: emitter.EventData) => {
         console.info(`eventData: ${JSON.stringify(data)}`);
         this.adjustSize();
       });
     }
     private unRegisterListener(): void {
       emitter.off('onResize');
     }
   }
   const keyboardController = new KeyboardController();

   export default keyboardController;
   ```
