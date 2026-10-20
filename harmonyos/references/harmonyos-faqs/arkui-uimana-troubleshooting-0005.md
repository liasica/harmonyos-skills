---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-uimana-troubleshooting-0005
title: 窗口横竖屏旋转问题排查与解决
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 故障排查 > 窗口横竖屏旋转问题排查与解决
category: harmonyos-faqs
scraped_at: 2026-10-21T07:11:10+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:0d4d7ba2a0e8f4d6956cd928fa22e0b7e5de05a7d24f408366de8bf0758694ca
---

## 横竖屏切换失败

### 问题现象

用户打开应用尝试切换横屏或竖屏时，切换失败。

### 定位过程

1. 检查代码，在代码中全局搜索module.json5的orientation字段，看是否应用在启动时设置了横竖屏切换。
2. 代码全局中有setPreferredOrientation方法，检查方法设置的参数是否设置成了强制横屏或强制竖屏；或在日志中搜索关键字orientation，如果发现有setWindowOrientation: 1 Succeeded.或OnSetPreferredOrientation end, window [xxxx, xxxx] orientation=1信息。使用orientation的枚举值来判断，如为1时，表示竖屏显示模式，其他枚举值参考背景知识。
3. 代码中既没有在module.json5内配置orientation字段，也没有通过setPreferredOrientation方法设置屏幕方向。

### 分析结论

1. 应用module.json5文件的orientation配置项是固定方向，导致无法横竖屏切换。
2. 应用内配置了setPreferredOrientation(window.Orientation.PORTRAIT)或者setPreferredOrientation(window.Orientation.LANDSCAPE)，使得应用只能竖屏或者横屏展示，导致无法进行横竖屏切换。
3. 应用没有设置setPreferredOrientation方法或module.json5的orientation字段导致不能横竖屏切换。

### 修改建议

1. 将module.json5文件中"orientation"配置项改为可随屏幕重力方向旋转的字段，例如auto\_rotation。详见[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)。
2. 在代码中通过调用窗口window的setPreferredOrientation方法进行设置，例如设置为AUTO\_ROTATION\_RESTRICTED跟随传感器自动旋转且受控制中心的旋转开关控制。代码如下：

   ```ts
   import { common } from '@kit.AbilityKit';
   import { window } from '@kit.ArkUI';

   @Entry
   @Component
   struct OrientationUsagePage {
     message: string = '横竖屏切换示例';

     aboutToAppear(): void {
       let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
       let windowClass: window.Window = context.windowStage.getMainWindowSync();
       windowClass.setPreferredOrientation(window.Orientation.AUTO_ROTATION_RESTRICTED); // 设置屏幕方向为跟随传感器自动旋转且受控制中心的旋转开关控制。
       let systemBarProperties: window.SystemBarProperties = {
         statusBarColor: '#00000000',
       };
       windowClass.setWindowSystemBarProperties(systemBarProperties); // 设置状态栏背景色为透明
     }

     build() {
       Column() {
         Text(this.message)
           .fontSize(30)
           .fontWeight(FontWeight.Bold)
       }
       .height('100%')
       .width('100%')
       .justifyContent(FlexAlign.Center)
     }
   }
   ```

## 应用在横竖屏切换旋转过程中丢帧

### 问题现象

应用切换横竖屏模式，在旋转为横屏或竖屏显示模式的过程中出现丢帧的现象。

### 定位过程

1. 使用DevEco Profiler的Frame模板抓取横竖屏切换旋转过程的Trace。在Frame泳道应用包名子泳道搜索H:WindowSessionImpl::UpdateRectForRotation作为横竖屏切换的起点，可以明显看到在此后有标红Trace点，出现丢帧现象。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/d6wGvP9CTNqFGDrxBp211g/zh-cn_image_0000002795449901.png "点击放大")
2. 点击编号为133的Trace点，在下方的Details中点击Corresponding Slice左侧的箭头按钮，可跳转至应用包名主泳道应用包名主线。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/E_4V56niQa21EgOTqkOowQ/zh-cn_image_0000002766051354.png "点击放大")
3. 跳转至应用包名主线程查看对应帧绘制的Trace信息，观察到泳道中存在大量Measure和Layout相关的Trace点，这是应用在测量组件宽高并进行布局。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/4X1WOQcWR9q0wsNnMXYheA/zh-cn_image_0000002795449907.png "点击放大")
4. 根据这一帧的起始时间和结束时间框选出分析范围，在下方Slice List中过滤出测量任务（H:Measure）和布局（H:Layout）任务。可以看到这一帧进行了254次测量、布局任务，单帧耗时达到23ms。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/TeqOhIx3QqOJLOIZxkSiCQ/zh-cn_image_0000002795449909.png "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/KGcM41kmSda6PcQJ-qyDxg/zh-cn_image_0000002765891426.png "点击放大")
5. 重复以上步骤查看后续帧的绘制情况，发现在长达640ms的旋转过程中单帧绘制耗时均在23ms左右，远超过屏幕刷新率120Hz所要求的8.33ms。综上所述是应用页面结构复杂导致在横竖屏切换时大量组件需要重新测量宽高并布局，造成单帧绘制超时，因而出现丢帧现象。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/2iWowkgZRuWj9ODF9_4ieg/zh-cn_image_0000002766051356.png "点击放大")

