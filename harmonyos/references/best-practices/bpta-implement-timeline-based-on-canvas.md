---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-implement-timeline-based-on-canvas
title: 基于Canvas实现录像回放时间轴
breadcrumb: 最佳实践 > 图形 > 图形绘制 > 基于Canvas实现录像回放时间轴
category: best-practices
scraped_at: 2026-04-28T08:20:53+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:e2a91c41d09983f8e1ef6c8cb83f6f8632112773394ee8f8b92b569a62c83f9b
---

## **概述**

在安防监控、车载回放等场景中，录像回放是核心功能。用户通过滑动时间轴，查看不同时间节点的历史视频。本文基于Canvas绘图能力和视频组件，提供功能完备的录像回放时间轴解决方案，封装了[核心组件TimeBarView](https://gitcode.com/harmonyos_samples/timebar/blob/master/time_bar/src/main/ets/components/TimeBarView.ets)，助力开发者快速实现时间轴功能。该组件集成了时间轴绘制、单指滑动浏览、双指缩放切换时间粒度等功能。

本文主要介绍如何实现TimeBarView时间轴组件，并结合“滑动时间轴控制视频播放”的核心场景，阐述TimeBarView组件的使用方法。

TimeBarView时间轴组件提供以下核心功能：

* 支持自定义时间轴样式，可配置刻度线、中间指示线、视频区域的外观（如颜色、尺寸、位置）。
* 支持双指缩放以调整时间刻度精度，单指滑动以定位至目标时间点。
* 支持设置时间轴当前进度。
* 支持基于时间轴组件的二次自定义绘制。

## **实现原理**

### 关键技术

TimeBarView组件采用分层绘制，依次为刻度线、中间线、视频区域及顶层自定义绘制区域。通过滑动和缩放手势事件，实时更新状态并触发时间轴重绘。详细实现参考本章[开发流程](bpta-implement-timeline-based-on-canvas.md#section42461138131619)。

刻度线绘制主要将时间戳转换为Canvas像素坐标。例如，开发者自定义刻度间隔的宽度为intervalWidth（如intervalWidth = 10vp），相同长度的时间间隔对应10分钟，实现“固定时间对应固定像素”的精准映射，确保任意时间戳均能通过公式计算出唯一的画布坐标。

**图1** 时间-像素映射示意图  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/qBZAhlnbTPW9CDdLhj5DWw/zh-cn_image_0000002478758526.png?HW-CC-KV=V1&HW-CC-Date=20260428T002051Z&HW-CC-Expire=86400&HW-CC-Sign=45DBFDC2410173C7A52B2CF42E6999971E6C1B842828197A8F0C872724660043 "点击放大")

### 开发流程

1. 绘制时间轴
   1. 时间刻度绘制

      **计算基本参数**

      * scaleNum属性：表示当前画布上需绘制的时间间隔数量。viewWidth属性表示时间轴画布的总宽度，intervalWidth属性表示每个时间格子在画布上占用的宽度（intervalWidth值为自定义，例如组件内为10vp/格）。加2是为了预留左右两边的额外格子，避免滚动或缩放时边缘出现空白。
      * middleLineDuration属性：计算画布左半部分对应的实际时间。
      * leftTime：表示画布最左侧边缘对应的实际时间戳（毫秒）。

      时间轴根据画布大小、缩放比例动态调整显示的时间范围，同时始终以中心点为视觉锚点，确保交互的连贯性。

      ```
      1. // Number of small divisions visible
      2. const scaleNum = Math.floor(viewWidth / this.intervalWidth) + 2;

      4. // Duration represented from left edge to the middle line
      5. // keep sub-minute precision to avoid truncation that caused a visual gap near the end when zoomed in.
      6. const middleLineDuration = (viewWidth / 2) * (TimeMsUnit.TEN_MINUTE / this.intervalWidth);

      8. // Time at the far left edge
      9. this.leftTime = this._currentTime - middleLineDuration;
      ```

      [TimeBarView.ets](https://gitcode.com/harmonyos_samples/timebar/blob/master/time_bar/src/main/ets/components/TimeBarView.ets#L456-L464)

      **绘制刻度线**

      以10分钟为最小单位生成刻度，在小时模式（MODE\_HOUR）下，每60分钟绘制一次大刻度及时间文本；在分钟模式（MODE\_MINUTE）下，将10分钟划分为10个细分刻度，因此循环10次绘制刻度线。drawTickLine()方法用于绘制大、小刻度，drawTimeText()方法用于绘制大刻度对应的时间文本。

      ```
      1. // Find the first tick (aligned to 10 minutes)
      2. let minuteNum = Math.floor(this.leftTime / TimeMsUnit.TEN_MINUTE);
      3. let xPosition =
      4. (minuteNum * TimeMsUnit.TEN_MINUTE - this.leftTime) * (this.intervalWidth / TimeMsUnit.TEN_MINUTE);

      6. for (let i = 0; i < scaleNum; i++) {
      7. const currentX = xPosition + i * this.intervalWidth;
      8. if (this.divisorMode == ScaleMode.MODE_HOUR) {
      9. const isMajorTick = minuteNum % 6 === 0;
      10. const tickLength =
      11. isMajorTick ? this.timeScaleOption.scaleLineHeight * 2 : this.timeScaleOption.scaleLineHeight;
      12. const tickRange = this.drawTickLine(currentX, tickLength);
      13. if (isMajorTick) {
      14. this.drawTimeText(currentX, minuteNum, tickRange);
      15. }

      17. } else if (this.divisorMode === ScaleMode.MODE_MINUTE) {
      18. for (let j = 0; j < 10; j++) {
      19. const positionX = j === 0 ? currentX : currentX + j * this.intervalWidth * 0.1;
      20. const isMajorTick = j === 0;
      21. const tickLength =
      22. isMajorTick ? this.timeScaleOption.scaleLineHeight * 2 : this.timeScaleOption.scaleLineHeight;
      23. const tickRange = this.drawTickLine(positionX, tickLength);
      24. if (isMajorTick) {
      25. this.drawTimeText(positionX, minuteNum, tickRange);
      26. }
      27. }
      28. }
      29. minuteNum++;
      30. }
      ```

      [TimeBarView.ets](https://gitcode.com/harmonyos_samples/timebar/blob/master/time_bar/src/main/ets/components/TimeBarView.ets#L468-L497)
   2. 中间指示线绘制

      中间线是时间轴上的当前时间标记，固定在画布中央，用于标识当前选中或播放的时间点。

      ```
      1. /** Draw middle indicator line at canvas center. */
      2. private drawMiddleLine() {
      3. this.context.beginPath();
      4. this.context.moveTo(this.context.width / 2, 0);
      5. this.context.lineTo(this.context.width / 2, this.middleIndicatorOption.length);
      6. this.context.strokeStyle = this.middleIndicatorOption.fillColor;
      7. this.context.lineWidth = 2;
      8. this.context.stroke();
      9. }
      ```

      [TimeBarView.ets](https://gitcode.com/harmonyos_samples/timebar/blob/master/time_bar/src/main/ets/components/TimeBarView.ets#L431-L440)
   3. 视频区域绘制

      **获取图片pixelMap对象**

      视频区域用于显示视频片段的时间分布（如录制片段、有效视频区间），采用离屏预渲染，避免滑动缩放时重复计算绘制。

      * 预渲染时机：当视频片段数据timeRange变化时（通过@Watch('onTimeRangeChange')监听），执行预渲染。
      * 预渲染规则：使用[OffscreenCanvasRenderingContext2D](../harmonyos-references/ts-offscreencanvasrenderingcontext2d.md)构造离屏Canvas画布对象offPaint，按1vp等于1分钟的比例绘制所有视频片段，调用offPaint.getPixelMap()方法生成videoPixelMap像素图。

      ```
      1. // Offscreen canvas (height uses current view height option)
      2. const offSettings: RenderingContextSettings = new RenderingContextSettings(false);
      3. const offCanvas: OffscreenCanvas = new OffscreenCanvas(videoAreaWidth, this.timeBarOption.height);
      4. const offPaint = offCanvas.getContext('2d', offSettings);
      5. // ...
      6. // Draw each segment; clamp and floor pixel coordinates to avoid overlap
      7. segArr.forEach((recordSegment) => {
      8. const beginTime = parseTimeString(recordSegment.beginTime).getTime();
      9. const endTime = parseTimeString(recordSegment.endTime).getTime();

      11. let leftX = (beginTime - this._minTime) / TimeMsUnit.ONE_MINUTE;
      12. let rightX = (endTime - this._minTime) / TimeMsUnit.ONE_MINUTE;

      14. // Clamp
      15. leftX = Math.max(0, Math.min(videoAreaWidth - 1, leftX));
      16. rightX = Math.max(leftX + 1, Math.min(videoAreaWidth, rightX));

      18. const width = Math.max(1, rightX - leftX);
      19. const videoAreaHeight = this.videoAreaOption.topOffset + this.videoAreaOption.height > this.timeBarOption.height
      20. ? this.timeBarOption.height - this.videoAreaOption.topOffset : this.videoAreaOption.height;
      21. offPaint.fillRect(leftX, this.videoAreaOption.topOffset, width, videoAreaHeight);
      22. });

      24. const data = offPaint.getPixelMap(0, 0, videoAreaWidth, this.timeBarOption.height);
      ```

      [TimeBarView.ets](https://gitcode.com/harmonyos_samples/timebar/blob/master/time_bar/src/main/ets/components/TimeBarView.ets#L304-L335)

      **实时绘制**

      缩放时，通过矩阵变换（缩放）将预渲染图适配当前画布比例，避免重复绘制。

      ```
      1. // Disable smoothing to keep crisp edges on narrow color bars
      2. this.context.imageSmoothingEnabled = false;

      4. // Offscreen bitmap uses 1px/minute base.
      5. // Compute the left bitmap x that corresponds to current leftTime.
      6. const bitmapLeftBase = (this._minTime - this.leftTime) / TimeMsUnit.ONE_MINUTE;

      8. // Front-scale: intervalWidth=10px => 1px/minute; so scale factor is intervalWidth/10.
      9. const videoZoomSize = this.intervalWidth / 10;

      11. // Draw with transform; do not clear the canvas here (we already cleared in drawScales)
      12. this.context.save();
      13. this.context.scale(videoZoomSize, 1);
      14. this.context.drawImage(this.videoPixelMap, bitmapLeftBase, 0);
      15. this.context.restore();
      ```

      [TimeBarView.ets](https://gitcode.com/harmonyos_samples/timebar/blob/master/time_bar/src/main/ets/components/TimeBarView.ets#L355-L369)
2. 滑动时间轴

   滑动功能允许用户通过单指拖拽浏览时间轴，核心逻辑如下：

   * 手势监听：通过PanGesture()回调监听手指按下、移动、抬起事件。
   * 灵敏度控制：当累计位移（\_panResidual）超过灵敏度阈值（MOVE\_SENSITIVE）时，将其作为有效位移（effectiveDelta ）处理，避免手指轻微抖动触发频繁更新。
   * 边界限制：通过clampToBounds()方法限制滑动范围，防止滑动至无数据区域。
   * 回调通知：滑动过程中实时触发onMoveScaleCallback()回调，通知外部当前选中时间。
   * 帧同步合并渲染：将一帧内的多次重绘请求合并为一次，确保每次重绘均在新帧开始时执行。重绘的scheduleRedraw()方法基于DisplaySync实现帧同步刷新。

   将有效位移（effectiveDelta）通过刻度密度（intervalWidth）属性转换为时间偏移量，更新时间轴当前时间（\_currentTime属性），同步至TimeBarModel组件控制器，供外部获取。调用scheduleRedraw()方法，延迟绘制至下一帧，减少频繁绘制引起的性能消耗，确保滑动过程的视觉流畅性。

   ```
   1. // Capture raw delta for accumulation.
   2. const rawDelta = event.offsetX - this._touchDownPosition;
   3. this._touchDownPosition = event.offsetX;

   5. // Accumulate sub-pixel movement for smoother tracking.
   6. this._panResidual += rawDelta;
   7. if (Math.abs(this._panResidual) < this.MOVE_SENSITIVE) {
   8. return;
   9. }

   11. const effectiveDelta = this._panResidual;
   12. this._panResidual = 0;

   14. // Update middle-line time, then clamp into [min, max]
   15. const nextTime = this._currentTime - (effectiveDelta * (TimeMsUnit.TEN_MINUTE / this.intervalWidth));
   16. this._currentTime = this.clampToBounds(nextTime);

   18. this.model.currentTime = this._currentTime;

   20. // Redraw and notify
   21. this.scheduleRedraw(); // Defer redraw to next frame for smoother visuals.
   22. this._onTimeBarMoveListener?.onMoveScaleCallback(this._currentTime, PlayStatus.PLAYING);
   ```

   [TimeBarView.ets](https://gitcode.com/harmonyos_samples/timebar/blob/master/time_bar/src/main/ets/components/TimeBarView.ets#L666-L687)
3. 缩放时间轴

   缩放功能允许通过双指捏合/张开切换时间粒度。核心逻辑如下：

   * 手势监听：通过PinchGesture()回调监听双指缩放事件。
   * 缩放因子过滤：设置scaleChange > 0.1，避免微小缩放动作触发频繁更新。
   * intervalWidth调整：缩放时修改intervalWidth属性（10分钟对应的像素宽度），放大时增加，缩小时减少。
   * 模式切换：根据intervalWidth阈值切换显示模式（小时/分钟）。
     + intervalWidth < 60：小时模式（10分钟/刻度，6个刻度 = 1小时）。
     + 60≤intervalWidth < 180：分钟模式（1分钟/细分刻度）。
     + intervalWidth ≥ 180：最大缩放限制，锁定分钟模式。
   * 边界限制：设置最小（10vp）和最大（180vp）缩放阈值，避免过度缩放。

   **图2** 缩放时间轴示意图  
   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/6t9Z-hzJRlGnwn-xsRleDw/zh-cn_image_0000002478598550.png?HW-CC-KV=V1&HW-CC-Date=20260428T002051Z&HW-CC-Expire=86400&HW-CC-Sign=22A89DAF258C258C13D7252008A7A8DEE217C9FF2BEE96854A1FAB8AC451F898 "点击放大")

   ```
   1. // Update per-division width
   2. if (this.zoomSize > 1) {
   3. this.intervalWidth += 10;
   4. } else {
   5. this.intervalWidth -= 10;
   6. }

   8. // Switch modes and enforce bounds
   9. if (this.intervalWidth < 60) {
   10. this.divisorMode = ScaleMode.MODE_HOUR;
   11. if (this.intervalWidth < 10) {
   12. this.intervalWidth = 10;
   13. }
   14. } else if (this.intervalWidth < 180) {
   15. this.divisorMode = ScaleMode.MODE_MINUTE;
   16. } else {
   17. this.divisorMode = ScaleMode.MODE_MINUTE;
   18. this.intervalWidth = 180;
   19. }
   ```

   [TimeBarView.ets](https://gitcode.com/harmonyos_samples/timebar/blob/master/time_bar/src/main/ets/components/TimeBarView.ets#L717-L735)
4. 数据驱动交互

   为实现时间轴组件与外部（如视频控制器）的数据联动，构建了TimeBarModel类。TimeBarModel封装了时间轴的两个核心数据：timeRange（视频片段集合）和currentTime（当前时间戳）。

   * timeRange：当外部传入录像片段时，自动对timeRange排序并计算有效时间边界（minTime/maxTime），确保时间轴仅显示有录像的时段。

     ```
     1. set timeRange(segments: RecordSegment[]) {
     2. if (!segments || segments.length === 0) {
     3. this._timeRange = [];
     4. this.updateTimeBounds();
     5. this.notifyDataChange('timeRange');
     6. return;
     7. }

     9. const segArr: RecordSegment[] = [...segments];

     11. segArr.sort((a, b) => {
     12. const ta = parseTimeString(a.beginTime).getTime();
     13. const tb = parseTimeString(b.beginTime).getTime();
     14. return ta - tb;
     15. });

     17. this._timeRange = [...segArr];

     19. // Update time bounds (min/max time)
     20. this.updateTimeBounds();
     21. // Ensure current time stays within valid bounds
     22. this.currentTime = this.clampToBounds(this._currentTime);
     23. // Notify external listeners of the data change
     24. this.notifyDataChange('timeRange');
     25. }
     ```

     [TimeBarModel.ets](https://gitcode.com/harmonyos_samples/timebar/blob/master/time_bar/src/main/ets/components/viewModel/TimeBarModel.ets#L50-L75)
   * currentTime：通过getter和setter机制实现双向同步，既接收外部视频播放进度的更新，也在时间轴滑动时将最新时间输出给外部。

     ```
     1. set currentTime(time: number) {
     2. if (!Number.isFinite(time) || time <= 0) {
     3. return;
     4. } // ignore invalid time values

     6. const clampedTime = this.clampToBounds(time);
     7. if (this._currentTime === clampedTime) {
     8. return;
     9. } // do not trigger update if time hasn't changed

     11. this._currentTime = clampedTime;
     12. this.notifyDataChange('currentTime');
     13. }
     ```

     [TimeBarModel.ets](https://gitcode.com/harmonyos_samples/timebar/blob/master/time_bar/src/main/ets/components/viewModel/TimeBarModel.ets#L91-L104)
   * 数据变更通知：通过onDataChange()回调，监听timeRange和currentTime的变化，简化了开发者调用。

     ```
     1. private notifyDataChange(type: 'timeRange' | 'currentTime') {
     2. this._onDataChange && this._onDataChange(type);
     3. }
     ```

     [TimeBarModel.ets](https://gitcode.com/harmonyos_samples/timebar/blob/master/time_bar/src/main/ets/components/viewModel/TimeBarModel.ets#L163-L166)

## 时间轴控制视频播放场景

### 场景描述

TimeBarView时间轴与视频播放联动，滑动时间轴可快速定位至目标录像片段。

滑动停止时，若时间轴中线对应的时间点在录像片段有效时间内，视频立即跳转并继续播放；若处于两端录像间的空白区域，系统自动跳转至最近的录像起始时间点，避免无画面时段，提高效率。时间轴滑动存在硬性边界限制，用户试图将时间轴向右滑动至所有录像片段的最末端（即最新一段录像的结束时间）时，将无法继续拖动，防止超出录像数据范围导致播放异常。

**图3** 效果图  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/00lzXCe-SS-TfVJ_OabaJg/zh-cn_image_0000002510798495.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002051Z&HW-CC-Expire=86400&HW-CC-Sign=91146C15F6A8C13FA12E89CDFD3CEB39293474C1B2EDEB51F851B7051C7DC2B3 "点击放大")

### 开发步骤

1. 引入TimeBarView时间轴组件

   创建TimeBarModel实例作为数据载体，实例对象viewModel通过组件参数传入TimeBarView时间轴组件，即可渲染基本的时间轴。核心代码如下：

   ```
   1. import {
   2. TimeBarView,
   3. TimeBarModel,
   4. // ...
   5. } from '@samples/time_bar';
   6. // ...
   7. @Component
   8. struct TimeBarVideoLinkage {
   9. // ...
   10. private viewModel: TimeBarModel = new TimeBarModel();
   11. // ...
   12. build() {
   13. NavDestination() {
   14. Row() {
   15. // ...
   16. Column() {
   17. TimeBarView({
   18. model: this.viewModel,
   19. // ...
   20. })
   21. }
   22. // ...
   23. }
   24. .height('100%')
   25. .alignItems(VerticalAlign.Top)
   26. }
   27. .title($r('app.string.route_title2'))
   28. }
   29. }
   ```

   [TimeBarVideoLinkage.ets](https://gitcode.com/harmonyos_samples/timebar/blob/master/entry/src/main/ets/pages/TimeBarVideoLinkage.ets#L17-L174)

   说明

   TimeBarView组件属性参考：[TimeBarView 接口信息](https://gitcode.com/harmonyos_samples/timebar#具体实现)。
2. 时间轴展示视频区域

   开发者处理视频片段，生成RecordSegment类型的集合。通过viewModel对象的timeRange属性传递给组件，在时间轴上即可绘制视频区域。核心代码如下：

   ```
   1. async getTimeInfoFromVideo() {
   2. if (this.videosInfo.length === 0) {
   3. try {
   4. this.videosInfo = await extractOnlineVideosInfo(LEGITIMATE_VIDEO_URLS);
   5. } catch (e) {
   6. this.videosInfo = [];
   7. }
   8. }
   9. // ...
   10. const fileInfoList: Array<RecordSegment> = [];
   11. const initialTimeISO = getTodayStartMs();

   13. // Generate segments aligned to the time bar (including gaps)
   14. this.videosInfo.forEach((curInfo, index) => {
   15. const seg = new RecordSegment();

   17. const startOffset = this.timelineOffsets[index] || 0;
   18. const durMs = Number(curInfo.duration) || 0;

   20. seg.beginTime = dayjs(initialTimeISO).add(startOffset, 'millisecond').format(MILLISECOND_FORMAT);
   21. seg.endTime = dayjs(initialTimeISO).add(startOffset + durMs, 'millisecond').format(MILLISECOND_FORMAT);

   23. fileInfoList.push(seg)
   24. });
   25. this.viewModel.timeRange = fileInfoList;
   26. }
   ```

   [TimeBarVideoLinkage.ets](https://gitcode.com/harmonyos_samples/timebar/blob/master/entry/src/main/ets/pages/TimeBarVideoLinkage.ets#L85-L119)

   说明

   可向TimeBarView组件传递videoAreaOption属性，以修改时间区域的背景色及在时间轴垂直方向的位置；传递timeScaleOption属性，以修改时间轴刻度的长度、颜色及对齐方式。
3. 绑定时间轴事件监听器，同步时间状态

   在onContextReady()回调中，获取TimeBarView实例并绑定setTimeBarMoveListener()方法，监听时间轴滑动事件，实时同步当前选中时间（curTime）与操作状态（timeBarStatus）。核心代码如下：

   ```
   1. private handleContextReady = (_ctx: CanvasRenderingContext2D, component: TimeBarView) => {
   2. this.timeBarRef = component;
   3. this.timeBarRef.setTimeBarMoveListener({
   4. onMoveScaleCallback: (curTime: number, status?: PlayStatus) => {
   5. this.currentTime = curTime;
   6. this.timeBarStatus = status;
   7. }
   8. })
   9. }
   ```

   [TimeBarVideoLinkage.ets](https://gitcode.com/harmonyos_samples/timebar/blob/master/entry/src/main/ets/pages/TimeBarVideoLinkage.ets#L68-L77)

   ```
   1. Column() {
   2. TimeBarView({
   3. model: this.viewModel,
   4. onContextReady: this.handleContextReady
   5. })
   6. }
   ```

   [TimeBarVideoLinkage.ets](https://gitcode.com/harmonyos_samples/timebar/blob/master/entry/src/main/ets/pages/TimeBarVideoLinkage.ets#L145-L152)

   说明

   onMoveScaleCallback()回调会在时间轴开始滑动（START）、滑动过程中（PLAYING）、松手后（STOP）触发，curTime为时间轴中间线对应的绝对时间戳，是视频跳转的核心依据。
4. 实现时间同步逻辑，处理视频跳转

   时间轴滑动时，通过@Watch监听currentTime属性变化，处理视频跳转逻辑。

   * 有效区域滑动：拖动时间轴至某段视频内，松手后视频精准跳转至对应时间并播放。
   * 空白区域滑动：拖动至两段视频的空白间隔，视频自动跳转至下一段视频的起始位置。
   * 边界滑动：拖动至视频范围最右侧（最后一段视频结束时间），时间轴无法继续右滑，视频停留在最后一帧。
     1. 计算目标视频位置（时间映射与边界处理）

        从时间轴拖动的currentTime（选中时间）出发，通过“时间偏移计算→片段定位→进度校正”，确定视频需跳转的目标进度。核心代码如下：

        ```
        1. const totalTimelineMs = this.totalTimelineMs || 0;
        2. const rawOffset = (this.curTime ?? this.initialTime) - this.initialTime; // relative offset (ms)
        3. const clampedOffset = clamp(rawOffset, 0, totalTimelineMs);

        5. // Resolve segment index (including gaps) and derive target segment window
        6. const info = findSegmentIndexByTimeline(this.timelineOffsets ?? [], this.videosInfo, clampedOffset);
        7. const prevIndex = this.curIndex;
        8. const nextIndex = info.index !== -1 ? info.index : prevIndex;

        10. // Start time and duration of the target segment
        11. const segStartMs = this.timelineOffsets?.[nextIndex] ?? 0;
        12. const segDurMs = Number(this.videosInfo[nextIndex]?.duration) || 0;

        14. // Whether dragged to the "absolute end"
        15. const playEnd = (nextIndex === this.videosInfo.length - 1) && (clampedOffset === totalTimelineMs);

        17. // Compute the preview/target progress inside the segment (seconds)
        18. const videoProgressSec = this.computeProgressSeconds(clampedOffset, segStartMs, segDurMs, info, playEnd);

        20. const prevSrc = this.videoSrcArray[prevIndex] ?? '';
        21. const nextSrc = this.videoSrcArray[nextIndex] ?? '';
        22. const indexChanged = nextIndex !== prevIndex;
        23. const willReload = indexChanged && nextSrc !== prevSrc;

        25. // Decide whether player source must reload (URL change) and apply index switch side-effects
        26. this.decideAndApplyIndexChange(indexChanged, willReload, nextIndex, segStartMs);
        ```

        [VideoView.ets](https://gitcode.com/harmonyos_samples/timebar/blob/master/entry/src/main/ets/components/VideoView.ets#L114-L139)
     2. 执行视频跳转与播放控制

        根据视频进度属性（目标进度）videoProgressSec，结合视频加载状态执行跳转，并控制播放行为。核心代码如下：

        ```
        1. private performSeek(videoProgressSec: number, willReload: boolean) {
        2. if (willReload) {
        3. // Source will reload: cache and let onPrepared execute precise seek
        4. this.pendingSeekSec = videoProgressSec;
        5. return;
        6. }

        8. // No reload (or no segment change): attempt immediate precise seek
        9. if (this.durationTime === 0) {
        10. // Duration is not available yet: still cache the seek
        11. this.pendingSeekSec = videoProgressSec;
        12. } else {
        13. this.controller.setCurrentTime(videoProgressSec, SeekMode.Accurate);
        14. }
        15. }
        ```

        [VideoView.ets](https://gitcode.com/harmonyos_samples/timebar/blob/master/entry/src/main/ets/components/VideoView.ets#L199-L214)

## 常见问题

### **canvas画的时间轴，在手势捏合缩放时画面不停闪烁，是否有解决方案**

在Canvas画布进行缩放操作时，尤其是在处理手势缩放时，可能会出现画面闪烁的问题。这是由于缩放操作导致画布上的图形重新计算和绘制，引起视觉上的闪烁效果。为减少这种现象，可采取以下方法：设置临界点，在手势捏合持续回调中，不是每次移动都重新绘制图形，而是设定特定条件，当满足这些条件时才重新绘制。例如，可检查手势移动的距离，当移动超过特定阈值时才更新画面。

```
1. if (Math.abs(offsetX - this.lastOffsetX) < 0.5 && Math.abs(offsetY - this.lastOffsetY) < 0.5) {
2. return;
3. }
4. this.lastOffsetX = offsetX;
```

此段代码表示仅当X轴与Y轴的位移均超过0.5时，才更新画布，从而减少不必要的重绘。

## 示例代码

* [实现可缩放时间轴功能](https://gitcode.com/harmonyos_samples/timebar)