### 分析结论

页面结构复杂导致在横竖屏切换时大量组件需要重新测量宽高并布局，造成单帧绘制超时，因而出现丢帧现象。

### 修改建议

针对结构复杂的页面，可进行[组件嵌套优化](../best-practices/bpta-component-nesting-optimization.md)，减少节点数，降低整体性能消耗。

## 横竖屏切换，一二级页面显示不全有截断

### 问题现象

横竖屏切换，页面显示不全有截断。

### 定位过程

1. 当窗口宽度或高度的最小值小于348vp时，可能导致布局无法自适应横竖屏切换，出现内容截断或挤压。检查当前窗口全屏尺寸是否符合设备要求（以MatePad Pro为例，平板窗口全屏时尺寸通常为711\*1137vp，需满足最小348vp阈值）。
2. 检查module.json5中是否正确声明orientation属性。
3. 检查是否在需要强制横竖屏的页面（如视频播放页），未调用[setPreferredOrientation](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)方法动态调整。

   ```ts
       // 示例代码：动态设置竖屏
       this.windowClass.setPreferredOrientation(window.Orientation.USER_ROTATION_PORTRAIT)
   ```
4. 检查是否未针对横竖屏差异设计响应式布局：
   * 组件使用百分比布局替代固定尺寸。
   * 结合栅格系统实现断点适配（如GridRow组件）。

### 分析结论

可能有以下几种原因：

1. 窗口尺寸不足。
2. 旋转策略配置错误。
3. 布局适配不足。

### 修改建议

1. 通过on('windowSizeChange')监听窗口尺寸变化实现动态布局调整，参考[通过断点刷新UI](../best-practices/bpta-multi-device-responsive-layout.md#section175001836203617)。
2. 旋转策略配置可参考[配置module.json5的orientation字段](../best-practices/bpta-landscape-and-portrait-development.md#section1188593118171)。
3. 使用百分比布局替代固定尺寸。以Search组件和List组件结合为例，如果将List组件设置为固定高度，那么在横屏转为竖屏时会出现截断现象。若设置为百分比高度或者设置layoutWeight(1)占用剩余空间则可以避免被截断的现象。

   ```ts
   @Entry
   @Component
   struct FourPage {
     @State changeValue: string = '';
     @State submitValue: string = '';
     private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14];
     controller: SearchController = new SearchController();

     build() {
       Column() {
         Search({ value: this.changeValue, placeholder: 'Type to search...', controller: this.controller })
           .searchButton('SEARCH')
           .width('95%')
           .height(40)
           .backgroundColor('#F5F5F5')
           .placeholderColor(Color.Grey)
           .placeholderFont({ size: 14, weight: 400 })
           .textFont({ size: 14, weight: 400 })
           .onSubmit((value: string) => {
             this.submitValue = value;
           })
           .onChange((value: string) => {
             this.changeValue = value;
           })
           .margin(20);

         List({ space: 20, initialIndex: 0 }) {
           ForEach(this.arr, (item: number) => {
             ListItem() {
               Text('' + item)
                 .width('100%')
                 .height(100)
                 .fontSize(16)
                 .textAlign(TextAlign.Center)
                 .borderRadius(10)
                 .backgroundColor(Color.Gray);
             };
           }, (item: string) => item);
         }
         .width('90%')
         .scrollBar(BarState.Off)
         .layoutWeight(1); // 设置占用剩余空间

       }
       .width('100%')
       .height('100%');
     }
   }
   ```

## 横屏播放视频后返回上一页，布局异常

### 问题现象

应用打开正常显示，点击某一视频横屏播放后，返回上一页，页面显示错位异常。其根本原因是系统的旋转特性针对窗口级别生效，当视频页面通过setPreferredOrientation()将窗口设为横屏时，同一窗口下的所有页面都会被强制进入横屏布局，退出视频页面时若未及时恢复竖屏方向，就会导致上一页面布局错位。

### 定位过程

1. 当应用无论竖屏还是横屏启动，页面显示正常，说明应用初次加载监听了屏幕大小，并正确设置了页面尺寸。
2. 当应用从横屏的视频页面切换回竖屏状态时，建议检查代码中是否使用on('windowSizeChange')监听了设备尺寸变化，判断当前是横屏还是竖屏。
3. 检查异常的页面是否通过判断当前是横屏还是竖屏，分别展示不同的布局。
4. 系统的旋转特性是针对窗口实现的，无法让单个页面独立进行旋转操作。当通过setPreferredOrientation()修改窗口方向为横屏时，同一窗口下的所有页面都会受到影响，导致其他页面也被强制变为横屏布局。

### 分析结论

应用在进入视频横屏时监听了屏幕方向变化，退出视频播放页面时，页面还根据横屏状态获取的屏幕尺寸进行页面布局，导致应用在返回上一页时，页面显示错位异常现象。此外，由于系统的旋转特性是针对窗口级别的，当横屏视频页面修改窗口方向时，同一窗口下的其他页面也会被强制进入横屏布局状态。

### 修改建议

* 方案一：通过窗口方向接口动态切换横竖屏。

  在触发横竖屏切换的事件（如视频全屏事件）中，通过setPreferredOrientation()修改方向，退出全屏时同样恢复竖屏状态。

  ```ts
  import { window } from '@kit.ArkUI';

  @Entry
  @Component
  struct VideoPage {
    @State videoSrc: Resource = $rawfile('example.mp4'); // 实际开发替换为实际视频资源
    @State curRate: PlaybackSpeed = PlaybackSpeed.Speed_Forward_1_00_X;
    private isAutoPlay: boolean = true;
    private showControls: boolean = true;
    private isShortcutKeyEnabled: boolean = false;
    controller: VideoController = new VideoController();

    build() {
      Column() {
        Video({
          src: this.videoSrc,
          currentProgressRate: this.curRate, // 设置播放速度
          controller: this.controller,
        })
          .width('100%')
          .height(600)
          .autoPlay(this.isAutoPlay)
          .controls(this.showControls)
          .enableShortcutKey(this.isShortcutKeyEnabled)
          .onFullscreenChange((e?: FullscreenObject) => {
            if (e != undefined) {
              if (e.fullscreen == true) {
                window.getLastWindow(this.getUIContext().getHostContext(), (err, data) => { // 获取window实例
                  let windowClass = data;
                  windowClass.setPreferredOrientation(window.Orientation.LANDSCAPE); // 点击全屏后，旋转为横屏显示
                });
              } else {
                window.getLastWindow(this.getUIContext().getHostContext(), (err, data) => { // 获取window实例
                  let windowClass = data;
                  windowClass.setPreferredOrientation(window.Orientation.PORTRAIT); // 退出全屏后，旋转为竖屏显示
                });
              }
            }
          });
      };
    }
  }

  interface FullscreenObject {
    fullscreen: boolean;
  }
  ```
* 方案二：使用独立UIAbility实现页面级横竖屏隔离。

  如果希望某个特定页面可以进行横竖屏转换，而完全不影响其他页面，建议将该页面放在独立的UIAbility中（与其他页面分开），在需要打开的时候通过启动该UIAbility实现相关功能。这样可以避免窗口旋转影响其他页面的布局。具体参考[启动UIAbility的指定页面](../harmonyos-guides/uiability-intra-device-interaction.md#启动uiability的指定页面)。
* 方案三：使用Navigation页面级旋转特性。

  Navigation中也提供了页面级的旋转特性，该功能仅支持ArkTS接口。通过Navigation的页面级旋转，可以实现单个页面的横竖屏切换而不影响其他页面。具体参考[横竖屏开发指导](../best-practices/bpta-landscape-and-portrait-development.md#section161651074615)。
