---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkui-hdc
title: ArkUI
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta1引入的API > ArkUI
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:55+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:b1a84d6706c8ad507916c0ad42f2f0d495bac8eebb986261200400087ef640e5
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API访问级别变更 | 类名：global；  API声明： declare enum BlurStyle  差异内容：systemapi | 类名：global；  API声明： declare enum BlurStyle  差异内容：NA | component/common.d.ts |
| API访问级别变更 | 类名：CommonMethod；  API声明：key(value: string): T;  差异内容：systemapi | 类名：CommonMethod；  API声明：key(value: string): T;  差异内容：NA | component/common.d.ts |
| API模型切换 | 类名：WindowStageEventType；  API声明：SHOWN = 1  差异内容：NA | 类名：WindowStageEventType；  API声明：SHOWN = 1  差异内容：stagemodelonly | api/@ohos.window.d.ts |
| API模型切换 | 类名：WindowStageEventType；  API声明：ACTIVE  差异内容：NA | 类名：WindowStageEventType；  API声明：ACTIVE  差异内容：stagemodelonly | api/@ohos.window.d.ts |
| API模型切换 | 类名：WindowStageEventType；  API声明：INACTIVE  差异内容：NA | 类名：WindowStageEventType；  API声明：INACTIVE  差异内容：stagemodelonly | api/@ohos.window.d.ts |
| API模型切换 | 类名：WindowStageEventType；  API声明：HIDDEN  差异内容：NA | 类名：WindowStageEventType；  API声明：HIDDEN  差异内容：stagemodelonly | api/@ohos.window.d.ts |
| API卡片权限变更 | 类名：global；  API声明： declare namespace mediaquery  差异内容：NA | 类名：global；  API声明： declare namespace mediaquery  差异内容：form | api/@ohos.mediaquery.d.ts |
| API卡片权限变更 | 类名：mediaquery；  API声明： interface MediaQueryResult  差异内容：NA | 类名：mediaquery；  API声明： interface MediaQueryResult  差异内容：form | api/@ohos.mediaquery.d.ts |
| API卡片权限变更 | 类名：MediaQueryResult；  API声明：readonly matches: boolean;  差异内容：NA | 类名：MediaQueryResult；  API声明：readonly matches: boolean;  差异内容：form | api/@ohos.mediaquery.d.ts |
| API卡片权限变更 | 类名：MediaQueryResult；  API声明：readonly media: string;  差异内容：NA | 类名：MediaQueryResult；  API声明：readonly media: string;  差异内容：form | api/@ohos.mediaquery.d.ts |
| API卡片权限变更 | 类名：mediaquery；  API声明： interface MediaQueryListener  差异内容：NA | 类名：mediaquery；  API声明： interface MediaQueryListener  差异内容：form | api/@ohos.mediaquery.d.ts |
| API卡片权限变更 | 类名：MediaQueryListener；  API声明：on(type: 'change', callback: Callback<MediaQueryResult>): void;  差异内容：NA | 类名：MediaQueryListener；  API声明：on(type: 'change', callback: Callback<MediaQueryResult>): void;  差异内容：form | api/@ohos.mediaquery.d.ts |
| API卡片权限变更 | 类名：MediaQueryListener；  API声明：off(type: 'change', callback?: Callback<MediaQueryResult>): void;  差异内容：NA | 类名：MediaQueryListener；  API声明：off(type: 'change', callback?: Callback<MediaQueryResult>): void;  差异内容：form | api/@ohos.mediaquery.d.ts |
| API卡片权限变更 | 类名：mediaquery；  API声明：function matchMediaSync(condition: string): MediaQueryListener;  差异内容：NA | 类名：mediaquery；  API声明：function matchMediaSync(condition: string): MediaQueryListener;  差异内容：form | api/@ohos.mediaquery.d.ts |
| API卡片权限变更 | 类名：global；  API声明： declare class CanvasAttribute  差异内容：NA | 类名：global；  API声明： declare class CanvasAttribute  差异内容：form | component/canvas.d.ts |
| API卡片权限变更 | 类名：global；  API声明： declare namespace focusControl  差异内容：NA | 类名：global；  API声明： declare namespace focusControl  差异内容：form | component/common.d.ts |
| API卡片权限变更 | 类名：global；  API声明： declare enum AnimationStatus  差异内容：NA | 类名：global；  API声明： declare enum AnimationStatus  差异内容：form | component/enums.d.ts |
| API卡片权限变更 | 类名：AnimationStatus；  API声明：Initial  差异内容：NA | 类名：AnimationStatus；  API声明：Initial  差异内容：form | component/enums.d.ts |
| API卡片权限变更 | 类名：AnimationStatus；  API声明：Running  差异内容：NA | 类名：AnimationStatus；  API声明：Running  差异内容：form | component/enums.d.ts |
| API卡片权限变更 | 类名：AnimationStatus；  API声明：Paused  差异内容：NA | 类名：AnimationStatus；  API声明：Paused  差异内容：form | component/enums.d.ts |
| API卡片权限变更 | 类名：AnimationStatus；  API声明：Stopped  差异内容：NA | 类名：AnimationStatus；  API声明：Stopped  差异内容：form | component/enums.d.ts |
| API卡片权限变更 | 类名：global；  API声明： declare enum FillMode  差异内容：NA | 类名：global；  API声明： declare enum FillMode  差异内容：form | component/enums.d.ts |
| API卡片权限变更 | 类名：FillMode；  API声明：None  差异内容：NA | 类名：FillMode；  API声明：None  差异内容：form | component/enums.d.ts |
| API卡片权限变更 | 类名：FillMode；  API声明：Forwards  差异内容：NA | 类名：FillMode；  API声明：Forwards  差异内容：form | component/enums.d.ts |
| API卡片权限变更 | 类名：FillMode；  API声明：Backwards  差异内容：NA | 类名：FillMode；  API声明：Backwards  差异内容：form | component/enums.d.ts |
| API卡片权限变更 | 类名：FillMode；  API声明：Both  差异内容：NA | 类名：FillMode；  API声明：Both  差异内容：form | component/enums.d.ts |
| API卡片权限变更 | 类名：global；  API声明： declare class GridColAttribute  差异内容：NA | 类名：global；  API声明： declare class GridColAttribute  差异内容：form | component/grid\_col.d.ts |
| API卡片权限变更 | 类名：global；  API声明： declare class GridRowAttribute  差异内容：NA | 类名：global；  API声明： declare class GridRowAttribute  差异内容：form | component/grid\_row.d.ts |
| API卡片权限变更 | 类名：global；  API声明： interface ImageAnimatorInterface  差异内容：NA | 类名：global；  API声明： interface ImageAnimatorInterface  差异内容：form | component/image\_animator.d.ts |
| API卡片权限变更 | 类名：global；  API声明： interface ImageFrameInfo  差异内容：NA | 类名：global；  API声明： interface ImageFrameInfo  差异内容：form | component/image\_animator.d.ts |
| API卡片权限变更 | 类名：ImageFrameInfo；  API声明：src: string | Resource;  差异内容：NA | 类名：ImageFrameInfo；  API声明：src: string | Resource | PixelMap;  差异内容：form | component/image\_animator.d.ts |
| API卡片权限变更 | 类名：ImageFrameInfo；  API声明：width?: number | string;  差异内容：NA | 类名：ImageFrameInfo；  API声明：width?: number | string;  差异内容：form | component/image\_animator.d.ts |
| API卡片权限变更 | 类名：ImageFrameInfo；  API声明：height?: number | string;  差异内容：NA | 类名：ImageFrameInfo；  API声明：height?: number | string;  差异内容：form | component/image\_animator.d.ts |
| API卡片权限变更 | 类名：ImageFrameInfo；  API声明：top?: number | string;  差异内容：NA | 类名：ImageFrameInfo；  API声明：top?: number | string;  差异内容：form | component/image\_animator.d.ts |
| API卡片权限变更 | 类名：ImageFrameInfo；  API声明：left?: number | string;  差异内容：NA | 类名：ImageFrameInfo；  API声明：left?: number | string;  差异内容：form | component/image\_animator.d.ts |
| API卡片权限变更 | 类名：global；  API声明： declare class ImageAnimatorAttribute  差异内容：NA | 类名：global；  API声明： declare class ImageAnimatorAttribute  差异内容：form | component/image\_animator.d.ts |
| API卡片权限变更 | 类名：ImageAnimatorAttribute；  API声明：images(value: Array<ImageFrameInfo>): ImageAnimatorAttribute;  差异内容：NA | 类名：ImageAnimatorAttribute；  API声明：images(value: Array<ImageFrameInfo>): ImageAnimatorAttribute;  差异内容：form | component/image\_animator.d.ts |
| API卡片权限变更 | 类名：ImageAnimatorAttribute；  API声明：state(value: AnimationStatus): ImageAnimatorAttribute;  差异内容：NA | 类名：ImageAnimatorAttribute；  API声明：state(value: AnimationStatus): ImageAnimatorAttribute;  差异内容：form | component/image\_animator.d.ts |
| API卡片权限变更 | 类名：ImageAnimatorAttribute；  API声明：duration(value: number): ImageAnimatorAttribute;  差异内容：NA | 类名：ImageAnimatorAttribute；  API声明：duration(value: number): ImageAnimatorAttribute;  差异内容：form | component/image\_animator.d.ts |
| API卡片权限变更 | 类名：ImageAnimatorAttribute；  API声明：reverse(value: boolean): ImageAnimatorAttribute;  差异内容：NA | 类名：ImageAnimatorAttribute；  API声明：reverse(value: boolean): ImageAnimatorAttribute;  差异内容：form | component/image\_animator.d.ts |
| API卡片权限变更 | 类名：ImageAnimatorAttribute；  API声明：fixedSize(value: boolean): ImageAnimatorAttribute;  差异内容：NA | 类名：ImageAnimatorAttribute；  API声明：fixedSize(value: boolean): ImageAnimatorAttribute;  差异内容：form | component/image\_animator.d.ts |
| API卡片权限变更 | 类名：ImageAnimatorAttribute；  API声明：fillMode(value: FillMode): ImageAnimatorAttribute;  差异内容：NA | 类名：ImageAnimatorAttribute；  API声明：fillMode(value: FillMode): ImageAnimatorAttribute;  差异内容：form | component/image\_animator.d.ts |
| API卡片权限变更 | 类名：ImageAnimatorAttribute；  API声明：onStart(event: () => void): ImageAnimatorAttribute;  差异内容：NA | 类名：ImageAnimatorAttribute；  API声明：onStart(event: () => void): ImageAnimatorAttribute;  差异内容：form | component/image\_animator.d.ts |
| API卡片权限变更 | 类名：ImageAnimatorAttribute；  API声明：onPause(event: () => void): ImageAnimatorAttribute;  差异内容：NA | 类名：ImageAnimatorAttribute；  API声明：onPause(event: () => void): ImageAnimatorAttribute;  差异内容：form | component/image\_animator.d.ts |
| API卡片权限变更 | 类名：ImageAnimatorAttribute；  API声明：onCancel(event: () => void): ImageAnimatorAttribute;  差异内容：NA | 类名：ImageAnimatorAttribute；  API声明：onCancel(event: () => void): ImageAnimatorAttribute;  差异内容：form | component/image\_animator.d.ts |
| API卡片权限变更 | 类名：ImageAnimatorAttribute；  API声明：onFinish(event: () => void): ImageAnimatorAttribute;  差异内容：NA | 类名：ImageAnimatorAttribute；  API声明：onFinish(event: () => void): ImageAnimatorAttribute;  差异内容：form | component/image\_animator.d.ts |
| API卡片权限变更 | 类名：global；  API声明：declare const ImageAnimator: ImageAnimatorInterface;  差异内容：NA | 类名：global；  API声明：declare const ImageAnimator: ImageAnimatorInterface;  差异内容：form | component/image\_animator.d.ts |
| API卡片权限变更 | 类名：global；  API声明：declare const ImageAnimatorInstance: ImageAnimatorAttribute;  差异内容：NA | 类名：global；  API声明：declare const ImageAnimatorInstance: ImageAnimatorAttribute;  差异内容：form | component/image\_animator.d.ts |
| API卡片权限变更 | 类名：ListItemAttribute；  API声明：selectable(value: boolean): ListItemAttribute;  差异内容：NA | 类名：ListItemAttribute；  API声明：selectable(value: boolean): ListItemAttribute;  差异内容：form | component/list\_item.d.ts |
| API卡片权限变更 | 类名：global；  API声明：declare type Matrix2D = import('../api/@internal/full/canvaspattern').Matrix2D;  差异内容：NA | 类名：global；  API声明： declare class Matrix2D  差异内容：form | component/matrix2d.d.ts |
| API卡片权限变更 | 类名：global；  API声明： declare class PolygonAttribute  差异内容：NA | 类名：global；  API声明： declare class PolygonAttribute  差异内容：form | component/polygon.d.ts |
| API卡片权限变更 | 类名：global；  API声明： declare class SwiperController  差异内容：NA | 类名：global；  API声明： declare class SwiperController  差异内容：form | component/swiper.d.ts |
| API卡片权限变更 | 类名：SwiperController；  API声明：showNext();  差异内容：NA | 类名：SwiperController；  API声明：showNext();  差异内容：form | component/swiper.d.ts |
| API卡片权限变更 | 类名：SwiperController；  API声明：showPrevious();  差异内容：NA | 类名：SwiperController；  API声明：showPrevious();  差异内容：form | component/swiper.d.ts |
| API卡片权限变更 | 类名：SwiperController；  API声明：finishAnimation(callback?: () => void);  差异内容：NA | 类名：SwiperController；  API声明：finishAnimation(callback?: () => void);  差异内容：form | component/swiper.d.ts |
| API卡片权限变更 | 类名：global；  API声明： declare enum SwiperDisplayMode  差异内容：NA | 类名：global；  API声明： declare enum SwiperDisplayMode  差异内容：form | component/swiper.d.ts |
| API卡片权限变更 | 类名：SwiperDisplayMode；  API声明：Stretch  差异内容：NA | 类名：SwiperDisplayMode；  API声明：Stretch  差异内容：form | component/swiper.d.ts |
| API卡片权限变更 | 类名：SwiperDisplayMode；  API声明：AutoLinear  差异内容：NA | 类名：SwiperDisplayMode；  API声明：AutoLinear  差异内容：form | component/swiper.d.ts |
| API卡片权限变更 | 类名：global；  API声明： interface SwiperInterface  差异内容：NA | 类名：global；  API声明： interface SwiperInterface  差异内容：form | component/swiper.d.ts |
| API卡片权限变更 | 类名：global；  API声明： declare class SwiperAttribute  差异内容：NA | 类名：global；  API声明： declare class SwiperAttribute  差异内容：form | component/swiper.d.ts |
| API卡片权限变更 | 类名：SwiperAttribute；  API声明：index(value: number): SwiperAttribute;  差异内容：NA | 类名：SwiperAttribute；  API声明：index(value: number): SwiperAttribute;  差异内容：form | component/swiper.d.ts |
| API卡片权限变更 | 类名：SwiperAttribute；  API声明：autoPlay(value: boolean): SwiperAttribute;  差异内容：NA | 类名：SwiperAttribute；  API声明：autoPlay(value: boolean): SwiperAttribute;  差异内容：form | component/swiper.d.ts |
| API卡片权限变更 | 类名：SwiperAttribute；  API声明：interval(value: number): SwiperAttribute;  差异内容：NA | 类名：SwiperAttribute；  API声明：interval(value: number): SwiperAttribute;  差异内容：form | component/swiper.d.ts |
| API卡片权限变更 | 类名：SwiperAttribute；  API声明：indicator(value: boolean): SwiperAttribute;  差异内容：NA | 类名：SwiperAttribute；  API声明：indicator(value: DotIndicator | DigitIndicator | boolean): SwiperAttribute;  差异内容：form | component/swiper.d.ts |
| API卡片权限变更 | 类名：SwiperAttribute；  API声明：loop(value: boolean): SwiperAttribute;  差异内容：NA | 类名：SwiperAttribute；  API声明：loop(value: boolean): SwiperAttribute;  差异内容：form | component/swiper.d.ts |
| API卡片权限变更 | 类名：SwiperAttribute；  API声明：vertical(value: boolean): SwiperAttribute;  差异内容：NA | 类名：SwiperAttribute；  API声明：vertical(value: boolean): SwiperAttribute;  差异内容：form | component/swiper.d.ts |
| API卡片权限变更 | 类名：SwiperAttribute；  API声明：itemSpace(value: number | string): SwiperAttribute;  差异内容：NA | 类名：SwiperAttribute；  API声明：itemSpace(value: number | string): SwiperAttribute;  差异内容：form | component/swiper.d.ts |
| API卡片权限变更 | 类名：SwiperAttribute；  API声明：displayMode(value: SwiperDisplayMode): SwiperAttribute;  差异内容：NA | 类名：SwiperAttribute；  API声明：displayMode(value: SwiperDisplayMode): SwiperAttribute;  差异内容：form | component/swiper.d.ts |
| API卡片权限变更 | 类名：SwiperAttribute；  API声明：cachedCount(value: number): SwiperAttribute;  差异内容：NA | 类名：SwiperAttribute；  API声明：cachedCount(value: number): SwiperAttribute;  差异内容：form | component/swiper.d.ts |
| API卡片权限变更 | 类名：SwiperAttribute；  API声明：displayCount(value: number | string): SwiperAttribute;  差异内容：NA | 类名：SwiperAttribute；  API声明：displayCount(value: number | string | SwiperAutoFill, swipeByGroup?: boolean): SwiperAttribute;  差异内容：form | component/swiper.d.ts |
| API卡片权限变更 | 类名：SwiperAttribute；  API声明：effectMode(value: EdgeEffect): SwiperAttribute;  差异内容：NA | 类名：SwiperAttribute；  API声明：effectMode(value: EdgeEffect): SwiperAttribute;  差异内容：form | component/swiper.d.ts |
| API卡片权限变更 | 类名：SwiperAttribute；  API声明：disableSwipe(value: boolean): SwiperAttribute;  差异内容：NA | 类名：SwiperAttribute；  API声明：disableSwipe(value: boolean): SwiperAttribute;  差异内容：form | component/swiper.d.ts |
| API卡片权限变更 | 类名：SwiperAttribute；  API声明：curve(value: Curve | string): SwiperAttribute;  差异内容：NA | 类名：SwiperAttribute；  API声明：curve(value: Curve | string | ICurve): SwiperAttribute;  差异内容：form | component/swiper.d.ts |
| API卡片权限变更 | 类名：SwiperAttribute；  API声明：onChange(event: (index: number) => void): SwiperAttribute;  差异内容：NA | 类名：SwiperAttribute；  API声明：onChange(event: (index: number) => void): SwiperAttribute;  差异内容：form | component/swiper.d.ts |
| API卡片权限变更 | 类名：SwiperAttribute；  API声明：onAnimationStart(event: (index: number) => void): SwiperAttribute;  差异内容：NA | 类名：SwiperAttribute；  API声明：onAnimationStart(event: (index: number, targetIndex: number, extraInfo: SwiperAnimationEvent) => void): SwiperAttribute;  差异内容：form | component/swiper.d.ts |
| API卡片权限变更 | 类名：SwiperAttribute；  API声明：onAnimationEnd(event: (index: number) => void): SwiperAttribute;  差异内容：NA | 类名：SwiperAttribute；  API声明：onAnimationEnd(event: (index: number, extraInfo: SwiperAnimationEvent) => void): SwiperAttribute;  差异内容：form | component/swiper.d.ts |
| API卡片权限变更 | 类名：global；  API声明：declare const Swiper: SwiperInterface;  差异内容：NA | 类名：global；  API声明：declare const Swiper: SwiperInterface;  差异内容：form | component/swiper.d.ts |
| API卡片权限变更 | 类名：global；  API声明：declare const SwiperInstance: SwiperAttribute;  差异内容：NA | 类名：global；  API声明：declare const SwiperInstance: SwiperAttribute;  差异内容：form | component/swiper.d.ts |
| API卡片权限变更 | 类名：global；  API声明： declare class TextClockController  差异内容：NA | 类名：global；  API声明： declare class TextClockController  差异内容：form | component/text\_clock.d.ts |
| API卡片权限变更 | 类名：TextClockController；  API声明：start();  差异内容：NA | 类名：TextClockController；  API声明：start();  差异内容：form | component/text\_clock.d.ts |
| API卡片权限变更 | 类名：TextClockController；  API声明：stop();  差异内容：NA | 类名：TextClockController；  API声明：stop();  差异内容：form | component/text\_clock.d.ts |
| API卡片权限变更 | 类名：global；  API声明： interface TextClockInterface  差异内容：NA | 类名：global；  API声明： interface TextClockInterface  差异内容：form | component/text\_clock.d.ts |
| API卡片权限变更 | 类名：global；  API声明： declare class TextClockAttribute  差异内容：NA | 类名：global；  API声明： declare class TextClockAttribute  差异内容：form | component/text\_clock.d.ts |
| API卡片权限变更 | 类名：TextClockAttribute；  API声明：format(value: string): TextClockAttribute;  差异内容：NA | 类名：TextClockAttribute；  API声明：format(value: string): TextClockAttribute;  差异内容：form | component/text\_clock.d.ts |
| API卡片权限变更 | 类名：TextClockAttribute；  API声明：onDateChange(event: (value: number) => void): TextClockAttribute;  差异内容：NA | 类名：TextClockAttribute；  API声明：onDateChange(event: (value: number) => void): TextClockAttribute;  差异内容：form | component/text\_clock.d.ts |
| API卡片权限变更 | 类名：TextClockAttribute；  API声明：fontColor(value: ResourceColor): TextClockAttribute;  差异内容：NA | 类名：TextClockAttribute；  API声明：fontColor(value: ResourceColor): TextClockAttribute;  差异内容：form | component/text\_clock.d.ts |
| API卡片权限变更 | 类名：TextClockAttribute；  API声明：fontSize(value: Length): TextClockAttribute;  差异内容：NA | 类名：TextClockAttribute；  API声明：fontSize(value: Length): TextClockAttribute;  差异内容：form | component/text\_clock.d.ts |
| API卡片权限变更 | 类名：TextClockAttribute；  API声明：fontStyle(value: FontStyle): TextClockAttribute;  差异内容：NA | 类名：TextClockAttribute；  API声明：fontStyle(value: FontStyle): TextClockAttribute;  差异内容：form | component/text\_clock.d.ts |
| API卡片权限变更 | 类名：TextClockAttribute；  API声明：fontWeight(value: number | FontWeight | string): TextClockAttribute;  差异内容：NA | 类名：TextClockAttribute；  API声明：fontWeight(value: number | FontWeight | string): TextClockAttribute;  差异内容：form | component/text\_clock.d.ts |
| API卡片权限变更 | 类名：TextClockAttribute；  API声明：fontFamily(value: ResourceStr): TextClockAttribute;  差异内容：NA | 类名：TextClockAttribute；  API声明：fontFamily(value: ResourceStr): TextClockAttribute;  差异内容：form | component/text\_clock.d.ts |
| API卡片权限变更 | 类名：global；  API声明：declare const TextClock: TextClockInterface;  差异内容：NA | 类名：global；  API声明：declare const TextClock: TextClockInterface;  差异内容：form | component/text\_clock.d.ts |
| API卡片权限变更 | 类名：global；  API声明：declare const TextClockInstance: TextClockAttribute;  差异内容：NA | 类名：global；  API声明：declare const TextClockInstance: TextClockAttribute;  差异内容：form | component/text\_clock.d.ts |
| API卡片权限变更 | 类名：global；  API声明： declare class TextTimerController  差异内容：NA | 类名：global；  API声明： declare class TextTimerController  差异内容：form | component/text\_timer.d.ts |
| API卡片权限变更 | 类名：TextTimerController；  API声明：start();  差异内容：NA | 类名：TextTimerController；  API声明：start();  差异内容：form | component/text\_timer.d.ts |
| API卡片权限变更 | 类名：TextTimerController；  API声明：pause();  差异内容：NA | 类名：TextTimerController；  API声明：pause();  差异内容：form | component/text\_timer.d.ts |
| API卡片权限变更 | 类名：TextTimerController；  API声明：reset();  差异内容：NA | 类名：TextTimerController；  API声明：reset();  差异内容：form | component/text\_timer.d.ts |
| API卡片权限变更 | 类名：global；  API声明： interface TextTimerOptions  差异内容：NA | 类名：global；  API声明： interface TextTimerOptions  差异内容：form | component/text\_timer.d.ts |
| API卡片权限变更 | 类名：TextTimerOptions；  API声明：isCountDown?: boolean;  差异内容：NA | 类名：TextTimerOptions；  API声明：isCountDown?: boolean;  差异内容：form | component/text\_timer.d.ts |
| API卡片权限变更 | 类名：TextTimerOptions；  API声明：count?: number;  差异内容：NA | 类名：TextTimerOptions；  API声明：count?: number;  差异内容：form | component/text\_timer.d.ts |
| API卡片权限变更 | 类名：TextTimerOptions；  API声明：controller?: TextTimerController;  差异内容：NA | 类名：TextTimerOptions；  API声明：controller?: TextTimerController;  差异内容：form | component/text\_timer.d.ts |
| API卡片权限变更 | 类名：global；  API声明： interface TextTimerInterface  差异内容：NA | 类名：global；  API声明： interface TextTimerInterface  差异内容：form | component/text\_timer.d.ts |
| API卡片权限变更 | 类名：global；  API声明： declare class TextTimerAttribute  差异内容：NA | 类名：global；  API声明： declare class TextTimerAttribute  差异内容：form | component/text\_timer.d.ts |
| API卡片权限变更 | 类名：TextTimerAttribute；  API声明：format(value: string): TextTimerAttribute;  差异内容：NA | 类名：TextTimerAttribute；  API声明：format(value: string): TextTimerAttribute;  差异内容：form | component/text\_timer.d.ts |
| API卡片权限变更 | 类名：TextTimerAttribute；  API声明：fontColor(value: ResourceColor): TextTimerAttribute;  差异内容：NA | 类名：TextTimerAttribute；  API声明：fontColor(value: ResourceColor): TextTimerAttribute;  差异内容：form | component/text\_timer.d.ts |
| API卡片权限变更 | 类名：TextTimerAttribute；  API声明：fontSize(value: Length): TextTimerAttribute;  差异内容：NA | 类名：TextTimerAttribute；  API声明：fontSize(value: Length): TextTimerAttribute;  差异内容：form | component/text\_timer.d.ts |
| API卡片权限变更 | 类名：TextTimerAttribute；  API声明：fontStyle(value: FontStyle): TextTimerAttribute;  差异内容：NA | 类名：TextTimerAttribute；  API声明：fontStyle(value: FontStyle): TextTimerAttribute;  差异内容：form | component/text\_timer.d.ts |
| API卡片权限变更 | 类名：TextTimerAttribute；  API声明：fontWeight(value: number | FontWeight | string): TextTimerAttribute;  差异内容：NA | 类名：TextTimerAttribute；  API声明：fontWeight(value: number | FontWeight | string): TextTimerAttribute;  差异内容：form | component/text\_timer.d.ts |
| API卡片权限变更 | 类名：TextTimerAttribute；  API声明：fontFamily(value: ResourceStr): TextTimerAttribute;  差异内容：NA | 类名：TextTimerAttribute；  API声明：fontFamily(value: ResourceStr): TextTimerAttribute;  差异内容：form | component/text\_timer.d.ts |
| API卡片权限变更 | 类名：TextTimerAttribute；  API声明：onTimer(event: (utc: number, elapsedTime: number) => void): TextTimerAttribute;  差异内容：NA | 类名：TextTimerAttribute；  API声明：onTimer(event: (utc: number, elapsedTime: number) => void): TextTimerAttribute;  差异内容：form | component/text\_timer.d.ts |
| API卡片权限变更 | 类名：global；  API声明：declare const TextTimer: TextTimerInterface;  差异内容：NA | 类名：global；  API声明：declare const TextTimer: TextTimerInterface;  差异内容：form | component/text\_timer.d.ts |
| API卡片权限变更 | 类名：global；  API声明：declare const TextTimerInstance: TextTimerAttribute;  差异内容：NA | 类名：global；  API声明：declare const TextTimerInstance: TextTimerAttribute;  差异内容：form | component/text\_timer.d.ts |
| API卡片权限变更 | 类名：global；  API声明： declare interface TransitionOptions  差异内容：form | 类名：global；  API声明： declare interface TransitionOptions  差异内容：NA | component/common.d.ts |
| API卡片权限变更 | 类名：TransitionOptions；  API声明：type?: TransitionType;  差异内容：form | 类名：TransitionOptions；  API声明：type?: TransitionType;  差异内容：NA | component/common.d.ts |
| API卡片权限变更 | 类名：TransitionOptions；  API声明：opacity?: number;  差异内容：form | 类名：TransitionOptions；  API声明：opacity?: number;  差异内容：NA | component/common.d.ts |
| API卡片权限变更 | 类名：TransitionOptions；  API声明：translate?: TranslateOptions;  差异内容：form | 类名：TransitionOptions；  API声明：translate?: TranslateOptions;  差异内容：NA | component/common.d.ts |
| API卡片权限变更 | 类名：TransitionOptions；  API声明：scale?: ScaleOptions;  差异内容：form | 类名：TransitionOptions；  API声明：scale?: ScaleOptions;  差异内容：NA | component/common.d.ts |
| API卡片权限变更 | 类名：TransitionOptions；  API声明：rotate?: RotateOptions;  差异内容：form | 类名：TransitionOptions；  API声明：rotate?: RotateOptions;  差异内容：NA | component/common.d.ts |
| API卡片权限变更 | 类名：ClickEvent；  API声明：screenX: number;  差异内容：form | 类名：ClickEvent；  API声明：screenX: number;  差异内容：NA | component/common.d.ts |
| API卡片权限变更 | 类名：ClickEvent；  API声明：screenY: number;  差异内容：form | 类名：ClickEvent；  API声明：screenY: number;  差异内容：NA | component/common.d.ts |
| API废弃版本变更 | 类名：Result；  API声明：code: number;  差异内容：NA | 类名：Result；  API声明：code: number;  差异内容：8 | api/@internal/full/featureability.d.ts |
| API废弃版本变更 | 类名：Result；  API声明：data: object;  差异内容：NA | 类名：Result；  API声明：data: object;  差异内容：8 | api/@internal/full/featureability.d.ts |
| API废弃版本变更 | 类名：SubscribeMessageResponse；  API声明：deviceId: string;  差异内容：NA | 类名：SubscribeMessageResponse；  API声明：deviceId: string;  差异内容：8 | api/@internal/full/featureability.d.ts |
| API废弃版本变更 | 类名：SubscribeMessageResponse；  API声明：bundleName: string;  差异内容：NA | 类名：SubscribeMessageResponse；  API声明：bundleName: string;  差异内容：8 | api/@internal/full/featureability.d.ts |
| API废弃版本变更 | 类名：SubscribeMessageResponse；  API声明：abilityName: string;  差异内容：NA | 类名：SubscribeMessageResponse；  API声明：abilityName: string;  差异内容：8 | api/@internal/full/featureability.d.ts |
| API废弃版本变更 | 类名：SubscribeMessageResponse；  API声明：message: string;  差异内容：NA | 类名：SubscribeMessageResponse；  API声明：message: string;  差异内容：8 | api/@internal/full/featureability.d.ts |
| API废弃版本变更 | 类名：CallAbilityParam；  API声明：bundleName: string;  差异内容：NA | 类名：CallAbilityParam；  API声明：bundleName: string;  差异内容：8 | api/@internal/full/featureability.d.ts |
| API废弃版本变更 | 类名：CallAbilityParam；  API声明：abilityName: string;  差异内容：NA | 类名：CallAbilityParam；  API声明：abilityName: string;  差异内容：8 | api/@internal/full/featureability.d.ts |
| API废弃版本变更 | 类名：CallAbilityParam；  API声明：messageCode: number;  差异内容：NA | 类名：CallAbilityParam；  API声明：messageCode: number;  差异内容：8 | api/@internal/full/featureability.d.ts |
| API废弃版本变更 | 类名：CallAbilityParam；  API声明：abilityType: number;  差异内容：NA | 类名：CallAbilityParam；  API声明：abilityType: number;  差异内容：8 | api/@internal/full/featureability.d.ts |
| API废弃版本变更 | 类名：CallAbilityParam；  API声明：data?: object;  差异内容：NA | 类名：CallAbilityParam；  API声明：data?: object;  差异内容：8 | api/@internal/full/featureability.d.ts |
| API废弃版本变更 | 类名：CallAbilityParam；  API声明：syncOption?: number;  差异内容：NA | 类名：CallAbilityParam；  API声明：syncOption?: number;  差异内容：8 | api/@internal/full/featureability.d.ts |
| API废弃版本变更 | 类名：SubscribeAbilityEventParam；  API声明：bundleName: string;  差异内容：NA | 类名：SubscribeAbilityEventParam；  API声明：bundleName: string;  差异内容：8 | api/@internal/full/featureability.d.ts |
| API废弃版本变更 | 类名：SubscribeAbilityEventParam；  API声明：abilityName: string;  差异内容：NA | 类名：SubscribeAbilityEventParam；  API声明：abilityName: string;  差异内容：8 | api/@internal/full/featureability.d.ts |
| API废弃版本变更 | 类名：SubscribeAbilityEventParam；  API声明：messageCode: number;  差异内容：NA | 类名：SubscribeAbilityEventParam；  API声明：messageCode: number;  差异内容：8 | api/@internal/full/featureability.d.ts |
| API废弃版本变更 | 类名：SubscribeAbilityEventParam；  API声明：abilityType: number;  差异内容：NA | 类名：SubscribeAbilityEventParam；  API声明：abilityType: number;  差异内容：8 | api/@internal/full/featureability.d.ts |
| API废弃版本变更 | 类名：SubscribeAbilityEventParam；  API声明：syncOption?: number;  差异内容：NA | 类名：SubscribeAbilityEventParam；  API声明：syncOption?: number;  差异内容：8 | api/@internal/full/featureability.d.ts |
| API废弃版本变更 | 类名：SendMessageOptions；  API声明：deviceId: string;  差异内容：NA | 类名：SendMessageOptions；  API声明：deviceId: string;  差异内容：8 | api/@internal/full/featureability.d.ts |
| API废弃版本变更 | 类名：SendMessageOptions；  API声明：bundleName: string;  差异内容：NA | 类名：SendMessageOptions；  API声明：bundleName: string;  差异内容：8 | api/@internal/full/featureability.d.ts |
| API废弃版本变更 | 类名：SendMessageOptions；  API声明：abilityName: string;  差异内容：NA | 类名：SendMessageOptions；  API声明：abilityName: string;  差异内容：8 | api/@internal/full/featureability.d.ts |
| API废弃版本变更 | 类名：SendMessageOptions；  API声明：message?: string;  差异内容：NA | 类名：SendMessageOptions；  API声明：message?: string;  差异内容：8 | api/@internal/full/featureability.d.ts |
| API废弃版本变更 | 类名：SendMessageOptions；  API声明：success?: () => void;  差异内容：NA | 类名：SendMessageOptions；  API声明：success?: () => void;  差异内容：8 | api/@internal/full/featureability.d.ts |
| API废弃版本变更 | 类名：SendMessageOptions；  API声明：fail?: (data: string, code: number) => void;  差异内容：NA | 类名：SendMessageOptions；  API声明：fail?: (data: string, code: number) => void;  差异内容：8 | api/@internal/full/featureability.d.ts |
| API废弃版本变更 | 类名：SendMessageOptions；  API声明：complete?: () => void;  差异内容：NA | 类名：SendMessageOptions；  API声明：complete?: () => void;  差异内容：8 | api/@internal/full/featureability.d.ts |
| API废弃版本变更 | 类名：SubscribeMessageOptions；  API声明：success?: (data: SubscribeMessageResponse) => void;  差异内容：NA | 类名：SubscribeMessageOptions；  API声明：success?: (data: SubscribeMessageResponse) => void;  差异内容：8 | api/@internal/full/featureability.d.ts |
| API废弃版本变更 | 类名：SubscribeMessageOptions；  API声明：fail?: (data: string, code: number) => void;  差异内容：NA | 类名：SubscribeMessageOptions；  API声明：fail?: (data: string, code: number) => void;  差异内容：8 | api/@internal/full/featureability.d.ts |
| API废弃版本变更 | 类名：RequestParams；  API声明：bundleName?: string;  差异内容：NA | 类名：RequestParams；  API声明：bundleName?: string;  差异内容：8 | api/@internal/full/featureability.d.ts |
| API废弃版本变更 | 类名：RequestParams；  API声明：abilityName?: string;  差异内容：NA | 类名：RequestParams；  API声明：abilityName?: string;  差异内容：8 | api/@internal/full/featureability.d.ts |
| API废弃版本变更 | 类名：RequestParams；  API声明：entities?: Array<string>;  差异内容：NA | 类名：RequestParams；  API声明：entities?: Array<string>;  差异内容：8 | api/@internal/full/featureability.d.ts |
| API废弃版本变更 | 类名：RequestParams；  API声明：action?: string;  差异内容：NA | 类名：RequestParams；  API声明：action?: string;  差异内容：8 | api/@internal/full/featureability.d.ts |
| API废弃版本变更 | 类名：RequestParams；  API声明：deviceType?: number;  差异内容：NA | 类名：RequestParams；  API声明：deviceType?: number;  差异内容：8 | api/@internal/full/featureability.d.ts |
| API废弃版本变更 | 类名：RequestParams；  API声明：data?: object;  差异内容：NA | 类名：RequestParams；  API声明：data?: object;  差异内容：8 | api/@internal/full/featureability.d.ts |
| API废弃版本变更 | 类名：RequestParams；  API声明：flag?: number;  差异内容：NA | 类名：RequestParams；  API声明：flag?: number;  差异内容：8 | api/@internal/full/featureability.d.ts |
| API废弃版本变更 | 类名：RequestParams；  API声明：url?: string;  差异内容：NA | 类名：RequestParams；  API声明：url?: string;  差异内容：8 | api/@internal/full/featureability.d.ts |
| API废弃版本变更 | 类名：FinishWithResultParams；  API声明：code: number;  差异内容：NA | 类名：FinishWithResultParams；  API声明：code: number;  差异内容：8 | api/@internal/full/featureability.d.ts |
| API废弃版本变更 | 类名：FinishWithResultParams；  API声明：result: object;  差异内容：NA | 类名：FinishWithResultParams；  API声明：result: object;  差异内容：8 | api/@internal/full/featureability.d.ts |
| API废弃版本变更 | 类名：AnimatorResult；  API声明：onframe: (progress: number) => void;  差异内容：NA | 类名：AnimatorResult；  API声明：onframe: (progress: number) => void;  差异内容：12 | api/@ohos.animator.d.ts |
| API废弃版本变更 | 类名：AnimatorResult；  API声明：onfinish: () => void;  差异内容：NA | 类名：AnimatorResult；  API声明：onfinish: () => void;  差异内容：12 | api/@ohos.animator.d.ts |
| API废弃版本变更 | 类名：AnimatorResult；  API声明：oncancel: () => void;  差异内容：NA | 类名：AnimatorResult；  API声明：oncancel: () => void;  差异内容：12 | api/@ohos.animator.d.ts |
| API废弃版本变更 | 类名：AnimatorResult；  API声明：onrepeat: () => void;  差异内容：NA | 类名：AnimatorResult；  API声明：onrepeat: () => void;  差异内容：12 | api/@ohos.animator.d.ts |
| API废弃版本变更 | 类名：matrix4；  API声明：function copy(): Matrix4Transit;  差异内容：NA | 类名：matrix4；  API声明：function copy(): Matrix4Transit;  差异内容：10 | api/@ohos.matrix4.d.ts |
| API废弃版本变更 | 类名：matrix4；  API声明：function invert(): Matrix4Transit;  差异内容：NA | 类名：matrix4；  API声明：function invert(): Matrix4Transit;  差异内容：10 | api/@ohos.matrix4.d.ts |
| API废弃版本变更 | 类名：matrix4；  API声明：function combine(options: Matrix4Transit): Matrix4Transit;  差异内容：NA | 类名：matrix4；  API声明：function combine(options: Matrix4Transit): Matrix4Transit;  差异内容：10 | api/@ohos.matrix4.d.ts |
| API废弃版本变更 | 类名：matrix4；  API声明：function translate(options: TranslateOption): Matrix4Transit;  差异内容：NA | 类名：matrix4；  API声明：function translate(options: TranslateOption): Matrix4Transit;  差异内容：10 | api/@ohos.matrix4.d.ts |
| API废弃版本变更 | 类名：matrix4；  API声明：function scale(options: ScaleOption): Matrix4Transit;  差异内容：NA | 类名：matrix4；  API声明：function scale(options: ScaleOption): Matrix4Transit;  差异内容：10 | api/@ohos.matrix4.d.ts |
| API废弃版本变更 | 类名：matrix4；  API声明：function rotate(options: RotateOption): Matrix4Transit;  差异内容：NA | 类名：matrix4；  API声明：function rotate(options: RotateOption): Matrix4Transit;  差异内容：10 | api/@ohos.matrix4.d.ts |
| API废弃版本变更 | 类名：matrix4；  API声明：function transformPoint(options: [  number,  number  ]): [  number,  number  ];  差异内容：NA | 类名：matrix4；  API声明：function transformPoint(options: [  number,  number  ]): [  number,  number  ];  差异内容：10 | api/@ohos.matrix4.d.ts |
| API废弃版本变更 | 类名：prompt；  API声明： interface ShowToastOptions  差异内容：NA | 类名：prompt；  API声明： interface ShowToastOptions  差异内容：9 | api/@ohos.prompt.d.ts |
| API废弃版本变更 | 类名：ShowToastOptions；  API声明：message: string;  差异内容：NA | 类名：ShowToastOptions；  API声明：message: string;  差异内容：9 | api/@ohos.prompt.d.ts |
| API废弃版本变更 | 类名：ShowToastOptions；  API声明：duration?: number;  差异内容：NA | 类名：ShowToastOptions；  API声明：duration?: number;  差异内容：9 | api/@ohos.prompt.d.ts |
| API废弃版本变更 | 类名：ShowToastOptions；  API声明：bottom?: string | number;  差异内容：NA | 类名：ShowToastOptions；  API声明：bottom?: string | number;  差异内容：9 | api/@ohos.prompt.d.ts |
| API废弃版本变更 | 类名：prompt；  API声明： interface Button  差异内容：NA | 类名：prompt；  API声明： interface Button  差异内容：9 | api/@ohos.prompt.d.ts |
| API废弃版本变更 | 类名：Button；  API声明：text: string;  差异内容：NA | 类名：Button；  API声明：text: string;  差异内容：9 | api/@ohos.prompt.d.ts |
| API废弃版本变更 | 类名：Button；  API声明：color: string;  差异内容：NA | 类名：Button；  API声明：color: string;  差异内容：9 | api/@ohos.prompt.d.ts |
| API废弃版本变更 | 类名：prompt；  API声明： interface ShowDialogSuccessResponse  差异内容：NA | 类名：prompt；  API声明： interface ShowDialogSuccessResponse  差异内容：9 | api/@ohos.prompt.d.ts |
| API废弃版本变更 | 类名：ShowDialogSuccessResponse；  API声明：index: number;  差异内容：NA | 类名：ShowDialogSuccessResponse；  API声明：index: number;  差异内容：9 | api/@ohos.prompt.d.ts |
| API废弃版本变更 | 类名：prompt；  API声明： interface ShowDialogOptions  差异内容：NA | 类名：prompt；  API声明： interface ShowDialogOptions  差异内容：9 | api/@ohos.prompt.d.ts |
| API废弃版本变更 | 类名：ShowDialogOptions；  API声明：title?: string;  差异内容：NA | 类名：ShowDialogOptions；  API声明：title?: string;  差异内容：9 | api/@ohos.prompt.d.ts |
| API废弃版本变更 | 类名：ShowDialogOptions；  API声明：message?: string;  差异内容：NA | 类名：ShowDialogOptions；  API声明：message?: string;  差异内容：9 | api/@ohos.prompt.d.ts |
| API废弃版本变更 | 类名：ShowDialogOptions；  API声明：buttons?: [  Button,  Button?,  Button?  ];  差异内容：NA | 类名：ShowDialogOptions；  API声明：buttons?: [  Button,  Button?,  Button?  ];  差异内容：9 | api/@ohos.prompt.d.ts |
| API废弃版本变更 | 类名：prompt；  API声明： interface ActionMenuSuccessResponse  差异内容：NA | 类名：prompt；  API声明： interface ActionMenuSuccessResponse  差异内容：9 | api/@ohos.prompt.d.ts |
| API废弃版本变更 | 类名：ActionMenuSuccessResponse；  API声明：index: number;  差异内容：NA | 类名：ActionMenuSuccessResponse；  API声明：index: number;  差异内容：9 | api/@ohos.prompt.d.ts |
| API废弃版本变更 | 类名：prompt；  API声明： interface ActionMenuOptions  差异内容：NA | 类名：prompt；  API声明： interface ActionMenuOptions  差异内容：9 | api/@ohos.prompt.d.ts |
| API废弃版本变更 | 类名：ActionMenuOptions；  API声明：title?: string;  差异内容：NA | 类名：ActionMenuOptions；  API声明：title?: string;  差异内容：9 | api/@ohos.prompt.d.ts |
| API废弃版本变更 | 类名：ActionMenuOptions；  API声明：buttons: [  Button,  Button?,  Button?,  Button?,  Button?,  Button?  ];  差异内容：NA | 类名：ActionMenuOptions；  API声明：buttons: [  Button,  Button?,  Button?,  Button?,  Button?,  Button?  ];  差异内容：9 | api/@ohos.prompt.d.ts |
| API废弃版本变更 | 类名：prompt；  API声明：function showToast(options: ShowToastOptions): void;  差异内容：NA | 类名：prompt；  API声明：function showToast(options: ShowToastOptions): void;  差异内容：9 | api/@ohos.prompt.d.ts |
| API废弃版本变更 | 类名：prompt；  API声明：function showDialog(options: ShowDialogOptions, callback: AsyncCallback<ShowDialogSuccessResponse>): void;  差异内容：NA | 类名：prompt；  API声明：function showDialog(options: ShowDialogOptions, callback: AsyncCallback<ShowDialogSuccessResponse>): void;  差异内容：9 | api/@ohos.prompt.d.ts |
| API废弃版本变更 | 类名：prompt；  API声明：function showDialog(options: ShowDialogOptions): Promise<ShowDialogSuccessResponse>;  差异内容：NA | 类名：prompt；  API声明：function showDialog(options: ShowDialogOptions): Promise<ShowDialogSuccessResponse>;  差异内容：9 | api/@ohos.prompt.d.ts |
| API废弃版本变更 | 类名：prompt；  API声明：function showActionMenu(options: ActionMenuOptions, callback: AsyncCallback<ActionMenuSuccessResponse>): void;  差异内容：NA | 类名：prompt；  API声明：function showActionMenu(options: ActionMenuOptions, callback: AsyncCallback<ActionMenuSuccessResponse>): void;  差异内容：9 | api/@ohos.prompt.d.ts |
| API废弃版本变更 | 类名：prompt；  API声明：function showActionMenu(options: ActionMenuOptions): Promise<ActionMenuSuccessResponse>;  差异内容：NA | 类名：prompt；  API声明：function showActionMenu(options: ActionMenuOptions): Promise<ActionMenuSuccessResponse>;  差异内容：9 | api/@ohos.prompt.d.ts |
| API废弃版本变更 | 类名：WindowType；  API声明：TYPE\_SYSTEM\_ALERT  差异内容：NA | 类名：WindowType；  API声明：TYPE\_SYSTEM\_ALERT  差异内容：11 | api/@ohos.window.d.ts |
| API废弃版本变更 | 类名：global；  API声明： export interface ShowToastOptions  差异内容：NA | 类名：global；  API声明： export interface ShowToastOptions  差异内容：8 | api/@system.prompt.d.ts |
| API废弃版本变更 | 类名：ShowToastOptions；  API声明：message: string;  差异内容：NA | 类名：ShowToastOptions；  API声明：message: string;  差异内容：8 | api/@system.prompt.d.ts |
| API废弃版本变更 | 类名：ShowToastOptions；  API声明：duration?: number;  差异内容：NA | 类名：ShowToastOptions；  API声明：duration?: number;  差异内容：8 | api/@system.prompt.d.ts |
| API废弃版本变更 | 类名：ShowToastOptions；  API声明：bottom?: string | number;  差异内容：NA | 类名：ShowToastOptions；  API声明：bottom?: string | number;  差异内容：8 | api/@system.prompt.d.ts |
| API废弃版本变更 | 类名：RouterOptions；  API声明：uri: string;  差异内容：NA | 类名：RouterOptions；  API声明：uri: string;  差异内容：8 | api/@system.router.d.ts |
| API废弃版本变更 | 类名：RouterOptions；  API声明：params?: Object;  差异内容：NA | 类名：RouterOptions；  API声明：params?: Object;  差异内容：8 | api/@system.router.d.ts |
| API废弃版本变更 | 类名：BackRouterOptions；  API声明：uri?: string;  差异内容：NA | 类名：BackRouterOptions；  API声明：uri?: string;  差异内容：8 | api/@system.router.d.ts |
| API废弃版本变更 | 类名：BackRouterOptions；  API声明：params?: Object;  差异内容：NA | 类名：BackRouterOptions；  API声明：params?: Object;  差异内容：8 | api/@system.router.d.ts |
| API废弃版本变更 | 类名：RouterState；  API声明：index: number;  差异内容：NA | 类名：RouterState；  API声明：index: number;  差异内容：8 | api/@system.router.d.ts |
| API废弃版本变更 | 类名：RouterState；  API声明：name: string;  差异内容：NA | 类名：RouterState；  API声明：name: string;  差异内容：8 | api/@system.router.d.ts |
| API废弃版本变更 | 类名：RouterState；  API声明：path: string;  差异内容：NA | 类名：RouterState；  API声明：path: string;  差异内容：8 | api/@system.router.d.ts |
| API废弃版本变更 | 类名：EnableAlertBeforeBackPageOptions；  API声明：message: string;  差异内容：NA | 类名：EnableAlertBeforeBackPageOptions；  API声明：message: string;  差异内容：8 | api/@system.router.d.ts |
| API废弃版本变更 | 类名：EnableAlertBeforeBackPageOptions；  API声明：success?: (errMsg: string) => void;  差异内容：NA | 类名：EnableAlertBeforeBackPageOptions；  API声明：success?: (errMsg: string) => void;  差异内容：8 | api/@system.router.d.ts |
| API废弃版本变更 | 类名：EnableAlertBeforeBackPageOptions；  API声明：cancel?: (errMsg: string) => void;  差异内容：NA | 类名：EnableAlertBeforeBackPageOptions；  API声明：cancel?: (errMsg: string) => void;  差异内容：8 | api/@system.router.d.ts |
| API废弃版本变更 | 类名：EnableAlertBeforeBackPageOptions；  API声明：complete?: () => void;  差异内容：NA | 类名：EnableAlertBeforeBackPageOptions；  API声明：complete?: () => void;  差异内容：8 | api/@system.router.d.ts |
| API废弃版本变更 | 类名：DisableAlertBeforeBackPageOptions；  API声明：success?: (errMsg: string) => void;  差异内容：NA | 类名：DisableAlertBeforeBackPageOptions；  API声明：success?: (errMsg: string) => void;  差异内容：8 | api/@system.router.d.ts |
| API废弃版本变更 | 类名：DisableAlertBeforeBackPageOptions；  API声明：cancel?: (errMsg: string) => void;  差异内容：NA | 类名：DisableAlertBeforeBackPageOptions；  API声明：cancel?: (errMsg: string) => void;  差异内容：8 | api/@system.router.d.ts |
| API废弃版本变更 | 类名：DisableAlertBeforeBackPageOptions；  API声明：complete?: () => void;  差异内容：NA | 类名：DisableAlertBeforeBackPageOptions；  API声明：complete?: () => void;  差异内容：8 | api/@system.router.d.ts |
| API废弃版本变更 | 类名：global；  API声明：type ParamsInterface = {  [key: string]: Object;  };  差异内容：NA | 类名：global；  API声明：type ParamsInterface = {  [key: string]: Object;  };  差异内容：8 | api/@system.router.d.ts |
| API废弃版本变更 | 类名：Router；  API声明：static push(options: RouterOptions): void;  差异内容：NA | 类名：Router；  API声明：static push(options: RouterOptions): void;  差异内容：8 | api/@system.router.d.ts |
| API废弃版本变更 | 类名：Router；  API声明：static replace(options: RouterOptions): void;  差异内容：NA | 类名：Router；  API声明：static replace(options: RouterOptions): void;  差异内容：8 | api/@system.router.d.ts |
| API废弃版本变更 | 类名：Router；  API声明：static back(options?: BackRouterOptions): void;  差异内容：NA | 类名：Router；  API声明：static back(options?: BackRouterOptions): void;  差异内容：8 | api/@system.router.d.ts |
| API废弃版本变更 | 类名：Router；  API声明：static getParams(): ParamsInterface;  差异内容：NA | 类名：Router；  API声明：static getParams(): ParamsInterface;  差异内容：8 | api/@system.router.d.ts |
| API废弃版本变更 | 类名：Router；  API声明：static clear(): void;  差异内容：NA | 类名：Router；  API声明：static clear(): void;  差异内容：8 | api/@system.router.d.ts |
| API废弃版本变更 | 类名：Router；  API声明：static getLength(): string;  差异内容：NA | 类名：Router；  API声明：static getLength(): string;  差异内容：8 | api/@system.router.d.ts |
| API废弃版本变更 | 类名：Router；  API声明：static getState(): RouterState;  差异内容：NA | 类名：Router；  API声明：static getState(): RouterState;  差异内容：8 | api/@system.router.d.ts |
| API废弃版本变更 | 类名：Router；  API声明：static enableAlertBeforeBackPage(options: EnableAlertBeforeBackPageOptions): void;  差异内容：NA | 类名：Router；  API声明：static enableAlertBeforeBackPage(options: EnableAlertBeforeBackPageOptions): void;  差异内容：8 | api/@system.router.d.ts |
| API废弃版本变更 | 类名：Router；  API声明：static disableAlertBeforeBackPage(options?: DisableAlertBeforeBackPageOptions): void;  差异内容：NA | 类名：Router；  API声明：static disableAlertBeforeBackPage(options?: DisableAlertBeforeBackPageOptions): void;  差异内容：8 | api/@system.router.d.ts |
| API废弃版本变更 | 类名：global；  API声明： declare interface TransitionOptions  差异内容：NA | 类名：global；  API声明： declare interface TransitionOptions  差异内容：10 | component/common.d.ts |
| API废弃版本变更 | 类名：TransitionOptions；  API声明：type?: TransitionType;  差异内容：NA | 类名：TransitionOptions；  API声明：type?: TransitionType;  差异内容：10 | component/common.d.ts |
| API废弃版本变更 | 类名：TransitionOptions；  API声明：opacity?: number;  差异内容：NA | 类名：TransitionOptions；  API声明：opacity?: number;  差异内容：10 | component/common.d.ts |
| API废弃版本变更 | 类名：TransitionOptions；  API声明：translate?: TranslateOptions;  差异内容：NA | 类名：TransitionOptions；  API声明：translate?: TranslateOptions;  差异内容：10 | component/common.d.ts |
| API废弃版本变更 | 类名：TransitionOptions；  API声明：scale?: ScaleOptions;  差异内容：NA | 类名：TransitionOptions；  API声明：scale?: ScaleOptions;  差异内容：10 | component/common.d.ts |
| API废弃版本变更 | 类名：TransitionOptions；  API声明：rotate?: RotateOptions;  差异内容：NA | 类名：TransitionOptions；  API声明：rotate?: RotateOptions;  差异内容：10 | component/common.d.ts |
| API废弃版本变更 | 类名：ClickEvent；  API声明：screenX: number;  差异内容：NA | 类名：ClickEvent；  API声明：screenX: number;  差异内容：10 | component/common.d.ts |
| API废弃版本变更 | 类名：ClickEvent；  API声明：screenY: number;  差异内容：NA | 类名：ClickEvent；  API声明：screenY: number;  差异内容：10 | component/common.d.ts |
| API废弃版本变更 | 类名：MouseEvent；  API声明：screenX: number;  差异内容：NA | 类名：MouseEvent；  API声明：screenX: number;  差异内容：10 | component/common.d.ts |
| API废弃版本变更 | 类名：MouseEvent；  API声明：screenY: number;  差异内容：NA | 类名：MouseEvent；  API声明：screenY: number;  差异内容：10 | component/common.d.ts |
| API废弃版本变更 | 类名：TouchObject；  API声明：screenX: number;  差异内容：NA | 类名：TouchObject；  API声明：screenX: number;  差异内容：10 | component/common.d.ts |
| API废弃版本变更 | 类名：TouchObject；  API声明：screenY: number;  差异内容：NA | 类名：TouchObject；  API声明：screenY: number;  差异内容：10 | component/common.d.ts |
| API废弃版本变更 | 类名：DragEvent；  API声明：getX(): number;  差异内容：NA | 类名：DragEvent；  API声明：getX(): number;  差异内容：10 | component/common.d.ts |
| API废弃版本变更 | 类名：DragEvent；  API声明：getY(): number;  差异内容：NA | 类名：DragEvent；  API声明：getY(): number;  差异内容：10 | component/common.d.ts |
| API废弃版本变更 | 类名：PopupOptions；  API声明：placementOnTop?: boolean;  差异内容：NA | 类名：PopupOptions；  API声明：placementOnTop?: boolean;  差异内容：10 | component/common.d.ts |
| API废弃版本变更 | 类名：CustomPopupOptions；  API声明：maskColor?: Color | string | Resource | number;  差异内容：NA | 类名：CustomPopupOptions；  API声明：maskColor?: Color | string | Resource | number;  差异内容：10 | component/common.d.ts |
| API废弃版本变更 | 类名：CommonMethod；  API声明：useSizeType(value: {  xs?: number | { span: number; offset: number };  sm?: number | { span: number; offset: number };  md?: number | { span: number; offset: number };  lg?: number | { span: number; offset: number };  }): T;  差异内容：NA | 类名：CommonMethod；  API声明：useSizeType(value: {  xs?: number | {  span: number;  offset: number;  };  sm?: number | {  span: number;  offset: number;  };  md?: number | {  span: number;  offset: number;  };  lg?: number | {  span: number;  offset: number;  };  }): T;  差异内容：9 | component/common.d.ts |
| API废弃版本变更 | 类名：CommonMethod；  API声明：clip(value: boolean | CircleAttribute | EllipseAttribute | PathAttribute | RectAttribute): T;  差异内容：NA | 类名：CommonMethod；  API声明：clip(value: boolean | CircleAttribute | EllipseAttribute | PathAttribute | RectAttribute): T;  差异内容：12 | component/common.d.ts |
| API废弃版本变更 | 类名：global；  API声明： declare interface LayoutBorderInfo  差异内容：NA | 类名：global；  API声明： declare interface LayoutBorderInfo  差异内容：10 | component/common.d.ts |
| API废弃版本变更 | 类名：LayoutBorderInfo；  API声明：borderWidth: EdgeWidths,  差异内容：NA | 类名：LayoutBorderInfo；  API声明：borderWidth: EdgeWidths;  差异内容：10 | component/common.d.ts |
| API废弃版本变更 | 类名：LayoutBorderInfo；  API声明：margin: Margin,  差异内容：NA | 类名：LayoutBorderInfo；  API声明：margin: Margin;  差异内容：10 | component/common.d.ts |
| API废弃版本变更 | 类名：LayoutBorderInfo；  API声明：padding: Padding,  差异内容：NA | 类名：LayoutBorderInfo；  API声明：padding: Padding;  差异内容：10 | component/common.d.ts |
| API废弃版本变更 | 类名：global；  API声明： declare interface LayoutInfo  差异内容：NA | 类名：global；  API声明： declare interface LayoutInfo  差异内容：10 | component/common.d.ts |
| API废弃版本变更 | 类名：LayoutInfo；  API声明：position: Position,  差异内容：NA | 类名：LayoutInfo；  API声明：position: Position;  差异内容：10 | component/common.d.ts |
| API废弃版本变更 | 类名：LayoutInfo；  API声明：constraint: ConstraintSizeOptions,  差异内容：NA | 类名：LayoutInfo；  API声明：constraint: ConstraintSizeOptions;  差异内容：10 | component/common.d.ts |
| API废弃版本变更 | 类名：global；  API声明： declare interface LayoutChild  差异内容：NA | 类名：global；  API声明： declare interface LayoutChild  差异内容：10 | component/common.d.ts |
| API废弃版本变更 | 类名：LayoutChild；  API声明：name: string,  差异内容：NA | 类名：LayoutChild；  API声明：name: string;  差异内容：10 | component/common.d.ts |
| API废弃版本变更 | 类名：LayoutChild；  API声明：id: string,  差异内容：NA | 类名：LayoutChild；  API声明：id: string;  差异内容：10 | component/common.d.ts |
| API废弃版本变更 | 类名：LayoutChild；  API声明：constraint: ConstraintSizeOptions,  差异内容：NA | 类名：LayoutChild；  API声明：constraint: ConstraintSizeOptions;  差异内容：10 | component/common.d.ts |
| API废弃版本变更 | 类名：LayoutChild；  API声明：borderInfo: LayoutBorderInfo,  差异内容：NA | 类名：LayoutChild；  API声明：borderInfo: LayoutBorderInfo;  差异内容：10 | component/common.d.ts |
| API废弃版本变更 | 类名：LayoutChild；  API声明：position: Position,  差异内容：NA | 类名：LayoutChild；  API声明：position: Position;  差异内容：10 | component/common.d.ts |
| API废弃版本变更 | 类名：LayoutChild；  API声明：measure(childConstraint: ConstraintSizeOptions),  差异内容：NA | 类名：LayoutChild；  API声明：measure(childConstraint: ConstraintSizeOptions);  差异内容：10 | component/common.d.ts |
| API废弃版本变更 | 类名：LayoutChild；  API声明：layout(childLayoutInfo: LayoutInfo)  差异内容：NA | 类名：LayoutChild；  API声明：layout(childLayoutInfo: LayoutInfo);  差异内容：10 | component/common.d.ts |
| API废弃版本变更 | 类名：CustomComponent；  API声明：onLayout?(children: Array<LayoutChild>, constraint: ConstraintSizeOptions): void;  差异内容：NA | 类名：CustomComponent；  API声明：onLayout?(children: Array<LayoutChild>, constraint: ConstraintSizeOptions): void;  差异内容：10 | component/common.d.ts |
| API废弃版本变更 | 类名：CustomComponent；  API声明：onMeasure?(children: Array<LayoutChild>, constraint: ConstraintSizeOptions): void;  差异内容：NA | 类名：CustomComponent；  API声明：onMeasure?(children: Array<LayoutChild>, constraint: ConstraintSizeOptions): void;  差异内容：10 | component/common.d.ts |
| API废弃版本变更 | 类名：AppStorage；  API声明：static Link(propName: string): any;  差异内容：NA | 类名：AppStorage；  API声明：static Link(propName: string): any;  差异内容：10 | component/common\_ts\_ets\_api.d.ts |
| API废弃版本变更 | 类名：AppStorage；  API声明：static SetAndLink<T>(propName: string, defaultValue: T): SubscribedAbstractProperty<T>;  差异内容：NA | 类名：AppStorage；  API声明：static SetAndLink<T>(propName: string, defaultValue: T): SubscribedAbstractProperty<T>;  差异内容：10 | component/common\_ts\_ets\_api.d.ts |
| API废弃版本变更 | 类名：AppStorage；  API声明：static Prop(propName: string): any;  差异内容：NA | 类名：AppStorage；  API声明：static Prop(propName: string): any;  差异内容：10 | component/common\_ts\_ets\_api.d.ts |
| API废弃版本变更 | 类名：AppStorage；  API声明：static SetAndProp<S>(propName: string, defaultValue: S): SubscribedAbstractProperty<S>;  差异内容：NA | 类名：AppStorage；  API声明：static SetAndProp<S>(propName: string, defaultValue: S): SubscribedAbstractProperty<S>;  差异内容：10 | component/common\_ts\_ets\_api.d.ts |
| API废弃版本变更 | 类名：AppStorage；  API声明：static Has(propName: string): boolean;  差异内容：NA | 类名：AppStorage；  API声明：static Has(propName: string): boolean;  差异内容：10 | component/common\_ts\_ets\_api.d.ts |
| API废弃版本变更 | 类名：AppStorage；  API声明：static Get<T>(propName: string): T | undefined;  差异内容：NA | 类名：AppStorage；  API声明：static Get<T>(propName: string): T | undefined;  差异内容：10 | component/common\_ts\_ets\_api.d.ts |
| API废弃版本变更 | 类名：AppStorage；  API声明：static Set<T>(propName: string, newValue: T): boolean;  差异内容：NA | 类名：AppStorage；  API声明：static Set<T>(propName: string, newValue: T): boolean;  差异内容：10 | component/common\_ts\_ets\_api.d.ts |
| API废弃版本变更 | 类名：AppStorage；  API声明：static SetOrCreate<T>(propName: string, newValue: T): void;  差异内容：NA | 类名：AppStorage；  API声明：static SetOrCreate<T>(propName: string, newValue: T): void;  差异内容：10 | component/common\_ts\_ets\_api.d.ts |
| API废弃版本变更 | 类名：AppStorage；  API声明：static Delete(propName: string): boolean;  差异内容：NA | 类名：AppStorage；  API声明：static Delete(propName: string): boolean;  差异内容：10 | component/common\_ts\_ets\_api.d.ts |
| API废弃版本变更 | 类名：AppStorage；  API声明：static Keys(): IterableIterator<string>;  差异内容：NA | 类名：AppStorage；  API声明：static Keys(): IterableIterator<string>;  差异内容：10 | component/common\_ts\_ets\_api.d.ts |
| API废弃版本变更 | 类名：AppStorage；  API声明：static Clear(): boolean;  差异内容：NA | 类名：AppStorage；  API声明：static Clear(): boolean;  差异内容：10 | component/common\_ts\_ets\_api.d.ts |
| API废弃版本变更 | 类名：AppStorage；  API声明：static IsMutable(propName: string): boolean;  差异内容：NA | 类名：AppStorage；  API声明：static IsMutable(propName: string): boolean;  差异内容：10 | component/common\_ts\_ets\_api.d.ts |
| API废弃版本变更 | 类名：AppStorage；  API声明：static Size(): number;  差异内容：NA | 类名：AppStorage；  API声明：static Size(): number;  差异内容：10 | component/common\_ts\_ets\_api.d.ts |
| API废弃版本变更 | 类名：Environment；  API声明：static EnvProp<S>(key: string, value: S): boolean;  差异内容：NA | 类名：Environment；  API声明：static EnvProp<S>(key: string, value: S): boolean;  差异内容：10 | component/common\_ts\_ets\_api.d.ts |
| API废弃版本变更 | 类名：Environment；  API声明：static EnvProps(props: {  key: string;  defaultValue: any;  }[]): void;  差异内容：NA | 类名：Environment；  API声明：static EnvProps(props: {  key: string;  defaultValue: any;  }[]): void;  差异内容：10 | component/common\_ts\_ets\_api.d.ts |
| API废弃版本变更 | 类名：Environment；  API声明：static Keys(): Array<string>;  差异内容：NA | 类名：Environment；  API声明：static Keys(): Array<string>;  差异内容：10 | component/common\_ts\_ets\_api.d.ts |
| API废弃版本变更 | 类名：PersistentStorage；  API声明：static PersistProp<T>(key: string, defaultValue: T): void;  差异内容：NA | 类名：PersistentStorage；  API声明：static PersistProp<T>(key: string, defaultValue: T): void;  差异内容：10 | component/common\_ts\_ets\_api.d.ts |
| API废弃版本变更 | 类名：PersistentStorage；  API声明：static DeleteProp(key: string): void;  差异内容：NA | 类名：PersistentStorage；  API声明：static DeleteProp(key: string): void;  差异内容：10 | component/common\_ts\_ets\_api.d.ts |
| API废弃版本变更 | 类名：PersistentStorage；  API声明：static PersistProps(properties: {  key: string;  defaultValue: any;  }[]): void;  差异内容：NA | 类名：PersistentStorage；  API声明：static PersistProps(properties: {  key: string;  defaultValue: any;  }[]): void;  差异内容：10 | component/common\_ts\_ets\_api.d.ts |
| API废弃版本变更 | 类名：PersistentStorage；  API声明：static Keys(): Array<string>;  差异内容：NA | 类名：PersistentStorage；  API声明：static Keys(): Array<string>;  差异内容：10 | component/common\_ts\_ets\_api.d.ts |
| API废弃版本变更 | 类名：LocalStorage；  API声明：static GetShared(): LocalStorage;  差异内容：NA | 类名：LocalStorage；  API声明：static GetShared(): LocalStorage;  差异内容：10 | component/common\_ts\_ets\_api.d.ts |
| API废弃版本变更 | 类名：DatePickerAttribute；  API声明：onChange(callback: (value: DatePickerResult) => void): DatePickerAttribute;  差异内容：NA | 类名：DatePickerAttribute；  API声明：onChange(callback: (value: DatePickerResult) => void): DatePickerAttribute;  差异内容：10 | component/date\_picker.d.ts |
| API废弃版本变更 | 类名：DatePickerDialogOptions；  API声明：onAccept?: (value: DatePickerResult) => void;  差异内容：NA | 类名：DatePickerDialogOptions；  API声明：onAccept?: (value: DatePickerResult) => void;  差异内容：10 | component/date\_picker.d.ts |
| API废弃版本变更 | 类名：DatePickerDialogOptions；  API声明：onChange?: (value: DatePickerResult) => void;  差异内容：NA | 类名：DatePickerDialogOptions；  API声明：onChange?: (value: DatePickerResult) => void;  差异内容：10 | component/date\_picker.d.ts |
| API废弃版本变更 | 类名：global；  API声明： declare enum SizeType  差异内容：NA | 类名：global；  API声明： declare enum SizeType  差异内容：9 | component/grid\_container.d.ts |
| API废弃版本变更 | 类名：SizeType；  API声明：Auto  差异内容：NA | 类名：SizeType；  API声明：Auto  差异内容：9 | component/grid\_container.d.ts |
| API废弃版本变更 | 类名：SizeType；  API声明：XS  差异内容：NA | 类名：SizeType；  API声明：XS  差异内容：9 | component/grid\_container.d.ts |
| API废弃版本变更 | 类名：SizeType；  API声明：SM  差异内容：NA | 类名：SizeType；  API声明：SM  差异内容：9 | component/grid\_container.d.ts |
| API废弃版本变更 | 类名：SizeType；  API声明：MD  差异内容：NA | 类名：SizeType；  API声明：MD  差异内容：9 | component/grid\_container.d.ts |
| API废弃版本变更 | 类名：SizeType；  API声明：LG  差异内容：NA | 类名：SizeType；  API声明：LG  差异内容：9 | component/grid\_container.d.ts |
| API废弃版本变更 | 类名：global；  API声明： declare interface GridContainerOptions  差异内容：NA | 类名：global；  API声明： declare interface GridContainerOptions  差异内容：9 | component/grid\_container.d.ts |
| API废弃版本变更 | 类名：GridContainerOptions；  API声明：columns?: number | "auto";  差异内容：NA | 类名：GridContainerOptions；  API声明：columns?: number | "auto";  差异内容：9 | component/grid\_container.d.ts |
| API废弃版本变更 | 类名：GridContainerOptions；  API声明：sizeType?: SizeType;  差异内容：NA | 类名：GridContainerOptions；  API声明：sizeType?: SizeType;  差异内容：9 | component/grid\_container.d.ts |
| API废弃版本变更 | 类名：GridContainerOptions；  API声明：gutter?: number | string;  差异内容：NA | 类名：GridContainerOptions；  API声明：gutter?: number | string;  差异内容：9 | component/grid\_container.d.ts |
| API废弃版本变更 | 类名：GridContainerOptions；  API声明：margin?: number | string;  差异内容：NA | 类名：GridContainerOptions；  API声明：margin?: number | string;  差异内容：9 | component/grid\_container.d.ts |
| API废弃版本变更 | 类名：global；  API声明： interface GridContainerInterface  差异内容：NA | 类名：global；  API声明： interface GridContainerInterface  差异内容：9 | component/grid\_container.d.ts |
| API废弃版本变更 | 类名：global；  API声明： declare class GridContainerAttribute  差异内容：NA | 类名：global；  API声明： declare class GridContainerAttribute  差异内容：9 | component/grid\_container.d.ts |
| API废弃版本变更 | 类名：ListAttribute；  API声明：onScroll(event: (scrollOffset: number, scrollState: ScrollState) => void): ListAttribute;  差异内容：NA | 类名：ListAttribute；  API声明：onScroll(event: (scrollOffset: number, scrollState: ScrollState) => void): ListAttribute;  差异内容：12 | component/list.d.ts |
| API废弃版本变更 | 类名：global；  API声明： declare enum Sticky  差异内容：NA | 类名：global；  API声明： declare enum Sticky  差异内容：9 | component/list\_item.d.ts |
| API废弃版本变更 | 类名：Sticky；  API声明：None  差异内容：NA | 类名：Sticky；  API声明：None  差异内容：9 | component/list\_item.d.ts |
| API废弃版本变更 | 类名：Sticky；  API声明：Normal  差异内容：NA | 类名：Sticky；  API声明：Normal  差异内容：9 | component/list\_item.d.ts |
| API废弃版本变更 | 类名：Sticky；  API声明：Opacity  差异内容：NA | 类名：Sticky；  API声明：Opacity  差异内容：9 | component/list\_item.d.ts |
| API废弃版本变更 | 类名：EditMode；  API声明：None  差异内容：NA | 类名：EditMode；  API声明：None  差异内容：9 | component/list\_item.d.ts |
| API废弃版本变更 | 类名：EditMode；  API声明：Deletable  差异内容：NA | 类名：EditMode；  API声明：Deletable  差异内容：9 | component/list\_item.d.ts |
| API废弃版本变更 | 类名：EditMode；  API声明：Movable  差异内容：NA | 类名：EditMode；  API声明：Movable  差异内容：9 | component/list\_item.d.ts |
| API废弃版本变更 | 类名：ListItemAttribute；  API声明：sticky(value: Sticky): ListItemAttribute;  差异内容：NA | 类名：ListItemAttribute；  API声明：sticky(value: Sticky): ListItemAttribute;  差异内容：9 | component/list\_item.d.ts |
| API废弃版本变更 | 类名：MenuAttribute；  API声明：fontSize(value: Length): MenuAttribute;  差异内容：NA | 类名：MenuAttribute；  API声明：fontSize(value: Length): MenuAttribute;  差异内容：10 | component/menu.d.ts |
| API废弃版本变更 | 类名：NavigationAttribute；  API声明：toolBar(value: object | CustomBuilder): NavigationAttribute;  差异内容：NA | 类名：NavigationAttribute；  API声明：toolBar(value: object | CustomBuilder): NavigationAttribute;  差异内容：10 | component/navigation.d.ts |
| API废弃版本变更 | 类名：global；  API声明： declare enum PanelMode  差异内容：NA | 类名：global；  API声明： declare enum PanelMode  差异内容：12 | component/panel.d.ts |
| API废弃版本变更 | 类名：PanelMode；  API声明：Mini  差异内容：NA | 类名：PanelMode；  API声明：Mini  差异内容：12 | component/panel.d.ts |
| API废弃版本变更 | 类名：PanelMode；  API声明：Half  差异内容：NA | 类名：PanelMode；  API声明：Half  差异内容：12 | component/panel.d.ts |
| API废弃版本变更 | 类名：PanelMode；  API声明：Full  差异内容：NA | 类名：PanelMode；  API声明：Full  差异内容：12 | component/panel.d.ts |
| API废弃版本变更 | 类名：global；  API声明： declare enum PanelType  差异内容：NA | 类名：global；  API声明： declare enum PanelType  差异内容：12 | component/panel.d.ts |
| API废弃版本变更 | 类名：PanelType；  API声明：Minibar  差异内容：NA | 类名：PanelType；  API声明：Minibar = 0  差异内容：12 | component/panel.d.ts |
| API废弃版本变更 | 类名：PanelType；  API声明：Foldable  差异内容：NA | 类名：PanelType；  API声明：Foldable = 1  差异内容：12 | component/panel.d.ts |
| API废弃版本变更 | 类名：PanelType；  API声明：Temporary  差异内容：NA | 类名：PanelType；  API声明：Temporary = 2  差异内容：12 | component/panel.d.ts |
| API废弃版本变更 | 类名：global；  API声明： interface PanelInterface  差异内容：NA | 类名：global；  API声明： interface PanelInterface  差异内容：12 | component/panel.d.ts |
| API废弃版本变更 | 类名：global；  API声明： declare class PanelAttribute  差异内容：NA | 类名：global；  API声明： declare class PanelAttribute  差异内容：12 | component/panel.d.ts |
| API废弃版本变更 | 类名：PanelAttribute；  API声明：mode(value: PanelMode): PanelAttribute;  差异内容：NA | 类名：PanelAttribute；  API声明：mode(value: PanelMode): PanelAttribute;  差异内容：12 | component/panel.d.ts |
| API废弃版本变更 | 类名：PanelAttribute；  API声明：type(value: PanelType): PanelAttribute;  差异内容：NA | 类名：PanelAttribute；  API声明：type(value: PanelType): PanelAttribute;  差异内容：12 | component/panel.d.ts |
| API废弃版本变更 | 类名：PanelAttribute；  API声明：dragBar(value: boolean): PanelAttribute;  差异内容：NA | 类名：PanelAttribute；  API声明：dragBar(value: boolean): PanelAttribute;  差异内容：12 | component/panel.d.ts |
| API废弃版本变更 | 类名：PanelAttribute；  API声明：fullHeight(value: number | string): PanelAttribute;  差异内容：NA | 类名：PanelAttribute；  API声明：fullHeight(value: number | string): PanelAttribute;  差异内容：12 | component/panel.d.ts |
| API废弃版本变更 | 类名：PanelAttribute；  API声明：halfHeight(value: number | string): PanelAttribute;  差异内容：NA | 类名：PanelAttribute；  API声明：halfHeight(value: number | string): PanelAttribute;  差异内容：12 | component/panel.d.ts |
| API废弃版本变更 | 类名：PanelAttribute；  API声明：miniHeight(value: number | string): PanelAttribute;  差异内容：NA | 类名：PanelAttribute；  API声明：miniHeight(value: number | string): PanelAttribute;  差异内容：12 | component/panel.d.ts |
| API废弃版本变更 | 类名：PanelAttribute；  API声明：show(value: boolean): PanelAttribute;  差异内容：NA | 类名：PanelAttribute；  API声明：show(value: boolean): PanelAttribute;  差异内容：12 | component/panel.d.ts |
| API废弃版本变更 | 类名：PanelAttribute；  API声明：backgroundMask(color: ResourceColor): PanelAttribute;  差异内容：NA | 类名：PanelAttribute；  API声明：backgroundMask(color: ResourceColor): PanelAttribute;  差异内容：12 | component/panel.d.ts |
| API废弃版本变更 | 类名：PanelAttribute；  API声明：onChange(event: (  /  **\* Width of content area.**  **\* @since 7**  **\*/**  **width: number,**  **/\*\***  **\* Height of content area.**  **\* @since 7**  **\*/**  **height: number,**  **/**    \* Initial state.  \* @since 7  \*/  mode: PanelMode) => void): PanelAttribute;  差异内容：NA | 类名：PanelAttribute；  API声明：onChange(event: (  /\*\*  \* Width of content area.  \*  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @since 7  \*/  /\*\*  \* Width of content area.  \*  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @atomicservice  \* @since 11  \* @deprecated since 12  \*/  width: number,  /\*\*  \* Height of content area.  \*  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @since 7  \*/  /\*\*  \* Height of content area.  \*  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @atomicservice  \* @since 11  \* @deprecated since 12  \*/  height: number,  /\*\*  \* Initial state.  \*  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @since 7  \*/  /\*\*  \* Initial state.  \*  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @atomicservice  \* @since 11  \* @deprecated since 12  \*/  mode: PanelMode) => void): PanelAttribute;  差异内容：12 | component/panel.d.ts |
| API废弃版本变更 | 类名：PanelAttribute；  API声明：onHeightChange(callback: (value: number) => void): PanelAttribute;  差异内容：NA | 类名：PanelAttribute；  API声明：onHeightChange(callback: (value: number) => void): PanelAttribute;  差异内容：12 | component/panel.d.ts |
| API废弃版本变更 | 类名：global；  API声明：declare const Panel: PanelInterface;  差异内容：NA | 类名：global；  API声明：declare const Panel: PanelInterface;  差异内容：12 | component/panel.d.ts |
| API废弃版本变更 | 类名：global；  API声明：declare const PanelInstance: PanelAttribute;  差异内容：NA | 类名：global；  API声明：declare const PanelInstance: PanelAttribute;  差异内容：12 | component/panel.d.ts |
| API废弃版本变更 | 类名：Scroller；  API声明：scrollPage(value: {  next: boolean;  });  差异内容：NA | 类名：Scroller；  API声明：scrollPage(value: {  next: boolean;  direction?: Axis;  });  差异内容：9 | component/scroll.d.ts |
| API废弃版本变更 | 类名：ScrollAttribute；  API声明：onScroll(event: (xOffset: number, yOffset: number) => void): ScrollAttribute;  差异内容：NA | 类名：ScrollAttribute；  API声明：onScroll(event: (xOffset: number, yOffset: number) => void): ScrollAttribute;  差异内容：12 | component/scroll.d.ts |
| API废弃版本变更 | 类名：SwiperDisplayMode；  API声明：Stretch  差异内容：NA | 类名：SwiperDisplayMode；  API声明：Stretch  差异内容：10 | component/swiper.d.ts |
| API废弃版本变更 | 类名：SwiperDisplayMode；  API声明：AutoLinear  差异内容：NA | 类名：SwiperDisplayMode；  API声明：AutoLinear  差异内容：10 | component/swiper.d.ts |
| API废弃版本变更 | 类名：global；  API声明： declare interface IndicatorStyle  差异内容：NA | 类名：global；  API声明： declare interface IndicatorStyle  差异内容：10 | component/swiper.d.ts |
| API废弃版本变更 | 类名：IndicatorStyle；  API声明：left?: Length;  差异内容：NA | 类名：IndicatorStyle；  API声明：left?: Length;  差异内容：10 | component/swiper.d.ts |
| API废弃版本变更 | 类名：IndicatorStyle；  API声明：top?: Length;  差异内容：NA | 类名：IndicatorStyle；  API声明：top?: Length;  差异内容：10 | component/swiper.d.ts |
| API废弃版本变更 | 类名：IndicatorStyle；  API声明：right?: Length;  差异内容：NA | 类名：IndicatorStyle；  API声明：right?: Length;  差异内容：10 | component/swiper.d.ts |
| API废弃版本变更 | 类名：IndicatorStyle；  API声明：bottom?: Length;  差异内容：NA | 类名：IndicatorStyle；  API声明：bottom?: Length;  差异内容：10 | component/swiper.d.ts |
| API废弃版本变更 | 类名：IndicatorStyle；  API声明：size?: Length;  差异内容：NA | 类名：IndicatorStyle；  API声明：size?: Length;  差异内容：10 | component/swiper.d.ts |
| API废弃版本变更 | 类名：IndicatorStyle；  API声明：mask?: boolean;  差异内容：NA | 类名：IndicatorStyle；  API声明：mask?: boolean;  差异内容：10 | component/swiper.d.ts |
| API废弃版本变更 | 类名：IndicatorStyle；  API声明：color?: ResourceColor;  差异内容：NA | 类名：IndicatorStyle；  API声明：color?: ResourceColor;  差异内容：10 | component/swiper.d.ts |
| API废弃版本变更 | 类名：IndicatorStyle；  API声明：selectedColor?: ResourceColor;  差异内容：NA | 类名：IndicatorStyle；  API声明：selectedColor?: ResourceColor;  差异内容：10 | component/swiper.d.ts |
| API废弃版本变更 | 类名：SwiperAttribute；  API声明：indicatorStyle(value?: IndicatorStyle): SwiperAttribute;  差异内容：NA | 类名：SwiperAttribute；  API声明：indicatorStyle(value?: IndicatorStyle): SwiperAttribute;  差异内容：10 | component/swiper.d.ts |
| API废弃版本变更 | 类名：TextPickerAttribute；  API声明：onAccept(callback: (value: string, index: number) => void): TextPickerAttribute;  差异内容：NA | 类名：TextPickerAttribute；  API声明：onAccept(callback: (value: string, index: number) => void): TextPickerAttribute;  差异内容：10 | component/text\_picker.d.ts |
| API废弃版本变更 | 类名：TextPickerAttribute；  API声明：onCancel(callback: () => void): TextPickerAttribute;  差异内容：NA | 类名：TextPickerAttribute；  API声明：onCancel(callback: () => void): TextPickerAttribute;  差异内容：10 | component/text\_picker.d.ts |
| API废弃版本变更 | 类名：XComponentController；  API声明：setXComponentSurfaceSize(value: {  surfaceWidth: number;  surfaceHeight: number;  }): void;  差异内容：NA | 类名：XComponentController；  API声明：setXComponentSurfaceSize(value: {  surfaceWidth: number;  surfaceHeight: number;  }): void;  差异内容：12 | component/xcomponent.d.ts |
| API废弃版本变更 | 类名：Scroller；  API声明：scrollPage(value: {  next: boolean;  direction?: Axis;  });  差异内容：9 | 类名：Scroller；  API声明：scrollPage(value: {  next: boolean;  });  差异内容：NA | component/scroll.d.ts |
| 错误码变更 | 类名：window；  API声明：function findWindow(name: string): Window;  差异内容：401 | 类名：window；  API声明：function findWindow(name: string): Window;  差异内容：1300002,401 | api/@ohos.window.d.ts |
| 错误码变更 | 类名：window；  API声明：function createWindow(config: Configuration, callback: AsyncCallback<Window>): void;  差异内容：1300001,1300006,201,401 | 类名：window；  API声明：function createWindow(config: Configuration, callback: AsyncCallback<Window>): void;  差异内容：1300001,1300006,1300008,1300009,201,401 | api/@ohos.window.d.ts |
| 错误码变更 | 类名：window；  API声明：function createWindow(config: Configuration): Promise<Window>;  差异内容：1300001,1300006,201,401 | 类名：window；  API声明：function createWindow(config: Configuration): Promise<Window>;  差异内容：1300001,1300006,1300008,1300009,201,401 | api/@ohos.window.d.ts |
| 函数变更 | 类名：CustomComponent；  API声明：onBackPress?(): void;  差异内容：NA | 类名：CustomComponent；  API声明：onBackPress?(): void | boolean;  差异内容：void,boolean | component/common.d.ts |
| 函数变更 | 类名：Scroller；  API声明：currentOffset();  差异内容：NA | 类名：Scroller；  API声明：currentOffset(): OffsetResult;  差异内容：OffsetResult | component/scroll.d.ts |
| 函数变更 | 类名：ProgressAttribute；  API声明：value(value: number): ProgressAttribute;  差异内容：ProgressAttribute | 类名：ProgressAttribute；  API声明：value(value: number): ProgressAttribute<Type>;  差异内容：ProgressAttribute<Type> | component/progress.d.ts |
| 函数变更 | 类名：ProgressAttribute；  API声明：color(value: ResourceColor): ProgressAttribute;  差异内容：ProgressAttribute | 类名：ProgressAttribute；  API声明：color(value: ResourceColor | LinearGradient): ProgressAttribute<Type>;  差异内容：ProgressAttribute<Type> | component/progress.d.ts |
| 函数变更 | 类名：ProgressAttribute；  API声明：style(value: ProgressStyleOptions): ProgressAttribute;  差异内容：ProgressAttribute | 类名：ProgressAttribute；  API声明：style(value: Style): ProgressAttribute<Type>;  差异内容：ProgressAttribute<Type> | component/progress.d.ts |
| 函数变更 | 类名：AlphabetIndexerAttribute；  API声明：alignStyle(value: IndexerAlign): AlphabetIndexerAttribute;  差异内容：NA | 类名：AlphabetIndexerAttribute；  API声明：alignStyle(value: IndexerAlign, offset?: Length): AlphabetIndexerAttribute;  差异内容：offset?: Length | component/alphabet\_indexer.d.ts |
| 函数变更 | 类名：CommonMethod；  API声明：backgroundBlurStyle(value: BlurStyle): T;  差异内容：NA | 类名：CommonMethod；  API声明：backgroundBlurStyle(value: BlurStyle, options?: BackgroundBlurStyleOptions): T;  差异内容：options?: BackgroundBlurStyleOptions | component/common.d.ts |
| 函数变更 | 类名：CommonMethod；  API声明：blur(value: number): T;  差异内容：NA | 类名：CommonMethod；  API声明：blur(value: number, options?: BlurOptions): T;  差异内容：options?: BlurOptions | component/common.d.ts |
| 函数变更 | 类名：CommonMethod；  API声明：backdropBlur(value: number): T;  差异内容：NA | 类名：CommonMethod；  API声明：backdropBlur(value: number, options?: BlurOptions): T;  差异内容：options?: BlurOptions | component/common.d.ts |
| 函数变更 | 类名：ListAttribute；  API声明：lanes(value: number | LengthConstrain): ListAttribute;  差异内容：NA | 类名：ListAttribute；  API声明：lanes(value: number | LengthConstrain, gutter?: Dimension): ListAttribute;  差异内容：gutter?: Dimension | component/list.d.ts |
| 函数变更 | 类名：ListAttribute；  API声明：edgeEffect(value: EdgeEffect): ListAttribute;  差异内容：NA | 类名：ListAttribute；  API声明：edgeEffect(value: EdgeEffect, options?: EdgeEffectOptions): ListAttribute;  差异内容：options?: EdgeEffectOptions | component/list.d.ts |
| 函数变更 | 类名：NavigationAttribute；  API声明：title(value: string | CustomBuilder | NavigationCommonTitle | NavigationCustomTitle): NavigationAttribute;  差异内容：NA | 类名：NavigationAttribute；  API声明：title(value: ResourceStr | CustomBuilder | NavigationCommonTitle | NavigationCustomTitle, options?: NavigationTitleOptions): NavigationAttribute;  差异内容：options?: NavigationTitleOptions | component/navigation.d.ts |
| 函数变更 | 类名：NavDestinationAttribute；  API声明：title(value: string | CustomBuilder | NavDestinationCommonTitle | NavDestinationCustomTitle): NavDestinationAttribute;  差异内容：NA | 类名：NavDestinationAttribute；  API声明：title(value: string | CustomBuilder | NavDestinationCommonTitle | NavDestinationCustomTitle, options?: NavigationTitleOptions): NavDestinationAttribute;  差异内容：options?: NavigationTitleOptions | component/nav\_destination.d.ts |
| 函数变更 | 类名：Scroller；  API声明：scrollEdge(value: Edge);  差异内容：NA | 类名：Scroller；  API声明：scrollEdge(value: Edge, options?: ScrollEdgeOptions);  差异内容：options?: ScrollEdgeOptions | component/scroll.d.ts |
| 函数变更 | 类名：Scroller；  API声明：scrollToIndex(value: number);  差异内容：NA | 类名：Scroller；  API声明：scrollToIndex(value: number, smooth?: boolean, align?: ScrollAlign, options?: ScrollToIndexOptions);  差异内容：smooth?: boolean, align?: ScrollAlign, options?: ScrollToIndexOptions | component/scroll.d.ts |
| 函数变更 | 类名：ScrollAttribute；  API声明：edgeEffect(edgeEffect: EdgeEffect): ScrollAttribute;  差异内容：NA | 类名：ScrollAttribute；  API声明：edgeEffect(edgeEffect: EdgeEffect, options?: EdgeEffectOptions): ScrollAttribute;  差异内容：options?: EdgeEffectOptions | component/scroll.d.ts |
| 函数变更 | 类名：SearchAttribute；  API声明：searchButton(value: string): SearchAttribute;  差异内容：NA | 类名：SearchAttribute；  API声明：searchButton(value: string, option?: SearchButtonOptions): SearchAttribute;  差异内容：option?: SearchButtonOptions | component/search.d.ts |
| 函数变更 | 类名：SliderAttribute；  API声明：showTips(value: boolean): SliderAttribute;  差异内容：NA | 类名：SliderAttribute；  API声明：showTips(value: boolean, content?: ResourceStr): SliderAttribute;  差异内容：content?: ResourceStr | component/slider.d.ts |
| 函数变更 | 类名：SwiperAttribute；  API声明：displayCount(value: number | string): SwiperAttribute;  差异内容：NA | 类名：SwiperAttribute；  API声明：displayCount(value: number | string | SwiperAutoFill, swipeByGroup?: boolean): SwiperAttribute;  差异内容：swipeByGroup?: boolean | component/swiper.d.ts |
| 函数变更 | 类名：Window；  API声明：on(type: 'avoidAreaChange', callback: Callback<{  type: AvoidAreaType;  area: AvoidArea;  }>): void;  差异内容：callback: Callback<{  type: AvoidAreaType;  area: AvoidArea;  }> | 类名：Window；  API声明：on(type: 'avoidAreaChange', callback: Callback<AvoidAreaOptions>): void;  差异内容：callback: Callback<AvoidAreaOptions> | api/@ohos.window.d.ts |
| 函数变更 | 类名：Window；  API声明：off(type: 'avoidAreaChange', callback?: Callback<{  type: AvoidAreaType;  area: AvoidArea;  }>): void;  差异内容：callback?: Callback<{  type: AvoidAreaType;  area: AvoidArea;  }> | 类名：Window；  API声明：off(type: 'avoidAreaChange', callback?: Callback<AvoidAreaOptions>): void;  差异内容：callback?: Callback<AvoidAreaOptions> | api/@ohos.window.d.ts |
| 函数变更 | 类名：ActionSheet；  API声明：static show(value: {  /  **\* Title Properties**  **\* @since 8**  **\*/**  **title: string | Resource;**  **/\*\***  **\* message Properties**  **\* @since 8**  **\*/**  **message: string | Resource;**  **/**    \* Invoke the commit function.  \* @since 8  \*/  confirm?: {  /  **\* Text content of the confirmation button.**  **\* @since 8**  **\*/**  **value: string | Resource;**  **/\*\***  **\* Method executed by the callback.**  **\* @since 8**  **\*/**  **action: () => void;**  **};**  **/**    \* Execute Cancel Function.  \* @since 8  \*/  cancel?: () => void;  /  **\* The Array of sheets**  **\* @since 8**  **\*/**  **sheets: Array<SheetInfo>;**  **/\*\***  **\* Allows users to click the mask layer to exit.**  **\* @since 8**  **\*/**  **autoCancel?: boolean;**  **/**    \* Alignment in the vertical direction.  \* @since 8  \*/  alignment?: DialogAlignment;  /  **\* Offset of the pop-up window relative to the alignment position.**  **\* @since 8**  **\*/**  **offset?: {**  **dx: number | string | Resource;**  **dy: number | string | Resource;**  **};**  **});**  **差异内容：value: {**  **/\*\***  **\* Title Properties**  **\* @since 8**  **\*/**  **title: string | Resource;**  **/**    \* message Properties  \* @since 8  \*/  message: string | Resource;  /  **\* Invoke the commit function.**  **\* @since 8**  **\*/**  **confirm?: {**  **/\*\***  **\* Text content of the confirmation button.**  **\* @since 8**  **\*/**  **value: string | Resource;**  **/**    \* Method executed by the callback.  \* @since 8  \*/  action: () => void;  };  /  **\* Execute Cancel Function.**  **\* @since 8**  **\*/**  **cancel?: () => void;**  **/\*\***  **\* The Array of sheets**  **\* @since 8**  **\*/**  **sheets: Array<SheetInfo>;**  **/**    \* Allows users to click the mask layer to exit.  \* @since 8  \*/  autoCancel?: boolean;  /\*\*  \* Alignment in the vertical direction.  \* @since 8  \*/  alignment?: DialogAlignment;  /\*\*  \* Offset of the pop-up window relative to the alignment position.  \* @since 8  \*/  offset?: {  dx: number | string | Resource;  dy: number | string | Resource;  };  } | 类名：ActionSheet；  API声明：static show(value: ActionSheetOptions);  差异内容：value: ActionSheetOptions | component/action\_sheet.d.ts |
| 函数变更 | 类名：CommonMethod；  API声明：onClick(event: (event?: ClickEvent) => void): T;  差异内容：event: (event?: ClickEvent) => void | 类名：CommonMethod；  API声明：onClick(event: (event: ClickEvent) => void): T;  差异内容：event: (event: ClickEvent) => void | component/common.d.ts |
| 函数变更 | 类名：CommonMethod；  API声明：onHover(event: (isHover?: boolean) => void): T;  差异内容：event: (isHover?: boolean) => void | 类名：CommonMethod；  API声明：onHover(event: (isHover: boolean, event: HoverEvent) => void): T;  差异内容：event: (isHover: boolean, event: HoverEvent) => void | component/common.d.ts |
| 函数变更 | 类名：CommonMethod；  API声明：onMouse(event: (event?: MouseEvent) => void): T;  差异内容：event: (event?: MouseEvent) => void | 类名：CommonMethod；  API声明：onMouse(event: (event: MouseEvent) => void): T;  差异内容：event: (event: MouseEvent) => void | component/common.d.ts |
| 函数变更 | 类名：CommonMethod；  API声明：onTouch(event: (event?: TouchEvent) => void): T;  差异内容：event: (event?: TouchEvent) => void | 类名：CommonMethod；  API声明：onTouch(event: (event: TouchEvent) => void): T;  差异内容：event: (event: TouchEvent) => void | component/common.d.ts |
| 函数变更 | 类名：CommonMethod；  API声明：onKeyEvent(event: (event?: KeyEvent) => void): T;  差异内容：event: (event?: KeyEvent) => void | 类名：CommonMethod；  API声明：onKeyEvent(event: (event: KeyEvent) => void): T;  差异内容：event: (event: KeyEvent) => void | component/common.d.ts |
| 函数变更 | 类名：CommonMethod；  API声明：useSizeType(value: {  xs?: number | { span: number; offset: number };  sm?: number | { span: number; offset: number };  md?: number | { span: number; offset: number };  lg?: number | { span: number; offset: number };  }): T;  差异内容：value: {  xs?: number | { span: number; offset: number };  sm?: number | { span: number; offset: number };  md?: number | { span: number; offset: number };  lg?: number | { span: number; offset: number };  } | 类名：CommonMethod；  API声明：useSizeType(value: {  xs?: number | {  span: number;  offset: number;  };  sm?: number | {  span: number;  offset: number;  };  md?: number | {  span: number;  offset: number;  };  lg?: number | {  span: number;  offset: number;  };  }): T;  差异内容：value: {  xs?: number | {  span: number;  offset: number;  };  sm?: number | {  span: number;  offset: number;  };  md?: number | {  span: number;  offset: number;  };  lg?: number | {  span: number;  offset: number;  };  } | component/common.d.ts |
| 函数变更 | 类名：CommonMethod；  API声明：onDragStart(event: (event?: DragEvent, extraParams?: string) => CustomBuilder | DragItemInfo): T;  差异内容：event: (event?: DragEvent, extraParams?: string) => CustomBuilder | DragItemInfo | 类名：CommonMethod；  API声明：onDragStart(event: (event: DragEvent, extraParams?: string) => CustomBuilder | DragItemInfo): T;  差异内容：event: (event: DragEvent, extraParams?: string) => CustomBuilder | DragItemInfo | component/common.d.ts |
| 函数变更 | 类名：CommonMethod；  API声明：onDragEnter(event: (event?: DragEvent, extraParams?: string) => void): T;  差异内容：event: (event?: DragEvent, extraParams?: string) => void | 类名：CommonMethod；  API声明：onDragEnter(event: (event: DragEvent, extraParams?: string) => void): T;  差异内容：event: (event: DragEvent, extraParams?: string) => void | component/common.d.ts |
| 函数变更 | 类名：CommonMethod；  API声明：onDragMove(event: (event?: DragEvent, extraParams?: string) => void): T;  差异内容：event: (event?: DragEvent, extraParams?: string) => void | 类名：CommonMethod；  API声明：onDragMove(event: (event: DragEvent, extraParams?: string) => void): T;  差异内容：event: (event: DragEvent, extraParams?: string) => void | component/common.d.ts |
| 函数变更 | 类名：CommonMethod；  API声明：onDragLeave(event: (event?: DragEvent, extraParams?: string) => void): T;  差异内容：event: (event?: DragEvent, extraParams?: string) => void | 类名：CommonMethod；  API声明：onDragLeave(event: (event: DragEvent, extraParams?: string) => void): T;  差异内容：event: (event: DragEvent, extraParams?: string) => void | component/common.d.ts |
| 函数变更 | 类名：CommonMethod；  API声明：onDrop(event: (event?: DragEvent, extraParams?: string) => void): T;  差异内容：event: (event?: DragEvent, extraParams?: string) => void | 类名：CommonMethod；  API声明：onDrop(event: (event: DragEvent, extraParams?: string) => void): T;  差异内容：event: (event: DragEvent, extraParams?: string) => void | component/common.d.ts |
| 函数变更 | 类名：CommonMethod；  API声明：overlay(value: string, options?: { align?: Alignment; offset?: { x?: number; y?: number } }): T;  差异内容：options?: { align?: Alignment; offset?: { x?: number; y?: number } } | 类名：CommonMethod；  API声明：overlay(value: string | CustomBuilder, options?: {  align?: Alignment;  offset?: {  x?: number;  y?: number;  };  }): T;  差异内容：options?: {  align?: Alignment;  offset?: {  x?: number;  y?: number;  };  } | component/common.d.ts |
| 函数变更 | 类名：CommonMethod；  API声明：linearGradient(value: {  angle?: number | string;  direction?: GradientDirection;  colors: Array<any>;  repeating?: boolean;  }): T;  差异内容：value: {  angle?: number | string;  direction?: GradientDirection;  colors: Array<any>;  repeating?: boolean;  } | 类名：CommonMethod；  API声明：linearGradient(value: {  angle?: number | string;  direction?: GradientDirection;  colors: Array<[  ResourceColor,  number  ]>;  repeating?: boolean;  }): T;  差异内容：value: {  angle?: number | string;  direction?: GradientDirection;  colors: Array<[  ResourceColor,  number  ]>;  repeating?: boolean;  } | component/common.d.ts |
| 函数变更 | 类名：CommonMethod；  API声明：sweepGradient(value: {  center: Array<any>;  start?: number | string;  end?: number | string;  rotation?: number | string;  colors: Array<any>;  repeating?: boolean;  }): T;  差异内容：value: {  center: Array<any>;  start?: number | string;  end?: number | string;  rotation?: number | string;  colors: Array<any>;  repeating?: boolean;  } | 类名：CommonMethod；  API声明：sweepGradient(value: {  center: [  Length,  Length  ];  start?: number | string;  end?: number | string;  rotation?: number | string;  colors: Array<[  ResourceColor,  number  ]>;  repeating?: boolean;  }): T;  差异内容：value: {  center: [  Length,  Length  ];  start?: number | string;  end?: number | string;  rotation?: number | string;  colors: Array<[  ResourceColor,  number  ]>;  repeating?: boolean;  } | component/common.d.ts |
| 函数变更 | 类名：CommonMethod；  API声明：radialGradient(value: { center: Array<any>; radius: number | string; colors: Array<any>; repeating?: boolean }): T;  差异内容：value: { center: Array<any>; radius: number | string; colors: Array<any>; repeating?: boolean } | 类名：CommonMethod；  API声明：radialGradient(value: {  center: [  Length,  Length  ];  radius: number | string;  colors: Array<[  ResourceColor,  number  ]>;  repeating?: boolean;  }): T;  差异内容：value: {  center: [  Length,  Length  ];  radius: number | string;  colors: Array<[  ResourceColor,  number  ]>;  repeating?: boolean;  } | component/common.d.ts |
| 函数变更 | 类名：CommonMethod；  API声明：shadow(value: {  radius: number | Resource;  color?: Color | string | Resource;  offsetX?: number | Resource;  offsetY?: number | Resource;  }): T;  差异内容：value: {  radius: number | Resource;  color?: Color | string | Resource;  offsetX?: number | Resource;  offsetY?: number | Resource;  } | 类名：CommonMethod；  API声明：shadow(value: ShadowOptions | ShadowStyle): T;  差异内容：value: ShadowOptions | ShadowStyle | component/common.d.ts |
| 函数变更 | 类名：GaugeAttribute；  API声明：colors(colors: Array<any>): GaugeAttribute;  差异内容：colors: Array<any> | 类名：GaugeAttribute；  API声明：colors(colors: ResourceColor | LinearGradient | Array<[  ResourceColor | LinearGradient,  number  ]>): GaugeAttribute;  差异内容：colors: ResourceColor | LinearGradient | Array<[  ResourceColor | LinearGradient,  number  ]> | component/gauge.d.ts |
| 函数变更 | 类名：TapGestureInterface；  API声明：onAction(event: (event?: GestureEvent) => void): TapGestureInterface;  差异内容：event: (event?: GestureEvent) => void | 类名：TapGestureInterface；  API声明：onAction(event: (event: GestureEvent) => void): TapGestureInterface;  差异内容：event: (event: GestureEvent) => void | component/gesture.d.ts |
| 函数变更 | 类名：LongPressGestureInterface；  API声明：onAction(event: (event?: GestureEvent) => void): LongPressGestureInterface;  差异内容：event: (event?: GestureEvent) => void | 类名：LongPressGestureInterface；  API声明：onAction(event: (event: GestureEvent) => void): LongPressGestureInterface;  差异内容：event: (event: GestureEvent) => void | component/gesture.d.ts |
| 函数变更 | 类名：LongPressGestureInterface；  API声明：onActionEnd(event: (event?: GestureEvent) => void): LongPressGestureInterface;  差异内容：event: (event?: GestureEvent) => void | 类名：LongPressGestureInterface；  API声明：onActionEnd(event: (event: GestureEvent) => void): LongPressGestureInterface;  差异内容：event: (event: GestureEvent) => void | component/gesture.d.ts |
| 函数变更 | 类名：PanGestureInterface；  API声明：onActionStart(event: (event?: GestureEvent) => void): PanGestureInterface;  差异内容：event: (event?: GestureEvent) => void | 类名：PanGestureInterface；  API声明：onActionStart(event: (event: GestureEvent) => void): PanGestureInterface;  差异内容：event: (event: GestureEvent) => void | component/gesture.d.ts |
| 函数变更 | 类名：PanGestureInterface；  API声明：onActionUpdate(event: (event?: GestureEvent) => void): PanGestureInterface;  差异内容：event: (event?: GestureEvent) => void | 类名：PanGestureInterface；  API声明：onActionUpdate(event: (event: GestureEvent) => void): PanGestureInterface;  差异内容：event: (event: GestureEvent) => void | component/gesture.d.ts |
| 函数变更 | 类名：PanGestureInterface；  API声明：onActionEnd(event: (event?: GestureEvent) => void): PanGestureInterface;  差异内容：event: (event?: GestureEvent) => void | 类名：PanGestureInterface；  API声明：onActionEnd(event: (event: GestureEvent) => void): PanGestureInterface;  差异内容：event: (event: GestureEvent) => void | component/gesture.d.ts |
| 函数变更 | 类名：SwipeGestureInterface；  API声明：onAction(event: (event?: GestureEvent) => void): SwipeGestureInterface;  差异内容：event: (event?: GestureEvent) => void | 类名：SwipeGestureInterface；  API声明：onAction(event: (event: GestureEvent) => void): SwipeGestureInterface;  差异内容：event: (event: GestureEvent) => void | component/gesture.d.ts |
| 函数变更 | 类名：PinchGestureInterface；  API声明：onActionStart(event: (event?: GestureEvent) => void): PinchGestureInterface;  差异内容：event: (event?: GestureEvent) => void | 类名：PinchGestureInterface；  API声明：onActionStart(event: (event: GestureEvent) => void): PinchGestureInterface;  差异内容：event: (event: GestureEvent) => void | component/gesture.d.ts |
| 函数变更 | 类名：PinchGestureInterface；  API声明：onActionUpdate(event: (event?: GestureEvent) => void): PinchGestureInterface;  差异内容：event: (event?: GestureEvent) => void | 类名：PinchGestureInterface；  API声明：onActionUpdate(event: (event: GestureEvent) => void): PinchGestureInterface;  差异内容：event: (event: GestureEvent) => void | component/gesture.d.ts |
| 函数变更 | 类名：PinchGestureInterface；  API声明：onActionEnd(event: (event?: GestureEvent) => void): PinchGestureInterface;  差异内容：event: (event?: GestureEvent) => void | 类名：PinchGestureInterface；  API声明：onActionEnd(event: (event: GestureEvent) => void): PinchGestureInterface;  差异内容：event: (event: GestureEvent) => void | component/gesture.d.ts |
| 函数变更 | 类名：RotationGestureInterface；  API声明：onActionStart(event: (event?: GestureEvent) => void): RotationGestureInterface;  差异内容：event: (event?: GestureEvent) => void | 类名：RotationGestureInterface；  API声明：onActionStart(event: (event: GestureEvent) => void): RotationGestureInterface;  差异内容：event: (event: GestureEvent) => void | component/gesture.d.ts |
| 函数变更 | 类名：RotationGestureInterface；  API声明：onActionUpdate(event: (event?: GestureEvent) => void): RotationGestureInterface;  差异内容：event: (event?: GestureEvent) => void | 类名：RotationGestureInterface；  API声明：onActionUpdate(event: (event: GestureEvent) => void): RotationGestureInterface;  差异内容：event: (event: GestureEvent) => void | component/gesture.d.ts |
| 函数变更 | 类名：RotationGestureInterface；  API声明：onActionEnd(event: (event?: GestureEvent) => void): RotationGestureInterface;  差异内容：event: (event?: GestureEvent) => void | 类名：RotationGestureInterface；  API声明：onActionEnd(event: (event: GestureEvent) => void): RotationGestureInterface;  差异内容：event: (event: GestureEvent) => void | component/gesture.d.ts |
| 函数变更 | 类名：GridAttribute；  API声明：onScrollIndex(event: (first: number) => void): GridAttribute;  差异内容：event: (first: number) => void | 类名：GridAttribute；  API声明：onScrollIndex(event: (first: number, last: number) => void): GridAttribute;  差异内容：event: (first: number, last: number) => void | component/grid.d.ts |
| 函数变更 | 类名：ImageAttribute；  API声明：onComplete(callback: (event?: {  width: number;  height: number;  componentWidth: number;  componentHeight: number;  loadingStatus: number;  }) => void): ImageAttribute;  差异内容：callback: (event?: {  width: number;  height: number;  componentWidth: number;  componentHeight: number;  loadingStatus: number;  }) => void | 类名：ImageAttribute；  API声明：onComplete(callback: (event?: {  /\*\*  \* The width of the image source.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @since 7  \*/  /\*\*  \* The width of the image source.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @since 9  \* @form  \*/  /\*\*  \* The width of the image source.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 10  \* @form  \*/  /\*\*  \* The width of the image source.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @atomicservice  \* @since 11  \* @form  \*/  width: number;  /\*\*  \* The height of the image source.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @since 7  \*/  /\*\*  \* The height of the image source.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @since 9  \* @form  \*/  /\*\*  \* The height of the image source.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 10  \* @form  \*/  /\*\*  \* The height of the image source.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @atomicservice  \* @since 11  \* @form  \*/  height: number;  /\*\*  \* The width of the component source.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @since 7  \*/  /\*\*  \* The width of the component source.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @since 9  \* @form  \*/  /\*\*  \* The width of the component source.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 10  \* @form  \*/  /\*\*  \* The width of the component source.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @atomicservice  \* @since 11  \* @form  \*/  componentWidth: number;  /\*\*  \* The height of the component source.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @since 7  \*/  /\*\*  \* The height of the component source.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @since 9  \* @form  \*/  /\*\*  \* The height of the component source.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 10  \* @form  \*/  /\*\*  \* The height of the component source.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @atomicservice  \* @since 11  \* @form  \*/  componentHeight: number;  /\*\*  \* The value of the status of the image being loaded successfully.  \* If the returned status value is 0, the image data is successfully loaded.  \* If the returned status value is 1, the image is successfully decoded.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @since 7  \*/  /\*\*  \* The value of the status of the image being loaded successfully.  \* If the returned status value is 0, the image data is successfully loaded.  \* If the returned status value is 1, the image is successfully decoded.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @since 9  \* @form  \*/  /\*\*  \* The value of the status of the image being loaded successfully.  \* If the returned status value is 0, the image data is successfully loaded.  \* If the returned status value is 1, the image is successfully decoded.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 10  \* @form  \*/  /\*\*  \* The value of the status of the image being loaded successfully.  \* If the returned status value is 0, the image data is successfully loaded.  \* If the returned status value is 1, the image is successfully decoded.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @atomicservice  \* @since 11  \* @form  \*/  loadingStatus: number;  /\*\*  \* The width of the picture that is actually drawn.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 10  \* @form  \*/  /\*\*  \* The width of the picture that is actually drawn.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @atomicservice  \* @since 11  \* @form  \*/  contentWidth: number;  /\*\*  \* The height of the picture that is actually drawn.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 10  \* @form  \*/  /\*\*  \* The height of the picture that is actually drawn.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @atomicservice  \* @since 11  \* @form  \*/  contentHeight: number;  /\*\*  \* The actual draw is offset from the x-axis of the component itself.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 10  \* @form  \*/  /\*\*  \* The actual draw is offset from the x-axis of the component itself.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @atomicservice  \* @since 11  \* @form  \*/  contentOffsetX: number;  /\*\*  \* The actual draw is offset from the y-axis of the component itself.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 10  \* @form  \*/  /\*\*  \* The actual draw is offset from the y-axis of the component itself.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @atomicservice  \* @since 11  \* @form  \*/  contentOffsetY: number;  }) => void): ImageAttribute;  差异内容：callback: (event?: {  /\*\*  \* The width of the image source.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @since 7  \*/  /\*\*  \* The width of the image source.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @since 9  \* @form  \*/  /\*\*  \* The width of the image source.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 10  \* @form  \*/  /\*\*  \* The width of the image source.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @atomicservice  \* @since 11  \* @form  \*/  width: number;  /\*\*  \* The height of the image source.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @since 7  \*/  /\*\*  \* The height of the image source.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @since 9  \* @form  \*/  /\*\*  \* The height of the image source.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 10  \* @form  \*/  /\*\*  \* The height of the image source.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @atomicservice  \* @since 11  \* @form  \*/  height: number;  /\*\*  \* The width of the component source.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @since 7  \*/  /\*\*  \* The width of the component source.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @since 9  \* @form  \*/  /\*\*  \* The width of the component source.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 10  \* @form  \*/  /\*\*  \* The width of the component source.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @atomicservice  \* @since 11  \* @form  \*/  componentWidth: number;  /\*\*  \* The height of the component source.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @since 7  \*/  /\*\*  \* The height of the component source.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @since 9  \* @form  \*/  /\*\*  \* The height of the component source.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 10  \* @form  \*/  /\*\*  \* The height of the component source.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @atomicservice  \* @since 11  \* @form  \*/  componentHeight: number;  /\*\*  \* The value of the status of the image being loaded successfully.  \* If the returned status value is 0, the image data is successfully loaded.  \* If the returned status value is 1, the image is successfully decoded.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @since 7  \*/  /\*\*  \* The value of the status of the image being loaded successfully.  \* If the returned status value is 0, the image data is successfully loaded.  \* If the returned status value is 1, the image is successfully decoded.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @since 9  \* @form  \*/  /\*\*  \* The value of the status of the image being loaded successfully.  \* If the returned status value is 0, the image data is successfully loaded.  \* If the returned status value is 1, the image is successfully decoded.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 10  \* @form  \*/  /\*\*  \* The value of the status of the image being loaded successfully.  \* If the returned status value is 0, the image data is successfully loaded.  \* If the returned status value is 1, the image is successfully decoded.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @atomicservice  \* @since 11  \* @form  \*/  loadingStatus: number;  /\*\*  \* The width of the picture that is actually drawn.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 10  \* @form  \*/  /\*\*  \* The width of the picture that is actually drawn.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @atomicservice  \* @since 11  \* @form  \*/  contentWidth: number;  /\*\*  \* The height of the picture that is actually drawn.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 10  \* @form  \*/  /\*\*  \* The height of the picture that is actually drawn.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @atomicservice  \* @since 11  \* @form  \*/  contentHeight: number;  /\*\*  \* The actual draw is offset from the x-axis of the component itself.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 10  \* @form  \*/  /\*\*  \* The actual draw is offset from the x-axis of the component itself.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @atomicservice  \* @since 11  \* @form  \*/  contentOffsetX: number;  /\*\*  \* The actual draw is offset from the y-axis of the component itself.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 10  \* @form  \*/  /\*\*  \* The actual draw is offset from the y-axis of the component itself.  \*  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @atomicservice  \* @since 11  \* @form  \*/  contentOffsetY: number;  }) => void | component/image.d.ts |
| 函数变更 | 类名：ListAttribute；  API声明：onScrollIndex(event: (start: number, end: number) => void): ListAttribute;  差异内容：event: (start: number, end: number) => void | 类名：ListAttribute；  API声明：onScrollIndex(event: (start: number, end: number, center: number) => void): ListAttribute;  差异内容：event: (start: number, end: number, center: number) => void | component/list.d.ts |
| 函数变更 | 类名：NavigationAttribute；  API声明：title(value: string | CustomBuilder | NavigationCommonTitle | NavigationCustomTitle): NavigationAttribute;  差异内容：value: string | CustomBuilder | NavigationCommonTitle | NavigationCustomTitle | 类名：NavigationAttribute；  API声明：title(value: ResourceStr | CustomBuilder | NavigationCommonTitle | NavigationCustomTitle, options?: NavigationTitleOptions): NavigationAttribute;  差异内容：value: ResourceStr | CustomBuilder | NavigationCommonTitle | NavigationCustomTitle | component/navigation.d.ts |
| 函数变更 | 类名：PageTransitionEnterInterface；  API声明：onEnter(event: (type?: RouteType, progress?: number) => void): PageTransitionEnterInterface;  差异内容：event: (type?: RouteType, progress?: number) => void | 类名：PageTransitionEnterInterface；  API声明：onEnter(event: (type: RouteType, progress: number) => void): PageTransitionEnterInterface;  差异内容：event: (type: RouteType, progress: number) => void | component/page\_transition.d.ts |
| 函数变更 | 类名：PageTransitionExitInterface；  API声明：onExit(event: (type?: RouteType, progress?: number) => void): PageTransitionExitInterface;  差异内容：event: (type?: RouteType, progress?: number) => void | 类名：PageTransitionExitInterface；  API声明：onExit(event: (type: RouteType, progress: number) => void): PageTransitionExitInterface;  差异内容：event: (type: RouteType, progress: number) => void | component/page\_transition.d.ts |
| 函数变更 | 类名：PanelAttribute；  API声明：onChange(event: (  /  **\* Width of content area.**  **\* @since 7**  **\*/**  **width: number,**  **/\*\***  **\* Height of content area.**  **\* @since 7**  **\*/**  **height: number,**  **/**    \* Initial state.  \* @since 7  \*/  mode: PanelMode) => void): PanelAttribute;  差异内容：event: (  /  **\* Width of content area.**  **\* @since 7**  **\*/**  **width: number,**  **/\*\***  **\* Height of content area.**  **\* @since 7**  **\*/**  **height: number,**  **/**    \* Initial state.  \* @since 7  \*/  mode: PanelMode) => void | 类名：PanelAttribute；  API声明：onChange(event: (  /\*\*  \* Width of content area.  \*  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @since 7  \*/  /\*\*  \* Width of content area.  \*  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @atomicservice  \* @since 11  \* @deprecated since 12  \*/  width: number,  /\*\*  \* Height of content area.  \*  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @since 7  \*/  /\*\*  \* Height of content area.  \*  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @atomicservice  \* @since 11  \* @deprecated since 12  \*/  height: number,  /\*\*  \* Initial state.  \*  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @since 7  \*/  /\*\*  \* Initial state.  \*  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @atomicservice  \* @since 11  \* @deprecated since 12  \*/  mode: PanelMode) => void): PanelAttribute;  差异内容：event: (  /\*\*  \* Width of content area.  \*  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @since 7  \*/  /\*\*  \* Width of content area.  \*  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @atomicservice  \* @since 11  \* @deprecated since 12  \*/  width: number,  /\*\*  \* Height of content area.  \*  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @since 7  \*/  /\*\*  \* Height of content area.  \*  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @atomicservice  \* @since 11  \* @deprecated since 12  \*/  height: number,  /\*\*  \* Initial state.  \*  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @since 7  \*/  /\*\*  \* Initial state.  \*  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @atomicservice  \* @since 11  \* @deprecated since 12  \*/  mode: PanelMode) => void | component/panel.d.ts |
| 函数变更 | 类名：ProgressAttribute；  API声明：style(value: ProgressStyleOptions): ProgressAttribute;  差异内容：value: ProgressStyleOptions | 类名：ProgressAttribute；  API声明：style(value: Style): ProgressAttribute<Type>;  差异内容：value: Style | component/progress.d.ts |
| 函数变更 | 类名：Scroller；  API声明：scrollTo(value: {  xOffset: number | string;  yOffset: number | string;  animation?: {  duration: number;  curve: Curve;  };  });  差异内容：value: {  xOffset: number | string;  yOffset: number | string;  animation?: {  duration: number;  curve: Curve;  };  } | 类名：Scroller；  API声明：scrollTo(value: {  /\*\*  \* The X-axis offset.  \*  \* @type { number | string }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 10  \*/  /\*\*  \* The X-axis offset.  \*  \* @type { number | string }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @atomicservice  \* @since 11  \*/  xOffset: number | string;  /\*\*  \* The Y-axis offset.  \*  \* @type { number | string }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 10  \*/  /\*\*  \* The Y-axis offset.  \*  \* @type { number | string }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @atomicservice  \* @since 11  \*/  yOffset: number | string;  /\*\*  \* Descriptive animation.  \*  \* @type { ?({ duration?: number; curve?: Curve | ICurve } | boolean) } The object type provides custom animation parameters  \* and the boolean type enables default spring animation.  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 10  \*/  /\*\*  \* Descriptive animation.  \*  \* @type { ?({ duration?: number; curve?: Curve | ICurve } | boolean) } The object type provides custom animation parameters  \* and the boolean type enables default spring animation.  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @atomicservice  \* @since 11  \*/  /\*\*  \* Descriptive animation.  \*  \* @type { ?( ScrollAnimationOptions | boolean) } The ScrollAnimationOptions type provides custom animation parameters  \* and the boolean type enables default spring animation.  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @atomicservice  \* @since 12  \*/  animation?: ScrollAnimationOptions | boolean;  });  差异内容：value: {  /\*\*  \* The X-axis offset.  \*  \* @type { number | string }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 10  \*/  /\*\*  \* The X-axis offset.  \*  \* @type { number | string }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @atomicservice  \* @since 11  \*/  xOffset: number | string;  /\*\*  \* The Y-axis offset.  \*  \* @type { number | string }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 10  \*/  /\*\*  \* The Y-axis offset.  \*  \* @type { number | string }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @atomicservice  \* @since 11  \*/  yOffset: number | string;  /\*\*  \* Descriptive animation.  \*  \* @type { ?({ duration?: number; curve?: Curve | ICurve } | boolean) } The object type provides custom animation parameters  \* and the boolean type enables default spring animation.  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 10  \*/  /\*\*  \* Descriptive animation.  \*  \* @type { ?({ duration?: number; curve?: Curve | ICurve } | boolean) } The object type provides custom animation parameters  \* and the boolean type enables default spring animation.  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @atomicservice  \* @since 11  \*/  /\*\*  \* Descriptive animation.  \*  \* @type { ?( ScrollAnimationOptions | boolean) } The ScrollAnimationOptions type provides custom animation parameters  \* and the boolean type enables default spring animation.  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @atomicservice  \* @since 12  \*/  animation?: ScrollAnimationOptions | boolean;  } | component/scroll.d.ts |
| 函数变更 | 类名：Scroller；  API声明：scrollPage(value: {  next: boolean;  direction?: Axis;  });  差异内容：value: {  next: boolean;  direction?: Axis;  } | 类名：Scroller；  API声明：scrollPage(value: {  next: boolean;  });  差异内容：value: {  next: boolean;  } | component/scroll.d.ts |
| 函数变更 | 类名：Scroller；  API声明：scrollPage(value: {  next: boolean;  });  差异内容：value: {  next: boolean;  } | 类名：Scroller；  API声明：scrollPage(value: {  next: boolean;  direction?: Axis;  });  差异内容：value: {  next: boolean;  direction?: Axis;  } | component/scroll.d.ts |
| 函数变更 | 类名：SearchAttribute；  API声明：onPaste(callback: (value: string) => void): SearchAttribute;  差异内容：callback: (value: string) => void | 类名：SearchAttribute；  API声明：onPaste(callback: (value: string, event: PasteEvent) => void): SearchAttribute;  差异内容：callback: (value: string, event: PasteEvent) => void | component/search.d.ts |
| 函数变更 | 类名：SelectAttribute；  API声明：value(value: string): SelectAttribute;  差异内容：value: string | 类名：SelectAttribute；  API声明：value(value: ResourceStr): SelectAttribute;  差异内容：value: ResourceStr | component/select.d.ts |
| 函数变更 | 类名：SelectAttribute；  API声明：onSelect(callback: (index: number, value?: string) => void): SelectAttribute;  差异内容：callback: (index: number, value?: string) => void | 类名：SelectAttribute；  API声明：onSelect(callback: (index: number, value: string) => void): SelectAttribute;  差异内容：callback: (index: number, value: string) => void | component/select.d.ts |
| 函数变更 | 类名：SpanAttribute；  API声明：decoration(value: {  type: TextDecorationType;  color?: ResourceColor;  }): SpanAttribute;  差异内容：value: {  type: TextDecorationType;  color?: ResourceColor;  } | 类名：SpanAttribute；  API声明：decoration(value: DecorationStyleInterface): SpanAttribute;  差异内容：value: DecorationStyleInterface | component/span.d.ts |
| 函数变更 | 类名：StepperAttribute；  API声明：onChange(callback: (prevIndex?: number, index?: number) => void): StepperAttribute;  差异内容：callback: (prevIndex?: number, index?: number) => void | 类名：StepperAttribute；  API声明：onChange(callback: (prevIndex: number, index: number) => void): StepperAttribute;  差异内容：callback: (prevIndex: number, index: number) => void | component/stepper.d.ts |
| 函数变更 | 类名：StepperAttribute；  API声明：onNext(callback: (index?: number, pendingIndex?: number) => void): StepperAttribute;  差异内容：callback: (index?: number, pendingIndex?: number) => void | 类名：StepperAttribute；  API声明：onNext(callback: (index: number, pendingIndex: number) => void): StepperAttribute;  差异内容：callback: (index: number, pendingIndex: number) => void | component/stepper.d.ts |
| 函数变更 | 类名：StepperAttribute；  API声明：onPrevious(callback: (index?: number, pendingIndex?: number) => void): StepperAttribute;  差异内容：callback: (index?: number, pendingIndex?: number) => void | 类名：StepperAttribute；  API声明：onPrevious(callback: (index: number, pendingIndex: number) => void): StepperAttribute;  差异内容：callback: (index: number, pendingIndex: number) => void | component/stepper.d.ts |
| 函数变更 | 类名：SwiperAttribute；  API声明：onAnimationStart(event: (index: number) => void): SwiperAttribute;  差异内容：event: (index: number) => void | 类名：SwiperAttribute；  API声明：onAnimationStart(event: (index: number, targetIndex: number, extraInfo: SwiperAnimationEvent) => void): SwiperAttribute;  差异内容：event: (index: number, targetIndex: number, extraInfo: SwiperAnimationEvent) => void | component/swiper.d.ts |
| 函数变更 | 类名：SwiperAttribute；  API声明：onAnimationEnd(event: (index: number) => void): SwiperAttribute;  差异内容：event: (index: number) => void | 类名：SwiperAttribute；  API声明：onAnimationEnd(event: (index: number, extraInfo: SwiperAnimationEvent) => void): SwiperAttribute;  差异内容：event: (index: number, extraInfo: SwiperAnimationEvent) => void | component/swiper.d.ts |
| 函数变更 | 类名：TextAttribute；  API声明：decoration(value: {  type: TextDecorationType;  color?: ResourceColor;  }): TextAttribute;  差异内容：value: {  type: TextDecorationType;  color?: ResourceColor;  } | 类名：TextAttribute；  API声明：decoration(value: DecorationStyleInterface): TextAttribute;  差异内容：value: DecorationStyleInterface | component/text.d.ts |
| 函数变更 | 类名：TextAreaAttribute；  API声明：onPaste(callback: (value: string) => void): TextAreaAttribute;  差异内容：callback: (value: string) => void | 类名：TextAreaAttribute；  API声明：onPaste(callback: (value: string, event: PasteEvent) => void): TextAreaAttribute;  差异内容：callback: (value: string, event: PasteEvent) => void | component/text\_area.d.ts |
| 函数变更 | 类名：TextInputAttribute；  API声明：onSubmit(callback: (enterKey: EnterKeyType) => void): TextInputAttribute;  差异内容：callback: (enterKey: EnterKeyType) => void | 类名：TextInputAttribute；  API声明：onSubmit(callback: (enterKey: EnterKeyType, event: SubmitEvent) => void): TextInputAttribute;  差异内容：callback: (enterKey: EnterKeyType, event: SubmitEvent) => void | component/text\_input.d.ts |
| 函数变更 | 类名：TextInputAttribute；  API声明：onPaste(callback: (value: string) => void): TextInputAttribute;  差异内容：callback: (value: string) => void | 类名：TextInputAttribute；  API声明：onPaste(callback: (value: string, event: PasteEvent) => void): TextInputAttribute;  差异内容：callback: (value: string, event: PasteEvent) => void | component/text\_input.d.ts |
| 函数变更 | 类名：TextPickerAttribute；  API声明：onChange(callback: (value: string, index: number) => void): TextPickerAttribute;  差异内容：callback: (value: string, index: number) => void | 类名：TextPickerAttribute；  API声明：onChange(callback: (value: string | string[], index: number | number[]) => void): TextPickerAttribute;  差异内容：callback: (value: string | string[], index: number | number[]) => void | component/text\_picker.d.ts |
| 函数变更 | 类名：VideoAttribute；  API声明：onFullscreenChange(callback: (event?: {  fullscreen: boolean;  }) => void): VideoAttribute;  差异内容：callback: (event?: {  fullscreen: boolean;  }) => void | 类名：VideoAttribute；  API声明：onFullscreenChange(callback: (event: {  /\*\*  \* Play the flag in full screen.  \*  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 10  \*/  /\*\*  \* Play the flag in full screen.  \*  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @atomicservice  \* @since 11  \*/  fullscreen: boolean;  }) => void): VideoAttribute;  差异内容：callback: (event: {  /\*\*  \* Play the flag in full screen.  \*  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 10  \*/  /\*\*  \* Play the flag in full screen.  \*  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @atomicservice  \* @since 11  \*/  fullscreen: boolean;  }) => void | component/video.d.ts |
| 函数变更 | 类名：VideoAttribute；  API声明：onPrepared(callback: (event?: {  duration: number;  }) => void): VideoAttribute;  差异内容：callback: (event?: {  duration: number;  }) => void | 类名：VideoAttribute；  API声明：onPrepared(callback: (event: {  /\*\*  \* Playback duration.  \*  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 10  \*/  /\*\*  \* Playback duration.  \*  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @atomicservice  \* @since 11  \*/  duration: number;  }) => void): VideoAttribute;  差异内容：callback: (event: {  /\*\*  \* Playback duration.  \*  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 10  \*/  /\*\*  \* Playback duration.  \*  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @atomicservice  \* @since 11  \*/  duration: number;  }) => void | component/video.d.ts |
| 函数变更 | 类名：VideoAttribute；  API声明：onSeeking(callback: (event?: {  time: number;  }) => void): VideoAttribute;  差异内容：callback: (event?: {  time: number;  }) => void | 类名：VideoAttribute；  API声明：onSeeking(callback: (event: {  /\*\*  \* Play time.  \*  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 10  \*/  /\*\*  \* Play time.  \*  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @atomicservice  \* @since 11  \*/  time: number;  }) => void): VideoAttribute;  差异内容：callback: (event: {  /\*\*  \* Play time.  \*  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 10  \*/  /\*\*  \* Play time.  \*  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @atomicservice  \* @since 11  \*/  time: number;  }) => void | component/video.d.ts |
| 函数变更 | 类名：VideoAttribute；  API声明：onSeeked(callback: (event?: {  time: number;  }) => void): VideoAttribute;  差异内容：callback: (event?: {  time: number;  }) => void | 类名：VideoAttribute；  API声明：onSeeked(callback: (event: {  /\*\*  \* Play time.  \*  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 10  \*/  /\*\*  \* Play time.  \*  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @atomicservice  \* @since 11  \*/  time: number;  }) => void): VideoAttribute;  差异内容：callback: (event: {  /\*\*  \* Play time.  \*  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 10  \*/  /\*\*  \* Play time.  \*  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @atomicservice  \* @since 11  \*/  time: number;  }) => void | component/video.d.ts |
| 函数变更 | 类名：VideoAttribute；  API声明：onUpdate(callback: (event?: {  time: number;  }) => void): VideoAttribute;  差异内容：callback: (event?: {  time: number;  }) => void | 类名：VideoAttribute；  API声明：onUpdate(callback: (event: {  /\*\*  \* Play time.  \*  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 10  \*/  /\*\*  \* Play time.  \*  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @atomicservice  \* @since 11  \*/  time: number;  }) => void): VideoAttribute;  差异内容：callback: (event: {  /\*\*  \* Play time.  \*  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 10  \*/  /\*\*  \* Play time.  \*  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @atomicservice  \* @since 11  \*/  time: number;  }) => void | component/video.d.ts |
| 函数变更 | 类名：AlertDialog；  API声明：static show(value: AlertDialogParamWithConfirm | AlertDialogParamWithButtons);  差异内容：value: AlertDialogParamWithConfirm | AlertDialogParamWithButtons | 类名：AlertDialog；  API声明：static show(value: AlertDialogParamWithConfirm | AlertDialogParamWithButtons | AlertDialogParamWithOptions);  差异内容：value: AlertDialogParamWithConfirm | AlertDialogParamWithButtons | AlertDialogParamWithOptions | component/alert\_dialog.d.ts |
| 函数变更 | 类名：CanvasRenderer；  API声明：putImageData(imagedata: ImageData, dx: number, dy: number): void;  差异内容：dx: number | 类名：CanvasRenderer；  API声明：putImageData(imagedata: ImageData, dx: number | string, dy: number | string): void;  差异内容：dx: number | string | component/canvas.d.ts |
| 函数变更 | 类名：CanvasRenderer；  API声明：putImageData(imagedata: ImageData, dx: number, dy: number): void;  差异内容：dy: number | 类名：CanvasRenderer；  API声明：putImageData(imagedata: ImageData, dx: number | string, dy: number | string): void;  差异内容：dy: number | string | component/canvas.d.ts |
| 函数变更 | 类名：CanvasRenderer；  API声明：putImageData(imagedata: ImageData, dx: number, dy: number, dirtyX: number, dirtyY: number, dirtyWidth: number, dirtyHeight: number): void;  差异内容：dx: number | 类名：CanvasRenderer；  API声明：putImageData(imagedata: ImageData, dx: number | string, dy: number | string, dirtyX: number | string, dirtyY: number | string, dirtyWidth: number | string, dirtyHeight: number | string): void;  差异内容：dx: number | string | component/canvas.d.ts |
| 函数变更 | 类名：CanvasRenderer；  API声明：putImageData(imagedata: ImageData, dx: number, dy: number, dirtyX: number, dirtyY: number, dirtyWidth: number, dirtyHeight: number): void;  差异内容：dy: number | 类名：CanvasRenderer；  API声明：putImageData(imagedata: ImageData, dx: number | string, dy: number | string, dirtyX: number | string, dirtyY: number | string, dirtyWidth: number | string, dirtyHeight: number | string): void;  差异内容：dy: number | string | component/canvas.d.ts |
| 函数变更 | 类名：CanvasRenderer；  API声明：putImageData(imagedata: ImageData, dx: number, dy: number, dirtyX: number, dirtyY: number, dirtyWidth: number, dirtyHeight: number): void;  差异内容：dirtyX: number | 类名：CanvasRenderer；  API声明：putImageData(imagedata: ImageData, dx: number | string, dy: number | string, dirtyX: number | string, dirtyY: number | string, dirtyWidth: number | string, dirtyHeight: number | string): void;  差异内容：dirtyX: number | string | component/canvas.d.ts |
| 函数变更 | 类名：CanvasRenderer；  API声明：putImageData(imagedata: ImageData, dx: number, dy: number, dirtyX: number, dirtyY: number, dirtyWidth: number, dirtyHeight: number): void;  差异内容：dirtyY: number | 类名：CanvasRenderer；  API声明：putImageData(imagedata: ImageData, dx: number | string, dy: number | string, dirtyX: number | string, dirtyY: number | string, dirtyWidth: number | string, dirtyHeight: number | string): void;  差异内容：dirtyY: number | string | component/canvas.d.ts |
| 函数变更 | 类名：CanvasRenderer；  API声明：putImageData(imagedata: ImageData, dx: number, dy: number, dirtyX: number, dirtyY: number, dirtyWidth: number, dirtyHeight: number): void;  差异内容：dirtyWidth: number | 类名：CanvasRenderer；  API声明：putImageData(imagedata: ImageData, dx: number | string, dy: number | string, dirtyX: number | string, dirtyY: number | string, dirtyWidth: number | string, dirtyHeight: number | string): void;  差异内容：dirtyWidth: number | string | component/canvas.d.ts |
| 函数变更 | 类名：CanvasRenderer；  API声明：putImageData(imagedata: ImageData, dx: number, dy: number, dirtyX: number, dirtyY: number, dirtyWidth: number, dirtyHeight: number): void;  差异内容：dirtyHeight: number | 类名：CanvasRenderer；  API声明：putImageData(imagedata: ImageData, dx: number | string, dy: number | string, dirtyX: number | string, dirtyY: number | string, dirtyWidth: number | string, dirtyHeight: number | string): void;  差异内容：dirtyHeight: number | string | component/canvas.d.ts |
| 函数变更 | 类名：CommonMethod；  API声明：padding(value: Padding | Length): T;  差异内容：value: Padding | Length | 类名：CommonMethod；  API声明：padding(value: Padding | Length | LocalizedPadding): T;  差异内容：value: Padding | Length | LocalizedPadding | component/common.d.ts |
| 函数变更 | 类名：CommonMethod；  API声明：margin(value: Margin | Length): T;  差异内容：value: Margin | Length | 类名：CommonMethod；  API声明：margin(value: Margin | Length | LocalizedMargin): T;  差异内容：value: Margin | Length | LocalizedMargin | component/common.d.ts |
| 函数变更 | 类名：CommonMethod；  API声明：backgroundImage(src: ResourceStr, repeat?: ImageRepeat): T;  差异内容：src: ResourceStr | 类名：CommonMethod；  API声明：backgroundImage(src: ResourceStr | PixelMap, repeat?: ImageRepeat): T;  差异内容：src: ResourceStr | PixelMap | component/common.d.ts |
| 函数变更 | 类名：CommonMethod；  API声明：transition(value: TransitionOptions): T;  差异内容：value: TransitionOptions | 类名：CommonMethod；  API声明：transition(value: TransitionOptions | TransitionEffect): T;  差异内容：value: TransitionOptions | TransitionEffect | component/common.d.ts |
| 函数变更 | 类名：CommonMethod；  API声明：invert(value: number): T;  差异内容：value: number | 类名：CommonMethod；  API声明：invert(value: number | InvertOptions): T;  差异内容：value: number | InvertOptions | component/common.d.ts |
| 函数变更 | 类名：CommonMethod；  API声明：position(value: Position): T;  差异内容：value: Position | 类名：CommonMethod；  API声明：position(value: Position | Edges | LocalizedEdges): T;  差异内容：value: Position | Edges | LocalizedEdges | component/common.d.ts |
| 函数变更 | 类名：CommonMethod；  API声明：markAnchor(value: Position): T;  差异内容：value: Position | 类名：CommonMethod；  API声明：markAnchor(value: Position | LocalizedPosition): T;  差异内容：value: Position | LocalizedPosition | component/common.d.ts |
| 函数变更 | 类名：CommonMethod；  API声明：offset(value: Position): T;  差异内容：value: Position | 类名：CommonMethod；  API声明：offset(value: Position | Edges | LocalizedEdges): T;  差异内容：value: Position | Edges | LocalizedEdges | component/common.d.ts |
| 函数变更 | 类名：CommonMethod；  API声明：overlay(value: string, options?: { align?: Alignment; offset?: { x?: number; y?: number } }): T;  差异内容：value: string | 类名：CommonMethod；  API声明：overlay(value: string | CustomBuilder, options?: {  align?: Alignment;  offset?: {  x?: number;  y?: number;  };  }): T;  差异内容：value: string | CustomBuilder | component/common.d.ts |
| 函数变更 | 类名：ImageAttribute；  API声明：alt(value: string | Resource): ImageAttribute;  差异内容：value: string | Resource | 类名：ImageAttribute；  API声明：alt(value: string | Resource | PixelMap): ImageAttribute;  差异内容：value: string | Resource | PixelMap | component/image.d.ts |
| 函数变更 | 类名：ImageAttribute；  API声明：colorFilter(value: ColorFilter): ImageAttribute;  差异内容：value: ColorFilter | 类名：ImageAttribute；  API声明：colorFilter(value: ColorFilter | DrawingColorFilter): ImageAttribute;  差异内容：value: ColorFilter | DrawingColorFilter | component/image.d.ts |
| 函数变更 | 类名：MenuItemAttribute；  API声明：selectIcon(value: boolean): MenuItemAttribute;  差异内容：value: boolean | 类名：MenuItemAttribute；  API声明：selectIcon(value: boolean | ResourceStr): MenuItemAttribute;  差异内容：value: boolean | ResourceStr | component/menu\_item.d.ts |
| 函数变更 | 类名：ProgressAttribute；  API声明：color(value: ResourceColor): ProgressAttribute;  差异内容：value: ResourceColor | 类名：ProgressAttribute；  API声明：color(value: ResourceColor | LinearGradient): ProgressAttribute<Type>;  差异内容：value: ResourceColor | LinearGradient | component/progress.d.ts |
| 函数变更 | 类名：SelectAttribute；  API声明：selected(value: number): SelectAttribute;  差异内容：value: number | 类名：SelectAttribute；  API声明：selected(value: number | Resource): SelectAttribute;  差异内容：value: number | Resource | component/select.d.ts |
| 函数变更 | 类名：SliderAttribute；  API声明：trackColor(value: ResourceColor): SliderAttribute;  差异内容：value: ResourceColor | 类名：SliderAttribute；  API声明：trackColor(value: ResourceColor | LinearGradient): SliderAttribute;  差异内容：value: ResourceColor | LinearGradient | component/slider.d.ts |
| 函数变更 | 类名：SwiperAttribute；  API声明：indicator(value: boolean): SwiperAttribute;  差异内容：value: boolean | 类名：SwiperAttribute；  API声明：indicator(value: DotIndicator | DigitIndicator | boolean): SwiperAttribute;  差异内容：value: DotIndicator | DigitIndicator | boolean | component/swiper.d.ts |
| 函数变更 | 类名：SwiperAttribute；  API声明：displayCount(value: number | string): SwiperAttribute;  差异内容：value: number | string | 类名：SwiperAttribute；  API声明：displayCount(value: number | string | SwiperAutoFill, swipeByGroup?: boolean): SwiperAttribute;  差异内容：value: number | string | SwiperAutoFill | component/swiper.d.ts |
| 函数变更 | 类名：SwiperAttribute；  API声明：curve(value: Curve | string): SwiperAttribute;  差异内容：value: Curve | string | 类名：SwiperAttribute；  API声明：curve(value: Curve | string | ICurve): SwiperAttribute;  差异内容：value: Curve | string | ICurve | component/swiper.d.ts |
| 函数变更 | 类名：TextInputAttribute；  API声明：style(value: TextInputStyle): TextInputAttribute;  差异内容：value: TextInputStyle | 类名：TextInputAttribute；  API声明：style(value: TextInputStyle | TextContentStyle): TextInputAttribute;  差异内容：value: TextInputStyle | TextContentStyle | component/text\_input.d.ts |
| 属性变更 | 类名：MouseEvent；  API声明：stopPropagation?: () => void;  差异内容：stopPropagation?: () => void; | 类名：MouseEvent；  API声明：stopPropagation: () => void;  差异内容：stopPropagation: () => void; | component/common.d.ts |
| 属性变更 | 类名：TouchEvent；  API声明：stopPropagation?: () => void;  差异内容：stopPropagation?: () => void; | 类名：TouchEvent；  API声明：stopPropagation: () => void;  差异内容：stopPropagation: () => void; | component/common.d.ts |
| 属性变更 | 类名：KeyEvent；  API声明：stopPropagation?: () => void;  差异内容：stopPropagation?: () => void; | 类名：KeyEvent；  API声明：stopPropagation: () => void;  差异内容：stopPropagation: () => void; | component/common.d.ts |
| 属性变更 | 类名：TimePickerResult；  API声明：hour?: number;  差异内容：hour?: number; | 类名：TimePickerResult；  API声明：hour: number;  差异内容：hour: number; | component/time\_picker.d.ts |
| 属性变更 | 类名：TimePickerResult；  API声明：minute?: number;  差异内容：minute?: number; | 类名：TimePickerResult；  API声明：minute: number;  差异内容：minute: number; | component/time\_picker.d.ts |
| 属性变更 | 类名：CanvasRenderer；  API声明：fillStyle: string | CanvasGradient | CanvasPattern;  差异内容：string,CanvasGradient,CanvasPattern | 类名：CanvasRenderer；  API声明：fillStyle: string | number | CanvasGradient | CanvasPattern;  差异内容：string,number,CanvasGradient,CanvasPattern | component/canvas.d.ts |
| 属性变更 | 类名：CanvasRenderer；  API声明：strokeStyle: string | CanvasGradient | CanvasPattern;  差异内容：string,CanvasGradient,CanvasPattern | 类名：CanvasRenderer；  API声明：strokeStyle: string | number | CanvasGradient | CanvasPattern;  差异内容：string,number,CanvasGradient,CanvasPattern | component/canvas.d.ts |
| 属性变更 | 类名：global；  API声明：declare const Entry: ClassDecorator & ((storage?: LocalStorage) => ClassDecorator);  差异内容：ClassDecorator & ((storage?: LocalStorage) => ClassDecorator) | 类名：global；  API声明：declare const Entry: ClassDecorator & ((options?: LocalStorage | EntryOptions) => ClassDecorator);  差异内容：ClassDecorator & ((options?: LocalStorage | EntryOptions) => ClassDecorator) | component/common.d.ts |
| 属性变更 | 类名：global；  API声明：declare const Provide: PropertyDecorator & ((value: string) => PropertyDecorator);  差异内容：PropertyDecorator & ((value: string) => PropertyDecorator) | 类名：global；  API声明：declare const Provide: PropertyDecorator & ((value: string | ProvideOptions) => PropertyDecorator);  差异内容：PropertyDecorator & ((value: string | ProvideOptions) => PropertyDecorator) | component/common.d.ts |
| 属性变更 | 类名：AlignRuleOption；  API声明：left?: { anchor: string, align: HorizontalAlign };  差异内容：{ anchor: string, align: HorizontalAlign } | 类名：AlignRuleOption；  API声明：left?: {  anchor: string;  align: HorizontalAlign;  };  差异内容：{  anchor: string;  align: HorizontalAlign;  } | component/common.d.ts |
| 属性变更 | 类名：AlignRuleOption；  API声明：right?: { anchor: string, align: HorizontalAlign };  差异内容：{ anchor: string, align: HorizontalAlign } | 类名：AlignRuleOption；  API声明：right?: {  anchor: string;  align: HorizontalAlign;  };  差异内容：{  anchor: string;  align: HorizontalAlign;  } | component/common.d.ts |
| 属性变更 | 类名：AlignRuleOption；  API声明：middle?: { anchor: string, align: HorizontalAlign };  差异内容：{ anchor: string, align: HorizontalAlign } | 类名：AlignRuleOption；  API声明：middle?: {  anchor: string;  align: HorizontalAlign;  };  差异内容：{  anchor: string;  align: HorizontalAlign;  } | component/common.d.ts |
| 属性变更 | 类名：AlignRuleOption；  API声明：top?: { anchor: string, align: VerticalAlign };  差异内容：{ anchor: string, align: VerticalAlign } | 类名：AlignRuleOption；  API声明：top?: {  anchor: string;  align: VerticalAlign;  };  差异内容：{  anchor: string;  align: VerticalAlign;  } | component/common.d.ts |
| 属性变更 | 类名：AlignRuleOption；  API声明：bottom?: { anchor: string, align: VerticalAlign };  差异内容：{ anchor: string, align: VerticalAlign } | 类名：AlignRuleOption；  API声明：bottom?: {  anchor: string;  align: VerticalAlign;  };  差异内容：{  anchor: string;  align: VerticalAlign;  } | component/common.d.ts |
| 属性变更 | 类名：AlignRuleOption；  API声明：center?: { anchor: string, align: VerticalAlign };  差异内容：{ anchor: string, align: VerticalAlign } | 类名：AlignRuleOption；  API声明：center?: {  anchor: string;  align: VerticalAlign;  };  差异内容：{  anchor: string;  align: VerticalAlign;  } | component/common.d.ts |
| 属性变更 | 类名：LinearGradient；  API声明：colors: Array<any>;  差异内容：Array<any> | 类名：LinearGradient；  API声明：colors: Array<[  ResourceColor,  number  ]>;  差异内容：Array<[  ResourceColor,  number  ]> | component/common.d.ts |
| 属性变更 | 类名：TextPickerOptions；  API声明：range: string[] | Resource;  差异内容：string[],Resource | 类名：TextPickerOptions；  API声明：range: string[] | string[][] | Resource | TextPickerRangeContent[] | TextCascadePickerRangeContent[];  差异内容：string[],string[][],Resource,TextPickerRangeContent[],TextCascadePickerRangeContent[] | component/text\_picker.d.ts |
| 属性变更 | 类名：global；  API声明：declare const Component: ClassDecorator;  差异内容：ClassDecorator | 类名：global；  API声明：declare const Component: ClassDecorator & ((options: ComponentOptions) => ClassDecorator);  差异内容：ClassDecorator & ((options: ComponentOptions) => ClassDecorator) | component/common.d.ts |
| 属性变更 | 类名：FontOptions；  API声明：familyName: string;  差异内容：string | 类名：FontOptions；  API声明：familyName: string | Resource;  差异内容：string,Resource | api/@ohos.font.d.ts |
| 属性变更 | 类名：FontOptions；  API声明：familySrc: string;  差异内容：string | 类名：FontOptions；  API声明：familySrc: string | Resource;  差异内容：string,Resource | api/@ohos.font.d.ts |
| 属性变更 | 类名：MeasureOptions；  API声明：textContent: string;  差异内容：string | 类名：MeasureOptions；  API声明：textContent: string | Resource;  差异内容：string,Resource | api/@ohos.measure.d.ts |
| 属性变更 | 类名：ShowDialogOptions；  API声明：buttons?: [  Button,  Button?,  Button?  ];  差异内容：[  Button,  Button?,  Button?  ] | 类名：ShowDialogOptions；  API声明：buttons?: Array<Button>;  差异内容：Array<Button> | api/@ohos.promptAction.d.ts |
| 属性变更 | 类名：BadgeParam；  API声明：position?: BadgePosition;  差异内容：BadgePosition | 类名：BadgeParam；  API声明：position?: BadgePosition | Position;  差异内容：BadgePosition,Position | component/badge.d.ts |
| 属性变更 | 类名：sharedTransitionOptions；  API声明：curve?: Curve | string;  差异内容：Curve,string | 类名：sharedTransitionOptions；  API声明：curve?: Curve | string | ICurve;  差异内容：Curve,string,ICurve | component/common.d.ts |
| 属性变更 | 类名：BorderImageOption；  API声明：slice?: Length | EdgeWidths,  差异内容：Length,EdgeWidths | 类名：BorderImageOption；  API声明：slice?: Length | EdgeWidths | LocalizedEdgeWidths;  差异内容：Length,EdgeWidths,LocalizedEdgeWidths | component/common.d.ts |
| 属性变更 | 类名：BorderImageOption；  API声明：width?: Length | EdgeWidths,  差异内容：Length,EdgeWidths | 类名：BorderImageOption；  API声明：width?: Length | EdgeWidths | LocalizedEdgeWidths;  差异内容：Length,EdgeWidths,LocalizedEdgeWidths | component/common.d.ts |
| 属性变更 | 类名：BorderImageOption；  API声明：outset?: Length | EdgeWidths,  差异内容：Length,EdgeWidths | 类名：BorderImageOption；  API声明：outset?: Length | EdgeWidths | LocalizedEdgeWidths;  差异内容：Length,EdgeWidths,LocalizedEdgeWidths | component/common.d.ts |
| 属性变更 | 类名：ImageFrameInfo；  API声明：src: string | Resource;  差异内容：string,Resource | 类名：ImageFrameInfo；  API声明：src: string | Resource | PixelMap;  差异内容：string,Resource,PixelMap | component/image\_animator.d.ts |
| 属性变更 | 类名：SwipeActionOptions；  API声明：start?: CustomBuilder;  差异内容：CustomBuilder | 类名：SwipeActionOptions；  API声明：start?: CustomBuilder | SwipeActionItem;  差异内容：CustomBuilder,SwipeActionItem | component/list\_item.d.ts |
| 属性变更 | 类名：SwipeActionOptions；  API声明：end?: CustomBuilder;  差异内容：CustomBuilder | 类名：SwipeActionOptions；  API声明：end?: CustomBuilder | SwipeActionItem;  差异内容：CustomBuilder,SwipeActionItem | component/list\_item.d.ts |
| 属性变更 | 类名：TextPickerOptions；  API声明：value?: string;  差异内容：string | 类名：TextPickerOptions；  API声明：value?: string | string[];  差异内容：string,string[] | component/text\_picker.d.ts |
| 属性变更 | 类名：TextPickerOptions；  API声明：selected?: number;  差异内容：number | 类名：TextPickerOptions；  API声明：selected?: number | number[];  差异内容：number,number[] | component/text\_picker.d.ts |
| 属性变更 | 类名：TextPickerResult；  API声明：value: string;  差异内容：string | 类名：TextPickerResult；  API声明：value: string | string[];  差异内容：string,string[] | component/text\_picker.d.ts |
| 属性变更 | 类名：TextPickerResult；  API声明：index: number;  差异内容：number | 类名：TextPickerResult；  API声明：index: number | number[];  差异内容：number,number[] | component/text\_picker.d.ts |
| 属性变更 | 类名：BorderOptions；  API声明：width?: EdgeWidths | Length;  差异内容：EdgeWidths,Length | 类名：BorderOptions；  API声明：width?: EdgeWidths | Length | LocalizedEdgeWidths;  差异内容：EdgeWidths,Length,LocalizedEdgeWidths | component/units.d.ts |
| 属性变更 | 类名：BorderOptions；  API声明：color?: EdgeColors | ResourceColor;  差异内容：EdgeColors,ResourceColor | 类名：BorderOptions；  API声明：color?: EdgeColors | ResourceColor | LocalizedEdgeColors;  差异内容：EdgeColors,ResourceColor,LocalizedEdgeColors | component/units.d.ts |
| 属性变更 | 类名：BorderOptions；  API声明：radius?: BorderRadiuses | Length;  差异内容：BorderRadiuses,Length | 类名：BorderOptions；  API声明：radius?: BorderRadiuses | Length | LocalizedBorderRadiuses;  差异内容：BorderRadiuses,Length,LocalizedBorderRadiuses | component/units.d.ts |
| 属性变更 | 类名：ProgressOptions；  API声明：type?: ProgressType;  差异内容：ProgressType | 类名：ProgressOptions；  API声明：type?: Type;  差异内容：Type | component/progress.d.ts |
| 枚举赋值发生改变 | 类名：TextOverflow；  API声明：Clip  差异内容：0 | 类名：TextOverflow；  API声明：Clip  差异内容：1 | component/enums.d.ts |
| 枚举赋值发生改变 | 类名：TextOverflow；  API声明：Ellipsis  差异内容：1 | 类名：TextOverflow；  API声明：Ellipsis  差异内容：2 | component/enums.d.ts |
| 枚举赋值发生改变 | 类名：TextOverflow；  API声明：None  差异内容：2 | 类名：TextOverflow；  API声明：None  差异内容：0 | component/enums.d.ts |
| 枚举赋值发生改变 | 类名：EnterKeyType；  API声明：Go  差异内容：0 | 类名：EnterKeyType；  API声明：Go = 2  差异内容：2 | component/text\_input.d.ts |
| 枚举赋值发生改变 | 类名：EnterKeyType；  API声明：Search  差异内容：1 | 类名：EnterKeyType；  API声明：Search = 3  差异内容：3 | component/text\_input.d.ts |
| 枚举赋值发生改变 | 类名：EnterKeyType；  API声明：Send  差异内容：2 | 类名：EnterKeyType；  API声明：Send = 4  差异内容：4 | component/text\_input.d.ts |
| 枚举赋值发生改变 | 类名：EnterKeyType；  API声明：Next  差异内容：3 | 类名：EnterKeyType；  API声明：Next = 5  差异内容：5 | component/text\_input.d.ts |
| 枚举赋值发生改变 | 类名：EnterKeyType；  API声明：Done  差异内容：4 | 类名：EnterKeyType；  API声明：Done = 6  差异内容：6 | component/text\_input.d.ts |
| 新增API | NA | 类名：console；  API声明：static assert(value?: Object, ...arguments: Object[]): void;  差异内容：static assert(value?: Object, ...arguments: Object[]): void; | api/@internal/full/global.d.ts |
| 新增API | NA | 类名：console；  API声明：static count(label?: string): void;  差异内容：static count(label?: string): void; | api/@internal/full/global.d.ts |
| 新增API | NA | 类名：console；  API声明：static countReset(label?: string): void;  差异内容：static countReset(label?: string): void; | api/@internal/full/global.d.ts |
| 新增API | NA | 类名：console；  API声明：static dir(dir?: Object): void;  差异内容：static dir(dir?: Object): void; | api/@internal/full/global.d.ts |
| 新增API | NA | 类名：console；  API声明：static dirxml(...arguments: Object[]): void;  差异内容：static dirxml(...arguments: Object[]): void; | api/@internal/full/global.d.ts |
| 新增API | NA | 类名：console；  API声明：static group(...arguments: Object[]): void;  差异内容：static group(...arguments: Object[]): void; | api/@internal/full/global.d.ts |
| 新增API | NA | 类名：console；  API声明：static groupCollapsed(...arguments: Object[]): void;  差异内容：static groupCollapsed(...arguments: Object[]): void; | api/@internal/full/global.d.ts |
| 新增API | NA | 类名：console；  API声明：static groupEnd(): void;  差异内容：static groupEnd(): void; | api/@internal/full/global.d.ts |
| 新增API | NA | 类名：console；  API声明：static table(tableData?: Object): void;  差异内容：static table(tableData?: Object): void; | api/@internal/full/global.d.ts |
| 新增API | NA | 类名：console；  API声明：static time(label?: string): void;  差异内容：static time(label?: string): void; | api/@internal/full/global.d.ts |
| 新增API | NA | 类名：console；  API声明：static timeEnd(label?: string): void;  差异内容：static timeEnd(label?: string): void; | api/@internal/full/global.d.ts |
| 新增API | NA | 类名：console；  API声明：static timeLog(label?: string, ...arguments: Object[]): void;  差异内容：static timeLog(label?: string, ...arguments: Object[]): void; | api/@internal/full/global.d.ts |
| 新增API | NA | 类名：console；  API声明：static trace(...arguments: Object[]): void;  差异内容：static trace(...arguments: Object[]): void; | api/@internal/full/global.d.ts |
| 新增API | NA | 类名：console；  API声明：static traceHybridStack(): void;  差异内容：static traceHybridStack(): void; | api/@internal/full/global.d.ts |
| 新增API | NA | 类名：AnimatorResult；  API声明：onFrame: (progress: number) => void;  差异内容：onFrame: (progress: number) => void; | api/@ohos.animator.d.ts |
| 新增API | NA | 类名：AnimatorResult；  API声明：onFinish: () => void;  差异内容：onFinish: () => void; | api/@ohos.animator.d.ts |
| 新增API | NA | 类名：AnimatorResult；  API声明：onCancel: () => void;  差异内容：onCancel: () => void; | api/@ohos.animator.d.ts |
| 新增API | NA | 类名：AnimatorResult；  API声明：onRepeat: () => void;  差异内容：onRepeat: () => void; | api/@ohos.animator.d.ts |
| 新增API | NA | 类名：AnimatorResult；  API声明：setExpectedFrameRateRange(rateRange: ExpectedFrameRateRange): void;  差异内容：setExpectedFrameRateRange(rateRange: ExpectedFrameRateRange): void; | api/@ohos.animator.d.ts |
| 新增API | NA | 类名：curves；  API声明：function customCurve(interpolate: (fraction: number) => number): ICurve;  差异内容：function customCurve(interpolate: (fraction: number) => number): ICurve; | api/@ohos.curves.d.ts |
| 新增API | NA | 类名：curves；  API声明：function interpolatingSpring(velocity: number, mass: number, stiffness: number, damping: number): ICurve;  差异内容：function interpolatingSpring(velocity: number, mass: number, stiffness: number, damping: number): ICurve; | api/@ohos.curves.d.ts |
| 新增API | NA | 类名：display；  API声明：function isFoldable(): boolean;  差异内容：function isFoldable(): boolean; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：display；  API声明：function getFoldStatus(): FoldStatus;  差异内容：function getFoldStatus(): FoldStatus; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：display；  API声明：function on(type: 'foldStatusChange', callback: Callback<FoldStatus>): void;  差异内容：function on(type: 'foldStatusChange', callback: Callback<FoldStatus>): void; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：display；  API声明：function off(type: 'foldStatusChange', callback?: Callback<FoldStatus>): void;  差异内容：function off(type: 'foldStatusChange', callback?: Callback<FoldStatus>): void; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：display；  API声明：function on(type: 'foldAngleChange', callback: Callback<Array<number>>): void;  差异内容：function on(type: 'foldAngleChange', callback: Callback<Array<number>>): void; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：display；  API声明：function off(type: 'foldAngleChange', callback?: Callback<Array<number>>): void;  差异内容：function off(type: 'foldAngleChange', callback?: Callback<Array<number>>): void; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：display；  API声明：function on(type: 'captureStatusChange', callback: Callback<boolean>): void;  差异内容：function on(type: 'captureStatusChange', callback: Callback<boolean>): void; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：display；  API声明：function off(type: 'captureStatusChange', callback?: Callback<boolean>): void;  差异内容：function off(type: 'captureStatusChange', callback?: Callback<boolean>): void; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：display；  API声明：function isCaptured(): boolean;  差异内容：function isCaptured(): boolean; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：display；  API声明：function getFoldDisplayMode(): FoldDisplayMode;  差异内容：function getFoldDisplayMode(): FoldDisplayMode; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：display；  API声明：function on(type: 'foldDisplayModeChange', callback: Callback<FoldDisplayMode>): void;  差异内容：function on(type: 'foldDisplayModeChange', callback: Callback<FoldDisplayMode>): void; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：display；  API声明：function off(type: 'foldDisplayModeChange', callback?: Callback<FoldDisplayMode>): void;  差异内容：function off(type: 'foldDisplayModeChange', callback?: Callback<FoldDisplayMode>): void; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：display；  API声明：function getCurrentFoldCreaseRegion(): FoldCreaseRegion;  差异内容：function getCurrentFoldCreaseRegion(): FoldCreaseRegion; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：display；  API声明： enum FoldStatus  差异内容： enum FoldStatus | api/@ohos.display.d.ts |
| 新增API | NA | 类名：FoldStatus；  API声明：FOLD\_STATUS\_UNKNOWN = 0  差异内容：FOLD\_STATUS\_UNKNOWN = 0 | api/@ohos.display.d.ts |
| 新增API | NA | 类名：FoldStatus；  API声明：FOLD\_STATUS\_EXPANDED  差异内容：FOLD\_STATUS\_EXPANDED | api/@ohos.display.d.ts |
| 新增API | NA | 类名：FoldStatus；  API声明：FOLD\_STATUS\_FOLDED  差异内容：FOLD\_STATUS\_FOLDED | api/@ohos.display.d.ts |
| 新增API | NA | 类名：FoldStatus；  API声明：FOLD\_STATUS\_HALF\_FOLDED  差异内容：FOLD\_STATUS\_HALF\_FOLDED | api/@ohos.display.d.ts |
| 新增API | NA | 类名：display；  API声明： enum FoldDisplayMode  差异内容： enum FoldDisplayMode | api/@ohos.display.d.ts |
| 新增API | NA | 类名：FoldDisplayMode；  API声明：FOLD\_DISPLAY\_MODE\_UNKNOWN = 0  差异内容：FOLD\_DISPLAY\_MODE\_UNKNOWN = 0 | api/@ohos.display.d.ts |
| 新增API | NA | 类名：FoldDisplayMode；  API声明：FOLD\_DISPLAY\_MODE\_FULL  差异内容：FOLD\_DISPLAY\_MODE\_FULL | api/@ohos.display.d.ts |
| 新增API | NA | 类名：FoldDisplayMode；  API声明：FOLD\_DISPLAY\_MODE\_MAIN  差异内容：FOLD\_DISPLAY\_MODE\_MAIN | api/@ohos.display.d.ts |
| 新增API | NA | 类名：FoldDisplayMode；  API声明：FOLD\_DISPLAY\_MODE\_SUB  差异内容：FOLD\_DISPLAY\_MODE\_SUB | api/@ohos.display.d.ts |
| 新增API | NA | 类名：FoldDisplayMode；  API声明：FOLD\_DISPLAY\_MODE\_COORDINATION  差异内容：FOLD\_DISPLAY\_MODE\_COORDINATION | api/@ohos.display.d.ts |
| 新增API | NA | 类名：display；  API声明： enum Orientation  差异内容： enum Orientation | api/@ohos.display.d.ts |
| 新增API | NA | 类名：Orientation；  API声明：PORTRAIT = 0  差异内容：PORTRAIT = 0 | api/@ohos.display.d.ts |
| 新增API | NA | 类名：Orientation；  API声明：LANDSCAPE = 1  差异内容：LANDSCAPE = 1 | api/@ohos.display.d.ts |
| 新增API | NA | 类名：Orientation；  API声明：PORTRAIT\_INVERTED = 2  差异内容：PORTRAIT\_INVERTED = 2 | api/@ohos.display.d.ts |
| 新增API | NA | 类名：Orientation；  API声明：LANDSCAPE\_INVERTED = 3  差异内容：LANDSCAPE\_INVERTED = 3 | api/@ohos.display.d.ts |
| 新增API | NA | 类名：display；  API声明： interface FoldCreaseRegion  差异内容： interface FoldCreaseRegion | api/@ohos.display.d.ts |
| 新增API | NA | 类名：FoldCreaseRegion；  API声明：readonly displayId: number;  差异内容：readonly displayId: number; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：FoldCreaseRegion；  API声明：readonly creaseRects: Array<Rect>;  差异内容：readonly creaseRects: Array<Rect>; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：Display；  API声明：orientation: Orientation;  差异内容：orientation: Orientation; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：Display；  API声明：colorSpaces: Array<colorSpaceManager.ColorSpace>;  差异内容：colorSpaces: Array<colorSpaceManager.ColorSpace>; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：Display；  API声明：hdrFormats: Array<hdrCapability.HDRFormat>;  差异内容：hdrFormats: Array<hdrCapability.HDRFormat>; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：font；  API声明： interface FontInfo  差异内容： interface FontInfo | api/@ohos.font.d.ts |
| 新增API | NA | 类名：FontInfo；  API声明：path: string;  差异内容：path: string; | api/@ohos.font.d.ts |
| 新增API | NA | 类名：FontInfo；  API声明：postScriptName: string;  差异内容：postScriptName: string; | api/@ohos.font.d.ts |
| 新增API | NA | 类名：FontInfo；  API声明：fullName: string;  差异内容：fullName: string; | api/@ohos.font.d.ts |
| 新增API | NA | 类名：FontInfo；  API声明：family: string;  差异内容：family: string; | api/@ohos.font.d.ts |
| 新增API | NA | 类名：FontInfo；  API声明：subfamily: string;  差异内容：subfamily: string; | api/@ohos.font.d.ts |
| 新增API | NA | 类名：FontInfo；  API声明：weight: number;  差异内容：weight: number; | api/@ohos.font.d.ts |
| 新增API | NA | 类名：FontInfo；  API声明：width: number;  差异内容：width: number; | api/@ohos.font.d.ts |
| 新增API | NA | 类名：FontInfo；  API声明：italic: boolean;  差异内容：italic: boolean; | api/@ohos.font.d.ts |
| 新增API | NA | 类名：FontInfo；  API声明：monoSpace: boolean;  差异内容：monoSpace: boolean; | api/@ohos.font.d.ts |
| 新增API | NA | 类名：FontInfo；  API声明：symbolic: boolean;  差异内容：symbolic: boolean; | api/@ohos.font.d.ts |
| 新增API | NA | 类名：font；  API声明： interface UIFontConfig  差异内容： interface UIFontConfig | api/@ohos.font.d.ts |
| 新增API | NA | 类名：UIFontConfig；  API声明：fontDir: Array<string>;  差异内容：fontDir: Array<string>; | api/@ohos.font.d.ts |
| 新增API | NA | 类名：UIFontConfig；  API声明：generic: Array<UIFontGenericInfo>;  差异内容：generic: Array<UIFontGenericInfo>; | api/@ohos.font.d.ts |
| 新增API | NA | 类名：UIFontConfig；  API声明：fallbackGroups: Array<UIFontFallbackGroupInfo>;  差异内容：fallbackGroups: Array<UIFontFallbackGroupInfo>; | api/@ohos.font.d.ts |
| 新增API | NA | 类名：font；  API声明： interface UIFontGenericInfo  差异内容： interface UIFontGenericInfo | api/@ohos.font.d.ts |
| 新增API | NA | 类名：UIFontGenericInfo；  API声明：family: string;  差异内容：family: string; | api/@ohos.font.d.ts |
| 新增API | NA | 类名：UIFontGenericInfo；  API声明：alias: Array<UIFontAliasInfo>;  差异内容：alias: Array<UIFontAliasInfo>; | api/@ohos.font.d.ts |
| 新增API | NA | 类名：UIFontGenericInfo；  API声明：adjust: Array<UIFontAdjustInfo>;  差异内容：adjust: Array<UIFontAdjustInfo>; | api/@ohos.font.d.ts |
| 新增API | NA | 类名：font；  API声明： interface UIFontAliasInfo  差异内容： interface UIFontAliasInfo | api/@ohos.font.d.ts |
| 新增API | NA | 类名：UIFontAliasInfo；  API声明：name: string;  差异内容：name: string; | api/@ohos.font.d.ts |
| 新增API | NA | 类名：UIFontAliasInfo；  API声明：weight: number;  差异内容：weight: number; | api/@ohos.font.d.ts |
| 新增API | NA | 类名：font；  API声明： interface UIFontAdjustInfo  差异内容： interface UIFontAdjustInfo | api/@ohos.font.d.ts |
| 新增API | NA | 类名：UIFontAdjustInfo；  API声明：weight: number;  差异内容：weight: number; | api/@ohos.font.d.ts |
| 新增API | NA | 类名：UIFontAdjustInfo；  API声明：to: number;  差异内容：to: number; | api/@ohos.font.d.ts |
| 新增API | NA | 类名：font；  API声明： interface UIFontFallbackGroupInfo  差异内容： interface UIFontFallbackGroupInfo | api/@ohos.font.d.ts |
| 新增API | NA | 类名：UIFontFallbackGroupInfo；  API声明：fontSetName: string;  差异内容：fontSetName: string; | api/@ohos.font.d.ts |
| 新增API | NA | 类名：UIFontFallbackGroupInfo；  API声明：fallback: Array<UIFontFallbackInfo>;  差异内容：fallback: Array<UIFontFallbackInfo>; | api/@ohos.font.d.ts |
| 新增API | NA | 类名：font；  API声明： interface UIFontFallbackInfo  差异内容： interface UIFontFallbackInfo | api/@ohos.font.d.ts |
| 新增API | NA | 类名：UIFontFallbackInfo；  API声明：language: string;  差异内容：language: string; | api/@ohos.font.d.ts |
| 新增API | NA | 类名：UIFontFallbackInfo；  API声明：family: string;  差异内容：family: string; | api/@ohos.font.d.ts |
| 新增API | NA | 类名：font；  API声明：function getSystemFontList(): Array<string>;  差异内容：function getSystemFontList(): Array<string>; | api/@ohos.font.d.ts |
| 新增API | NA | 类名：font；  API声明：function getFontByName(fontName: string): FontInfo;  差异内容：function getFontByName(fontName: string): FontInfo; | api/@ohos.font.d.ts |
| 新增API | NA | 类名：font；  API声明：function getUIFontConfig(): UIFontConfig;  差异内容：function getUIFontConfig(): UIFontConfig; | api/@ohos.font.d.ts |
| 新增API | NA | 类名：matrix4；  API声明： export interface Point  差异内容： export interface Point | api/@ohos.matrix4.d.ts |
| 新增API | NA | 类名：Point；  API声明：x: number;  差异内容：x: number; | api/@ohos.matrix4.d.ts |
| 新增API | NA | 类名：Point；  API声明：y: number;  差异内容：y: number; | api/@ohos.matrix4.d.ts |
| 新增API | NA | 类名：matrix4；  API声明： export interface PolyToPolyOptions  差异内容： export interface PolyToPolyOptions | api/@ohos.matrix4.d.ts |
| 新增API | NA | 类名：PolyToPolyOptions；  API声明：src: Array<Point>;  差异内容：src: Array<Point>; | api/@ohos.matrix4.d.ts |
| 新增API | NA | 类名：PolyToPolyOptions；  API声明：srcIndex?: number;  差异内容：srcIndex?: number; | api/@ohos.matrix4.d.ts |
| 新增API | NA | 类名：PolyToPolyOptions；  API声明：dst: Array<Point>;  差异内容：dst: Array<Point>; | api/@ohos.matrix4.d.ts |
| 新增API | NA | 类名：PolyToPolyOptions；  API声明：dstIndex?: number;  差异内容：dstIndex?: number; | api/@ohos.matrix4.d.ts |
| 新增API | NA | 类名：PolyToPolyOptions；  API声明：pointCount?: number;  差异内容：pointCount?: number; | api/@ohos.matrix4.d.ts |
| 新增API | NA | 类名：Matrix4Transit；  API声明：skew(x: number, y: number): Matrix4Transit;  差异内容：skew(x: number, y: number): Matrix4Transit; | api/@ohos.matrix4.d.ts |
| 新增API | NA | 类名：Matrix4Transit；  API声明：setPolyToPoly(options: PolyToPolyOptions): Matrix4Transit;  差异内容：setPolyToPoly(options: PolyToPolyOptions): Matrix4Transit; | api/@ohos.matrix4.d.ts |
| 新增API | NA | 类名：MeasureOptions；  API声明：constraintWidth?: number | string | Resource;  差异内容：constraintWidth?: number | string | Resource; | api/@ohos.measure.d.ts |
| 新增API | NA | 类名：MeasureOptions；  API声明：textAlign?: number | TextAlign;  差异内容：textAlign?: number | TextAlign; | api/@ohos.measure.d.ts |
| 新增API | NA | 类名：MeasureOptions；  API声明：overflow?: number | TextOverflow;  差异内容：overflow?: number | TextOverflow; | api/@ohos.measure.d.ts |
| 新增API | NA | 类名：MeasureOptions；  API声明：maxLines?: number;  差异内容：maxLines?: number; | api/@ohos.measure.d.ts |
| 新增API | NA | 类名：MeasureOptions；  API声明：lineHeight?: number | string | Resource;  差异内容：lineHeight?: number | string | Resource; | api/@ohos.measure.d.ts |
| 新增API | NA | 类名：MeasureOptions；  API声明：baselineOffset?: number | string;  差异内容：baselineOffset?: number | string; | api/@ohos.measure.d.ts |
| 新增API | NA | 类名：MeasureOptions；  API声明：textCase?: number | TextCase;  差异内容：textCase?: number | TextCase; | api/@ohos.measure.d.ts |
| 新增API | NA | 类名：MeasureOptions；  API声明：textIndent?: number | string;  差异内容：textIndent?: number | string; | api/@ohos.measure.d.ts |
| 新增API | NA | 类名：MeasureOptions；  API声明：wordBreak?: WordBreak;  差异内容：wordBreak?: WordBreak; | api/@ohos.measure.d.ts |
| 新增API | NA | 类名：MeasureText；  API声明：static measureTextSize(options: MeasureOptions): SizeOptions;  差异内容：static measureTextSize(options: MeasureOptions): SizeOptions; | api/@ohos.measure.d.ts |
| 新增API | NA | 类名：ShowToastOptions；  API声明：showMode?: ToastShowMode;  差异内容：showMode?: ToastShowMode; | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：ShowToastOptions；  API声明：alignment?: Alignment;  差异内容：alignment?: Alignment; | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：ShowToastOptions；  API声明：offset?: Offset;  差异内容：offset?: Offset; | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：promptAction；  API声明： export enum ToastShowMode  差异内容： export enum ToastShowMode | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：ToastShowMode；  API声明：DEFAULT = 0  差异内容：DEFAULT = 0 | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：ToastShowMode；  API声明：TOP\_MOST = 1  差异内容：TOP\_MOST = 1 | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：Button；  API声明：primary?: boolean;  差异内容：primary?: boolean; | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：ShowDialogOptions；  API声明：maskRect?: Rectangle;  差异内容：maskRect?: Rectangle; | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：ShowDialogOptions；  API声明：alignment?: DialogAlignment;  差异内容：alignment?: DialogAlignment; | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：ShowDialogOptions；  API声明：offset?: Offset;  差异内容：offset?: Offset; | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：ShowDialogOptions；  API声明：showInSubWindow?: boolean;  差异内容：showInSubWindow?: boolean; | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：ShowDialogOptions；  API声明：isModal?: boolean;  差异内容：isModal?: boolean; | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：ShowDialogOptions；  API声明：backgroundColor?: ResourceColor;  差异内容：backgroundColor?: ResourceColor; | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：ShowDialogOptions；  API声明：backgroundBlurStyle?: BlurStyle;  差异内容：backgroundBlurStyle?: BlurStyle; | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：ShowDialogOptions；  API声明：shadow?: ShadowOptions | ShadowStyle;  差异内容：shadow?: ShadowOptions | ShadowStyle; | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：promptAction；  API声明： interface BaseDialogOptions  差异内容： interface BaseDialogOptions | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：BaseDialogOptions；  API声明：maskRect?: Rectangle;  差异内容：maskRect?: Rectangle; | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：BaseDialogOptions；  API声明：alignment?: DialogAlignment;  差异内容：alignment?: DialogAlignment; | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：BaseDialogOptions；  API声明：offset?: Offset;  差异内容：offset?: Offset; | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：BaseDialogOptions；  API声明：showInSubWindow?: boolean;  差异内容：showInSubWindow?: boolean; | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：BaseDialogOptions；  API声明：isModal?: boolean;  差异内容：isModal?: boolean; | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：BaseDialogOptions；  API声明：autoCancel?: boolean;  差异内容：autoCancel?: boolean; | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：BaseDialogOptions；  API声明：transition?: TransitionEffect;  差异内容：transition?: TransitionEffect; | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：BaseDialogOptions；  API声明：maskColor?: ResourceColor;  差异内容：maskColor?: ResourceColor; | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：BaseDialogOptions；  API声明：onWillDismiss?: Callback<DismissDialogAction>;  差异内容：onWillDismiss?: Callback<DismissDialogAction>; | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：BaseDialogOptions；  API声明：onDidAppear?: () => void;  差异内容：onDidAppear?: () => void; | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：BaseDialogOptions；  API声明：onDidDisappear?: () => void;  差异内容：onDidDisappear?: () => void; | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：BaseDialogOptions；  API声明：onWillAppear?: () => void;  差异内容：onWillAppear?: () => void; | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：BaseDialogOptions；  API声明：onWillDisappear?: () => void;  差异内容：onWillDisappear?: () => void; | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：promptAction；  API声明： interface CustomDialogOptions  差异内容： interface CustomDialogOptions | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：CustomDialogOptions；  API声明：builder: CustomBuilder;  差异内容：builder: CustomBuilder; | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：CustomDialogOptions；  API声明：backgroundColor?: ResourceColor;  差异内容：backgroundColor?: ResourceColor; | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：CustomDialogOptions；  API声明：cornerRadius?: Dimension | BorderRadiuses;  差异内容：cornerRadius?: Dimension | BorderRadiuses; | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：CustomDialogOptions；  API声明：width?: Dimension;  差异内容：width?: Dimension; | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：CustomDialogOptions；  API声明：height?: Dimension;  差异内容：height?: Dimension; | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：CustomDialogOptions；  API声明：borderWidth?: Dimension | EdgeWidths;  差异内容：borderWidth?: Dimension | EdgeWidths; | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：CustomDialogOptions；  API声明：borderColor?: ResourceColor | EdgeColors;  差异内容：borderColor?: ResourceColor | EdgeColors; | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：CustomDialogOptions；  API声明：borderStyle?: BorderStyle | EdgeStyles;  差异内容：borderStyle?: BorderStyle | EdgeStyles; | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：CustomDialogOptions；  API声明：shadow?: ShadowOptions | ShadowStyle;  差异内容：shadow?: ShadowOptions | ShadowStyle; | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：CustomDialogOptions；  API声明：backgroundBlurStyle?: BlurStyle;  差异内容：backgroundBlurStyle?: BlurStyle; | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：ActionMenuOptions；  API声明：showInSubWindow?: boolean;  差异内容：showInSubWindow?: boolean; | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：ActionMenuOptions；  API声明：isModal?: boolean;  差异内容：isModal?: boolean; | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：promptAction；  API声明：function openCustomDialog(options: CustomDialogOptions): Promise<number>;  差异内容：function openCustomDialog(options: CustomDialogOptions): Promise<number>; | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：promptAction；  API声明：function closeCustomDialog(dialogId: number): void;  差异内容：function closeCustomDialog(dialogId: number): void; | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface DismissDialogAction  差异内容： declare interface DismissDialogAction | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：DismissDialogAction；  API声明：dismiss: Callback<void>;  差异内容：dismiss: Callback<void>; | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：DismissDialogAction；  API声明：reason: DismissReason;  差异内容：reason: DismissReason; | api/@ohos.promptAction.d.ts |
| 新增API | NA | 类名：router；  API声明：function back(index: number, params?: Object): void;  差异内容：function back(index: number, params?: Object): void; | api/@ohos.router.d.ts |
| 新增API | NA | 类名：RouterState；  API声明：params: Object;  差异内容：params: Object; | api/@ohos.router.d.ts |
| 新增API | NA | 类名：router；  API声明：function getStateByIndex(index: number): RouterState | undefined;  差异内容：function getStateByIndex(index: number): RouterState | undefined; | api/@ohos.router.d.ts |
| 新增API | NA | 类名：router；  API声明：function getStateByUrl(url: string): Array<RouterState>;  差异内容：function getStateByUrl(url: string): Array<RouterState>; | api/@ohos.router.d.ts |
| 新增API | NA | 类名：router；  API声明： interface NamedRouterOptions  差异内容： interface NamedRouterOptions | api/@ohos.router.d.ts |
| 新增API | NA | 类名：NamedRouterOptions；  API声明：name: string;  差异内容：name: string; | api/@ohos.router.d.ts |
| 新增API | NA | 类名：NamedRouterOptions；  API声明：params?: Object;  差异内容：params?: Object; | api/@ohos.router.d.ts |
| 新增API | NA | 类名：router；  API声明：function pushNamedRoute(options: NamedRouterOptions, callback: AsyncCallback<void>): void;  差异内容：function pushNamedRoute(options: NamedRouterOptions, callback: AsyncCallback<void>): void; | api/@ohos.router.d.ts |
| 新增API | NA | 类名：router；  API声明：function pushNamedRoute(options: NamedRouterOptions): Promise<void>;  差异内容：function pushNamedRoute(options: NamedRouterOptions): Promise<void>; | api/@ohos.router.d.ts |
| 新增API | NA | 类名：router；  API声明：function pushNamedRoute(options: NamedRouterOptions, mode: RouterMode, callback: AsyncCallback<void>): void;  差异内容：function pushNamedRoute(options: NamedRouterOptions, mode: RouterMode, callback: AsyncCallback<void>): void; | api/@ohos.router.d.ts |
| 新增API | NA | 类名：router；  API声明：function pushNamedRoute(options: NamedRouterOptions, mode: RouterMode): Promise<void>;  差异内容：function pushNamedRoute(options: NamedRouterOptions, mode: RouterMode): Promise<void>; | api/@ohos.router.d.ts |
| 新增API | NA | 类名：router；  API声明：function replaceNamedRoute(options: NamedRouterOptions, callback: AsyncCallback<void>): void;  差异内容：function replaceNamedRoute(options: NamedRouterOptions, callback: AsyncCallback<void>): void; | api/@ohos.router.d.ts |
| 新增API | NA | 类名：router；  API声明：function replaceNamedRoute(options: NamedRouterOptions): Promise<void>;  差异内容：function replaceNamedRoute(options: NamedRouterOptions): Promise<void>; | api/@ohos.router.d.ts |
| 新增API | NA | 类名：router；  API声明：function replaceNamedRoute(options: NamedRouterOptions, mode: RouterMode, callback: AsyncCallback<void>): void;  差异内容：function replaceNamedRoute(options: NamedRouterOptions, mode: RouterMode, callback: AsyncCallback<void>): void; | api/@ohos.router.d.ts |
| 新增API | NA | 类名：router；  API声明：function replaceNamedRoute(options: NamedRouterOptions, mode: RouterMode): Promise<void>;  差异内容：function replaceNamedRoute(options: NamedRouterOptions, mode: RouterMode): Promise<void>; | api/@ohos.router.d.ts |
| 新增API | NA | 类名：WindowType；  API声明：TYPE\_DIALOG  差异内容：TYPE\_DIALOG | api/@ohos.window.d.ts |
| 新增API | NA | 类名：AvoidAreaType；  API声明：TYPE\_NAVIGATION\_INDICATOR  差异内容：TYPE\_NAVIGATION\_INDICATOR | api/@ohos.window.d.ts |
| 新增API | NA | 类名：window；  API声明： enum WindowStatusType  差异内容： enum WindowStatusType | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowStatusType；  API声明：UNDEFINED = 0  差异内容：UNDEFINED = 0 | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowStatusType；  API声明：FULL\_SCREEN  差异内容：FULL\_SCREEN | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowStatusType；  API声明：MAXIMIZE  差异内容：MAXIMIZE | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowStatusType；  API声明：MINIMIZE  差异内容：MINIMIZE | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowStatusType；  API声明：FLOATING  差异内容：FLOATING | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowStatusType；  API声明：SPLIT\_SCREEN  差异内容：SPLIT\_SCREEN | api/@ohos.window.d.ts |
| 新增API | NA | 类名：SystemBarProperties；  API声明：enableStatusBarAnimation?: boolean;  差异内容：enableStatusBarAnimation?: boolean; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：SystemBarProperties；  API声明：enableNavigationBarAnimation?: boolean;  差异内容：enableNavigationBarAnimation?: boolean; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowProperties；  API声明：drawableRect: Rect;  差异内容：drawableRect: Rect; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Configuration；  API声明：decorEnabled?: boolean;  差异内容：decorEnabled?: boolean; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Configuration；  API声明：title?: string;  差异内容：title?: string; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：window；  API声明： interface WindowLimits  差异内容： interface WindowLimits | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowLimits；  API声明：maxWidth?: number;  差异内容：maxWidth?: number; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowLimits；  API声明：maxHeight?: number;  差异内容：maxHeight?: number; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowLimits；  API声明：minWidth?: number;  差异内容：minWidth?: number; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowLimits；  API声明：minHeight?: number;  差异内容：minHeight?: number; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：window；  API声明： interface TitleButtonRect  差异内容： interface TitleButtonRect | api/@ohos.window.d.ts |
| 新增API | NA | 类名：TitleButtonRect；  API声明：right: number;  差异内容：right: number; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：TitleButtonRect；  API声明：top: number;  差异内容：top: number; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：TitleButtonRect；  API声明：width: number;  差异内容：width: number; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：TitleButtonRect；  API声明：height: number;  差异内容：height: number; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：window；  API声明： interface RectChangeOptions  差异内容： interface RectChangeOptions | api/@ohos.window.d.ts |
| 新增API | NA | 类名：RectChangeOptions；  API声明：rect: Rect;  差异内容：rect: Rect; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：RectChangeOptions；  API声明：reason: RectChangeReason;  差异内容：reason: RectChangeReason; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：window；  API声明： interface AvoidAreaOptions  差异内容： interface AvoidAreaOptions | api/@ohos.window.d.ts |
| 新增API | NA | 类名：AvoidAreaOptions；  API声明：type: AvoidAreaType;  差异内容：type: AvoidAreaType; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：AvoidAreaOptions；  API声明：area: AvoidArea;  差异内容：area: AvoidArea; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：window；  API声明： enum RectChangeReason  差异内容： enum RectChangeReason | api/@ohos.window.d.ts |
| 新增API | NA | 类名：RectChangeReason；  API声明：UNDEFINED = 0  差异内容：UNDEFINED = 0 | api/@ohos.window.d.ts |
| 新增API | NA | 类名：RectChangeReason；  API声明：MAXIMIZE  差异内容：MAXIMIZE | api/@ohos.window.d.ts |
| 新增API | NA | 类名：RectChangeReason；  API声明：RECOVER  差异内容：RECOVER | api/@ohos.window.d.ts |
| 新增API | NA | 类名：RectChangeReason；  API声明：MOVE  差异内容：MOVE | api/@ohos.window.d.ts |
| 新增API | NA | 类名：RectChangeReason；  API声明：DRAG  差异内容：DRAG | api/@ohos.window.d.ts |
| 新增API | NA | 类名：RectChangeReason；  API声明：DRAG\_START  差异内容：DRAG\_START | api/@ohos.window.d.ts |
| 新增API | NA | 类名：RectChangeReason；  API声明：DRAG\_END  差异内容：DRAG\_END | api/@ohos.window.d.ts |
| 新增API | NA | 类名：window；  API声明：function shiftAppWindowFocus(sourceWindowId: number, targetWindowId: number): Promise<void>;  差异内容：function shiftAppWindowFocus(sourceWindowId: number, targetWindowId: number): Promise<void>; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Orientation；  API声明：AUTO\_ROTATION\_UNSPECIFIED = 12  差异内容：AUTO\_ROTATION\_UNSPECIFIED = 12 | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Orientation；  API声明：USER\_ROTATION\_PORTRAIT = 13  差异内容：USER\_ROTATION\_PORTRAIT = 13 | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Orientation；  API声明：USER\_ROTATION\_LANDSCAPE = 14  差异内容：USER\_ROTATION\_LANDSCAPE = 14 | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Orientation；  API声明：USER\_ROTATION\_PORTRAIT\_INVERTED = 15  差异内容：USER\_ROTATION\_PORTRAIT\_INVERTED = 15 | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Orientation；  API声明：USER\_ROTATION\_LANDSCAPE\_INVERTED = 16  差异内容：USER\_ROTATION\_LANDSCAPE\_INVERTED = 16 | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Orientation；  API声明：FOLLOW\_DESKTOP = 17  差异内容：FOLLOW\_DESKTOP = 17 | api/@ohos.window.d.ts |
| 新增API | NA | 类名：window；  API声明： enum WindowEventType  差异内容： enum WindowEventType | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowEventType；  API声明：WINDOW\_SHOWN = 1  差异内容：WINDOW\_SHOWN = 1 | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowEventType；  API声明：WINDOW\_ACTIVE = 2  差异内容：WINDOW\_ACTIVE = 2 | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowEventType；  API声明：WINDOW\_INACTIVE = 3  差异内容：WINDOW\_INACTIVE = 3 | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowEventType；  API声明：WINDOW\_HIDDEN = 4  差异内容：WINDOW\_HIDDEN = 4 | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowEventType；  API声明：WINDOW\_DESTROYED = 7  差异内容：WINDOW\_DESTROYED = 7 | api/@ohos.window.d.ts |
| 新增API | NA | 类名：window；  API声明：type SpecificSystemBar = 'status' | 'navigation' | 'navigationIndicator';  差异内容：type SpecificSystemBar = 'status' | 'navigation' | 'navigationIndicator'; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：setSpecificSystemBarEnabled(name: SpecificSystemBar, enable: boolean, enableAnimation?: boolean): Promise<void>;  差异内容：setSpecificSystemBarEnabled(name: SpecificSystemBar, enable: boolean, enableAnimation?: boolean): Promise<void>; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：getWindowSystemBarProperties(): SystemBarProperties;  差异内容：getWindowSystemBarProperties(): SystemBarProperties; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：getPreferredOrientation(): Orientation;  差异内容：getPreferredOrientation(): Orientation; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：getUIContext(): UIContext;  差异内容：getUIContext(): UIContext; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：loadContentByName(name: string, storage: LocalStorage, callback: AsyncCallback<void>): void;  差异内容：loadContentByName(name: string, storage: LocalStorage, callback: AsyncCallback<void>): void; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：loadContentByName(name: string, callback: AsyncCallback<void>): void;  差异内容：loadContentByName(name: string, callback: AsyncCallback<void>): void; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：loadContentByName(name: string, storage?: LocalStorage): Promise<void>;  差异内容：loadContentByName(name: string, storage?: LocalStorage): Promise<void>; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：on(type: 'touchOutside', callback: Callback<void>): void;  差异内容：on(type: 'touchOutside', callback: Callback<void>): void; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：off(type: 'touchOutside', callback?: Callback<void>): void;  差异内容：off(type: 'touchOutside', callback?: Callback<void>): void; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：on(type: 'windowVisibilityChange', callback: Callback<boolean>): void;  差异内容：on(type: 'windowVisibilityChange', callback: Callback<boolean>): void; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：off(type: 'windowVisibilityChange', callback?: Callback<boolean>): void;  差异内容：off(type: 'windowVisibilityChange', callback?: Callback<boolean>): void; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：on(type: 'noInteractionDetected', timeout: number, callback: Callback<void>): void;  差异内容：on(type: 'noInteractionDetected', timeout: number, callback: Callback<void>): void; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：off(type: 'noInteractionDetected', callback?: Callback<void>): void;  差异内容：off(type: 'noInteractionDetected', callback?: Callback<void>): void; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：on(type: 'dialogTargetTouch', callback: Callback<void>): void;  差异内容：on(type: 'dialogTargetTouch', callback: Callback<void>): void; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：off(type: 'dialogTargetTouch', callback?: Callback<void>): void;  差异内容：off(type: 'dialogTargetTouch', callback?: Callback<void>): void; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：on(type: 'windowEvent', callback: Callback<WindowEventType>): void;  差异内容：on(type: 'windowEvent', callback: Callback<WindowEventType>): void; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：off(type: 'windowEvent', callback?: Callback<WindowEventType>): void;  差异内容：off(type: 'windowEvent', callback?: Callback<WindowEventType>): void; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：on(type: 'windowStatusChange', callback: Callback<WindowStatusType>): void;  差异内容：on(type: 'windowStatusChange', callback: Callback<WindowStatusType>): void; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：off(type: 'windowStatusChange', callback?: Callback<WindowStatusType>): void;  差异内容：off(type: 'windowStatusChange', callback?: Callback<WindowStatusType>): void; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：setAspectRatio(ratio: number, callback: AsyncCallback<void>): void;  差异内容：setAspectRatio(ratio: number, callback: AsyncCallback<void>): void; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：setAspectRatio(ratio: number): Promise<void>;  差异内容：setAspectRatio(ratio: number): Promise<void>; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：resetAspectRatio(callback: AsyncCallback<void>): void;  差异内容：resetAspectRatio(callback: AsyncCallback<void>): void; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：resetAspectRatio(): Promise<void>;  差异内容：resetAspectRatio(): Promise<void>; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：minimize(callback: AsyncCallback<void>): void;  差异内容：minimize(callback: AsyncCallback<void>): void; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：minimize(): Promise<void>;  差异内容：minimize(): Promise<void>; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：maximize(): Promise<void>;  差异内容：maximize(): Promise<void>; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：getWindowLimits(): WindowLimits;  差异内容：getWindowLimits(): WindowLimits; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：setWindowLimits(windowLimits: WindowLimits): Promise<WindowLimits>;  差异内容：setWindowLimits(windowLimits: WindowLimits): Promise<WindowLimits>; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：keepKeyboardOnFocus(keepKeyboardFlag: boolean): void;  差异内容：keepKeyboardOnFocus(keepKeyboardFlag: boolean): void; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：recover(): Promise<void>;  差异内容：recover(): Promise<void>; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：setWindowDecorVisible(isVisible: boolean): void;  差异内容：setWindowDecorVisible(isVisible: boolean): void; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：setSubWindowModal(isModal: boolean): Promise<void>;  差异内容：setSubWindowModal(isModal: boolean): Promise<void>; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：setWindowDecorHeight(height: number): void;  差异内容：setWindowDecorHeight(height: number): void; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：getWindowDecorHeight(): number;  差异内容：getWindowDecorHeight(): number; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：getTitleButtonRect(): TitleButtonRect;  差异内容：getTitleButtonRect(): TitleButtonRect; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：enableLandscapeMultiWindow(): Promise<void>;  差异内容：enableLandscapeMultiWindow(): Promise<void>; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：disableLandscapeMultiWindow(): Promise<void>;  差异内容：disableLandscapeMultiWindow(): Promise<void>; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：on(type: 'windowTitleButtonRectChange', callback: Callback<TitleButtonRect>): void;  差异内容：on(type: 'windowTitleButtonRectChange', callback: Callback<TitleButtonRect>): void; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：off(type: 'windowTitleButtonRectChange', callback?: Callback<TitleButtonRect>): void;  差异内容：off(type: 'windowTitleButtonRectChange', callback?: Callback<TitleButtonRect>): void; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：setWindowMask(windowMask: Array<Array<number>>): Promise<void>;  差异内容：setWindowMask(windowMask: Array<Array<number>>): Promise<void>; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：on(type: 'windowRectChange', callback: Callback<RectChangeOptions>): void;  差异内容：on(type: 'windowRectChange', callback: Callback<RectChangeOptions>): void; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：off(type: 'windowRectChange', callback?: Callback<RectChangeOptions>): void;  差异内容：off(type: 'windowRectChange', callback?: Callback<RectChangeOptions>): void; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：Window；  API声明：setWindowGrayScale(grayScale: number): Promise<void>;  差异内容：setWindowGrayScale(grayScale: number): Promise<void>; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowStageEventType；  API声明：RESUMED  差异内容：RESUMED | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowStageEventType；  API声明：PAUSED  差异内容：PAUSED | api/@ohos.window.d.ts |
| 新增API | NA | 类名：window；  API声明： interface SubWindowOptions  差异内容： interface SubWindowOptions | api/@ohos.window.d.ts |
| 新增API | NA | 类名：SubWindowOptions；  API声明：title: string;  差异内容：title: string; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：SubWindowOptions；  API声明：decorEnabled: boolean;  差异内容：decorEnabled: boolean; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：SubWindowOptions；  API声明：isModal?: boolean;  差异内容：isModal?: boolean; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowStage；  API声明：createSubWindowWithOptions(name: string, options: SubWindowOptions): Promise<Window>;  差异内容：createSubWindowWithOptions(name: string, options: SubWindowOptions): Promise<Window>; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowStage；  API声明：loadContentByName(name: string, storage: LocalStorage, callback: AsyncCallback<void>): void;  差异内容：loadContentByName(name: string, storage: LocalStorage, callback: AsyncCallback<void>): void; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowStage；  API声明：loadContentByName(name: string, callback: AsyncCallback<void>): void;  差异内容：loadContentByName(name: string, callback: AsyncCallback<void>): void; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowStage；  API声明：loadContentByName(name: string, storage?: LocalStorage): Promise<void>;  差异内容：loadContentByName(name: string, storage?: LocalStorage): Promise<void>; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：WindowStage；  API声明：setDefaultDensityEnabled(enabled: boolean): void;  差异内容：setDefaultDensityEnabled(enabled: boolean): void; | api/@ohos.window.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface DismissDialogAction  差异内容： declare interface DismissDialogAction | component/action\_sheet.d.ts |
| 新增API | NA | 类名：DismissDialogAction；  API声明：dismiss: Callback<void>;  差异内容：dismiss: Callback<void>; | component/action\_sheet.d.ts |
| 新增API | NA | 类名：DismissDialogAction；  API声明：reason: DismissReason;  差异内容：reason: DismissReason; | component/action\_sheet.d.ts |
| 新增API | NA | 类名：global；  API声明： interface ActionSheetOptions  差异内容： interface ActionSheetOptions | component/action\_sheet.d.ts |
| 新增API | NA | 类名：ActionSheetOptions；  API声明：title: string | Resource;  差异内容：title: string | Resource; | component/action\_sheet.d.ts |
| 新增API | NA | 类名：ActionSheetOptions；  API声明：subtitle?: ResourceStr;  差异内容：subtitle?: ResourceStr; | component/action\_sheet.d.ts |
| 新增API | NA | 类名：ActionSheetOptions；  API声明：message: string | Resource;  差异内容：message: string | Resource; | component/action\_sheet.d.ts |
| 新增API | NA | 类名：ActionSheetOptions；  API声明：cancel?: () => void;  差异内容：cancel?: () => void; | component/action\_sheet.d.ts |
| 新增API | NA | 类名：ActionSheetOptions；  API声明：sheets: Array<SheetInfo>;  差异内容：sheets: Array<SheetInfo>; | component/action\_sheet.d.ts |
| 新增API | NA | 类名：ActionSheetOptions；  API声明：autoCancel?: boolean;  差异内容：autoCancel?: boolean; | component/action\_sheet.d.ts |
| 新增API | NA | 类名：ActionSheetOptions；  API声明：alignment?: DialogAlignment;  差异内容：alignment?: DialogAlignment; | component/action\_sheet.d.ts |
| 新增API | NA | 类名：ActionSheetOptions；  API声明：offset?: {  dx: number | string | Resource;  dy: number | string | Resource;  };  差异内容：offset?: {  dx: number | string | Resource;  dy: number | string | Resource;  }; | component/action\_sheet.d.ts |
| 新增API | NA | 类名：ActionSheetOptions；  API声明：maskRect?: Rectangle;  差异内容：maskRect?: Rectangle; | component/action\_sheet.d.ts |
| 新增API | NA | 类名：ActionSheetOptions；  API声明：showInSubWindow?: boolean;  差异内容：showInSubWindow?: boolean; | component/action\_sheet.d.ts |
| 新增API | NA | 类名：ActionSheetOptions；  API声明：isModal?: boolean;  差异内容：isModal?: boolean; | component/action\_sheet.d.ts |
| 新增API | NA | 类名：ActionSheetOptions；  API声明：backgroundColor?: ResourceColor;  差异内容：backgroundColor?: ResourceColor; | component/action\_sheet.d.ts |
| 新增API | NA | 类名：ActionSheetOptions；  API声明：backgroundBlurStyle?: BlurStyle;  差异内容：backgroundBlurStyle?: BlurStyle; | component/action\_sheet.d.ts |
| 新增API | NA | 类名：ActionSheetOptions；  API声明：onWillDismiss?: Callback<DismissDialogAction>;  差异内容：onWillDismiss?: Callback<DismissDialogAction>; | component/action\_sheet.d.ts |
| 新增API | NA | 类名：ActionSheetOptions；  API声明：transition?: TransitionEffect;  差异内容：transition?: TransitionEffect; | component/action\_sheet.d.ts |
| 新增API | NA | 类名：ActionSheetOptions；  API声明：cornerRadius?: Dimension | BorderRadiuses;  差异内容：cornerRadius?: Dimension | BorderRadiuses; | component/action\_sheet.d.ts |
| 新增API | NA | 类名：ActionSheetOptions；  API声明：width?: Dimension;  差异内容：width?: Dimension; | component/action\_sheet.d.ts |
| 新增API | NA | 类名：ActionSheetOptions；  API声明：height?: Dimension;  差异内容：height?: Dimension; | component/action\_sheet.d.ts |
| 新增API | NA | 类名：ActionSheetOptions；  API声明：borderWidth?: Dimension | EdgeWidths;  差异内容：borderWidth?: Dimension | EdgeWidths; | component/action\_sheet.d.ts |
| 新增API | NA | 类名：ActionSheetOptions；  API声明：borderColor?: ResourceColor | EdgeColors;  差异内容：borderColor?: ResourceColor | EdgeColors; | component/action\_sheet.d.ts |
| 新增API | NA | 类名：ActionSheetOptions；  API声明：borderStyle?: BorderStyle | EdgeStyles;  差异内容：borderStyle?: BorderStyle | EdgeStyles; | component/action\_sheet.d.ts |
| 新增API | NA | 类名：ActionSheetOptions；  API声明：shadow?: ShadowOptions | ShadowStyle;  差异内容：shadow?: ShadowOptions | ShadowStyle; | component/action\_sheet.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum DialogButtonDirection  差异内容： declare enum DialogButtonDirection | component/alert\_dialog.d.ts |
| 新增API | NA | 类名：DialogButtonDirection；  API声明：AUTO = 0  差异内容：AUTO = 0 | component/alert\_dialog.d.ts |
| 新增API | NA | 类名：DialogButtonDirection；  API声明：HORIZONTAL = 1  差异内容：HORIZONTAL = 1 | component/alert\_dialog.d.ts |
| 新增API | NA | 类名：DialogButtonDirection；  API声明：VERTICAL = 2  差异内容：VERTICAL = 2 | component/alert\_dialog.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface AlertDialogButtonOptions  差异内容： declare interface AlertDialogButtonOptions | component/alert\_dialog.d.ts |
| 新增API | NA | 类名：AlertDialogButtonOptions；  API声明：enabled?: boolean;  差异内容：enabled?: boolean; | component/alert\_dialog.d.ts |
| 新增API | NA | 类名：AlertDialogButtonOptions；  API声明：defaultFocus?: boolean;  差异内容：defaultFocus?: boolean; | component/alert\_dialog.d.ts |
| 新增API | NA | 类名：AlertDialogButtonOptions；  API声明：style?: DialogButtonStyle;  差异内容：style?: DialogButtonStyle; | component/alert\_dialog.d.ts |
| 新增API | NA | 类名：AlertDialogButtonOptions；  API声明：value: ResourceStr;  差异内容：value: ResourceStr; | component/alert\_dialog.d.ts |
| 新增API | NA | 类名：AlertDialogButtonOptions；  API声明：fontColor?: ResourceColor;  差异内容：fontColor?: ResourceColor; | component/alert\_dialog.d.ts |
| 新增API | NA | 类名：AlertDialogButtonOptions；  API声明：backgroundColor?: ResourceColor;  差异内容：backgroundColor?: ResourceColor; | component/alert\_dialog.d.ts |
| 新增API | NA | 类名：AlertDialogButtonOptions；  API声明：action: () => void;  差异内容：action: () => void; | component/alert\_dialog.d.ts |
| 新增API | NA | 类名：AlertDialogButtonOptions；  API声明：primary?: boolean;  差异内容：primary?: boolean; | component/alert\_dialog.d.ts |
| 新增API | NA | 类名：AlertDialogParam；  API声明：subtitle?: ResourceStr;  差异内容：subtitle?: ResourceStr; | component/alert\_dialog.d.ts |
| 新增API | NA | 类名：AlertDialogParam；  API声明：maskRect?: Rectangle;  差异内容：maskRect?: Rectangle; | component/alert\_dialog.d.ts |
| 新增API | NA | 类名：AlertDialogParam；  API声明：showInSubWindow?: boolean;  差异内容：showInSubWindow?: boolean; | component/alert\_dialog.d.ts |
| 新增API | NA | 类名：AlertDialogParam；  API声明：isModal?: boolean;  差异内容：isModal?: boolean; | component/alert\_dialog.d.ts |
| 新增API | NA | 类名：AlertDialogParam；  API声明：backgroundColor?: ResourceColor;  差异内容：backgroundColor?: ResourceColor; | component/alert\_dialog.d.ts |
| 新增API | NA | 类名：AlertDialogParam；  API声明：backgroundBlurStyle?: BlurStyle;  差异内容：backgroundBlurStyle?: BlurStyle; | component/alert\_dialog.d.ts |
| 新增API | NA | 类名：AlertDialogParam；  API声明：onWillDismiss?: Callback<DismissDialogAction>;  差异内容：onWillDismiss?: Callback<DismissDialogAction>; | component/alert\_dialog.d.ts |
| 新增API | NA | 类名：AlertDialogParam；  API声明：transition?: TransitionEffect;  差异内容：transition?: TransitionEffect; | component/alert\_dialog.d.ts |
| 新增API | NA | 类名：AlertDialogParam；  API声明：cornerRadius?: Dimension | BorderRadiuses;  差异内容：cornerRadius?: Dimension | BorderRadiuses; | component/alert\_dialog.d.ts |
| 新增API | NA | 类名：AlertDialogParam；  API声明：width?: Dimension;  差异内容：width?: Dimension; | component/alert\_dialog.d.ts |
| 新增API | NA | 类名：AlertDialogParam；  API声明：height?: Dimension;  差异内容：height?: Dimension; | component/alert\_dialog.d.ts |
| 新增API | NA | 类名：AlertDialogParam；  API声明：borderWidth?: Dimension | EdgeWidths;  差异内容：borderWidth?: Dimension | EdgeWidths; | component/alert\_dialog.d.ts |
| 新增API | NA | 类名：AlertDialogParam；  API声明：borderColor?: ResourceColor | EdgeColors;  差异内容：borderColor?: ResourceColor | EdgeColors; | component/alert\_dialog.d.ts |
| 新增API | NA | 类名：AlertDialogParam；  API声明：borderStyle?: BorderStyle | EdgeStyles;  差异内容：borderStyle?: BorderStyle | EdgeStyles; | component/alert\_dialog.d.ts |
| 新增API | NA | 类名：AlertDialogParam；  API声明：shadow?: ShadowOptions | ShadowStyle;  差异内容：shadow?: ShadowOptions | ShadowStyle; | component/alert\_dialog.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface DismissDialogAction  差异内容： declare interface DismissDialogAction | component/alert\_dialog.d.ts |
| 新增API | NA | 类名：DismissDialogAction；  API声明：dismiss: Callback<void>;  差异内容：dismiss: Callback<void>; | component/alert\_dialog.d.ts |
| 新增API | NA | 类名：DismissDialogAction；  API声明：reason: DismissReason;  差异内容：reason: DismissReason; | component/alert\_dialog.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface AlertDialogParamWithOptions  差异内容： declare interface AlertDialogParamWithOptions | component/alert\_dialog.d.ts |
| 新增API | NA | 类名：AlertDialogParamWithOptions；  API声明：buttons: Array<AlertDialogButtonOptions>;  差异内容：buttons: Array<AlertDialogButtonOptions>; | component/alert\_dialog.d.ts |
| 新增API | NA | 类名：AlertDialogParamWithOptions；  API声明：buttonDirection?: DialogButtonDirection;  差异内容：buttonDirection?: DialogButtonDirection; | component/alert\_dialog.d.ts |
| 新增API | NA | 类名：AlphabetIndexerAttribute；  API声明：popupSelectedColor(value: ResourceColor): AlphabetIndexerAttribute;  差异内容：popupSelectedColor(value: ResourceColor): AlphabetIndexerAttribute; | component/alphabet\_indexer.d.ts |
| 新增API | NA | 类名：AlphabetIndexerAttribute；  API声明：popupUnselectedColor(value: ResourceColor): AlphabetIndexerAttribute;  差异内容：popupUnselectedColor(value: ResourceColor): AlphabetIndexerAttribute; | component/alphabet\_indexer.d.ts |
| 新增API | NA | 类名：AlphabetIndexerAttribute；  API声明：popupItemBackgroundColor(value: ResourceColor): AlphabetIndexerAttribute;  差异内容：popupItemBackgroundColor(value: ResourceColor): AlphabetIndexerAttribute; | component/alphabet\_indexer.d.ts |
| 新增API | NA | 类名：AlphabetIndexerAttribute；  API声明：popupItemFont(value: Font): AlphabetIndexerAttribute;  差异内容：popupItemFont(value: Font): AlphabetIndexerAttribute; | component/alphabet\_indexer.d.ts |
| 新增API | NA | 类名：AlphabetIndexerAttribute；  API声明：autoCollapse(value: boolean): AlphabetIndexerAttribute;  差异内容：autoCollapse(value: boolean): AlphabetIndexerAttribute; | component/alphabet\_indexer.d.ts |
| 新增API | NA | 类名：AlphabetIndexerAttribute；  API声明：popupItemBorderRadius(value: number): AlphabetIndexerAttribute;  差异内容：popupItemBorderRadius(value: number): AlphabetIndexerAttribute; | component/alphabet\_indexer.d.ts |
| 新增API | NA | 类名：AlphabetIndexerAttribute；  API声明：itemBorderRadius(value: number): AlphabetIndexerAttribute;  差异内容：itemBorderRadius(value: number): AlphabetIndexerAttribute; | component/alphabet\_indexer.d.ts |
| 新增API | NA | 类名：AlphabetIndexerAttribute；  API声明：popupBackgroundBlurStyle(value: BlurStyle): AlphabetIndexerAttribute;  差异内容：popupBackgroundBlurStyle(value: BlurStyle): AlphabetIndexerAttribute; | component/alphabet\_indexer.d.ts |
| 新增API | NA | 类名：AlphabetIndexerAttribute；  API声明：popupTitleBackground(value: ResourceColor): AlphabetIndexerAttribute;  差异内容：popupTitleBackground(value: ResourceColor): AlphabetIndexerAttribute; | component/alphabet\_indexer.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type Initializer<T> = () => T;  差异内容：declare type Initializer<T> = () => T; | api/arkui/AttributeUpdater.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class AttributeUpdater  差异内容： export declare class AttributeUpdater | api/arkui/AttributeUpdater.d.ts |
| 新增API | NA | 类名：AttributeUpdater；  API声明：applyNormalAttribute?(instance: T): void;  差异内容：applyNormalAttribute?(instance: T): void; | api/arkui/AttributeUpdater.d.ts |
| 新增API | NA | 类名：AttributeUpdater；  API声明：initializeModifier(instance: T): void;  差异内容：initializeModifier(instance: T): void; | api/arkui/AttributeUpdater.d.ts |
| 新增API | NA | 类名：AttributeUpdater；  API声明：updateConstructorParams: C;  差异内容：updateConstructorParams: C; | api/arkui/AttributeUpdater.d.ts |
| 新增API | NA | 类名：BadgeStyle；  API声明：borderColor?: ResourceColor;  差异内容：borderColor?: ResourceColor; | component/badge.d.ts |
| 新增API | NA | 类名：BadgeStyle；  API声明：borderWidth?: Length;  差异内容：borderWidth?: Length; | component/badge.d.ts |
| 新增API | NA | 类名：BadgeStyle；  API声明：fontWeight?: number | FontWeight | string;  差异内容：fontWeight?: number | FontWeight | string; | component/badge.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum ButtonStyleMode  差异内容： declare enum ButtonStyleMode | component/button.d.ts |
| 新增API | NA | 类名：ButtonStyleMode；  API声明：NORMAL = 0  差异内容：NORMAL = 0 | component/button.d.ts |
| 新增API | NA | 类名：ButtonStyleMode；  API声明：EMPHASIZED = 1  差异内容：EMPHASIZED = 1 | component/button.d.ts |
| 新增API | NA | 类名：ButtonStyleMode；  API声明：TEXTUAL = 2  差异内容：TEXTUAL = 2 | component/button.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum ButtonRole  差异内容： declare enum ButtonRole | component/button.d.ts |
| 新增API | NA | 类名：ButtonRole；  API声明：NORMAL = 0  差异内容：NORMAL = 0 | component/button.d.ts |
| 新增API | NA | 类名：ButtonRole；  API声明：ERROR = 1  差异内容：ERROR = 1 | component/button.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type ButtonTriggerClickCallback = (xPos: number, yPos: number) => void;  差异内容：declare type ButtonTriggerClickCallback = (xPos: number, yPos: number) => void; | component/button.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface ButtonConfiguration  差异内容： declare interface ButtonConfiguration | component/button.d.ts |
| 新增API | NA | 类名：ButtonConfiguration；  API声明：label: string;  差异内容：label: string; | component/button.d.ts |
| 新增API | NA | 类名：ButtonConfiguration；  API声明：pressed: boolean;  差异内容：pressed: boolean; | component/button.d.ts |
| 新增API | NA | 类名：ButtonConfiguration；  API声明：triggerClick: ButtonTriggerClickCallback;  差异内容：triggerClick: ButtonTriggerClickCallback; | component/button.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum ControlSize  差异内容： declare enum ControlSize | component/button.d.ts |
| 新增API | NA | 类名：ControlSize；  API声明：SMALL = 'small'  差异内容：SMALL = 'small' | component/button.d.ts |
| 新增API | NA | 类名：ControlSize；  API声明：NORMAL = 'normal'  差异内容：NORMAL = 'normal' | component/button.d.ts |
| 新增API | NA | 类名：ButtonOptions；  API声明：buttonStyle?: ButtonStyleMode;  差异内容：buttonStyle?: ButtonStyleMode; | component/button.d.ts |
| 新增API | NA | 类名：ButtonOptions；  API声明：controlSize?: ControlSize;  差异内容：controlSize?: ControlSize; | component/button.d.ts |
| 新增API | NA | 类名：ButtonOptions；  API声明：role?: ButtonRole;  差异内容：role?: ButtonRole; | component/button.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface LabelStyle  差异内容： declare interface LabelStyle | component/button.d.ts |
| 新增API | NA | 类名：LabelStyle；  API声明：overflow?: TextOverflow;  差异内容：overflow?: TextOverflow; | component/button.d.ts |
| 新增API | NA | 类名：LabelStyle；  API声明：maxLines?: number;  差异内容：maxLines?: number; | component/button.d.ts |
| 新增API | NA | 类名：LabelStyle；  API声明：minFontSize?: number | ResourceStr;  差异内容：minFontSize?: number | ResourceStr; | component/button.d.ts |
| 新增API | NA | 类名：LabelStyle；  API声明：maxFontSize?: number | ResourceStr;  差异内容：maxFontSize?: number | ResourceStr; | component/button.d.ts |
| 新增API | NA | 类名：LabelStyle；  API声明：heightAdaptivePolicy?: TextHeightAdaptivePolicy;  差异内容：heightAdaptivePolicy?: TextHeightAdaptivePolicy; | component/button.d.ts |
| 新增API | NA | 类名：LabelStyle；  API声明：font?: Font;  差异内容：font?: Font; | component/button.d.ts |
| 新增API | NA | 类名：ButtonAttribute；  API声明：buttonStyle(value: ButtonStyleMode): ButtonAttribute;  差异内容：buttonStyle(value: ButtonStyleMode): ButtonAttribute; | component/button.d.ts |
| 新增API | NA | 类名：ButtonAttribute；  API声明：controlSize(value: ControlSize): ButtonAttribute;  差异内容：controlSize(value: ControlSize): ButtonAttribute; | component/button.d.ts |
| 新增API | NA | 类名：ButtonAttribute；  API声明：role(value: ButtonRole): ButtonAttribute;  差异内容：role(value: ButtonRole): ButtonAttribute; | component/button.d.ts |
| 新增API | NA | 类名：ButtonAttribute；  API声明：contentModifier(modifier: ContentModifier<ButtonConfiguration>): ButtonAttribute;  差异内容：contentModifier(modifier: ContentModifier<ButtonConfiguration>): ButtonAttribute; | component/button.d.ts |
| 新增API | NA | 类名：ButtonAttribute；  API声明：labelStyle(value: LabelStyle): ButtonAttribute;  差异内容：labelStyle(value: LabelStyle): ButtonAttribute; | component/button.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type DrawingCanvas = import('../api/@ohos.graphics.drawing').default.Canvas;  差异内容：declare type DrawingCanvas = import('../api/@ohos.graphics.drawing').default.Canvas; | component/canvas.d.ts |
| 新增API | NA | 类名：CanvasPattern；  API声明：setTransform(transform?: Matrix2D): void;  差异内容：setTransform(transform?: Matrix2D): void; | component/canvas.d.ts |
| 新增API | NA | 类名：CanvasRenderer；  API声明：createConicGradient(startAngle: number, x: number, y: number): CanvasGradient;  差异内容：createConicGradient(startAngle: number, x: number, y: number): CanvasGradient; | component/canvas.d.ts |
| 新增API | NA | 类名：CanvasRenderer；  API声明：saveLayer(): void;  差异内容：saveLayer(): void; | component/canvas.d.ts |
| 新增API | NA | 类名：CanvasRenderer；  API声明：restoreLayer(): void;  差异内容：restoreLayer(): void; | component/canvas.d.ts |
| 新增API | NA | 类名：CanvasRenderer；  API声明：reset(): void;  差异内容：reset(): void; | component/canvas.d.ts |
| 新增API | NA | 类名：CanvasRenderingContext2D；  API声明：startImageAnalyzer(config: ImageAnalyzerConfig): Promise<void>;  差异内容：startImageAnalyzer(config: ImageAnalyzerConfig): Promise<void>; | component/canvas.d.ts |
| 新增API | NA | 类名：CanvasRenderingContext2D；  API声明：stopImageAnalyzer(): void;  差异内容：stopImageAnalyzer(): void; | component/canvas.d.ts |
| 新增API | NA | 类名：OffscreenCanvas；  API声明：getContext(contextType: "2d", options?: RenderingContextSettings): OffscreenCanvasRenderingContext2D;  差异内容：getContext(contextType: "2d", options?: RenderingContextSettings): OffscreenCanvasRenderingContext2D; | component/canvas.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface Size  差异内容： declare interface Size | component/canvas.d.ts |
| 新增API | NA | 类名：Size；  API声明：width: number;  差异内容：width: number; | component/canvas.d.ts |
| 新增API | NA | 类名：Size；  API声明：height: number;  差异内容：height: number; | component/canvas.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class DrawingRenderingContext  差异内容： declare class DrawingRenderingContext | component/canvas.d.ts |
| 新增API | NA | 类名：DrawingRenderingContext；  API声明：invalidate(): void;  差异内容：invalidate(): void; | component/canvas.d.ts |
| 新增API | NA | 类名：CanvasAttribute；  API声明：enableAnalyzer(enable: boolean): CanvasAttribute;  差异内容：enableAnalyzer(enable: boolean): CanvasAttribute; | component/canvas.d.ts |
| 新增API | NA | 类名：CheckboxOptions；  API声明：indicatorBuilder?: CustomBuilder;  差异内容：indicatorBuilder?: CustomBuilder; | component/checkbox.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface CheckBoxConfiguration  差异内容： declare interface CheckBoxConfiguration | component/checkbox.d.ts |
| 新增API | NA | 类名：CheckBoxConfiguration；  API声明：name: string;  差异内容：name: string; | component/checkbox.d.ts |
| 新增API | NA | 类名：CheckBoxConfiguration；  API声明：selected: boolean;  差异内容：selected: boolean; | component/checkbox.d.ts |
| 新增API | NA | 类名：CheckBoxConfiguration；  API声明：triggerChange: Callback<boolean>;  差异内容：triggerChange: Callback<boolean>; | component/checkbox.d.ts |
| 新增API | NA | 类名：CheckboxAttribute；  API声明：shape(value: CheckBoxShape): CheckboxAttribute;  差异内容：shape(value: CheckBoxShape): CheckboxAttribute; | component/checkbox.d.ts |
| 新增API | NA | 类名：CheckboxAttribute；  API声明：unselectedColor(value: ResourceColor): CheckboxAttribute;  差异内容：unselectedColor(value: ResourceColor): CheckboxAttribute; | component/checkbox.d.ts |
| 新增API | NA | 类名：CheckboxAttribute；  API声明：mark(value: MarkStyle): CheckboxAttribute;  差异内容：mark(value: MarkStyle): CheckboxAttribute; | component/checkbox.d.ts |
| 新增API | NA | 类名：CheckboxAttribute；  API声明：contentModifier(modifier: ContentModifier<CheckBoxConfiguration>): CheckboxAttribute;  差异内容：contentModifier(modifier: ContentModifier<CheckBoxConfiguration>): CheckboxAttribute; | component/checkbox.d.ts |
| 新增API | NA | 类名：CheckboxGroupAttribute；  API声明：unselectedColor(value: ResourceColor): CheckboxGroupAttribute;  差异内容：unselectedColor(value: ResourceColor): CheckboxGroupAttribute; | component/checkboxgroup.d.ts |
| 新增API | NA | 类名：CheckboxGroupAttribute；  API声明：mark(value: MarkStyle): CheckboxGroupAttribute;  差异内容：mark(value: MarkStyle): CheckboxGroupAttribute; | component/checkboxgroup.d.ts |
| 新增API | NA | 类名：CheckboxGroupAttribute；  API声明：checkboxShape(value: CheckBoxShape): CheckboxGroupAttribute;  差异内容：checkboxShape(value: CheckBoxShape): CheckboxGroupAttribute; | component/checkboxgroup.d.ts |
| 新增API | NA | 类名：global；  API声明： interface ColumnSplitDividerStyle  差异内容： interface ColumnSplitDividerStyle | component/column\_split.d.ts |
| 新增API | NA | 类名：ColumnSplitDividerStyle；  API声明：startMargin?: Dimension;  差异内容：startMargin?: Dimension; | component/column\_split.d.ts |
| 新增API | NA | 类名：ColumnSplitDividerStyle；  API声明：endMargin?: Dimension;  差异内容：endMargin?: Dimension; | component/column\_split.d.ts |
| 新增API | NA | 类名：ColumnSplitAttribute；  API声明：divider(value: ColumnSplitDividerStyle | null): ColumnSplitAttribute;  差异内容：divider(value: ColumnSplitDividerStyle | null): ColumnSplitAttribute; | component/column\_split.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：borderStyle(value: BorderStyle | EdgeStyles): T;  差异内容：borderStyle(value: BorderStyle | EdgeStyles): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：borderWidth(value: Length | EdgeWidths | LocalizedEdgeWidths): T;  差异内容：borderWidth(value: Length | EdgeWidths | LocalizedEdgeWidths): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：borderColor(value: ResourceColor | EdgeColors | LocalizedEdgeColors): T;  差异内容：borderColor(value: ResourceColor | EdgeColors | LocalizedEdgeColors): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：borderRadius(value: Length | BorderRadiuses | LocalizedBorderRadiuses): T;  差异内容：borderRadius(value: Length | BorderRadiuses | LocalizedBorderRadiuses): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：clip(value: boolean): T;  差异内容：clip(value: boolean): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：mask(value: ProgressMask): T;  差异内容：mask(value: ProgressMask): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：mask(value: CircleAttribute | EllipseAttribute | PathAttribute | RectAttribute | ProgressMask): T;  差异内容：mask(value: CircleAttribute | EllipseAttribute | PathAttribute | RectAttribute | ProgressMask): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：geometryTransition(id: string, options?: GeometryTransitionOptions): T;  差异内容：geometryTransition(id: string, options?: GeometryTransitionOptions): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：bindMenu(content: Array<MenuElement> | CustomBuilder, options?: MenuOptions): T;  差异内容：bindMenu(content: Array<MenuElement> | CustomBuilder, options?: MenuOptions): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：bindMenu(isShow: boolean, content: Array<MenuElement> | CustomBuilder, options?: MenuOptions): T;  差异内容：bindMenu(isShow: boolean, content: Array<MenuElement> | CustomBuilder, options?: MenuOptions): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：bindContextMenu(content: CustomBuilder, responseType: ResponseType, options?: ContextMenuOptions): T;  差异内容：bindContextMenu(content: CustomBuilder, responseType: ResponseType, options?: ContextMenuOptions): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：bindContextMenu(isShown: boolean, content: CustomBuilder, options?: ContextMenuOptions): T;  差异内容：bindContextMenu(isShown: boolean, content: CustomBuilder, options?: ContextMenuOptions): T; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface ComponentOptions  差异内容： declare interface ComponentOptions | component/common.d.ts |
| 新增API | NA | 类名：ComponentOptions；  API声明：freezeWhenInactive: boolean;  差异内容：freezeWhenInactive: boolean; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface InputCounterOptions  差异内容： declare interface InputCounterOptions | component/common.d.ts |
| 新增API | NA | 类名：InputCounterOptions；  API声明：thresholdPercentage?: number;  差异内容：thresholdPercentage?: number; | component/common.d.ts |
| 新增API | NA | 类名：InputCounterOptions；  API声明：highlightBorder?: boolean;  差异内容：highlightBorder?: boolean; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface TextDecorationOptions  差异内容： declare interface TextDecorationOptions | component/common.d.ts |
| 新增API | NA | 类名：TextDecorationOptions；  API声明：type: TextDecorationType;  差异内容：type: TextDecorationType; | component/common.d.ts |
| 新增API | NA | 类名：TextDecorationOptions；  API声明：color?: ResourceColor;  差异内容：color?: ResourceColor; | component/common.d.ts |
| 新增API | NA | 类名：TextDecorationOptions；  API声明：style?: TextDecorationStyle;  差异内容：style?: TextDecorationStyle; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const ComponentV2: ClassDecorator;  差异内容：declare const ComponentV2: ClassDecorator; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface EntryOptions  差异内容： declare interface EntryOptions | component/common.d.ts |
| 新增API | NA | 类名：EntryOptions；  API声明：routeName?: string;  差异内容：routeName?: string; | component/common.d.ts |
| 新增API | NA | 类名：EntryOptions；  API声明：storage?: LocalStorage;  差异内容：storage?: LocalStorage; | component/common.d.ts |
| 新增API | NA | 类名：EntryOptions；  API声明：useSharedStorage?: boolean;  差异内容：useSharedStorage?: boolean; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const ObservedV2: ClassDecorator;  差异内容：declare const ObservedV2: ClassDecorator; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const Require: PropertyDecorator;  差异内容：declare const Require: PropertyDecorator; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const Local: PropertyDecorator;  差异内容：declare const Local: PropertyDecorator; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const Param: PropertyDecorator;  差异内容：declare const Param: PropertyDecorator; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const Once: PropertyDecorator;  差异内容：declare const Once: PropertyDecorator; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const Event: PropertyDecorator;  差异内容：declare const Event: PropertyDecorator; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const Track: PropertyDecorator;  差异内容：declare const Track: PropertyDecorator; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const Trace: PropertyDecorator;  差异内容：declare const Trace: PropertyDecorator; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface ProvideOptions  差异内容： declare interface ProvideOptions | component/common.d.ts |
| 新增API | NA | 类名：ProvideOptions；  API声明：allowOverride?: string;  差异内容：allowOverride?: string; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const Provider: (aliasName?: string) => PropertyDecorator;  差异内容：declare const Provider: (aliasName?: string) => PropertyDecorator; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const Consumer: (aliasName?: string) => PropertyDecorator;  差异内容：declare const Consumer: (aliasName?: string) => PropertyDecorator; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const Computed: MethodDecorator;  差异内容：declare const Computed: MethodDecorator; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const AnimatableExtend: MethodDecorator & ((value: Object) => MethodDecorator);  差异内容：declare const AnimatableExtend: MethodDecorator & ((value: Object) => MethodDecorator); | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const Monitor: MonitorDecorator;  差异内容：declare const Monitor: MonitorDecorator; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type MonitorDecorator = (value: string, ...args: string[]) => MethodDecorator;  差异内容：declare type MonitorDecorator = (value: string, ...args: string[]) => MethodDecorator; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface IMonitor  差异内容： declare interface IMonitor | component/common.d.ts |
| 新增API | NA | 类名：IMonitor；  API声明：dirty: Array<string>;  差异内容：dirty: Array<string>; | component/common.d.ts |
| 新增API | NA | 类名：IMonitor；  API声明：value<T>(path?: string): IMonitorValue<T> | undefined;  差异内容：value<T>(path?: string): IMonitorValue<T> | undefined; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface IMonitorValue  差异内容： declare interface IMonitorValue | component/common.d.ts |
| 新增API | NA | 类名：IMonitorValue；  API声明：before: T;  差异内容：before: T; | component/common.d.ts |
| 新增API | NA | 类名：IMonitorValue；  API声明：now: T;  差异内容：now: T; | component/common.d.ts |
| 新增API | NA | 类名：IMonitorValue；  API声明：path: string;  差异内容：path: string; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface AnimatableArithmetic  差异内容： declare interface AnimatableArithmetic | component/common.d.ts |
| 新增API | NA | 类名：AnimatableArithmetic；  API声明：plus(rhs: AnimatableArithmetic<T>): AnimatableArithmetic<T>;  差异内容：plus(rhs: AnimatableArithmetic<T>): AnimatableArithmetic<T>; | component/common.d.ts |
| 新增API | NA | 类名：AnimatableArithmetic；  API声明：subtract(rhs: AnimatableArithmetic<T>): AnimatableArithmetic<T>;  差异内容：subtract(rhs: AnimatableArithmetic<T>): AnimatableArithmetic<T>; | component/common.d.ts |
| 新增API | NA | 类名：AnimatableArithmetic；  API声明：multiply(scale: number): AnimatableArithmetic<T>;  差异内容：multiply(scale: number): AnimatableArithmetic<T>; | component/common.d.ts |
| 新增API | NA | 类名：AnimatableArithmetic；  API声明：equals(rhs: AnimatableArithmetic<T>): boolean;  差异内容：equals(rhs: AnimatableArithmetic<T>): boolean; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const Sendable: ClassDecorator;  差异内容：declare const Sendable: ClassDecorator; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const Reusable: ClassDecorator;  差异内容：declare const Reusable: ClassDecorator; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface ExpectedFrameRateRange  差异内容： declare interface ExpectedFrameRateRange | component/common.d.ts |
| 新增API | NA | 类名：ExpectedFrameRateRange；  API声明：min: number;  差异内容：min: number; | component/common.d.ts |
| 新增API | NA | 类名：ExpectedFrameRateRange；  API声明：max: number;  差异内容：max: number; | component/common.d.ts |
| 新增API | NA | 类名：ExpectedFrameRateRange；  API声明：expected: number;  差异内容：expected: number; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum FinishCallbackType  差异内容： declare enum FinishCallbackType | component/common.d.ts |
| 新增API | NA | 类名：FinishCallbackType；  API声明：REMOVED = 0  差异内容：REMOVED = 0 | component/common.d.ts |
| 新增API | NA | 类名：FinishCallbackType；  API声明：LOGICALLY = 1  差异内容：LOGICALLY = 1 | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum TouchTestStrategy  差异内容： declare enum TouchTestStrategy | component/common.d.ts |
| 新增API | NA | 类名：TouchTestStrategy；  API声明：DEFAULT = 0  差异内容：DEFAULT = 0 | component/common.d.ts |
| 新增API | NA | 类名：TouchTestStrategy；  API声明：FORWARD\_COMPETITION = 1  差异内容：FORWARD\_COMPETITION = 1 | component/common.d.ts |
| 新增API | NA | 类名：TouchTestStrategy；  API声明：FORWARD = 2  差异内容：FORWARD = 2 | component/common.d.ts |
| 新增API | NA | 类名：AnimateParam；  API声明：finishCallbackType?: FinishCallbackType;  差异内容：finishCallbackType?: FinishCallbackType; | component/common.d.ts |
| 新增API | NA | 类名：AnimateParam；  API声明：expectedFrameRateRange?: ExpectedFrameRateRange;  差异内容：expectedFrameRateRange?: ExpectedFrameRateRange; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface GeometryTransitionOptions  差异内容： declare interface GeometryTransitionOptions | component/common.d.ts |
| 新增API | NA | 类名：GeometryTransitionOptions；  API声明：follow?: boolean;  差异内容：follow?: boolean; | component/common.d.ts |
| 新增API | NA | 类名：AlignRuleOption；  API声明：bias?: Bias;  差异内容：bias?: Bias; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum ChainStyle  差异内容： declare enum ChainStyle | component/common.d.ts |
| 新增API | NA | 类名：ChainStyle；  API声明：SPREAD  差异内容：SPREAD | component/common.d.ts |
| 新增API | NA | 类名：ChainStyle；  API声明：SPREAD\_INSIDE  差异内容：SPREAD\_INSIDE | component/common.d.ts |
| 新增API | NA | 类名：ChainStyle；  API声明：PACKED  差异内容：PACKED | component/common.d.ts |
| 新增API | NA | 类名：RotateOptions；  API声明：centerZ?: number;  差异内容：centerZ?: number; | component/common.d.ts |
| 新增API | NA | 类名：RotateOptions；  API声明：perspective?: number;  差异内容：perspective?: number; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum TransitionEdge  差异内容： declare enum TransitionEdge | component/common.d.ts |
| 新增API | NA | 类名：TransitionEdge；  API声明：TOP  差异内容：TOP | component/common.d.ts |
| 新增API | NA | 类名：TransitionEdge；  API声明：BOTTOM  差异内容：BOTTOM | component/common.d.ts |
| 新增API | NA | 类名：TransitionEdge；  API声明：START  差异内容：START | component/common.d.ts |
| 新增API | NA | 类名：TransitionEdge；  API声明：END  差异内容：END | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type TransitionEffects = {  identity: undefined;  opacity: number;  slideSwitch: undefined;  move: TransitionEdge;  translate: TranslateOptions;  rotate: RotateOptions;  scale: ScaleOptions;  asymmetric: {  appear: TransitionEffect;  disappear: TransitionEffect;  };  };  差异内容：declare type TransitionEffects = {  identity: undefined;  opacity: number;  slideSwitch: undefined;  move: TransitionEdge;  translate: TranslateOptions;  rotate: RotateOptions;  scale: ScaleOptions;  asymmetric: {  appear: TransitionEffect;  disappear: TransitionEffect;  };  }; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class DrawModifier  差异内容： declare class DrawModifier | component/common.d.ts |
| 新增API | NA | 类名：DrawModifier；  API声明：drawBehind?(drawContext: DrawContext): void;  差异内容：drawBehind?(drawContext: DrawContext): void; | component/common.d.ts |
| 新增API | NA | 类名：DrawModifier；  API声明：drawContent?(drawContext: DrawContext): void;  差异内容：drawContent?(drawContext: DrawContext): void; | component/common.d.ts |
| 新增API | NA | 类名：DrawModifier；  API声明：drawFront?(drawContext: DrawContext): void;  差异内容：drawFront?(drawContext: DrawContext): void; | component/common.d.ts |
| 新增API | NA | 类名：DrawModifier；  API声明：invalidate(): void;  差异内容：invalidate(): void; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class TransitionEffect  差异内容： declare class TransitionEffect | component/common.d.ts |
| 新增API | NA | 类名：TransitionEffect；  API声明：static readonly IDENTITY: TransitionEffect<"identity">;  差异内容：static readonly IDENTITY: TransitionEffect<"identity">; | component/common.d.ts |
| 新增API | NA | 类名：TransitionEffect；  API声明：static readonly OPACITY: TransitionEffect<"opacity">;  差异内容：static readonly OPACITY: TransitionEffect<"opacity">; | component/common.d.ts |
| 新增API | NA | 类名：TransitionEffect；  API声明：static readonly SLIDE: TransitionEffect<"asymmetric", {  appear: TransitionEffect<"move", TransitionEdge>;  disappear: TransitionEffect<"move", TransitionEdge>;  }>;  差异内容：static readonly SLIDE: TransitionEffect<"asymmetric", {  appear: TransitionEffect<"move", TransitionEdge>;  disappear: TransitionEffect<"move", TransitionEdge>;  }>; | component/common.d.ts |
| 新增API | NA | 类名：TransitionEffect；  API声明：static readonly SLIDE\_SWITCH: TransitionEffect<"slideSwitch">;  差异内容：static readonly SLIDE\_SWITCH: TransitionEffect<"slideSwitch">; | component/common.d.ts |
| 新增API | NA | 类名：TransitionEffect；  API声明：static translate(options: TranslateOptions): TransitionEffect<"translate">;  差异内容：static translate(options: TranslateOptions): TransitionEffect<"translate">; | component/common.d.ts |
| 新增API | NA | 类名：TransitionEffect；  API声明：static rotate(options: RotateOptions): TransitionEffect<"rotate">;  差异内容：static rotate(options: RotateOptions): TransitionEffect<"rotate">; | component/common.d.ts |
| 新增API | NA | 类名：TransitionEffect；  API声明：static scale(options: ScaleOptions): TransitionEffect<"scale">;  差异内容：static scale(options: ScaleOptions): TransitionEffect<"scale">; | component/common.d.ts |
| 新增API | NA | 类名：TransitionEffect；  API声明：static opacity(alpha: number): TransitionEffect<"opacity">;  差异内容：static opacity(alpha: number): TransitionEffect<"opacity">; | component/common.d.ts |
| 新增API | NA | 类名：TransitionEffect；  API声明：static move(edge: TransitionEdge): TransitionEffect<"move">;  差异内容：static move(edge: TransitionEdge): TransitionEffect<"move">; | component/common.d.ts |
| 新增API | NA | 类名：TransitionEffect；  API声明：static asymmetric(appear: TransitionEffect, disappear: TransitionEffect): TransitionEffect<"asymmetric">;  差异内容：static asymmetric(appear: TransitionEffect, disappear: TransitionEffect): TransitionEffect<"asymmetric">; | component/common.d.ts |
| 新增API | NA | 类名：TransitionEffect；  API声明：animation(value: AnimateParam): TransitionEffect;  差异内容：animation(value: AnimateParam): TransitionEffect; | component/common.d.ts |
| 新增API | NA | 类名：TransitionEffect；  API声明：combine(transitionEffect: TransitionEffect): TransitionEffect;  差异内容：combine(transitionEffect: TransitionEffect): TransitionEffect; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum PreDragStatus  差异内容： declare enum PreDragStatus | component/common.d.ts |
| 新增API | NA | 类名：PreDragStatus；  API声明：ACTION\_DETECTING\_STATUS = 0  差异内容：ACTION\_DETECTING\_STATUS = 0 | component/common.d.ts |
| 新增API | NA | 类名：PreDragStatus；  API声明：READY\_TO\_TRIGGER\_DRAG\_ACTION = 1  差异内容：READY\_TO\_TRIGGER\_DRAG\_ACTION = 1 | component/common.d.ts |
| 新增API | NA | 类名：PreDragStatus；  API声明：PREVIEW\_LIFT\_STARTED = 2  差异内容：PREVIEW\_LIFT\_STARTED = 2 | component/common.d.ts |
| 新增API | NA | 类名：PreDragStatus；  API声明：PREVIEW\_LIFT\_FINISHED = 3  差异内容：PREVIEW\_LIFT\_FINISHED = 3 | component/common.d.ts |
| 新增API | NA | 类名：PreDragStatus；  API声明：PREVIEW\_LANDING\_STARTED = 4  差异内容：PREVIEW\_LANDING\_STARTED = 4 | component/common.d.ts |
| 新增API | NA | 类名：PreDragStatus；  API声明：PREVIEW\_LANDING\_FINISHED = 5  差异内容：PREVIEW\_LANDING\_FINISHED = 5 | component/common.d.ts |
| 新增API | NA | 类名：PreDragStatus；  API声明：ACTION\_CANCELED\_BEFORE\_DRAG = 6  差异内容：ACTION\_CANCELED\_BEFORE\_DRAG = 6 | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare function animateToImmediately(value: AnimateParam, event: () => void): void;  差异内容：declare function animateToImmediately(value: AnimateParam, event: () => void): void; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type PointerStyle = import('../api/@ohos.multimodalInput.pointer').default.PointerStyle;  差异内容：declare type PointerStyle = import('../api/@ohos.multimodalInput.pointer').default.PointerStyle; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare namespace cursorControl  差异内容： declare namespace cursorControl | component/common.d.ts |
| 新增API | NA | 类名：cursorControl；  API声明：function setCursor(value: PointerStyle): void;  差异内容：function setCursor(value: PointerStyle): void; | component/common.d.ts |
| 新增API | NA | 类名：cursorControl；  API声明：function restoreDefault(): void;  差异内容：function restoreDefault(): void; | component/common.d.ts |
| 新增API | NA | 类名：SourceTool；  API声明：Finger  差异内容：Finger | component/common.d.ts |
| 新增API | NA | 类名：SourceTool；  API声明：Pen  差异内容：Pen | component/common.d.ts |
| 新增API | NA | 类名：SourceTool；  API声明：MOUSE  差异内容：MOUSE | component/common.d.ts |
| 新增API | NA | 类名：SourceTool；  API声明：TOUCHPAD  差异内容：TOUCHPAD | component/common.d.ts |
| 新增API | NA | 类名：SourceTool；  API声明：JOYSTICK  差异内容：JOYSTICK | component/common.d.ts |
| 新增API | NA | 类名：BlurStyle；  API声明：BACKGROUND\_THIN  差异内容：BACKGROUND\_THIN | component/common.d.ts |
| 新增API | NA | 类名：BlurStyle；  API声明：BACKGROUND\_REGULAR  差异内容：BACKGROUND\_REGULAR | component/common.d.ts |
| 新增API | NA | 类名：BlurStyle；  API声明：BACKGROUND\_THICK  差异内容：BACKGROUND\_THICK | component/common.d.ts |
| 新增API | NA | 类名：BlurStyle；  API声明：BACKGROUND\_ULTRA\_THICK  差异内容：BACKGROUND\_ULTRA\_THICK | component/common.d.ts |
| 新增API | NA | 类名：BlurStyle；  API声明：NONE  差异内容：NONE | component/common.d.ts |
| 新增API | NA | 类名：BlurStyle；  API声明：COMPONENT\_ULTRA\_THIN = 8  差异内容：COMPONENT\_ULTRA\_THIN = 8 | component/common.d.ts |
| 新增API | NA | 类名：BlurStyle；  API声明：COMPONENT\_THIN = 9  差异内容：COMPONENT\_THIN = 9 | component/common.d.ts |
| 新增API | NA | 类名：BlurStyle；  API声明：COMPONENT\_REGULAR = 10  差异内容：COMPONENT\_REGULAR = 10 | component/common.d.ts |
| 新增API | NA | 类名：BlurStyle；  API声明：COMPONENT\_THICK = 11  差异内容：COMPONENT\_THICK = 11 | component/common.d.ts |
| 新增API | NA | 类名：BlurStyle；  API声明：COMPONENT\_ULTRA\_THICK = 12  差异内容：COMPONENT\_ULTRA\_THICK = 12 | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum ThemeColorMode  差异内容： declare enum ThemeColorMode | component/common.d.ts |
| 新增API | NA | 类名：ThemeColorMode；  API声明：SYSTEM  差异内容：SYSTEM | component/common.d.ts |
| 新增API | NA | 类名：ThemeColorMode；  API声明：LIGHT  差异内容：LIGHT | component/common.d.ts |
| 新增API | NA | 类名：ThemeColorMode；  API声明：DARK  差异内容：DARK | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum AdaptiveColor  差异内容： declare enum AdaptiveColor | component/common.d.ts |
| 新增API | NA | 类名：AdaptiveColor；  API声明：DEFAULT  差异内容：DEFAULT | component/common.d.ts |
| 新增API | NA | 类名：AdaptiveColor；  API声明：AVERAGE  差异内容：AVERAGE | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum ModalTransition  差异内容： declare enum ModalTransition | component/common.d.ts |
| 新增API | NA | 类名：ModalTransition；  API声明：DEFAULT  差异内容：DEFAULT | component/common.d.ts |
| 新增API | NA | 类名：ModalTransition；  API声明：NONE  差异内容：NONE | component/common.d.ts |
| 新增API | NA | 类名：ModalTransition；  API声明：ALPHA  差异内容：ALPHA | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface BackgroundBlurStyleOptions  差异内容： declare interface BackgroundBlurStyleOptions | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface ForegroundBlurStyleOptions  差异内容： declare interface ForegroundBlurStyleOptions | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface BlurOptions  差异内容： declare interface BlurOptions | component/common.d.ts |
| 新增API | NA | 类名：BlurOptions；  API声明：grayscale: [  number,  number  ];  差异内容：grayscale: [  number,  number  ]; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface BlurStyleOptions  差异内容： declare interface BlurStyleOptions | component/common.d.ts |
| 新增API | NA | 类名：BlurStyleOptions；  API声明：colorMode?: ThemeColorMode;  差异内容：colorMode?: ThemeColorMode; | component/common.d.ts |
| 新增API | NA | 类名：BlurStyleOptions；  API声明：adaptiveColor?: AdaptiveColor;  差异内容：adaptiveColor?: AdaptiveColor; | component/common.d.ts |
| 新增API | NA | 类名：BlurStyleOptions；  API声明：scale?: number;  差异内容：scale?: number; | component/common.d.ts |
| 新增API | NA | 类名：BlurStyleOptions；  API声明：blurOptions?: BlurOptions;  差异内容：blurOptions?: BlurOptions; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface BackgroundEffectOptions  差异内容： declare interface BackgroundEffectOptions | component/common.d.ts |
| 新增API | NA | 类名：BackgroundEffectOptions；  API声明：radius: number;  差异内容：radius: number; | component/common.d.ts |
| 新增API | NA | 类名：BackgroundEffectOptions；  API声明：saturation?: number;  差异内容：saturation?: number; | component/common.d.ts |
| 新增API | NA | 类名：BackgroundEffectOptions；  API声明：brightness?: number;  差异内容：brightness?: number; | component/common.d.ts |
| 新增API | NA | 类名：BackgroundEffectOptions；  API声明：color?: ResourceColor;  差异内容：color?: ResourceColor; | component/common.d.ts |
| 新增API | NA | 类名：BackgroundEffectOptions；  API声明：adaptiveColor?: AdaptiveColor;  差异内容：adaptiveColor?: AdaptiveColor; | component/common.d.ts |
| 新增API | NA | 类名：BackgroundEffectOptions；  API声明：blurOptions?: BlurOptions;  差异内容：blurOptions?: BlurOptions; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface ForegroundEffectOptions  差异内容： declare interface ForegroundEffectOptions | component/common.d.ts |
| 新增API | NA | 类名：ForegroundEffectOptions；  API声明：radius: number;  差异内容：radius: number; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface PickerTextStyle  差异内容： declare interface PickerTextStyle | component/common.d.ts |
| 新增API | NA | 类名：PickerTextStyle；  API声明：color?: ResourceColor;  差异内容：color?: ResourceColor; | component/common.d.ts |
| 新增API | NA | 类名：PickerTextStyle；  API声明：font?: Font;  差异内容：font?: Font; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface PickerDialogButtonStyle  差异内容： declare interface PickerDialogButtonStyle | component/common.d.ts |
| 新增API | NA | 类名：PickerDialogButtonStyle；  API声明：type?: ButtonType;  差异内容：type?: ButtonType; | component/common.d.ts |
| 新增API | NA | 类名：PickerDialogButtonStyle；  API声明：style?: ButtonStyleMode;  差异内容：style?: ButtonStyleMode; | component/common.d.ts |
| 新增API | NA | 类名：PickerDialogButtonStyle；  API声明：role?: ButtonRole;  差异内容：role?: ButtonRole; | component/common.d.ts |
| 新增API | NA | 类名：PickerDialogButtonStyle；  API声明：fontSize?: Length;  差异内容：fontSize?: Length; | component/common.d.ts |
| 新增API | NA | 类名：PickerDialogButtonStyle；  API声明：fontColor?: ResourceColor;  差异内容：fontColor?: ResourceColor; | component/common.d.ts |
| 新增API | NA | 类名：PickerDialogButtonStyle；  API声明：fontWeight?: FontWeight | number | string;  差异内容：fontWeight?: FontWeight | number | string; | component/common.d.ts |
| 新增API | NA | 类名：PickerDialogButtonStyle；  API声明：fontStyle?: FontStyle;  差异内容：fontStyle?: FontStyle; | component/common.d.ts |
| 新增API | NA | 类名：PickerDialogButtonStyle；  API声明：fontFamily?: Resource | string;  差异内容：fontFamily?: Resource | string; | component/common.d.ts |
| 新增API | NA | 类名：PickerDialogButtonStyle；  API声明：backgroundColor?: ResourceColor;  差异内容：backgroundColor?: ResourceColor; | component/common.d.ts |
| 新增API | NA | 类名：PickerDialogButtonStyle；  API声明：borderRadius?: Length | BorderRadiuses;  差异内容：borderRadius?: Length | BorderRadiuses; | component/common.d.ts |
| 新增API | NA | 类名：PickerDialogButtonStyle；  API声明：primary?: boolean;  差异内容：primary?: boolean; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum ShadowType  差异内容： declare enum ShadowType | component/common.d.ts |
| 新增API | NA | 类名：ShadowType；  API声明：COLOR  差异内容：COLOR | component/common.d.ts |
| 新增API | NA | 类名：ShadowType；  API声明：BLUR  差异内容：BLUR | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface ShadowOptions  差异内容： declare interface ShadowOptions | component/common.d.ts |
| 新增API | NA | 类名：ShadowOptions；  API声明：radius: number | Resource;  差异内容：radius: number | Resource; | component/common.d.ts |
| 新增API | NA | 类名：ShadowOptions；  API声明：type?: ShadowType;  差异内容：type?: ShadowType; | component/common.d.ts |
| 新增API | NA | 类名：ShadowOptions；  API声明：color?: Color | string | Resource | ColoringStrategy;  差异内容：color?: Color | string | Resource | ColoringStrategy; | component/common.d.ts |
| 新增API | NA | 类名：ShadowOptions；  API声明：offsetX?: number | Resource;  差异内容：offsetX?: number | Resource; | component/common.d.ts |
| 新增API | NA | 类名：ShadowOptions；  API声明：offsetY?: number | Resource;  差异内容：offsetY?: number | Resource; | component/common.d.ts |
| 新增API | NA | 类名：ShadowOptions；  API声明：fill?: boolean;  差异内容：fill?: boolean; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum ShadowStyle  差异内容： declare enum ShadowStyle | component/common.d.ts |
| 新增API | NA | 类名：ShadowStyle；  API声明：OUTER\_DEFAULT\_XS  差异内容：OUTER\_DEFAULT\_XS | component/common.d.ts |
| 新增API | NA | 类名：ShadowStyle；  API声明：OUTER\_DEFAULT\_SM  差异内容：OUTER\_DEFAULT\_SM | component/common.d.ts |
| 新增API | NA | 类名：ShadowStyle；  API声明：OUTER\_DEFAULT\_MD  差异内容：OUTER\_DEFAULT\_MD | component/common.d.ts |
| 新增API | NA | 类名：ShadowStyle；  API声明：OUTER\_DEFAULT\_LG  差异内容：OUTER\_DEFAULT\_LG | component/common.d.ts |
| 新增API | NA | 类名：ShadowStyle；  API声明：OUTER\_FLOATING\_SM  差异内容：OUTER\_FLOATING\_SM | component/common.d.ts |
| 新增API | NA | 类名：ShadowStyle；  API声明：OUTER\_FLOATING\_MD  差异内容：OUTER\_FLOATING\_MD | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface MultiShadowOptions  差异内容： declare interface MultiShadowOptions | component/common.d.ts |
| 新增API | NA | 类名：MultiShadowOptions；  API声明：radius?: number | Resource;  差异内容：radius?: number | Resource; | component/common.d.ts |
| 新增API | NA | 类名：MultiShadowOptions；  API声明：offsetX?: number | Resource;  差异内容：offsetX?: number | Resource; | component/common.d.ts |
| 新增API | NA | 类名：MultiShadowOptions；  API声明：offsetY?: number | Resource;  差异内容：offsetY?: number | Resource; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum SafeAreaType  差异内容： declare enum SafeAreaType | component/common.d.ts |
| 新增API | NA | 类名：SafeAreaType；  API声明：SYSTEM  差异内容：SYSTEM | component/common.d.ts |
| 新增API | NA | 类名：SafeAreaType；  API声明：CUTOUT  差异内容：CUTOUT | component/common.d.ts |
| 新增API | NA | 类名：SafeAreaType；  API声明：KEYBOARD  差异内容：KEYBOARD | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum SafeAreaEdge  差异内容： declare enum SafeAreaEdge | component/common.d.ts |
| 新增API | NA | 类名：SafeAreaEdge；  API声明：TOP  差异内容：TOP | component/common.d.ts |
| 新增API | NA | 类名：SafeAreaEdge；  API声明：BOTTOM  差异内容：BOTTOM | component/common.d.ts |
| 新增API | NA | 类名：SafeAreaEdge；  API声明：START  差异内容：START | component/common.d.ts |
| 新增API | NA | 类名：SafeAreaEdge；  API声明：END  差异内容：END | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum SheetSize  差异内容： declare enum SheetSize | component/common.d.ts |
| 新增API | NA | 类名：SheetSize；  API声明：MEDIUM  差异内容：MEDIUM | component/common.d.ts |
| 新增API | NA | 类名：SheetSize；  API声明：LARGE  差异内容：LARGE | component/common.d.ts |
| 新增API | NA | 类名：SheetSize；  API声明：FIT\_CONTENT = 2  差异内容：FIT\_CONTENT = 2 | component/common.d.ts |
| 新增API | NA | 类名：BaseEvent；  API声明：axisHorizontal?: number;  差异内容：axisHorizontal?: number; | component/common.d.ts |
| 新增API | NA | 类名：BaseEvent；  API声明：axisVertical?: number;  差异内容：axisVertical?: number; | component/common.d.ts |
| 新增API | NA | 类名：ClickEvent；  API声明：displayX: number;  差异内容：displayX: number; | component/common.d.ts |
| 新增API | NA | 类名：ClickEvent；  API声明：displayY: number;  差异内容：displayY: number; | component/common.d.ts |
| 新增API | NA | 类名：ClickEvent；  API声明：windowX: number;  差异内容：windowX: number; | component/common.d.ts |
| 新增API | NA | 类名：ClickEvent；  API声明：windowY: number;  差异内容：windowY: number; | component/common.d.ts |
| 新增API | NA | 类名：ClickEvent；  API声明：preventDefault: () => void;  差异内容：preventDefault: () => void; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface HoverEvent  差异内容： declare interface HoverEvent | component/common.d.ts |
| 新增API | NA | 类名：HoverEvent；  API声明：stopPropagation: () => void;  差异内容：stopPropagation: () => void; | component/common.d.ts |
| 新增API | NA | 类名：MouseEvent；  API声明：displayX: number;  差异内容：displayX: number; | component/common.d.ts |
| 新增API | NA | 类名：MouseEvent；  API声明：displayY: number;  差异内容：displayY: number; | component/common.d.ts |
| 新增API | NA | 类名：MouseEvent；  API声明：windowX: number;  差异内容：windowX: number; | component/common.d.ts |
| 新增API | NA | 类名：MouseEvent；  API声明：windowY: number;  差异内容：windowY: number; | component/common.d.ts |
| 新增API | NA | 类名：TouchObject；  API声明：displayX: number;  差异内容：displayX: number; | component/common.d.ts |
| 新增API | NA | 类名：TouchObject；  API声明：displayY: number;  差异内容：displayY: number; | component/common.d.ts |
| 新增API | NA | 类名：TouchObject；  API声明：windowX: number;  差异内容：windowX: number; | component/common.d.ts |
| 新增API | NA | 类名：TouchObject；  API声明：windowY: number;  差异内容：windowY: number; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface HistoricalPoint  差异内容： declare interface HistoricalPoint | component/common.d.ts |
| 新增API | NA | 类名：HistoricalPoint；  API声明：touchObject: TouchObject;  差异内容：touchObject: TouchObject; | component/common.d.ts |
| 新增API | NA | 类名：HistoricalPoint；  API声明：size: number;  差异内容：size: number; | component/common.d.ts |
| 新增API | NA | 类名：HistoricalPoint；  API声明：force: number;  差异内容：force: number; | component/common.d.ts |
| 新增API | NA | 类名：HistoricalPoint；  API声明：timestamp: number;  差异内容：timestamp: number; | component/common.d.ts |
| 新增API | NA | 类名：TouchEvent；  API声明：getHistoricalPoints(): Array<HistoricalPoint>;  差异内容：getHistoricalPoints(): Array<HistoricalPoint>; | component/common.d.ts |
| 新增API | NA | 类名：TouchEvent；  API声明：preventDefault: () => void;  差异内容：preventDefault: () => void; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type SizeChangeCallback = (oldValue: SizeOptions, newValue: SizeOptions) => void;  差异内容：declare type SizeChangeCallback = (oldValue: SizeOptions, newValue: SizeOptions) => void; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type GestureRecognizerJudgeBeginCallback = (event: BaseGestureEvent, current: GestureRecognizer, recognizers: Array<GestureRecognizer>) => GestureJudgeResult;  差异内容：declare type GestureRecognizerJudgeBeginCallback = (event: BaseGestureEvent, current: GestureRecognizer, recognizers: Array<GestureRecognizer>) => GestureJudgeResult; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type ShouldBuiltInRecognizerParallelWithCallback = (current: GestureRecognizer, others: Array<GestureRecognizer>) => GestureRecognizer;  差异内容：declare type ShouldBuiltInRecognizerParallelWithCallback = (current: GestureRecognizer, others: Array<GestureRecognizer>) => GestureRecognizer; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum DragBehavior  差异内容： declare enum DragBehavior | component/common.d.ts |
| 新增API | NA | 类名：DragBehavior；  API声明：COPY  差异内容：COPY | component/common.d.ts |
| 新增API | NA | 类名：DragBehavior；  API声明：MOVE  差异内容：MOVE | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type UnifiedData = import('../api/@ohos.data.unifiedDataChannel').default.UnifiedData;  差异内容：declare type UnifiedData = import('../api/@ohos.data.unifiedDataChannel').default.UnifiedData; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type Summary = import('../api/@ohos.data.unifiedDataChannel').default.Summary;  差异内容：declare type Summary = import('../api/@ohos.data.unifiedDataChannel').default.Summary; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type UniformDataType = import('../api/@ohos.data.uniformTypeDescriptor').default.UniformDataType;  差异内容：declare type UniformDataType = import('../api/@ohos.data.uniformTypeDescriptor').default.UniformDataType; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum DragResult  差异内容： declare enum DragResult | component/common.d.ts |
| 新增API | NA | 类名：DragResult；  API声明：DRAG\_SUCCESSFUL = 0  差异内容：DRAG\_SUCCESSFUL = 0 | component/common.d.ts |
| 新增API | NA | 类名：DragResult；  API声明：DRAG\_FAILED = 1  差异内容：DRAG\_FAILED = 1 | component/common.d.ts |
| 新增API | NA | 类名：DragResult；  API声明：DRAG\_CANCELED = 2  差异内容：DRAG\_CANCELED = 2 | component/common.d.ts |
| 新增API | NA | 类名：DragResult；  API声明：DROP\_ENABLED = 3  差异内容：DROP\_ENABLED = 3 | component/common.d.ts |
| 新增API | NA | 类名：DragResult；  API声明：DROP\_DISABLED = 4  差异内容：DROP\_DISABLED = 4 | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum BlendMode  差异内容： declare enum BlendMode | component/common.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：NONE = 0  差异内容：NONE = 0 | component/common.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：CLEAR = 1  差异内容：CLEAR = 1 | component/common.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：SRC = 2  差异内容：SRC = 2 | component/common.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：DST = 3  差异内容：DST = 3 | component/common.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：SRC\_OVER = 4  差异内容：SRC\_OVER = 4 | component/common.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：DST\_OVER = 5  差异内容：DST\_OVER = 5 | component/common.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：SRC\_IN = 6  差异内容：SRC\_IN = 6 | component/common.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：DST\_IN = 7  差异内容：DST\_IN = 7 | component/common.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：SRC\_OUT = 8  差异内容：SRC\_OUT = 8 | component/common.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：DST\_OUT = 9  差异内容：DST\_OUT = 9 | component/common.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：SRC\_ATOP = 10  差异内容：SRC\_ATOP = 10 | component/common.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：DST\_ATOP = 11  差异内容：DST\_ATOP = 11 | component/common.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：XOR = 12  差异内容：XOR = 12 | component/common.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：PLUS = 13  差异内容：PLUS = 13 | component/common.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：MODULATE = 14  差异内容：MODULATE = 14 | component/common.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：SCREEN = 15  差异内容：SCREEN = 15 | component/common.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：OVERLAY = 16  差异内容：OVERLAY = 16 | component/common.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：DARKEN = 17  差异内容：DARKEN = 17 | component/common.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：LIGHTEN = 18  差异内容：LIGHTEN = 18 | component/common.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：COLOR\_DODGE = 19  差异内容：COLOR\_DODGE = 19 | component/common.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：COLOR\_BURN = 20  差异内容：COLOR\_BURN = 20 | component/common.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：HARD\_LIGHT = 21  差异内容：HARD\_LIGHT = 21 | component/common.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：SOFT\_LIGHT = 22  差异内容：SOFT\_LIGHT = 22 | component/common.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：DIFFERENCE = 23  差异内容：DIFFERENCE = 23 | component/common.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：EXCLUSION = 24  差异内容：EXCLUSION = 24 | component/common.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：MULTIPLY = 25  差异内容：MULTIPLY = 25 | component/common.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：HUE = 26  差异内容：HUE = 26 | component/common.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：SATURATION = 27  差异内容：SATURATION = 27 | component/common.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：COLOR = 28  差异内容：COLOR = 28 | component/common.d.ts |
| 新增API | NA | 类名：BlendMode；  API声明：LUMINOSITY = 29  差异内容：LUMINOSITY = 29 | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum BlendApplyType  差异内容： declare enum BlendApplyType | component/common.d.ts |
| 新增API | NA | 类名：BlendApplyType；  API声明：FAST = 0  差异内容：FAST = 0 | component/common.d.ts |
| 新增API | NA | 类名：BlendApplyType；  API声明：OFFSCREEN = 1  差异内容：OFFSCREEN = 1 | component/common.d.ts |
| 新增API | NA | 类名：DragEvent；  API声明：getDisplayX(): number;  差异内容：getDisplayX(): number; | component/common.d.ts |
| 新增API | NA | 类名：DragEvent；  API声明：getDisplayY(): number;  差异内容：getDisplayY(): number; | component/common.d.ts |
| 新增API | NA | 类名：DragEvent；  API声明：getWindowX(): number;  差异内容：getWindowX(): number; | component/common.d.ts |
| 新增API | NA | 类名：DragEvent；  API声明：getWindowY(): number;  差异内容：getWindowY(): number; | component/common.d.ts |
| 新增API | NA | 类名：DragEvent；  API声明：dragBehavior: DragBehavior;  差异内容：dragBehavior: DragBehavior; | component/common.d.ts |
| 新增API | NA | 类名：DragEvent；  API声明：useCustomDropAnimation: boolean;  差异内容：useCustomDropAnimation: boolean; | component/common.d.ts |
| 新增API | NA | 类名：DragEvent；  API声明：setData(unifiedData: UnifiedData): void;  差异内容：setData(unifiedData: UnifiedData): void; | component/common.d.ts |
| 新增API | NA | 类名：DragEvent；  API声明：getData(): UnifiedData;  差异内容：getData(): UnifiedData; | component/common.d.ts |
| 新增API | NA | 类名：DragEvent；  API声明：getSummary(): Summary;  差异内容：getSummary(): Summary; | component/common.d.ts |
| 新增API | NA | 类名：DragEvent；  API声明：setResult(dragResult: DragResult): void;  差异内容：setResult(dragResult: DragResult): void; | component/common.d.ts |
| 新增API | NA | 类名：DragEvent；  API声明：getResult(): DragResult;  差异内容：getResult(): DragResult; | component/common.d.ts |
| 新增API | NA | 类名：DragEvent；  API声明：getPreviewRect(): Rectangle;  差异内容：getPreviewRect(): Rectangle; | component/common.d.ts |
| 新增API | NA | 类名：DragEvent；  API声明：getVelocityX(): number;  差异内容：getVelocityX(): number; | component/common.d.ts |
| 新增API | NA | 类名：DragEvent；  API声明：getVelocityY(): number;  差异内容：getVelocityY(): number; | component/common.d.ts |
| 新增API | NA | 类名：DragEvent；  API声明：getVelocity(): number;  差异内容：getVelocity(): number; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type IntentionCode = import('../api/@ohos.multimodalInput.intentionCode').IntentionCode;  差异内容：declare type IntentionCode = import('../api/@ohos.multimodalInput.intentionCode').IntentionCode; | component/common.d.ts |
| 新增API | NA | 类名：KeyEvent；  API声明：intentionCode: IntentionCode;  差异内容：intentionCode: IntentionCode; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface BindOptions  差异内容： declare interface BindOptions | component/common.d.ts |
| 新增API | NA | 类名：BindOptions；  API声明：backgroundColor?: ResourceColor;  差异内容：backgroundColor?: ResourceColor; | component/common.d.ts |
| 新增API | NA | 类名：BindOptions；  API声明：onAppear?: () => void;  差异内容：onAppear?: () => void; | component/common.d.ts |
| 新增API | NA | 类名：BindOptions；  API声明：onDisappear?: () => void;  差异内容：onDisappear?: () => void; | component/common.d.ts |
| 新增API | NA | 类名：BindOptions；  API声明：onWillAppear?: () => void;  差异内容：onWillAppear?: () => void; | component/common.d.ts |
| 新增API | NA | 类名：BindOptions；  API声明：onWillDisappear?: () => void;  差异内容：onWillDisappear?: () => void; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface DismissContentCoverAction  差异内容： declare interface DismissContentCoverAction | component/common.d.ts |
| 新增API | NA | 类名：DismissContentCoverAction；  API声明：dismiss: Callback<void>;  差异内容：dismiss: Callback<void>; | component/common.d.ts |
| 新增API | NA | 类名：DismissContentCoverAction；  API声明：reason: DismissReason;  差异内容：reason: DismissReason; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface ContentCoverOptions  差异内容： declare interface ContentCoverOptions | component/common.d.ts |
| 新增API | NA | 类名：ContentCoverOptions；  API声明：modalTransition?: ModalTransition;  差异内容：modalTransition?: ModalTransition; | component/common.d.ts |
| 新增API | NA | 类名：ContentCoverOptions；  API声明：onWillDismiss?: Callback<DismissContentCoverAction>;  差异内容：onWillDismiss?: Callback<DismissContentCoverAction>; | component/common.d.ts |
| 新增API | NA | 类名：ContentCoverOptions；  API声明：transition?: TransitionEffect;  差异内容：transition?: TransitionEffect; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface SheetTitleOptions  差异内容： declare interface SheetTitleOptions | component/common.d.ts |
| 新增API | NA | 类名：SheetTitleOptions；  API声明：title: ResourceStr;  差异内容：title: ResourceStr; | component/common.d.ts |
| 新增API | NA | 类名：SheetTitleOptions；  API声明：subtitle?: ResourceStr;  差异内容：subtitle?: ResourceStr; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum SheetType  差异内容： declare enum SheetType | component/common.d.ts |
| 新增API | NA | 类名：SheetType；  API声明：BOTTOM = 0  差异内容：BOTTOM = 0 | component/common.d.ts |
| 新增API | NA | 类名：SheetType；  API声明：CENTER = 1  差异内容：CENTER = 1 | component/common.d.ts |
| 新增API | NA | 类名：SheetType；  API声明：POPUP = 2  差异内容：POPUP = 2 | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum SheetMode  差异内容： declare enum SheetMode | component/common.d.ts |
| 新增API | NA | 类名：SheetMode；  API声明：OVERLAY = 0  差异内容：OVERLAY = 0 | component/common.d.ts |
| 新增API | NA | 类名：SheetMode；  API声明：EMBEDDED = 1  差异内容：EMBEDDED = 1 | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum ScrollSizeMode  差异内容： declare enum ScrollSizeMode | component/common.d.ts |
| 新增API | NA | 类名：ScrollSizeMode；  API声明：FOLLOW\_DETENT = 0  差异内容：FOLLOW\_DETENT = 0 | component/common.d.ts |
| 新增API | NA | 类名：ScrollSizeMode；  API声明：CONTINUOUS = 1  差异内容：CONTINUOUS = 1 | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface SheetDismiss  差异内容： declare interface SheetDismiss | component/common.d.ts |
| 新增API | NA | 类名：SheetDismiss；  API声明：dismiss: () => void;  差异内容：dismiss: () => void; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface DismissSheetAction  差异内容： declare interface DismissSheetAction | component/common.d.ts |
| 新增API | NA | 类名：DismissSheetAction；  API声明：dismiss: Callback<void>;  差异内容：dismiss: Callback<void>; | component/common.d.ts |
| 新增API | NA | 类名：DismissSheetAction；  API声明：reason: DismissReason;  差异内容：reason: DismissReason; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface SpringBackAction  差异内容： declare interface SpringBackAction | component/common.d.ts |
| 新增API | NA | 类名：SpringBackAction；  API声明：springBack: Callback<void>;  差异内容：springBack: Callback<void>; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface SheetOptions  差异内容： declare interface SheetOptions | component/common.d.ts |
| 新增API | NA | 类名：SheetOptions；  API声明：height?: SheetSize | Length;  差异内容：height?: SheetSize | Length; | component/common.d.ts |
| 新增API | NA | 类名：SheetOptions；  API声明：dragBar?: boolean;  差异内容：dragBar?: boolean; | component/common.d.ts |
| 新增API | NA | 类名：SheetOptions；  API声明：maskColor?: ResourceColor;  差异内容：maskColor?: ResourceColor; | component/common.d.ts |
| 新增API | NA | 类名：SheetOptions；  API声明：detents?: [  (SheetSize | Length),  (SheetSize | Length)?,  (SheetSize | Length)?  ];  差异内容：detents?: [  (SheetSize | Length),  (SheetSize | Length)?,  (SheetSize | Length)?  ]; | component/common.d.ts |
| 新增API | NA | 类名：SheetOptions；  API声明：blurStyle?: BlurStyle;  差异内容：blurStyle?: BlurStyle; | component/common.d.ts |
| 新增API | NA | 类名：SheetOptions；  API声明：showClose?: boolean | Resource;  差异内容：showClose?: boolean | Resource; | component/common.d.ts |
| 新增API | NA | 类名：SheetOptions；  API声明：preferType?: SheetType;  差异内容：preferType?: SheetType; | component/common.d.ts |
| 新增API | NA | 类名：SheetOptions；  API声明：title?: SheetTitleOptions | CustomBuilder;  差异内容：title?: SheetTitleOptions | CustomBuilder; | component/common.d.ts |
| 新增API | NA | 类名：SheetOptions；  API声明：shouldDismiss?: (sheetDismiss: SheetDismiss) => void;  差异内容：shouldDismiss?: (sheetDismiss: SheetDismiss) => void; | component/common.d.ts |
| 新增API | NA | 类名：SheetOptions；  API声明：onWillDismiss?: Callback<DismissSheetAction>;  差异内容：onWillDismiss?: Callback<DismissSheetAction>; | component/common.d.ts |
| 新增API | NA | 类名：SheetOptions；  API声明：onWillSpringBackWhenDismiss?: Callback<SpringBackAction>;  差异内容：onWillSpringBackWhenDismiss?: Callback<SpringBackAction>; | component/common.d.ts |
| 新增API | NA | 类名：SheetOptions；  API声明：enableOutsideInteractive?: boolean;  差异内容：enableOutsideInteractive?: boolean; | component/common.d.ts |
| 新增API | NA | 类名：SheetOptions；  API声明：width?: Dimension;  差异内容：width?: Dimension; | component/common.d.ts |
| 新增API | NA | 类名：SheetOptions；  API声明：borderWidth?: Dimension | EdgeWidths | LocalizedEdgeWidths;  差异内容：borderWidth?: Dimension | EdgeWidths | LocalizedEdgeWidths; | component/common.d.ts |
| 新增API | NA | 类名：SheetOptions；  API声明：borderColor?: ResourceColor | EdgeColors | LocalizedEdgeColors;  差异内容：borderColor?: ResourceColor | EdgeColors | LocalizedEdgeColors; | component/common.d.ts |
| 新增API | NA | 类名：SheetOptions；  API声明：borderStyle?: BorderStyle | EdgeStyles;  差异内容：borderStyle?: BorderStyle | EdgeStyles; | component/common.d.ts |
| 新增API | NA | 类名：SheetOptions；  API声明：shadow?: ShadowOptions | ShadowStyle;  差异内容：shadow?: ShadowOptions | ShadowStyle; | component/common.d.ts |
| 新增API | NA | 类名：SheetOptions；  API声明：onHeightDidChange?: Callback<number>;  差异内容：onHeightDidChange?: Callback<number>; | component/common.d.ts |
| 新增API | NA | 类名：SheetOptions；  API声明：mode?: SheetMode;  差异内容：mode?: SheetMode; | component/common.d.ts |
| 新增API | NA | 类名：SheetOptions；  API声明：scrollSizeMode?: ScrollSizeMode;  差异内容：scrollSizeMode?: ScrollSizeMode; | component/common.d.ts |
| 新增API | NA | 类名：SheetOptions；  API声明：onDetentsDidChange?: Callback<number>;  差异内容：onDetentsDidChange?: Callback<number>; | component/common.d.ts |
| 新增API | NA | 类名：SheetOptions；  API声明：onWidthDidChange?: Callback<number>;  差异内容：onWidthDidChange?: Callback<number>; | component/common.d.ts |
| 新增API | NA | 类名：SheetOptions；  API声明：onTypeDidChange?: Callback<SheetType>;  差异内容：onTypeDidChange?: Callback<SheetType>; | component/common.d.ts |
| 新增API | NA | 类名：SheetOptions；  API声明：uiContext?: UIContext;  差异内容：uiContext?: UIContext; | component/common.d.ts |
| 新增API | NA | 类名：StateStyles；  API声明：selected?: object;  差异内容：selected?: object; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface PopupMessageOptions  差异内容： declare interface PopupMessageOptions | component/common.d.ts |
| 新增API | NA | 类名：PopupMessageOptions；  API声明：textColor?: ResourceColor;  差异内容：textColor?: ResourceColor; | component/common.d.ts |
| 新增API | NA | 类名：PopupMessageOptions；  API声明：font?: Font;  差异内容：font?: Font; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum DismissReason  差异内容： declare enum DismissReason | component/common.d.ts |
| 新增API | NA | 类名：DismissReason；  API声明：PRESS\_BACK = 0  差异内容：PRESS\_BACK = 0 | component/common.d.ts |
| 新增API | NA | 类名：DismissReason；  API声明：TOUCH\_OUTSIDE = 1  差异内容：TOUCH\_OUTSIDE = 1 | component/common.d.ts |
| 新增API | NA | 类名：DismissReason；  API声明：CLOSE\_BUTTON = 2  差异内容：CLOSE\_BUTTON = 2 | component/common.d.ts |
| 新增API | NA | 类名：DismissReason；  API声明：SLIDE\_DOWN = 3  差异内容：SLIDE\_DOWN = 3 | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface DismissPopupAction  差异内容： declare interface DismissPopupAction | component/common.d.ts |
| 新增API | NA | 类名：DismissPopupAction；  API声明：dismiss: Callback<void>;  差异内容：dismiss: Callback<void>; | component/common.d.ts |
| 新增API | NA | 类名：DismissPopupAction；  API声明：reason: DismissReason;  差异内容：reason: DismissReason; | component/common.d.ts |
| 新增API | NA | 类名：PopupOptions；  API声明：placement?: Placement;  差异内容：placement?: Placement; | component/common.d.ts |
| 新增API | NA | 类名：PopupOptions；  API声明：mask?: boolean | {  color: ResourceColor;  };  差异内容：mask?: boolean | {  color: ResourceColor;  }; | component/common.d.ts |
| 新增API | NA | 类名：PopupOptions；  API声明：messageOptions?: PopupMessageOptions;  差异内容：messageOptions?: PopupMessageOptions; | component/common.d.ts |
| 新增API | NA | 类名：PopupOptions；  API声明：targetSpace?: Length;  差异内容：targetSpace?: Length; | component/common.d.ts |
| 新增API | NA | 类名：PopupOptions；  API声明：enableArrow?: boolean;  差异内容：enableArrow?: boolean; | component/common.d.ts |
| 新增API | NA | 类名：PopupOptions；  API声明：offset?: Position;  差异内容：offset?: Position; | component/common.d.ts |
| 新增API | NA | 类名：PopupOptions；  API声明：popupColor?: Color | string | Resource | number;  差异内容：popupColor?: Color | string | Resource | number; | component/common.d.ts |
| 新增API | NA | 类名：PopupOptions；  API声明：autoCancel?: boolean;  差异内容：autoCancel?: boolean; | component/common.d.ts |
| 新增API | NA | 类名：PopupOptions；  API声明：width?: Dimension;  差异内容：width?: Dimension; | component/common.d.ts |
| 新增API | NA | 类名：PopupOptions；  API声明：arrowPointPosition?: ArrowPointPosition;  差异内容：arrowPointPosition?: ArrowPointPosition; | component/common.d.ts |
| 新增API | NA | 类名：PopupOptions；  API声明：arrowWidth?: Dimension;  差异内容：arrowWidth?: Dimension; | component/common.d.ts |
| 新增API | NA | 类名：PopupOptions；  API声明：arrowHeight?: Dimension;  差异内容：arrowHeight?: Dimension; | component/common.d.ts |
| 新增API | NA | 类名：PopupOptions；  API声明：radius?: Dimension;  差异内容：radius?: Dimension; | component/common.d.ts |
| 新增API | NA | 类名：PopupOptions；  API声明：shadow?: ShadowOptions | ShadowStyle;  差异内容：shadow?: ShadowOptions | ShadowStyle; | component/common.d.ts |
| 新增API | NA | 类名：PopupOptions；  API声明：backgroundBlurStyle?: BlurStyle;  差异内容：backgroundBlurStyle?: BlurStyle; | component/common.d.ts |
| 新增API | NA | 类名：PopupOptions；  API声明：transition?: TransitionEffect;  差异内容：transition?: TransitionEffect; | component/common.d.ts |
| 新增API | NA | 类名：PopupOptions；  API声明：onWillDismiss?: boolean | Callback<DismissPopupAction>;  差异内容：onWillDismiss?: boolean | Callback<DismissPopupAction>; | component/common.d.ts |
| 新增API | NA | 类名：CustomPopupOptions；  API声明：mask?: boolean | {  color: ResourceColor;  };  差异内容：mask?: boolean | {  color: ResourceColor;  }; | component/common.d.ts |
| 新增API | NA | 类名：CustomPopupOptions；  API声明：targetSpace?: Length;  差异内容：targetSpace?: Length; | component/common.d.ts |
| 新增API | NA | 类名：CustomPopupOptions；  API声明：offset?: Position;  差异内容：offset?: Position; | component/common.d.ts |
| 新增API | NA | 类名：CustomPopupOptions；  API声明：width?: Dimension;  差异内容：width?: Dimension; | component/common.d.ts |
| 新增API | NA | 类名：CustomPopupOptions；  API声明：arrowPointPosition?: ArrowPointPosition;  差异内容：arrowPointPosition?: ArrowPointPosition; | component/common.d.ts |
| 新增API | NA | 类名：CustomPopupOptions；  API声明：arrowWidth?: Dimension;  差异内容：arrowWidth?: Dimension; | component/common.d.ts |
| 新增API | NA | 类名：CustomPopupOptions；  API声明：arrowHeight?: Dimension;  差异内容：arrowHeight?: Dimension; | component/common.d.ts |
| 新增API | NA | 类名：CustomPopupOptions；  API声明：radius?: Dimension;  差异内容：radius?: Dimension; | component/common.d.ts |
| 新增API | NA | 类名：CustomPopupOptions；  API声明：shadow?: ShadowOptions | ShadowStyle;  差异内容：shadow?: ShadowOptions | ShadowStyle; | component/common.d.ts |
| 新增API | NA | 类名：CustomPopupOptions；  API声明：backgroundBlurStyle?: BlurStyle;  差异内容：backgroundBlurStyle?: BlurStyle; | component/common.d.ts |
| 新增API | NA | 类名：CustomPopupOptions；  API声明：focusable?: boolean;  差异内容：focusable?: boolean; | component/common.d.ts |
| 新增API | NA | 类名：CustomPopupOptions；  API声明：transition?: TransitionEffect;  差异内容：transition?: TransitionEffect; | component/common.d.ts |
| 新增API | NA | 类名：CustomPopupOptions；  API声明：onWillDismiss?: boolean | Callback<DismissPopupAction>;  差异内容：onWillDismiss?: boolean | Callback<DismissPopupAction>; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum MenuPreviewMode  差异内容： declare enum MenuPreviewMode | component/common.d.ts |
| 新增API | NA | 类名：MenuPreviewMode；  API声明：NONE = 0  差异内容：NONE = 0 | component/common.d.ts |
| 新增API | NA | 类名：MenuPreviewMode；  API声明：IMAGE = 1  差异内容：IMAGE = 1 | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type AnimationRange<T> = [  from: T,  to: T  ];  差异内容：declare type AnimationRange<T> = [  from: T,  to: T  ]; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： interface ContextMenuAnimationOptions  差异内容： interface ContextMenuAnimationOptions | component/common.d.ts |
| 新增API | NA | 类名：ContextMenuAnimationOptions；  API声明：scale?: AnimationRange<number>;  差异内容：scale?: AnimationRange<number>; | component/common.d.ts |
| 新增API | NA | 类名：ContextMenuAnimationOptions；  API声明：transition?: TransitionEffect;  差异内容：transition?: TransitionEffect; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface ContextMenuOptions  差异内容： declare interface ContextMenuOptions | component/common.d.ts |
| 新增API | NA | 类名：ContextMenuOptions；  API声明：offset?: Position;  差异内容：offset?: Position; | component/common.d.ts |
| 新增API | NA | 类名：ContextMenuOptions；  API声明：placement?: Placement;  差异内容：placement?: Placement; | component/common.d.ts |
| 新增API | NA | 类名：ContextMenuOptions；  API声明：enableArrow?: boolean;  差异内容：enableArrow?: boolean; | component/common.d.ts |
| 新增API | NA | 类名：ContextMenuOptions；  API声明：arrowOffset?: Length;  差异内容：arrowOffset?: Length; | component/common.d.ts |
| 新增API | NA | 类名：ContextMenuOptions；  API声明：preview?: MenuPreviewMode | CustomBuilder;  差异内容：preview?: MenuPreviewMode | CustomBuilder; | component/common.d.ts |
| 新增API | NA | 类名：ContextMenuOptions；  API声明：borderRadius?: Length | BorderRadiuses;  差异内容：borderRadius?: Length | BorderRadiuses; | component/common.d.ts |
| 新增API | NA | 类名：ContextMenuOptions；  API声明：onAppear?: () => void;  差异内容：onAppear?: () => void; | component/common.d.ts |
| 新增API | NA | 类名：ContextMenuOptions；  API声明：onDisappear?: () => void;  差异内容：onDisappear?: () => void; | component/common.d.ts |
| 新增API | NA | 类名：ContextMenuOptions；  API声明：aboutToAppear?: () => void;  差异内容：aboutToAppear?: () => void; | component/common.d.ts |
| 新增API | NA | 类名：ContextMenuOptions；  API声明：aboutToDisappear?: () => void;  差异内容：aboutToDisappear?: () => void; | component/common.d.ts |
| 新增API | NA | 类名：ContextMenuOptions；  API声明：previewAnimationOptions?: ContextMenuAnimationOptions;  差异内容：previewAnimationOptions?: ContextMenuAnimationOptions; | component/common.d.ts |
| 新增API | NA | 类名：ContextMenuOptions；  API声明：backgroundColor?: ResourceColor;  差异内容：backgroundColor?: ResourceColor; | component/common.d.ts |
| 新增API | NA | 类名：ContextMenuOptions；  API声明：backgroundBlurStyle?: BlurStyle;  差异内容：backgroundBlurStyle?: BlurStyle; | component/common.d.ts |
| 新增API | NA | 类名：ContextMenuOptions；  API声明：transition?: TransitionEffect;  差异内容：transition?: TransitionEffect; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface MenuOptions  差异内容： declare interface MenuOptions | component/common.d.ts |
| 新增API | NA | 类名：MenuOptions；  API声明：title?: ResourceStr;  差异内容：title?: ResourceStr; | component/common.d.ts |
| 新增API | NA | 类名：MenuOptions；  API声明：showInSubWindow?: boolean;  差异内容：showInSubWindow?: boolean; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class ProgressMask  差异内容： declare class ProgressMask | component/common.d.ts |
| 新增API | NA | 类名：ProgressMask；  API声明：updateProgress(value: number): void;  差异内容：updateProgress(value: number): void; | component/common.d.ts |
| 新增API | NA | 类名：ProgressMask；  API声明：updateColor(value: ResourceColor): void;  差异内容：updateColor(value: ResourceColor): void; | component/common.d.ts |
| 新增API | NA | 类名：ProgressMask；  API声明：enableBreathingAnimation(value: boolean): void;  差异内容：enableBreathingAnimation(value: boolean): void; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class TouchTestInfo  差异内容： declare class TouchTestInfo | component/common.d.ts |
| 新增API | NA | 类名：TouchTestInfo；  API声明：windowX: number;  差异内容：windowX: number; | component/common.d.ts |
| 新增API | NA | 类名：TouchTestInfo；  API声明：windowY: number;  差异内容：windowY: number; | component/common.d.ts |
| 新增API | NA | 类名：TouchTestInfo；  API声明：parentX: number;  差异内容：parentX: number; | component/common.d.ts |
| 新增API | NA | 类名：TouchTestInfo；  API声明：parentY: number;  差异内容：parentY: number; | component/common.d.ts |
| 新增API | NA | 类名：TouchTestInfo；  API声明：x: number;  差异内容：x: number; | component/common.d.ts |
| 新增API | NA | 类名：TouchTestInfo；  API声明：y: number;  差异内容：y: number; | component/common.d.ts |
| 新增API | NA | 类名：TouchTestInfo；  API声明：rect: RectResult;  差异内容：rect: RectResult; | component/common.d.ts |
| 新增API | NA | 类名：TouchTestInfo；  API声明：id: string;  差异内容：id: string; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class TouchResult  差异内容： declare class TouchResult | component/common.d.ts |
| 新增API | NA | 类名：TouchResult；  API声明：strategy: TouchTestStrategy;  差异内容：strategy: TouchTestStrategy; | component/common.d.ts |
| 新增API | NA | 类名：TouchResult；  API声明：id?: string;  差异内容：id?: string; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface PixelStretchEffectOptions  差异内容： declare interface PixelStretchEffectOptions | component/common.d.ts |
| 新增API | NA | 类名：PixelStretchEffectOptions；  API声明：top?: Length;  差异内容：top?: Length; | component/common.d.ts |
| 新增API | NA | 类名：PixelStretchEffectOptions；  API声明：bottom?: Length;  差异内容：bottom?: Length; | component/common.d.ts |
| 新增API | NA | 类名：PixelStretchEffectOptions；  API声明：left?: Length;  差异内容：left?: Length; | component/common.d.ts |
| 新增API | NA | 类名：PixelStretchEffectOptions；  API声明：right?: Length;  差异内容：right?: Length; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface ClickEffect  差异内容： declare interface ClickEffect | component/common.d.ts |
| 新增API | NA | 类名：ClickEffect；  API声明：level: ClickEffectLevel;  差异内容：level: ClickEffectLevel; | component/common.d.ts |
| 新增API | NA | 类名：ClickEffect；  API声明：scale?: number;  差异内容：scale?: number; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface NestedScrollOptions  差异内容： declare interface NestedScrollOptions | component/common.d.ts |
| 新增API | NA | 类名：NestedScrollOptions；  API声明：scrollForward: NestedScrollMode;  差异内容：scrollForward: NestedScrollMode; | component/common.d.ts |
| 新增API | NA | 类名：NestedScrollOptions；  API声明：scrollBackward: NestedScrollMode;  差异内容：scrollBackward: NestedScrollMode; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface MenuElement  差异内容： declare interface MenuElement | component/common.d.ts |
| 新增API | NA | 类名：MenuElement；  API声明：value: ResourceStr;  差异内容：value: ResourceStr; | component/common.d.ts |
| 新增API | NA | 类名：MenuElement；  API声明：icon?: ResourceStr;  差异内容：icon?: ResourceStr; | component/common.d.ts |
| 新增API | NA | 类名：MenuElement；  API声明：enabled?: boolean;  差异内容：enabled?: boolean; | component/common.d.ts |
| 新增API | NA | 类名：MenuElement；  API声明：action: () => void;  差异内容：action: () => void; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface AttributeModifier  差异内容： declare interface AttributeModifier | component/common.d.ts |
| 新增API | NA | 类名：AttributeModifier；  API声明：applyNormalAttribute?(instance: T): void;  差异内容：applyNormalAttribute?(instance: T): void; | component/common.d.ts |
| 新增API | NA | 类名：AttributeModifier；  API声明：applyPressedAttribute?(instance: T): void;  差异内容：applyPressedAttribute?(instance: T): void; | component/common.d.ts |
| 新增API | NA | 类名：AttributeModifier；  API声明：applyFocusedAttribute?(instance: T): void;  差异内容：applyFocusedAttribute?(instance: T): void; | component/common.d.ts |
| 新增API | NA | 类名：AttributeModifier；  API声明：applyDisabledAttribute?(instance: T): void;  差异内容：applyDisabledAttribute?(instance: T): void; | component/common.d.ts |
| 新增API | NA | 类名：AttributeModifier；  API声明：applySelectedAttribute?(instance: T): void;  差异内容：applySelectedAttribute?(instance: T): void; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface ContentModifier  差异内容： declare interface ContentModifier | component/common.d.ts |
| 新增API | NA | 类名：ContentModifier；  API声明：applyContent(): WrappedBuilder<[  T  ]>;  差异内容：applyContent(): WrappedBuilder<[  T  ]>; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface CommonConfiguration  差异内容： declare interface CommonConfiguration | component/common.d.ts |
| 新增API | NA | 类名：CommonConfiguration；  API声明：enabled: boolean;  差异内容：enabled: boolean; | component/common.d.ts |
| 新增API | NA | 类名：CommonConfiguration；  API声明：contentModifier: ContentModifier<T>;  差异内容：contentModifier: ContentModifier<T>; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum OutlineStyle  差异内容： declare enum OutlineStyle | component/common.d.ts |
| 新增API | NA | 类名：OutlineStyle；  API声明：SOLID = 0  差异内容：SOLID = 0 | component/common.d.ts |
| 新增API | NA | 类名：OutlineStyle；  API声明：DASHED = 1  差异内容：DASHED = 1 | component/common.d.ts |
| 新增API | NA | 类名：OutlineStyle；  API声明：DOTTED = 2  差异内容：DOTTED = 2 | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum DragPreviewMode  差异内容： declare enum DragPreviewMode | component/common.d.ts |
| 新增API | NA | 类名：DragPreviewMode；  API声明：AUTO = 1  差异内容：AUTO = 1 | component/common.d.ts |
| 新增API | NA | 类名：DragPreviewMode；  API声明：DISABLE\_SCALE = 2  差异内容：DISABLE\_SCALE = 2 | component/common.d.ts |
| 新增API | NA | 类名：DragPreviewMode；  API声明：ENABLE\_DEFAULT\_SHADOW = 3  差异内容：ENABLE\_DEFAULT\_SHADOW = 3 | component/common.d.ts |
| 新增API | NA | 类名：DragPreviewMode；  API声明：ENABLE\_DEFAULT\_RADIUS = 4  差异内容：ENABLE\_DEFAULT\_RADIUS = 4 | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum MenuPolicy  差异内容： declare enum MenuPolicy | component/common.d.ts |
| 新增API | NA | 类名：MenuPolicy；  API声明：DEFAULT = 0  差异内容：DEFAULT = 0 | component/common.d.ts |
| 新增API | NA | 类名：MenuPolicy；  API声明：HIDE = 1  差异内容：HIDE = 1 | component/common.d.ts |
| 新增API | NA | 类名：MenuPolicy；  API声明：SHOW = 2  差异内容：SHOW = 2 | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type ImageModifier = import('../api/arkui/ImageModifier').ImageModifier;  差异内容：declare type ImageModifier = import('../api/arkui/ImageModifier').ImageModifier; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type SymbolGlyphModifier = import('../api/arkui/SymbolGlyphModifier').SymbolGlyphModifier;  差异内容：declare type SymbolGlyphModifier = import('../api/arkui/SymbolGlyphModifier').SymbolGlyphModifier; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface DragPreviewOptions  差异内容： declare interface DragPreviewOptions | component/common.d.ts |
| 新增API | NA | 类名：DragPreviewOptions；  API声明：mode?: DragPreviewMode | Array<DragPreviewMode>;  差异内容：mode?: DragPreviewMode | Array<DragPreviewMode>; | component/common.d.ts |
| 新增API | NA | 类名：DragPreviewOptions；  API声明：modifier?: ImageModifier;  差异内容：modifier?: ImageModifier; | component/common.d.ts |
| 新增API | NA | 类名：DragPreviewOptions；  API声明：numberBadge?: boolean | number;  差异内容：numberBadge?: boolean | number; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface DragInteractionOptions  差异内容： declare interface DragInteractionOptions | component/common.d.ts |
| 新增API | NA | 类名：DragInteractionOptions；  API声明：isMultiSelectionEnabled?: boolean;  差异内容：isMultiSelectionEnabled?: boolean; | component/common.d.ts |
| 新增API | NA | 类名：DragInteractionOptions；  API声明：defaultAnimationBeforeLifting?: boolean;  差异内容：defaultAnimationBeforeLifting?: boolean; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface InvertOptions  差异内容： declare interface InvertOptions | component/common.d.ts |
| 新增API | NA | 类名：InvertOptions；  API声明：low: number;  差异内容：low: number; | component/common.d.ts |
| 新增API | NA | 类名：InvertOptions；  API声明：high: number;  差异内容：high: number; | component/common.d.ts |
| 新增API | NA | 类名：InvertOptions；  API声明：threshold: number;  差异内容：threshold: number; | component/common.d.ts |
| 新增API | NA | 类名：InvertOptions；  API声明：thresholdRange: number;  差异内容：thresholdRange: number; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type CircleShape = import('../api/@ohos.arkui.shape').CircleShape;  差异内容：declare type CircleShape = import('../api/@ohos.arkui.shape').CircleShape; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type EllipseShape = import('../api/@ohos.arkui.shape').EllipseShape;  差异内容：declare type EllipseShape = import('../api/@ohos.arkui.shape').EllipseShape; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type PathShape = import('../api/@ohos.arkui.shape').PathShape;  差异内容：declare type PathShape = import('../api/@ohos.arkui.shape').PathShape; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type RectShape = import('../api/@ohos.arkui.shape').RectShape;  差异内容：declare type RectShape = import('../api/@ohos.arkui.shape').RectShape; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type Optional<T> = T | undefined;  差异内容：declare type Optional<T> = T | undefined; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：drawModifier(modifier: DrawModifier | undefined): T;  差异内容：drawModifier(modifier: DrawModifier | undefined): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：customProperty(name: string, value: Optional<Object>): T;  差异内容：customProperty(name: string, value: Optional<Object>): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：expandSafeArea(types?: Array<SafeAreaType>, edges?: Array<SafeAreaEdge>): T;  差异内容：expandSafeArea(types?: Array<SafeAreaType>, edges?: Array<SafeAreaEdge>): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：mouseResponseRegion(value: Array<Rectangle> | Rectangle): T;  差异内容：mouseResponseRegion(value: Array<Rectangle> | Rectangle): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：onChildTouchTest(event: (value: Array<TouchTestInfo>) => TouchResult): T;  差异内容：onChildTouchTest(event: (value: Array<TouchTestInfo>) => TouchResult): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：background(builder: CustomBuilder, options?: {  align?: Alignment;  }): T;  差异内容：background(builder: CustomBuilder, options?: {  align?: Alignment;  }): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：pixelRound(value: PixelRoundPolicy): T;  差异内容：pixelRound(value: PixelRoundPolicy): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：backgroundEffect(options: BackgroundEffectOptions): T;  差异内容：backgroundEffect(options: BackgroundEffectOptions): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：backgroundImageResizable(value: ResizableOptions): T;  差异内容：backgroundImageResizable(value: ResizableOptions): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：foregroundEffect(options: ForegroundEffectOptions): T;  差异内容：foregroundEffect(options: ForegroundEffectOptions): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：visualEffect(effect: VisualEffect): T;  差异内容：visualEffect(effect: VisualEffect): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：backgroundFilter(filter: Filter): T;  差异内容：backgroundFilter(filter: Filter): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：foregroundFilter(filter: Filter): T;  差异内容：foregroundFilter(filter: Filter): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：compositingFilter(filter: Filter): T;  差异内容：compositingFilter(filter: Filter): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：foregroundBlurStyle(value: BlurStyle, options?: ForegroundBlurStyleOptions): T;  差异内容：foregroundBlurStyle(value: BlurStyle, options?: ForegroundBlurStyleOptions): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：outline(value: OutlineOptions): T;  差异内容：outline(value: OutlineOptions): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：outlineStyle(value: OutlineStyle | EdgeOutlineStyles): T;  差异内容：outlineStyle(value: OutlineStyle | EdgeOutlineStyles): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：outlineWidth(value: Dimension | EdgeOutlineWidths): T;  差异内容：outlineWidth(value: Dimension | EdgeOutlineWidths): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：outlineColor(value: ResourceColor | EdgeColors | LocalizedEdgeColors): T;  差异内容：outlineColor(value: ResourceColor | EdgeColors | LocalizedEdgeColors): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：outlineRadius(value: Dimension | OutlineRadiuses): T;  差异内容：outlineRadius(value: Dimension | OutlineRadiuses): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：foregroundColor(value: ResourceColor | ColoringStrategy): T;  差异内容：foregroundColor(value: ResourceColor | ColoringStrategy): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：onKeyPreIme(event: Callback<KeyEvent, boolean>): T;  差异内容：onKeyPreIme(event: Callback<KeyEvent, boolean>): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：focusBox(style: FocusBoxStyle): T;  差异内容：focusBox(style: FocusBoxStyle): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：linearGradientBlur(value: number, options: LinearGradientBlurOptions): T;  差异内容：linearGradientBlur(value: number, options: LinearGradientBlurOptions): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：motionBlur(value: MotionBlurOptions): T;  差异内容：motionBlur(value: MotionBlurOptions): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：systemBarEffect(): T;  差异内容：systemBarEffect(): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：useShadowBatching(value: boolean): T;  差异内容：useShadowBatching(value: boolean): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：useEffect(value: boolean): T;  差异内容：useEffect(value: boolean): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：renderGroup(value: boolean): T;  差异内容：renderGroup(value: boolean): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：freeze(value: boolean): T;  差异内容：freeze(value: boolean): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：onAttach(callback: Callback<void>): T;  差异内容：onAttach(callback: Callback<void>): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：onDetach(callback: Callback<void>): T;  差异内容：onDetach(callback: Callback<void>): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：chainMode(direction: Axis, style: ChainStyle): T;  差异内容：chainMode(direction: Axis, style: ChainStyle): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：clickEffect(value: ClickEffect | null): T;  差异内容：clickEffect(value: ClickEffect | null): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：onDragEnd(event: (event: DragEvent, extraParams?: string) => void): T;  差异内容：onDragEnd(event: (event: DragEvent, extraParams?: string) => void): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：allowDrop(value: Array<UniformDataType> | null): T;  差异内容：allowDrop(value: Array<UniformDataType> | null): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：draggable(value: boolean): T;  差异内容：draggable(value: boolean): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：dragPreview(value: CustomBuilder | DragItemInfo | string): T;  差异内容：dragPreview(value: CustomBuilder | DragItemInfo | string): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：dragPreviewOptions(value: DragPreviewOptions, options?: DragInteractionOptions): T;  差异内容：dragPreviewOptions(value: DragPreviewOptions, options?: DragInteractionOptions): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：onPreDrag(callback: Callback<PreDragStatus>): T;  差异内容：onPreDrag(callback: Callback<PreDragStatus>): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：blendMode(value: BlendMode, type?: BlendApplyType): T;  差异内容：blendMode(value: BlendMode, type?: BlendApplyType): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：clipShape(value: CircleShape | EllipseShape | PathShape | RectShape): T;  差异内容：clipShape(value: CircleShape | EllipseShape | PathShape | RectShape): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：maskShape(value: CircleShape | EllipseShape | PathShape | RectShape): T;  差异内容：maskShape(value: CircleShape | EllipseShape | PathShape | RectShape): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：bindContentCover(isShow: boolean, builder: CustomBuilder, type?: ModalTransition): T;  差异内容：bindContentCover(isShow: boolean, builder: CustomBuilder, type?: ModalTransition): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：bindContentCover(isShow: boolean, builder: CustomBuilder, options?: ContentCoverOptions): T;  差异内容：bindContentCover(isShow: boolean, builder: CustomBuilder, options?: ContentCoverOptions): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：bindSheet(isShow: boolean, builder: CustomBuilder, options?: SheetOptions): T;  差异内容：bindSheet(isShow: boolean, builder: CustomBuilder, options?: SheetOptions): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：sphericalEffect(value: number): T;  差异内容：sphericalEffect(value: number): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：lightUpEffect(value: number): T;  差异内容：lightUpEffect(value: number): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：pixelStretchEffect(options: PixelStretchEffectOptions): T;  差异内容：pixelStretchEffect(options: PixelStretchEffectOptions): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：keyboardShortcut(value: string | FunctionKey, keys: Array<ModifierKey>, action?: () => void): T;  差异内容：keyboardShortcut(value: string | FunctionKey, keys: Array<ModifierKey>, action?: () => void): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：accessibilityGroup(value: boolean): T;  差异内容：accessibilityGroup(value: boolean): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：accessibilityText(value: string): T;  差异内容：accessibilityText(value: string): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：accessibilityTextHint(value: string): T;  差异内容：accessibilityTextHint(value: string): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：accessibilityDescription(value: string): T;  差异内容：accessibilityDescription(value: string): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：accessibilityLevel(value: string): T;  差异内容：accessibilityLevel(value: string): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：accessibilityVirtualNode(builder: CustomBuilder): T;  差异内容：accessibilityVirtualNode(builder: CustomBuilder): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：obscured(reasons: Array<ObscuredReasons>): T;  差异内容：obscured(reasons: Array<ObscuredReasons>): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：reuseId(id: string): T;  差异内容：reuseId(id: string): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：renderFit(fitMode: RenderFit): T;  差异内容：renderFit(fitMode: RenderFit): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：attributeModifier(modifier: AttributeModifier<T>): T;  差异内容：attributeModifier(modifier: AttributeModifier<T>): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：gestureModifier(modifier: GestureModifier): T;  差异内容：gestureModifier(modifier: GestureModifier): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：backgroundBrightness(params: BackgroundBrightnessOptions): T;  差异内容：backgroundBrightness(params: BackgroundBrightnessOptions): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：onGestureJudgeBegin(callback: (gestureInfo: GestureInfo, event: BaseGestureEvent) => GestureJudgeResult): T;  差异内容：onGestureJudgeBegin(callback: (gestureInfo: GestureInfo, event: BaseGestureEvent) => GestureJudgeResult): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：onGestureRecognizerJudgeBegin(callback: GestureRecognizerJudgeBeginCallback): T;  差异内容：onGestureRecognizerJudgeBegin(callback: GestureRecognizerJudgeBeginCallback): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：shouldBuiltInRecognizerParallelWith(callback: ShouldBuiltInRecognizerParallelWithCallback): T;  差异内容：shouldBuiltInRecognizerParallelWith(callback: ShouldBuiltInRecognizerParallelWithCallback): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：monopolizeEvents(monopolize: boolean): T;  差异内容：monopolizeEvents(monopolize: boolean): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：onTouchIntercept(callback: Callback<TouchEvent, HitTestMode>): T;  差异内容：onTouchIntercept(callback: Callback<TouchEvent, HitTestMode>): T; | component/common.d.ts |
| 新增API | NA | 类名：CommonMethod；  API声明：onSizeChange(event: SizeChangeCallback): T;  差异内容：onSizeChange(event: SizeChangeCallback): T; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type FractionStop = [  number,  number  ];  差异内容：declare type FractionStop = [  number,  number  ]; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface PixelRoundPolicy  差异内容： declare interface PixelRoundPolicy | component/common.d.ts |
| 新增API | NA | 类名：PixelRoundPolicy；  API声明：start?: PixelRoundCalcPolicy;  差异内容：start?: PixelRoundCalcPolicy; | component/common.d.ts |
| 新增API | NA | 类名：PixelRoundPolicy；  API声明：top?: PixelRoundCalcPolicy;  差异内容：top?: PixelRoundCalcPolicy; | component/common.d.ts |
| 新增API | NA | 类名：PixelRoundPolicy；  API声明：end?: PixelRoundCalcPolicy;  差异内容：end?: PixelRoundCalcPolicy; | component/common.d.ts |
| 新增API | NA | 类名：PixelRoundPolicy；  API声明：bottom?: PixelRoundCalcPolicy;  差异内容：bottom?: PixelRoundCalcPolicy; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface LinearGradientBlurOptions  差异内容： declare interface LinearGradientBlurOptions | component/common.d.ts |
| 新增API | NA | 类名：LinearGradientBlurOptions；  API声明：fractionStops: FractionStop[];  差异内容：fractionStops: FractionStop[]; | component/common.d.ts |
| 新增API | NA | 类名：LinearGradientBlurOptions；  API声明：direction: GradientDirection;  差异内容：direction: GradientDirection; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface MotionBlurAnchor  差异内容： declare interface MotionBlurAnchor | component/common.d.ts |
| 新增API | NA | 类名：MotionBlurAnchor；  API声明：x: number;  差异内容：x: number; | component/common.d.ts |
| 新增API | NA | 类名：MotionBlurAnchor；  API声明：y: number;  差异内容：y: number; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface MotionBlurOptions  差异内容： declare interface MotionBlurOptions | component/common.d.ts |
| 新增API | NA | 类名：MotionBlurOptions；  API声明：radius: number;  差异内容：radius: number; | component/common.d.ts |
| 新增API | NA | 类名：MotionBlurOptions；  API声明：anchor: MotionBlurAnchor;  差异内容：anchor: MotionBlurAnchor; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface GeometryInfo  差异内容： declare interface GeometryInfo | component/common.d.ts |
| 新增API | NA | 类名：GeometryInfo；  API声明：borderWidth: EdgeWidth;  差异内容：borderWidth: EdgeWidth; | component/common.d.ts |
| 新增API | NA | 类名：GeometryInfo；  API声明：margin: Margin;  差异内容：margin: Margin; | component/common.d.ts |
| 新增API | NA | 类名：GeometryInfo；  API声明：padding: Padding;  差异内容：padding: Padding; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface Layoutable  差异内容： declare interface Layoutable | component/common.d.ts |
| 新增API | NA | 类名：Layoutable；  API声明：measureResult: MeasureResult;  差异内容：measureResult: MeasureResult; | component/common.d.ts |
| 新增API | NA | 类名：Layoutable；  API声明：layout(position: Position): void;  差异内容：layout(position: Position): void; | component/common.d.ts |
| 新增API | NA | 类名：Layoutable；  API声明：getMargin(): DirectionalEdgesT<number>;  差异内容：getMargin(): DirectionalEdgesT<number>; | component/common.d.ts |
| 新增API | NA | 类名：Layoutable；  API声明：getPadding(): DirectionalEdgesT<number>;  差异内容：getPadding(): DirectionalEdgesT<number>; | component/common.d.ts |
| 新增API | NA | 类名：Layoutable；  API声明：getBorderWidth(): DirectionalEdgesT<number>;  差异内容：getBorderWidth(): DirectionalEdgesT<number>; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface Measurable  差异内容： declare interface Measurable | component/common.d.ts |
| 新增API | NA | 类名：Measurable；  API声明：measure(constraint: ConstraintSizeOptions): MeasureResult;  差异内容：measure(constraint: ConstraintSizeOptions): MeasureResult; | component/common.d.ts |
| 新增API | NA | 类名：Measurable；  API声明：getMargin(): DirectionalEdgesT<number>;  差异内容：getMargin(): DirectionalEdgesT<number>; | component/common.d.ts |
| 新增API | NA | 类名：Measurable；  API声明：getPadding(): DirectionalEdgesT<number>;  差异内容：getPadding(): DirectionalEdgesT<number>; | component/common.d.ts |
| 新增API | NA | 类名：Measurable；  API声明：getBorderWidth(): DirectionalEdgesT<number>;  差异内容：getBorderWidth(): DirectionalEdgesT<number>; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface SizeResult  差异内容： declare interface SizeResult | component/common.d.ts |
| 新增API | NA | 类名：SizeResult；  API声明：width: number;  差异内容：width: number; | component/common.d.ts |
| 新增API | NA | 类名：SizeResult；  API声明：height: number;  差异内容：height: number; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface MeasureResult  差异内容： declare interface MeasureResult | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type NavDestinationInfo = import('../api/@ohos.arkui.observer').default.NavDestinationInfo;  差异内容：declare type NavDestinationInfo = import('../api/@ohos.arkui.observer').default.NavDestinationInfo; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type NavigationInfo = import('../api/@ohos.arkui.observer').default.NavigationInfo;  差异内容：declare type NavigationInfo = import('../api/@ohos.arkui.observer').default.NavigationInfo; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type RouterPageInfo = import('../api/@ohos.arkui.observer').default.RouterPageInfo;  差异内容：declare type RouterPageInfo = import('../api/@ohos.arkui.observer').default.RouterPageInfo; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type UIContext = import('../api/@ohos.arkui.UIContext').UIContext;  差异内容：declare type UIContext = import('../api/@ohos.arkui.UIContext').UIContext; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type DrawContext = import('../api/arkui/Graphics').DrawContext;  差异内容：declare type DrawContext = import('../api/arkui/Graphics').DrawContext; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type VisualEffect = import('../api/@ohos.graphics.uiEffect').default.VisualEffect;  差异内容：declare type VisualEffect = import('../api/@ohos.graphics.uiEffect').default.VisualEffect; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type Filter = import('../api/@ohos.graphics.uiEffect').default.Filter;  差异内容：declare type Filter = import('../api/@ohos.graphics.uiEffect').default.Filter; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type ComponentContent = import('../api/arkui/ComponentContent').ComponentContent;  差异内容：declare type ComponentContent = import('../api/arkui/ComponentContent').ComponentContent; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type Theme = import('../api/@ohos.arkui.theme').Theme;  差异内容：declare type Theme = import('../api/@ohos.arkui.theme').Theme; | component/common.d.ts |
| 新增API | NA | 类名：CustomComponent；  API声明：aboutToReuse?(params: {  [key: string]: unknown;  }): void;  差异内容：aboutToReuse?(params: {  [key: string]: unknown;  }): void; | component/common.d.ts |
| 新增API | NA | 类名：CustomComponent；  API声明：aboutToRecycle?(): void;  差异内容：aboutToRecycle?(): void; | component/common.d.ts |
| 新增API | NA | 类名：CustomComponent；  API声明：onWillApplyTheme?(theme: Theme): void;  差异内容：onWillApplyTheme?(theme: Theme): void; | component/common.d.ts |
| 新增API | NA | 类名：CustomComponent；  API声明：onPlaceChildren?(selfLayoutInfo: GeometryInfo, children: Array<Layoutable>, constraint: ConstraintSizeOptions): void;  差异内容：onPlaceChildren?(selfLayoutInfo: GeometryInfo, children: Array<Layoutable>, constraint: ConstraintSizeOptions): void; | component/common.d.ts |
| 新增API | NA | 类名：CustomComponent；  API声明：onMeasureSize?(selfLayoutInfo: GeometryInfo, children: Array<Measurable>, constraint: ConstraintSizeOptions): SizeResult;  差异内容：onMeasureSize?(selfLayoutInfo: GeometryInfo, children: Array<Measurable>, constraint: ConstraintSizeOptions): SizeResult; | component/common.d.ts |
| 新增API | NA | 类名：CustomComponent；  API声明：onFormRecycle?(): string;  差异内容：onFormRecycle?(): string; | component/common.d.ts |
| 新增API | NA | 类名：CustomComponent；  API声明：onFormRecover?(statusData: string): void;  差异内容：onFormRecover?(statusData: string): void; | component/common.d.ts |
| 新增API | NA | 类名：CustomComponent；  API声明：getUIContext(): UIContext;  差异内容：getUIContext(): UIContext; | component/common.d.ts |
| 新增API | NA | 类名：CustomComponent；  API声明：getUniqueId(): number;  差异内容：getUniqueId(): number; | component/common.d.ts |
| 新增API | NA | 类名：CustomComponent；  API声明：queryNavDestinationInfo(): NavDestinationInfo | undefined;  差异内容：queryNavDestinationInfo(): NavDestinationInfo | undefined; | component/common.d.ts |
| 新增API | NA | 类名：CustomComponent；  API声明：queryNavigationInfo(): NavigationInfo | undefined;  差异内容：queryNavigationInfo(): NavigationInfo | undefined; | component/common.d.ts |
| 新增API | NA | 类名：CustomComponent；  API声明：queryRouterPageInfo(): RouterPageInfo | undefined;  差异内容：queryRouterPageInfo(): RouterPageInfo | undefined; | component/common.d.ts |
| 新增API | NA | 类名：CustomComponent；  API声明：onDidBuild?(): void;  差异内容：onDidBuild?(): void; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface RectResult  差异内容： declare interface RectResult | component/common.d.ts |
| 新增API | NA | 类名：RectResult；  API声明：x: number;  差异内容：x: number; | component/common.d.ts |
| 新增API | NA | 类名：RectResult；  API声明：y: number;  差异内容：y: number; | component/common.d.ts |
| 新增API | NA | 类名：RectResult；  API声明：width: number;  差异内容：width: number; | component/common.d.ts |
| 新增API | NA | 类名：RectResult；  API声明：height: number;  差异内容：height: number; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface CaretOffset  差异内容： declare interface CaretOffset | component/common.d.ts |
| 新增API | NA | 类名：CaretOffset；  API声明：index: number;  差异内容：index: number; | component/common.d.ts |
| 新增API | NA | 类名：CaretOffset；  API声明：x: number;  差异内容：x: number; | component/common.d.ts |
| 新增API | NA | 类名：CaretOffset；  API声明：y: number;  差异内容：y: number; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare abstract class TextContentControllerBase  差异内容： declare abstract class TextContentControllerBase | component/common.d.ts |
| 新增API | NA | 类名：TextContentControllerBase；  API声明：getCaretOffset(): CaretOffset;  差异内容：getCaretOffset(): CaretOffset; | component/common.d.ts |
| 新增API | NA | 类名：TextContentControllerBase；  API声明：getTextContentRect(): RectResult;  差异内容：getTextContentRect(): RectResult; | component/common.d.ts |
| 新增API | NA | 类名：TextContentControllerBase；  API声明：getTextContentLineCount(): number;  差异内容：getTextContentLineCount(): number; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class ScrollableCommonMethod  差异内容： declare class ScrollableCommonMethod | component/common.d.ts |
| 新增API | NA | 类名：ScrollableCommonMethod；  API声明：scrollBar(barState: BarState): T;  差异内容：scrollBar(barState: BarState): T; | component/common.d.ts |
| 新增API | NA | 类名：ScrollableCommonMethod；  API声明：scrollBarColor(color: Color | number | string): T;  差异内容：scrollBarColor(color: Color | number | string): T; | component/common.d.ts |
| 新增API | NA | 类名：ScrollableCommonMethod；  API声明：scrollBarWidth(value: number | string): T;  差异内容：scrollBarWidth(value: number | string): T; | component/common.d.ts |
| 新增API | NA | 类名：ScrollableCommonMethod；  API声明：edgeEffect(edgeEffect: EdgeEffect, options?: EdgeEffectOptions): T;  差异内容：edgeEffect(edgeEffect: EdgeEffect, options?: EdgeEffectOptions): T; | component/common.d.ts |
| 新增API | NA | 类名：ScrollableCommonMethod；  API声明：nestedScroll(value: NestedScrollOptions): T;  差异内容：nestedScroll(value: NestedScrollOptions): T; | component/common.d.ts |
| 新增API | NA | 类名：ScrollableCommonMethod；  API声明：enableScrollInteraction(value: boolean): T;  差异内容：enableScrollInteraction(value: boolean): T; | component/common.d.ts |
| 新增API | NA | 类名：ScrollableCommonMethod；  API声明：friction(value: number | Resource): T;  差异内容：friction(value: number | Resource): T; | component/common.d.ts |
| 新增API | NA | 类名：ScrollableCommonMethod；  API声明：onScroll(event: (scrollOffset: number, scrollState: ScrollState) => void): T;  差异内容：onScroll(event: (scrollOffset: number, scrollState: ScrollState) => void): T; | component/common.d.ts |
| 新增API | NA | 类名：ScrollableCommonMethod；  API声明：onWillScroll(handler: Optional<OnWillScrollCallback>): T;  差异内容：onWillScroll(handler: Optional<OnWillScrollCallback>): T; | component/common.d.ts |
| 新增API | NA | 类名：ScrollableCommonMethod；  API声明：onDidScroll(handler: OnScrollCallback): T;  差异内容：onDidScroll(handler: OnScrollCallback): T; | component/common.d.ts |
| 新增API | NA | 类名：ScrollableCommonMethod；  API声明：onReachStart(event: () => void): T;  差异内容：onReachStart(event: () => void): T; | component/common.d.ts |
| 新增API | NA | 类名：ScrollableCommonMethod；  API声明：onReachEnd(event: () => void): T;  差异内容：onReachEnd(event: () => void): T; | component/common.d.ts |
| 新增API | NA | 类名：ScrollableCommonMethod；  API声明：onScrollStart(event: () => void): T;  差异内容：onScrollStart(event: () => void): T; | component/common.d.ts |
| 新增API | NA | 类名：ScrollableCommonMethod；  API声明：onScrollStop(event: () => void): T;  差异内容：onScrollStop(event: () => void): T; | component/common.d.ts |
| 新增API | NA | 类名：ScrollableCommonMethod；  API声明：flingSpeedLimit(speedLimit: number): T;  差异内容：flingSpeedLimit(speedLimit: number): T; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class ScrollResult  差异内容： declare class ScrollResult | component/common.d.ts |
| 新增API | NA | 类名：ScrollResult；  API声明：offsetRemain: number;  差异内容：offsetRemain: number; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type OnWillScrollCallback = (scrollOffset: number, scrollState: ScrollState, scrollSource: ScrollSource) => void | ScrollResult;  差异内容：declare type OnWillScrollCallback = (scrollOffset: number, scrollState: ScrollState, scrollSource: ScrollSource) => void | ScrollResult; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type OnScrollCallback = (scrollOffset: number, scrollState: ScrollState) => void;  差异内容：declare type OnScrollCallback = (scrollOffset: number, scrollState: ScrollState) => void; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface EdgeEffectOptions  差异内容： declare interface EdgeEffectOptions | component/common.d.ts |
| 新增API | NA | 类名：EdgeEffectOptions；  API声明：alwaysEnabled: boolean;  差异内容：alwaysEnabled: boolean; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class ChildrenMainSize  差异内容： declare class ChildrenMainSize | component/common.d.ts |
| 新增API | NA | 类名：ChildrenMainSize；  API声明：splice(start: number, deleteCount?: number, childrenSize?: Array<number>): void;  差异内容：splice(start: number, deleteCount?: number, childrenSize?: Array<number>): void; | component/common.d.ts |
| 新增API | NA | 类名：ChildrenMainSize；  API声明：update(index: number, childSize: number): void;  差异内容：update(index: number, childSize: number): void; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface BackgroundBrightnessOptions  差异内容： declare interface BackgroundBrightnessOptions | component/common.d.ts |
| 新增API | NA | 类名：BackgroundBrightnessOptions；  API声明：rate: number;  差异内容：rate: number; | component/common.d.ts |
| 新增API | NA | 类名：BackgroundBrightnessOptions；  API声明：lightUpDegree: number;  差异内容：lightUpDegree: number; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare function wrapBuilder<Args extends Object[]>(builder: (...args: Args) => void): WrappedBuilder<Args>;  差异内容：declare function wrapBuilder<Args extends Object[]>(builder: (...args: Args) => void): WrappedBuilder<Args>; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class WrappedBuilder  差异内容： declare class WrappedBuilder | component/common.d.ts |
| 新增API | NA | 类名：WrappedBuilder；  API声明：builder: (...args: Args) => void;  差异内容：builder: (...args: Args) => void; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface KeyframeAnimateParam  差异内容： declare interface KeyframeAnimateParam | component/common.d.ts |
| 新增API | NA | 类名：KeyframeAnimateParam；  API声明：delay?: number;  差异内容：delay?: number; | component/common.d.ts |
| 新增API | NA | 类名：KeyframeAnimateParam；  API声明：iterations?: number;  差异内容：iterations?: number; | component/common.d.ts |
| 新增API | NA | 类名：KeyframeAnimateParam；  API声明：onFinish?: () => void;  差异内容：onFinish?: () => void; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface KeyframeState  差异内容： declare interface KeyframeState | component/common.d.ts |
| 新增API | NA | 类名：KeyframeState；  API声明：duration: number;  差异内容：duration: number; | component/common.d.ts |
| 新增API | NA | 类名：KeyframeState；  API声明：curve?: Curve | string | ICurve;  差异内容：curve?: Curve | string | ICurve; | component/common.d.ts |
| 新增API | NA | 类名：KeyframeState；  API声明：event: () => void;  差异内容：event: () => void; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface Callback  差异内容： declare interface Callback | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type HoverCallback = (isHover: boolean, event: HoverEvent) => void;  差异内容：declare type HoverCallback = (isHover: boolean, event: HoverEvent) => void; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface VisibleAreaEventOptions  差异内容： declare interface VisibleAreaEventOptions | component/common.d.ts |
| 新增API | NA | 类名：VisibleAreaEventOptions；  API声明：ratios: Array<number>;  差异内容：ratios: Array<number>; | component/common.d.ts |
| 新增API | NA | 类名：VisibleAreaEventOptions；  API声明：expectedUpdateInterval?: number;  差异内容：expectedUpdateInterval?: number; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type VisibleAreaChangeCallback = (isVisible: boolean, currentRatio: number) => void;  差异内容：declare type VisibleAreaChangeCallback = (isVisible: boolean, currentRatio: number) => void; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface UICommonEvent  差异内容： declare interface UICommonEvent | component/common.d.ts |
| 新增API | NA | 类名：UICommonEvent；  API声明：setOnClick(callback: Callback<ClickEvent> | undefined): void;  差异内容：setOnClick(callback: Callback<ClickEvent> | undefined): void; | component/common.d.ts |
| 新增API | NA | 类名：UICommonEvent；  API声明：setOnTouch(callback: Callback<TouchEvent> | undefined): void;  差异内容：setOnTouch(callback: Callback<TouchEvent> | undefined): void; | component/common.d.ts |
| 新增API | NA | 类名：UICommonEvent；  API声明：setOnAppear(callback: Callback<void> | undefined): void;  差异内容：setOnAppear(callback: Callback<void> | undefined): void; | component/common.d.ts |
| 新增API | NA | 类名：UICommonEvent；  API声明：setOnDisappear(callback: Callback<void> | undefined): void;  差异内容：setOnDisappear(callback: Callback<void> | undefined): void; | component/common.d.ts |
| 新增API | NA | 类名：UICommonEvent；  API声明：setOnKeyEvent(callback: Callback<KeyEvent> | undefined): void;  差异内容：setOnKeyEvent(callback: Callback<KeyEvent> | undefined): void; | component/common.d.ts |
| 新增API | NA | 类名：UICommonEvent；  API声明：setOnFocus(callback: Callback<void> | undefined): void;  差异内容：setOnFocus(callback: Callback<void> | undefined): void; | component/common.d.ts |
| 新增API | NA | 类名：UICommonEvent；  API声明：setOnBlur(callback: Callback<void> | undefined): void;  差异内容：setOnBlur(callback: Callback<void> | undefined): void; | component/common.d.ts |
| 新增API | NA | 类名：UICommonEvent；  API声明：setOnHover(callback: HoverCallback | undefined): void;  差异内容：setOnHover(callback: HoverCallback | undefined): void; | component/common.d.ts |
| 新增API | NA | 类名：UICommonEvent；  API声明：setOnMouse(callback: Callback<MouseEvent> | undefined): void;  差异内容：setOnMouse(callback: Callback<MouseEvent> | undefined): void; | component/common.d.ts |
| 新增API | NA | 类名：UICommonEvent；  API声明：setOnSizeChange(callback: SizeChangeCallback | undefined): void;  差异内容：setOnSizeChange(callback: SizeChangeCallback | undefined): void; | component/common.d.ts |
| 新增API | NA | 类名：UICommonEvent；  API声明：setOnVisibleAreaApproximateChange(options: VisibleAreaEventOptions, event: VisibleAreaChangeCallback | undefined): void;  差异内容：setOnVisibleAreaApproximateChange(options: VisibleAreaEventOptions, event: VisibleAreaChangeCallback | undefined): void; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface UIGestureEvent  差异内容： declare interface UIGestureEvent | component/common.d.ts |
| 新增API | NA | 类名：UIGestureEvent；  API声明：addGesture<T>(gesture: GestureHandler<T>, priority?: GesturePriority, mask?: GestureMask): void;  差异内容：addGesture<T>(gesture: GestureHandler<T>, priority?: GesturePriority, mask?: GestureMask): void; | component/common.d.ts |
| 新增API | NA | 类名：UIGestureEvent；  API声明：addParallelGesture<T>(gesture: GestureHandler<T>, mask?: GestureMask): void;  差异内容：addParallelGesture<T>(gesture: GestureHandler<T>, mask?: GestureMask): void; | component/common.d.ts |
| 新增API | NA | 类名：UIGestureEvent；  API声明：removeGestureByTag(tag: string): void;  差异内容：removeGestureByTag(tag: string): void; | component/common.d.ts |
| 新增API | NA | 类名：UIGestureEvent；  API声明：clearGestures(): void;  差异内容：clearGestures(): void; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface GestureModifier  差异内容： declare interface GestureModifier | component/common.d.ts |
| 新增API | NA | 类名：GestureModifier；  API声明：applyGesture(event: UIGestureEvent): void;  差异内容：applyGesture(event: UIGestureEvent): void; | component/common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface SelectionOptions  差异内容： declare interface SelectionOptions | component/common.d.ts |
| 新增API | NA | 类名：SelectionOptions；  API声明：menuPolicy?: MenuPolicy;  差异内容：menuPolicy?: MenuPolicy; | component/common.d.ts |
| 新增API | NA | 类名：AppStorage；  API声明：static ref<T>(propName: string): AbstractProperty<T> | undefined;  差异内容：static ref<T>(propName: string): AbstractProperty<T> | undefined; | component/common\_ts\_ets\_api.d.ts |
| 新增API | NA | 类名：AppStorage；  API声明：static setAndRef<T>(propName: string, defaultValue: T): AbstractProperty<T>;  差异内容：static setAndRef<T>(propName: string, defaultValue: T): AbstractProperty<T>; | component/common\_ts\_ets\_api.d.ts |
| 新增API | NA | 类名：AppStorage；  API声明：static link<T>(propName: string): SubscribedAbstractProperty<T>;  差异内容：static link<T>(propName: string): SubscribedAbstractProperty<T>; | component/common\_ts\_ets\_api.d.ts |
| 新增API | NA | 类名：AppStorage；  API声明：static setAndLink<T>(propName: string, defaultValue: T): SubscribedAbstractProperty<T>;  差异内容：static setAndLink<T>(propName: string, defaultValue: T): SubscribedAbstractProperty<T>; | component/common\_ts\_ets\_api.d.ts |
| 新增API | NA | 类名：AppStorage；  API声明：static prop<T>(propName: string): SubscribedAbstractProperty<T>;  差异内容：static prop<T>(propName: string): SubscribedAbstractProperty<T>; | component/common\_ts\_ets\_api.d.ts |
| 新增API | NA | 类名：AppStorage；  API声明：static setAndProp<T>(propName: string, defaultValue: T): SubscribedAbstractProperty<T>;  差异内容：static setAndProp<T>(propName: string, defaultValue: T): SubscribedAbstractProperty<T>; | component/common\_ts\_ets\_api.d.ts |
| 新增API | NA | 类名：AppStorage；  API声明：static has(propName: string): boolean;  差异内容：static has(propName: string): boolean; | component/common\_ts\_ets\_api.d.ts |
| 新增API | NA | 类名：AppStorage；  API声明：static get<T>(propName: string): T | undefined;  差异内容：static get<T>(propName: string): T | undefined; | component/common\_ts\_ets\_api.d.ts |
| 新增API | NA | 类名：AppStorage；  API声明：static set<T>(propName: string, newValue: T): boolean;  差异内容：static set<T>(propName: string, newValue: T): boolean; | component/common\_ts\_ets\_api.d.ts |
| 新增API | NA | 类名：AppStorage；  API声明：static setOrCreate<T>(propName: string, newValue: T): void;  差异内容：static setOrCreate<T>(propName: string, newValue: T): void; | component/common\_ts\_ets\_api.d.ts |
| 新增API | NA | 类名：AppStorage；  API声明：static delete(propName: string): boolean;  差异内容：static delete(propName: string): boolean; | component/common\_ts\_ets\_api.d.ts |
| 新增API | NA | 类名：AppStorage；  API声明：static keys(): IterableIterator<string>;  差异内容：static keys(): IterableIterator<string>; | component/common\_ts\_ets\_api.d.ts |
| 新增API | NA | 类名：AppStorage；  API声明：static clear(): boolean;  差异内容：static clear(): boolean; | component/common\_ts\_ets\_api.d.ts |
| 新增API | NA | 类名：AppStorage；  API声明：static size(): number;  差异内容：static size(): number; | component/common\_ts\_ets\_api.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface AbstractProperty  差异内容： declare interface AbstractProperty | component/common\_ts\_ets\_api.d.ts |
| 新增API | NA | 类名：AbstractProperty；  API声明：get(): T;  差异内容：get(): T; | component/common\_ts\_ets\_api.d.ts |
| 新增API | NA | 类名：AbstractProperty；  API声明：set(newValue: T): void;  差异内容：set(newValue: T): void; | component/common\_ts\_ets\_api.d.ts |
| 新增API | NA | 类名：AbstractProperty；  API声明：info(): string;  差异内容：info(): string; | component/common\_ts\_ets\_api.d.ts |
| 新增API | NA | 类名：SubscribedAbstractProperty；  API声明：info(): string;  差异内容：info(): string; | component/common\_ts\_ets\_api.d.ts |
| 新增API | NA | 类名：SubscribedAbstractProperty；  API声明：abstract aboutToBeDeleted(): void;  差异内容：abstract aboutToBeDeleted(): void; | component/common\_ts\_ets\_api.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface EnvPropsOptions  差异内容： declare interface EnvPropsOptions | component/common\_ts\_ets\_api.d.ts |
| 新增API | NA | 类名：EnvPropsOptions；  API声明：key: string;  差异内容：key: string; | component/common\_ts\_ets\_api.d.ts |
| 新增API | NA | 类名：EnvPropsOptions；  API声明：defaultValue: number | string | boolean;  差异内容：defaultValue: number | string | boolean; | component/common\_ts\_ets\_api.d.ts |
| 新增API | NA | 类名：Environment；  API声明：static envProp<S>(key: string, value: S): boolean;  差异内容：static envProp<S>(key: string, value: S): boolean; | component/common\_ts\_ets\_api.d.ts |
| 新增API | NA | 类名：Environment；  API声明：static envProps(props: EnvPropsOptions[]): void;  差异内容：static envProps(props: EnvPropsOptions[]): void; | component/common\_ts\_ets\_api.d.ts |
| 新增API | NA | 类名：Environment；  API声明：static keys(): Array<string>;  差异内容：static keys(): Array<string>; | component/common\_ts\_ets\_api.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface PersistPropsOptions  差异内容： declare interface PersistPropsOptions | component/common\_ts\_ets\_api.d.ts |
| 新增API | NA | 类名：PersistPropsOptions；  API声明：key: string;  差异内容：key: string; | component/common\_ts\_ets\_api.d.ts |
| 新增API | NA | 类名：PersistPropsOptions；  API声明：defaultValue: number | string | boolean | Object;  差异内容：defaultValue: number | string | boolean | Object; | component/common\_ts\_ets\_api.d.ts |
| 新增API | NA | 类名：PersistentStorage；  API声明：static persistProp<T>(key: string, defaultValue: T): void;  差异内容：static persistProp<T>(key: string, defaultValue: T): void; | component/common\_ts\_ets\_api.d.ts |
| 新增API | NA | 类名：PersistentStorage；  API声明：static deleteProp(key: string): void;  差异内容：static deleteProp(key: string): void; | component/common\_ts\_ets\_api.d.ts |
| 新增API | NA | 类名：PersistentStorage；  API声明：static persistProps(props: PersistPropsOptions[]): void;  差异内容：static persistProps(props: PersistPropsOptions[]): void; | component/common\_ts\_ets\_api.d.ts |
| 新增API | NA | 类名：PersistentStorage；  API声明：static keys(): Array<string>;  差异内容：static keys(): Array<string>; | component/common\_ts\_ets\_api.d.ts |
| 新增API | NA | 类名：LocalStorage；  API声明：static getShared(): LocalStorage;  差异内容：static getShared(): LocalStorage; | component/common\_ts\_ets\_api.d.ts |
| 新增API | NA | 类名：LocalStorage；  API声明：public ref<T>(propName: string): AbstractProperty<T> | undefined;  差异内容：public ref<T>(propName: string): AbstractProperty<T> | undefined; | component/common\_ts\_ets\_api.d.ts |
| 新增API | NA | 类名：LocalStorage；  API声明：public setAndRef<T>(propName: string, defaultValue: T): AbstractProperty<T>;  差异内容：public setAndRef<T>(propName: string, defaultValue: T): AbstractProperty<T>; | component/common\_ts\_ets\_api.d.ts |
| 新增API | NA | 类名：CounterAttribute；  API声明：enableDec(value: boolean): CounterAttribute;  差异内容：enableDec(value: boolean): CounterAttribute; | component/counter.d.ts |
| 新增API | NA | 类名：CounterAttribute；  API声明：enableInc(value: boolean): CounterAttribute;  差异内容：enableInc(value: boolean): CounterAttribute; | component/counter.d.ts |
| 新增API | NA | 类名：CustomDialogControllerOptions；  API声明：maskColor?: ResourceColor;  差异内容：maskColor?: ResourceColor; | component/custom\_dialog\_controller.d.ts |
| 新增API | NA | 类名：CustomDialogControllerOptions；  API声明：maskRect?: Rectangle;  差异内容：maskRect?: Rectangle; | component/custom\_dialog\_controller.d.ts |
| 新增API | NA | 类名：CustomDialogControllerOptions；  API声明：openAnimation?: AnimateParam;  差异内容：openAnimation?: AnimateParam; | component/custom\_dialog\_controller.d.ts |
| 新增API | NA | 类名：CustomDialogControllerOptions；  API声明：closeAnimation?: AnimateParam;  差异内容：closeAnimation?: AnimateParam; | component/custom\_dialog\_controller.d.ts |
| 新增API | NA | 类名：CustomDialogControllerOptions；  API声明：showInSubWindow?: boolean;  差异内容：showInSubWindow?: boolean; | component/custom\_dialog\_controller.d.ts |
| 新增API | NA | 类名：CustomDialogControllerOptions；  API声明：backgroundColor?: ResourceColor;  差异内容：backgroundColor?: ResourceColor; | component/custom\_dialog\_controller.d.ts |
| 新增API | NA | 类名：CustomDialogControllerOptions；  API声明：cornerRadius?: Dimension | BorderRadiuses;  差异内容：cornerRadius?: Dimension | BorderRadiuses; | component/custom\_dialog\_controller.d.ts |
| 新增API | NA | 类名：CustomDialogControllerOptions；  API声明：isModal?: boolean;  差异内容：isModal?: boolean; | component/custom\_dialog\_controller.d.ts |
| 新增API | NA | 类名：CustomDialogControllerOptions；  API声明：onWillDismiss?: Callback<DismissDialogAction>;  差异内容：onWillDismiss?: Callback<DismissDialogAction>; | component/custom\_dialog\_controller.d.ts |
| 新增API | NA | 类名：CustomDialogControllerOptions；  API声明：width?: Dimension;  差异内容：width?: Dimension; | component/custom\_dialog\_controller.d.ts |
| 新增API | NA | 类名：CustomDialogControllerOptions；  API声明：height?: Dimension;  差异内容：height?: Dimension; | component/custom\_dialog\_controller.d.ts |
| 新增API | NA | 类名：CustomDialogControllerOptions；  API声明：borderWidth?: Dimension | EdgeWidths;  差异内容：borderWidth?: Dimension | EdgeWidths; | component/custom\_dialog\_controller.d.ts |
| 新增API | NA | 类名：CustomDialogControllerOptions；  API声明：borderColor?: ResourceColor | EdgeColors;  差异内容：borderColor?: ResourceColor | EdgeColors; | component/custom\_dialog\_controller.d.ts |
| 新增API | NA | 类名：CustomDialogControllerOptions；  API声明：borderStyle?: BorderStyle | EdgeStyles;  差异内容：borderStyle?: BorderStyle | EdgeStyles; | component/custom\_dialog\_controller.d.ts |
| 新增API | NA | 类名：CustomDialogControllerOptions；  API声明：shadow?: ShadowOptions | ShadowStyle;  差异内容：shadow?: ShadowOptions | ShadowStyle; | component/custom\_dialog\_controller.d.ts |
| 新增API | NA | 类名：CustomDialogControllerOptions；  API声明：backgroundBlurStyle?: BlurStyle;  差异内容：backgroundBlurStyle?: BlurStyle; | component/custom\_dialog\_controller.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface DismissDialogAction  差异内容： declare interface DismissDialogAction | component/custom\_dialog\_controller.d.ts |
| 新增API | NA | 类名：DismissDialogAction；  API声明：dismiss: Callback<void>;  差异内容：dismiss: Callback<void>; | component/custom\_dialog\_controller.d.ts |
| 新增API | NA | 类名：DismissDialogAction；  API声明：reason: DismissReason;  差异内容：reason: DismissReason; | component/custom\_dialog\_controller.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type ColorStop = {  /  **\* Color property.**  **\* @type { ResourceColor } color - the color value.**  **\* @syscap SystemCapability.ArkUI.ArkUI.Full**  **\* @crossplatform**  **\* @since 10**  **\*/**  **/\*\***  **\* Color property.**  **\* @type { ResourceColor } color - the color value.**  **\* @syscap SystemCapability.ArkUI.ArkUI.Full**  **\* @crossplatform**  **\* @atomicservice**  **\* @since 11**  **\*/**  **color: ResourceColor;**  **/**    \* Offset property.  \* @type { Length } offset - the color offset.  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 10  \*/  /  **\* Offset property.**  **\* @type { Length } offset - the color offset.**  **\* @syscap SystemCapability.ArkUI.ArkUI.Full**  **\* @crossplatform**  **\* @atomicservice**  **\* @since 11**  **\*/**  **offset: Length;**  **};**  **差异内容：declare type ColorStop = {**  **/\*\***  **\* Color property.**  **\* @type { ResourceColor } color - the color value.**  **\* @syscap SystemCapability.ArkUI.ArkUI.Full**  **\* @crossplatform**  **\* @since 10**  **\*/**  **/**    \* Color property.  \* @type { ResourceColor } color - the color value.  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @atomicservice  \* @since 11  \*/  color: ResourceColor;  /\*\*  \* Offset property.  \* @type { Length } offset - the color offset.  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 10  \*/  /\*\*  \* Offset property.  \* @type { Length } offset - the color offset.  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @atomicservice  \* @since 11  \*/  offset: Length;  }; | component/data\_panel.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class LinearGradient  差异内容： declare class LinearGradient | component/data\_panel.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface DataPanelShadowOptions  差异内容： declare interface DataPanelShadowOptions | component/data\_panel.d.ts |
| 新增API | NA | 类名：DataPanelShadowOptions；  API声明：colors?: Array<ResourceColor | LinearGradient>;  差异内容：colors?: Array<ResourceColor | LinearGradient>; | component/data\_panel.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface DataPanelConfiguration  差异内容： declare interface DataPanelConfiguration | component/data\_panel.d.ts |
| 新增API | NA | 类名：DataPanelConfiguration；  API声明：values: number[];  差异内容：values: number[]; | component/data\_panel.d.ts |
| 新增API | NA | 类名：DataPanelConfiguration；  API声明：maxValue: number;  差异内容：maxValue: number; | component/data\_panel.d.ts |
| 新增API | NA | 类名：DataPanelAttribute；  API声明：valueColors(value: Array<ResourceColor | LinearGradient>): DataPanelAttribute;  差异内容：valueColors(value: Array<ResourceColor | LinearGradient>): DataPanelAttribute; | component/data\_panel.d.ts |
| 新增API | NA | 类名：DataPanelAttribute；  API声明：trackBackgroundColor(value: ResourceColor): DataPanelAttribute;  差异内容：trackBackgroundColor(value: ResourceColor): DataPanelAttribute; | component/data\_panel.d.ts |
| 新增API | NA | 类名：DataPanelAttribute；  API声明：strokeWidth(value: Length): DataPanelAttribute;  差异内容：strokeWidth(value: Length): DataPanelAttribute; | component/data\_panel.d.ts |
| 新增API | NA | 类名：DataPanelAttribute；  API声明：trackShadow(value: DataPanelShadowOptions): DataPanelAttribute;  差异内容：trackShadow(value: DataPanelShadowOptions): DataPanelAttribute; | component/data\_panel.d.ts |
| 新增API | NA | 类名：DataPanelAttribute；  API声明：contentModifier(modifier: ContentModifier<DataPanelConfiguration>): DataPanelAttribute;  差异内容：contentModifier(modifier: ContentModifier<DataPanelConfiguration>): DataPanelAttribute; | component/data\_panel.d.ts |
| 新增API | NA | 类名：DatePickerAttribute；  API声明：disappearTextStyle(value: PickerTextStyle): DatePickerAttribute;  差异内容：disappearTextStyle(value: PickerTextStyle): DatePickerAttribute; | component/date\_picker.d.ts |
| 新增API | NA | 类名：DatePickerAttribute；  API声明：textStyle(value: PickerTextStyle): DatePickerAttribute;  差异内容：textStyle(value: PickerTextStyle): DatePickerAttribute; | component/date\_picker.d.ts |
| 新增API | NA | 类名：DatePickerAttribute；  API声明：selectedTextStyle(value: PickerTextStyle): DatePickerAttribute;  差异内容：selectedTextStyle(value: PickerTextStyle): DatePickerAttribute; | component/date\_picker.d.ts |
| 新增API | NA | 类名：DatePickerAttribute；  API声明：onDateChange(callback: (value: Date) => void): DatePickerAttribute;  差异内容：onDateChange(callback: (value: Date) => void): DatePickerAttribute; | component/date\_picker.d.ts |
| 新增API | NA | 类名：DatePickerDialogOptions；  API声明：lunarSwitch?: boolean;  差异内容：lunarSwitch?: boolean; | component/date\_picker.d.ts |
| 新增API | NA | 类名：DatePickerDialogOptions；  API声明：showTime?: boolean;  差异内容：showTime?: boolean; | component/date\_picker.d.ts |
| 新增API | NA | 类名：DatePickerDialogOptions；  API声明：useMilitaryTime?: boolean;  差异内容：useMilitaryTime?: boolean; | component/date\_picker.d.ts |
| 新增API | NA | 类名：DatePickerDialogOptions；  API声明：disappearTextStyle?: PickerTextStyle;  差异内容：disappearTextStyle?: PickerTextStyle; | component/date\_picker.d.ts |
| 新增API | NA | 类名：DatePickerDialogOptions；  API声明：textStyle?: PickerTextStyle;  差异内容：textStyle?: PickerTextStyle; | component/date\_picker.d.ts |
| 新增API | NA | 类名：DatePickerDialogOptions；  API声明：acceptButtonStyle?: PickerDialogButtonStyle;  差异内容：acceptButtonStyle?: PickerDialogButtonStyle; | component/date\_picker.d.ts |
| 新增API | NA | 类名：DatePickerDialogOptions；  API声明：cancelButtonStyle?: PickerDialogButtonStyle;  差异内容：cancelButtonStyle?: PickerDialogButtonStyle; | component/date\_picker.d.ts |
| 新增API | NA | 类名：DatePickerDialogOptions；  API声明：selectedTextStyle?: PickerTextStyle;  差异内容：selectedTextStyle?: PickerTextStyle; | component/date\_picker.d.ts |
| 新增API | NA | 类名：DatePickerDialogOptions；  API声明：maskRect?: Rectangle;  差异内容：maskRect?: Rectangle; | component/date\_picker.d.ts |
| 新增API | NA | 类名：DatePickerDialogOptions；  API声明：alignment?: DialogAlignment;  差异内容：alignment?: DialogAlignment; | component/date\_picker.d.ts |
| 新增API | NA | 类名：DatePickerDialogOptions；  API声明：offset?: Offset;  差异内容：offset?: Offset; | component/date\_picker.d.ts |
| 新增API | NA | 类名：DatePickerDialogOptions；  API声明：onDateAccept?: (value: Date) => void;  差异内容：onDateAccept?: (value: Date) => void; | component/date\_picker.d.ts |
| 新增API | NA | 类名：DatePickerDialogOptions；  API声明：onDateChange?: (value: Date) => void;  差异内容：onDateChange?: (value: Date) => void; | component/date\_picker.d.ts |
| 新增API | NA | 类名：DatePickerDialogOptions；  API声明：backgroundColor?: ResourceColor;  差异内容：backgroundColor?: ResourceColor; | component/date\_picker.d.ts |
| 新增API | NA | 类名：DatePickerDialogOptions；  API声明：backgroundBlurStyle?: BlurStyle;  差异内容：backgroundBlurStyle?: BlurStyle; | component/date\_picker.d.ts |
| 新增API | NA | 类名：DatePickerDialogOptions；  API声明：onDidAppear?: () => void;  差异内容：onDidAppear?: () => void; | component/date\_picker.d.ts |
| 新增API | NA | 类名：DatePickerDialogOptions；  API声明：onDidDisappear?: () => void;  差异内容：onDidDisappear?: () => void; | component/date\_picker.d.ts |
| 新增API | NA | 类名：DatePickerDialogOptions；  API声明：onWillAppear?: () => void;  差异内容：onWillAppear?: () => void; | component/date\_picker.d.ts |
| 新增API | NA | 类名：DatePickerDialogOptions；  API声明：onWillDisappear?: () => void;  差异内容：onWillDisappear?: () => void; | component/date\_picker.d.ts |
| 新增API | NA | 类名：DatePickerDialogOptions；  API声明：shadow?: ShadowOptions | ShadowStyle;  差异内容：shadow?: ShadowOptions | ShadowStyle; | component/date\_picker.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum CheckBoxShape  差异内容： declare enum CheckBoxShape | component/enums.d.ts |
| 新增API | NA | 类名：CheckBoxShape；  API声明：CIRCLE = 0  差异内容：CIRCLE = 0 | component/enums.d.ts |
| 新增API | NA | 类名：CheckBoxShape；  API声明：ROUNDED\_SQUARE = 1  差异内容：ROUNDED\_SQUARE = 1 | component/enums.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum ColoringStrategy  差异内容： declare enum ColoringStrategy | component/enums.d.ts |
| 新增API | NA | 类名：ColoringStrategy；  API声明：INVERT = 'invert'  差异内容：INVERT = 'invert' | component/enums.d.ts |
| 新增API | NA | 类名：ColoringStrategy；  API声明：AVERAGE = 'average'  差异内容：AVERAGE = 'average' | component/enums.d.ts |
| 新增API | NA | 类名：ColoringStrategy；  API声明：PRIMARY = 'primary'  差异内容：PRIMARY = 'primary' | component/enums.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum PixelRoundCalcPolicy  差异内容： declare enum PixelRoundCalcPolicy | component/enums.d.ts |
| 新增API | NA | 类名：PixelRoundCalcPolicy；  API声明：NO\_FORCE\_ROUND = 0  差异内容：NO\_FORCE\_ROUND = 0 | component/enums.d.ts |
| 新增API | NA | 类名：PixelRoundCalcPolicy；  API声明：FORCE\_CEIL = 1  差异内容：FORCE\_CEIL = 1 | component/enums.d.ts |
| 新增API | NA | 类名：PixelRoundCalcPolicy；  API声明：FORCE\_FLOOR = 2  差异内容：FORCE\_FLOOR = 2 | component/enums.d.ts |
| 新增API | NA | 类名：ImageSize；  API声明：FILL = 3  差异内容：FILL = 3 | component/enums.d.ts |
| 新增API | NA | 类名：TextAlign；  API声明：JUSTIFY  差异内容：JUSTIFY | component/enums.d.ts |
| 新增API | NA | 类名：TextOverflow；  API声明：MARQUEE  差异内容：MARQUEE | component/enums.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum TextHeightAdaptivePolicy  差异内容： declare enum TextHeightAdaptivePolicy | component/enums.d.ts |
| 新增API | NA | 类名：TextHeightAdaptivePolicy；  API声明：MAX\_LINES\_FIRST  差异内容：MAX\_LINES\_FIRST | component/enums.d.ts |
| 新增API | NA | 类名：TextHeightAdaptivePolicy；  API声明：MIN\_FONT\_SIZE\_FIRST  差异内容：MIN\_FONT\_SIZE\_FIRST | component/enums.d.ts |
| 新增API | NA | 类名：TextHeightAdaptivePolicy；  API声明：LAYOUT\_CONSTRAINT\_FIRST  差异内容：LAYOUT\_CONSTRAINT\_FIRST | component/enums.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum ArrowPointPosition  差异内容： declare enum ArrowPointPosition | component/enums.d.ts |
| 新增API | NA | 类名：ArrowPointPosition；  API声明：START = 'Start'  差异内容：START = 'Start' | component/enums.d.ts |
| 新增API | NA | 类名：ArrowPointPosition；  API声明：CENTER = 'Center'  差异内容：CENTER = 'Center' | component/enums.d.ts |
| 新增API | NA | 类名：ArrowPointPosition；  API声明：END = 'End'  差异内容：END = 'End' | component/enums.d.ts |
| 新增API | NA | 类名：CopyOptions；  API声明：CROSS\_DEVICE = 3  差异内容：CROSS\_DEVICE = 3 | component/enums.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum ModifierKey  差异内容： declare enum ModifierKey | component/enums.d.ts |
| 新增API | NA | 类名：ModifierKey；  API声明：CTRL  差异内容：CTRL | component/enums.d.ts |
| 新增API | NA | 类名：ModifierKey；  API声明：SHIFT  差异内容：SHIFT | component/enums.d.ts |
| 新增API | NA | 类名：ModifierKey；  API声明：ALT  差异内容：ALT | component/enums.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum FunctionKey  差异内容： declare enum FunctionKey | component/enums.d.ts |
| 新增API | NA | 类名：FunctionKey；  API声明：ESC  差异内容：ESC | component/enums.d.ts |
| 新增API | NA | 类名：FunctionKey；  API声明：F1  差异内容：F1 | component/enums.d.ts |
| 新增API | NA | 类名：FunctionKey；  API声明：F2  差异内容：F2 | component/enums.d.ts |
| 新增API | NA | 类名：FunctionKey；  API声明：F3  差异内容：F3 | component/enums.d.ts |
| 新增API | NA | 类名：FunctionKey；  API声明：F4  差异内容：F4 | component/enums.d.ts |
| 新增API | NA | 类名：FunctionKey；  API声明：F5  差异内容：F5 | component/enums.d.ts |
| 新增API | NA | 类名：FunctionKey；  API声明：F6  差异内容：F6 | component/enums.d.ts |
| 新增API | NA | 类名：FunctionKey；  API声明：F7  差异内容：F7 | component/enums.d.ts |
| 新增API | NA | 类名：FunctionKey；  API声明：F8  差异内容：F8 | component/enums.d.ts |
| 新增API | NA | 类名：FunctionKey；  API声明：F9  差异内容：F9 | component/enums.d.ts |
| 新增API | NA | 类名：FunctionKey；  API声明：F10  差异内容：F10 | component/enums.d.ts |
| 新增API | NA | 类名：FunctionKey；  API声明：F11  差异内容：F11 | component/enums.d.ts |
| 新增API | NA | 类名：FunctionKey；  API声明：F12  差异内容：F12 | component/enums.d.ts |
| 新增API | NA | 类名：FunctionKey；  API声明：TAB  差异内容：TAB | component/enums.d.ts |
| 新增API | NA | 类名：FunctionKey；  API声明：DPAD\_UP  差异内容：DPAD\_UP | component/enums.d.ts |
| 新增API | NA | 类名：FunctionKey；  API声明：DPAD\_DOWN  差异内容：DPAD\_DOWN | component/enums.d.ts |
| 新增API | NA | 类名：FunctionKey；  API声明：DPAD\_LEFT  差异内容：DPAD\_LEFT | component/enums.d.ts |
| 新增API | NA | 类名：FunctionKey；  API声明：DPAD\_RIGHT  差异内容：DPAD\_RIGHT | component/enums.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum ImageSpanAlignment  差异内容： declare enum ImageSpanAlignment | component/enums.d.ts |
| 新增API | NA | 类名：ImageSpanAlignment；  API声明：BASELINE  差异内容：BASELINE | component/enums.d.ts |
| 新增API | NA | 类名：ImageSpanAlignment；  API声明：BOTTOM  差异内容：BOTTOM | component/enums.d.ts |
| 新增API | NA | 类名：ImageSpanAlignment；  API声明：CENTER  差异内容：CENTER | component/enums.d.ts |
| 新增API | NA | 类名：ImageSpanAlignment；  API声明：TOP  差异内容：TOP | component/enums.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum ObscuredReasons  差异内容： declare enum ObscuredReasons | component/enums.d.ts |
| 新增API | NA | 类名：ObscuredReasons；  API声明：PLACEHOLDER = 0  差异内容：PLACEHOLDER = 0 | component/enums.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum TextContentStyle  差异内容： declare enum TextContentStyle | component/enums.d.ts |
| 新增API | NA | 类名：TextContentStyle；  API声明：DEFAULT  差异内容：DEFAULT | component/enums.d.ts |
| 新增API | NA | 类名：TextContentStyle；  API声明：INLINE  差异内容：INLINE | component/enums.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum ClickEffectLevel  差异内容： declare enum ClickEffectLevel | component/enums.d.ts |
| 新增API | NA | 类名：ClickEffectLevel；  API声明：LIGHT  差异内容：LIGHT | component/enums.d.ts |
| 新增API | NA | 类名：ClickEffectLevel；  API声明：MIDDLE  差异内容：MIDDLE | component/enums.d.ts |
| 新增API | NA | 类名：ClickEffectLevel；  API声明：HEAVY  差异内容：HEAVY | component/enums.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum XComponentType  差异内容： declare enum XComponentType | component/enums.d.ts |
| 新增API | NA | 类名：XComponentType；  API声明：SURFACE  差异内容：SURFACE | component/enums.d.ts |
| 新增API | NA | 类名：XComponentType；  API声明：COMPONENT  差异内容：COMPONENT | component/enums.d.ts |
| 新增API | NA | 类名：XComponentType；  API声明：TEXTURE  差异内容：TEXTURE | component/enums.d.ts |
| 新增API | NA | 类名：XComponentType；  API声明：NODE  差异内容：NODE | component/enums.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum NestedScrollMode  差异内容： declare enum NestedScrollMode | component/enums.d.ts |
| 新增API | NA | 类名：NestedScrollMode；  API声明：SELF\_ONLY  差异内容：SELF\_ONLY | component/enums.d.ts |
| 新增API | NA | 类名：NestedScrollMode；  API声明：SELF\_FIRST  差异内容：SELF\_FIRST | component/enums.d.ts |
| 新增API | NA | 类名：NestedScrollMode；  API声明：PARENT\_FIRST  差异内容：PARENT\_FIRST | component/enums.d.ts |
| 新增API | NA | 类名：NestedScrollMode；  API声明：PARALLEL  差异内容：PARALLEL | component/enums.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum ScrollSource  差异内容： declare enum ScrollSource | component/enums.d.ts |
| 新增API | NA | 类名：ScrollSource；  API声明：DRAG = 0  差异内容：DRAG = 0 | component/enums.d.ts |
| 新增API | NA | 类名：ScrollSource；  API声明：FLING  差异内容：FLING | component/enums.d.ts |
| 新增API | NA | 类名：ScrollSource；  API声明：EDGE\_EFFECT  差异内容：EDGE\_EFFECT | component/enums.d.ts |
| 新增API | NA | 类名：ScrollSource；  API声明：OTHER\_USER\_INPUT  差异内容：OTHER\_USER\_INPUT | component/enums.d.ts |
| 新增API | NA | 类名：ScrollSource；  API声明：SCROLL\_BAR  差异内容：SCROLL\_BAR | component/enums.d.ts |
| 新增API | NA | 类名：ScrollSource；  API声明：SCROLL\_BAR\_FLING  差异内容：SCROLL\_BAR\_FLING | component/enums.d.ts |
| 新增API | NA | 类名：ScrollSource；  API声明：SCROLLER  差异内容：SCROLLER | component/enums.d.ts |
| 新增API | NA | 类名：ScrollSource；  API声明：SCROLLER\_ANIMATION  差异内容：SCROLLER\_ANIMATION | component/enums.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum RenderFit  差异内容： declare enum RenderFit | component/enums.d.ts |
| 新增API | NA | 类名：RenderFit；  API声明：CENTER = 0  差异内容：CENTER = 0 | component/enums.d.ts |
| 新增API | NA | 类名：RenderFit；  API声明：TOP = 1  差异内容：TOP = 1 | component/enums.d.ts |
| 新增API | NA | 类名：RenderFit；  API声明：BOTTOM = 2  差异内容：BOTTOM = 2 | component/enums.d.ts |
| 新增API | NA | 类名：RenderFit；  API声明：LEFT = 3  差异内容：LEFT = 3 | component/enums.d.ts |
| 新增API | NA | 类名：RenderFit；  API声明：RIGHT = 4  差异内容：RIGHT = 4 | component/enums.d.ts |
| 新增API | NA | 类名：RenderFit；  API声明：TOP\_LEFT = 5  差异内容：TOP\_LEFT = 5 | component/enums.d.ts |
| 新增API | NA | 类名：RenderFit；  API声明：TOP\_RIGHT = 6  差异内容：TOP\_RIGHT = 6 | component/enums.d.ts |
| 新增API | NA | 类名：RenderFit；  API声明：BOTTOM\_LEFT = 7  差异内容：BOTTOM\_LEFT = 7 | component/enums.d.ts |
| 新增API | NA | 类名：RenderFit；  API声明：BOTTOM\_RIGHT = 8  差异内容：BOTTOM\_RIGHT = 8 | component/enums.d.ts |
| 新增API | NA | 类名：RenderFit；  API声明：RESIZE\_FILL = 9  差异内容：RESIZE\_FILL = 9 | component/enums.d.ts |
| 新增API | NA | 类名：RenderFit；  API声明：RESIZE\_CONTAIN = 10  差异内容：RESIZE\_CONTAIN = 10 | component/enums.d.ts |
| 新增API | NA | 类名：RenderFit；  API声明：RESIZE\_CONTAIN\_TOP\_LEFT = 11  差异内容：RESIZE\_CONTAIN\_TOP\_LEFT = 11 | component/enums.d.ts |
| 新增API | NA | 类名：RenderFit；  API声明：RESIZE\_CONTAIN\_BOTTOM\_RIGHT = 12  差异内容：RESIZE\_CONTAIN\_BOTTOM\_RIGHT = 12 | component/enums.d.ts |
| 新增API | NA | 类名：RenderFit；  API声明：RESIZE\_COVER = 13  差异内容：RESIZE\_COVER = 13 | component/enums.d.ts |
| 新增API | NA | 类名：RenderFit；  API声明：RESIZE\_COVER\_TOP\_LEFT = 14  差异内容：RESIZE\_COVER\_TOP\_LEFT = 14 | component/enums.d.ts |
| 新增API | NA | 类名：RenderFit；  API声明：RESIZE\_COVER\_BOTTOM\_RIGHT = 15  差异内容：RESIZE\_COVER\_BOTTOM\_RIGHT = 15 | component/enums.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum DialogButtonStyle  差异内容： declare enum DialogButtonStyle | component/enums.d.ts |
| 新增API | NA | 类名：DialogButtonStyle；  API声明：DEFAULT = 0  差异内容：DEFAULT = 0 | component/enums.d.ts |
| 新增API | NA | 类名：DialogButtonStyle；  API声明：HIGHLIGHT = 1  差异内容：HIGHLIGHT = 1 | component/enums.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum WordBreak  差异内容： declare enum WordBreak | component/enums.d.ts |
| 新增API | NA | 类名：WordBreak；  API声明：NORMAL = 0  差异内容：NORMAL = 0 | component/enums.d.ts |
| 新增API | NA | 类名：WordBreak；  API声明：BREAK\_ALL = 1  差异内容：BREAK\_ALL = 1 | component/enums.d.ts |
| 新增API | NA | 类名：WordBreak；  API声明：BREAK\_WORD = 2  差异内容：BREAK\_WORD = 2 | component/enums.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum LineBreakStrategy  差异内容： declare enum LineBreakStrategy | component/enums.d.ts |
| 新增API | NA | 类名：LineBreakStrategy；  API声明：GREEDY = 0  差异内容：GREEDY = 0 | component/enums.d.ts |
| 新增API | NA | 类名：LineBreakStrategy；  API声明：HIGH\_QUALITY = 1  差异内容：HIGH\_QUALITY = 1 | component/enums.d.ts |
| 新增API | NA | 类名：LineBreakStrategy；  API声明：BALANCED = 2  差异内容：BALANCED = 2 | component/enums.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum EllipsisMode  差异内容： declare enum EllipsisMode | component/enums.d.ts |
| 新增API | NA | 类名：EllipsisMode；  API声明：START = 0  差异内容：START = 0 | component/enums.d.ts |
| 新增API | NA | 类名：EllipsisMode；  API声明：CENTER = 1  差异内容：CENTER = 1 | component/enums.d.ts |
| 新增API | NA | 类名：EllipsisMode；  API声明：END = 2  差异内容：END = 2 | component/enums.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type Nullable<T> = T | undefined;  差异内容：declare type Nullable<T> = T | undefined; | component/enums.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum OptionWidthMode  差异内容： declare enum OptionWidthMode | component/enums.d.ts |
| 新增API | NA | 类名：OptionWidthMode；  API声明：FIT\_CONTENT = 'fit\_content'  差异内容：FIT\_CONTENT = 'fit\_content' | component/enums.d.ts |
| 新增API | NA | 类名：OptionWidthMode；  API声明：FIT\_TRIGGER = 'fit\_trigger'  差异内容：FIT\_TRIGGER = 'fit\_trigger' | component/enums.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum FoldStatus  差异内容： declare enum FoldStatus | component/enums.d.ts |
| 新增API | NA | 类名：FoldStatus；  API声明：FOLD\_STATUS\_UNKNOWN = 0  差异内容：FOLD\_STATUS\_UNKNOWN = 0 | component/enums.d.ts |
| 新增API | NA | 类名：FoldStatus；  API声明：FOLD\_STATUS\_EXPANDED = 1  差异内容：FOLD\_STATUS\_EXPANDED = 1 | component/enums.d.ts |
| 新增API | NA | 类名：FoldStatus；  API声明：FOLD\_STATUS\_FOLDED = 2  差异内容：FOLD\_STATUS\_FOLDED = 2 | component/enums.d.ts |
| 新增API | NA | 类名：FoldStatus；  API声明：FOLD\_STATUS\_HALF\_FOLDED = 3  差异内容：FOLD\_STATUS\_HALF\_FOLDED = 3 | component/enums.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum AppRotation  差异内容： declare enum AppRotation | component/enums.d.ts |
| 新增API | NA | 类名：AppRotation；  API声明：ROTATION\_0 = 0  差异内容：ROTATION\_0 = 0 | component/enums.d.ts |
| 新增API | NA | 类名：AppRotation；  API声明：ROTATION\_90 = 1  差异内容：ROTATION\_90 = 1 | component/enums.d.ts |
| 新增API | NA | 类名：AppRotation；  API声明：ROTATION\_180 = 2  差异内容：ROTATION\_180 = 2 | component/enums.d.ts |
| 新增API | NA | 类名：AppRotation；  API声明：ROTATION\_270 = 3  差异内容：ROTATION\_270 = 3 | component/enums.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum EmbeddedType  差异内容： declare enum EmbeddedType | component/enums.d.ts |
| 新增API | NA | 类名：EmbeddedType；  API声明：EMBEDDED\_UI\_EXTENSION = 0  差异内容：EMBEDDED\_UI\_EXTENSION = 0 | component/enums.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum MarqueeUpdateStrategy  差异内容： declare enum MarqueeUpdateStrategy | component/enums.d.ts |
| 新增API | NA | 类名：MarqueeUpdateStrategy；  API声明：DEFAULT = 0  差异内容：DEFAULT = 0 | component/enums.d.ts |
| 新增API | NA | 类名：MarqueeUpdateStrategy；  API声明：PRESERVE\_POSITION = 1  差异内容：PRESERVE\_POSITION = 1 | component/enums.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum TextDecorationStyle  差异内容： declare enum TextDecorationStyle | component/enums.d.ts |
| 新增API | NA | 类名：TextDecorationStyle；  API声明：SOLID = 0  差异内容：SOLID = 0 | component/enums.d.ts |
| 新增API | NA | 类名：TextDecorationStyle；  API声明：DOUBLE = 1  差异内容：DOUBLE = 1 | component/enums.d.ts |
| 新增API | NA | 类名：TextDecorationStyle；  API声明：DOTTED = 2  差异内容：DOTTED = 2 | component/enums.d.ts |
| 新增API | NA | 类名：TextDecorationStyle；  API声明：DASHED = 3  差异内容：DASHED = 3 | component/enums.d.ts |
| 新增API | NA | 类名：TextDecorationStyle；  API声明：WAVY = 4  差异内容：WAVY = 4 | component/enums.d.ts |
| 新增API | NA | 类名：FlexOptions；  API声明：space?: FlexSpaceOptions;  差异内容：space?: FlexSpaceOptions; | component/flex.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface FlexSpaceOptions  差异内容： declare interface FlexSpaceOptions | component/flex.d.ts |
| 新增API | NA | 类名：FlexSpaceOptions；  API声明：main?: LengthMetrics;  差异内容：main?: LengthMetrics; | component/flex.d.ts |
| 新增API | NA | 类名：FlexSpaceOptions；  API声明：cross?: LengthMetrics;  差异内容：cross?: LengthMetrics; | component/flex.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface GaugeShadowOptions  差异内容： declare interface GaugeShadowOptions | component/gauge.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface GaugeIndicatorOptions  差异内容： declare interface GaugeIndicatorOptions | component/gauge.d.ts |
| 新增API | NA | 类名：GaugeIndicatorOptions；  API声明：icon?: ResourceStr;  差异内容：icon?: ResourceStr; | component/gauge.d.ts |
| 新增API | NA | 类名：GaugeIndicatorOptions；  API声明：space?: Dimension;  差异内容：space?: Dimension; | component/gauge.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface GaugeConfiguration  差异内容： declare interface GaugeConfiguration | component/gauge.d.ts |
| 新增API | NA | 类名：GaugeConfiguration；  API声明：value: number;  差异内容：value: number; | component/gauge.d.ts |
| 新增API | NA | 类名：GaugeConfiguration；  API声明：min: number;  差异内容：min: number; | component/gauge.d.ts |
| 新增API | NA | 类名：GaugeConfiguration；  API声明：max: number;  差异内容：max: number; | component/gauge.d.ts |
| 新增API | NA | 类名：GaugeAttribute；  API声明：description(value: CustomBuilder): GaugeAttribute;  差异内容：description(value: CustomBuilder): GaugeAttribute; | component/gauge.d.ts |
| 新增API | NA | 类名：GaugeAttribute；  API声明：trackShadow(value: GaugeShadowOptions): GaugeAttribute;  差异内容：trackShadow(value: GaugeShadowOptions): GaugeAttribute; | component/gauge.d.ts |
| 新增API | NA | 类名：GaugeAttribute；  API声明：indicator(value: GaugeIndicatorOptions): GaugeAttribute;  差异内容：indicator(value: GaugeIndicatorOptions): GaugeAttribute; | component/gauge.d.ts |
| 新增API | NA | 类名：GaugeAttribute；  API声明：contentModifier(modifier: ContentModifier<GaugeConfiguration>): GaugeAttribute;  差异内容：contentModifier(modifier: ContentModifier<GaugeConfiguration>): GaugeAttribute; | component/gauge.d.ts |
| 新增API | NA | 类名：GaugeAttribute；  API声明：privacySensitive(isPrivacySensitiveMode: Optional<boolean>): GaugeAttribute;  差异内容：privacySensitive(isPrivacySensitiveMode: Optional<boolean>): GaugeAttribute; | component/gauge.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum GestureJudgeResult  差异内容： declare enum GestureJudgeResult | component/gesture.d.ts |
| 新增API | NA | 类名：GestureJudgeResult；  API声明：CONTINUE = 0  差异内容：CONTINUE = 0 | component/gesture.d.ts |
| 新增API | NA | 类名：GestureJudgeResult；  API声明：REJECT = 1  差异内容：REJECT = 1 | component/gesture.d.ts |
| 新增API | NA | 类名：global；  API声明： declare namespace GestureControl  差异内容： declare namespace GestureControl | component/gesture.d.ts |
| 新增API | NA | 类名：GestureControl；  API声明： enum GestureType  差异内容： enum GestureType | component/gesture.d.ts |
| 新增API | NA | 类名：GestureType；  API声明：TAP\_GESTURE = 0  差异内容：TAP\_GESTURE = 0 | component/gesture.d.ts |
| 新增API | NA | 类名：GestureType；  API声明：LONG\_PRESS\_GESTURE = 1  差异内容：LONG\_PRESS\_GESTURE = 1 | component/gesture.d.ts |
| 新增API | NA | 类名：GestureType；  API声明：PAN\_GESTURE = 2  差异内容：PAN\_GESTURE = 2 | component/gesture.d.ts |
| 新增API | NA | 类名：GestureType；  API声明：PINCH\_GESTURE = 3  差异内容：PINCH\_GESTURE = 3 | component/gesture.d.ts |
| 新增API | NA | 类名：GestureType；  API声明：SWIPE\_GESTURE = 4  差异内容：SWIPE\_GESTURE = 4 | component/gesture.d.ts |
| 新增API | NA | 类名：GestureType；  API声明：ROTATION\_GESTURE = 5  差异内容：ROTATION\_GESTURE = 5 | component/gesture.d.ts |
| 新增API | NA | 类名：GestureType；  API声明：DRAG = 6  差异内容：DRAG = 6 | component/gesture.d.ts |
| 新增API | NA | 类名：GestureType；  API声明：CLICK = 7  差异内容：CLICK = 7 | component/gesture.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface GestureInfo  差异内容： declare interface GestureInfo | component/gesture.d.ts |
| 新增API | NA | 类名：GestureInfo；  API声明：tag?: string;  差异内容：tag?: string; | component/gesture.d.ts |
| 新增API | NA | 类名：GestureInfo；  API声明：type: GestureControl.GestureType;  差异内容：type: GestureControl.GestureType; | component/gesture.d.ts |
| 新增API | NA | 类名：GestureInfo；  API声明：isSystemGesture: boolean;  差异内容：isSystemGesture: boolean; | component/gesture.d.ts |
| 新增API | NA | 类名：FingerInfo；  API声明：displayX: number;  差异内容：displayX: number; | component/gesture.d.ts |
| 新增API | NA | 类名：FingerInfo；  API声明：displayY: number;  差异内容：displayY: number; | component/gesture.d.ts |
| 新增API | NA | 类名：global；  API声明： interface BaseGestureEvent  差异内容： interface BaseGestureEvent | component/gesture.d.ts |
| 新增API | NA | 类名：BaseGestureEvent；  API声明：fingerList: FingerInfo[];  差异内容：fingerList: FingerInfo[]; | component/gesture.d.ts |
| 新增API | NA | 类名：global；  API声明： interface TapGestureEvent  差异内容： interface TapGestureEvent | component/gesture.d.ts |
| 新增API | NA | 类名：global；  API声明： interface LongPressGestureEvent  差异内容： interface LongPressGestureEvent | component/gesture.d.ts |
| 新增API | NA | 类名：LongPressGestureEvent；  API声明：repeat: boolean;  差异内容：repeat: boolean; | component/gesture.d.ts |
| 新增API | NA | 类名：global；  API声明： interface PanGestureEvent  差异内容： interface PanGestureEvent | component/gesture.d.ts |
| 新增API | NA | 类名：PanGestureEvent；  API声明：offsetX: number;  差异内容：offsetX: number; | component/gesture.d.ts |
| 新增API | NA | 类名：PanGestureEvent；  API声明：offsetY: number;  差异内容：offsetY: number; | component/gesture.d.ts |
| 新增API | NA | 类名：PanGestureEvent；  API声明：velocityX: number;  差异内容：velocityX: number; | component/gesture.d.ts |
| 新增API | NA | 类名：PanGestureEvent；  API声明：velocityY: number;  差异内容：velocityY: number; | component/gesture.d.ts |
| 新增API | NA | 类名：PanGestureEvent；  API声明：velocity: number;  差异内容：velocity: number; | component/gesture.d.ts |
| 新增API | NA | 类名：global；  API声明： interface PinchGestureEvent  差异内容： interface PinchGestureEvent | component/gesture.d.ts |
| 新增API | NA | 类名：PinchGestureEvent；  API声明：scale: number;  差异内容：scale: number; | component/gesture.d.ts |
| 新增API | NA | 类名：PinchGestureEvent；  API声明：pinchCenterX: number;  差异内容：pinchCenterX: number; | component/gesture.d.ts |
| 新增API | NA | 类名：PinchGestureEvent；  API声明：pinchCenterY: number;  差异内容：pinchCenterY: number; | component/gesture.d.ts |
| 新增API | NA | 类名：global；  API声明： interface RotationGestureEvent  差异内容： interface RotationGestureEvent | component/gesture.d.ts |
| 新增API | NA | 类名：RotationGestureEvent；  API声明：angle: number;  差异内容：angle: number; | component/gesture.d.ts |
| 新增API | NA | 类名：global；  API声明： interface SwipeGestureEvent  差异内容： interface SwipeGestureEvent | component/gesture.d.ts |
| 新增API | NA | 类名：SwipeGestureEvent；  API声明：angle: number;  差异内容：angle: number; | component/gesture.d.ts |
| 新增API | NA | 类名：SwipeGestureEvent；  API声明：speed: number;  差异内容：speed: number; | component/gesture.d.ts |
| 新增API | NA | 类名：GestureEvent；  API声明：velocityX: number;  差异内容：velocityX: number; | component/gesture.d.ts |
| 新增API | NA | 类名：GestureEvent；  API声明：velocityY: number;  差异内容：velocityY: number; | component/gesture.d.ts |
| 新增API | NA | 类名：GestureEvent；  API声明：velocity: number;  差异内容：velocity: number; | component/gesture.d.ts |
| 新增API | NA | 类名：global；  API声明： interface GestureInterface  差异内容： interface GestureInterface | component/gesture.d.ts |
| 新增API | NA | 类名：GestureInterface；  API声明：tag(tag: string): T;  差异内容：tag(tag: string): T; | component/gesture.d.ts |
| 新增API | NA | 类名：PanGestureOptions；  API声明：getDirection(): PanDirection;  差异内容：getDirection(): PanDirection; | component/gesture.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class GestureHandler  差异内容： declare class GestureHandler | component/gesture.d.ts |
| 新增API | NA | 类名：GestureHandler；  API声明：tag(tag: string): T;  差异内容：tag(tag: string): T; | component/gesture.d.ts |
| 新增API | NA | 类名：global；  API声明： interface TapGestureHandlerOptions  差异内容： interface TapGestureHandlerOptions | component/gesture.d.ts |
| 新增API | NA | 类名：TapGestureHandlerOptions；  API声明：count?: number;  差异内容：count?: number; | component/gesture.d.ts |
| 新增API | NA | 类名：TapGestureHandlerOptions；  API声明：fingers?: number;  差异内容：fingers?: number; | component/gesture.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class TapGestureHandler  差异内容： declare class TapGestureHandler | component/gesture.d.ts |
| 新增API | NA | 类名：TapGestureHandler；  API声明：onAction(event: Callback<GestureEvent>): TapGestureHandler;  差异内容：onAction(event: Callback<GestureEvent>): TapGestureHandler; | component/gesture.d.ts |
| 新增API | NA | 类名：global；  API声明： interface LongPressGestureHandlerOptions  差异内容： interface LongPressGestureHandlerOptions | component/gesture.d.ts |
| 新增API | NA | 类名：LongPressGestureHandlerOptions；  API声明：fingers?: number;  差异内容：fingers?: number; | component/gesture.d.ts |
| 新增API | NA | 类名：LongPressGestureHandlerOptions；  API声明：repeat?: boolean;  差异内容：repeat?: boolean; | component/gesture.d.ts |
| 新增API | NA | 类名：LongPressGestureHandlerOptions；  API声明：duration?: number;  差异内容：duration?: number; | component/gesture.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class LongPressGestureHandler  差异内容： declare class LongPressGestureHandler | component/gesture.d.ts |
| 新增API | NA | 类名：LongPressGestureHandler；  API声明：onAction(event: Callback<GestureEvent>): LongPressGestureHandler;  差异内容：onAction(event: Callback<GestureEvent>): LongPressGestureHandler; | component/gesture.d.ts |
| 新增API | NA | 类名：LongPressGestureHandler；  API声明：onActionEnd(event: Callback<GestureEvent>): LongPressGestureHandler;  差异内容：onActionEnd(event: Callback<GestureEvent>): LongPressGestureHandler; | component/gesture.d.ts |
| 新增API | NA | 类名：LongPressGestureHandler；  API声明：onActionCancel(event: Callback<void>): LongPressGestureHandler;  差异内容：onActionCancel(event: Callback<void>): LongPressGestureHandler; | component/gesture.d.ts |
| 新增API | NA | 类名：global；  API声明： interface PanGestureHandlerOptions  差异内容： interface PanGestureHandlerOptions | component/gesture.d.ts |
| 新增API | NA | 类名：PanGestureHandlerOptions；  API声明：fingers?: number;  差异内容：fingers?: number; | component/gesture.d.ts |
| 新增API | NA | 类名：PanGestureHandlerOptions；  API声明：direction?: PanDirection;  差异内容：direction?: PanDirection; | component/gesture.d.ts |
| 新增API | NA | 类名：PanGestureHandlerOptions；  API声明：distance?: number;  差异内容：distance?: number; | component/gesture.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class PanGestureHandler  差异内容： declare class PanGestureHandler | component/gesture.d.ts |
| 新增API | NA | 类名：PanGestureHandler；  API声明：onActionStart(event: Callback<GestureEvent>): PanGestureHandler;  差异内容：onActionStart(event: Callback<GestureEvent>): PanGestureHandler; | component/gesture.d.ts |
| 新增API | NA | 类名：PanGestureHandler；  API声明：onActionUpdate(event: Callback<GestureEvent>): PanGestureHandler;  差异内容：onActionUpdate(event: Callback<GestureEvent>): PanGestureHandler; | component/gesture.d.ts |
| 新增API | NA | 类名：PanGestureHandler；  API声明：onActionEnd(event: Callback<GestureEvent>): PanGestureHandler;  差异内容：onActionEnd(event: Callback<GestureEvent>): PanGestureHandler; | component/gesture.d.ts |
| 新增API | NA | 类名：PanGestureHandler；  API声明：onActionCancel(event: Callback<void>): PanGestureHandler;  差异内容：onActionCancel(event: Callback<void>): PanGestureHandler; | component/gesture.d.ts |
| 新增API | NA | 类名：global；  API声明： interface SwipeGestureHandlerOptions  差异内容： interface SwipeGestureHandlerOptions | component/gesture.d.ts |
| 新增API | NA | 类名：SwipeGestureHandlerOptions；  API声明：fingers?: number;  差异内容：fingers?: number; | component/gesture.d.ts |
| 新增API | NA | 类名：SwipeGestureHandlerOptions；  API声明：direction?: SwipeDirection;  差异内容：direction?: SwipeDirection; | component/gesture.d.ts |
| 新增API | NA | 类名：SwipeGestureHandlerOptions；  API声明：speed?: number;  差异内容：speed?: number; | component/gesture.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class SwipeGestureHandler  差异内容： declare class SwipeGestureHandler | component/gesture.d.ts |
| 新增API | NA | 类名：SwipeGestureHandler；  API声明：onAction(event: Callback<GestureEvent>): SwipeGestureHandler;  差异内容：onAction(event: Callback<GestureEvent>): SwipeGestureHandler; | component/gesture.d.ts |
| 新增API | NA | 类名：global；  API声明： interface PinchGestureHandlerOptions  差异内容： interface PinchGestureHandlerOptions | component/gesture.d.ts |
| 新增API | NA | 类名：PinchGestureHandlerOptions；  API声明：fingers?: number;  差异内容：fingers?: number; | component/gesture.d.ts |
| 新增API | NA | 类名：PinchGestureHandlerOptions；  API声明：distance?: number;  差异内容：distance?: number; | component/gesture.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class PinchGestureHandler  差异内容： declare class PinchGestureHandler | component/gesture.d.ts |
| 新增API | NA | 类名：PinchGestureHandler；  API声明：onActionStart(event: Callback<GestureEvent>): PinchGestureHandler;  差异内容：onActionStart(event: Callback<GestureEvent>): PinchGestureHandler; | component/gesture.d.ts |
| 新增API | NA | 类名：PinchGestureHandler；  API声明：onActionUpdate(event: Callback<GestureEvent>): PinchGestureHandler;  差异内容：onActionUpdate(event: Callback<GestureEvent>): PinchGestureHandler; | component/gesture.d.ts |
| 新增API | NA | 类名：PinchGestureHandler；  API声明：onActionEnd(event: Callback<GestureEvent>): PinchGestureHandler;  差异内容：onActionEnd(event: Callback<GestureEvent>): PinchGestureHandler; | component/gesture.d.ts |
| 新增API | NA | 类名：PinchGestureHandler；  API声明：onActionCancel(event: Callback<void>): PinchGestureHandler;  差异内容：onActionCancel(event: Callback<void>): PinchGestureHandler; | component/gesture.d.ts |
| 新增API | NA | 类名：global；  API声明： interface RotationGestureHandlerOptions  差异内容： interface RotationGestureHandlerOptions | component/gesture.d.ts |
| 新增API | NA | 类名：RotationGestureHandlerOptions；  API声明：fingers?: number;  差异内容：fingers?: number; | component/gesture.d.ts |
| 新增API | NA | 类名：RotationGestureHandlerOptions；  API声明：angle?: number;  差异内容：angle?: number; | component/gesture.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class RotationGestureHandler  差异内容： declare class RotationGestureHandler | component/gesture.d.ts |
| 新增API | NA | 类名：RotationGestureHandler；  API声明：onActionStart(event: Callback<GestureEvent>): RotationGestureHandler;  差异内容：onActionStart(event: Callback<GestureEvent>): RotationGestureHandler; | component/gesture.d.ts |
| 新增API | NA | 类名：RotationGestureHandler；  API声明：onActionUpdate(event: Callback<GestureEvent>): RotationGestureHandler;  差异内容：onActionUpdate(event: Callback<GestureEvent>): RotationGestureHandler; | component/gesture.d.ts |
| 新增API | NA | 类名：RotationGestureHandler；  API声明：onActionEnd(event: Callback<GestureEvent>): RotationGestureHandler;  差异内容：onActionEnd(event: Callback<GestureEvent>): RotationGestureHandler; | component/gesture.d.ts |
| 新增API | NA | 类名：RotationGestureHandler；  API声明：onActionCancel(event: Callback<void>): RotationGestureHandler;  差异内容：onActionCancel(event: Callback<void>): RotationGestureHandler; | component/gesture.d.ts |
| 新增API | NA | 类名：global；  API声明： interface GestureGroupGestureHandlerOptions  差异内容： interface GestureGroupGestureHandlerOptions | component/gesture.d.ts |
| 新增API | NA | 类名：GestureGroupGestureHandlerOptions；  API声明：mode: GestureMode;  差异内容：mode: GestureMode; | component/gesture.d.ts |
| 新增API | NA | 类名：GestureGroupGestureHandlerOptions；  API声明：gestures: GestureHandler<TapGestureHandler | LongPressGestureHandler | PanGestureHandler | SwipeGestureHandler | PinchGestureHandler | RotationGestureHandler | GestureGroupHandler>[];  差异内容：gestures: GestureHandler<TapGestureHandler | LongPressGestureHandler | PanGestureHandler | SwipeGestureHandler | PinchGestureHandler | RotationGestureHandler | GestureGroupHandler>[]; | component/gesture.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class GestureGroupHandler  差异内容： declare class GestureGroupHandler | component/gesture.d.ts |
| 新增API | NA | 类名：GestureGroupHandler；  API声明：onCancel(event: Callback<void>): GestureGroupHandler;  差异内容：onCancel(event: Callback<void>): GestureGroupHandler; | component/gesture.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum GesturePriority  差异内容： declare enum GesturePriority | component/gesture.d.ts |
| 新增API | NA | 类名：GesturePriority；  API声明：NORMAL = 0  差异内容：NORMAL = 0 | component/gesture.d.ts |
| 新增API | NA | 类名：GesturePriority；  API声明：PRIORITY = 1  差异内容：PRIORITY = 1 | component/gesture.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum GestureRecognizerState  差异内容： declare enum GestureRecognizerState | component/gesture.d.ts |
| 新增API | NA | 类名：GestureRecognizerState；  API声明：READY = 0  差异内容：READY = 0 | component/gesture.d.ts |
| 新增API | NA | 类名：GestureRecognizerState；  API声明：DETECTING = 1  差异内容：DETECTING = 1 | component/gesture.d.ts |
| 新增API | NA | 类名：GestureRecognizerState；  API声明：PENDING = 2  差异内容：PENDING = 2 | component/gesture.d.ts |
| 新增API | NA | 类名：GestureRecognizerState；  API声明：BLOCKED = 3  差异内容：BLOCKED = 3 | component/gesture.d.ts |
| 新增API | NA | 类名：GestureRecognizerState；  API声明：SUCCESSFUL = 4  差异内容：SUCCESSFUL = 4 | component/gesture.d.ts |
| 新增API | NA | 类名：GestureRecognizerState；  API声明：FAILED = 5  差异内容：FAILED = 5 | component/gesture.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class ScrollableTargetInfo  差异内容： declare class ScrollableTargetInfo | component/gesture.d.ts |
| 新增API | NA | 类名：ScrollableTargetInfo；  API声明：isBegin(): boolean;  差异内容：isBegin(): boolean; | component/gesture.d.ts |
| 新增API | NA | 类名：ScrollableTargetInfo；  API声明：isEnd(): boolean;  差异内容：isEnd(): boolean; | component/gesture.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class EventTargetInfo  差异内容： declare class EventTargetInfo | component/gesture.d.ts |
| 新增API | NA | 类名：EventTargetInfo；  API声明：getId(): string;  差异内容：getId(): string; | component/gesture.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class GestureRecognizer  差异内容： declare class GestureRecognizer | component/gesture.d.ts |
| 新增API | NA | 类名：GestureRecognizer；  API声明：getTag(): string;  差异内容：getTag(): string; | component/gesture.d.ts |
| 新增API | NA | 类名：GestureRecognizer；  API声明：getType(): GestureControl.GestureType;  差异内容：getType(): GestureControl.GestureType; | component/gesture.d.ts |
| 新增API | NA | 类名：GestureRecognizer；  API声明：isBuiltIn(): boolean;  差异内容：isBuiltIn(): boolean; | component/gesture.d.ts |
| 新增API | NA | 类名：GestureRecognizer；  API声明：setEnabled(isEnabled: boolean): void;  差异内容：setEnabled(isEnabled: boolean): void; | component/gesture.d.ts |
| 新增API | NA | 类名：GestureRecognizer；  API声明：isEnabled(): boolean;  差异内容：isEnabled(): boolean; | component/gesture.d.ts |
| 新增API | NA | 类名：GestureRecognizer；  API声明：getState(): GestureRecognizerState;  差异内容：getState(): GestureRecognizerState; | component/gesture.d.ts |
| 新增API | NA | 类名：GestureRecognizer；  API声明：getEventTargetInfo(): EventTargetInfo;  差异内容：getEventTargetInfo(): EventTargetInfo; | component/gesture.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class PanRecognizer  差异内容： declare class PanRecognizer | component/gesture.d.ts |
| 新增API | NA | 类名：PanRecognizer；  API声明：getPanGestureOptions(): PanGestureOptions;  差异内容：getPanGestureOptions(): PanGestureOptions; | component/gesture.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface GridLayoutOptions  差异内容： declare interface GridLayoutOptions | component/grid.d.ts |
| 新增API | NA | 类名：GridLayoutOptions；  API声明：regularSize: [  number,  number  ];  差异内容：regularSize: [  number,  number  ]; | component/grid.d.ts |
| 新增API | NA | 类名：GridLayoutOptions；  API声明：irregularIndexes?: number[];  差异内容：irregularIndexes?: number[]; | component/grid.d.ts |
| 新增API | NA | 类名：GridLayoutOptions；  API声明：onGetIrregularSizeByIndex?: (index: number) => [  number,  number  ];  差异内容：onGetIrregularSizeByIndex?: (index: number) => [  number,  number  ]; | component/grid.d.ts |
| 新增API | NA | 类名：GridLayoutOptions；  API声明：onGetRectByIndex?: (index: number) => [  number,  number,  number,  number  ];  差异内容：onGetRectByIndex?: (index: number) => [  number,  number,  number,  number  ]; | component/grid.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface ComputedBarAttribute  差异内容： declare interface ComputedBarAttribute | component/grid.d.ts |
| 新增API | NA | 类名：ComputedBarAttribute；  API声明：totalOffset: number;  差异内容：totalOffset: number; | component/grid.d.ts |
| 新增API | NA | 类名：ComputedBarAttribute；  API声明：totalLength: number;  差异内容：totalLength: number; | component/grid.d.ts |
| 新增API | NA | 类名：GridAttribute；  API声明：onScrollBarUpdate(event: (index: number, offset: number) => ComputedBarAttribute): GridAttribute;  差异内容：onScrollBarUpdate(event: (index: number, offset: number) => ComputedBarAttribute): GridAttribute; | component/grid.d.ts |
| 新增API | NA | 类名：GridAttribute；  API声明：edgeEffect(value: EdgeEffect, options?: EdgeEffectOptions): GridAttribute;  差异内容：edgeEffect(value: EdgeEffect, options?: EdgeEffectOptions): GridAttribute; | component/grid.d.ts |
| 新增API | NA | 类名：GridAttribute；  API声明：nestedScroll(value: NestedScrollOptions): GridAttribute;  差异内容：nestedScroll(value: NestedScrollOptions): GridAttribute; | component/grid.d.ts |
| 新增API | NA | 类名：GridAttribute；  API声明：enableScrollInteraction(value: boolean): GridAttribute;  差异内容：enableScrollInteraction(value: boolean): GridAttribute; | component/grid.d.ts |
| 新增API | NA | 类名：GridAttribute；  API声明：friction(value: number | Resource): GridAttribute;  差异内容：friction(value: number | Resource): GridAttribute; | component/grid.d.ts |
| 新增API | NA | 类名：GridAttribute；  API声明：onScroll(event: (scrollOffset: number, scrollState: ScrollState) => void): GridAttribute;  差异内容：onScroll(event: (scrollOffset: number, scrollState: ScrollState) => void): GridAttribute; | component/grid.d.ts |
| 新增API | NA | 类名：GridAttribute；  API声明：onReachStart(event: () => void): GridAttribute;  差异内容：onReachStart(event: () => void): GridAttribute; | component/grid.d.ts |
| 新增API | NA | 类名：GridAttribute；  API声明：onReachEnd(event: () => void): GridAttribute;  差异内容：onReachEnd(event: () => void): GridAttribute; | component/grid.d.ts |
| 新增API | NA | 类名：GridAttribute；  API声明：onScrollStart(event: () => void): GridAttribute;  差异内容：onScrollStart(event: () => void): GridAttribute; | component/grid.d.ts |
| 新增API | NA | 类名：GridAttribute；  API声明：onScrollStop(event: () => void): GridAttribute;  差异内容：onScrollStop(event: () => void): GridAttribute; | component/grid.d.ts |
| 新增API | NA | 类名：GridAttribute；  API声明：onScrollFrameBegin(event: (offset: number, state: ScrollState) => {  offsetRemain: number;  }): GridAttribute;  差异内容：onScrollFrameBegin(event: (offset: number, state: ScrollState) => {  offsetRemain: number;  }): GridAttribute; | component/grid.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum GridItemStyle  差异内容： declare enum GridItemStyle | component/gridItem.d.ts |
| 新增API | NA | 类名：GridItemStyle；  API声明：NONE = 0  差异内容：NONE = 0 | component/gridItem.d.ts |
| 新增API | NA | 类名：GridItemStyle；  API声明：PLAIN = 1  差异内容：PLAIN = 1 | component/gridItem.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface GridItemOptions  差异内容： declare interface GridItemOptions | component/gridItem.d.ts |
| 新增API | NA | 类名：GridItemOptions；  API声明：style?: GridItemStyle;  差异内容：style?: GridItemStyle; | component/gridItem.d.ts |
| 新增API | NA | 类名：GridItemAttribute；  API声明：selected(value: boolean): GridItemAttribute;  差异内容：selected(value: boolean): GridItemAttribute; | component/gridItem.d.ts |
| 新增API | NA | 类名：GridRowAttribute；  API声明：alignItems(value: ItemAlign): GridRowAttribute;  差异内容：alignItems(value: ItemAlign): GridRowAttribute; | component/grid\_row.d.ts |
| 新增API | NA | 类名：ImageAttribute；  API声明：onError(callback: ImageErrorCallback): ImageAttribute;  差异内容：onError(callback: ImageErrorCallback): ImageAttribute; | component/image.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type DrawableDescriptor = import('../api/@ohos.arkui.drawableDescriptor').DrawableDescriptor;  差异内容：declare type DrawableDescriptor = import('../api/@ohos.arkui.drawableDescriptor').DrawableDescriptor; | component/image.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type DrawingColorFilter = import('../api/@ohos.graphics.drawing').default.ColorFilter;  差异内容：declare type DrawingColorFilter = import('../api/@ohos.graphics.drawing').default.ColorFilter; | component/image.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum DynamicRangeMode  差异内容： declare enum DynamicRangeMode | component/image.d.ts |
| 新增API | NA | 类名：DynamicRangeMode；  API声明：HIGH = 0  差异内容：HIGH = 0 | component/image.d.ts |
| 新增API | NA | 类名：DynamicRangeMode；  API声明：CONSTRAINT = 1  差异内容：CONSTRAINT = 1 | component/image.d.ts |
| 新增API | NA | 类名：DynamicRangeMode；  API声明：STANDARD = 2  差异内容：STANDARD = 2 | component/image.d.ts |
| 新增API | NA | 类名：ImageAttribute；  API声明：dynamicRangeMode(value: DynamicRangeMode): ImageAttribute;  差异内容：dynamicRangeMode(value: DynamicRangeMode): ImageAttribute; | component/image.d.ts |
| 新增API | NA | 类名：ImageAttribute；  API声明：enableAnalyzer(enable: boolean): ImageAttribute;  差异内容：enableAnalyzer(enable: boolean): ImageAttribute; | component/image.d.ts |
| 新增API | NA | 类名：ImageAttribute；  API声明：resizable(value: ResizableOptions): ImageAttribute;  差异内容：resizable(value: ResizableOptions): ImageAttribute; | component/image.d.ts |
| 新增API | NA | 类名：ImageAttribute；  API声明：privacySensitive(supported: boolean): ImageAttribute;  差异内容：privacySensitive(supported: boolean): ImageAttribute; | component/image.d.ts |
| 新增API | NA | 类名：global；  API声明：type ImageErrorCallback = (error: ImageError) => void;  差异内容：type ImageErrorCallback = (error: ImageError) => void; | component/image.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface ImageError  差异内容： declare interface ImageError | component/image.d.ts |
| 新增API | NA | 类名：ImageError；  API声明：componentWidth: number;  差异内容：componentWidth: number; | component/image.d.ts |
| 新增API | NA | 类名：ImageError；  API声明：componentHeight: number;  差异内容：componentHeight: number; | component/image.d.ts |
| 新增API | NA | 类名：ImageError；  API声明：message: string;  差异内容：message: string; | component/image.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface ResizableOptions  差异内容： declare interface ResizableOptions | component/image.d.ts |
| 新增API | NA | 类名：ResizableOptions；  API声明：slice?: EdgeWidths;  差异内容：slice?: EdgeWidths; | component/image.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum DataOperationType  差异内容： declare enum DataOperationType | component/lazy\_for\_each.d.ts |
| 新增API | NA | 类名：DataOperationType；  API声明：ADD = 'add'  差异内容：ADD = 'add' | component/lazy\_for\_each.d.ts |
| 新增API | NA | 类名：DataOperationType；  API声明：DELETE = 'delete'  差异内容：DELETE = 'delete' | component/lazy\_for\_each.d.ts |
| 新增API | NA | 类名：DataOperationType；  API声明：EXCHANGE = 'exchange'  差异内容：EXCHANGE = 'exchange' | component/lazy\_for\_each.d.ts |
| 新增API | NA | 类名：DataOperationType；  API声明：MOVE = 'move'  差异内容：MOVE = 'move' | component/lazy\_for\_each.d.ts |
| 新增API | NA | 类名：DataOperationType；  API声明：CHANGE = 'change'  差异内容：CHANGE = 'change' | component/lazy\_for\_each.d.ts |
| 新增API | NA | 类名：DataOperationType；  API声明：RELOAD = 'reload'  差异内容：RELOAD = 'reload' | component/lazy\_for\_each.d.ts |
| 新增API | NA | 类名：global；  API声明： interface DataAddOperation  差异内容： interface DataAddOperation | component/lazy\_for\_each.d.ts |
| 新增API | NA | 类名：DataAddOperation；  API声明：type: DataOperationType.ADD;  差异内容：type: DataOperationType.ADD; | component/lazy\_for\_each.d.ts |
| 新增API | NA | 类名：DataAddOperation；  API声明：index: number;  差异内容：index: number; | component/lazy\_for\_each.d.ts |
| 新增API | NA | 类名：DataAddOperation；  API声明：count?: number;  差异内容：count?: number; | component/lazy\_for\_each.d.ts |
| 新增API | NA | 类名：DataAddOperation；  API声明：key?: string | Array<string>;  差异内容：key?: string | Array<string>; | component/lazy\_for\_each.d.ts |
| 新增API | NA | 类名：global；  API声明： interface DataDeleteOperation  差异内容： interface DataDeleteOperation | component/lazy\_for\_each.d.ts |
| 新增API | NA | 类名：DataDeleteOperation；  API声明：type: DataOperationType.DELETE;  差异内容：type: DataOperationType.DELETE; | component/lazy\_for\_each.d.ts |
| 新增API | NA | 类名：DataDeleteOperation；  API声明：index: number;  差异内容：index: number; | component/lazy\_for\_each.d.ts |
| 新增API | NA | 类名：DataDeleteOperation；  API声明：count?: number;  差异内容：count?: number; | component/lazy\_for\_each.d.ts |
| 新增API | NA | 类名：global；  API声明： interface DataChangeOperation  差异内容： interface DataChangeOperation | component/lazy\_for\_each.d.ts |
| 新增API | NA | 类名：DataChangeOperation；  API声明：type: DataOperationType.CHANGE;  差异内容：type: DataOperationType.CHANGE; | component/lazy\_for\_each.d.ts |
| 新增API | NA | 类名：DataChangeOperation；  API声明：index: number;  差异内容：index: number; | component/lazy\_for\_each.d.ts |
| 新增API | NA | 类名：DataChangeOperation；  API声明：key?: string;  差异内容：key?: string; | component/lazy\_for\_each.d.ts |
| 新增API | NA | 类名：global；  API声明： interface MoveIndex  差异内容： interface MoveIndex | component/lazy\_for\_each.d.ts |
| 新增API | NA | 类名：MoveIndex；  API声明：from: number;  差异内容：from: number; | component/lazy\_for\_each.d.ts |
| 新增API | NA | 类名：MoveIndex；  API声明：to: number;  差异内容：to: number; | component/lazy\_for\_each.d.ts |
| 新增API | NA | 类名：global；  API声明： interface ExchangeIndex  差异内容： interface ExchangeIndex | component/lazy\_for\_each.d.ts |
| 新增API | NA | 类名：ExchangeIndex；  API声明：start: number;  差异内容：start: number; | component/lazy\_for\_each.d.ts |
| 新增API | NA | 类名：ExchangeIndex；  API声明：end: number;  差异内容：end: number; | component/lazy\_for\_each.d.ts |
| 新增API | NA | 类名：global；  API声明： interface ExchangeKey  差异内容： interface ExchangeKey | component/lazy\_for\_each.d.ts |
| 新增API | NA | 类名：ExchangeKey；  API声明：start: string;  差异内容：start: string; | component/lazy\_for\_each.d.ts |
| 新增API | NA | 类名：ExchangeKey；  API声明：end: string;  差异内容：end: string; | component/lazy\_for\_each.d.ts |
| 新增API | NA | 类名：global；  API声明： interface DataMoveOperation  差异内容： interface DataMoveOperation | component/lazy\_for\_each.d.ts |
| 新增API | NA | 类名：DataMoveOperation；  API声明：type: DataOperationType.MOVE;  差异内容：type: DataOperationType.MOVE; | component/lazy\_for\_each.d.ts |
| 新增API | NA | 类名：DataMoveOperation；  API声明：index: MoveIndex;  差异内容：index: MoveIndex; | component/lazy\_for\_each.d.ts |
| 新增API | NA | 类名：DataMoveOperation；  API声明：key?: string;  差异内容：key?: string; | component/lazy\_for\_each.d.ts |
| 新增API | NA | 类名：global；  API声明： interface DataExchangeOperation  差异内容： interface DataExchangeOperation | component/lazy\_for\_each.d.ts |
| 新增API | NA | 类名：DataExchangeOperation；  API声明：type: DataOperationType.EXCHANGE;  差异内容：type: DataOperationType.EXCHANGE; | component/lazy\_for\_each.d.ts |
| 新增API | NA | 类名：DataExchangeOperation；  API声明：index: ExchangeIndex;  差异内容：index: ExchangeIndex; | component/lazy\_for\_each.d.ts |
| 新增API | NA | 类名：DataExchangeOperation；  API声明：key?: ExchangeKey;  差异内容：key?: ExchangeKey; | component/lazy\_for\_each.d.ts |
| 新增API | NA | 类名：global；  API声明： interface DataReloadOperation  差异内容： interface DataReloadOperation | component/lazy\_for\_each.d.ts |
| 新增API | NA | 类名：DataReloadOperation；  API声明：type: DataOperationType.RELOAD;  差异内容：type: DataOperationType.RELOAD; | component/lazy\_for\_each.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type DataOperation = DataAddOperation | DataDeleteOperation | DataChangeOperation | DataMoveOperation | DataExchangeOperation | DataReloadOperation;  差异内容：declare type DataOperation = DataAddOperation | DataDeleteOperation | DataChangeOperation | DataMoveOperation | DataExchangeOperation | DataReloadOperation; | component/lazy\_for\_each.d.ts |
| 新增API | NA | 类名：DataChangeListener；  API声明：onDatasetChange(dataOperations: DataOperation[]): void;  差异内容：onDatasetChange(dataOperations: DataOperation[]): void; | component/lazy\_for\_each.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum ListItemGroupArea  差异内容： declare enum ListItemGroupArea | component/list.d.ts |
| 新增API | NA | 类名：ListItemGroupArea；  API声明：NONE = 0  差异内容：NONE = 0 | component/list.d.ts |
| 新增API | NA | 类名：ListItemGroupArea；  API声明：IN\_LIST\_ITEM\_AREA = 1  差异内容：IN\_LIST\_ITEM\_AREA = 1 | component/list.d.ts |
| 新增API | NA | 类名：ListItemGroupArea；  API声明：IN\_HEADER\_AREA = 2  差异内容：IN\_HEADER\_AREA = 2 | component/list.d.ts |
| 新增API | NA | 类名：ListItemGroupArea；  API声明：IN\_FOOTER\_AREA = 3  差异内容：IN\_FOOTER\_AREA = 3 | component/list.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum ScrollSnapAlign  差异内容： declare enum ScrollSnapAlign | component/list.d.ts |
| 新增API | NA | 类名：ScrollSnapAlign；  API声明：NONE  差异内容：NONE | component/list.d.ts |
| 新增API | NA | 类名：ScrollSnapAlign；  API声明：START  差异内容：START | component/list.d.ts |
| 新增API | NA | 类名：ScrollSnapAlign；  API声明：CENTER  差异内容：CENTER | component/list.d.ts |
| 新增API | NA | 类名：ScrollSnapAlign；  API声明：END  差异内容：END | component/list.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface CloseSwipeActionOptions  差异内容： declare interface CloseSwipeActionOptions | component/list.d.ts |
| 新增API | NA | 类名：CloseSwipeActionOptions；  API声明：onFinish?: () => void;  差异内容：onFinish?: () => void; | component/list.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface VisibleListContentInfo  差异内容： declare interface VisibleListContentInfo | component/list.d.ts |
| 新增API | NA | 类名：VisibleListContentInfo；  API声明：index: number;  差异内容：index: number; | component/list.d.ts |
| 新增API | NA | 类名：VisibleListContentInfo；  API声明：itemGroupArea?: ListItemGroupArea;  差异内容：itemGroupArea?: ListItemGroupArea; | component/list.d.ts |
| 新增API | NA | 类名：VisibleListContentInfo；  API声明：itemIndexInGroup?: number;  差异内容：itemIndexInGroup?: number; | component/list.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type OnScrollVisibleContentChangeCallback = (start: VisibleListContentInfo, end: VisibleListContentInfo) => void;  差异内容：declare type OnScrollVisibleContentChangeCallback = (start: VisibleListContentInfo, end: VisibleListContentInfo) => void; | component/list.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class ListScroller  差异内容： declare class ListScroller | component/list.d.ts |
| 新增API | NA | 类名：ListScroller；  API声明：getItemRectInGroup(index: number, indexInGroup: number): RectResult;  差异内容：getItemRectInGroup(index: number, indexInGroup: number): RectResult; | component/list.d.ts |
| 新增API | NA | 类名：ListScroller；  API声明：scrollToItemInGroup(index: number, indexInGroup: number, smooth?: boolean, align?: ScrollAlign): void;  差异内容：scrollToItemInGroup(index: number, indexInGroup: number, smooth?: boolean, align?: ScrollAlign): void; | component/list.d.ts |
| 新增API | NA | 类名：ListScroller；  API声明：closeAllSwipeActions(options?: CloseSwipeActionOptions): void;  差异内容：closeAllSwipeActions(options?: CloseSwipeActionOptions): void; | component/list.d.ts |
| 新增API | NA | 类名：ListAttribute；  API声明：fadingEdge(value: Optional<boolean>): ListAttribute;  差异内容：fadingEdge(value: Optional<boolean>): ListAttribute; | component/list.d.ts |
| 新增API | NA | 类名：ListAttribute；  API声明：contentStartOffset(value: number): ListAttribute;  差异内容：contentStartOffset(value: number): ListAttribute; | component/list.d.ts |
| 新增API | NA | 类名：ListAttribute；  API声明：contentEndOffset(value: number): ListAttribute;  差异内容：contentEndOffset(value: number): ListAttribute; | component/list.d.ts |
| 新增API | NA | 类名：ListAttribute；  API声明：scrollSnapAlign(value: ScrollSnapAlign): ListAttribute;  差异内容：scrollSnapAlign(value: ScrollSnapAlign): ListAttribute; | component/list.d.ts |
| 新增API | NA | 类名：ListAttribute；  API声明：nestedScroll(value: NestedScrollOptions): ListAttribute;  差异内容：nestedScroll(value: NestedScrollOptions): ListAttribute; | component/list.d.ts |
| 新增API | NA | 类名：ListAttribute；  API声明：enableScrollInteraction(value: boolean): ListAttribute;  差异内容：enableScrollInteraction(value: boolean): ListAttribute; | component/list.d.ts |
| 新增API | NA | 类名：ListAttribute；  API声明：friction(value: number | Resource): ListAttribute;  差异内容：friction(value: number | Resource): ListAttribute; | component/list.d.ts |
| 新增API | NA | 类名：ListAttribute；  API声明：childrenMainSize(value: ChildrenMainSize): ListAttribute;  差异内容：childrenMainSize(value: ChildrenMainSize): ListAttribute; | component/list.d.ts |
| 新增API | NA | 类名：ListAttribute；  API声明：onScrollVisibleContentChange(handler: OnScrollVisibleContentChangeCallback): ListAttribute;  差异内容：onScrollVisibleContentChange(handler: OnScrollVisibleContentChangeCallback): ListAttribute; | component/list.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum SwipeActionState  差异内容： declare enum SwipeActionState | component/list\_item.d.ts |
| 新增API | NA | 类名：SwipeActionState；  API声明：COLLAPSED  差异内容：COLLAPSED | component/list\_item.d.ts |
| 新增API | NA | 类名：SwipeActionState；  API声明：EXPANDED  差异内容：EXPANDED | component/list\_item.d.ts |
| 新增API | NA | 类名：SwipeActionState；  API声明：ACTIONING  差异内容：ACTIONING | component/list\_item.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface SwipeActionItem  差异内容： declare interface SwipeActionItem | component/list\_item.d.ts |
| 新增API | NA | 类名：SwipeActionItem；  API声明：builder?: CustomBuilder;  差异内容：builder?: CustomBuilder; | component/list\_item.d.ts |
| 新增API | NA | 类名：SwipeActionItem；  API声明：actionAreaDistance?: Length;  差异内容：actionAreaDistance?: Length; | component/list\_item.d.ts |
| 新增API | NA | 类名：SwipeActionItem；  API声明：onAction?: () => void;  差异内容：onAction?: () => void; | component/list\_item.d.ts |
| 新增API | NA | 类名：SwipeActionItem；  API声明：onEnterActionArea?: () => void;  差异内容：onEnterActionArea?: () => void; | component/list\_item.d.ts |
| 新增API | NA | 类名：SwipeActionItem；  API声明：onExitActionArea?: () => void;  差异内容：onExitActionArea?: () => void; | component/list\_item.d.ts |
| 新增API | NA | 类名：SwipeActionItem；  API声明：onStateChange?: (state: SwipeActionState) => void;  差异内容：onStateChange?: (state: SwipeActionState) => void; | component/list\_item.d.ts |
| 新增API | NA | 类名：SwipeActionOptions；  API声明：onOffsetChange?: (offset: number) => void;  差异内容：onOffsetChange?: (offset: number) => void; | component/list\_item.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum ListItemStyle  差异内容： declare enum ListItemStyle | component/list\_item.d.ts |
| 新增API | NA | 类名：ListItemStyle；  API声明：NONE = 0  差异内容：NONE = 0 | component/list\_item.d.ts |
| 新增API | NA | 类名：ListItemStyle；  API声明：CARD = 1  差异内容：CARD = 1 | component/list\_item.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface ListItemOptions  差异内容： declare interface ListItemOptions | component/list\_item.d.ts |
| 新增API | NA | 类名：ListItemOptions；  API声明：style?: ListItemStyle;  差异内容：style?: ListItemStyle; | component/list\_item.d.ts |
| 新增API | NA | 类名：ListItemAttribute；  API声明：selected(value: boolean): ListItemAttribute;  差异内容：selected(value: boolean): ListItemAttribute; | component/list\_item.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum ListItemGroupStyle  差异内容： declare enum ListItemGroupStyle | component/list\_item\_group.d.ts |
| 新增API | NA | 类名：ListItemGroupStyle；  API声明：NONE = 0  差异内容：NONE = 0 | component/list\_item\_group.d.ts |
| 新增API | NA | 类名：ListItemGroupStyle；  API声明：CARD = 1  差异内容：CARD = 1 | component/list\_item\_group.d.ts |
| 新增API | NA | 类名：ListItemGroupOptions；  API声明：style?: ListItemGroupStyle;  差异内容：style?: ListItemGroupStyle; | component/list\_item\_group.d.ts |
| 新增API | NA | 类名：ListItemGroupAttribute；  API声明：childrenMainSize(value: ChildrenMainSize): ListItemGroupAttribute;  差异内容：childrenMainSize(value: ChildrenMainSize): ListItemGroupAttribute; | component/list\_item\_group.d.ts |
| 新增API | NA | 类名：LoadingProgressAttribute；  API声明：enableLoading(value: boolean): LoadingProgressAttribute;  差异内容：enableLoading(value: boolean): LoadingProgressAttribute; | component/loading\_progress.d.ts |
| 新增API | NA | 类名：LoadingProgressAttribute；  API声明：contentModifier(modifier: ContentModifier<LoadingProgressConfiguration>): LoadingProgressAttribute;  差异内容：contentModifier(modifier: ContentModifier<LoadingProgressConfiguration>): LoadingProgressAttribute; | component/loading\_progress.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface LoadingProgressConfiguration  差异内容： declare interface LoadingProgressConfiguration | component/loading\_progress.d.ts |
| 新增API | NA | 类名：LoadingProgressConfiguration；  API声明：enableLoading: boolean;  差异内容：enableLoading: boolean; | component/loading\_progress.d.ts |
| 新增API | NA | 类名：MarqueeAttribute；  API声明：marqueeUpdateStrategy(value: MarqueeUpdateStrategy): MarqueeAttribute;  差异内容：marqueeUpdateStrategy(value: MarqueeUpdateStrategy): MarqueeAttribute; | component/marquee.d.ts |
| 新增API | NA | 类名：Matrix2D；  API声明：scaleX?: number;  差异内容：scaleX?: number; | component/matrix2d.d.ts |
| 新增API | NA | 类名：Matrix2D；  API声明：rotateY?: number;  差异内容：rotateY?: number; | component/matrix2d.d.ts |
| 新增API | NA | 类名：Matrix2D；  API声明：rotateX?: number;  差异内容：rotateX?: number; | component/matrix2d.d.ts |
| 新增API | NA | 类名：Matrix2D；  API声明：scaleY?: number;  差异内容：scaleY?: number; | component/matrix2d.d.ts |
| 新增API | NA | 类名：Matrix2D；  API声明：translateX?: number;  差异内容：translateX?: number; | component/matrix2d.d.ts |
| 新增API | NA | 类名：Matrix2D；  API声明：translateY?: number;  差异内容：translateY?: number; | component/matrix2d.d.ts |
| 新增API | NA | 类名：Matrix2D；  API声明：identity(): Matrix2D;  差异内容：identity(): Matrix2D; | component/matrix2d.d.ts |
| 新增API | NA | 类名：Matrix2D；  API声明：invert(): Matrix2D;  差异内容：invert(): Matrix2D; | component/matrix2d.d.ts |
| 新增API | NA | 类名：Matrix2D；  API声明：multiply(other?: Matrix2D): Matrix2D;  差异内容：multiply(other?: Matrix2D): Matrix2D; | component/matrix2d.d.ts |
| 新增API | NA | 类名：Matrix2D；  API声明：rotate(rx?: number, ry?: number): Matrix2D;  差异内容：rotate(rx?: number, ry?: number): Matrix2D; | component/matrix2d.d.ts |
| 新增API | NA | 类名：Matrix2D；  API声明：rotate(degree: number, rx?: number, ry?: number): Matrix2D;  差异内容：rotate(degree: number, rx?: number, ry?: number): Matrix2D; | component/matrix2d.d.ts |
| 新增API | NA | 类名：Matrix2D；  API声明：translate(tx?: number, ty?: number): Matrix2D;  差异内容：translate(tx?: number, ty?: number): Matrix2D; | component/matrix2d.d.ts |
| 新增API | NA | 类名：Matrix2D；  API声明：scale(sx?: number, sy?: number): Matrix2D;  差异内容：scale(sx?: number, sy?: number): Matrix2D; | component/matrix2d.d.ts |
| 新增API | NA | 类名：MenuAttribute；  API声明：font(value: Font): MenuAttribute;  差异内容：font(value: Font): MenuAttribute; | component/menu.d.ts |
| 新增API | NA | 类名：MenuAttribute；  API声明：fontColor(value: ResourceColor): MenuAttribute;  差异内容：fontColor(value: ResourceColor): MenuAttribute; | component/menu.d.ts |
| 新增API | NA | 类名：MenuAttribute；  API声明：radius(value: Dimension | BorderRadiuses): MenuAttribute;  差异内容：radius(value: Dimension | BorderRadiuses): MenuAttribute; | component/menu.d.ts |
| 新增API | NA | 类名：MenuItemAttribute；  API声明：contentFont(value: Font): MenuItemAttribute;  差异内容：contentFont(value: Font): MenuItemAttribute; | component/menu\_item.d.ts |
| 新增API | NA | 类名：MenuItemAttribute；  API声明：contentFontColor(value: ResourceColor): MenuItemAttribute;  差异内容：contentFontColor(value: ResourceColor): MenuItemAttribute; | component/menu\_item.d.ts |
| 新增API | NA | 类名：MenuItemAttribute；  API声明：labelFont(value: Font): MenuItemAttribute;  差异内容：labelFont(value: Font): MenuItemAttribute; | component/menu\_item.d.ts |
| 新增API | NA | 类名：MenuItemAttribute；  API声明：labelFontColor(value: ResourceColor): MenuItemAttribute;  差异内容：labelFontColor(value: ResourceColor): MenuItemAttribute; | component/menu\_item.d.ts |
| 新增API | NA | 类名：NavigationMenuItem；  API声明：isEnabled?: boolean;  差异内容：isEnabled?: boolean; | component/navigation.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface PopInfo  差异内容： declare interface PopInfo | component/navigation.d.ts |
| 新增API | NA | 类名：PopInfo；  API声明：info: NavPathInfo;  差异内容：info: NavPathInfo; | component/navigation.d.ts |
| 新增API | NA | 类名：PopInfo；  API声明：result: Object;  差异内容：result: Object; | component/navigation.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class NavPathInfo  差异内容： declare class NavPathInfo | component/navigation.d.ts |
| 新增API | NA | 类名：NavPathInfo；  API声明：name: string;  差异内容：name: string; | component/navigation.d.ts |
| 新增API | NA | 类名：NavPathInfo；  API声明：param?: unknown;  差异内容：param?: unknown; | component/navigation.d.ts |
| 新增API | NA | 类名：NavPathInfo；  API声明：onPop?: import('../api/@ohos.base').Callback<PopInfo>;  差异内容：onPop?: import('../api/@ohos.base').Callback<PopInfo>; | component/navigation.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class NavPathStack  差异内容： declare class NavPathStack | component/navigation.d.ts |
| 新增API | NA | 类名：NavPathStack；  API声明：pushPath(info: NavPathInfo, animated?: boolean): void;  差异内容：pushPath(info: NavPathInfo, animated?: boolean): void; | component/navigation.d.ts |
| 新增API | NA | 类名：NavPathStack；  API声明：pushDestination(info: NavPathInfo, animated?: boolean): Promise<void>;  差异内容：pushDestination(info: NavPathInfo, animated?: boolean): Promise<void>; | component/navigation.d.ts |
| 新增API | NA | 类名：NavPathStack；  API声明：pushPathByName(name: string, param: unknown, animated?: boolean): void;  差异内容：pushPathByName(name: string, param: unknown, animated?: boolean): void; | component/navigation.d.ts |
| 新增API | NA | 类名：NavPathStack；  API声明：pushPathByName(name: string, param: Object, onPop: import('../api/@ohos.base').Callback<PopInfo>, animated?: boolean): void;  差异内容：pushPathByName(name: string, param: Object, onPop: import('../api/@ohos.base').Callback<PopInfo>, animated?: boolean): void; | component/navigation.d.ts |
| 新增API | NA | 类名：NavPathStack；  API声明：pushDestinationByName(name: string, param: Object, animated?: boolean): Promise<void>;  差异内容：pushDestinationByName(name: string, param: Object, animated?: boolean): Promise<void>; | component/navigation.d.ts |
| 新增API | NA | 类名：NavPathStack；  API声明：pushDestinationByName(name: string, param: Object, onPop: import('../api/@ohos.base').Callback<PopInfo>, animated?: boolean): Promise<void>;  差异内容：pushDestinationByName(name: string, param: Object, onPop: import('../api/@ohos.base').Callback<PopInfo>, animated?: boolean): Promise<void>; | component/navigation.d.ts |
| 新增API | NA | 类名：NavPathStack；  API声明：replacePath(info: NavPathInfo, animated?: boolean): void;  差异内容：replacePath(info: NavPathInfo, animated?: boolean): void; | component/navigation.d.ts |
| 新增API | NA | 类名：NavPathStack；  API声明：replacePathByName(name: string, param: Object, animated?: boolean): void;  差异内容：replacePathByName(name: string, param: Object, animated?: boolean): void; | component/navigation.d.ts |
| 新增API | NA | 类名：NavPathStack；  API声明：removeByIndexes(indexes: Array<number>): number;  差异内容：removeByIndexes(indexes: Array<number>): number; | component/navigation.d.ts |
| 新增API | NA | 类名：NavPathStack；  API声明：removeByName(name: string): number;  差异内容：removeByName(name: string): number; | component/navigation.d.ts |
| 新增API | NA | 类名：NavPathStack；  API声明：pop(animated?: boolean): NavPathInfo | undefined;  差异内容：pop(animated?: boolean): NavPathInfo | undefined; | component/navigation.d.ts |
| 新增API | NA | 类名：NavPathStack；  API声明：pop(result: Object, animated?: boolean): NavPathInfo | undefined;  差异内容：pop(result: Object, animated?: boolean): NavPathInfo | undefined; | component/navigation.d.ts |
| 新增API | NA | 类名：NavPathStack；  API声明：popToName(name: string, animated?: boolean): number;  差异内容：popToName(name: string, animated?: boolean): number; | component/navigation.d.ts |
| 新增API | NA | 类名：NavPathStack；  API声明：popToName(name: string, result: Object, animated?: boolean): number;  差异内容：popToName(name: string, result: Object, animated?: boolean): number; | component/navigation.d.ts |
| 新增API | NA | 类名：NavPathStack；  API声明：popToIndex(index: number, animated?: boolean): void;  差异内容：popToIndex(index: number, animated?: boolean): void; | component/navigation.d.ts |
| 新增API | NA | 类名：NavPathStack；  API声明：popToIndex(index: number, result: Object, animated?: boolean): void;  差异内容：popToIndex(index: number, result: Object, animated?: boolean): void; | component/navigation.d.ts |
| 新增API | NA | 类名：NavPathStack；  API声明：moveToTop(name: string, animated?: boolean): number;  差异内容：moveToTop(name: string, animated?: boolean): number; | component/navigation.d.ts |
| 新增API | NA | 类名：NavPathStack；  API声明：moveIndexToTop(index: number, animated?: boolean): void;  差异内容：moveIndexToTop(index: number, animated?: boolean): void; | component/navigation.d.ts |
| 新增API | NA | 类名：NavPathStack；  API声明：clear(animated?: boolean): void;  差异内容：clear(animated?: boolean): void; | component/navigation.d.ts |
| 新增API | NA | 类名：NavPathStack；  API声明：getAllPathName(): Array<string>;  差异内容：getAllPathName(): Array<string>; | component/navigation.d.ts |
| 新增API | NA | 类名：NavPathStack；  API声明：getParamByIndex(index: number): unknown | undefined;  差异内容：getParamByIndex(index: number): unknown | undefined; | component/navigation.d.ts |
| 新增API | NA | 类名：NavPathStack；  API声明：getParamByName(name: string): Array<unknown>;  差异内容：getParamByName(name: string): Array<unknown>; | component/navigation.d.ts |
| 新增API | NA | 类名：NavPathStack；  API声明：getIndexByName(name: string): Array<number>;  差异内容：getIndexByName(name: string): Array<number>; | component/navigation.d.ts |
| 新增API | NA | 类名：NavPathStack；  API声明：getParent(): NavPathStack | null;  差异内容：getParent(): NavPathStack | null; | component/navigation.d.ts |
| 新增API | NA | 类名：NavPathStack；  API声明：size(): number;  差异内容：size(): number; | component/navigation.d.ts |
| 新增API | NA | 类名：NavPathStack；  API声明：disableAnimation(value: boolean): void;  差异内容：disableAnimation(value: boolean): void; | component/navigation.d.ts |
| 新增API | NA | 类名：NavPathStack；  API声明：setInterception(interception: NavigationInterception): void;  差异内容：setInterception(interception: NavigationInterception): void; | component/navigation.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type NavBar = 'navBar';  差异内容：declare type NavBar = 'navBar'; | component/navigation.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type InterceptionShowCallback = (from: NavDestinationContext | NavBar, to: NavDestinationContext | NavBar, operation: NavigationOperation, isAnimated: boolean) => void;  差异内容：declare type InterceptionShowCallback = (from: NavDestinationContext | NavBar, to: NavDestinationContext | NavBar, operation: NavigationOperation, isAnimated: boolean) => void; | component/navigation.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type InterceptionModeCallback = (mode: NavigationMode) => void;  差异内容：declare type InterceptionModeCallback = (mode: NavigationMode) => void; | component/navigation.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface NavigationInterception  差异内容： declare interface NavigationInterception | component/navigation.d.ts |
| 新增API | NA | 类名：NavigationInterception；  API声明：willShow?: InterceptionShowCallback;  差异内容：willShow?: InterceptionShowCallback; | component/navigation.d.ts |
| 新增API | NA | 类名：NavigationInterception；  API声明：didShow?: InterceptionShowCallback;  差异内容：didShow?: InterceptionShowCallback; | component/navigation.d.ts |
| 新增API | NA | 类名：NavigationInterception；  API声明：modeChange?: InterceptionModeCallback;  差异内容：modeChange?: InterceptionModeCallback; | component/navigation.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum ToolbarItemStatus  差异内容： declare enum ToolbarItemStatus | component/navigation.d.ts |
| 新增API | NA | 类名：ToolbarItemStatus；  API声明：NORMAL = 0  差异内容：NORMAL = 0 | component/navigation.d.ts |
| 新增API | NA | 类名：ToolbarItemStatus；  API声明：DISABLED = 1  差异内容：DISABLED = 1 | component/navigation.d.ts |
| 新增API | NA | 类名：ToolbarItemStatus；  API声明：ACTIVE = 2  差异内容：ACTIVE = 2 | component/navigation.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum NavigationOperation  差异内容： declare enum NavigationOperation | component/navigation.d.ts |
| 新增API | NA | 类名：NavigationOperation；  API声明：PUSH = 1  差异内容：PUSH = 1 | component/navigation.d.ts |
| 新增API | NA | 类名：NavigationOperation；  API声明：POP = 2  差异内容：POP = 2 | component/navigation.d.ts |
| 新增API | NA | 类名：NavigationOperation；  API声明：REPLACE = 3  差异内容：REPLACE = 3 | component/navigation.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface ToolbarItem  差异内容： declare interface ToolbarItem | component/navigation.d.ts |
| 新增API | NA | 类名：ToolbarItem；  API声明：value: ResourceStr;  差异内容：value: ResourceStr; | component/navigation.d.ts |
| 新增API | NA | 类名：ToolbarItem；  API声明：icon?: ResourceStr;  差异内容：icon?: ResourceStr; | component/navigation.d.ts |
| 新增API | NA | 类名：ToolbarItem；  API声明：action?: () => void;  差异内容：action?: () => void; | component/navigation.d.ts |
| 新增API | NA | 类名：ToolbarItem；  API声明：status?: ToolbarItemStatus;  差异内容：status?: ToolbarItemStatus; | component/navigation.d.ts |
| 新增API | NA | 类名：ToolbarItem；  API声明：activeIcon?: ResourceStr;  差异内容：activeIcon?: ResourceStr; | component/navigation.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface NavigationTitleOptions  差异内容： declare interface NavigationTitleOptions | component/navigation.d.ts |
| 新增API | NA | 类名：NavigationTitleOptions；  API声明：backgroundColor?: ResourceColor;  差异内容：backgroundColor?: ResourceColor; | component/navigation.d.ts |
| 新增API | NA | 类名：NavigationTitleOptions；  API声明：backgroundBlurStyle?: BlurStyle;  差异内容：backgroundBlurStyle?: BlurStyle; | component/navigation.d.ts |
| 新增API | NA | 类名：NavigationTitleOptions；  API声明：barStyle?: BarStyle;  差异内容：barStyle?: BarStyle; | component/navigation.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum BarStyle  差异内容： declare enum BarStyle | component/navigation.d.ts |
| 新增API | NA | 类名：BarStyle；  API声明：STANDARD = 0  差异内容：STANDARD = 0 | component/navigation.d.ts |
| 新增API | NA | 类名：BarStyle；  API声明：STACK = 1  差异内容：STACK = 1 | component/navigation.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface NavigationToolbarOptions  差异内容： declare interface NavigationToolbarOptions | component/navigation.d.ts |
| 新增API | NA | 类名：NavigationToolbarOptions；  API声明：backgroundColor?: ResourceColor;  差异内容：backgroundColor?: ResourceColor; | component/navigation.d.ts |
| 新增API | NA | 类名：NavigationToolbarOptions；  API声明：backgroundBlurStyle?: BlurStyle;  差异内容：backgroundBlurStyle?: BlurStyle; | component/navigation.d.ts |
| 新增API | NA | 类名：NavigationAttribute；  API声明：navBarWidthRange(value: [  Dimension,  Dimension  ]): NavigationAttribute;  差异内容：navBarWidthRange(value: [  Dimension,  Dimension  ]): NavigationAttribute; | component/navigation.d.ts |
| 新增API | NA | 类名：NavigationAttribute；  API声明：minContentWidth(value: Dimension): NavigationAttribute;  差异内容：minContentWidth(value: Dimension): NavigationAttribute; | component/navigation.d.ts |
| 新增API | NA | 类名：NavigationAttribute；  API声明：toolbarConfiguration(value: Array<ToolbarItem> | CustomBuilder, options?: NavigationToolbarOptions): NavigationAttribute;  差异内容：toolbarConfiguration(value: Array<ToolbarItem> | CustomBuilder, options?: NavigationToolbarOptions): NavigationAttribute; | component/navigation.d.ts |
| 新增API | NA | 类名：NavigationAttribute；  API声明：onNavigationModeChange(callback: (mode: NavigationMode) => void): NavigationAttribute;  差异内容：onNavigationModeChange(callback: (mode: NavigationMode) => void): NavigationAttribute; | component/navigation.d.ts |
| 新增API | NA | 类名：NavigationAttribute；  API声明：navDestination(builder: (name: string, param: unknown) => void): NavigationAttribute;  差异内容：navDestination(builder: (name: string, param: unknown) => void): NavigationAttribute; | component/navigation.d.ts |
| 新增API | NA | 类名：NavigationAttribute；  API声明：customNavContentTransition(delegate: (from: NavContentInfo, to: NavContentInfo, operation: NavigationOperation) => NavigationAnimatedTransition | undefined): NavigationAttribute;  差异内容：customNavContentTransition(delegate: (from: NavContentInfo, to: NavContentInfo, operation: NavigationOperation) => NavigationAnimatedTransition | undefined): NavigationAttribute; | component/navigation.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface NavigationAnimatedTransition  差异内容： declare interface NavigationAnimatedTransition | component/navigation.d.ts |
| 新增API | NA | 类名：NavigationAnimatedTransition；  API声明：onTransitionEnd?: (success: boolean) => void;  差异内容：onTransitionEnd?: (success: boolean) => void; | component/navigation.d.ts |
| 新增API | NA | 类名：NavigationAnimatedTransition；  API声明：timeout?: number;  差异内容：timeout?: number; | component/navigation.d.ts |
| 新增API | NA | 类名：NavigationAnimatedTransition；  API声明：transition: (transitionProxy: NavigationTransitionProxy) => void;  差异内容：transition: (transitionProxy: NavigationTransitionProxy) => void; | component/navigation.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface NavigationTransitionProxy  差异内容： declare interface NavigationTransitionProxy | component/navigation.d.ts |
| 新增API | NA | 类名：NavigationTransitionProxy；  API声明：from: NavContentInfo;  差异内容：from: NavContentInfo; | component/navigation.d.ts |
| 新增API | NA | 类名：NavigationTransitionProxy；  API声明：to: NavContentInfo;  差异内容：to: NavContentInfo; | component/navigation.d.ts |
| 新增API | NA | 类名：NavigationTransitionProxy；  API声明：finishTransition(): void;  差异内容：finishTransition(): void; | component/navigation.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface NavContentInfo  差异内容： declare interface NavContentInfo | component/navigation.d.ts |
| 新增API | NA | 类名：NavContentInfo；  API声明：name?: string;  差异内容：name?: string; | component/navigation.d.ts |
| 新增API | NA | 类名：NavContentInfo；  API声明：index: number;  差异内容：index: number; | component/navigation.d.ts |
| 新增API | NA | 类名：NavContentInfo；  API声明：mode?: NavDestinationMode;  差异内容：mode?: NavDestinationMode; | component/navigation.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum NavDestinationMode  差异内容： declare enum NavDestinationMode | component/nav\_destination.d.ts |
| 新增API | NA | 类名：NavDestinationMode；  API声明：STANDARD = 0  差异内容：STANDARD = 0 | component/nav\_destination.d.ts |
| 新增API | NA | 类名：NavDestinationMode；  API声明：DIALOG = 1  差异内容：DIALOG = 1 | component/nav\_destination.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface RouteMapConfig  差异内容： declare interface RouteMapConfig | component/nav\_destination.d.ts |
| 新增API | NA | 类名：RouteMapConfig；  API声明：name: string;  差异内容：name: string; | component/nav\_destination.d.ts |
| 新增API | NA | 类名：RouteMapConfig；  API声明：pageSourceFile: string;  差异内容：pageSourceFile: string; | component/nav\_destination.d.ts |
| 新增API | NA | 类名：RouteMapConfig；  API声明：data: Object;  差异内容：data: Object; | component/nav\_destination.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface NavDestinationContext  差异内容： declare interface NavDestinationContext | component/nav\_destination.d.ts |
| 新增API | NA | 类名：NavDestinationContext；  API声明：pathInfo: NavPathInfo;  差异内容：pathInfo: NavPathInfo; | component/nav\_destination.d.ts |
| 新增API | NA | 类名：NavDestinationContext；  API声明：pathStack: NavPathStack;  差异内容：pathStack: NavPathStack; | component/nav\_destination.d.ts |
| 新增API | NA | 类名：NavDestinationContext；  API声明：navDestinationId?: string;  差异内容：navDestinationId?: string; | component/nav\_destination.d.ts |
| 新增API | NA | 类名：NavDestinationContext；  API声明：getConfigInRouteMap(): RouteMapConfig | undefined;  差异内容：getConfigInRouteMap(): RouteMapConfig | undefined; | component/nav\_destination.d.ts |
| 新增API | NA | 类名：NavDestinationAttribute；  API声明：onShown(callback: () => void): NavDestinationAttribute;  差异内容：onShown(callback: () => void): NavDestinationAttribute; | component/nav\_destination.d.ts |
| 新增API | NA | 类名：NavDestinationAttribute；  API声明：onHidden(callback: () => void): NavDestinationAttribute;  差异内容：onHidden(callback: () => void): NavDestinationAttribute; | component/nav\_destination.d.ts |
| 新增API | NA | 类名：NavDestinationAttribute；  API声明：onBackPressed(callback: () => boolean): NavDestinationAttribute;  差异内容：onBackPressed(callback: () => boolean): NavDestinationAttribute; | component/nav\_destination.d.ts |
| 新增API | NA | 类名：NavDestinationAttribute；  API声明：mode(value: NavDestinationMode): NavDestinationAttribute;  差异内容：mode(value: NavDestinationMode): NavDestinationAttribute; | component/nav\_destination.d.ts |
| 新增API | NA | 类名：NavDestinationAttribute；  API声明：backButtonIcon(value: ResourceStr | PixelMap): NavDestinationAttribute;  差异内容：backButtonIcon(value: ResourceStr | PixelMap): NavDestinationAttribute; | component/nav\_destination.d.ts |
| 新增API | NA | 类名：NavDestinationAttribute；  API声明：menus(value: Array<NavigationMenuItem> | CustomBuilder): NavDestinationAttribute;  差异内容：menus(value: Array<NavigationMenuItem> | CustomBuilder): NavDestinationAttribute; | component/nav\_destination.d.ts |
| 新增API | NA | 类名：NavDestinationAttribute；  API声明：onReady(callback: import('../api/@ohos.base').Callback<NavDestinationContext>): NavDestinationAttribute;  差异内容：onReady(callback: import('../api/@ohos.base').Callback<NavDestinationContext>): NavDestinationAttribute; | component/nav\_destination.d.ts |
| 新增API | NA | 类名：NavDestinationAttribute；  API声明：onWillAppear(callback: Callback<void>): NavDestinationAttribute;  差异内容：onWillAppear(callback: Callback<void>): NavDestinationAttribute; | component/nav\_destination.d.ts |
| 新增API | NA | 类名：NavDestinationAttribute；  API声明：onWillDisappear(callback: Callback<void>): NavDestinationAttribute;  差异内容：onWillDisappear(callback: Callback<void>): NavDestinationAttribute; | component/nav\_destination.d.ts |
| 新增API | NA | 类名：NavDestinationAttribute；  API声明：onWillShow(callback: Callback<void>): NavDestinationAttribute;  差异内容：onWillShow(callback: Callback<void>): NavDestinationAttribute; | component/nav\_destination.d.ts |
| 新增API | NA | 类名：NavDestinationAttribute；  API声明：onWillHide(callback: Callback<void>): NavDestinationAttribute;  差异内容：onWillHide(callback: Callback<void>): NavDestinationAttribute; | component/nav\_destination.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface RouteInfo  差异内容： declare interface RouteInfo | component/nav\_router.d.ts |
| 新增API | NA | 类名：RouteInfo；  API声明：name: string;  差异内容：name: string; | component/nav\_router.d.ts |
| 新增API | NA | 类名：RouteInfo；  API声明：param?: unknown;  差异内容：param?: unknown; | component/nav\_router.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum NavRouteMode  差异内容： declare enum NavRouteMode | component/nav\_router.d.ts |
| 新增API | NA | 类名：NavRouteMode；  API声明：PUSH\_WITH\_RECREATE  差异内容：PUSH\_WITH\_RECREATE | component/nav\_router.d.ts |
| 新增API | NA | 类名：NavRouteMode；  API声明：PUSH  差异内容：PUSH | component/nav\_router.d.ts |
| 新增API | NA | 类名：NavRouteMode；  API声明：REPLACE  差异内容：REPLACE | component/nav\_router.d.ts |
| 新增API | NA | 类名：NavRouterAttribute；  API声明：mode(mode: NavRouteMode): NavRouterAttribute;  差异内容：mode(mode: NavRouteMode): NavRouterAttribute; | component/nav\_router.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface PageTransitionOptions  差异内容： declare interface PageTransitionOptions | component/page\_transition.d.ts |
| 新增API | NA | 类名：PageTransitionOptions；  API声明：type?: RouteType;  差异内容：type?: RouteType; | component/page\_transition.d.ts |
| 新增API | NA | 类名：PageTransitionOptions；  API声明：duration?: number;  差异内容：duration?: number; | component/page\_transition.d.ts |
| 新增API | NA | 类名：PageTransitionOptions；  API声明：curve?: Curve | string | ICurve;  差异内容：curve?: Curve | string | ICurve; | component/page\_transition.d.ts |
| 新增API | NA | 类名：PageTransitionOptions；  API声明：delay?: number;  差异内容：delay?: number; | component/page\_transition.d.ts |
| 新增API | NA | 类名：PanelType；  API声明：CUSTOM = 3  差异内容：CUSTOM = 3 | component/panel.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum PanelHeight  差异内容： declare enum PanelHeight | component/panel.d.ts |
| 新增API | NA | 类名：PanelHeight；  API声明：WRAP\_CONTENT = 'wrapContent'  差异内容：WRAP\_CONTENT = 'wrapContent' | component/panel.d.ts |
| 新增API | NA | 类名：PanelAttribute；  API声明：customHeight(value: Dimension | PanelHeight): PanelAttribute;  差异内容：customHeight(value: Dimension | PanelHeight): PanelAttribute; | component/panel.d.ts |
| 新增API | NA | 类名：PanelAttribute；  API声明：showCloseIcon(value: boolean): PanelAttribute;  差异内容：showCloseIcon(value: boolean): PanelAttribute; | component/panel.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum PatternLockChallengeResult  差异内容： declare enum PatternLockChallengeResult | component/pattern\_lock.d.ts |
| 新增API | NA | 类名：PatternLockChallengeResult；  API声明：CORRECT = 1  差异内容：CORRECT = 1 | component/pattern\_lock.d.ts |
| 新增API | NA | 类名：PatternLockChallengeResult；  API声明：WRONG = 2  差异内容：WRONG = 2 | component/pattern\_lock.d.ts |
| 新增API | NA | 类名：PatternLockController；  API声明：setChallengeResult(result: PatternLockChallengeResult): void;  差异内容：setChallengeResult(result: PatternLockChallengeResult): void; | component/pattern\_lock.d.ts |
| 新增API | NA | 类名：PatternLockAttribute；  API声明：onDotConnect(callback: import('../api/@ohos.base').Callback<number>): PatternLockAttribute;  差异内容：onDotConnect(callback: import('../api/@ohos.base').Callback<number>): PatternLockAttribute; | component/pattern\_lock.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum ProgressStatus  差异内容： declare enum ProgressStatus | component/progress.d.ts |
| 新增API | NA | 类名：ProgressStatus；  API声明：LOADING  差异内容：LOADING | component/progress.d.ts |
| 新增API | NA | 类名：ProgressStatus；  API声明：PROGRESSING  差异内容：PROGRESSING | component/progress.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface CommonProgressStyleOptions  差异内容： declare interface CommonProgressStyleOptions | component/progress.d.ts |
| 新增API | NA | 类名：CommonProgressStyleOptions；  API声明：enableSmoothEffect?: boolean;  差异内容：enableSmoothEffect?: boolean; | component/progress.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface ScanEffectOptions  差异内容： declare interface ScanEffectOptions | component/progress.d.ts |
| 新增API | NA | 类名：ScanEffectOptions；  API声明：enableScanEffect?: boolean;  差异内容：enableScanEffect?: boolean; | component/progress.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface EclipseStyleOptions  差异内容： declare interface EclipseStyleOptions | component/progress.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface ScaleRingStyleOptions  差异内容： declare interface ScaleRingStyleOptions | component/progress.d.ts |
| 新增API | NA | 类名：ScaleRingStyleOptions；  API声明：strokeWidth?: Length;  差异内容：strokeWidth?: Length; | component/progress.d.ts |
| 新增API | NA | 类名：ScaleRingStyleOptions；  API声明：scaleWidth?: Length;  差异内容：scaleWidth?: Length; | component/progress.d.ts |
| 新增API | NA | 类名：ScaleRingStyleOptions；  API声明：scaleCount?: number;  差异内容：scaleCount?: number; | component/progress.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface RingStyleOptions  差异内容： declare interface RingStyleOptions | component/progress.d.ts |
| 新增API | NA | 类名：RingStyleOptions；  API声明：strokeWidth?: Length;  差异内容：strokeWidth?: Length; | component/progress.d.ts |
| 新增API | NA | 类名：RingStyleOptions；  API声明：shadow?: boolean;  差异内容：shadow?: boolean; | component/progress.d.ts |
| 新增API | NA | 类名：RingStyleOptions；  API声明：status?: ProgressStatus;  差异内容：status?: ProgressStatus; | component/progress.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface LinearStyleOptions  差异内容： declare interface LinearStyleOptions | component/progress.d.ts |
| 新增API | NA | 类名：LinearStyleOptions；  API声明：strokeWidth?: Length;  差异内容：strokeWidth?: Length; | component/progress.d.ts |
| 新增API | NA | 类名：LinearStyleOptions；  API声明：strokeRadius?: PX | VP | LPX | Resource;  差异内容：strokeRadius?: PX | VP | LPX | Resource; | component/progress.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface CapsuleStyleOptions  差异内容： declare interface CapsuleStyleOptions | component/progress.d.ts |
| 新增API | NA | 类名：CapsuleStyleOptions；  API声明：borderColor?: ResourceColor;  差异内容：borderColor?: ResourceColor; | component/progress.d.ts |
| 新增API | NA | 类名：CapsuleStyleOptions；  API声明：borderWidth?: Length;  差异内容：borderWidth?: Length; | component/progress.d.ts |
| 新增API | NA | 类名：CapsuleStyleOptions；  API声明：content?: string;  差异内容：content?: string; | component/progress.d.ts |
| 新增API | NA | 类名：CapsuleStyleOptions；  API声明：font?: Font;  差异内容：font?: Font; | component/progress.d.ts |
| 新增API | NA | 类名：CapsuleStyleOptions；  API声明：fontColor?: ResourceColor;  差异内容：fontColor?: ResourceColor; | component/progress.d.ts |
| 新增API | NA | 类名：CapsuleStyleOptions；  API声明：showDefaultPercentage?: boolean;  差异内容：showDefaultPercentage?: boolean; | component/progress.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface ProgressStyleMap  差异内容： declare interface ProgressStyleMap | component/progress.d.ts |
| 新增API | NA | 类名：ProgressStyleMap；  API声明：[ProgressType.Linear]: LinearStyleOptions | ProgressStyleOptions;  差异内容：[ProgressType.Linear]: LinearStyleOptions | ProgressStyleOptions; | component/progress.d.ts |
| 新增API | NA | 类名：ProgressStyleMap；  API声明：[ProgressType.Ring]: RingStyleOptions | ProgressStyleOptions;  差异内容：[ProgressType.Ring]: RingStyleOptions | ProgressStyleOptions; | component/progress.d.ts |
| 新增API | NA | 类名：ProgressStyleMap；  API声明：[ProgressType.Eclipse]: EclipseStyleOptions | ProgressStyleOptions;  差异内容：[ProgressType.Eclipse]: EclipseStyleOptions | ProgressStyleOptions; | component/progress.d.ts |
| 新增API | NA | 类名：ProgressStyleMap；  API声明：[ProgressType.ScaleRing]: ScaleRingStyleOptions | ProgressStyleOptions;  差异内容：[ProgressType.ScaleRing]: ScaleRingStyleOptions | ProgressStyleOptions; | component/progress.d.ts |
| 新增API | NA | 类名：ProgressStyleMap；  API声明：[ProgressType.Capsule]: CapsuleStyleOptions | ProgressStyleOptions;  差异内容：[ProgressType.Capsule]: CapsuleStyleOptions | ProgressStyleOptions; | component/progress.d.ts |
| 新增API | NA | 类名：ProgressAttribute；  API声明：contentModifier(modifier: ContentModifier<ProgressConfiguration>): ProgressAttribute<Type>;  差异内容：contentModifier(modifier: ContentModifier<ProgressConfiguration>): ProgressAttribute<Type>; | component/progress.d.ts |
| 新增API | NA | 类名：ProgressAttribute；  API声明：privacySensitive(isPrivacySensitiveMode: Optional<boolean>): ProgressAttribute<Type>;  差异内容：privacySensitive(isPrivacySensitiveMode: Optional<boolean>): ProgressAttribute<Type>; | component/progress.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface ProgressConfiguration  差异内容： declare interface ProgressConfiguration | component/progress.d.ts |
| 新增API | NA | 类名：ProgressConfiguration；  API声明：value: number;  差异内容：value: number; | component/progress.d.ts |
| 新增API | NA | 类名：ProgressConfiguration；  API声明：total: number;  差异内容：total: number; | component/progress.d.ts |
| 新增API | NA | 类名：QRCodeAttribute；  API声明：contentOpacity(value: number | Resource): QRCodeAttribute;  差异内容：contentOpacity(value: number | Resource): QRCodeAttribute; | component/qrcode.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum RadioIndicatorType  差异内容： declare enum RadioIndicatorType | component/radio.d.ts |
| 新增API | NA | 类名：RadioIndicatorType；  API声明：TICK = 0  差异内容：TICK = 0 | component/radio.d.ts |
| 新增API | NA | 类名：RadioIndicatorType；  API声明：DOT = 1  差异内容：DOT = 1 | component/radio.d.ts |
| 新增API | NA | 类名：RadioIndicatorType；  API声明：CUSTOM = 2  差异内容：CUSTOM = 2 | component/radio.d.ts |
| 新增API | NA | 类名：RadioOptions；  API声明：indicatorType?: RadioIndicatorType;  差异内容：indicatorType?: RadioIndicatorType; | component/radio.d.ts |
| 新增API | NA | 类名：RadioOptions；  API声明：indicatorBuilder?: CustomBuilder;  差异内容：indicatorBuilder?: CustomBuilder; | component/radio.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface RadioStyle  差异内容： declare interface RadioStyle | component/radio.d.ts |
| 新增API | NA | 类名：RadioStyle；  API声明：checkedBackgroundColor?: ResourceColor;  差异内容：checkedBackgroundColor?: ResourceColor; | component/radio.d.ts |
| 新增API | NA | 类名：RadioStyle；  API声明：uncheckedBorderColor?: ResourceColor;  差异内容：uncheckedBorderColor?: ResourceColor; | component/radio.d.ts |
| 新增API | NA | 类名：RadioStyle；  API声明：indicatorColor?: ResourceColor;  差异内容：indicatorColor?: ResourceColor; | component/radio.d.ts |
| 新增API | NA | 类名：RadioAttribute；  API声明：radioStyle(value?: RadioStyle): RadioAttribute;  差异内容：radioStyle(value?: RadioStyle): RadioAttribute; | component/radio.d.ts |
| 新增API | NA | 类名：RadioAttribute；  API声明：contentModifier(modifier: ContentModifier<RadioConfiguration>): RadioAttribute;  差异内容：contentModifier(modifier: ContentModifier<RadioConfiguration>): RadioAttribute; | component/radio.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface RadioConfiguration  差异内容： declare interface RadioConfiguration | component/radio.d.ts |
| 新增API | NA | 类名：RadioConfiguration；  API声明：value: string;  差异内容：value: string; | component/radio.d.ts |
| 新增API | NA | 类名：RadioConfiguration；  API声明：checked: boolean;  差异内容：checked: boolean; | component/radio.d.ts |
| 新增API | NA | 类名：RadioConfiguration；  API声明：triggerChange: Callback<boolean>;  差异内容：triggerChange: Callback<boolean>; | component/radio.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface RatingConfiguration  差异内容： declare interface RatingConfiguration | component/rating.d.ts |
| 新增API | NA | 类名：RatingConfiguration；  API声明：rating: number;  差异内容：rating: number; | component/rating.d.ts |
| 新增API | NA | 类名：RatingConfiguration；  API声明：indicator: boolean;  差异内容：indicator: boolean; | component/rating.d.ts |
| 新增API | NA | 类名：RatingConfiguration；  API声明：stars: number;  差异内容：stars: number; | component/rating.d.ts |
| 新增API | NA | 类名：RatingConfiguration；  API声明：stepSize: number;  差异内容：stepSize: number; | component/rating.d.ts |
| 新增API | NA | 类名：RatingConfiguration；  API声明：triggerChange: Callback<number>;  差异内容：triggerChange: Callback<number>; | component/rating.d.ts |
| 新增API | NA | 类名：RatingAttribute；  API声明：contentModifier(modifier: ContentModifier<RatingConfiguration>): RatingAttribute;  差异内容：contentModifier(modifier: ContentModifier<RatingConfiguration>): RatingAttribute; | component/rating.d.ts |
| 新增API | NA | 类名：global；  API声明： interface RefreshOptions  差异内容： interface RefreshOptions | component/refresh.d.ts |
| 新增API | NA | 类名：RefreshOptions；  API声明：refreshing: boolean;  差异内容：refreshing: boolean; | component/refresh.d.ts |
| 新增API | NA | 类名：RefreshOptions；  API声明：offset?: number | string;  差异内容：offset?: number | string; | component/refresh.d.ts |
| 新增API | NA | 类名：RefreshOptions；  API声明：friction?: number | string;  差异内容：friction?: number | string; | component/refresh.d.ts |
| 新增API | NA | 类名：RefreshOptions；  API声明：promptText?: ResourceStr;  差异内容：promptText?: ResourceStr; | component/refresh.d.ts |
| 新增API | NA | 类名：RefreshOptions；  API声明：builder?: CustomBuilder;  差异内容：builder?: CustomBuilder; | component/refresh.d.ts |
| 新增API | NA | 类名：RefreshAttribute；  API声明：refreshOffset(value: number): RefreshAttribute;  差异内容：refreshOffset(value: number): RefreshAttribute; | component/refresh.d.ts |
| 新增API | NA | 类名：RefreshAttribute；  API声明：pullToRefresh(value: boolean): RefreshAttribute;  差异内容：pullToRefresh(value: boolean): RefreshAttribute; | component/refresh.d.ts |
| 新增API | NA | 类名：RefreshAttribute；  API声明：onOffsetChange(callback: Callback<number>): RefreshAttribute;  差异内容：onOffsetChange(callback: Callback<number>): RefreshAttribute; | component/refresh.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface GuideLinePosition  差异内容： declare interface GuideLinePosition | component/relative\_container.d.ts |
| 新增API | NA | 类名：GuideLinePosition；  API声明：start?: Dimension;  差异内容：start?: Dimension; | component/relative\_container.d.ts |
| 新增API | NA | 类名：GuideLinePosition；  API声明：end?: Dimension;  差异内容：end?: Dimension; | component/relative\_container.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface GuideLineStyle  差异内容： declare interface GuideLineStyle | component/relative\_container.d.ts |
| 新增API | NA | 类名：GuideLineStyle；  API声明：id: string;  差异内容：id: string; | component/relative\_container.d.ts |
| 新增API | NA | 类名：GuideLineStyle；  API声明：direction: Axis;  差异内容：direction: Axis; | component/relative\_container.d.ts |
| 新增API | NA | 类名：GuideLineStyle；  API声明：position: GuideLinePosition;  差异内容：position: GuideLinePosition; | component/relative\_container.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum BarrierDirection  差异内容： declare enum BarrierDirection | component/relative\_container.d.ts |
| 新增API | NA | 类名：BarrierDirection；  API声明：LEFT  差异内容：LEFT | component/relative\_container.d.ts |
| 新增API | NA | 类名：BarrierDirection；  API声明：RIGHT  差异内容：RIGHT | component/relative\_container.d.ts |
| 新增API | NA | 类名：BarrierDirection；  API声明：TOP  差异内容：TOP | component/relative\_container.d.ts |
| 新增API | NA | 类名：BarrierDirection；  API声明：BOTTOM  差异内容：BOTTOM | component/relative\_container.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface BarrierStyle  差异内容： declare interface BarrierStyle | component/relative\_container.d.ts |
| 新增API | NA | 类名：BarrierStyle；  API声明：id: string;  差异内容：id: string; | component/relative\_container.d.ts |
| 新增API | NA | 类名：BarrierStyle；  API声明：direction: BarrierDirection;  差异内容：direction: BarrierDirection; | component/relative\_container.d.ts |
| 新增API | NA | 类名：BarrierStyle；  API声明：referencedId: Array<string>;  差异内容：referencedId: Array<string>; | component/relative\_container.d.ts |
| 新增API | NA | 类名：RelativeContainerAttribute；  API声明：guideLine(value: Array<GuideLineStyle>): RelativeContainerAttribute;  差异内容：guideLine(value: Array<GuideLineStyle>): RelativeContainerAttribute; | component/relative\_container.d.ts |
| 新增API | NA | 类名：RelativeContainerAttribute；  API声明：barrier(value: Array<BarrierStyle>): RelativeContainerAttribute;  差异内容：barrier(value: Array<BarrierStyle>): RelativeContainerAttribute; | component/relative\_container.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum ScrollAlign  差异内容： declare enum ScrollAlign | component/scroll.d.ts |
| 新增API | NA | 类名：ScrollAlign；  API声明：START  差异内容：START | component/scroll.d.ts |
| 新增API | NA | 类名：ScrollAlign；  API声明：CENTER  差异内容：CENTER | component/scroll.d.ts |
| 新增API | NA | 类名：ScrollAlign；  API声明：END  差异内容：END | component/scroll.d.ts |
| 新增API | NA | 类名：ScrollAlign；  API声明：AUTO  差异内容：AUTO | component/scroll.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface OffsetResult  差异内容： declare interface OffsetResult | component/scroll.d.ts |
| 新增API | NA | 类名：OffsetResult；  API声明：xOffset: number;  差异内容：xOffset: number; | component/scroll.d.ts |
| 新增API | NA | 类名：OffsetResult；  API声明：yOffset: number;  差异内容：yOffset: number; | component/scroll.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface ScrollEdgeOptions  差异内容： declare interface ScrollEdgeOptions | component/scroll.d.ts |
| 新增API | NA | 类名：ScrollEdgeOptions；  API声明：velocity?: number;  差异内容：velocity?: number; | component/scroll.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface ScrollToIndexOptions  差异内容： declare interface ScrollToIndexOptions | component/scroll.d.ts |
| 新增API | NA | 类名：ScrollToIndexOptions；  API声明：extraOffset?: LengthMetrics;  差异内容：extraOffset?: LengthMetrics; | component/scroll.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface ScrollAnimationOptions  差异内容： declare interface ScrollAnimationOptions | component/scroll.d.ts |
| 新增API | NA | 类名：ScrollAnimationOptions；  API声明：duration?: number;  差异内容：duration?: number; | component/scroll.d.ts |
| 新增API | NA | 类名：ScrollAnimationOptions；  API声明：curve?: Curve | ICurve;  差异内容：curve?: Curve | ICurve; | component/scroll.d.ts |
| 新增API | NA | 类名：ScrollAnimationOptions；  API声明：canOverScroll?: boolean;  差异内容：canOverScroll?: boolean; | component/scroll.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface OffsetOptions  差异内容： declare interface OffsetOptions | component/scroll.d.ts |
| 新增API | NA | 类名：OffsetOptions；  API声明：xOffset?: Dimension;  差异内容：xOffset?: Dimension; | component/scroll.d.ts |
| 新增API | NA | 类名：OffsetOptions；  API声明：yOffset?: Dimension;  差异内容：yOffset?: Dimension; | component/scroll.d.ts |
| 新增API | NA | 类名：Scroller；  API声明：fling(velocity: number): void;  差异内容：fling(velocity: number): void; | component/scroll.d.ts |
| 新增API | NA | 类名：Scroller；  API声明：isAtEnd(): boolean;  差异内容：isAtEnd(): boolean; | component/scroll.d.ts |
| 新增API | NA | 类名：Scroller；  API声明：getItemRect(index: number): RectResult;  差异内容：getItemRect(index: number): RectResult; | component/scroll.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface ScrollSnapOptions  差异内容： declare interface ScrollSnapOptions | component/scroll.d.ts |
| 新增API | NA | 类名：ScrollSnapOptions；  API声明：snapAlign: ScrollSnapAlign;  差异内容：snapAlign: ScrollSnapAlign; | component/scroll.d.ts |
| 新增API | NA | 类名：ScrollSnapOptions；  API声明：snapPagination?: Dimension | Array<Dimension>;  差异内容：snapPagination?: Dimension | Array<Dimension>; | component/scroll.d.ts |
| 新增API | NA | 类名：ScrollSnapOptions；  API声明：enableSnapToStart?: boolean;  差异内容：enableSnapToStart?: boolean; | component/scroll.d.ts |
| 新增API | NA | 类名：ScrollSnapOptions；  API声明：enableSnapToEnd?: boolean;  差异内容：enableSnapToEnd?: boolean; | component/scroll.d.ts |
| 新增API | NA | 类名：ScrollAttribute；  API声明：onWillScroll(handler: ScrollOnWillScrollCallback): ScrollAttribute;  差异内容：onWillScroll(handler: ScrollOnWillScrollCallback): ScrollAttribute; | component/scroll.d.ts |
| 新增API | NA | 类名：ScrollAttribute；  API声明：onDidScroll(handler: ScrollOnScrollCallback): ScrollAttribute;  差异内容：onDidScroll(handler: ScrollOnScrollCallback): ScrollAttribute; | component/scroll.d.ts |
| 新增API | NA | 类名：ScrollAttribute；  API声明：nestedScroll(value: NestedScrollOptions): ScrollAttribute;  差异内容：nestedScroll(value: NestedScrollOptions): ScrollAttribute; | component/scroll.d.ts |
| 新增API | NA | 类名：ScrollAttribute；  API声明：enableScrollInteraction(value: boolean): ScrollAttribute;  差异内容：enableScrollInteraction(value: boolean): ScrollAttribute; | component/scroll.d.ts |
| 新增API | NA | 类名：ScrollAttribute；  API声明：friction(value: number | Resource): ScrollAttribute;  差异内容：friction(value: number | Resource): ScrollAttribute; | component/scroll.d.ts |
| 新增API | NA | 类名：ScrollAttribute；  API声明：scrollSnap(value: ScrollSnapOptions): ScrollAttribute;  差异内容：scrollSnap(value: ScrollSnapOptions): ScrollAttribute; | component/scroll.d.ts |
| 新增API | NA | 类名：ScrollAttribute；  API声明：enablePaging(value: boolean): ScrollAttribute;  差异内容：enablePaging(value: boolean): ScrollAttribute; | component/scroll.d.ts |
| 新增API | NA | 类名：ScrollAttribute；  API声明：initialOffset(value: OffsetOptions): ScrollAttribute;  差异内容：initialOffset(value: OffsetOptions): ScrollAttribute; | component/scroll.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type ScrollOnScrollCallback = (xOffset: number, yOffset: number, scrollState: ScrollState) => void;  差异内容：declare type ScrollOnScrollCallback = (xOffset: number, yOffset: number, scrollState: ScrollState) => void; | component/scroll.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type ScrollOnWillScrollCallback = (xOffset: number, yOffset: number, scrollState: ScrollState, scrollSource: ScrollSource) => void | OffsetResult;  差异内容：declare type ScrollOnWillScrollCallback = (xOffset: number, yOffset: number, scrollState: ScrollState, scrollSource: ScrollSource) => void | OffsetResult; | component/scroll.d.ts |
| 新增API | NA | 类名：SearchController；  API声明：stopEditing(): void;  差异内容：stopEditing(): void; | component/search.d.ts |
| 新增API | NA | 类名：SearchController；  API声明：setTextSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void;  差异内容：setTextSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void; | component/search.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum CancelButtonStyle  差异内容： declare enum CancelButtonStyle | component/search.d.ts |
| 新增API | NA | 类名：CancelButtonStyle；  API声明：CONSTANT  差异内容：CONSTANT | component/search.d.ts |
| 新增API | NA | 类名：CancelButtonStyle；  API声明：INVISIBLE  差异内容：INVISIBLE | component/search.d.ts |
| 新增API | NA | 类名：CancelButtonStyle；  API声明：INPUT  差异内容：INPUT | component/search.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum SearchType  差异内容： declare enum SearchType | component/search.d.ts |
| 新增API | NA | 类名：SearchType；  API声明：NORMAL = 0  差异内容：NORMAL = 0 | component/search.d.ts |
| 新增API | NA | 类名：SearchType；  API声明：NUMBER = 2  差异内容：NUMBER = 2 | component/search.d.ts |
| 新增API | NA | 类名：SearchType；  API声明：PHONE\_NUMBER = 3  差异内容：PHONE\_NUMBER = 3 | component/search.d.ts |
| 新增API | NA | 类名：SearchType；  API声明：EMAIL = 5  差异内容：EMAIL = 5 | component/search.d.ts |
| 新增API | NA | 类名：SearchType；  API声明：NUMBER\_DECIMAL = 12  差异内容：NUMBER\_DECIMAL = 12 | component/search.d.ts |
| 新增API | NA | 类名：global；  API声明： interface IconOptions  差异内容： interface IconOptions | component/search.d.ts |
| 新增API | NA | 类名：IconOptions；  API声明：size?: Length;  差异内容：size?: Length; | component/search.d.ts |
| 新增API | NA | 类名：IconOptions；  API声明：color?: ResourceColor;  差异内容：color?: ResourceColor; | component/search.d.ts |
| 新增API | NA | 类名：IconOptions；  API声明：src?: ResourceStr;  差异内容：src?: ResourceStr; | component/search.d.ts |
| 新增API | NA | 类名：global；  API声明： interface SearchButtonOptions  差异内容： interface SearchButtonOptions | component/search.d.ts |
| 新增API | NA | 类名：SearchButtonOptions；  API声明：fontSize?: Length;  差异内容：fontSize?: Length; | component/search.d.ts |
| 新增API | NA | 类名：SearchButtonOptions；  API声明：fontColor?: ResourceColor;  差异内容：fontColor?: ResourceColor; | component/search.d.ts |
| 新增API | NA | 类名：SearchAttribute；  API声明：fontColor(value: ResourceColor): SearchAttribute;  差异内容：fontColor(value: ResourceColor): SearchAttribute; | component/search.d.ts |
| 新增API | NA | 类名：SearchAttribute；  API声明：searchIcon(value: IconOptions): SearchAttribute;  差异内容：searchIcon(value: IconOptions): SearchAttribute; | component/search.d.ts |
| 新增API | NA | 类名：SearchAttribute；  API声明：cancelButton(value: {  style?: CancelButtonStyle;  icon?: IconOptions;  }): SearchAttribute;  差异内容：cancelButton(value: {  style?: CancelButtonStyle;  icon?: IconOptions;  }): SearchAttribute; | component/search.d.ts |
| 新增API | NA | 类名：SearchAttribute；  API声明：textIndent(value: Dimension): SearchAttribute;  差异内容：textIndent(value: Dimension): SearchAttribute; | component/search.d.ts |
| 新增API | NA | 类名：SearchAttribute；  API声明：inputFilter(value: ResourceStr, error?: Callback<string>): SearchAttribute;  差异内容：inputFilter(value: ResourceStr, error?: Callback<string>): SearchAttribute; | component/search.d.ts |
| 新增API | NA | 类名：SearchAttribute；  API声明：onEditChange(callback: Callback<boolean>): SearchAttribute;  差异内容：onEditChange(callback: Callback<boolean>): SearchAttribute; | component/search.d.ts |
| 新增API | NA | 类名：SearchAttribute；  API声明：selectedBackgroundColor(value: ResourceColor): SearchAttribute;  差异内容：selectedBackgroundColor(value: ResourceColor): SearchAttribute; | component/search.d.ts |
| 新增API | NA | 类名：SearchAttribute；  API声明：caretStyle(value: CaretStyle): SearchAttribute;  差异内容：caretStyle(value: CaretStyle): SearchAttribute; | component/search.d.ts |
| 新增API | NA | 类名：SearchAttribute；  API声明：enterKeyType(value: EnterKeyType): SearchAttribute;  差异内容：enterKeyType(value: EnterKeyType): SearchAttribute; | component/search.d.ts |
| 新增API | NA | 类名：SearchAttribute；  API声明：onTextSelectionChange(callback: (selectionStart: number, selectionEnd: number) => void): SearchAttribute;  差异内容：onTextSelectionChange(callback: (selectionStart: number, selectionEnd: number) => void): SearchAttribute; | component/search.d.ts |
| 新增API | NA | 类名：SearchAttribute；  API声明：onContentScroll(callback: (totalOffsetX: number, totalOffsetY: number) => void): SearchAttribute;  差异内容：onContentScroll(callback: (totalOffsetX: number, totalOffsetY: number) => void): SearchAttribute; | component/search.d.ts |
| 新增API | NA | 类名：SearchAttribute；  API声明：maxLength(value: number): SearchAttribute;  差异内容：maxLength(value: number): SearchAttribute; | component/search.d.ts |
| 新增API | NA | 类名：SearchAttribute；  API声明：enableKeyboardOnFocus(value: boolean): SearchAttribute;  差异内容：enableKeyboardOnFocus(value: boolean): SearchAttribute; | component/search.d.ts |
| 新增API | NA | 类名：SearchAttribute；  API声明：selectionMenuHidden(value: boolean): SearchAttribute;  差异内容：selectionMenuHidden(value: boolean): SearchAttribute; | component/search.d.ts |
| 新增API | NA | 类名：SearchAttribute；  API声明：minFontSize(value: number | string | Resource): SearchAttribute;  差异内容：minFontSize(value: number | string | Resource): SearchAttribute; | component/search.d.ts |
| 新增API | NA | 类名：SearchAttribute；  API声明：maxFontSize(value: number | string | Resource): SearchAttribute;  差异内容：maxFontSize(value: number | string | Resource): SearchAttribute; | component/search.d.ts |
| 新增API | NA | 类名：SearchAttribute；  API声明：customKeyboard(value: CustomBuilder, options?: KeyboardOptions): SearchAttribute;  差异内容：customKeyboard(value: CustomBuilder, options?: KeyboardOptions): SearchAttribute; | component/search.d.ts |
| 新增API | NA | 类名：SearchAttribute；  API声明：decoration(value: TextDecorationOptions): SearchAttribute;  差异内容：decoration(value: TextDecorationOptions): SearchAttribute; | component/search.d.ts |
| 新增API | NA | 类名：SearchAttribute；  API声明：letterSpacing(value: number | string | Resource): SearchAttribute;  差异内容：letterSpacing(value: number | string | Resource): SearchAttribute; | component/search.d.ts |
| 新增API | NA | 类名：SearchAttribute；  API声明：lineHeight(value: number | string | Resource): SearchAttribute;  差异内容：lineHeight(value: number | string | Resource): SearchAttribute; | component/search.d.ts |
| 新增API | NA | 类名：SearchAttribute；  API声明：type(value: SearchType): SearchAttribute;  差异内容：type(value: SearchType): SearchAttribute; | component/search.d.ts |
| 新增API | NA | 类名：SearchAttribute；  API声明：fontFeature(value: string): SearchAttribute;  差异内容：fontFeature(value: string): SearchAttribute; | component/search.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum ArrowPosition  差异内容： declare enum ArrowPosition | component/select.d.ts |
| 新增API | NA | 类名：ArrowPosition；  API声明：END = 0  差异内容：END = 0 | component/select.d.ts |
| 新增API | NA | 类名：ArrowPosition；  API声明：START = 1  差异内容：START = 1 | component/select.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum MenuAlignType  差异内容： declare enum MenuAlignType | component/select.d.ts |
| 新增API | NA | 类名：MenuAlignType；  API声明：START  差异内容：START | component/select.d.ts |
| 新增API | NA | 类名：MenuAlignType；  API声明：CENTER  差异内容：CENTER | component/select.d.ts |
| 新增API | NA | 类名：MenuAlignType；  API声明：END  差异内容：END | component/select.d.ts |
| 新增API | NA | 类名：SelectAttribute；  API声明：space(value: Length): SelectAttribute;  差异内容：space(value: Length): SelectAttribute; | component/select.d.ts |
| 新增API | NA | 类名：SelectAttribute；  API声明：arrowPosition(value: ArrowPosition): SelectAttribute;  差异内容：arrowPosition(value: ArrowPosition): SelectAttribute; | component/select.d.ts |
| 新增API | NA | 类名：SelectAttribute；  API声明：menuAlign(alignType: MenuAlignType, offset?: Offset): SelectAttribute;  差异内容：menuAlign(alignType: MenuAlignType, offset?: Offset): SelectAttribute; | component/select.d.ts |
| 新增API | NA | 类名：SelectAttribute；  API声明：optionWidth(value: Dimension | OptionWidthMode): SelectAttribute;  差异内容：optionWidth(value: Dimension | OptionWidthMode): SelectAttribute; | component/select.d.ts |
| 新增API | NA | 类名：SelectAttribute；  API声明：optionHeight(value: Dimension): SelectAttribute;  差异内容：optionHeight(value: Dimension): SelectAttribute; | component/select.d.ts |
| 新增API | NA | 类名：SelectAttribute；  API声明：menuBackgroundColor(value: ResourceColor): SelectAttribute;  差异内容：menuBackgroundColor(value: ResourceColor): SelectAttribute; | component/select.d.ts |
| 新增API | NA | 类名：SelectAttribute；  API声明：menuBackgroundBlurStyle(value: BlurStyle): SelectAttribute;  差异内容：menuBackgroundBlurStyle(value: BlurStyle): SelectAttribute; | component/select.d.ts |
| 新增API | NA | 类名：SelectAttribute；  API声明：controlSize(value: ControlSize): SelectAttribute;  差异内容：controlSize(value: ControlSize): SelectAttribute; | component/select.d.ts |
| 新增API | NA | 类名：SelectAttribute；  API声明：menuItemContentModifier(modifier: ContentModifier<MenuItemConfiguration>): SelectAttribute;  差异内容：menuItemContentModifier(modifier: ContentModifier<MenuItemConfiguration>): SelectAttribute; | component/select.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface MenuItemConfiguration  差异内容： declare interface MenuItemConfiguration | component/select.d.ts |
| 新增API | NA | 类名：MenuItemConfiguration；  API声明：value: ResourceStr;  差异内容：value: ResourceStr; | component/select.d.ts |
| 新增API | NA | 类名：MenuItemConfiguration；  API声明：icon?: ResourceStr;  差异内容：icon?: ResourceStr; | component/select.d.ts |
| 新增API | NA | 类名：MenuItemConfiguration；  API声明：selected: boolean;  差异内容：selected: boolean; | component/select.d.ts |
| 新增API | NA | 类名：MenuItemConfiguration；  API声明：index: number;  差异内容：index: number; | component/select.d.ts |
| 新增API | NA | 类名：MenuItemConfiguration；  API声明：triggerSelect(index: number, value: string): void;  差异内容：triggerSelect(index: number, value: string): void; | component/select.d.ts |
| 新增API | NA | 类名：SideBarContainerType；  API声明：AUTO  差异内容：AUTO | component/sidebar.d.ts |
| 新增API | NA | 类名：global；  API声明： interface DividerStyle  差异内容： interface DividerStyle | component/sidebar.d.ts |
| 新增API | NA | 类名：DividerStyle；  API声明：strokeWidth: Length;  差异内容：strokeWidth: Length; | component/sidebar.d.ts |
| 新增API | NA | 类名：DividerStyle；  API声明：color?: ResourceColor;  差异内容：color?: ResourceColor; | component/sidebar.d.ts |
| 新增API | NA | 类名：DividerStyle；  API声明：startMargin?: Length;  差异内容：startMargin?: Length; | component/sidebar.d.ts |
| 新增API | NA | 类名：DividerStyle；  API声明：endMargin?: Length;  差异内容：endMargin?: Length; | component/sidebar.d.ts |
| 新增API | NA | 类名：SideBarContainerAttribute；  API声明：divider(value: DividerStyle | null): SideBarContainerAttribute;  差异内容：divider(value: DividerStyle | null): SideBarContainerAttribute; | component/sidebar.d.ts |
| 新增API | NA | 类名：SideBarContainerAttribute；  API声明：minContentWidth(value: Dimension): SideBarContainerAttribute;  差异内容：minContentWidth(value: Dimension): SideBarContainerAttribute; | component/sidebar.d.ts |
| 新增API | NA | 类名：SliderStyle；  API声明：NONE  差异内容：NONE | component/slider.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum SliderInteraction  差异内容： declare enum SliderInteraction | component/slider.d.ts |
| 新增API | NA | 类名：SliderInteraction；  API声明：SLIDE\_AND\_CLICK  差异内容：SLIDE\_AND\_CLICK | component/slider.d.ts |
| 新增API | NA | 类名：SliderInteraction；  API声明：SLIDE\_ONLY  差异内容：SLIDE\_ONLY | component/slider.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface SlideRange  差异内容： declare interface SlideRange | component/slider.d.ts |
| 新增API | NA | 类名：SlideRange；  API声明：from?: number;  差异内容：from?: number; | component/slider.d.ts |
| 新增API | NA | 类名：SlideRange；  API声明：to?: number;  差异内容：to?: number; | component/slider.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum SliderBlockType  差异内容： declare enum SliderBlockType | component/slider.d.ts |
| 新增API | NA | 类名：SliderBlockType；  API声明：DEFAULT  差异内容：DEFAULT | component/slider.d.ts |
| 新增API | NA | 类名：SliderBlockType；  API声明：IMAGE  差异内容：IMAGE | component/slider.d.ts |
| 新增API | NA | 类名：SliderBlockType；  API声明：SHAPE  差异内容：SHAPE | component/slider.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface SliderBlockStyle  差异内容： declare interface SliderBlockStyle | component/slider.d.ts |
| 新增API | NA | 类名：SliderBlockStyle；  API声明：type: SliderBlockType;  差异内容：type: SliderBlockType; | component/slider.d.ts |
| 新增API | NA | 类名：SliderBlockStyle；  API声明：image?: ResourceStr;  差异内容：image?: ResourceStr; | component/slider.d.ts |
| 新增API | NA | 类名：SliderBlockStyle；  API声明：shape?: CircleAttribute | EllipseAttribute | PathAttribute | RectAttribute;  差异内容：shape?: CircleAttribute | EllipseAttribute | PathAttribute | RectAttribute; | component/slider.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type SliderTriggerChangeCallback = (value: number, mode: SliderChangeMode) => void;  差异内容：declare type SliderTriggerChangeCallback = (value: number, mode: SliderChangeMode) => void; | component/slider.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface SliderConfiguration  差异内容： declare interface SliderConfiguration | component/slider.d.ts |
| 新增API | NA | 类名：SliderConfiguration；  API声明：value: number;  差异内容：value: number; | component/slider.d.ts |
| 新增API | NA | 类名：SliderConfiguration；  API声明：min: number;  差异内容：min: number; | component/slider.d.ts |
| 新增API | NA | 类名：SliderConfiguration；  API声明：max: number;  差异内容：max: number; | component/slider.d.ts |
| 新增API | NA | 类名：SliderConfiguration；  API声明：step: number;  差异内容：step: number; | component/slider.d.ts |
| 新增API | NA | 类名：SliderConfiguration；  API声明：triggerChange: SliderTriggerChangeCallback;  差异内容：triggerChange: SliderTriggerChangeCallback; | component/slider.d.ts |
| 新增API | NA | 类名：SliderAttribute；  API声明：blockBorderColor(value: ResourceColor): SliderAttribute;  差异内容：blockBorderColor(value: ResourceColor): SliderAttribute; | component/slider.d.ts |
| 新增API | NA | 类名：SliderAttribute；  API声明：blockBorderWidth(value: Length): SliderAttribute;  差异内容：blockBorderWidth(value: Length): SliderAttribute; | component/slider.d.ts |
| 新增API | NA | 类名：SliderAttribute；  API声明：stepColor(value: ResourceColor): SliderAttribute;  差异内容：stepColor(value: ResourceColor): SliderAttribute; | component/slider.d.ts |
| 新增API | NA | 类名：SliderAttribute；  API声明：trackBorderRadius(value: Length): SliderAttribute;  差异内容：trackBorderRadius(value: Length): SliderAttribute; | component/slider.d.ts |
| 新增API | NA | 类名：SliderAttribute；  API声明：selectedBorderRadius(value: Dimension): SliderAttribute;  差异内容：selectedBorderRadius(value: Dimension): SliderAttribute; | component/slider.d.ts |
| 新增API | NA | 类名：SliderAttribute；  API声明：blockSize(value: SizeOptions): SliderAttribute;  差异内容：blockSize(value: SizeOptions): SliderAttribute; | component/slider.d.ts |
| 新增API | NA | 类名：SliderAttribute；  API声明：blockStyle(value: SliderBlockStyle): SliderAttribute;  差异内容：blockStyle(value: SliderBlockStyle): SliderAttribute; | component/slider.d.ts |
| 新增API | NA | 类名：SliderAttribute；  API声明：stepSize(value: Length): SliderAttribute;  差异内容：stepSize(value: Length): SliderAttribute; | component/slider.d.ts |
| 新增API | NA | 类名：SliderAttribute；  API声明：sliderInteractionMode(value: SliderInteraction): SliderAttribute;  差异内容：sliderInteractionMode(value: SliderInteraction): SliderAttribute; | component/slider.d.ts |
| 新增API | NA | 类名：SliderAttribute；  API声明：minResponsiveDistance(value: number): SliderAttribute;  差异内容：minResponsiveDistance(value: number): SliderAttribute; | component/slider.d.ts |
| 新增API | NA | 类名：SliderAttribute；  API声明：contentModifier(modifier: ContentModifier<SliderConfiguration>): SliderAttribute;  差异内容：contentModifier(modifier: ContentModifier<SliderConfiguration>): SliderAttribute; | component/slider.d.ts |
| 新增API | NA | 类名：SliderAttribute；  API声明：slideRange(value: SlideRange): SliderAttribute;  差异内容：slideRange(value: SlideRange): SliderAttribute; | component/slider.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface TextBackgroundStyle  差异内容： declare interface TextBackgroundStyle | component/span.d.ts |
| 新增API | NA | 类名：TextBackgroundStyle；  API声明：color?: ResourceColor;  差异内容：color?: ResourceColor; | component/span.d.ts |
| 新增API | NA | 类名：TextBackgroundStyle；  API声明：radius?: Dimension | BorderRadiuses;  差异内容：radius?: Dimension | BorderRadiuses; | component/span.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class BaseSpan  差异内容： declare class BaseSpan | component/span.d.ts |
| 新增API | NA | 类名：BaseSpan；  API声明：textBackgroundStyle(style: TextBackgroundStyle): T;  差异内容：textBackgroundStyle(style: TextBackgroundStyle): T; | component/span.d.ts |
| 新增API | NA | 类名：BaseSpan；  API声明：baselineOffset(value: LengthMetrics): T;  差异内容：baselineOffset(value: LengthMetrics): T; | component/span.d.ts |
| 新增API | NA | 类名：SpanAttribute；  API声明：font(value: Font): SpanAttribute;  差异内容：font(value: Font): SpanAttribute; | component/span.d.ts |
| 新增API | NA | 类名：SpanAttribute；  API声明：lineHeight(value: Length): SpanAttribute;  差异内容：lineHeight(value: Length): SpanAttribute; | component/span.d.ts |
| 新增API | NA | 类名：SpanAttribute；  API声明：textShadow(value: ShadowOptions | Array<ShadowOptions>): SpanAttribute;  差异内容：textShadow(value: ShadowOptions | Array<ShadowOptions>): SpanAttribute; | component/span.d.ts |
| 新增API | NA | 类名：SwiperController；  API声明：changeIndex(index: number, useAnimation?: boolean);  差异内容：changeIndex(index: number, useAnimation?: boolean); | component/swiper.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class Indicator  差异内容： declare class Indicator | component/swiper.d.ts |
| 新增API | NA | 类名：Indicator；  API声明：left(value: Length): T;  差异内容：left(value: Length): T; | component/swiper.d.ts |
| 新增API | NA | 类名：Indicator；  API声明：top(value: Length): T;  差异内容：top(value: Length): T; | component/swiper.d.ts |
| 新增API | NA | 类名：Indicator；  API声明：right(value: Length): T;  差异内容：right(value: Length): T; | component/swiper.d.ts |
| 新增API | NA | 类名：Indicator；  API声明：bottom(value: Length): T;  差异内容：bottom(value: Length): T; | component/swiper.d.ts |
| 新增API | NA | 类名：Indicator；  API声明：static dot(): DotIndicator;  差异内容：static dot(): DotIndicator; | component/swiper.d.ts |
| 新增API | NA | 类名：Indicator；  API声明：static digit(): DigitIndicator;  差异内容：static digit(): DigitIndicator; | component/swiper.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class DotIndicator  差异内容： declare class DotIndicator | component/swiper.d.ts |
| 新增API | NA | 类名：DotIndicator；  API声明：itemWidth(value: Length): DotIndicator;  差异内容：itemWidth(value: Length): DotIndicator; | component/swiper.d.ts |
| 新增API | NA | 类名：DotIndicator；  API声明：itemHeight(value: Length): DotIndicator;  差异内容：itemHeight(value: Length): DotIndicator; | component/swiper.d.ts |
| 新增API | NA | 类名：DotIndicator；  API声明：selectedItemWidth(value: Length): DotIndicator;  差异内容：selectedItemWidth(value: Length): DotIndicator; | component/swiper.d.ts |
| 新增API | NA | 类名：DotIndicator；  API声明：selectedItemHeight(value: Length): DotIndicator;  差异内容：selectedItemHeight(value: Length): DotIndicator; | component/swiper.d.ts |
| 新增API | NA | 类名：DotIndicator；  API声明：mask(value: boolean): DotIndicator;  差异内容：mask(value: boolean): DotIndicator; | component/swiper.d.ts |
| 新增API | NA | 类名：DotIndicator；  API声明：color(value: ResourceColor): DotIndicator;  差异内容：color(value: ResourceColor): DotIndicator; | component/swiper.d.ts |
| 新增API | NA | 类名：DotIndicator；  API声明：selectedColor(value: ResourceColor): DotIndicator;  差异内容：selectedColor(value: ResourceColor): DotIndicator; | component/swiper.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type SwiperAutoFill = {  /\*\*  \* Set minSize size.  \*  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @since 10  \* @form  \*/  /\*\*  \* Set minSize size.  \*  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @atomicservice  \* @since 11  \* @form  \*/  minSize: VP;  };  差异内容：declare type SwiperAutoFill = {  /\*\*  \* Set minSize size.  \*  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @since 10  \* @form  \*/  /\*\*  \* Set minSize size.  \*  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @atomicservice  \* @since 11  \* @form  \*/  minSize: VP;  }; | component/swiper.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class DigitIndicator  差异内容： declare class DigitIndicator | component/swiper.d.ts |
| 新增API | NA | 类名：DigitIndicator；  API声明：fontColor(value: ResourceColor): DigitIndicator;  差异内容：fontColor(value: ResourceColor): DigitIndicator; | component/swiper.d.ts |
| 新增API | NA | 类名：DigitIndicator；  API声明：selectedFontColor(value: ResourceColor): DigitIndicator;  差异内容：selectedFontColor(value: ResourceColor): DigitIndicator; | component/swiper.d.ts |
| 新增API | NA | 类名：DigitIndicator；  API声明：digitFont(value: Font): DigitIndicator;  差异内容：digitFont(value: Font): DigitIndicator; | component/swiper.d.ts |
| 新增API | NA | 类名：DigitIndicator；  API声明：selectedDigitFont(value: Font): DigitIndicator;  差异内容：selectedDigitFont(value: Font): DigitIndicator; | component/swiper.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface ArrowStyle  差异内容： declare interface ArrowStyle | component/swiper.d.ts |
| 新增API | NA | 类名：ArrowStyle；  API声明：showBackground?: boolean;  差异内容：showBackground?: boolean; | component/swiper.d.ts |
| 新增API | NA | 类名：ArrowStyle；  API声明：isSidebarMiddle?: boolean;  差异内容：isSidebarMiddle?: boolean; | component/swiper.d.ts |
| 新增API | NA | 类名：ArrowStyle；  API声明：backgroundSize?: Length;  差异内容：backgroundSize?: Length; | component/swiper.d.ts |
| 新增API | NA | 类名：ArrowStyle；  API声明：backgroundColor?: ResourceColor;  差异内容：backgroundColor?: ResourceColor; | component/swiper.d.ts |
| 新增API | NA | 类名：ArrowStyle；  API声明：arrowSize?: Length;  差异内容：arrowSize?: Length; | component/swiper.d.ts |
| 新增API | NA | 类名：ArrowStyle；  API声明：arrowColor?: ResourceColor;  差异内容：arrowColor?: ResourceColor; | component/swiper.d.ts |
| 新增API | NA | 类名：SwiperDisplayMode；  API声明：STRETCH  差异内容：STRETCH | component/swiper.d.ts |
| 新增API | NA | 类名：SwiperDisplayMode；  API声明：AUTO\_LINEAR  差异内容：AUTO\_LINEAR | component/swiper.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface SwiperAnimationEvent  差异内容： declare interface SwiperAnimationEvent | component/swiper.d.ts |
| 新增API | NA | 类名：SwiperAnimationEvent；  API声明：currentOffset: number;  差异内容：currentOffset: number; | component/swiper.d.ts |
| 新增API | NA | 类名：SwiperAnimationEvent；  API声明：targetOffset: number;  差异内容：targetOffset: number; | component/swiper.d.ts |
| 新增API | NA | 类名：SwiperAnimationEvent；  API声明：velocity: number;  差异内容：velocity: number; | component/swiper.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum SwiperNestedScrollMode  差异内容： declare enum SwiperNestedScrollMode | component/swiper.d.ts |
| 新增API | NA | 类名：SwiperNestedScrollMode；  API声明：SELF\_ONLY = 0  差异内容：SELF\_ONLY = 0 | component/swiper.d.ts |
| 新增API | NA | 类名：SwiperNestedScrollMode；  API声明：SELF\_FIRST = 1  差异内容：SELF\_FIRST = 1 | component/swiper.d.ts |
| 新增API | NA | 类名：SwiperAttribute；  API声明：displayArrow(value: ArrowStyle | boolean, isHoverShow?: boolean): SwiperAttribute;  差异内容：displayArrow(value: ArrowStyle | boolean, isHoverShow?: boolean): SwiperAttribute; | component/swiper.d.ts |
| 新增API | NA | 类名：SwiperAttribute；  API声明：prevMargin(value: Length): SwiperAttribute;  差异内容：prevMargin(value: Length): SwiperAttribute; | component/swiper.d.ts |
| 新增API | NA | 类名：SwiperAttribute；  API声明：nextMargin(value: Length): SwiperAttribute;  差异内容：nextMargin(value: Length): SwiperAttribute; | component/swiper.d.ts |
| 新增API | NA | 类名：SwiperAttribute；  API声明：onGestureSwipe(event: (index: number, extraInfo: SwiperAnimationEvent) => void): SwiperAttribute;  差异内容：onGestureSwipe(event: (index: number, extraInfo: SwiperAnimationEvent) => void): SwiperAttribute; | component/swiper.d.ts |
| 新增API | NA | 类名：SwiperAttribute；  API声明：nestedScroll(value: SwiperNestedScrollMode): SwiperAttribute;  差异内容：nestedScroll(value: SwiperNestedScrollMode): SwiperAttribute; | component/swiper.d.ts |
| 新增API | NA | 类名：SwiperAttribute；  API声明：customContentTransition(transition: SwiperContentAnimatedTransition): SwiperAttribute;  差异内容：customContentTransition(transition: SwiperContentAnimatedTransition): SwiperAttribute; | component/swiper.d.ts |
| 新增API | NA | 类名：SwiperAttribute；  API声明：onContentDidScroll(handler: ContentDidScrollCallback): SwiperAttribute;  差异内容：onContentDidScroll(handler: ContentDidScrollCallback): SwiperAttribute; | component/swiper.d.ts |
| 新增API | NA | 类名：SwiperAttribute；  API声明：indicatorInteractive(value: boolean): SwiperAttribute;  差异内容：indicatorInteractive(value: boolean): SwiperAttribute; | component/swiper.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface SwiperContentAnimatedTransition  差异内容： declare interface SwiperContentAnimatedTransition | component/swiper.d.ts |
| 新增API | NA | 类名：SwiperContentAnimatedTransition；  API声明：timeout?: number;  差异内容：timeout?: number; | component/swiper.d.ts |
| 新增API | NA | 类名：SwiperContentAnimatedTransition；  API声明：transition: Callback<SwiperContentTransitionProxy>;  差异内容：transition: Callback<SwiperContentTransitionProxy>; | component/swiper.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface SwiperContentTransitionProxy  差异内容： declare interface SwiperContentTransitionProxy | component/swiper.d.ts |
| 新增API | NA | 类名：SwiperContentTransitionProxy；  API声明：selectedIndex: number;  差异内容：selectedIndex: number; | component/swiper.d.ts |
| 新增API | NA | 类名：SwiperContentTransitionProxy；  API声明：index: number;  差异内容：index: number; | component/swiper.d.ts |
| 新增API | NA | 类名：SwiperContentTransitionProxy；  API声明：position: number;  差异内容：position: number; | component/swiper.d.ts |
| 新增API | NA | 类名：SwiperContentTransitionProxy；  API声明：mainAxisLength: number;  差异内容：mainAxisLength: number; | component/swiper.d.ts |
| 新增API | NA | 类名：SwiperContentTransitionProxy；  API声明：finishTransition(): void;  差异内容：finishTransition(): void; | component/swiper.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type ContentDidScrollCallback = (selectedIndex: number, index: number, position: number, mainAxisLength: number) => void;  差异内容：declare type ContentDidScrollCallback = (selectedIndex: number, index: number, position: number, mainAxisLength: number) => void; | component/swiper.d.ts |
| 新增API | NA | 类名：TabsAttribute；  API声明：barMode(value: BarMode.Fixed): TabsAttribute;  差异内容：barMode(value: BarMode.Fixed): TabsAttribute; | component/tabs.d.ts |
| 新增API | NA | 类名：TabsAttribute；  API声明：barMode(value: BarMode.Scrollable, options: ScrollableBarModeOptions): TabsAttribute;  差异内容：barMode(value: BarMode.Scrollable, options: ScrollableBarModeOptions): TabsAttribute; | component/tabs.d.ts |
| 新增API | NA | 类名：TabsAttribute；  API声明：barMode(value: BarMode, options?: ScrollableBarModeOptions): TabsAttribute;  差异内容：barMode(value: BarMode, options?: ScrollableBarModeOptions): TabsAttribute; | component/tabs.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum AnimationMode  差异内容： declare enum AnimationMode | component/tabs.d.ts |
| 新增API | NA | 类名：AnimationMode；  API声明：CONTENT\_FIRST = 0  差异内容：CONTENT\_FIRST = 0 | component/tabs.d.ts |
| 新增API | NA | 类名：AnimationMode；  API声明：ACTION\_FIRST = 1  差异内容：ACTION\_FIRST = 1 | component/tabs.d.ts |
| 新增API | NA | 类名：AnimationMode；  API声明：NO\_ANIMATION = 2  差异内容：NO\_ANIMATION = 2 | component/tabs.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum LayoutStyle  差异内容： declare enum LayoutStyle | component/tabs.d.ts |
| 新增API | NA | 类名：LayoutStyle；  API声明：ALWAYS\_CENTER = 0  差异内容：ALWAYS\_CENTER = 0 | component/tabs.d.ts |
| 新增API | NA | 类名：LayoutStyle；  API声明：ALWAYS\_AVERAGE\_SPLIT = 1  差异内容：ALWAYS\_AVERAGE\_SPLIT = 1 | component/tabs.d.ts |
| 新增API | NA | 类名：LayoutStyle；  API声明：SPACE\_BETWEEN\_OR\_CENTER = 2  差异内容：SPACE\_BETWEEN\_OR\_CENTER = 2 | component/tabs.d.ts |
| 新增API | NA | 类名：global；  API声明： interface DividerStyle  差异内容： interface DividerStyle | component/tabs.d.ts |
| 新增API | NA | 类名：DividerStyle；  API声明：strokeWidth: Length;  差异内容：strokeWidth: Length; | component/tabs.d.ts |
| 新增API | NA | 类名：DividerStyle；  API声明：color?: ResourceColor;  差异内容：color?: ResourceColor; | component/tabs.d.ts |
| 新增API | NA | 类名：DividerStyle；  API声明：startMargin?: Length;  差异内容：startMargin?: Length; | component/tabs.d.ts |
| 新增API | NA | 类名：DividerStyle；  API声明：endMargin?: Length;  差异内容：endMargin?: Length; | component/tabs.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface TabsAnimationEvent  差异内容： declare interface TabsAnimationEvent | component/tabs.d.ts |
| 新增API | NA | 类名：TabsAnimationEvent；  API声明：currentOffset: number;  差异内容：currentOffset: number; | component/tabs.d.ts |
| 新增API | NA | 类名：TabsAnimationEvent；  API声明：targetOffset: number;  差异内容：targetOffset: number; | component/tabs.d.ts |
| 新增API | NA | 类名：TabsAnimationEvent；  API声明：velocity: number;  差异内容：velocity: number; | component/tabs.d.ts |
| 新增API | NA | 类名：global；  API声明： interface BarGridColumnOptions  差异内容： interface BarGridColumnOptions | component/tabs.d.ts |
| 新增API | NA | 类名：BarGridColumnOptions；  API声明：sm?: number;  差异内容：sm?: number; | component/tabs.d.ts |
| 新增API | NA | 类名：BarGridColumnOptions；  API声明：md?: number;  差异内容：md?: number; | component/tabs.d.ts |
| 新增API | NA | 类名：BarGridColumnOptions；  API声明：lg?: number;  差异内容：lg?: number; | component/tabs.d.ts |
| 新增API | NA | 类名：BarGridColumnOptions；  API声明：margin?: Dimension;  差异内容：margin?: Dimension; | component/tabs.d.ts |
| 新增API | NA | 类名：BarGridColumnOptions；  API声明：gutter?: Dimension;  差异内容：gutter?: Dimension; | component/tabs.d.ts |
| 新增API | NA | 类名：global；  API声明： interface ScrollableBarModeOptions  差异内容： interface ScrollableBarModeOptions | component/tabs.d.ts |
| 新增API | NA | 类名：ScrollableBarModeOptions；  API声明：margin?: Dimension;  差异内容：margin?: Dimension; | component/tabs.d.ts |
| 新增API | NA | 类名：ScrollableBarModeOptions；  API声明：nonScrollableLayoutStyle?: LayoutStyle;  差异内容：nonScrollableLayoutStyle?: LayoutStyle; | component/tabs.d.ts |
| 新增API | NA | 类名：TabsAttribute；  API声明：animationMode(mode: Optional<AnimationMode>): TabsAttribute;  差异内容：animationMode(mode: Optional<AnimationMode>): TabsAttribute; | component/tabs.d.ts |
| 新增API | NA | 类名：TabsAttribute；  API声明：onTabBarClick(event: (index: number) => void): TabsAttribute;  差异内容：onTabBarClick(event: (index: number) => void): TabsAttribute; | component/tabs.d.ts |
| 新增API | NA | 类名：TabsAttribute；  API声明：onAnimationStart(handler: (index: number, targetIndex: number, event: TabsAnimationEvent) => void): TabsAttribute;  差异内容：onAnimationStart(handler: (index: number, targetIndex: number, event: TabsAnimationEvent) => void): TabsAttribute; | component/tabs.d.ts |
| 新增API | NA | 类名：TabsAttribute；  API声明：onAnimationEnd(handler: (index: number, event: TabsAnimationEvent) => void): TabsAttribute;  差异内容：onAnimationEnd(handler: (index: number, event: TabsAnimationEvent) => void): TabsAttribute; | component/tabs.d.ts |
| 新增API | NA | 类名：TabsAttribute；  API声明：onGestureSwipe(handler: (index: number, event: TabsAnimationEvent) => void): TabsAttribute;  差异内容：onGestureSwipe(handler: (index: number, event: TabsAnimationEvent) => void): TabsAttribute; | component/tabs.d.ts |
| 新增API | NA | 类名：TabsAttribute；  API声明：fadingEdge(value: boolean): TabsAttribute;  差异内容：fadingEdge(value: boolean): TabsAttribute; | component/tabs.d.ts |
| 新增API | NA | 类名：TabsAttribute；  API声明：divider(value: DividerStyle | null): TabsAttribute;  差异内容：divider(value: DividerStyle | null): TabsAttribute; | component/tabs.d.ts |
| 新增API | NA | 类名：TabsAttribute；  API声明：barOverlap(value: boolean): TabsAttribute;  差异内容：barOverlap(value: boolean): TabsAttribute; | component/tabs.d.ts |
| 新增API | NA | 类名：TabsAttribute；  API声明：barBackgroundColor(value: ResourceColor): TabsAttribute;  差异内容：barBackgroundColor(value: ResourceColor): TabsAttribute; | component/tabs.d.ts |
| 新增API | NA | 类名：TabsAttribute；  API声明：barGridAlign(value: BarGridColumnOptions): TabsAttribute;  差异内容：barGridAlign(value: BarGridColumnOptions): TabsAttribute; | component/tabs.d.ts |
| 新增API | NA | 类名：TabsAttribute；  API声明：customContentTransition(delegate: (from: number, to: number) => TabContentAnimatedTransition | undefined): TabsAttribute;  差异内容：customContentTransition(delegate: (from: number, to: number) => TabContentAnimatedTransition | undefined): TabsAttribute; | component/tabs.d.ts |
| 新增API | NA | 类名：TabsAttribute；  API声明：barBackgroundBlurStyle(value: BlurStyle): TabsAttribute;  差异内容：barBackgroundBlurStyle(value: BlurStyle): TabsAttribute; | component/tabs.d.ts |
| 新增API | NA | 类名：TabsAttribute；  API声明：onContentWillChange(handler: (currentIndex: number, comingIndex: number) => boolean): TabsAttribute;  差异内容：onContentWillChange(handler: (currentIndex: number, comingIndex: number) => boolean): TabsAttribute; | component/tabs.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface TabContentAnimatedTransition  差异内容： declare interface TabContentAnimatedTransition | component/tabs.d.ts |
| 新增API | NA | 类名：TabContentAnimatedTransition；  API声明：timeout?: number;  差异内容：timeout?: number; | component/tabs.d.ts |
| 新增API | NA | 类名：TabContentAnimatedTransition；  API声明：transition: (proxy: TabContentTransitionProxy) => void;  差异内容：transition: (proxy: TabContentTransitionProxy) => void; | component/tabs.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface TabContentTransitionProxy  差异内容： declare interface TabContentTransitionProxy | component/tabs.d.ts |
| 新增API | NA | 类名：TabContentTransitionProxy；  API声明：from: number;  差异内容：from: number; | component/tabs.d.ts |
| 新增API | NA | 类名：TabContentTransitionProxy；  API声明：to: number;  差异内容：to: number; | component/tabs.d.ts |
| 新增API | NA | 类名：TabContentTransitionProxy；  API声明：finishTransition(): void;  差异内容：finishTransition(): void; | component/tabs.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum SelectedMode  差异内容： declare enum SelectedMode | component/tab\_content.d.ts |
| 新增API | NA | 类名：SelectedMode；  API声明：INDICATOR  差异内容：INDICATOR | component/tab\_content.d.ts |
| 新增API | NA | 类名：SelectedMode；  API声明：BOARD  差异内容：BOARD | component/tab\_content.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum LayoutMode  差异内容： declare enum LayoutMode | component/tab\_content.d.ts |
| 新增API | NA | 类名：LayoutMode；  API声明：AUTO = 0  差异内容：AUTO = 0 | component/tab\_content.d.ts |
| 新增API | NA | 类名：LayoutMode；  API声明：VERTICAL = 1  差异内容：VERTICAL = 1 | component/tab\_content.d.ts |
| 新增API | NA | 类名：LayoutMode；  API声明：HORIZONTAL = 2  差异内容：HORIZONTAL = 2 | component/tab\_content.d.ts |
| 新增API | NA | 类名：global；  API声明： interface IndicatorStyle  差异内容： interface IndicatorStyle | component/tab\_content.d.ts |
| 新增API | NA | 类名：IndicatorStyle；  API声明：color?: ResourceColor;  差异内容：color?: ResourceColor; | component/tab\_content.d.ts |
| 新增API | NA | 类名：IndicatorStyle；  API声明：height?: Length;  差异内容：height?: Length; | component/tab\_content.d.ts |
| 新增API | NA | 类名：IndicatorStyle；  API声明：width?: Length;  差异内容：width?: Length; | component/tab\_content.d.ts |
| 新增API | NA | 类名：IndicatorStyle；  API声明：borderRadius?: Length;  差异内容：borderRadius?: Length; | component/tab\_content.d.ts |
| 新增API | NA | 类名：IndicatorStyle；  API声明：marginTop?: Length;  差异内容：marginTop?: Length; | component/tab\_content.d.ts |
| 新增API | NA | 类名：global；  API声明： interface BoardStyle  差异内容： interface BoardStyle | component/tab\_content.d.ts |
| 新增API | NA | 类名：BoardStyle；  API声明：borderRadius?: Length;  差异内容：borderRadius?: Length; | component/tab\_content.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface LabelStyle  差异内容： declare interface LabelStyle | component/tab\_content.d.ts |
| 新增API | NA | 类名：LabelStyle；  API声明：overflow?: TextOverflow;  差异内容：overflow?: TextOverflow; | component/tab\_content.d.ts |
| 新增API | NA | 类名：LabelStyle；  API声明：maxLines?: number;  差异内容：maxLines?: number; | component/tab\_content.d.ts |
| 新增API | NA | 类名：LabelStyle；  API声明：minFontSize?: number | ResourceStr;  差异内容：minFontSize?: number | ResourceStr; | component/tab\_content.d.ts |
| 新增API | NA | 类名：LabelStyle；  API声明：maxFontSize?: number | ResourceStr;  差异内容：maxFontSize?: number | ResourceStr; | component/tab\_content.d.ts |
| 新增API | NA | 类名：LabelStyle；  API声明：heightAdaptivePolicy?: TextHeightAdaptivePolicy;  差异内容：heightAdaptivePolicy?: TextHeightAdaptivePolicy; | component/tab\_content.d.ts |
| 新增API | NA | 类名：LabelStyle；  API声明：font?: Font;  差异内容：font?: Font; | component/tab\_content.d.ts |
| 新增API | NA | 类名：LabelStyle；  API声明：selectedColor?: ResourceColor;  差异内容：selectedColor?: ResourceColor; | component/tab\_content.d.ts |
| 新增API | NA | 类名：LabelStyle；  API声明：unselectedColor?: ResourceColor;  差异内容：unselectedColor?: ResourceColor; | component/tab\_content.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface TabBarIconStyle  差异内容： declare interface TabBarIconStyle | component/tab\_content.d.ts |
| 新增API | NA | 类名：TabBarIconStyle；  API声明：selectedColor?: ResourceColor;  差异内容：selectedColor?: ResourceColor; | component/tab\_content.d.ts |
| 新增API | NA | 类名：TabBarIconStyle；  API声明：unselectedColor?: ResourceColor;  差异内容：unselectedColor?: ResourceColor; | component/tab\_content.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class TabBarSymbol  差异内容： declare class TabBarSymbol | component/tab\_content.d.ts |
| 新增API | NA | 类名：TabBarSymbol；  API声明：normal: SymbolGlyphModifier;  差异内容：normal: SymbolGlyphModifier; | component/tab\_content.d.ts |
| 新增API | NA | 类名：TabBarSymbol；  API声明：selected?: SymbolGlyphModifier;  差异内容：selected?: SymbolGlyphModifier; | component/tab\_content.d.ts |
| 新增API | NA | 类名：SubTabBarStyle；  API声明：static of(content: ResourceStr): SubTabBarStyle;  差异内容：static of(content: ResourceStr): SubTabBarStyle; | component/tab\_content.d.ts |
| 新增API | NA | 类名：SubTabBarStyle；  API声明：static of(content: ResourceStr | ComponentContent): SubTabBarStyle;  差异内容：static of(content: ResourceStr | ComponentContent): SubTabBarStyle; | component/tab\_content.d.ts |
| 新增API | NA | 类名：SubTabBarStyle；  API声明：indicator(value: IndicatorStyle): SubTabBarStyle;  差异内容：indicator(value: IndicatorStyle): SubTabBarStyle; | component/tab\_content.d.ts |
| 新增API | NA | 类名：SubTabBarStyle；  API声明：selectedMode(value: SelectedMode): SubTabBarStyle;  差异内容：selectedMode(value: SelectedMode): SubTabBarStyle; | component/tab\_content.d.ts |
| 新增API | NA | 类名：SubTabBarStyle；  API声明：board(value: BoardStyle): SubTabBarStyle;  差异内容：board(value: BoardStyle): SubTabBarStyle; | component/tab\_content.d.ts |
| 新增API | NA | 类名：SubTabBarStyle；  API声明：labelStyle(value: LabelStyle): SubTabBarStyle;  差异内容：labelStyle(value: LabelStyle): SubTabBarStyle; | component/tab\_content.d.ts |
| 新增API | NA | 类名：SubTabBarStyle；  API声明：padding(value: Padding | Dimension): SubTabBarStyle;  差异内容：padding(value: Padding | Dimension): SubTabBarStyle; | component/tab\_content.d.ts |
| 新增API | NA | 类名：SubTabBarStyle；  API声明：id(value: string): SubTabBarStyle;  差异内容：id(value: string): SubTabBarStyle; | component/tab\_content.d.ts |
| 新增API | NA | 类名：BottomTabBarStyle；  API声明：static of(icon: ResourceStr | TabBarSymbol, text: ResourceStr): BottomTabBarStyle;  差异内容：static of(icon: ResourceStr | TabBarSymbol, text: ResourceStr): BottomTabBarStyle; | component/tab\_content.d.ts |
| 新增API | NA | 类名：BottomTabBarStyle；  API声明：labelStyle(value: LabelStyle): BottomTabBarStyle;  差异内容：labelStyle(value: LabelStyle): BottomTabBarStyle; | component/tab\_content.d.ts |
| 新增API | NA | 类名：BottomTabBarStyle；  API声明：padding(value: Padding | Dimension): BottomTabBarStyle;  差异内容：padding(value: Padding | Dimension): BottomTabBarStyle; | component/tab\_content.d.ts |
| 新增API | NA | 类名：BottomTabBarStyle；  API声明：layoutMode(value: LayoutMode): BottomTabBarStyle;  差异内容：layoutMode(value: LayoutMode): BottomTabBarStyle; | component/tab\_content.d.ts |
| 新增API | NA | 类名：BottomTabBarStyle；  API声明：verticalAlign(value: VerticalAlign): BottomTabBarStyle;  差异内容：verticalAlign(value: VerticalAlign): BottomTabBarStyle; | component/tab\_content.d.ts |
| 新增API | NA | 类名：BottomTabBarStyle；  API声明：symmetricExtensible(value: boolean): BottomTabBarStyle;  差异内容：symmetricExtensible(value: boolean): BottomTabBarStyle; | component/tab\_content.d.ts |
| 新增API | NA | 类名：BottomTabBarStyle；  API声明：id(value: string): BottomTabBarStyle;  差异内容：id(value: string): BottomTabBarStyle; | component/tab\_content.d.ts |
| 新增API | NA | 类名：BottomTabBarStyle；  API声明：iconStyle(style: TabBarIconStyle): BottomTabBarStyle;  差异内容：iconStyle(style: TabBarIconStyle): BottomTabBarStyle; | component/tab\_content.d.ts |
| 新增API | NA | 类名：TabContentAttribute；  API声明：onWillShow(event: VoidCallback): TabContentAttribute;  差异内容：onWillShow(event: VoidCallback): TabContentAttribute; | component/tab\_content.d.ts |
| 新增API | NA | 类名：TabContentAttribute；  API声明：onWillHide(event: VoidCallback): TabContentAttribute;  差异内容：onWillHide(event: VoidCallback): TabContentAttribute; | component/tab\_content.d.ts |
| 新增API | NA | 类名：TextAttribute；  API声明：font(value: Font): TextAttribute;  差异内容：font(value: Font): TextAttribute; | component/text.d.ts |
| 新增API | NA | 类名：TextAttribute；  API声明：lineSpacing(value: LengthMetrics): TextAttribute;  差异内容：lineSpacing(value: LengthMetrics): TextAttribute; | component/text.d.ts |
| 新增API | NA | 类名：TextAttribute；  API声明：draggable(value: boolean): TextAttribute;  差异内容：draggable(value: boolean): TextAttribute; | component/text.d.ts |
| 新增API | NA | 类名：TextAttribute；  API声明：textShadow(value: ShadowOptions | Array<ShadowOptions>): TextAttribute;  差异内容：textShadow(value: ShadowOptions | Array<ShadowOptions>): TextAttribute; | component/text.d.ts |
| 新增API | NA | 类名：TextAttribute；  API声明：heightAdaptivePolicy(value: TextHeightAdaptivePolicy): TextAttribute;  差异内容：heightAdaptivePolicy(value: TextHeightAdaptivePolicy): TextAttribute; | component/text.d.ts |
| 新增API | NA | 类名：TextAttribute；  API声明：textIndent(value: Length): TextAttribute;  差异内容：textIndent(value: Length): TextAttribute; | component/text.d.ts |
| 新增API | NA | 类名：TextAttribute；  API声明：wordBreak(value: WordBreak): TextAttribute;  差异内容：wordBreak(value: WordBreak): TextAttribute; | component/text.d.ts |
| 新增API | NA | 类名：TextAttribute；  API声明：lineBreakStrategy(strategy: LineBreakStrategy): TextAttribute;  差异内容：lineBreakStrategy(strategy: LineBreakStrategy): TextAttribute; | component/text.d.ts |
| 新增API | NA | 类名：TextAttribute；  API声明：onCopy(callback: (value: string) => void): TextAttribute;  差异内容：onCopy(callback: (value: string) => void): TextAttribute; | component/text.d.ts |
| 新增API | NA | 类名：TextAttribute；  API声明：selection(selectionStart: number, selectionEnd: number): TextAttribute;  差异内容：selection(selectionStart: number, selectionEnd: number): TextAttribute; | component/text.d.ts |
| 新增API | NA | 类名：TextAttribute；  API声明：ellipsisMode(value: EllipsisMode): TextAttribute;  差异内容：ellipsisMode(value: EllipsisMode): TextAttribute; | component/text.d.ts |
| 新增API | NA | 类名：TextAttribute；  API声明：enableDataDetector(enable: boolean): TextAttribute;  差异内容：enableDataDetector(enable: boolean): TextAttribute; | component/text.d.ts |
| 新增API | NA | 类名：TextAttribute；  API声明：dataDetectorConfig(config: TextDataDetectorConfig): TextAttribute;  差异内容：dataDetectorConfig(config: TextDataDetectorConfig): TextAttribute; | component/text.d.ts |
| 新增API | NA | 类名：TextAttribute；  API声明：bindSelectionMenu(spanType: TextSpanType, content: CustomBuilder, responseType: TextResponseType, options?: SelectionMenuOptions): TextAttribute;  差异内容：bindSelectionMenu(spanType: TextSpanType, content: CustomBuilder, responseType: TextResponseType, options?: SelectionMenuOptions): TextAttribute; | component/text.d.ts |
| 新增API | NA | 类名：TextAttribute；  API声明：onTextSelectionChange(callback: (selectionStart: number, selectionEnd: number) => void): TextAttribute;  差异内容：onTextSelectionChange(callback: (selectionStart: number, selectionEnd: number) => void): TextAttribute; | component/text.d.ts |
| 新增API | NA | 类名：TextAttribute；  API声明：fontFeature(value: string): TextAttribute;  差异内容：fontFeature(value: string): TextAttribute; | component/text.d.ts |
| 新增API | NA | 类名：TextAttribute；  API声明：privacySensitive(supported: boolean): TextAttribute;  差异内容：privacySensitive(supported: boolean): TextAttribute; | component/text.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum TextSpanType  差异内容： declare enum TextSpanType | component/text.d.ts |
| 新增API | NA | 类名：TextSpanType；  API声明：TEXT = 0  差异内容：TEXT = 0 | component/text.d.ts |
| 新增API | NA | 类名：TextSpanType；  API声明：IMAGE = 1  差异内容：IMAGE = 1 | component/text.d.ts |
| 新增API | NA | 类名：TextSpanType；  API声明：MIXED = 2  差异内容：MIXED = 2 | component/text.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum TextResponseType  差异内容： declare enum TextResponseType | component/text.d.ts |
| 新增API | NA | 类名：TextResponseType；  API声明：RIGHT\_CLICK = 0  差异内容：RIGHT\_CLICK = 0 | component/text.d.ts |
| 新增API | NA | 类名：TextResponseType；  API声明：LONG\_PRESS = 1  差异内容：LONG\_PRESS = 1 | component/text.d.ts |
| 新增API | NA | 类名：TextResponseType；  API声明：SELECT = 2  差异内容：SELECT = 2 | component/text.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface TextOptions  差异内容： declare interface TextOptions | component/text.d.ts |
| 新增API | NA | 类名：TextOptions；  API声明：controller: TextController;  差异内容：controller: TextController; | component/text.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class TextController  差异内容： declare class TextController | component/text.d.ts |
| 新增API | NA | 类名：TextController；  API声明：closeSelectionMenu(): void;  差异内容：closeSelectionMenu(): void; | component/text.d.ts |
| 新增API | NA | 类名：TextController；  API声明：setStyledString(value: StyledString): void;  差异内容：setStyledString(value: StyledString): void; | component/text.d.ts |
| 新增API | NA | 类名：TextAreaController；  API声明：setTextSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void;  差异内容：setTextSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void; | component/text\_area.d.ts |
| 新增API | NA | 类名：TextAreaController；  API声明：stopEditing(): void;  差异内容：stopEditing(): void; | component/text\_area.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum TextAreaType  差异内容： declare enum TextAreaType | component/text\_area.d.ts |
| 新增API | NA | 类名：TextAreaType；  API声明：NORMAL = 0  差异内容：NORMAL = 0 | component/text\_area.d.ts |
| 新增API | NA | 类名：TextAreaType；  API声明：NUMBER = 2  差异内容：NUMBER = 2 | component/text\_area.d.ts |
| 新增API | NA | 类名：TextAreaType；  API声明：PHONE\_NUMBER = 3  差异内容：PHONE\_NUMBER = 3 | component/text\_area.d.ts |
| 新增API | NA | 类名：TextAreaType；  API声明：EMAIL = 5  差异内容：EMAIL = 5 | component/text\_area.d.ts |
| 新增API | NA | 类名：TextAreaType；  API声明：NUMBER\_DECIMAL = 12  差异内容：NUMBER\_DECIMAL = 12 | component/text\_area.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum ContentType  差异内容： declare enum ContentType | component/text\_area.d.ts |
| 新增API | NA | 类名：ContentType；  API声明：USER\_NAME = 0  差异内容：USER\_NAME = 0 | component/text\_area.d.ts |
| 新增API | NA | 类名：ContentType；  API声明：PASSWORD = 1  差异内容：PASSWORD = 1 | component/text\_area.d.ts |
| 新增API | NA | 类名：ContentType；  API声明：NEW\_PASSWORD = 2  差异内容：NEW\_PASSWORD = 2 | component/text\_area.d.ts |
| 新增API | NA | 类名：ContentType；  API声明：FULL\_STREET\_ADDRESS = 3  差异内容：FULL\_STREET\_ADDRESS = 3 | component/text\_area.d.ts |
| 新增API | NA | 类名：ContentType；  API声明：HOUSE\_NUMBER = 4  差异内容：HOUSE\_NUMBER = 4 | component/text\_area.d.ts |
| 新增API | NA | 类名：ContentType；  API声明：DISTRICT\_ADDRESS = 5  差异内容：DISTRICT\_ADDRESS = 5 | component/text\_area.d.ts |
| 新增API | NA | 类名：ContentType；  API声明：CITY\_ADDRESS = 6  差异内容：CITY\_ADDRESS = 6 | component/text\_area.d.ts |
| 新增API | NA | 类名：ContentType；  API声明：PROVINCE\_ADDRESS = 7  差异内容：PROVINCE\_ADDRESS = 7 | component/text\_area.d.ts |
| 新增API | NA | 类名：ContentType；  API声明：COUNTRY\_ADDRESS = 8  差异内容：COUNTRY\_ADDRESS = 8 | component/text\_area.d.ts |
| 新增API | NA | 类名：ContentType；  API声明：PERSON\_FULL\_NAME = 9  差异内容：PERSON\_FULL\_NAME = 9 | component/text\_area.d.ts |
| 新增API | NA | 类名：ContentType；  API声明：PERSON\_LAST\_NAME = 10  差异内容：PERSON\_LAST\_NAME = 10 | component/text\_area.d.ts |
| 新增API | NA | 类名：ContentType；  API声明：PERSON\_FIRST\_NAME = 11  差异内容：PERSON\_FIRST\_NAME = 11 | component/text\_area.d.ts |
| 新增API | NA | 类名：ContentType；  API声明：PHONE\_NUMBER = 12  差异内容：PHONE\_NUMBER = 12 | component/text\_area.d.ts |
| 新增API | NA | 类名：ContentType；  API声明：PHONE\_COUNTRY\_CODE = 13  差异内容：PHONE\_COUNTRY\_CODE = 13 | component/text\_area.d.ts |
| 新增API | NA | 类名：ContentType；  API声明：FULL\_PHONE\_NUMBER = 14  差异内容：FULL\_PHONE\_NUMBER = 14 | component/text\_area.d.ts |
| 新增API | NA | 类名：ContentType；  API声明：EMAIL\_ADDRESS = 15  差异内容：EMAIL\_ADDRESS = 15 | component/text\_area.d.ts |
| 新增API | NA | 类名：ContentType；  API声明：BANK\_CARD\_NUMBER = 16  差异内容：BANK\_CARD\_NUMBER = 16 | component/text\_area.d.ts |
| 新增API | NA | 类名：ContentType；  API声明：ID\_CARD\_NUMBER = 17  差异内容：ID\_CARD\_NUMBER = 17 | component/text\_area.d.ts |
| 新增API | NA | 类名：ContentType；  API声明：NICKNAME = 23  差异内容：NICKNAME = 23 | component/text\_area.d.ts |
| 新增API | NA | 类名：ContentType；  API声明：DETAIL\_INFO\_WITHOUT\_STREET = 24  差异内容：DETAIL\_INFO\_WITHOUT\_STREET = 24 | component/text\_area.d.ts |
| 新增API | NA | 类名：ContentType；  API声明：FORMAT\_ADDRESS = 25  差异内容：FORMAT\_ADDRESS = 25 | component/text\_area.d.ts |
| 新增API | NA | 类名：TextAreaAttribute；  API声明：enterKeyType(value: EnterKeyType): TextAreaAttribute;  差异内容：enterKeyType(value: EnterKeyType): TextAreaAttribute; | component/text\_area.d.ts |
| 新增API | NA | 类名：TextAreaAttribute；  API声明：textOverflow(value: TextOverflow): TextAreaAttribute;  差异内容：textOverflow(value: TextOverflow): TextAreaAttribute; | component/text\_area.d.ts |
| 新增API | NA | 类名：TextAreaAttribute；  API声明：textIndent(value: Dimension): TextAreaAttribute;  差异内容：textIndent(value: Dimension): TextAreaAttribute; | component/text\_area.d.ts |
| 新增API | NA | 类名：TextAreaAttribute；  API声明：caretStyle(value: CaretStyle): TextAreaAttribute;  差异内容：caretStyle(value: CaretStyle): TextAreaAttribute; | component/text\_area.d.ts |
| 新增API | NA | 类名：TextAreaAttribute；  API声明：selectedBackgroundColor(value: ResourceColor): TextAreaAttribute;  差异内容：selectedBackgroundColor(value: ResourceColor): TextAreaAttribute; | component/text\_area.d.ts |
| 新增API | NA | 类名：TextAreaAttribute；  API声明：onSubmit(callback: (enterKey: EnterKeyType) => void): TextAreaAttribute;  差异内容：onSubmit(callback: (enterKey: EnterKeyType) => void): TextAreaAttribute; | component/text\_area.d.ts |
| 新增API | NA | 类名：TextAreaAttribute；  API声明：onTextSelectionChange(callback: (selectionStart: number, selectionEnd: number) => void): TextAreaAttribute;  差异内容：onTextSelectionChange(callback: (selectionStart: number, selectionEnd: number) => void): TextAreaAttribute; | component/text\_area.d.ts |
| 新增API | NA | 类名：TextAreaAttribute；  API声明：onContentScroll(callback: (totalOffsetX: number, totalOffsetY: number) => void): TextAreaAttribute;  差异内容：onContentScroll(callback: (totalOffsetX: number, totalOffsetY: number) => void): TextAreaAttribute; | component/text\_area.d.ts |
| 新增API | NA | 类名：TextAreaAttribute；  API声明：onEditChange(callback: (isEditing: boolean) => void): TextAreaAttribute;  差异内容：onEditChange(callback: (isEditing: boolean) => void): TextAreaAttribute; | component/text\_area.d.ts |
| 新增API | NA | 类名：TextAreaAttribute；  API声明：enableKeyboardOnFocus(value: boolean): TextAreaAttribute;  差异内容：enableKeyboardOnFocus(value: boolean): TextAreaAttribute; | component/text\_area.d.ts |
| 新增API | NA | 类名：TextAreaAttribute；  API声明：maxLength(value: number): TextAreaAttribute;  差异内容：maxLength(value: number): TextAreaAttribute; | component/text\_area.d.ts |
| 新增API | NA | 类名：TextAreaAttribute；  API声明：showCounter(value: boolean, options?: InputCounterOptions): TextAreaAttribute;  差异内容：showCounter(value: boolean, options?: InputCounterOptions): TextAreaAttribute; | component/text\_area.d.ts |
| 新增API | NA | 类名：TextAreaAttribute；  API声明：style(value: TextContentStyle): TextAreaAttribute;  差异内容：style(value: TextContentStyle): TextAreaAttribute; | component/text\_area.d.ts |
| 新增API | NA | 类名：TextAreaAttribute；  API声明：barState(value: BarState): TextAreaAttribute;  差异内容：barState(value: BarState): TextAreaAttribute; | component/text\_area.d.ts |
| 新增API | NA | 类名：TextAreaAttribute；  API声明：selectionMenuHidden(value: boolean): TextAreaAttribute;  差异内容：selectionMenuHidden(value: boolean): TextAreaAttribute; | component/text\_area.d.ts |
| 新增API | NA | 类名：TextAreaAttribute；  API声明：minFontSize(value: number | string | Resource): TextAreaAttribute;  差异内容：minFontSize(value: number | string | Resource): TextAreaAttribute; | component/text\_area.d.ts |
| 新增API | NA | 类名：TextAreaAttribute；  API声明：maxFontSize(value: number | string | Resource): TextAreaAttribute;  差异内容：maxFontSize(value: number | string | Resource): TextAreaAttribute; | component/text\_area.d.ts |
| 新增API | NA | 类名：TextAreaAttribute；  API声明：heightAdaptivePolicy(value: TextHeightAdaptivePolicy): TextAreaAttribute;  差异内容：heightAdaptivePolicy(value: TextHeightAdaptivePolicy): TextAreaAttribute; | component/text\_area.d.ts |
| 新增API | NA | 类名：TextAreaAttribute；  API声明：maxLines(value: number): TextAreaAttribute;  差异内容：maxLines(value: number): TextAreaAttribute; | component/text\_area.d.ts |
| 新增API | NA | 类名：TextAreaAttribute；  API声明：wordBreak(value: WordBreak): TextAreaAttribute;  差异内容：wordBreak(value: WordBreak): TextAreaAttribute; | component/text\_area.d.ts |
| 新增API | NA | 类名：TextAreaAttribute；  API声明：lineBreakStrategy(strategy: LineBreakStrategy): TextAreaAttribute;  差异内容：lineBreakStrategy(strategy: LineBreakStrategy): TextAreaAttribute; | component/text\_area.d.ts |
| 新增API | NA | 类名：TextAreaAttribute；  API声明：customKeyboard(value: CustomBuilder, options?: KeyboardOptions): TextAreaAttribute;  差异内容：customKeyboard(value: CustomBuilder, options?: KeyboardOptions): TextAreaAttribute; | component/text\_area.d.ts |
| 新增API | NA | 类名：TextAreaAttribute；  API声明：decoration(value: TextDecorationOptions): TextAreaAttribute;  差异内容：decoration(value: TextDecorationOptions): TextAreaAttribute; | component/text\_area.d.ts |
| 新增API | NA | 类名：TextAreaAttribute；  API声明：letterSpacing(value: number | string | Resource): TextAreaAttribute;  差异内容：letterSpacing(value: number | string | Resource): TextAreaAttribute; | component/text\_area.d.ts |
| 新增API | NA | 类名：TextAreaAttribute；  API声明：lineSpacing(value: LengthMetrics): TextAreaAttribute;  差异内容：lineSpacing(value: LengthMetrics): TextAreaAttribute; | component/text\_area.d.ts |
| 新增API | NA | 类名：TextAreaAttribute；  API声明：lineHeight(value: number | string | Resource): TextAreaAttribute;  差异内容：lineHeight(value: number | string | Resource): TextAreaAttribute; | component/text\_area.d.ts |
| 新增API | NA | 类名：TextAreaAttribute；  API声明：type(value: TextAreaType): TextAreaAttribute;  差异内容：type(value: TextAreaType): TextAreaAttribute; | component/text\_area.d.ts |
| 新增API | NA | 类名：TextAreaAttribute；  API声明：enableAutoFill(value: boolean): TextAreaAttribute;  差异内容：enableAutoFill(value: boolean): TextAreaAttribute; | component/text\_area.d.ts |
| 新增API | NA | 类名：TextAreaAttribute；  API声明：contentType(contentType: ContentType): TextAreaAttribute;  差异内容：contentType(contentType: ContentType): TextAreaAttribute; | component/text\_area.d.ts |
| 新增API | NA | 类名：TextAreaAttribute；  API声明：fontFeature(value: string): TextAreaAttribute;  差异内容：fontFeature(value: string): TextAreaAttribute; | component/text\_area.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface TextClockConfiguration  差异内容： declare interface TextClockConfiguration | component/text\_clock.d.ts |
| 新增API | NA | 类名：TextClockConfiguration；  API声明：timeZoneOffset: number;  差异内容：timeZoneOffset: number; | component/text\_clock.d.ts |
| 新增API | NA | 类名：TextClockConfiguration；  API声明：started: boolean;  差异内容：started: boolean; | component/text\_clock.d.ts |
| 新增API | NA | 类名：TextClockConfiguration；  API声明：timeValue: number;  差异内容：timeValue: number; | component/text\_clock.d.ts |
| 新增API | NA | 类名：TextClockAttribute；  API声明：textShadow(value: ShadowOptions | Array<ShadowOptions>): TextClockAttribute;  差异内容：textShadow(value: ShadowOptions | Array<ShadowOptions>): TextClockAttribute; | component/text\_clock.d.ts |
| 新增API | NA | 类名：TextClockAttribute；  API声明：fontFeature(value: string): TextClockAttribute;  差异内容：fontFeature(value: string): TextClockAttribute; | component/text\_clock.d.ts |
| 新增API | NA | 类名：TextClockAttribute；  API声明：contentModifier(modifier: ContentModifier<TextClockConfiguration>): TextClockAttribute;  差异内容：contentModifier(modifier: ContentModifier<TextClockConfiguration>): TextClockAttribute; | component/text\_clock.d.ts |
| 新增API | NA | 类名：InputType；  API声明：NUMBER\_PASSWORD = 8  差异内容：NUMBER\_PASSWORD = 8 | component/text\_input.d.ts |
| 新增API | NA | 类名：InputType；  API声明：USER\_NAME = 10  差异内容：USER\_NAME = 10 | component/text\_input.d.ts |
| 新增API | NA | 类名：InputType；  API声明：NEW\_PASSWORD = 11  差异内容：NEW\_PASSWORD = 11 | component/text\_input.d.ts |
| 新增API | NA | 类名：InputType；  API声明：NUMBER\_DECIMAL = 12  差异内容：NUMBER\_DECIMAL = 12 | component/text\_input.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum ContentType  差异内容： declare enum ContentType | component/text\_input.d.ts |
| 新增API | NA | 类名：ContentType；  API声明：USER\_NAME = 0  差异内容：USER\_NAME = 0 | component/text\_input.d.ts |
| 新增API | NA | 类名：ContentType；  API声明：PASSWORD = 1  差异内容：PASSWORD = 1 | component/text\_input.d.ts |
| 新增API | NA | 类名：ContentType；  API声明：NEW\_PASSWORD = 2  差异内容：NEW\_PASSWORD = 2 | component/text\_input.d.ts |
| 新增API | NA | 类名：ContentType；  API声明：FULL\_STREET\_ADDRESS = 3  差异内容：FULL\_STREET\_ADDRESS = 3 | component/text\_input.d.ts |
| 新增API | NA | 类名：ContentType；  API声明：HOUSE\_NUMBER = 4  差异内容：HOUSE\_NUMBER = 4 | component/text\_input.d.ts |
| 新增API | NA | 类名：ContentType；  API声明：DISTRICT\_ADDRESS = 5  差异内容：DISTRICT\_ADDRESS = 5 | component/text\_input.d.ts |
| 新增API | NA | 类名：ContentType；  API声明：CITY\_ADDRESS = 6  差异内容：CITY\_ADDRESS = 6 | component/text\_input.d.ts |
| 新增API | NA | 类名：ContentType；  API声明：PROVINCE\_ADDRESS = 7  差异内容：PROVINCE\_ADDRESS = 7 | component/text\_input.d.ts |
| 新增API | NA | 类名：ContentType；  API声明：COUNTRY\_ADDRESS = 8  差异内容：COUNTRY\_ADDRESS = 8 | component/text\_input.d.ts |
| 新增API | NA | 类名：ContentType；  API声明：PERSON\_FULL\_NAME = 9  差异内容：PERSON\_FULL\_NAME = 9 | component/text\_input.d.ts |
| 新增API | NA | 类名：ContentType；  API声明：PERSON\_LAST\_NAME = 10  差异内容：PERSON\_LAST\_NAME = 10 | component/text\_input.d.ts |
| 新增API | NA | 类名：ContentType；  API声明：PERSON\_FIRST\_NAME = 11  差异内容：PERSON\_FIRST\_NAME = 11 | component/text\_input.d.ts |
| 新增API | NA | 类名：ContentType；  API声明：PHONE\_NUMBER = 12  差异内容：PHONE\_NUMBER = 12 | component/text\_input.d.ts |
| 新增API | NA | 类名：ContentType；  API声明：PHONE\_COUNTRY\_CODE = 13  差异内容：PHONE\_COUNTRY\_CODE = 13 | component/text\_input.d.ts |
| 新增API | NA | 类名：ContentType；  API声明：FULL\_PHONE\_NUMBER = 14  差异内容：FULL\_PHONE\_NUMBER = 14 | component/text\_input.d.ts |
| 新增API | NA | 类名：ContentType；  API声明：EMAIL\_ADDRESS = 15  差异内容：EMAIL\_ADDRESS = 15 | component/text\_input.d.ts |
| 新增API | NA | 类名：ContentType；  API声明：BANK\_CARD\_NUMBER = 16  差异内容：BANK\_CARD\_NUMBER = 16 | component/text\_input.d.ts |
| 新增API | NA | 类名：ContentType；  API声明：ID\_CARD\_NUMBER = 17  差异内容：ID\_CARD\_NUMBER = 17 | component/text\_input.d.ts |
| 新增API | NA | 类名：ContentType；  API声明：NICKNAME = 23  差异内容：NICKNAME = 23 | component/text\_input.d.ts |
| 新增API | NA | 类名：ContentType；  API声明：DETAIL\_INFO\_WITHOUT\_STREET = 24  差异内容：DETAIL\_INFO\_WITHOUT\_STREET = 24 | component/text\_input.d.ts |
| 新增API | NA | 类名：ContentType；  API声明：FORMAT\_ADDRESS = 25  差异内容：FORMAT\_ADDRESS = 25 | component/text\_input.d.ts |
| 新增API | NA | 类名：EnterKeyType；  API声明：PREVIOUS = 7  差异内容：PREVIOUS = 7 | component/text\_input.d.ts |
| 新增API | NA | 类名：EnterKeyType；  API声明：NEW\_LINE = 8  差异内容：NEW\_LINE = 8 | component/text\_input.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface UnderlineColor  差异内容： declare interface UnderlineColor | component/text\_input.d.ts |
| 新增API | NA | 类名：UnderlineColor；  API声明：typing?: ResourceColor | undefined;  差异内容：typing?: ResourceColor | undefined; | component/text\_input.d.ts |
| 新增API | NA | 类名：UnderlineColor；  API声明：normal?: ResourceColor | undefined;  差异内容：normal?: ResourceColor | undefined; | component/text\_input.d.ts |
| 新增API | NA | 类名：UnderlineColor；  API声明：error?: ResourceColor | undefined;  差异内容：error?: ResourceColor | undefined; | component/text\_input.d.ts |
| 新增API | NA | 类名：UnderlineColor；  API声明：disable?: ResourceColor | undefined;  差异内容：disable?: ResourceColor | undefined; | component/text\_input.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface SubmitEvent  差异内容： declare interface SubmitEvent | component/text\_input.d.ts |
| 新增API | NA | 类名：SubmitEvent；  API声明：keepEditableState(): void;  差异内容：keepEditableState(): void; | component/text\_input.d.ts |
| 新增API | NA | 类名：SubmitEvent；  API声明：text: string;  差异内容：text: string; | component/text\_input.d.ts |
| 新增API | NA | 类名：TextInputController；  API声明：setTextSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void;  差异内容：setTextSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void; | component/text\_input.d.ts |
| 新增API | NA | 类名：TextInputController；  API声明：stopEditing(): void;  差异内容：stopEditing(): void; | component/text\_input.d.ts |
| 新增API | NA | 类名：global；  API声明： interface PasswordIcon  差异内容： interface PasswordIcon | component/text\_input.d.ts |
| 新增API | NA | 类名：PasswordIcon；  API声明：onIconSrc?: string | Resource;  差异内容：onIconSrc?: string | Resource; | component/text\_input.d.ts |
| 新增API | NA | 类名：PasswordIcon；  API声明：offIconSrc?: string | Resource;  差异内容：offIconSrc?: string | Resource; | component/text\_input.d.ts |
| 新增API | NA | 类名：TextInputAttribute；  API声明：contentType(value: ContentType): TextInputAttribute;  差异内容：contentType(value: ContentType): TextInputAttribute; | component/text\_input.d.ts |
| 新增API | NA | 类名：TextInputAttribute；  API声明：textOverflow(value: TextOverflow): TextInputAttribute;  差异内容：textOverflow(value: TextOverflow): TextInputAttribute; | component/text\_input.d.ts |
| 新增API | NA | 类名：TextInputAttribute；  API声明：textIndent(value: Dimension): TextInputAttribute;  差异内容：textIndent(value: Dimension): TextInputAttribute; | component/text\_input.d.ts |
| 新增API | NA | 类名：TextInputAttribute；  API声明：onTextSelectionChange(callback: (selectionStart: number, selectionEnd: number) => void): TextInputAttribute;  差异内容：onTextSelectionChange(callback: (selectionStart: number, selectionEnd: number) => void): TextInputAttribute; | component/text\_input.d.ts |
| 新增API | NA | 类名：TextInputAttribute；  API声明：onContentScroll(callback: (totalOffsetX: number, totalOffsetY: number) => void): TextInputAttribute;  差异内容：onContentScroll(callback: (totalOffsetX: number, totalOffsetY: number) => void): TextInputAttribute; | component/text\_input.d.ts |
| 新增API | NA | 类名：TextInputAttribute；  API声明：caretStyle(value: CaretStyle): TextInputAttribute;  差异内容：caretStyle(value: CaretStyle): TextInputAttribute; | component/text\_input.d.ts |
| 新增API | NA | 类名：TextInputAttribute；  API声明：selectedBackgroundColor(value: ResourceColor): TextInputAttribute;  差异内容：selectedBackgroundColor(value: ResourceColor): TextInputAttribute; | component/text\_input.d.ts |
| 新增API | NA | 类名：TextInputAttribute；  API声明：caretPosition(value: number): TextInputAttribute;  差异内容：caretPosition(value: number): TextInputAttribute; | component/text\_input.d.ts |
| 新增API | NA | 类名：TextInputAttribute；  API声明：enableKeyboardOnFocus(value: boolean): TextInputAttribute;  差异内容：enableKeyboardOnFocus(value: boolean): TextInputAttribute; | component/text\_input.d.ts |
| 新增API | NA | 类名：TextInputAttribute；  API声明：passwordIcon(value: PasswordIcon): TextInputAttribute;  差异内容：passwordIcon(value: PasswordIcon): TextInputAttribute; | component/text\_input.d.ts |
| 新增API | NA | 类名：TextInputAttribute；  API声明：showError(value?: string | undefined): TextInputAttribute;  差异内容：showError(value?: string | undefined): TextInputAttribute; | component/text\_input.d.ts |
| 新增API | NA | 类名：TextInputAttribute；  API声明：showUnit(value: CustomBuilder): TextInputAttribute;  差异内容：showUnit(value: CustomBuilder): TextInputAttribute; | component/text\_input.d.ts |
| 新增API | NA | 类名：TextInputAttribute；  API声明：showUnderline(value: boolean): TextInputAttribute;  差异内容：showUnderline(value: boolean): TextInputAttribute; | component/text\_input.d.ts |
| 新增API | NA | 类名：TextInputAttribute；  API声明：underlineColor(value: ResourceColor | UnderlineColor | undefined): TextInputAttribute;  差异内容：underlineColor(value: ResourceColor | UnderlineColor | undefined): TextInputAttribute; | component/text\_input.d.ts |
| 新增API | NA | 类名：TextInputAttribute；  API声明：selectionMenuHidden(value: boolean): TextInputAttribute;  差异内容：selectionMenuHidden(value: boolean): TextInputAttribute; | component/text\_input.d.ts |
| 新增API | NA | 类名：TextInputAttribute；  API声明：barState(value: BarState): TextInputAttribute;  差异内容：barState(value: BarState): TextInputAttribute; | component/text\_input.d.ts |
| 新增API | NA | 类名：TextInputAttribute；  API声明：maxLines(value: number): TextInputAttribute;  差异内容：maxLines(value: number): TextInputAttribute; | component/text\_input.d.ts |
| 新增API | NA | 类名：TextInputAttribute；  API声明：wordBreak(value: WordBreak): TextInputAttribute;  差异内容：wordBreak(value: WordBreak): TextInputAttribute; | component/text\_input.d.ts |
| 新增API | NA | 类名：TextInputAttribute；  API声明：lineBreakStrategy(strategy: LineBreakStrategy): TextInputAttribute;  差异内容：lineBreakStrategy(strategy: LineBreakStrategy): TextInputAttribute; | component/text\_input.d.ts |
| 新增API | NA | 类名：TextInputAttribute；  API声明：customKeyboard(value: CustomBuilder, options?: KeyboardOptions): TextInputAttribute;  差异内容：customKeyboard(value: CustomBuilder, options?: KeyboardOptions): TextInputAttribute; | component/text\_input.d.ts |
| 新增API | NA | 类名：TextInputAttribute；  API声明：showCounter(value: boolean, options?: InputCounterOptions): TextInputAttribute;  差异内容：showCounter(value: boolean, options?: InputCounterOptions): TextInputAttribute; | component/text\_input.d.ts |
| 新增API | NA | 类名：TextInputAttribute；  API声明：cancelButton(value: {  style?: CancelButtonStyle;  icon?: IconOptions;  }): TextInputAttribute;  差异内容：cancelButton(value: {  style?: CancelButtonStyle;  icon?: IconOptions;  }): TextInputAttribute; | component/text\_input.d.ts |
| 新增API | NA | 类名：TextInputAttribute；  API声明：selectAll(value: boolean): TextInputAttribute;  差异内容：selectAll(value: boolean): TextInputAttribute; | component/text\_input.d.ts |
| 新增API | NA | 类名：TextInputAttribute；  API声明：minFontSize(value: number | string | Resource): TextInputAttribute;  差异内容：minFontSize(value: number | string | Resource): TextInputAttribute; | component/text\_input.d.ts |
| 新增API | NA | 类名：TextInputAttribute；  API声明：maxFontSize(value: number | string | Resource): TextInputAttribute;  差异内容：maxFontSize(value: number | string | Resource): TextInputAttribute; | component/text\_input.d.ts |
| 新增API | NA | 类名：TextInputAttribute；  API声明：heightAdaptivePolicy(value: TextHeightAdaptivePolicy): TextInputAttribute;  差异内容：heightAdaptivePolicy(value: TextHeightAdaptivePolicy): TextInputAttribute; | component/text\_input.d.ts |
| 新增API | NA | 类名：TextInputAttribute；  API声明：enableAutoFill(value: boolean): TextInputAttribute;  差异内容：enableAutoFill(value: boolean): TextInputAttribute; | component/text\_input.d.ts |
| 新增API | NA | 类名：TextInputAttribute；  API声明：decoration(value: TextDecorationOptions): TextInputAttribute;  差异内容：decoration(value: TextDecorationOptions): TextInputAttribute; | component/text\_input.d.ts |
| 新增API | NA | 类名：TextInputAttribute；  API声明：letterSpacing(value: number | string | Resource): TextInputAttribute;  差异内容：letterSpacing(value: number | string | Resource): TextInputAttribute; | component/text\_input.d.ts |
| 新增API | NA | 类名：TextInputAttribute；  API声明：lineHeight(value: number | string | Resource): TextInputAttribute;  差异内容：lineHeight(value: number | string | Resource): TextInputAttribute; | component/text\_input.d.ts |
| 新增API | NA | 类名：TextInputAttribute；  API声明：passwordRules(value: string): TextInputAttribute;  差异内容：passwordRules(value: string): TextInputAttribute; | component/text\_input.d.ts |
| 新增API | NA | 类名：TextInputAttribute；  API声明：fontFeature(value: string): TextInputAttribute;  差异内容：fontFeature(value: string): TextInputAttribute; | component/text\_input.d.ts |
| 新增API | NA | 类名：TextInputAttribute；  API声明：showPassword(visible: boolean): TextInputAttribute;  差异内容：showPassword(visible: boolean): TextInputAttribute; | component/text\_input.d.ts |
| 新增API | NA | 类名：TextInputAttribute；  API声明：onSecurityStateChange(callback: Callback<boolean>): TextInputAttribute;  差异内容：onSecurityStateChange(callback: Callback<boolean>): TextInputAttribute; | component/text\_input.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface TextPickerRangeContent  差异内容： declare interface TextPickerRangeContent | component/text\_picker.d.ts |
| 新增API | NA | 类名：TextPickerRangeContent；  API声明：icon: string | Resource;  差异内容：icon: string | Resource; | component/text\_picker.d.ts |
| 新增API | NA | 类名：TextPickerRangeContent；  API声明：text?: string | Resource;  差异内容：text?: string | Resource; | component/text\_picker.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface TextCascadePickerRangeContent  差异内容： declare interface TextCascadePickerRangeContent | component/text\_picker.d.ts |
| 新增API | NA | 类名：TextCascadePickerRangeContent；  API声明：text: string | Resource;  差异内容：text: string | Resource; | component/text\_picker.d.ts |
| 新增API | NA | 类名：TextCascadePickerRangeContent；  API声明：children?: TextCascadePickerRangeContent[];  差异内容：children?: TextCascadePickerRangeContent[]; | component/text\_picker.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface DividerOptions  差异内容： declare interface DividerOptions | component/text\_picker.d.ts |
| 新增API | NA | 类名：DividerOptions；  API声明：strokeWidth?: Dimension;  差异内容：strokeWidth?: Dimension; | component/text\_picker.d.ts |
| 新增API | NA | 类名：DividerOptions；  API声明：color?: ResourceColor;  差异内容：color?: ResourceColor; | component/text\_picker.d.ts |
| 新增API | NA | 类名：DividerOptions；  API声明：startMargin?: Dimension;  差异内容：startMargin?: Dimension; | component/text\_picker.d.ts |
| 新增API | NA | 类名：DividerOptions；  API声明：endMargin?: Dimension;  差异内容：endMargin?: Dimension; | component/text\_picker.d.ts |
| 新增API | NA | 类名：TextPickerAttribute；  API声明：canLoop(value: boolean): TextPickerAttribute;  差异内容：canLoop(value: boolean): TextPickerAttribute; | component/text\_picker.d.ts |
| 新增API | NA | 类名：TextPickerAttribute；  API声明：disappearTextStyle(value: PickerTextStyle): TextPickerAttribute;  差异内容：disappearTextStyle(value: PickerTextStyle): TextPickerAttribute; | component/text\_picker.d.ts |
| 新增API | NA | 类名：TextPickerAttribute；  API声明：textStyle(value: PickerTextStyle): TextPickerAttribute;  差异内容：textStyle(value: PickerTextStyle): TextPickerAttribute; | component/text\_picker.d.ts |
| 新增API | NA | 类名：TextPickerAttribute；  API声明：selectedTextStyle(value: PickerTextStyle): TextPickerAttribute;  差异内容：selectedTextStyle(value: PickerTextStyle): TextPickerAttribute; | component/text\_picker.d.ts |
| 新增API | NA | 类名：TextPickerAttribute；  API声明：selectedIndex(value: number | number[]): TextPickerAttribute;  差异内容：selectedIndex(value: number | number[]): TextPickerAttribute; | component/text\_picker.d.ts |
| 新增API | NA | 类名：TextPickerAttribute；  API声明：divider(value: DividerOptions | null): TextPickerAttribute;  差异内容：divider(value: DividerOptions | null): TextPickerAttribute; | component/text\_picker.d.ts |
| 新增API | NA | 类名：TextPickerAttribute；  API声明：gradientHeight(value: Dimension): TextPickerAttribute;  差异内容：gradientHeight(value: Dimension): TextPickerAttribute; | component/text\_picker.d.ts |
| 新增API | NA | 类名：TextPickerDialogOptions；  API声明：canLoop?: boolean;  差异内容：canLoop?: boolean; | component/text\_picker.d.ts |
| 新增API | NA | 类名：TextPickerDialogOptions；  API声明：disappearTextStyle?: PickerTextStyle;  差异内容：disappearTextStyle?: PickerTextStyle; | component/text\_picker.d.ts |
| 新增API | NA | 类名：TextPickerDialogOptions；  API声明：textStyle?: PickerTextStyle;  差异内容：textStyle?: PickerTextStyle; | component/text\_picker.d.ts |
| 新增API | NA | 类名：TextPickerDialogOptions；  API声明：acceptButtonStyle?: PickerDialogButtonStyle;  差异内容：acceptButtonStyle?: PickerDialogButtonStyle; | component/text\_picker.d.ts |
| 新增API | NA | 类名：TextPickerDialogOptions；  API声明：cancelButtonStyle?: PickerDialogButtonStyle;  差异内容：cancelButtonStyle?: PickerDialogButtonStyle; | component/text\_picker.d.ts |
| 新增API | NA | 类名：TextPickerDialogOptions；  API声明：selectedTextStyle?: PickerTextStyle;  差异内容：selectedTextStyle?: PickerTextStyle; | component/text\_picker.d.ts |
| 新增API | NA | 类名：TextPickerDialogOptions；  API声明：maskRect?: Rectangle;  差异内容：maskRect?: Rectangle; | component/text\_picker.d.ts |
| 新增API | NA | 类名：TextPickerDialogOptions；  API声明：alignment?: DialogAlignment;  差异内容：alignment?: DialogAlignment; | component/text\_picker.d.ts |
| 新增API | NA | 类名：TextPickerDialogOptions；  API声明：offset?: Offset;  差异内容：offset?: Offset; | component/text\_picker.d.ts |
| 新增API | NA | 类名：TextPickerDialogOptions；  API声明：backgroundColor?: ResourceColor;  差异内容：backgroundColor?: ResourceColor; | component/text\_picker.d.ts |
| 新增API | NA | 类名：TextPickerDialogOptions；  API声明：backgroundBlurStyle?: BlurStyle;  差异内容：backgroundBlurStyle?: BlurStyle; | component/text\_picker.d.ts |
| 新增API | NA | 类名：TextPickerDialogOptions；  API声明：onDidAppear?: () => void;  差异内容：onDidAppear?: () => void; | component/text\_picker.d.ts |
| 新增API | NA | 类名：TextPickerDialogOptions；  API声明：onDidDisappear?: () => void;  差异内容：onDidDisappear?: () => void; | component/text\_picker.d.ts |
| 新增API | NA | 类名：TextPickerDialogOptions；  API声明：onWillAppear?: () => void;  差异内容：onWillAppear?: () => void; | component/text\_picker.d.ts |
| 新增API | NA | 类名：TextPickerDialogOptions；  API声明：onWillDisappear?: () => void;  差异内容：onWillDisappear?: () => void; | component/text\_picker.d.ts |
| 新增API | NA | 类名：TextPickerDialogOptions；  API声明：shadow?: ShadowOptions | ShadowStyle;  差异内容：shadow?: ShadowOptions | ShadowStyle; | component/text\_picker.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface TextTimerConfiguration  差异内容： declare interface TextTimerConfiguration | component/text\_timer.d.ts |
| 新增API | NA | 类名：TextTimerConfiguration；  API声明：count: number;  差异内容：count: number; | component/text\_timer.d.ts |
| 新增API | NA | 类名：TextTimerConfiguration；  API声明：isCountDown: boolean;  差异内容：isCountDown: boolean; | component/text\_timer.d.ts |
| 新增API | NA | 类名：TextTimerConfiguration；  API声明：started: boolean;  差异内容：started: boolean; | component/text\_timer.d.ts |
| 新增API | NA | 类名：TextTimerConfiguration；  API声明：elapsedTime: number;  差异内容：elapsedTime: number; | component/text\_timer.d.ts |
| 新增API | NA | 类名：TextTimerAttribute；  API声明：textShadow(value: ShadowOptions | Array<ShadowOptions>): TextTimerAttribute;  差异内容：textShadow(value: ShadowOptions | Array<ShadowOptions>): TextTimerAttribute; | component/text\_timer.d.ts |
| 新增API | NA | 类名：TextTimerAttribute；  API声明：contentModifier(modifier: ContentModifier<TextTimerConfiguration>): TextTimerAttribute;  差异内容：contentModifier(modifier: ContentModifier<TextTimerConfiguration>): TextTimerAttribute; | component/text\_timer.d.ts |
| 新增API | NA | 类名：TimePickerResult；  API声明：second: number;  差异内容：second: number; | component/time\_picker.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum TimePickerFormat  差异内容： declare enum TimePickerFormat | component/time\_picker.d.ts |
| 新增API | NA | 类名：TimePickerFormat；  API声明：HOUR\_MINUTE  差异内容：HOUR\_MINUTE | component/time\_picker.d.ts |
| 新增API | NA | 类名：TimePickerFormat；  API声明：HOUR\_MINUTE\_SECOND  差异内容：HOUR\_MINUTE\_SECOND | component/time\_picker.d.ts |
| 新增API | NA | 类名：TimePickerOptions；  API声明：format?: TimePickerFormat;  差异内容：format?: TimePickerFormat; | component/time\_picker.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type DateTimeOptions = import('../api/@ohos.intl').default.DateTimeOptions;  差异内容：declare type DateTimeOptions = import('../api/@ohos.intl').default.DateTimeOptions; | component/time\_picker.d.ts |
| 新增API | NA | 类名：TimePickerAttribute；  API声明：loop(value: boolean): TimePickerAttribute;  差异内容：loop(value: boolean): TimePickerAttribute; | component/time\_picker.d.ts |
| 新增API | NA | 类名：TimePickerAttribute；  API声明：disappearTextStyle(value: PickerTextStyle): TimePickerAttribute;  差异内容：disappearTextStyle(value: PickerTextStyle): TimePickerAttribute; | component/time\_picker.d.ts |
| 新增API | NA | 类名：TimePickerAttribute；  API声明：textStyle(value: PickerTextStyle): TimePickerAttribute;  差异内容：textStyle(value: PickerTextStyle): TimePickerAttribute; | component/time\_picker.d.ts |
| 新增API | NA | 类名：TimePickerAttribute；  API声明：selectedTextStyle(value: PickerTextStyle): TimePickerAttribute;  差异内容：selectedTextStyle(value: PickerTextStyle): TimePickerAttribute; | component/time\_picker.d.ts |
| 新增API | NA | 类名：TimePickerAttribute；  API声明：dateTimeOptions(value: DateTimeOptions): TimePickerAttribute;  差异内容：dateTimeOptions(value: DateTimeOptions): TimePickerAttribute; | component/time\_picker.d.ts |
| 新增API | NA | 类名：TimePickerDialogOptions；  API声明：disappearTextStyle?: PickerTextStyle;  差异内容：disappearTextStyle?: PickerTextStyle; | component/time\_picker.d.ts |
| 新增API | NA | 类名：TimePickerDialogOptions；  API声明：textStyle?: PickerTextStyle;  差异内容：textStyle?: PickerTextStyle; | component/time\_picker.d.ts |
| 新增API | NA | 类名：TimePickerDialogOptions；  API声明：acceptButtonStyle?: PickerDialogButtonStyle;  差异内容：acceptButtonStyle?: PickerDialogButtonStyle; | component/time\_picker.d.ts |
| 新增API | NA | 类名：TimePickerDialogOptions；  API声明：cancelButtonStyle?: PickerDialogButtonStyle;  差异内容：cancelButtonStyle?: PickerDialogButtonStyle; | component/time\_picker.d.ts |
| 新增API | NA | 类名：TimePickerDialogOptions；  API声明：selectedTextStyle?: PickerTextStyle;  差异内容：selectedTextStyle?: PickerTextStyle; | component/time\_picker.d.ts |
| 新增API | NA | 类名：TimePickerDialogOptions；  API声明：maskRect?: Rectangle;  差异内容：maskRect?: Rectangle; | component/time\_picker.d.ts |
| 新增API | NA | 类名：TimePickerDialogOptions；  API声明：alignment?: DialogAlignment;  差异内容：alignment?: DialogAlignment; | component/time\_picker.d.ts |
| 新增API | NA | 类名：TimePickerDialogOptions；  API声明：offset?: Offset;  差异内容：offset?: Offset; | component/time\_picker.d.ts |
| 新增API | NA | 类名：TimePickerDialogOptions；  API声明：backgroundColor?: ResourceColor;  差异内容：backgroundColor?: ResourceColor; | component/time\_picker.d.ts |
| 新增API | NA | 类名：TimePickerDialogOptions；  API声明：backgroundBlurStyle?: BlurStyle;  差异内容：backgroundBlurStyle?: BlurStyle; | component/time\_picker.d.ts |
| 新增API | NA | 类名：TimePickerDialogOptions；  API声明：onDidAppear?: () => void;  差异内容：onDidAppear?: () => void; | component/time\_picker.d.ts |
| 新增API | NA | 类名：TimePickerDialogOptions；  API声明：onDidDisappear?: () => void;  差异内容：onDidDisappear?: () => void; | component/time\_picker.d.ts |
| 新增API | NA | 类名：TimePickerDialogOptions；  API声明：onWillAppear?: () => void;  差异内容：onWillAppear?: () => void; | component/time\_picker.d.ts |
| 新增API | NA | 类名：TimePickerDialogOptions；  API声明：onWillDisappear?: () => void;  差异内容：onWillDisappear?: () => void; | component/time\_picker.d.ts |
| 新增API | NA | 类名：TimePickerDialogOptions；  API声明：shadow?: ShadowOptions | ShadowStyle;  差异内容：shadow?: ShadowOptions | ShadowStyle; | component/time\_picker.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface SwitchStyle  差异内容： declare interface SwitchStyle | component/toggle.d.ts |
| 新增API | NA | 类名：SwitchStyle；  API声明：pointRadius?: number | Resource;  差异内容：pointRadius?: number | Resource; | component/toggle.d.ts |
| 新增API | NA | 类名：SwitchStyle；  API声明：unselectedColor?: ResourceColor;  差异内容：unselectedColor?: ResourceColor; | component/toggle.d.ts |
| 新增API | NA | 类名：SwitchStyle；  API声明：pointColor?: ResourceColor;  差异内容：pointColor?: ResourceColor; | component/toggle.d.ts |
| 新增API | NA | 类名：SwitchStyle；  API声明：trackBorderRadius?: number | Resource;  差异内容：trackBorderRadius?: number | Resource; | component/toggle.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface ToggleConfiguration  差异内容： declare interface ToggleConfiguration | component/toggle.d.ts |
| 新增API | NA | 类名：ToggleConfiguration；  API声明：isOn: boolean;  差异内容：isOn: boolean; | component/toggle.d.ts |
| 新增API | NA | 类名：ToggleConfiguration；  API声明：enabled: boolean;  差异内容：enabled: boolean; | component/toggle.d.ts |
| 新增API | NA | 类名：ToggleConfiguration；  API声明：triggerChange: Callback<boolean>;  差异内容：triggerChange: Callback<boolean>; | component/toggle.d.ts |
| 新增API | NA | 类名：ToggleAttribute；  API声明：contentModifier(modifier: ContentModifier<ToggleConfiguration>): ToggleAttribute;  差异内容：contentModifier(modifier: ContentModifier<ToggleConfiguration>): ToggleAttribute; | component/toggle.d.ts |
| 新增API | NA | 类名：ToggleAttribute；  API声明：switchStyle(value: SwitchStyle): ToggleAttribute;  差异内容：switchStyle(value: SwitchStyle): ToggleAttribute; | component/toggle.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type PX = ${number}px;  差异内容：declare type PX = ${number}px; | component/units.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type VP = ${number}vp | number;  差异内容：declare type VP = ${number}vp | number; | component/units.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type FP = ${number}fp;  差异内容：declare type FP = ${number}fp; | component/units.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type LPX = ${number}lpx;  差异内容：declare type LPX = ${number}lpx; | component/units.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type Percentage = ${number}%;  差异内容：declare type Percentage = ${number}%; | component/units.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type Degree = ${number}deg;  差异内容：declare type Degree = ${number}deg; | component/units.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type Dimension = PX | VP | FP | LPX | Percentage | Resource;  差异内容：declare type Dimension = PX | VP | FP | LPX | Percentage | Resource; | component/units.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface LocalizedPadding  差异内容： declare interface LocalizedPadding | component/units.d.ts |
| 新增API | NA | 类名：LocalizedPadding；  API声明：top?: LengthMetrics;  差异内容：top?: LengthMetrics; | component/units.d.ts |
| 新增API | NA | 类名：LocalizedPadding；  API声明：end?: LengthMetrics;  差异内容：end?: LengthMetrics; | component/units.d.ts |
| 新增API | NA | 类名：LocalizedPadding；  API声明：bottom?: LengthMetrics;  差异内容：bottom?: LengthMetrics; | component/units.d.ts |
| 新增API | NA | 类名：LocalizedPadding；  API声明：start?: LengthMetrics;  差异内容：start?: LengthMetrics; | component/units.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type EdgeWidth = EdgeWidths;  差异内容：declare type EdgeWidth = EdgeWidths; | component/units.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface LocalizedEdgeWidths  差异内容： declare interface LocalizedEdgeWidths | component/units.d.ts |
| 新增API | NA | 类名：LocalizedEdgeWidths；  API声明：top?: LengthMetrics;  差异内容：top?: LengthMetrics; | component/units.d.ts |
| 新增API | NA | 类名：LocalizedEdgeWidths；  API声明：end?: LengthMetrics;  差异内容：end?: LengthMetrics; | component/units.d.ts |
| 新增API | NA | 类名：LocalizedEdgeWidths；  API声明：bottom?: LengthMetrics;  差异内容：bottom?: LengthMetrics; | component/units.d.ts |
| 新增API | NA | 类名：LocalizedEdgeWidths；  API声明：start?: LengthMetrics;  差异内容：start?: LengthMetrics; | component/units.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type EdgeOutlineWidths = {  /\*\*  \* top outline width property.  \*  \* @type { ?Dimension }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 11  \* @form  \*/  top?: Dimension;  /\*\*  \* right outline width property.  \*  \* @type { ?Dimension }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 11  \* @form  \*/  right?: Dimension;  /\*\*  \* bottom outline width property.  \*  \* @type { ?Dimension }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 11  \* @form  \*/  bottom?: Dimension;  /\*\*  \* left outline width property.  \*  \* @type { ?Dimension }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 11  \* @form  \*/  left?: Dimension;  };  差异内容：declare type EdgeOutlineWidths = {  /\*\*  \* top outline width property.  \*  \* @type { ?Dimension }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 11  \* @form  \*/  top?: Dimension;  /\*\*  \* right outline width property.  \*  \* @type { ?Dimension }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 11  \* @form  \*/  right?: Dimension;  /\*\*  \* bottom outline width property.  \*  \* @type { ?Dimension }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 11  \* @form  \*/  bottom?: Dimension;  /\*\*  \* left outline width property.  \*  \* @type { ?Dimension }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 11  \* @form  \*/  left?: Dimension;  }; | component/units.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface LocalizedBorderRadiuses  差异内容： declare interface LocalizedBorderRadiuses | component/units.d.ts |
| 新增API | NA | 类名：LocalizedBorderRadiuses；  API声明：topStart?: LengthMetrics;  差异内容：topStart?: LengthMetrics; | component/units.d.ts |
| 新增API | NA | 类名：LocalizedBorderRadiuses；  API声明：topEnd?: LengthMetrics;  差异内容：topEnd?: LengthMetrics; | component/units.d.ts |
| 新增API | NA | 类名：LocalizedBorderRadiuses；  API声明：bottomStart?: LengthMetrics;  差异内容：bottomStart?: LengthMetrics; | component/units.d.ts |
| 新增API | NA | 类名：LocalizedBorderRadiuses；  API声明：bottomEnd?: LengthMetrics;  差异内容：bottomEnd?: LengthMetrics; | component/units.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type OutlineRadiuses = {  /\*\*  \* top-left property.  \*  \* @type { ?Dimension }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 11  \* @form  \*/  topLeft?: Dimension;  /\*\*  \* top-right property.  \*  \* @type { ?Dimension }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 11  \* @form  \*/  topRight?: Dimension;  /\*\*  \* bottom-left property.  \*  \* @type { ?Dimension }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 11  \* @form  \*/  bottomLeft?: Dimension;  /\*\*  \* bottom-right property.  \*  \* @type { ?Dimension }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 11  \* @form  \*/  bottomRight?: Dimension;  };  差异内容：declare type OutlineRadiuses = {  /\*\*  \* top-left property.  \*  \* @type { ?Dimension }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 11  \* @form  \*/  topLeft?: Dimension;  /\*\*  \* top-right property.  \*  \* @type { ?Dimension }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 11  \* @form  \*/  topRight?: Dimension;  /\*\*  \* bottom-left property.  \*  \* @type { ?Dimension }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 11  \* @form  \*/  bottomLeft?: Dimension;  /\*\*  \* bottom-right property.  \*  \* @type { ?Dimension }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 11  \* @form  \*/  bottomRight?: Dimension;  }; | component/units.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface LocalizedEdgeColors  差异内容： declare interface LocalizedEdgeColors | component/units.d.ts |
| 新增API | NA | 类名：LocalizedEdgeColors；  API声明：top?: ResourceColor;  差异内容：top?: ResourceColor; | component/units.d.ts |
| 新增API | NA | 类名：LocalizedEdgeColors；  API声明：end?: ResourceColor;  差异内容：end?: ResourceColor; | component/units.d.ts |
| 新增API | NA | 类名：LocalizedEdgeColors；  API声明：bottom?: ResourceColor;  差异内容：bottom?: ResourceColor; | component/units.d.ts |
| 新增API | NA | 类名：LocalizedEdgeColors；  API声明：start?: ResourceColor;  差异内容：start?: ResourceColor; | component/units.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type LocalizedMargin = LocalizedPadding;  差异内容：declare type LocalizedMargin = LocalizedPadding; | component/units.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type EdgeOutlineStyles = {  /\*\*  \* top property.  \*  \* @type { ?OutlineStyle }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 11  \* @form  \*/  top?: OutlineStyle;  /\*\*  \* right property.  \*  \* @type { ?OutlineStyle }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 11  \* @form  \*/  right?: OutlineStyle;  /\*\*  \* bottom property.  \*  \* @type { ?OutlineStyle }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 11  \* @form  \*/  bottom?: OutlineStyle;  /\*\*  \* left property.  \*  \* @type { ?OutlineStyle }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 11  \* @form  \*/  left?: OutlineStyle;  };  差异内容：declare type EdgeOutlineStyles = {  /\*\*  \* top property.  \*  \* @type { ?OutlineStyle }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 11  \* @form  \*/  top?: OutlineStyle;  /\*\*  \* right property.  \*  \* @type { ?OutlineStyle }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 11  \* @form  \*/  right?: OutlineStyle;  /\*\*  \* bottom property.  \*  \* @type { ?OutlineStyle }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 11  \* @form  \*/  bottom?: OutlineStyle;  /\*\*  \* left property.  \*  \* @type { ?OutlineStyle }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 11  \* @form  \*/  left?: OutlineStyle;  }; | component/units.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type VoidCallback = () => void;  差异内容：declare type VoidCallback = () => void; | component/units.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type LengthMetricsUnit = import('../api/arkui/Graphics').LengthMetricsUnit;  差异内容：declare type LengthMetricsUnit = import('../api/arkui/Graphics').LengthMetricsUnit; | component/units.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type LengthMetrics = import('../api/arkui/Graphics').LengthMetrics;  差异内容：declare type LengthMetrics = import('../api/arkui/Graphics').LengthMetrics; | component/units.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type ColorMetrics = import('../api/arkui/Graphics').ColorMetrics;  差异内容：declare type ColorMetrics = import('../api/arkui/Graphics').ColorMetrics; | component/units.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface LocalizedPosition  差异内容： declare interface LocalizedPosition | component/units.d.ts |
| 新增API | NA | 类名：LocalizedPosition；  API声明：start?: LengthMetrics;  差异内容：start?: LengthMetrics; | component/units.d.ts |
| 新增API | NA | 类名：LocalizedPosition；  API声明：top?: LengthMetrics;  差异内容：top?: LengthMetrics; | component/units.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface Edges  差异内容： declare interface Edges | component/units.d.ts |
| 新增API | NA | 类名：Edges；  API声明：top?: Dimension;  差异内容：top?: Dimension; | component/units.d.ts |
| 新增API | NA | 类名：Edges；  API声明：left?: Dimension;  差异内容：left?: Dimension; | component/units.d.ts |
| 新增API | NA | 类名：Edges；  API声明：bottom?: Dimension;  差异内容：bottom?: Dimension; | component/units.d.ts |
| 新增API | NA | 类名：Edges；  API声明：right?: Dimension;  差异内容：right?: Dimension; | component/units.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface LocalizedEdges  差异内容： declare interface LocalizedEdges | component/units.d.ts |
| 新增API | NA | 类名：LocalizedEdges；  API声明：top?: LengthMetrics;  差异内容：top?: LengthMetrics; | component/units.d.ts |
| 新增API | NA | 类名：LocalizedEdges；  API声明：start?: LengthMetrics;  差异内容：start?: LengthMetrics; | component/units.d.ts |
| 新增API | NA | 类名：LocalizedEdges；  API声明：bottom?: LengthMetrics;  差异内容：bottom?: LengthMetrics; | component/units.d.ts |
| 新增API | NA | 类名：LocalizedEdges；  API声明：end?: LengthMetrics;  差异内容：end?: LengthMetrics; | component/units.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface Bias  差异内容： declare interface Bias | component/units.d.ts |
| 新增API | NA | 类名：Bias；  API声明：horizontal?: number;  差异内容：horizontal?: number; | component/units.d.ts |
| 新增API | NA | 类名：Bias；  API声明：vertical?: number;  差异内容：vertical?: number; | component/units.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface OutlineOptions  差异内容： declare interface OutlineOptions | component/units.d.ts |
| 新增API | NA | 类名：OutlineOptions；  API声明：width?: EdgeOutlineWidths | Dimension;  差异内容：width?: EdgeOutlineWidths | Dimension; | component/units.d.ts |
| 新增API | NA | 类名：OutlineOptions；  API声明：color?: EdgeColors | ResourceColor | LocalizedEdgeColors;  差异内容：color?: EdgeColors | ResourceColor | LocalizedEdgeColors; | component/units.d.ts |
| 新增API | NA | 类名：OutlineOptions；  API声明：radius?: OutlineRadiuses | Dimension;  差异内容：radius?: OutlineRadiuses | Dimension; | component/units.d.ts |
| 新增API | NA | 类名：OutlineOptions；  API声明：style?: EdgeOutlineStyles | OutlineStyle;  差异内容：style?: EdgeOutlineStyles | OutlineStyle; | component/units.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface MarkStyle  差异内容： declare interface MarkStyle | component/units.d.ts |
| 新增API | NA | 类名：MarkStyle；  API声明：strokeColor?: ResourceColor;  差异内容：strokeColor?: ResourceColor; | component/units.d.ts |
| 新增API | NA | 类名：MarkStyle；  API声明：size?: Length;  差异内容：size?: Length; | component/units.d.ts |
| 新增API | NA | 类名：MarkStyle；  API声明：strokeWidth?: Length;  差异内容：strokeWidth?: Length; | component/units.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface TouchPoint  差异内容： declare interface TouchPoint | component/units.d.ts |
| 新增API | NA | 类名：TouchPoint；  API声明：x: Dimension;  差异内容：x: Dimension; | component/units.d.ts |
| 新增API | NA | 类名：TouchPoint；  API声明：y: Dimension;  差异内容：y: Dimension; | component/units.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface DirectionalEdgesT  差异内容： declare interface DirectionalEdgesT | component/units.d.ts |
| 新增API | NA | 类名：DirectionalEdgesT；  API声明：start: T;  差异内容：start: T; | component/units.d.ts |
| 新增API | NA | 类名：DirectionalEdgesT；  API声明：end: T;  差异内容：end: T; | component/units.d.ts |
| 新增API | NA | 类名：DirectionalEdgesT；  API声明：top: T;  差异内容：top: T; | component/units.d.ts |
| 新增API | NA | 类名：DirectionalEdgesT；  API声明：bottom: T;  差异内容：bottom: T; | component/units.d.ts |
| 新增API | NA | 类名：VideoController；  API声明：reset(): void;  差异内容：reset(): void; | component/video.d.ts |
| 新增API | NA | 类名：VideoAttribute；  API声明：onStop(event: Callback<void>): VideoAttribute;  差异内容：onStop(event: Callback<void>): VideoAttribute; | component/video.d.ts |
| 新增API | NA | 类名：VideoAttribute；  API声明：enableAnalyzer(enable: boolean): VideoAttribute;  差异内容：enableAnalyzer(enable: boolean): VideoAttribute; | component/video.d.ts |
| 新增API | NA | 类名：VideoAttribute；  API声明：analyzerConfig(config: ImageAnalyzerConfig): VideoAttribute;  差异内容：analyzerConfig(config: ImageAnalyzerConfig): VideoAttribute; | component/video.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type GetItemMainSizeByIndex = (index: number) => number;  差异内容：declare type GetItemMainSizeByIndex = (index: number) => number; | component/water\_flow.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class SectionOptions  差异内容： declare class SectionOptions | component/water\_flow.d.ts |
| 新增API | NA | 类名：SectionOptions；  API声明：itemsCount: number;  差异内容：itemsCount: number; | component/water\_flow.d.ts |
| 新增API | NA | 类名：SectionOptions；  API声明：crossCount?: number;  差异内容：crossCount?: number; | component/water\_flow.d.ts |
| 新增API | NA | 类名：SectionOptions；  API声明：onGetItemMainSizeByIndex?: GetItemMainSizeByIndex;  差异内容：onGetItemMainSizeByIndex?: GetItemMainSizeByIndex; | component/water\_flow.d.ts |
| 新增API | NA | 类名：SectionOptions；  API声明：columnsGap?: Dimension;  差异内容：columnsGap?: Dimension; | component/water\_flow.d.ts |
| 新增API | NA | 类名：SectionOptions；  API声明：rowsGap?: Dimension;  差异内容：rowsGap?: Dimension; | component/water\_flow.d.ts |
| 新增API | NA | 类名：SectionOptions；  API声明：margin?: Margin | Dimension;  差异内容：margin?: Margin | Dimension; | component/water\_flow.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class WaterFlowSections  差异内容： declare class WaterFlowSections | component/water\_flow.d.ts |
| 新增API | NA | 类名：WaterFlowSections；  API声明：splice(start: number, deleteCount?: number, sections?: Array<SectionOptions>): boolean;  差异内容：splice(start: number, deleteCount?: number, sections?: Array<SectionOptions>): boolean; | component/water\_flow.d.ts |
| 新增API | NA | 类名：WaterFlowSections；  API声明：push(section: SectionOptions): boolean;  差异内容：push(section: SectionOptions): boolean; | component/water\_flow.d.ts |
| 新增API | NA | 类名：WaterFlowSections；  API声明：update(sectionIndex: number, section: SectionOptions): boolean;  差异内容：update(sectionIndex: number, section: SectionOptions): boolean; | component/water\_flow.d.ts |
| 新增API | NA | 类名：WaterFlowSections；  API声明：values(): Array<SectionOptions>;  差异内容：values(): Array<SectionOptions>; | component/water\_flow.d.ts |
| 新增API | NA | 类名：WaterFlowSections；  API声明：length(): number;  差异内容：length(): number; | component/water\_flow.d.ts |
| 新增API | NA | 类名：WaterFlowOptions；  API声明：sections?: WaterFlowSections;  差异内容：sections?: WaterFlowSections; | component/water\_flow.d.ts |
| 新增API | NA | 类名：WaterFlowAttribute；  API声明：nestedScroll(value: NestedScrollOptions): WaterFlowAttribute;  差异内容：nestedScroll(value: NestedScrollOptions): WaterFlowAttribute; | component/water\_flow.d.ts |
| 新增API | NA | 类名：WaterFlowAttribute；  API声明：enableScrollInteraction(value: boolean): WaterFlowAttribute;  差异内容：enableScrollInteraction(value: boolean): WaterFlowAttribute; | component/water\_flow.d.ts |
| 新增API | NA | 类名：WaterFlowAttribute；  API声明：friction(value: number | Resource): WaterFlowAttribute;  差异内容：friction(value: number | Resource): WaterFlowAttribute; | component/water\_flow.d.ts |
| 新增API | NA | 类名：WaterFlowAttribute；  API声明：cachedCount(value: number): WaterFlowAttribute;  差异内容：cachedCount(value: number): WaterFlowAttribute; | component/water\_flow.d.ts |
| 新增API | NA | 类名：WaterFlowAttribute；  API声明：onScrollFrameBegin(event: (offset: number, state: ScrollState) => {  offsetRemain: number;  }): WaterFlowAttribute;  差异内容：onScrollFrameBegin(event: (offset: number, state: ScrollState) => {  offsetRemain: number;  }): WaterFlowAttribute; | component/water\_flow.d.ts |
| 新增API | NA | 类名：WaterFlowAttribute；  API声明：onScrollIndex(event: (first: number, last: number) => void): WaterFlowAttribute;  差异内容：onScrollIndex(event: (first: number, last: number) => void): WaterFlowAttribute; | component/water\_flow.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface SurfaceRect  差异内容： declare interface SurfaceRect | component/xcomponent.d.ts |
| 新增API | NA | 类名：SurfaceRect；  API声明：offsetX?: number;  差异内容：offsetX?: number; | component/xcomponent.d.ts |
| 新增API | NA | 类名：SurfaceRect；  API声明：offsetY?: number;  差异内容：offsetY?: number; | component/xcomponent.d.ts |
| 新增API | NA | 类名：SurfaceRect；  API声明：surfaceWidth: number;  差异内容：surfaceWidth: number; | component/xcomponent.d.ts |
| 新增API | NA | 类名：SurfaceRect；  API声明：surfaceHeight: number;  差异内容：surfaceHeight: number; | component/xcomponent.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface SurfaceRotationOptions  差异内容： declare interface SurfaceRotationOptions | component/xcomponent.d.ts |
| 新增API | NA | 类名：SurfaceRotationOptions；  API声明：lock?: boolean;  差异内容：lock?: boolean; | component/xcomponent.d.ts |
| 新增API | NA | 类名：XComponentController；  API声明：setXComponentSurfaceRect(rect: SurfaceRect): void;  差异内容：setXComponentSurfaceRect(rect: SurfaceRect): void; | component/xcomponent.d.ts |
| 新增API | NA | 类名：XComponentController；  API声明：getXComponentSurfaceRect(): SurfaceRect;  差异内容：getXComponentSurfaceRect(): SurfaceRect; | component/xcomponent.d.ts |
| 新增API | NA | 类名：XComponentController；  API声明：setXComponentSurfaceRotation(rotationOptions: SurfaceRotationOptions): void;  差异内容：setXComponentSurfaceRotation(rotationOptions: SurfaceRotationOptions): void; | component/xcomponent.d.ts |
| 新增API | NA | 类名：XComponentController；  API声明：getXComponentSurfaceRotation(): Required<SurfaceRotationOptions>;  差异内容：getXComponentSurfaceRotation(): Required<SurfaceRotationOptions>; | component/xcomponent.d.ts |
| 新增API | NA | 类名：XComponentController；  API声明：onSurfaceCreated(surfaceId: string): void;  差异内容：onSurfaceCreated(surfaceId: string): void; | component/xcomponent.d.ts |
| 新增API | NA | 类名：XComponentController；  API声明：onSurfaceChanged(surfaceId: string, rect: SurfaceRect): void;  差异内容：onSurfaceChanged(surfaceId: string, rect: SurfaceRect): void; | component/xcomponent.d.ts |
| 新增API | NA | 类名：XComponentController；  API声明：onSurfaceDestroyed(surfaceId: string): void;  差异内容：onSurfaceDestroyed(surfaceId: string): void; | component/xcomponent.d.ts |
| 新增API | NA | 类名：XComponentController；  API声明：startImageAnalyzer(config: ImageAnalyzerConfig): Promise<void>;  差异内容：startImageAnalyzer(config: ImageAnalyzerConfig): Promise<void>; | component/xcomponent.d.ts |
| 新增API | NA | 类名：XComponentController；  API声明：stopImageAnalyzer(): void;  差异内容：stopImageAnalyzer(): void; | component/xcomponent.d.ts |
| 新增API | NA | 类名：XComponentAttribute；  API声明：enableAnalyzer(enable: boolean): XComponentAttribute;  差异内容：enableAnalyzer(enable: boolean): XComponentAttribute; | component/xcomponent.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare enum ChipSize  差异内容： export declare enum ChipSize | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：ChipSize；  API声明：NORMAL = "NORMAL"  差异内容：NORMAL = "NORMAL" | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：ChipSize；  API声明：SMALL = "SMALL"  差异内容：SMALL = "SMALL" | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：global；  API声明： export interface IconCommonOptions  差异内容： export interface IconCommonOptions | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：IconCommonOptions；  API声明：src: ResourceStr;  差异内容：src: ResourceStr; | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：IconCommonOptions；  API声明：size?: SizeOptions;  差异内容：size?: SizeOptions; | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：IconCommonOptions；  API声明：fillColor?: ResourceColor;  差异内容：fillColor?: ResourceColor; | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：IconCommonOptions；  API声明：activatedFillColor?: ResourceColor;  差异内容：activatedFillColor?: ResourceColor; | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：global；  API声明： export interface SuffixIconOptions  差异内容： export interface SuffixIconOptions | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：SuffixIconOptions；  API声明：action?: () => void;  差异内容：action?: () => void; | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：global；  API声明： export interface PrefixIconOptions  差异内容： export interface PrefixIconOptions | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：global；  API声明： export interface LabelMarginOptions  差异内容： export interface LabelMarginOptions | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：LabelMarginOptions；  API声明：left?: Dimension;  差异内容：left?: Dimension; | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：LabelMarginOptions；  API声明：right?: Dimension;  差异内容：right?: Dimension; | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：global；  API声明： export interface LabelOptions  差异内容： export interface LabelOptions | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：LabelOptions；  API声明：text: string;  差异内容：text: string; | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：LabelOptions；  API声明：fontSize?: Dimension;  差异内容：fontSize?: Dimension; | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：LabelOptions；  API声明：fontColor?: ResourceColor;  差异内容：fontColor?: ResourceColor; | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：LabelOptions；  API声明：activatedFontColor?: ResourceColor;  差异内容：activatedFontColor?: ResourceColor; | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：LabelOptions；  API声明：fontFamily?: string;  差异内容：fontFamily?: string; | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：LabelOptions；  API声明：labelMargin?: LabelMarginOptions;  差异内容：labelMargin?: LabelMarginOptions; | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：global；  API声明： export interface ChipOptions  差异内容： export interface ChipOptions | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：ChipOptions；  API声明：prefixIcon?: PrefixIconOptions;  差异内容：prefixIcon?: PrefixIconOptions; | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：ChipOptions；  API声明：label: LabelOptions;  差异内容：label: LabelOptions; | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：ChipOptions；  API声明：suffixIcon?: SuffixIconOptions;  差异内容：suffixIcon?: SuffixIconOptions; | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：ChipOptions；  API声明：allowClose?: boolean;  差异内容：allowClose?: boolean; | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：ChipOptions；  API声明：enabled?: boolean;  差异内容：enabled?: boolean; | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：ChipOptions；  API声明：activated?: boolean;  差异内容：activated?: boolean; | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：ChipOptions；  API声明：backgroundColor?: ResourceColor;  差异内容：backgroundColor?: ResourceColor; | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：ChipOptions；  API声明：activatedBackgroundColor?: ResourceColor;  差异内容：activatedBackgroundColor?: ResourceColor; | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：ChipOptions；  API声明：borderRadius?: Dimension;  差异内容：borderRadius?: Dimension; | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：ChipOptions；  API声明：size?: ChipSize | SizeOptions;  差异内容：size?: ChipSize | SizeOptions; | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：ChipOptions；  API声明：onClose?: () => void;  差异内容：onClose?: () => void; | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：ChipOptions；  API声明：onClicked?: Callback<void>;  差异内容：onClicked?: Callback<void>; | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：global；  API声明：@Builder  export declare function Chip(options: ChipOptions): void;  差异内容：@Builder  export declare function Chip(options: ChipOptions): void; | api/@ohos.arkui.advanced.Chip.d.ets |
| 新增API | NA | 类名：global；  API声明： export interface IconOptions  差异内容： export interface IconOptions | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：IconOptions；  API声明：src: ResourceStr;  差异内容：src: ResourceStr; | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：IconOptions；  API声明：size?: SizeOptions;  差异内容：size?: SizeOptions; | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：global；  API声明： export interface LabelOptions  差异内容： export interface LabelOptions | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：LabelOptions；  API声明：text: string;  差异内容：text: string; | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：global；  API声明： export interface ChipGroupItemOptions  差异内容： export interface ChipGroupItemOptions | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：ChipGroupItemOptions；  API声明：prefixIcon?: IconOptions;  差异内容：prefixIcon?: IconOptions; | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：ChipGroupItemOptions；  API声明：label: LabelOptions;  差异内容：label: LabelOptions; | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：ChipGroupItemOptions；  API声明：suffixIcon?: IconOptions;  差异内容：suffixIcon?: IconOptions; | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：ChipGroupItemOptions；  API声明：allowClose?: boolean;  差异内容：allowClose?: boolean; | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：global；  API声明： export interface ChipItemStyle  差异内容： export interface ChipItemStyle | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：ChipItemStyle；  API声明：size?: ChipSize | SizeOptions;  差异内容：size?: ChipSize | SizeOptions; | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：ChipItemStyle；  API声明：backgroundColor?: ResourceColor;  差异内容：backgroundColor?: ResourceColor; | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：ChipItemStyle；  API声明：fontColor?: ResourceColor;  差异内容：fontColor?: ResourceColor; | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：ChipItemStyle；  API声明：selectedFontColor?: ResourceColor;  差异内容：selectedFontColor?: ResourceColor; | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：ChipItemStyle；  API声明：selectedBackgroundColor?: ResourceColor;  差异内容：selectedBackgroundColor?: ResourceColor; | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：global；  API声明： export interface ChipGroupSpaceOptions  差异内容： export interface ChipGroupSpaceOptions | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：ChipGroupSpaceOptions；  API声明：itemSpace?: string | number;  差异内容：itemSpace?: string | number; | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：ChipGroupSpaceOptions；  API声明：startSpace?: Length;  差异内容：startSpace?: Length; | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：ChipGroupSpaceOptions；  API声明：endSpace?: Length;  差异内容：endSpace?: Length; | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：global；  API声明： export interface IconItemOptions  差异内容： export interface IconItemOptions | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：IconItemOptions；  API声明：icon: IconOptions;  差异内容：icon: IconOptions; | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：IconItemOptions；  API声明：action: Callback<void>;  差异内容：action: Callback<void>; | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare struct IconGroupSuffix  差异内容： export declare struct IconGroupSuffix | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：IconGroupSuffix；  API声明：@Prop  items: Array<IconItemOptions>;  差异内容：@Prop  items: Array<IconItemOptions>; | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare struct ChipGroup  差异内容： export declare struct ChipGroup | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：ChipGroup；  API声明：@Prop  items: ChipGroupItemOptions[];  差异内容：@Prop  items: ChipGroupItemOptions[]; | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：ChipGroup；  API声明：@Prop  itemStyle?: ChipItemStyle;  差异内容：@Prop  itemStyle?: ChipItemStyle; | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：ChipGroup；  API声明：@Prop  selectedIndexes?: Array<number>;  差异内容：@Prop  selectedIndexes?: Array<number>; | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：ChipGroup；  API声明：@Prop  multiple?: boolean;  差异内容：@Prop  multiple?: boolean; | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：ChipGroup；  API声明：@Prop  chipGroupSpace?: ChipGroupSpaceOptions;  差异内容：@Prop  chipGroupSpace?: ChipGroupSpaceOptions; | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：ChipGroup；  API声明：onChange?: Callback<Array<number>>;  差异内容：onChange?: Callback<Array<number>>; | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：ChipGroup；  API声明：@BuilderParam  suffix?: Callback<void>;  差异内容：@BuilderParam  suffix?: Callback<void>; | api/@ohos.arkui.advanced.ChipGroup.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare enum IconType  差异内容： export declare enum IconType | api/@ohos.arkui.advanced.ComposeListItem.d.ets |
| 新增API | NA | 类名：IconType；  API声明：BADGE = 1  差异内容：BADGE = 1 | api/@ohos.arkui.advanced.ComposeListItem.d.ets |
| 新增API | NA | 类名：IconType；  API声明：NORMAL\_ICON = 2  差异内容：NORMAL\_ICON = 2 | api/@ohos.arkui.advanced.ComposeListItem.d.ets |
| 新增API | NA | 类名：IconType；  API声明：SYSTEM\_ICON = 3  差异内容：SYSTEM\_ICON = 3 | api/@ohos.arkui.advanced.ComposeListItem.d.ets |
| 新增API | NA | 类名：IconType；  API声明：HEAD\_SCULPTURE = 4  差异内容：HEAD\_SCULPTURE = 4 | api/@ohos.arkui.advanced.ComposeListItem.d.ets |
| 新增API | NA | 类名：IconType；  API声明：APP\_ICON = 5  差异内容：APP\_ICON = 5 | api/@ohos.arkui.advanced.ComposeListItem.d.ets |
| 新增API | NA | 类名：IconType；  API声明：PREVIEW = 6  差异内容：PREVIEW = 6 | api/@ohos.arkui.advanced.ComposeListItem.d.ets |
| 新增API | NA | 类名：IconType；  API声明：LONGITUDINAL = 7  差异内容：LONGITUDINAL = 7 | api/@ohos.arkui.advanced.ComposeListItem.d.ets |
| 新增API | NA | 类名：IconType；  API声明：VERTICAL = 8  差异内容：VERTICAL = 8 | api/@ohos.arkui.advanced.ComposeListItem.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare class OperateIcon  差异内容： export declare class OperateIcon | api/@ohos.arkui.advanced.ComposeListItem.d.ets |
| 新增API | NA | 类名：OperateIcon；  API声明：value: ResourceStr;  差异内容：value: ResourceStr; | api/@ohos.arkui.advanced.ComposeListItem.d.ets |
| 新增API | NA | 类名：OperateIcon；  API声明：action?: () => void;  差异内容：action?: () => void; | api/@ohos.arkui.advanced.ComposeListItem.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare class OperateCheck  差异内容： export declare class OperateCheck | api/@ohos.arkui.advanced.ComposeListItem.d.ets |
| 新增API | NA | 类名：OperateCheck；  API声明：isCheck?: boolean;  差异内容：isCheck?: boolean; | api/@ohos.arkui.advanced.ComposeListItem.d.ets |
| 新增API | NA | 类名：OperateCheck；  API声明：onChange?: (value: boolean) => void;  差异内容：onChange?: (value: boolean) => void; | api/@ohos.arkui.advanced.ComposeListItem.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare class OperateButton  差异内容： export declare class OperateButton | api/@ohos.arkui.advanced.ComposeListItem.d.ets |
| 新增API | NA | 类名：OperateButton；  API声明：text?: ResourceStr;  差异内容：text?: ResourceStr; | api/@ohos.arkui.advanced.ComposeListItem.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare class ContentItem  差异内容： export declare class ContentItem | api/@ohos.arkui.advanced.ComposeListItem.d.ets |
| 新增API | NA | 类名：ContentItem；  API声明：iconStyle?: IconType;  差异内容：iconStyle?: IconType; | api/@ohos.arkui.advanced.ComposeListItem.d.ets |
| 新增API | NA | 类名：ContentItem；  API声明：icon?: ResourceStr;  差异内容：icon?: ResourceStr; | api/@ohos.arkui.advanced.ComposeListItem.d.ets |
| 新增API | NA | 类名：ContentItem；  API声明：primaryText?: ResourceStr;  差异内容：primaryText?: ResourceStr; | api/@ohos.arkui.advanced.ComposeListItem.d.ets |
| 新增API | NA | 类名：ContentItem；  API声明：secondaryText?: ResourceStr;  差异内容：secondaryText?: ResourceStr; | api/@ohos.arkui.advanced.ComposeListItem.d.ets |
| 新增API | NA | 类名：ContentItem；  API声明：description?: ResourceStr;  差异内容：description?: ResourceStr; | api/@ohos.arkui.advanced.ComposeListItem.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare class OperateItem  差异内容： export declare class OperateItem | api/@ohos.arkui.advanced.ComposeListItem.d.ets |
| 新增API | NA | 类名：OperateItem；  API声明：icon?: OperateIcon;  差异内容：icon?: OperateIcon; | api/@ohos.arkui.advanced.ComposeListItem.d.ets |
| 新增API | NA | 类名：OperateItem；  API声明：subIcon?: OperateIcon;  差异内容：subIcon?: OperateIcon; | api/@ohos.arkui.advanced.ComposeListItem.d.ets |
| 新增API | NA | 类名：OperateItem；  API声明：button?: OperateButton;  差异内容：button?: OperateButton; | api/@ohos.arkui.advanced.ComposeListItem.d.ets |
| 新增API | NA | 类名：OperateItem；  API声明：switch?: OperateCheck;  差异内容：switch?: OperateCheck; | api/@ohos.arkui.advanced.ComposeListItem.d.ets |
| 新增API | NA | 类名：OperateItem；  API声明：checkbox?: OperateCheck;  差异内容：checkbox?: OperateCheck; | api/@ohos.arkui.advanced.ComposeListItem.d.ets |
| 新增API | NA | 类名：OperateItem；  API声明：radio?: OperateCheck;  差异内容：radio?: OperateCheck; | api/@ohos.arkui.advanced.ComposeListItem.d.ets |
| 新增API | NA | 类名：OperateItem；  API声明：image?: ResourceStr;  差异内容：image?: ResourceStr; | api/@ohos.arkui.advanced.ComposeListItem.d.ets |
| 新增API | NA | 类名：OperateItem；  API声明：text?: ResourceStr;  差异内容：text?: ResourceStr; | api/@ohos.arkui.advanced.ComposeListItem.d.ets |
| 新增API | NA | 类名：OperateItem；  API声明：arrow?: OperateIcon;  差异内容：arrow?: OperateIcon; | api/@ohos.arkui.advanced.ComposeListItem.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare struct ComposeListItem  差异内容： export declare struct ComposeListItem | api/@ohos.arkui.advanced.ComposeListItem.d.ets |
| 新增API | NA | 类名：ComposeListItem；  API声明：@Prop  contentItem?: ContentItem;  差异内容：@Prop  contentItem?: ContentItem; | api/@ohos.arkui.advanced.ComposeListItem.d.ets |
| 新增API | NA | 类名：ComposeListItem；  API声明：@Prop  operateItem?: OperateItem;  差异内容：@Prop  operateItem?: OperateItem; | api/@ohos.arkui.advanced.ComposeListItem.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare class ComposeTitleBarMenuItem  差异内容： export declare class ComposeTitleBarMenuItem | api/@ohos.arkui.advanced.ComposeTitleBar.d.ets |
| 新增API | NA | 类名：ComposeTitleBarMenuItem；  API声明：value: ResourceStr;  差异内容：value: ResourceStr; | api/@ohos.arkui.advanced.ComposeTitleBar.d.ets |
| 新增API | NA | 类名：ComposeTitleBarMenuItem；  API声明：isEnabled?: boolean;  差异内容：isEnabled?: boolean; | api/@ohos.arkui.advanced.ComposeTitleBar.d.ets |
| 新增API | NA | 类名：ComposeTitleBarMenuItem；  API声明：action?: () => void;  差异内容：action?: () => void; | api/@ohos.arkui.advanced.ComposeTitleBar.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare struct ComposeTitleBar  差异内容： export declare struct ComposeTitleBar | api/@ohos.arkui.advanced.ComposeTitleBar.d.ets |
| 新增API | NA | 类名：ComposeTitleBar；  API声明：item?: ComposeTitleBarMenuItem;  差异内容：item?: ComposeTitleBarMenuItem; | api/@ohos.arkui.advanced.ComposeTitleBar.d.ets |
| 新增API | NA | 类名：ComposeTitleBar；  API声明：title: ResourceStr;  差异内容：title: ResourceStr; | api/@ohos.arkui.advanced.ComposeTitleBar.d.ets |
| 新增API | NA | 类名：ComposeTitleBar；  API声明：subtitle?: ResourceStr;  差异内容：subtitle?: ResourceStr; | api/@ohos.arkui.advanced.ComposeTitleBar.d.ets |
| 新增API | NA | 类名：ComposeTitleBar；  API声明：menuItems?: Array<ComposeTitleBarMenuItem>;  差异内容：menuItems?: Array<ComposeTitleBarMenuItem>; | api/@ohos.arkui.advanced.ComposeTitleBar.d.ets |
| 新增API | NA | 类名：global；  API声明： declare enum CounterType  差异内容： declare enum CounterType | api/@ohos.arkui.advanced.Counter.d.ets |
| 新增API | NA | 类名：CounterType；  API声明：LIST = 0  差异内容：LIST = 0 | api/@ohos.arkui.advanced.Counter.d.ets |
| 新增API | NA | 类名：CounterType；  API声明：COMPACT = 1  差异内容：COMPACT = 1 | api/@ohos.arkui.advanced.Counter.d.ets |
| 新增API | NA | 类名：CounterType；  API声明：INLINE = 2  差异内容：INLINE = 2 | api/@ohos.arkui.advanced.Counter.d.ets |
| 新增API | NA | 类名：CounterType；  API声明：INLINE\_DATE = 3  差异内容：INLINE\_DATE = 3 | api/@ohos.arkui.advanced.Counter.d.ets |
| 新增API | NA | 类名：global；  API声明： declare class CommonOptions  差异内容： declare class CommonOptions | api/@ohos.arkui.advanced.Counter.d.ets |
| 新增API | NA | 类名：CommonOptions；  API声明：focusable?: boolean;  差异内容：focusable?: boolean; | api/@ohos.arkui.advanced.Counter.d.ets |
| 新增API | NA | 类名：CommonOptions；  API声明：step?: number;  差异内容：step?: number; | api/@ohos.arkui.advanced.Counter.d.ets |
| 新增API | NA | 类名：CommonOptions；  API声明：onHoverIncrease?: (isHover: boolean) => void;  差异内容：onHoverIncrease?: (isHover: boolean) => void; | api/@ohos.arkui.advanced.Counter.d.ets |
| 新增API | NA | 类名：CommonOptions；  API声明：onHoverDecrease?: (isHover: boolean) => void;  差异内容：onHoverDecrease?: (isHover: boolean) => void; | api/@ohos.arkui.advanced.Counter.d.ets |
| 新增API | NA | 类名：global；  API声明： declare class InlineStyleOptions  差异内容： declare class InlineStyleOptions | api/@ohos.arkui.advanced.Counter.d.ets |
| 新增API | NA | 类名：InlineStyleOptions；  API声明：value?: number;  差异内容：value?: number; | api/@ohos.arkui.advanced.Counter.d.ets |
| 新增API | NA | 类名：InlineStyleOptions；  API声明：min?: number;  差异内容：min?: number; | api/@ohos.arkui.advanced.Counter.d.ets |
| 新增API | NA | 类名：InlineStyleOptions；  API声明：max?: number;  差异内容：max?: number; | api/@ohos.arkui.advanced.Counter.d.ets |
| 新增API | NA | 类名：InlineStyleOptions；  API声明：textWidth?: number;  差异内容：textWidth?: number; | api/@ohos.arkui.advanced.Counter.d.ets |
| 新增API | NA | 类名：InlineStyleOptions；  API声明：onChange?: (value: number) => void;  差异内容：onChange?: (value: number) => void; | api/@ohos.arkui.advanced.Counter.d.ets |
| 新增API | NA | 类名：global；  API声明： declare class NumberStyleOptions  差异内容： declare class NumberStyleOptions | api/@ohos.arkui.advanced.Counter.d.ets |
| 新增API | NA | 类名：NumberStyleOptions；  API声明：label?: ResourceStr;  差异内容：label?: ResourceStr; | api/@ohos.arkui.advanced.Counter.d.ets |
| 新增API | NA | 类名：NumberStyleOptions；  API声明：onFocusIncrease?: () => void;  差异内容：onFocusIncrease?: () => void; | api/@ohos.arkui.advanced.Counter.d.ets |
| 新增API | NA | 类名：NumberStyleOptions；  API声明：onFocusDecrease?: () => void;  差异内容：onFocusDecrease?: () => void; | api/@ohos.arkui.advanced.Counter.d.ets |
| 新增API | NA | 类名：NumberStyleOptions；  API声明：onBlurIncrease?: () => void;  差异内容：onBlurIncrease?: () => void; | api/@ohos.arkui.advanced.Counter.d.ets |
| 新增API | NA | 类名：NumberStyleOptions；  API声明：onBlurDecrease?: () => void;  差异内容：onBlurDecrease?: () => void; | api/@ohos.arkui.advanced.Counter.d.ets |
| 新增API | NA | 类名：global；  API声明： declare class DateData  差异内容： declare class DateData | api/@ohos.arkui.advanced.Counter.d.ets |
| 新增API | NA | 类名：DateData；  API声明：year: number;  差异内容：year: number; | api/@ohos.arkui.advanced.Counter.d.ets |
| 新增API | NA | 类名：DateData；  API声明：month: number;  差异内容：month: number; | api/@ohos.arkui.advanced.Counter.d.ets |
| 新增API | NA | 类名：DateData；  API声明：day: number;  差异内容：day: number; | api/@ohos.arkui.advanced.Counter.d.ets |
| 新增API | NA | 类名：DateData；  API声明：toString(): string;  差异内容：toString(): string; | api/@ohos.arkui.advanced.Counter.d.ets |
| 新增API | NA | 类名：global；  API声明： declare class DateStyleOptions  差异内容： declare class DateStyleOptions | api/@ohos.arkui.advanced.Counter.d.ets |
| 新增API | NA | 类名：DateStyleOptions；  API声明：year?: number;  差异内容：year?: number; | api/@ohos.arkui.advanced.Counter.d.ets |
| 新增API | NA | 类名：DateStyleOptions；  API声明：month?: number;  差异内容：month?: number; | api/@ohos.arkui.advanced.Counter.d.ets |
| 新增API | NA | 类名：DateStyleOptions；  API声明：day?: number;  差异内容：day?: number; | api/@ohos.arkui.advanced.Counter.d.ets |
| 新增API | NA | 类名：DateStyleOptions；  API声明：onDateChange?: (date: DateData) => void;  差异内容：onDateChange?: (date: DateData) => void; | api/@ohos.arkui.advanced.Counter.d.ets |
| 新增API | NA | 类名：global；  API声明： declare class CounterOptions  差异内容： declare class CounterOptions | api/@ohos.arkui.advanced.Counter.d.ets |
| 新增API | NA | 类名：CounterOptions；  API声明：type: CounterType;  差异内容：type: CounterType; | api/@ohos.arkui.advanced.Counter.d.ets |
| 新增API | NA | 类名：CounterOptions；  API声明：numberOptions?: NumberStyleOptions;  差异内容：numberOptions?: NumberStyleOptions; | api/@ohos.arkui.advanced.Counter.d.ets |
| 新增API | NA | 类名：CounterOptions；  API声明：inlineOptions?: InlineStyleOptions;  差异内容：inlineOptions?: InlineStyleOptions; | api/@ohos.arkui.advanced.Counter.d.ets |
| 新增API | NA | 类名：CounterOptions；  API声明：dateOptions?: DateStyleOptions;  差异内容：dateOptions?: DateStyleOptions; | api/@ohos.arkui.advanced.Counter.d.ets |
| 新增API | NA | 类名：global；  API声明： declare struct CounterComponent  差异内容： declare struct CounterComponent | api/@ohos.arkui.advanced.Counter.d.ets |
| 新增API | NA | 类名：CounterComponent；  API声明：@Prop  options: CounterOptions;  差异内容：@Prop  options: CounterOptions; | api/@ohos.arkui.advanced.Counter.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare class ButtonOptions  差异内容： export declare class ButtonOptions | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：ButtonOptions；  API声明：value: ResourceStr;  差异内容：value: ResourceStr; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：ButtonOptions；  API声明：action?: () => void;  差异内容：action?: () => void; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：ButtonOptions；  API声明：background?: ResourceColor;  差异内容：background?: ResourceColor; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：ButtonOptions；  API声明：fontColor?: ResourceColor;  差异内容：fontColor?: ResourceColor; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：ButtonOptions；  API声明：buttonStyle?: ButtonStyleMode;  差异内容：buttonStyle?: ButtonStyleMode; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：ButtonOptions；  API声明：role?: ButtonRole;  差异内容：role?: ButtonRole; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare struct TipsDialog  差异内容： export declare struct TipsDialog | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：TipsDialog；  API声明：controller: CustomDialogController;  差异内容：controller: CustomDialogController; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：TipsDialog；  API声明：imageRes: Resource;  差异内容：imageRes: Resource; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：TipsDialog；  API声明：imageSize?: SizeOptions;  差异内容：imageSize?: SizeOptions; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：TipsDialog；  API声明：title?: ResourceStr;  差异内容：title?: ResourceStr; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：TipsDialog；  API声明：content?: ResourceStr;  差异内容：content?: ResourceStr; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：TipsDialog；  API声明：checkTips?: ResourceStr;  差异内容：checkTips?: ResourceStr; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：TipsDialog；  API声明：@Prop  isChecked?: boolean;  差异内容：@Prop  isChecked?: boolean; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：TipsDialog；  API声明：checkAction?: (isChecked: boolean) => void;  差异内容：checkAction?: (isChecked: boolean) => void; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：TipsDialog；  API声明：primaryButton?: ButtonOptions;  差异内容：primaryButton?: ButtonOptions; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：TipsDialog；  API声明：secondaryButton?: ButtonOptions;  差异内容：secondaryButton?: ButtonOptions; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：TipsDialog；  API声明：theme?: Theme | CustomTheme;  差异内容：theme?: Theme | CustomTheme; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare struct SelectDialog  差异内容： export declare struct SelectDialog | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：SelectDialog；  API声明：controller: CustomDialogController;  差异内容：controller: CustomDialogController; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：SelectDialog；  API声明：title: ResourceStr;  差异内容：title: ResourceStr; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：SelectDialog；  API声明：content?: ResourceStr;  差异内容：content?: ResourceStr; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：SelectDialog；  API声明：selectedIndex?: number;  差异内容：selectedIndex?: number; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：SelectDialog；  API声明：confirm?: ButtonOptions;  差异内容：confirm?: ButtonOptions; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：SelectDialog；  API声明：radioContent: Array<SheetInfo>;  差异内容：radioContent: Array<SheetInfo>; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：SelectDialog；  API声明：theme?: Theme | CustomTheme;  差异内容：theme?: Theme | CustomTheme; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare struct ConfirmDialog  差异内容： export declare struct ConfirmDialog | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：ConfirmDialog；  API声明：controller: CustomDialogController;  差异内容：controller: CustomDialogController; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：ConfirmDialog；  API声明：title: ResourceStr;  差异内容：title: ResourceStr; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：ConfirmDialog；  API声明：content?: ResourceStr;  差异内容：content?: ResourceStr; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：ConfirmDialog；  API声明：checkTips?: ResourceStr;  差异内容：checkTips?: ResourceStr; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：ConfirmDialog；  API声明：@Prop  isChecked?: boolean;  差异内容：@Prop  isChecked?: boolean; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：ConfirmDialog；  API声明：primaryButton?: ButtonOptions;  差异内容：primaryButton?: ButtonOptions; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：ConfirmDialog；  API声明：secondaryButton?: ButtonOptions;  差异内容：secondaryButton?: ButtonOptions; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：ConfirmDialog；  API声明：theme?: Theme | CustomTheme;  差异内容：theme?: Theme | CustomTheme; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare struct AlertDialog  差异内容： export declare struct AlertDialog | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：AlertDialog；  API声明：controller: CustomDialogController;  差异内容：controller: CustomDialogController; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：AlertDialog；  API声明：primaryTitle?: ResourceStr;  差异内容：primaryTitle?: ResourceStr; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：AlertDialog；  API声明：secondaryTitle?: ResourceStr;  差异内容：secondaryTitle?: ResourceStr; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：AlertDialog；  API声明：content: ResourceStr;  差异内容：content: ResourceStr; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：AlertDialog；  API声明：primaryButton?: ButtonOptions;  差异内容：primaryButton?: ButtonOptions; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：AlertDialog；  API声明：secondaryButton?: ButtonOptions;  差异内容：secondaryButton?: ButtonOptions; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：AlertDialog；  API声明：theme?: Theme | CustomTheme;  差异内容：theme?: Theme | CustomTheme; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare struct LoadingDialog  差异内容： export declare struct LoadingDialog | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：LoadingDialog；  API声明：Controller: CustomDialogController;  差异内容：Controller: CustomDialogController; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：LoadingDialog；  API声明：content?: ResourceStr;  差异内容：content?: ResourceStr; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：LoadingDialog；  API声明：theme?: Theme | CustomTheme;  差异内容：theme?: Theme | CustomTheme; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare struct CustomContentDialog  差异内容： export declare struct CustomContentDialog | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：CustomContentDialog；  API声明：controller: CustomDialogController;  差异内容：controller: CustomDialogController; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：CustomContentDialog；  API声明：primaryTitle?: ResourceStr;  差异内容：primaryTitle?: ResourceStr; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：CustomContentDialog；  API声明：secondaryTitle?: ResourceStr;  差异内容：secondaryTitle?: ResourceStr; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：CustomContentDialog；  API声明：@BuilderParam  contentBuilder: () => void;  差异内容：@BuilderParam  contentBuilder: () => void; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：CustomContentDialog；  API声明：contentAreaPadding?: Padding;  差异内容：contentAreaPadding?: Padding; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：CustomContentDialog；  API声明：buttons?: ButtonOptions[];  差异内容：buttons?: ButtonOptions[]; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：CustomContentDialog；  API声明：theme?: Theme | CustomTheme;  差异内容：theme?: Theme | CustomTheme; | api/@ohos.arkui.advanced.Dialog.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare enum DownloadIconStyle  差异内容： export declare enum DownloadIconStyle | api/@ohos.arkui.advanced.DownloadFileButton.d.ets |
| 新增API | NA | 类名：DownloadIconStyle；  API声明：FULL\_FILLED = 1  差异内容：FULL\_FILLED = 1 | api/@ohos.arkui.advanced.DownloadFileButton.d.ets |
| 新增API | NA | 类名：DownloadIconStyle；  API声明：LINES = 2  差异内容：LINES = 2 | api/@ohos.arkui.advanced.DownloadFileButton.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare enum DownloadDescription  差异内容： export declare enum DownloadDescription | api/@ohos.arkui.advanced.DownloadFileButton.d.ets |
| 新增API | NA | 类名：DownloadDescription；  API声明：DOWNLOAD = 1  差异内容：DOWNLOAD = 1 | api/@ohos.arkui.advanced.DownloadFileButton.d.ets |
| 新增API | NA | 类名：DownloadDescription；  API声明：DOWNLOAD\_FILE = 2  差异内容：DOWNLOAD\_FILE = 2 | api/@ohos.arkui.advanced.DownloadFileButton.d.ets |
| 新增API | NA | 类名：DownloadDescription；  API声明：SAVE = 3  差异内容：SAVE = 3 | api/@ohos.arkui.advanced.DownloadFileButton.d.ets |
| 新增API | NA | 类名：DownloadDescription；  API声明：SAVE\_IMAGE = 4  差异内容：SAVE\_IMAGE = 4 | api/@ohos.arkui.advanced.DownloadFileButton.d.ets |
| 新增API | NA | 类名：DownloadDescription；  API声明：SAVE\_FILE = 5  差异内容：SAVE\_FILE = 5 | api/@ohos.arkui.advanced.DownloadFileButton.d.ets |
| 新增API | NA | 类名：DownloadDescription；  API声明：DOWNLOAD\_AND\_SHARE = 6  差异内容：DOWNLOAD\_AND\_SHARE = 6 | api/@ohos.arkui.advanced.DownloadFileButton.d.ets |
| 新增API | NA | 类名：DownloadDescription；  API声明：RECEIVE = 7  差异内容：RECEIVE = 7 | api/@ohos.arkui.advanced.DownloadFileButton.d.ets |
| 新增API | NA | 类名：DownloadDescription；  API声明：CONTINUE\_TO\_RECEIVE = 8  差异内容：CONTINUE\_TO\_RECEIVE = 8 | api/@ohos.arkui.advanced.DownloadFileButton.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare enum DownloadLayoutDirection  差异内容： export declare enum DownloadLayoutDirection | api/@ohos.arkui.advanced.DownloadFileButton.d.ets |
| 新增API | NA | 类名：DownloadLayoutDirection；  API声明：HORIZONTAL = 0  差异内容：HORIZONTAL = 0 | api/@ohos.arkui.advanced.DownloadFileButton.d.ets |
| 新增API | NA | 类名：DownloadLayoutDirection；  API声明：VERTICAL = 1  差异内容：VERTICAL = 1 | api/@ohos.arkui.advanced.DownloadFileButton.d.ets |
| 新增API | NA | 类名：global；  API声明： export interface DownloadContentOptions  差异内容： export interface DownloadContentOptions | api/@ohos.arkui.advanced.DownloadFileButton.d.ets |
| 新增API | NA | 类名：DownloadContentOptions；  API声明：icon?: DownloadIconStyle;  差异内容：icon?: DownloadIconStyle; | api/@ohos.arkui.advanced.DownloadFileButton.d.ets |
| 新增API | NA | 类名：DownloadContentOptions；  API声明：text?: DownloadDescription;  差异内容：text?: DownloadDescription; | api/@ohos.arkui.advanced.DownloadFileButton.d.ets |
| 新增API | NA | 类名：global；  API声明： export interface DownloadStyleOptions  差异内容： export interface DownloadStyleOptions | api/@ohos.arkui.advanced.DownloadFileButton.d.ets |
| 新增API | NA | 类名：DownloadStyleOptions；  API声明：iconSize?: Dimension;  差异内容：iconSize?: Dimension; | api/@ohos.arkui.advanced.DownloadFileButton.d.ets |
| 新增API | NA | 类名：DownloadStyleOptions；  API声明：layoutDirection?: DownloadLayoutDirection;  差异内容：layoutDirection?: DownloadLayoutDirection; | api/@ohos.arkui.advanced.DownloadFileButton.d.ets |
| 新增API | NA | 类名：DownloadStyleOptions；  API声明：fontSize?: Dimension;  差异内容：fontSize?: Dimension; | api/@ohos.arkui.advanced.DownloadFileButton.d.ets |
| 新增API | NA | 类名：DownloadStyleOptions；  API声明：fontStyle?: FontStyle;  差异内容：fontStyle?: FontStyle; | api/@ohos.arkui.advanced.DownloadFileButton.d.ets |
| 新增API | NA | 类名：DownloadStyleOptions；  API声明：fontWeight?: number | FontWeight | string;  差异内容：fontWeight?: number | FontWeight | string; | api/@ohos.arkui.advanced.DownloadFileButton.d.ets |
| 新增API | NA | 类名：DownloadStyleOptions；  API声明：fontFamily?: string | Resource;  差异内容：fontFamily?: string | Resource; | api/@ohos.arkui.advanced.DownloadFileButton.d.ets |
| 新增API | NA | 类名：DownloadStyleOptions；  API声明：fontColor?: ResourceColor;  差异内容：fontColor?: ResourceColor; | api/@ohos.arkui.advanced.DownloadFileButton.d.ets |
| 新增API | NA | 类名：DownloadStyleOptions；  API声明：iconColor?: ResourceColor;  差异内容：iconColor?: ResourceColor; | api/@ohos.arkui.advanced.DownloadFileButton.d.ets |
| 新增API | NA | 类名：DownloadStyleOptions；  API声明：textIconSpace?: Dimension;  差异内容：textIconSpace?: Dimension; | api/@ohos.arkui.advanced.DownloadFileButton.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare struct DownloadFileButton  差异内容： export declare struct DownloadFileButton | api/@ohos.arkui.advanced.DownloadFileButton.d.ets |
| 新增API | NA | 类名：DownloadFileButton；  API声明：@State  contentOptions: DownloadContentOptions;  差异内容：@State  contentOptions: DownloadContentOptions; | api/@ohos.arkui.advanced.DownloadFileButton.d.ets |
| 新增API | NA | 类名：DownloadFileButton；  API声明：@State  styleOptions: DownloadStyleOptions;  差异内容：@State  styleOptions: DownloadStyleOptions; | api/@ohos.arkui.advanced.DownloadFileButton.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare class EditableTitleBarMenuItem  差异内容： export declare class EditableTitleBarMenuItem | api/@ohos.arkui.advanced.EditableTitleBar.d.ets |
| 新增API | NA | 类名：EditableTitleBarMenuItem；  API声明：value: ResourceStr;  差异内容：value: ResourceStr; | api/@ohos.arkui.advanced.EditableTitleBar.d.ets |
| 新增API | NA | 类名：EditableTitleBarMenuItem；  API声明：isEnabled?: boolean;  差异内容：isEnabled?: boolean; | api/@ohos.arkui.advanced.EditableTitleBar.d.ets |
| 新增API | NA | 类名：EditableTitleBarMenuItem；  API声明：action?: () => void;  差异内容：action?: () => void; | api/@ohos.arkui.advanced.EditableTitleBar.d.ets |
| 新增API | NA | 类名：global；  API声明：export type EditableTitleBarItem = EditableTitleBarMenuItem;  差异内容：export type EditableTitleBarItem = EditableTitleBarMenuItem; | api/@ohos.arkui.advanced.EditableTitleBar.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare enum EditableLeftIconType  差异内容： export declare enum EditableLeftIconType | api/@ohos.arkui.advanced.EditableTitleBar.d.ets |
| 新增API | NA | 类名：EditableLeftIconType；  API声明：Back = 0  差异内容：Back = 0 | api/@ohos.arkui.advanced.EditableTitleBar.d.ets |
| 新增API | NA | 类名：EditableLeftIconType；  API声明：Cancel = 1  差异内容：Cancel = 1 | api/@ohos.arkui.advanced.EditableTitleBar.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare interface EditableTitleBarOptions  差异内容： export declare interface EditableTitleBarOptions | api/@ohos.arkui.advanced.EditableTitleBar.d.ets |
| 新增API | NA | 类名：EditableTitleBarOptions；  API声明：backgroundColor?: ResourceColor;  差异内容：backgroundColor?: ResourceColor; | api/@ohos.arkui.advanced.EditableTitleBar.d.ets |
| 新增API | NA | 类名：EditableTitleBarOptions；  API声明：backgroundBlurStyle?: BlurStyle;  差异内容：backgroundBlurStyle?: BlurStyle; | api/@ohos.arkui.advanced.EditableTitleBar.d.ets |
| 新增API | NA | 类名：EditableTitleBarOptions；  API声明：safeAreaTypes?: Array<SafeAreaType>;  差异内容：safeAreaTypes?: Array<SafeAreaType>; | api/@ohos.arkui.advanced.EditableTitleBar.d.ets |
| 新增API | NA | 类名：EditableTitleBarOptions；  API声明：safeAreaEdges?: Array<SafeAreaEdge>;  差异内容：safeAreaEdges?: Array<SafeAreaEdge>; | api/@ohos.arkui.advanced.EditableTitleBar.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare struct EditableTitleBar  差异内容： export declare struct EditableTitleBar | api/@ohos.arkui.advanced.EditableTitleBar.d.ets |
| 新增API | NA | 类名：EditableTitleBar；  API声明：leftIconStyle: EditableLeftIconType;  差异内容：leftIconStyle: EditableLeftIconType; | api/@ohos.arkui.advanced.EditableTitleBar.d.ets |
| 新增API | NA | 类名：EditableTitleBar；  API声明：imageItem?: EditableTitleBarItem;  差异内容：imageItem?: EditableTitleBarItem; | api/@ohos.arkui.advanced.EditableTitleBar.d.ets |
| 新增API | NA | 类名：EditableTitleBar；  API声明：title: ResourceStr;  差异内容：title: ResourceStr; | api/@ohos.arkui.advanced.EditableTitleBar.d.ets |
| 新增API | NA | 类名：EditableTitleBar；  API声明：subtitle?: ResourceStr;  差异内容：subtitle?: ResourceStr; | api/@ohos.arkui.advanced.EditableTitleBar.d.ets |
| 新增API | NA | 类名：EditableTitleBar；  API声明：isSaveIconRequired: boolean;  差异内容：isSaveIconRequired: boolean; | api/@ohos.arkui.advanced.EditableTitleBar.d.ets |
| 新增API | NA | 类名：EditableTitleBar；  API声明：menuItems?: Array<EditableTitleBarMenuItem>;  差异内容：menuItems?: Array<EditableTitleBarMenuItem>; | api/@ohos.arkui.advanced.EditableTitleBar.d.ets |
| 新增API | NA | 类名：EditableTitleBar；  API声明：onSave?: () => void;  差异内容：onSave?: () => void; | api/@ohos.arkui.advanced.EditableTitleBar.d.ets |
| 新增API | NA | 类名：EditableTitleBar；  API声明：onCancel?: () => void;  差异内容：onCancel?: () => void; | api/@ohos.arkui.advanced.EditableTitleBar.d.ets |
| 新增API | NA | 类名：EditableTitleBar；  API声明：options: EditableTitleBarOptions;  差异内容：options: EditableTitleBarOptions; | api/@ohos.arkui.advanced.EditableTitleBar.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare enum MarginType  差异内容： export declare enum MarginType | api/@ohos.arkui.advanced.ExceptionPrompt.d.ets |
| 新增API | NA | 类名：MarginType；  API声明：DEFAULT\_MARGIN = 0  差异内容：DEFAULT\_MARGIN = 0 | api/@ohos.arkui.advanced.ExceptionPrompt.d.ets |
| 新增API | NA | 类名：MarginType；  API声明：FIT\_MARGIN = 1  差异内容：FIT\_MARGIN = 1 | api/@ohos.arkui.advanced.ExceptionPrompt.d.ets |
| 新增API | NA | 类名：global；  API声明： export interface PromptOptions  差异内容： export interface PromptOptions | api/@ohos.arkui.advanced.ExceptionPrompt.d.ets |
| 新增API | NA | 类名：PromptOptions；  API声明：icon?: ResourceStr;  差异内容：icon?: ResourceStr; | api/@ohos.arkui.advanced.ExceptionPrompt.d.ets |
| 新增API | NA | 类名：PromptOptions；  API声明：tip?: ResourceStr;  差异内容：tip?: ResourceStr; | api/@ohos.arkui.advanced.ExceptionPrompt.d.ets |
| 新增API | NA | 类名：PromptOptions；  API声明：marginType: MarginType;  差异内容：marginType: MarginType; | api/@ohos.arkui.advanced.ExceptionPrompt.d.ets |
| 新增API | NA | 类名：PromptOptions；  API声明：actionText?: ResourceStr;  差异内容：actionText?: ResourceStr; | api/@ohos.arkui.advanced.ExceptionPrompt.d.ets |
| 新增API | NA | 类名：PromptOptions；  API声明：marginTop: Dimension;  差异内容：marginTop: Dimension; | api/@ohos.arkui.advanced.ExceptionPrompt.d.ets |
| 新增API | NA | 类名：PromptOptions；  API声明：isShown?: boolean;  差异内容：isShown?: boolean; | api/@ohos.arkui.advanced.ExceptionPrompt.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare struct ExceptionPrompt  差异内容： export declare struct ExceptionPrompt | api/@ohos.arkui.advanced.ExceptionPrompt.d.ets |
| 新增API | NA | 类名：ExceptionPrompt；  API声明：@Prop  options: PromptOptions;  差异内容：@Prop  options: PromptOptions; | api/@ohos.arkui.advanced.ExceptionPrompt.d.ets |
| 新增API | NA | 类名：ExceptionPrompt；  API声明：onTipClick?: () => void;  差异内容：onTipClick?: () => void; | api/@ohos.arkui.advanced.ExceptionPrompt.d.ets |
| 新增API | NA | 类名：ExceptionPrompt；  API声明：onActionTextClick?: () => void;  差异内容：onActionTextClick?: () => void; | api/@ohos.arkui.advanced.ExceptionPrompt.d.ets |
| 新增API | NA | 类名：ExceptionPrompt；  API声明：build(): void;  差异内容：build(): void; | api/@ohos.arkui.advanced.ExceptionPrompt.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare enum FilterType  差异内容： export declare enum FilterType | api/@ohos.arkui.advanced.Filter.d.ets |
| 新增API | NA | 类名：FilterType；  API声明：MULTI\_LINE\_FILTER = 0  差异内容：MULTI\_LINE\_FILTER = 0 | api/@ohos.arkui.advanced.Filter.d.ets |
| 新增API | NA | 类名：FilterType；  API声明：LIST\_FILTER = 1  差异内容：LIST\_FILTER = 1 | api/@ohos.arkui.advanced.Filter.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare class FilterParams  差异内容： export declare class FilterParams | api/@ohos.arkui.advanced.Filter.d.ets |
| 新增API | NA | 类名：FilterParams；  API声明：name: ResourceStr;  差异内容：name: ResourceStr; | api/@ohos.arkui.advanced.Filter.d.ets |
| 新增API | NA | 类名：FilterParams；  API声明：options: Array<ResourceStr>;  差异内容：options: Array<ResourceStr>; | api/@ohos.arkui.advanced.Filter.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare class FilterResult  差异内容： export declare class FilterResult | api/@ohos.arkui.advanced.Filter.d.ets |
| 新增API | NA | 类名：FilterResult；  API声明：name: ResourceStr;  差异内容：name: ResourceStr; | api/@ohos.arkui.advanced.Filter.d.ets |
| 新增API | NA | 类名：FilterResult；  API声明：index: number;  差异内容：index: number; | api/@ohos.arkui.advanced.Filter.d.ets |
| 新增API | NA | 类名：FilterResult；  API声明：value: ResourceStr;  差异内容：value: ResourceStr; | api/@ohos.arkui.advanced.Filter.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare struct Filter  差异内容： export declare struct Filter | api/@ohos.arkui.advanced.Filter.d.ets |
| 新增API | NA | 类名：Filter；  API声明：@BuilderParam  container: () => void;  差异内容：@BuilderParam  container: () => void; | api/@ohos.arkui.advanced.Filter.d.ets |
| 新增API | NA | 类名：Filter；  API声明：@Prop  multiFilters: Array<FilterParams>;  差异内容：@Prop  multiFilters: Array<FilterParams>; | api/@ohos.arkui.advanced.Filter.d.ets |
| 新增API | NA | 类名：Filter；  API声明：@Prop  additionFilters?: FilterParams;  差异内容：@Prop  additionFilters?: FilterParams; | api/@ohos.arkui.advanced.Filter.d.ets |
| 新增API | NA | 类名：Filter；  API声明：onFilterChanged: (filterResults: Array<FilterResult>) => void;  差异内容：onFilterChanged: (filterResults: Array<FilterResult>) => void; | api/@ohos.arkui.advanced.Filter.d.ets |
| 新增API | NA | 类名：Filter；  API声明：@Prop  filterType?: FilterType;  差异内容：@Prop  filterType?: FilterType; | api/@ohos.arkui.advanced.Filter.d.ets |
| 新增API | NA | 类名：global；  API声明： export interface FormMenuItemStyle  差异内容： export interface FormMenuItemStyle | api/@ohos.arkui.advanced.FormMenu.d.ets |
| 新增API | NA | 类名：FormMenuItemStyle；  API声明：options?: MenuItemOptions;  差异内容：options?: MenuItemOptions; | api/@ohos.arkui.advanced.FormMenu.d.ets |
| 新增API | NA | 类名：global；  API声明： export interface AddFormOptions  差异内容： export interface AddFormOptions | api/@ohos.arkui.advanced.FormMenu.d.ets |
| 新增API | NA | 类名：AddFormOptions；  API声明：formBindingData?: formBindingData.FormBindingData;  差异内容：formBindingData?: formBindingData.FormBindingData; | api/@ohos.arkui.advanced.FormMenu.d.ets |
| 新增API | NA | 类名：AddFormOptions；  API声明：callback?: AsyncCallback<string>;  差异内容：callback?: AsyncCallback<string>; | api/@ohos.arkui.advanced.FormMenu.d.ets |
| 新增API | NA | 类名：AddFormOptions；  API声明：style?: FormMenuItemStyle;  差异内容：style?: FormMenuItemStyle; | api/@ohos.arkui.advanced.FormMenu.d.ets |
| 新增API | NA | 类名：global；  API声明：@Builder  export declare function AddFormMenuItem(want: Want, componentId: string, options?: AddFormOptions): void;  差异内容：@Builder  export declare function AddFormMenuItem(want: Want, componentId: string, options?: AddFormOptions): void; | api/@ohos.arkui.advanced.FormMenu.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare struct FullScreenLaunchComponent  差异内容： export declare struct FullScreenLaunchComponent | api/@ohos.arkui.advanced.FullScreenLaunchComponent.d.ets |
| 新增API | NA | 类名：FullScreenLaunchComponent；  API声明：@BuilderParam  content: Callback<void>;  差异内容：@BuilderParam  content: Callback<void>; | api/@ohos.arkui.advanced.FullScreenLaunchComponent.d.ets |
| 新增API | NA | 类名：FullScreenLaunchComponent；  API声明：appId: string;  差异内容：appId: string; | api/@ohos.arkui.advanced.FullScreenLaunchComponent.d.ets |
| 新增API | NA | 类名：FullScreenLaunchComponent；  API声明：options?: AtomicServiceOptions;  差异内容：options?: AtomicServiceOptions; | api/@ohos.arkui.advanced.FullScreenLaunchComponent.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare enum GridObjectSortComponentType  差异内容： export declare enum GridObjectSortComponentType | api/@ohos.arkui.advanced.GridObjectSortComponent.d.ets |
| 新增API | NA | 类名：GridObjectSortComponentType；  API声明：IMAGE\_TEXT = "image\_text"  差异内容：IMAGE\_TEXT = "image\_text" | api/@ohos.arkui.advanced.GridObjectSortComponent.d.ets |
| 新增API | NA | 类名：GridObjectSortComponentType；  API声明：TEXT = "text"  差异内容：TEXT = "text" | api/@ohos.arkui.advanced.GridObjectSortComponent.d.ets |
| 新增API | NA | 类名：global；  API声明： export interface GridObjectSortComponentItem  差异内容： export interface GridObjectSortComponentItem | api/@ohos.arkui.advanced.GridObjectSortComponent.d.ets |
| 新增API | NA | 类名：GridObjectSortComponentItem；  API声明：id: number | string;  差异内容：id: number | string; | api/@ohos.arkui.advanced.GridObjectSortComponent.d.ets |
| 新增API | NA | 类名：GridObjectSortComponentItem；  API声明：text: ResourceStr;  差异内容：text: ResourceStr; | api/@ohos.arkui.advanced.GridObjectSortComponent.d.ets |
| 新增API | NA | 类名：GridObjectSortComponentItem；  API声明：selected: boolean;  差异内容：selected: boolean; | api/@ohos.arkui.advanced.GridObjectSortComponent.d.ets |
| 新增API | NA | 类名：GridObjectSortComponentItem；  API声明：order: number;  差异内容：order: number; | api/@ohos.arkui.advanced.GridObjectSortComponent.d.ets |
| 新增API | NA | 类名：GridObjectSortComponentItem；  API声明：url?: ResourceStr;  差异内容：url?: ResourceStr; | api/@ohos.arkui.advanced.GridObjectSortComponent.d.ets |
| 新增API | NA | 类名：global；  API声明： export interface GridObjectSortComponentOptions  差异内容： export interface GridObjectSortComponentOptions | api/@ohos.arkui.advanced.GridObjectSortComponent.d.ets |
| 新增API | NA | 类名：GridObjectSortComponentOptions；  API声明：type?: GridObjectSortComponentType;  差异内容：type?: GridObjectSortComponentType; | api/@ohos.arkui.advanced.GridObjectSortComponent.d.ets |
| 新增API | NA | 类名：GridObjectSortComponentOptions；  API声明：imageSize?: number | Resource;  差异内容：imageSize?: number | Resource; | api/@ohos.arkui.advanced.GridObjectSortComponent.d.ets |
| 新增API | NA | 类名：GridObjectSortComponentOptions；  API声明：normalTitle?: ResourceStr;  差异内容：normalTitle?: ResourceStr; | api/@ohos.arkui.advanced.GridObjectSortComponent.d.ets |
| 新增API | NA | 类名：GridObjectSortComponentOptions；  API声明：editTitle?: ResourceStr;  差异内容：editTitle?: ResourceStr; | api/@ohos.arkui.advanced.GridObjectSortComponent.d.ets |
| 新增API | NA | 类名：GridObjectSortComponentOptions；  API声明：showAreaTitle?: ResourceStr;  差异内容：showAreaTitle?: ResourceStr; | api/@ohos.arkui.advanced.GridObjectSortComponent.d.ets |
| 新增API | NA | 类名：GridObjectSortComponentOptions；  API声明：addAreaTitle?: ResourceStr;  差异内容：addAreaTitle?: ResourceStr; | api/@ohos.arkui.advanced.GridObjectSortComponent.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare struct GridObjectSortComponent  差异内容： export declare struct GridObjectSortComponent | api/@ohos.arkui.advanced.GridObjectSortComponent.d.ets |
| 新增API | NA | 类名：GridObjectSortComponent；  API声明：@Prop  options: GridObjectSortComponentOptions;  差异内容：@Prop  options: GridObjectSortComponentOptions; | api/@ohos.arkui.advanced.GridObjectSortComponent.d.ets |
| 新增API | NA | 类名：GridObjectSortComponent；  API声明：dataList: Array<GridObjectSortComponentItem>;  差异内容：dataList: Array<GridObjectSortComponentItem>; | api/@ohos.arkui.advanced.GridObjectSortComponent.d.ets |
| 新增API | NA | 类名：GridObjectSortComponent；  API声明：onSave: (select: Array<GridObjectSortComponentItem>, unselect: Array<GridObjectSortComponentItem>) => void;  差异内容：onSave: (select: Array<GridObjectSortComponentItem>, unselect: Array<GridObjectSortComponentItem>) => void; | api/@ohos.arkui.advanced.GridObjectSortComponent.d.ets |
| 新增API | NA | 类名：GridObjectSortComponent；  API声明：onCancel: () => void;  差异内容：onCancel: () => void; | api/@ohos.arkui.advanced.GridObjectSortComponent.d.ets |
| 新增API | NA | 类名：GridObjectSortComponent；  API声明：build(): void;  差异内容：build(): void; | api/@ohos.arkui.advanced.GridObjectSortComponent.d.ets |
| 新增API | NA | 类名：global；  API声明： export interface PopupTextOptions  差异内容： export interface PopupTextOptions | api/@ohos.arkui.advanced.Popup.d.ets |
| 新增API | NA | 类名：PopupTextOptions；  API声明：text: ResourceStr;  差异内容：text: ResourceStr; | api/@ohos.arkui.advanced.Popup.d.ets |
| 新增API | NA | 类名：PopupTextOptions；  API声明：fontSize?: number | string | Resource;  差异内容：fontSize?: number | string | Resource; | api/@ohos.arkui.advanced.Popup.d.ets |
| 新增API | NA | 类名：PopupTextOptions；  API声明：fontColor?: ResourceColor;  差异内容：fontColor?: ResourceColor; | api/@ohos.arkui.advanced.Popup.d.ets |
| 新增API | NA | 类名：PopupTextOptions；  API声明：fontWeight?: number | FontWeight | string;  差异内容：fontWeight?: number | FontWeight | string; | api/@ohos.arkui.advanced.Popup.d.ets |
| 新增API | NA | 类名：global；  API声明： export interface PopupButtonOptions  差异内容： export interface PopupButtonOptions | api/@ohos.arkui.advanced.Popup.d.ets |
| 新增API | NA | 类名：PopupButtonOptions；  API声明：text: ResourceStr;  差异内容：text: ResourceStr; | api/@ohos.arkui.advanced.Popup.d.ets |
| 新增API | NA | 类名：PopupButtonOptions；  API声明：action?: () => void;  差异内容：action?: () => void; | api/@ohos.arkui.advanced.Popup.d.ets |
| 新增API | NA | 类名：PopupButtonOptions；  API声明：fontSize?: number | string | Resource;  差异内容：fontSize?: number | string | Resource; | api/@ohos.arkui.advanced.Popup.d.ets |
| 新增API | NA | 类名：PopupButtonOptions；  API声明：fontColor?: ResourceColor;  差异内容：fontColor?: ResourceColor; | api/@ohos.arkui.advanced.Popup.d.ets |
| 新增API | NA | 类名：global；  API声明： export interface PopupIconOptions  差异内容： export interface PopupIconOptions | api/@ohos.arkui.advanced.Popup.d.ets |
| 新增API | NA | 类名：PopupIconOptions；  API声明：image: ResourceStr;  差异内容：image: ResourceStr; | api/@ohos.arkui.advanced.Popup.d.ets |
| 新增API | NA | 类名：PopupIconOptions；  API声明：width?: Dimension;  差异内容：width?: Dimension; | api/@ohos.arkui.advanced.Popup.d.ets |
| 新增API | NA | 类名：PopupIconOptions；  API声明：height?: Dimension;  差异内容：height?: Dimension; | api/@ohos.arkui.advanced.Popup.d.ets |
| 新增API | NA | 类名：PopupIconOptions；  API声明：fillColor?: ResourceColor;  差异内容：fillColor?: ResourceColor; | api/@ohos.arkui.advanced.Popup.d.ets |
| 新增API | NA | 类名：PopupIconOptions；  API声明：borderRadius?: Length | BorderRadiuses;  差异内容：borderRadius?: Length | BorderRadiuses; | api/@ohos.arkui.advanced.Popup.d.ets |
| 新增API | NA | 类名：global；  API声明： export interface PopupOptions  差异内容： export interface PopupOptions | api/@ohos.arkui.advanced.Popup.d.ets |
| 新增API | NA | 类名：PopupOptions；  API声明：icon?: PopupIconOptions;  差异内容：icon?: PopupIconOptions; | api/@ohos.arkui.advanced.Popup.d.ets |
| 新增API | NA | 类名：PopupOptions；  API声明：title?: PopupTextOptions;  差异内容：title?: PopupTextOptions; | api/@ohos.arkui.advanced.Popup.d.ets |
| 新增API | NA | 类名：PopupOptions；  API声明：message: PopupTextOptions;  差异内容：message: PopupTextOptions; | api/@ohos.arkui.advanced.Popup.d.ets |
| 新增API | NA | 类名：PopupOptions；  API声明：showClose?: boolean | Resource;  差异内容：showClose?: boolean | Resource; | api/@ohos.arkui.advanced.Popup.d.ets |
| 新增API | NA | 类名：PopupOptions；  API声明：onClose?: () => void;  差异内容：onClose?: () => void; | api/@ohos.arkui.advanced.Popup.d.ets |
| 新增API | NA | 类名：PopupOptions；  API声明：buttons?: [  PopupButtonOptions?,  PopupButtonOptions?  ];  差异内容：buttons?: [  PopupButtonOptions?,  PopupButtonOptions?  ]; | api/@ohos.arkui.advanced.Popup.d.ets |
| 新增API | NA | 类名：global；  API声明：@Builder  export declare function Popup(options: PopupOptions): void;  差异内容：@Builder  export declare function Popup(options: PopupOptions): void; | api/@ohos.arkui.advanced.Popup.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare struct ProgressButton  差异内容： export declare struct ProgressButton | api/@ohos.arkui.advanced.ProgressButton.d.ets |
| 新增API | NA | 类名：ProgressButton；  API声明：@Prop  progress: number;  差异内容：@Prop  progress: number; | api/@ohos.arkui.advanced.ProgressButton.d.ets |
| 新增API | NA | 类名：ProgressButton；  API声明：@Prop  content: string;  差异内容：@Prop  content: string; | api/@ohos.arkui.advanced.ProgressButton.d.ets |
| 新增API | NA | 类名：ProgressButton；  API声明：progressButtonWidth?: Length;  差异内容：progressButtonWidth?: Length; | api/@ohos.arkui.advanced.ProgressButton.d.ets |
| 新增API | NA | 类名：ProgressButton；  API声明：clickCallback: () => void;  差异内容：clickCallback: () => void; | api/@ohos.arkui.advanced.ProgressButton.d.ets |
| 新增API | NA | 类名：ProgressButton；  API声明：@Prop  enable: boolean;  差异内容：@Prop  enable: boolean; | api/@ohos.arkui.advanced.ProgressButton.d.ets |
| 新增API | NA | 类名：global；  API声明： interface SegmentButtonTextItem  差异内容： interface SegmentButtonTextItem | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：SegmentButtonTextItem；  API声明：text: ResourceStr;  差异内容：text: ResourceStr; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：global；  API声明： interface SegmentButtonIconItem  差异内容： interface SegmentButtonIconItem | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：SegmentButtonIconItem；  API声明：icon: ResourceStr;  差异内容：icon: ResourceStr; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：SegmentButtonIconItem；  API声明：selectedIcon: ResourceStr;  差异内容：selectedIcon: ResourceStr; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：global；  API声明： interface SegmentButtonIconTextItem  差异内容： interface SegmentButtonIconTextItem | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：SegmentButtonIconTextItem；  API声明：icon: ResourceStr;  差异内容：icon: ResourceStr; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：SegmentButtonIconTextItem；  API声明：selectedIcon: ResourceStr;  差异内容：selectedIcon: ResourceStr; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：SegmentButtonIconTextItem；  API声明：text: ResourceStr;  差异内容：text: ResourceStr; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：global；  API声明：declare type DimensionNoPercentage = PX | VP | FP | LPX | Resource;  差异内容：declare type DimensionNoPercentage = PX | VP | FP | LPX | Resource; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：global；  API声明： interface CommonSegmentButtonOptions  差异内容： interface CommonSegmentButtonOptions | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：CommonSegmentButtonOptions；  API声明：fontColor?: ResourceColor;  差异内容：fontColor?: ResourceColor; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：CommonSegmentButtonOptions；  API声明：selectedFontColor?: ResourceColor;  差异内容：selectedFontColor?: ResourceColor; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：CommonSegmentButtonOptions；  API声明：fontSize?: DimensionNoPercentage;  差异内容：fontSize?: DimensionNoPercentage; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：CommonSegmentButtonOptions；  API声明：selectedFontSize?: DimensionNoPercentage;  差异内容：selectedFontSize?: DimensionNoPercentage; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：CommonSegmentButtonOptions；  API声明：fontWeight?: FontWeight;  差异内容：fontWeight?: FontWeight; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：CommonSegmentButtonOptions；  API声明：selectedFontWeight?: FontWeight;  差异内容：selectedFontWeight?: FontWeight; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：CommonSegmentButtonOptions；  API声明：backgroundColor?: ResourceColor;  差异内容：backgroundColor?: ResourceColor; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：CommonSegmentButtonOptions；  API声明：selectedBackgroundColor?: ResourceColor;  差异内容：selectedBackgroundColor?: ResourceColor; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：CommonSegmentButtonOptions；  API声明：imageSize?: SizeOptions;  差异内容：imageSize?: SizeOptions; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：CommonSegmentButtonOptions；  API声明：buttonPadding?: Padding | Dimension;  差异内容：buttonPadding?: Padding | Dimension; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：CommonSegmentButtonOptions；  API声明：textPadding?: Padding | Dimension;  差异内容：textPadding?: Padding | Dimension; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：CommonSegmentButtonOptions；  API声明：backgroundBlurStyle?: BlurStyle;  差异内容：backgroundBlurStyle?: BlurStyle; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：global；  API声明：declare type ItemRestriction<T> = [  T,  T,  T?,  T?,  T?  ];  差异内容：declare type ItemRestriction<T> = [  T,  T,  T?,  T?,  T?  ]; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：global；  API声明：declare type SegmentButtonItemTuple = ItemRestriction<SegmentButtonTextItem> | ItemRestriction<SegmentButtonIconItem> | ItemRestriction<SegmentButtonIconTextItem>;  差异内容：declare type SegmentButtonItemTuple = ItemRestriction<SegmentButtonTextItem> | ItemRestriction<SegmentButtonIconItem> | ItemRestriction<SegmentButtonIconTextItem>; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：global；  API声明：declare type SegmentButtonItemArray = Array<SegmentButtonTextItem> | Array<SegmentButtonIconItem> | Array<SegmentButtonIconTextItem>;  差异内容：declare type SegmentButtonItemArray = Array<SegmentButtonTextItem> | Array<SegmentButtonIconItem> | Array<SegmentButtonIconTextItem>; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：global；  API声明： interface TabSegmentButtonConstructionOptions  差异内容： interface TabSegmentButtonConstructionOptions | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：TabSegmentButtonConstructionOptions；  API声明：buttons: ItemRestriction<SegmentButtonTextItem>;  差异内容：buttons: ItemRestriction<SegmentButtonTextItem>; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：global；  API声明： interface CapsuleSegmentButtonConstructionOptions  差异内容： interface CapsuleSegmentButtonConstructionOptions | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：CapsuleSegmentButtonConstructionOptions；  API声明：buttons: SegmentButtonItemTuple;  差异内容：buttons: SegmentButtonItemTuple; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：CapsuleSegmentButtonConstructionOptions；  API声明：multiply?: boolean;  差异内容：multiply?: boolean; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：global；  API声明： interface TabSegmentButtonOptions  差异内容： interface TabSegmentButtonOptions | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：TabSegmentButtonOptions；  API声明：type: "tab";  差异内容：type: "tab"; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：global；  API声明： interface CapsuleSegmentButtonOptions  差异内容： interface CapsuleSegmentButtonOptions | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：CapsuleSegmentButtonOptions；  API声明：type: "capsule";  差异内容：type: "capsule"; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：global；  API声明： interface SegmentButtonItemOptionsConstructorOptions  差异内容： interface SegmentButtonItemOptionsConstructorOptions | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：SegmentButtonItemOptionsConstructorOptions；  API声明：icon?: ResourceStr;  差异内容：icon?: ResourceStr; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：SegmentButtonItemOptionsConstructorOptions；  API声明：selectedIcon?: ResourceStr;  差异内容：selectedIcon?: ResourceStr; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：SegmentButtonItemOptionsConstructorOptions；  API声明：text?: ResourceStr;  差异内容：text?: ResourceStr; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：global；  API声明： declare class SegmentButtonItemOptions  差异内容： declare class SegmentButtonItemOptions | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：SegmentButtonItemOptions；  API声明：icon?: ResourceStr;  差异内容：icon?: ResourceStr; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：SegmentButtonItemOptions；  API声明：selectedIcon?: ResourceStr;  差异内容：selectedIcon?: ResourceStr; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：SegmentButtonItemOptions；  API声明：text?: ResourceStr;  差异内容：text?: ResourceStr; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：global；  API声明： declare class SegmentButtonItemOptionsArray  差异内容： declare class SegmentButtonItemOptionsArray | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：SegmentButtonItemOptionsArray；  API声明：push(...items: SegmentButtonItemArray): number;  差异内容：push(...items: SegmentButtonItemArray): number; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：SegmentButtonItemOptionsArray；  API声明：pop(): SegmentButtonItemOptions | undefined;  差异内容：pop(): SegmentButtonItemOptions | undefined; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：SegmentButtonItemOptionsArray；  API声明：shift(): SegmentButtonItemOptions | undefined;  差异内容：shift(): SegmentButtonItemOptions | undefined; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：SegmentButtonItemOptionsArray；  API声明：unshift(...items: SegmentButtonItemArray): number;  差异内容：unshift(...items: SegmentButtonItemArray): number; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：SegmentButtonItemOptionsArray；  API声明：splice(start: number, deleteCount: number, ...items: SegmentButtonItemOptions[]): SegmentButtonItemOptions[];  差异内容：splice(start: number, deleteCount: number, ...items: SegmentButtonItemOptions[]): SegmentButtonItemOptions[]; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：SegmentButtonItemOptionsArray；  API声明：static create(elements: SegmentButtonItemTuple): SegmentButtonItemOptionsArray;  差异内容：static create(elements: SegmentButtonItemTuple): SegmentButtonItemOptionsArray; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：global；  API声明： declare class SegmentButtonOptions  差异内容： declare class SegmentButtonOptions | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：SegmentButtonOptions；  API声明：type: "tab" | "capsule";  差异内容：type: "tab" | "capsule"; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：SegmentButtonOptions；  API声明：multiply: boolean;  差异内容：multiply: boolean; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：SegmentButtonOptions；  API声明：buttons: SegmentButtonItemOptionsArray;  差异内容：buttons: SegmentButtonItemOptionsArray; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：SegmentButtonOptions；  API声明：fontColor: ResourceColor;  差异内容：fontColor: ResourceColor; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：SegmentButtonOptions；  API声明：selectedFontColor: ResourceColor;  差异内容：selectedFontColor: ResourceColor; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：SegmentButtonOptions；  API声明：fontSize: DimensionNoPercentage;  差异内容：fontSize: DimensionNoPercentage; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：SegmentButtonOptions；  API声明：selectedFontSize: DimensionNoPercentage;  差异内容：selectedFontSize: DimensionNoPercentage; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：SegmentButtonOptions；  API声明：fontWeight: FontWeight;  差异内容：fontWeight: FontWeight; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：SegmentButtonOptions；  API声明：selectedFontWeight: FontWeight;  差异内容：selectedFontWeight: FontWeight; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：SegmentButtonOptions；  API声明：backgroundColor: ResourceColor;  差异内容：backgroundColor: ResourceColor; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：SegmentButtonOptions；  API声明：selectedBackgroundColor: ResourceColor;  差异内容：selectedBackgroundColor: ResourceColor; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：SegmentButtonOptions；  API声明：imageSize: SizeOptions;  差异内容：imageSize: SizeOptions; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：SegmentButtonOptions；  API声明：buttonPadding: Padding | Dimension;  差异内容：buttonPadding: Padding | Dimension; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：SegmentButtonOptions；  API声明：textPadding: Padding | Dimension;  差异内容：textPadding: Padding | Dimension; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：SegmentButtonOptions；  API声明：backgroundBlurStyle: BlurStyle;  差异内容：backgroundBlurStyle: BlurStyle; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：SegmentButtonOptions；  API声明：static tab(options: TabSegmentButtonConstructionOptions): SegmentButtonOptions;  差异内容：static tab(options: TabSegmentButtonConstructionOptions): SegmentButtonOptions; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：SegmentButtonOptions；  API声明：static capsule(options: CapsuleSegmentButtonConstructionOptions): SegmentButtonOptions;  差异内容：static capsule(options: CapsuleSegmentButtonConstructionOptions): SegmentButtonOptions; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：global；  API声明： declare struct SegmentButton  差异内容： declare struct SegmentButton | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：SegmentButton；  API声明：@ObjectLink  options: SegmentButtonOptions;  差异内容：@ObjectLink  options: SegmentButtonOptions; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：SegmentButton；  API声明：@Link  selectedIndexes: number[];  差异内容：@Link  selectedIndexes: number[]; | api/@ohos.arkui.advanced.SegmentButton.d.ets |
| 新增API | NA | 类名：global；  API声明： export interface EditorMenuOptions  差异内容： export interface EditorMenuOptions | api/@ohos.arkui.advanced.SelectionMenu.d.ets |
| 新增API | NA | 类名：EditorMenuOptions；  API声明：icon: ResourceStr;  差异内容：icon: ResourceStr; | api/@ohos.arkui.advanced.SelectionMenu.d.ets |
| 新增API | NA | 类名：EditorMenuOptions；  API声明：action?: () => void;  差异内容：action?: () => void; | api/@ohos.arkui.advanced.SelectionMenu.d.ets |
| 新增API | NA | 类名：EditorMenuOptions；  API声明：builder?: () => void;  差异内容：builder?: () => void; | api/@ohos.arkui.advanced.SelectionMenu.d.ets |
| 新增API | NA | 类名：global；  API声明： export interface ExpandedMenuOptions  差异内容： export interface ExpandedMenuOptions | api/@ohos.arkui.advanced.SelectionMenu.d.ets |
| 新增API | NA | 类名：ExpandedMenuOptions；  API声明：action?: () => void;  差异内容：action?: () => void; | api/@ohos.arkui.advanced.SelectionMenu.d.ets |
| 新增API | NA | 类名：global；  API声明： export interface EditorEventInfo  差异内容： export interface EditorEventInfo | api/@ohos.arkui.advanced.SelectionMenu.d.ets |
| 新增API | NA | 类名：EditorEventInfo；  API声明：content?: RichEditorSelection;  差异内容：content?: RichEditorSelection; | api/@ohos.arkui.advanced.SelectionMenu.d.ets |
| 新增API | NA | 类名：global；  API声明： export interface SelectionMenuOptions  差异内容： export interface SelectionMenuOptions | api/@ohos.arkui.advanced.SelectionMenu.d.ets |
| 新增API | NA | 类名：SelectionMenuOptions；  API声明：editorMenuOptions?: Array<EditorMenuOptions>;  差异内容：editorMenuOptions?: Array<EditorMenuOptions>; | api/@ohos.arkui.advanced.SelectionMenu.d.ets |
| 新增API | NA | 类名：SelectionMenuOptions；  API声明：expandedMenuOptions?: Array<ExpandedMenuOptions>;  差异内容：expandedMenuOptions?: Array<ExpandedMenuOptions>; | api/@ohos.arkui.advanced.SelectionMenu.d.ets |
| 新增API | NA | 类名：SelectionMenuOptions；  API声明：controller?: RichEditorController;  差异内容：controller?: RichEditorController; | api/@ohos.arkui.advanced.SelectionMenu.d.ets |
| 新增API | NA | 类名：SelectionMenuOptions；  API声明：onPaste?: (event?: EditorEventInfo) => void;  差异内容：onPaste?: (event?: EditorEventInfo) => void; | api/@ohos.arkui.advanced.SelectionMenu.d.ets |
| 新增API | NA | 类名：SelectionMenuOptions；  API声明：onCopy?: (event?: EditorEventInfo) => void;  差异内容：onCopy?: (event?: EditorEventInfo) => void; | api/@ohos.arkui.advanced.SelectionMenu.d.ets |
| 新增API | NA | 类名：SelectionMenuOptions；  API声明：onCut?: (event?: EditorEventInfo) => void;  差异内容：onCut?: (event?: EditorEventInfo) => void; | api/@ohos.arkui.advanced.SelectionMenu.d.ets |
| 新增API | NA | 类名：SelectionMenuOptions；  API声明：onSelectAll?: (event?: EditorEventInfo) => void;  差异内容：onSelectAll?: (event?: EditorEventInfo) => void; | api/@ohos.arkui.advanced.SelectionMenu.d.ets |
| 新增API | NA | 类名：global；  API声明：@Builder  export declare function SelectionMenu(options: SelectionMenuOptions): void;  差异内容：@Builder  export declare function SelectionMenu(options: SelectionMenuOptions): void; | api/@ohos.arkui.advanced.SelectionMenu.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare class SelectTitleBarMenuItem  差异内容： export declare class SelectTitleBarMenuItem | api/@ohos.arkui.advanced.SelectTitleBar.d.ets |
| 新增API | NA | 类名：SelectTitleBarMenuItem；  API声明：value: ResourceStr;  差异内容：value: ResourceStr; | api/@ohos.arkui.advanced.SelectTitleBar.d.ets |
| 新增API | NA | 类名：SelectTitleBarMenuItem；  API声明：isEnabled?: boolean;  差异内容：isEnabled?: boolean; | api/@ohos.arkui.advanced.SelectTitleBar.d.ets |
| 新增API | NA | 类名：SelectTitleBarMenuItem；  API声明：action?: () => void;  差异内容：action?: () => void; | api/@ohos.arkui.advanced.SelectTitleBar.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare struct SelectTitleBar  差异内容： export declare struct SelectTitleBar | api/@ohos.arkui.advanced.SelectTitleBar.d.ets |
| 新增API | NA | 类名：SelectTitleBar；  API声明：@Prop  selected: number;  差异内容：@Prop  selected: number; | api/@ohos.arkui.advanced.SelectTitleBar.d.ets |
| 新增API | NA | 类名：SelectTitleBar；  API声明：options: Array<SelectOption>;  差异内容：options: Array<SelectOption>; | api/@ohos.arkui.advanced.SelectTitleBar.d.ets |
| 新增API | NA | 类名：SelectTitleBar；  API声明：menuItems?: Array<SelectTitleBarMenuItem>;  差异内容：menuItems?: Array<SelectTitleBarMenuItem>; | api/@ohos.arkui.advanced.SelectTitleBar.d.ets |
| 新增API | NA | 类名：SelectTitleBar；  API声明：subtitle?: ResourceStr;  差异内容：subtitle?: ResourceStr; | api/@ohos.arkui.advanced.SelectTitleBar.d.ets |
| 新增API | NA | 类名：SelectTitleBar；  API声明：badgeValue?: number;  差异内容：badgeValue?: number; | api/@ohos.arkui.advanced.SelectTitleBar.d.ets |
| 新增API | NA | 类名：SelectTitleBar；  API声明：hidesBackButton?: boolean;  差异内容：hidesBackButton?: boolean; | api/@ohos.arkui.advanced.SelectTitleBar.d.ets |
| 新增API | NA | 类名：SelectTitleBar；  API声明：onSelected?: ((index: number) => void);  差异内容：onSelected?: ((index: number) => void); | api/@ohos.arkui.advanced.SelectTitleBar.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare struct SplitLayout  差异内容： export declare struct SplitLayout | api/@ohos.arkui.advanced.SplitLayout.d.ets |
| 新增API | NA | 类名：SplitLayout；  API声明：@BuilderParam  container: () => void;  差异内容：@BuilderParam  container: () => void; | api/@ohos.arkui.advanced.SplitLayout.d.ets |
| 新增API | NA | 类名：SplitLayout；  API声明：@State  mainImage: ResourceStr;  差异内容：@State  mainImage: ResourceStr; | api/@ohos.arkui.advanced.SplitLayout.d.ets |
| 新增API | NA | 类名：SplitLayout；  API声明：@Prop  primaryText: ResourceStr;  差异内容：@Prop  primaryText: ResourceStr; | api/@ohos.arkui.advanced.SplitLayout.d.ets |
| 新增API | NA | 类名：SplitLayout；  API声明：@Prop  secondaryText?: ResourceStr;  差异内容：@Prop  secondaryText?: ResourceStr; | api/@ohos.arkui.advanced.SplitLayout.d.ets |
| 新增API | NA | 类名：SplitLayout；  API声明：@Prop  tertiaryText?: ResourceStr;  差异内容：@Prop  tertiaryText?: ResourceStr; | api/@ohos.arkui.advanced.SplitLayout.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare enum OperationType  差异内容： export declare enum OperationType | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 新增API | NA | 类名：OperationType；  API声明：TEXT\_ARROW = 0  差异内容：TEXT\_ARROW = 0 | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 新增API | NA | 类名：OperationType；  API声明：BUTTON = 1  差异内容：BUTTON = 1 | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 新增API | NA | 类名：OperationType；  API声明：ICON\_GROUP = 2  差异内容：ICON\_GROUP = 2 | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 新增API | NA | 类名：OperationType；  API声明：LOADING = 3  差异内容：LOADING = 3 | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare class OperationOption  差异内容： export declare class OperationOption | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 新增API | NA | 类名：OperationOption；  API声明：value: ResourceStr;  差异内容：value: ResourceStr; | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 新增API | NA | 类名：OperationOption；  API声明：action?: () => void;  差异内容：action?: () => void; | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare class SelectOptions  差异内容： export declare class SelectOptions | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 新增API | NA | 类名：SelectOptions；  API声明：options: Array<SelectOption>;  差异内容：options: Array<SelectOption>; | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 新增API | NA | 类名：SelectOptions；  API声明：selected?: number;  差异内容：selected?: number; | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 新增API | NA | 类名：SelectOptions；  API声明：value?: string;  差异内容：value?: string; | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 新增API | NA | 类名：SelectOptions；  API声明：onSelect?: (index: number, value?: string) => void;  差异内容：onSelect?: (index: number, value?: string) => void; | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 新增API | NA | 类名：global；  API声明： declare enum SymbolRenderingStrategy  差异内容： declare enum SymbolRenderingStrategy | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 新增API | NA | 类名：SymbolRenderingStrategy；  API声明：SINGLE = 0  差异内容：SINGLE = 0 | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 新增API | NA | 类名：SymbolRenderingStrategy；  API声明：MULTIPLE\_COLOR = 1  差异内容：MULTIPLE\_COLOR = 1 | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 新增API | NA | 类名：SymbolRenderingStrategy；  API声明：MULTIPLE\_OPACITY = 2  差异内容：MULTIPLE\_OPACITY = 2 | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 新增API | NA | 类名：global；  API声明： declare enum SymbolEffectStrategy  差异内容： declare enum SymbolEffectStrategy | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 新增API | NA | 类名：SymbolEffectStrategy；  API声明：NONE = 0  差异内容：NONE = 0 | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 新增API | NA | 类名：SymbolEffectStrategy；  API声明：SCALE = 1  差异内容：SCALE = 1 | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 新增API | NA | 类名：SymbolEffectStrategy；  API声明：HIERARCHICAL = 2  差异内容：HIERARCHICAL = 2 | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare class SymbolOptions  差异内容： export declare class SymbolOptions | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 新增API | NA | 类名：SymbolOptions；  API声明：fontSize?: number | string | Resource;  差异内容：fontSize?: number | string | Resource; | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 新增API | NA | 类名：SymbolOptions；  API声明：fontColor?: Array<ResourceColor>;  差异内容：fontColor?: Array<ResourceColor>; | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 新增API | NA | 类名：SymbolOptions；  API声明：fontWeight?: number | FontWeight | string;  差异内容：fontWeight?: number | FontWeight | string; | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 新增API | NA | 类名：SymbolOptions；  API声明：effectStrategy?: SymbolEffectStrategy;  差异内容：effectStrategy?: SymbolEffectStrategy; | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 新增API | NA | 类名：SymbolOptions；  API声明：renderingStrategy?: SymbolRenderingStrategy;  差异内容：renderingStrategy?: SymbolRenderingStrategy; | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare struct SubHeader  差异内容： export declare struct SubHeader | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 新增API | NA | 类名：SubHeader；  API声明：@Prop  icon?: ResourceStr;  差异内容：@Prop  icon?: ResourceStr; | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 新增API | NA | 类名：SubHeader；  API声明：iconSymbolOptions?: SymbolOptions;  差异内容：iconSymbolOptions?: SymbolOptions; | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 新增API | NA | 类名：SubHeader；  API声明：@Prop  primaryTitle?: ResourceStr;  差异内容：@Prop  primaryTitle?: ResourceStr; | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 新增API | NA | 类名：SubHeader；  API声明：@Prop  secondaryTitle?: ResourceStr;  差异内容：@Prop  secondaryTitle?: ResourceStr; | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 新增API | NA | 类名：SubHeader；  API声明：select?: SelectOptions;  差异内容：select?: SelectOptions; | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 新增API | NA | 类名：SubHeader；  API声明：@Prop  operationType?: OperationType;  差异内容：@Prop  operationType?: OperationType; | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 新增API | NA | 类名：SubHeader；  API声明：operationItem?: Array<OperationOption>;  差异内容：operationItem?: Array<OperationOption>; | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 新增API | NA | 类名：SubHeader；  API声明：operationSymbolOptions?: Array<SymbolOptions>;  差异内容：operationSymbolOptions?: Array<SymbolOptions>; | api/@ohos.arkui.advanced.SubHeader.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare struct SwipeRefresher  差异内容： export declare struct SwipeRefresher | api/@ohos.arkui.advanced.SwipeRefresher.d.ets |
| 新增API | NA | 类名：SwipeRefresher；  API声明：@Prop  content?: string;  差异内容：@Prop  content?: string; | api/@ohos.arkui.advanced.SwipeRefresher.d.ets |
| 新增API | NA | 类名：SwipeRefresher；  API声明：@Prop  isLoading: boolean;  差异内容：@Prop  isLoading: boolean; | api/@ohos.arkui.advanced.SwipeRefresher.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare class TabTitleBarMenuItem  差异内容： export declare class TabTitleBarMenuItem | api/@ohos.arkui.advanced.TabTitleBar.d.ets |
| 新增API | NA | 类名：TabTitleBarMenuItem；  API声明：value: ResourceStr;  差异内容：value: ResourceStr; | api/@ohos.arkui.advanced.TabTitleBar.d.ets |
| 新增API | NA | 类名：TabTitleBarMenuItem；  API声明：isEnabled?: boolean;  差异内容：isEnabled?: boolean; | api/@ohos.arkui.advanced.TabTitleBar.d.ets |
| 新增API | NA | 类名：TabTitleBarMenuItem；  API声明：action?: () => void;  差异内容：action?: () => void; | api/@ohos.arkui.advanced.TabTitleBar.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare class TabTitleBarTabItem  差异内容： export declare class TabTitleBarTabItem | api/@ohos.arkui.advanced.TabTitleBar.d.ets |
| 新增API | NA | 类名：TabTitleBarTabItem；  API声明：title: ResourceStr;  差异内容：title: ResourceStr; | api/@ohos.arkui.advanced.TabTitleBar.d.ets |
| 新增API | NA | 类名：TabTitleBarTabItem；  API声明：icon?: ResourceStr;  差异内容：icon?: ResourceStr; | api/@ohos.arkui.advanced.TabTitleBar.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare struct TabTitleBar  差异内容： export declare struct TabTitleBar | api/@ohos.arkui.advanced.TabTitleBar.d.ets |
| 新增API | NA | 类名：TabTitleBar；  API声明：tabItems: Array<TabTitleBarTabItem>;  差异内容：tabItems: Array<TabTitleBarTabItem>; | api/@ohos.arkui.advanced.TabTitleBar.d.ets |
| 新增API | NA | 类名：TabTitleBar；  API声明：menuItems?: Array<TabTitleBarMenuItem>;  差异内容：menuItems?: Array<TabTitleBarMenuItem>; | api/@ohos.arkui.advanced.TabTitleBar.d.ets |
| 新增API | NA | 类名：TabTitleBar；  API声明：@BuilderParam  swiperContent: () => void;  差异内容：@BuilderParam  swiperContent: () => void; | api/@ohos.arkui.advanced.TabTitleBar.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare enum ItemState  差异内容： export declare enum ItemState | api/@ohos.arkui.advanced.ToolBar.d.ets |
| 新增API | NA | 类名：ItemState；  API声明：ENABLE = 1  差异内容：ENABLE = 1 | api/@ohos.arkui.advanced.ToolBar.d.ets |
| 新增API | NA | 类名：ItemState；  API声明：DISABLE = 2  差异内容：DISABLE = 2 | api/@ohos.arkui.advanced.ToolBar.d.ets |
| 新增API | NA | 类名：ItemState；  API声明：ACTIVATE = 3  差异内容：ACTIVATE = 3 | api/@ohos.arkui.advanced.ToolBar.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare class ToolBarOption  差异内容： export declare class ToolBarOption | api/@ohos.arkui.advanced.ToolBar.d.ets |
| 新增API | NA | 类名：ToolBarOption；  API声明：content: ResourceStr;  差异内容：content: ResourceStr; | api/@ohos.arkui.advanced.ToolBar.d.ets |
| 新增API | NA | 类名：ToolBarOption；  API声明：action?: () => void;  差异内容：action?: () => void; | api/@ohos.arkui.advanced.ToolBar.d.ets |
| 新增API | NA | 类名：ToolBarOption；  API声明：icon?: Resource;  差异内容：icon?: Resource; | api/@ohos.arkui.advanced.ToolBar.d.ets |
| 新增API | NA | 类名：ToolBarOption；  API声明：state?: ItemState;  差异内容：state?: ItemState; | api/@ohos.arkui.advanced.ToolBar.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare class ToolBarOptions  差异内容： export declare class ToolBarOptions | api/@ohos.arkui.advanced.ToolBar.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare struct ToolBar  差异内容： export declare struct ToolBar | api/@ohos.arkui.advanced.ToolBar.d.ets |
| 新增API | NA | 类名：ToolBar；  API声明：@ObjectLink  toolBarList: ToolBarOptions;  差异内容：@ObjectLink  toolBarList: ToolBarOptions; | api/@ohos.arkui.advanced.ToolBar.d.ets |
| 新增API | NA | 类名：ToolBar；  API声明：@Prop  activateIndex?: number;  差异内容：@Prop  activateIndex?: number; | api/@ohos.arkui.advanced.ToolBar.d.ets |
| 新增API | NA | 类名：ToolBar；  API声明：controller: TabsController;  差异内容：controller: TabsController; | api/@ohos.arkui.advanced.ToolBar.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare enum TreeListenType  差异内容： export declare enum TreeListenType | api/@ohos.arkui.advanced.TreeView.d.ets |
| 新增API | NA | 类名：TreeListenType；  API声明：NODE\_CLICK = "NodeClick"  差异内容：NODE\_CLICK = "NodeClick" | api/@ohos.arkui.advanced.TreeView.d.ets |
| 新增API | NA | 类名：TreeListenType；  API声明：NODE\_ADD = "NodeAdd"  差异内容：NODE\_ADD = "NodeAdd" | api/@ohos.arkui.advanced.TreeView.d.ets |
| 新增API | NA | 类名：TreeListenType；  API声明：NODE\_DELETE = "NodeDelete"  差异内容：NODE\_DELETE = "NodeDelete" | api/@ohos.arkui.advanced.TreeView.d.ets |
| 新增API | NA | 类名：TreeListenType；  API声明：NODE\_MODIFY = "NodeModify"  差异内容：NODE\_MODIFY = "NodeModify" | api/@ohos.arkui.advanced.TreeView.d.ets |
| 新增API | NA | 类名：TreeListenType；  API声明：NODE\_MOVE = "NodeMove"  差异内容：NODE\_MOVE = "NodeMove" | api/@ohos.arkui.advanced.TreeView.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare class TreeListener  差异内容： export declare class TreeListener | api/@ohos.arkui.advanced.TreeView.d.ets |
| 新增API | NA | 类名：TreeListener；  API声明：on(type: TreeListenType, callback: (callbackParam: CallbackParam) => void): void;  差异内容：on(type: TreeListenType, callback: (callbackParam: CallbackParam) => void): void; | api/@ohos.arkui.advanced.TreeView.d.ets |
| 新增API | NA | 类名：TreeListener；  API声明：once(type: TreeListenType, callback: (callbackParam: CallbackParam) => void): void;  差异内容：once(type: TreeListenType, callback: (callbackParam: CallbackParam) => void): void; | api/@ohos.arkui.advanced.TreeView.d.ets |
| 新增API | NA | 类名：TreeListener；  API声明：off(type: TreeListenType, callback?: (callbackParam: CallbackParam) => void): void;  差异内容：off(type: TreeListenType, callback?: (callbackParam: CallbackParam) => void): void; | api/@ohos.arkui.advanced.TreeView.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare class TreeListenerManager  差异内容： export declare class TreeListenerManager | api/@ohos.arkui.advanced.TreeView.d.ets |
| 新增API | NA | 类名：TreeListenerManager；  API声明：static getInstance(): TreeListenerManager;  差异内容：static getInstance(): TreeListenerManager; | api/@ohos.arkui.advanced.TreeView.d.ets |
| 新增API | NA | 类名：TreeListenerManager；  API声明：getTreeListener(): TreeListener;  差异内容：getTreeListener(): TreeListener; | api/@ohos.arkui.advanced.TreeView.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare struct TreeView  差异内容： export declare struct TreeView | api/@ohos.arkui.advanced.TreeView.d.ets |
| 新增API | NA | 类名：TreeView；  API声明：treeController: TreeController;  差异内容：treeController: TreeController; | api/@ohos.arkui.advanced.TreeView.d.ets |
| 新增API | NA | 类名：global；  API声明： export interface CallbackParam  差异内容： export interface CallbackParam | api/@ohos.arkui.advanced.TreeView.d.ets |
| 新增API | NA | 类名：CallbackParam；  API声明：currentNodeId: number;  差异内容：currentNodeId: number; | api/@ohos.arkui.advanced.TreeView.d.ets |
| 新增API | NA | 类名：CallbackParam；  API声明：parentNodeId?: number;  差异内容：parentNodeId?: number; | api/@ohos.arkui.advanced.TreeView.d.ets |
| 新增API | NA | 类名：CallbackParam；  API声明：childIndex?: number;  差异内容：childIndex?: number; | api/@ohos.arkui.advanced.TreeView.d.ets |
| 新增API | NA | 类名：global；  API声明： export interface NodeParam  差异内容： export interface NodeParam | api/@ohos.arkui.advanced.TreeView.d.ets |
| 新增API | NA | 类名：NodeParam；  API声明：parentNodeId?: number;  差异内容：parentNodeId?: number; | api/@ohos.arkui.advanced.TreeView.d.ets |
| 新增API | NA | 类名：NodeParam；  API声明：currentNodeId?: number;  差异内容：currentNodeId?: number; | api/@ohos.arkui.advanced.TreeView.d.ets |
| 新增API | NA | 类名：NodeParam；  API声明：isFolder?: boolean;  差异内容：isFolder?: boolean; | api/@ohos.arkui.advanced.TreeView.d.ets |
| 新增API | NA | 类名：NodeParam；  API声明：icon?: ResourceStr;  差异内容：icon?: ResourceStr; | api/@ohos.arkui.advanced.TreeView.d.ets |
| 新增API | NA | 类名：NodeParam；  API声明：selectedIcon?: ResourceStr;  差异内容：selectedIcon?: ResourceStr; | api/@ohos.arkui.advanced.TreeView.d.ets |
| 新增API | NA | 类名：NodeParam；  API声明：editIcon?: ResourceStr;  差异内容：editIcon?: ResourceStr; | api/@ohos.arkui.advanced.TreeView.d.ets |
| 新增API | NA | 类名：NodeParam；  API声明：primaryTitle?: ResourceStr;  差异内容：primaryTitle?: ResourceStr; | api/@ohos.arkui.advanced.TreeView.d.ets |
| 新增API | NA | 类名：NodeParam；  API声明：secondaryTitle?: ResourceStr;  差异内容：secondaryTitle?: ResourceStr; | api/@ohos.arkui.advanced.TreeView.d.ets |
| 新增API | NA | 类名：NodeParam；  API声明：container?: () => void;  差异内容：container?: () => void; | api/@ohos.arkui.advanced.TreeView.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare class TreeController  差异内容： export declare class TreeController | api/@ohos.arkui.advanced.TreeView.d.ets |
| 新增API | NA | 类名：TreeController；  API声明：removeNode(): void;  差异内容：removeNode(): void; | api/@ohos.arkui.advanced.TreeView.d.ets |
| 新增API | NA | 类名：TreeController；  API声明：modifyNode(): void;  差异内容：modifyNode(): void; | api/@ohos.arkui.advanced.TreeView.d.ets |
| 新增API | NA | 类名：TreeController；  API声明：addNode(nodeParam?: NodeParam): TreeController;  差异内容：addNode(nodeParam?: NodeParam): TreeController; | api/@ohos.arkui.advanced.TreeView.d.ets |
| 新增API | NA | 类名：TreeController；  API声明：refreshNode(parentId: number, parentSubTitle: ResourceStr, currentSubtitle: ResourceStr): void;  差异内容：refreshNode(parentId: number, parentSubTitle: ResourceStr, currentSubtitle: ResourceStr): void; | api/@ohos.arkui.advanced.TreeView.d.ets |
| 新增API | NA | 类名：TreeController；  API声明：buildDone(): void;  差异内容：buildDone(): void; | api/@ohos.arkui.advanced.TreeView.d.ets |
| 新增API | NA | 类名：global；  API声明： declare namespace componentSnapshot  差异内容： declare namespace componentSnapshot | api/@ohos.arkui.componentSnapshot.d.ts |
| 新增API | NA | 类名：componentSnapshot；  API声明：function get(id: string, callback: AsyncCallback<image.PixelMap>): void;  差异内容：function get(id: string, callback: AsyncCallback<image.PixelMap>): void; | api/@ohos.arkui.componentSnapshot.d.ts |
| 新增API | NA | 类名：componentSnapshot；  API声明：function get(id: string): Promise<image.PixelMap>;  差异内容：function get(id: string): Promise<image.PixelMap>; | api/@ohos.arkui.componentSnapshot.d.ts |
| 新增API | NA | 类名：componentSnapshot；  API声明：function createFromBuilder(builder: CustomBuilder, callback: AsyncCallback<image.PixelMap>): void;  差异内容：function createFromBuilder(builder: CustomBuilder, callback: AsyncCallback<image.PixelMap>): void; | api/@ohos.arkui.componentSnapshot.d.ts |
| 新增API | NA | 类名：componentSnapshot；  API声明：function createFromBuilder(builder: CustomBuilder): Promise<image.PixelMap>;  差异内容：function createFromBuilder(builder: CustomBuilder): Promise<image.PixelMap>; | api/@ohos.arkui.componentSnapshot.d.ts |
| 新增API | NA | 类名：global；  API声明： declare namespace componentUtils  差异内容： declare namespace componentUtils | api/@ohos.arkui.componentUtils.d.ts |
| 新增API | NA | 类名：componentUtils；  API声明： interface ComponentInfo  差异内容： interface ComponentInfo | api/@ohos.arkui.componentUtils.d.ts |
| 新增API | NA | 类名：ComponentInfo；  API声明：size: Size;  差异内容：size: Size; | api/@ohos.arkui.componentUtils.d.ts |
| 新增API | NA | 类名：ComponentInfo；  API声明：localOffset: Offset;  差异内容：localOffset: Offset; | api/@ohos.arkui.componentUtils.d.ts |
| 新增API | NA | 类名：ComponentInfo；  API声明：windowOffset: Offset;  差异内容：windowOffset: Offset; | api/@ohos.arkui.componentUtils.d.ts |
| 新增API | NA | 类名：ComponentInfo；  API声明：screenOffset: Offset;  差异内容：screenOffset: Offset; | api/@ohos.arkui.componentUtils.d.ts |
| 新增API | NA | 类名：ComponentInfo；  API声明：translate: TranslateResult;  差异内容：translate: TranslateResult; | api/@ohos.arkui.componentUtils.d.ts |
| 新增API | NA | 类名：ComponentInfo；  API声明：scale: ScaleResult;  差异内容：scale: ScaleResult; | api/@ohos.arkui.componentUtils.d.ts |
| 新增API | NA | 类名：ComponentInfo；  API声明：rotate: RotateResult;  差异内容：rotate: RotateResult; | api/@ohos.arkui.componentUtils.d.ts |
| 新增API | NA | 类名：ComponentInfo；  API声明：transform: Matrix4Result;  差异内容：transform: Matrix4Result; | api/@ohos.arkui.componentUtils.d.ts |
| 新增API | NA | 类名：componentUtils；  API声明： interface Size  差异内容： interface Size | api/@ohos.arkui.componentUtils.d.ts |
| 新增API | NA | 类名：Size；  API声明：width: number;  差异内容：width: number; | api/@ohos.arkui.componentUtils.d.ts |
| 新增API | NA | 类名：Size；  API声明：height: number;  差异内容：height: number; | api/@ohos.arkui.componentUtils.d.ts |
| 新增API | NA | 类名：componentUtils；  API声明： interface Offset  差异内容： interface Offset | api/@ohos.arkui.componentUtils.d.ts |
| 新增API | NA | 类名：Offset；  API声明：x: number;  差异内容：x: number; | api/@ohos.arkui.componentUtils.d.ts |
| 新增API | NA | 类名：Offset；  API声明：y: number;  差异内容：y: number; | api/@ohos.arkui.componentUtils.d.ts |
| 新增API | NA | 类名：componentUtils；  API声明： interface TranslateResult  差异内容： interface TranslateResult | api/@ohos.arkui.componentUtils.d.ts |
| 新增API | NA | 类名：TranslateResult；  API声明：x: number;  差异内容：x: number; | api/@ohos.arkui.componentUtils.d.ts |
| 新增API | NA | 类名：TranslateResult；  API声明：y: number;  差异内容：y: number; | api/@ohos.arkui.componentUtils.d.ts |
| 新增API | NA | 类名：TranslateResult；  API声明：z: number;  差异内容：z: number; | api/@ohos.arkui.componentUtils.d.ts |
| 新增API | NA | 类名：componentUtils；  API声明： interface ScaleResult  差异内容： interface ScaleResult | api/@ohos.arkui.componentUtils.d.ts |
| 新增API | NA | 类名：ScaleResult；  API声明：x: number;  差异内容：x: number; | api/@ohos.arkui.componentUtils.d.ts |
| 新增API | NA | 类名：ScaleResult；  API声明：y: number;  差异内容：y: number; | api/@ohos.arkui.componentUtils.d.ts |
| 新增API | NA | 类名：ScaleResult；  API声明：z: number;  差异内容：z: number; | api/@ohos.arkui.componentUtils.d.ts |
| 新增API | NA | 类名：ScaleResult；  API声明：centerX: number;  差异内容：centerX: number; | api/@ohos.arkui.componentUtils.d.ts |
| 新增API | NA | 类名：ScaleResult；  API声明：centerY: number;  差异内容：centerY: number; | api/@ohos.arkui.componentUtils.d.ts |
| 新增API | NA | 类名：componentUtils；  API声明： interface RotateResult  差异内容： interface RotateResult | api/@ohos.arkui.componentUtils.d.ts |
| 新增API | NA | 类名：RotateResult；  API声明：x: number;  差异内容：x: number; | api/@ohos.arkui.componentUtils.d.ts |
| 新增API | NA | 类名：RotateResult；  API声明：y: number;  差异内容：y: number; | api/@ohos.arkui.componentUtils.d.ts |
| 新增API | NA | 类名：RotateResult；  API声明：z: number;  差异内容：z: number; | api/@ohos.arkui.componentUtils.d.ts |
| 新增API | NA | 类名：RotateResult；  API声明：centerX: number;  差异内容：centerX: number; | api/@ohos.arkui.componentUtils.d.ts |
| 新增API | NA | 类名：RotateResult；  API声明：centerY: number;  差异内容：centerY: number; | api/@ohos.arkui.componentUtils.d.ts |
| 新增API | NA | 类名：RotateResult；  API声明：angle: number;  差异内容：angle: number; | api/@ohos.arkui.componentUtils.d.ts |
| 新增API | NA | 类名：componentUtils；  API声明：type Matrix4Result = [  number,  number,  number,  number,  number,  number,  number,  number,  number,  number,  number,  number,  number,  number,  number,  number  ];  差异内容：type Matrix4Result = [  number,  number,  number,  number,  number,  number,  number,  number,  number,  number,  number,  number,  number,  number,  number,  number  ]; | api/@ohos.arkui.componentUtils.d.ts |
| 新增API | NA | 类名：componentUtils；  API声明：function getRectangleById(id: string): ComponentInfo;  差异内容：function getRectangleById(id: string): ComponentInfo; | api/@ohos.arkui.componentUtils.d.ts |
| 新增API | NA | 类名：global；  API声明： declare namespace dragController  差异内容： declare namespace dragController | api/@ohos.arkui.dragController.d.ts |
| 新增API | NA | 类名：dragController；  API声明： const enum DragStatus  差异内容： const enum DragStatus | api/@ohos.arkui.dragController.d.ts |
| 新增API | NA | 类名：DragStatus；  API声明：STARTED = 0  差异内容：STARTED = 0 | api/@ohos.arkui.dragController.d.ts |
| 新增API | NA | 类名：DragStatus；  API声明：ENDED = 1  差异内容：ENDED = 1 | api/@ohos.arkui.dragController.d.ts |
| 新增API | NA | 类名：dragController；  API声明： interface DragAndDropInfo  差异内容： interface DragAndDropInfo | api/@ohos.arkui.dragController.d.ts |
| 新增API | NA | 类名：DragAndDropInfo；  API声明：status: DragStatus;  差异内容：status: DragStatus; | api/@ohos.arkui.dragController.d.ts |
| 新增API | NA | 类名：DragAndDropInfo；  API声明：event: DragEvent;  差异内容：event: DragEvent; | api/@ohos.arkui.dragController.d.ts |
| 新增API | NA | 类名：DragAndDropInfo；  API声明：extraParams?: string;  差异内容：extraParams?: string; | api/@ohos.arkui.dragController.d.ts |
| 新增API | NA | 类名：dragController；  API声明： interface DragAction  差异内容： interface DragAction | api/@ohos.arkui.dragController.d.ts |
| 新增API | NA | 类名：DragAction；  API声明：startDrag(): Promise<void>;  差异内容：startDrag(): Promise<void>; | api/@ohos.arkui.dragController.d.ts |
| 新增API | NA | 类名：DragAction；  API声明：on(type: 'statusChange', callback: Callback<DragAndDropInfo>): void;  差异内容：on(type: 'statusChange', callback: Callback<DragAndDropInfo>): void; | api/@ohos.arkui.dragController.d.ts |
| 新增API | NA | 类名：DragAction；  API声明：off(type: 'statusChange', callback?: Callback<DragAndDropInfo>): void;  差异内容：off(type: 'statusChange', callback?: Callback<DragAndDropInfo>): void; | api/@ohos.arkui.dragController.d.ts |
| 新增API | NA | 类名：dragController；  API声明： interface DragInfo  差异内容： interface DragInfo | api/@ohos.arkui.dragController.d.ts |
| 新增API | NA | 类名：DragInfo；  API声明：pointerId: number;  差异内容：pointerId: number; | api/@ohos.arkui.dragController.d.ts |
| 新增API | NA | 类名：DragInfo；  API声明：data?: unifiedDataChannel.UnifiedData;  差异内容：data?: unifiedDataChannel.UnifiedData; | api/@ohos.arkui.dragController.d.ts |
| 新增API | NA | 类名：DragInfo；  API声明：extraParams?: string;  差异内容：extraParams?: string; | api/@ohos.arkui.dragController.d.ts |
| 新增API | NA | 类名：DragInfo；  API声明：touchPoint?: TouchPoint;  差异内容：touchPoint?: TouchPoint; | api/@ohos.arkui.dragController.d.ts |
| 新增API | NA | 类名：DragInfo；  API声明：previewOptions?: DragPreviewOptions;  差异内容：previewOptions?: DragPreviewOptions; | api/@ohos.arkui.dragController.d.ts |
| 新增API | NA | 类名：dragController；  API声明： interface AnimationOptions  差异内容： interface AnimationOptions | api/@ohos.arkui.dragController.d.ts |
| 新增API | NA | 类名：AnimationOptions；  API声明：duration?: number;  差异内容：duration?: number; | api/@ohos.arkui.dragController.d.ts |
| 新增API | NA | 类名：AnimationOptions；  API声明：curve?: Curve | ICurve;  差异内容：curve?: Curve | ICurve; | api/@ohos.arkui.dragController.d.ts |
| 新增API | NA | 类名：dragController；  API声明： export class DragPreview  差异内容： export class DragPreview | api/@ohos.arkui.dragController.d.ts |
| 新增API | NA | 类名：DragPreview；  API声明：setForegroundColor(color: ResourceColor): void;  差异内容：setForegroundColor(color: ResourceColor): void; | api/@ohos.arkui.dragController.d.ts |
| 新增API | NA | 类名：DragPreview；  API声明：animate(options: AnimationOptions, handler: () => void): void;  差异内容：animate(options: AnimationOptions, handler: () => void): void; | api/@ohos.arkui.dragController.d.ts |
| 新增API | NA | 类名：dragController；  API声明：function executeDrag(custom: CustomBuilder | DragItemInfo, dragInfo: DragInfo, callback: AsyncCallback<{  event: DragEvent;  extraParams: string;  }>): void;  差异内容：function executeDrag(custom: CustomBuilder | DragItemInfo, dragInfo: DragInfo, callback: AsyncCallback<{  event: DragEvent;  extraParams: string;  }>): void; | api/@ohos.arkui.dragController.d.ts |
| 新增API | NA | 类名：dragController；  API声明：function executeDrag(custom: CustomBuilder | DragItemInfo, dragInfo: DragInfo): Promise<{  event: DragEvent;  extraParams: string;  }>;  差异内容：function executeDrag(custom: CustomBuilder | DragItemInfo, dragInfo: DragInfo): Promise<{  event: DragEvent;  extraParams: string;  }>; | api/@ohos.arkui.dragController.d.ts |
| 新增API | NA | 类名：dragController；  API声明：function createDragAction(customArray: Array<CustomBuilder | DragItemInfo>, dragInfo: DragInfo): DragAction;  差异内容：function createDragAction(customArray: Array<CustomBuilder | DragItemInfo>, dragInfo: DragInfo): DragAction; | api/@ohos.arkui.dragController.d.ts |
| 新增API | NA | 类名：dragController；  API声明：function getDragPreview(): DragPreview;  差异内容：function getDragPreview(): DragPreview; | api/@ohos.arkui.dragController.d.ts |
| 新增API | NA | 类名：global；  API声明： export class DrawableDescriptor  差异内容： export class DrawableDescriptor | api/@ohos.arkui.drawableDescriptor.d.ts |
| 新增API | NA | 类名：DrawableDescriptor；  API声明：getPixelMap(): image.PixelMap;  差异内容：getPixelMap(): image.PixelMap; | api/@ohos.arkui.drawableDescriptor.d.ts |
| 新增API | NA | 类名：global；  API声明： export class LayeredDrawableDescriptor  差异内容： export class LayeredDrawableDescriptor | api/@ohos.arkui.drawableDescriptor.d.ts |
| 新增API | NA | 类名：LayeredDrawableDescriptor；  API声明：getForeground(): DrawableDescriptor;  差异内容：getForeground(): DrawableDescriptor; | api/@ohos.arkui.drawableDescriptor.d.ts |
| 新增API | NA | 类名：LayeredDrawableDescriptor；  API声明：getBackground(): DrawableDescriptor;  差异内容：getBackground(): DrawableDescriptor; | api/@ohos.arkui.drawableDescriptor.d.ts |
| 新增API | NA | 类名：LayeredDrawableDescriptor；  API声明：getMask(): DrawableDescriptor;  差异内容：getMask(): DrawableDescriptor; | api/@ohos.arkui.drawableDescriptor.d.ts |
| 新增API | NA | 类名：LayeredDrawableDescriptor；  API声明：static getMaskClipPath(): string;  差异内容：static getMaskClipPath(): string; | api/@ohos.arkui.drawableDescriptor.d.ts |
| 新增API | NA | 类名：global；  API声明： export class PixelMapDrawableDescriptor  差异内容： export class PixelMapDrawableDescriptor | api/@ohos.arkui.drawableDescriptor.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface AnimationOptions  差异内容： declare interface AnimationOptions | api/@ohos.arkui.drawableDescriptor.d.ts |
| 新增API | NA | 类名：AnimationOptions；  API声明：duration?: number;  差异内容：duration?: number; | api/@ohos.arkui.drawableDescriptor.d.ts |
| 新增API | NA | 类名：AnimationOptions；  API声明：iterations?: number;  差异内容：iterations?: number; | api/@ohos.arkui.drawableDescriptor.d.ts |
| 新增API | NA | 类名：global；  API声明： export class AnimatedDrawableDescriptor  差异内容： export class AnimatedDrawableDescriptor | api/@ohos.arkui.drawableDescriptor.d.ts |
| 新增API | NA | 类名：global；  API声明： declare namespace inspector  差异内容： declare namespace inspector | api/@ohos.arkui.inspector.d.ts |
| 新增API | NA | 类名：inspector；  API声明： interface ComponentObserver  差异内容： interface ComponentObserver | api/@ohos.arkui.inspector.d.ts |
| 新增API | NA | 类名：ComponentObserver；  API声明：on(type: 'layout', callback: () => void): void;  差异内容：on(type: 'layout', callback: () => void): void; | api/@ohos.arkui.inspector.d.ts |
| 新增API | NA | 类名：ComponentObserver；  API声明：off(type: 'layout', callback?: () => void): void;  差异内容：off(type: 'layout', callback?: () => void): void; | api/@ohos.arkui.inspector.d.ts |
| 新增API | NA | 类名：ComponentObserver；  API声明：on(type: 'draw', callback: () => void): void;  差异内容：on(type: 'draw', callback: () => void): void; | api/@ohos.arkui.inspector.d.ts |
| 新增API | NA | 类名：ComponentObserver；  API声明：off(type: 'draw', callback?: () => void): void;  差异内容：off(type: 'draw', callback?: () => void): void; | api/@ohos.arkui.inspector.d.ts |
| 新增API | NA | 类名：inspector；  API声明：function createComponentObserver(id: string): ComponentObserver;  差异内容：function createComponentObserver(id: string): ComponentObserver; | api/@ohos.arkui.inspector.d.ts |
| 新增API | NA | 类名：global；  API声明： declare namespace uiObserver  差异内容： declare namespace uiObserver | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：uiObserver；  API声明： export enum NavDestinationState  差异内容： export enum NavDestinationState | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：NavDestinationState；  API声明：ON\_SHOWN = 0  差异内容：ON\_SHOWN = 0 | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：NavDestinationState；  API声明：ON\_HIDDEN = 1  差异内容：ON\_HIDDEN = 1 | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：NavDestinationState；  API声明：ON\_APPEAR = 2  差异内容：ON\_APPEAR = 2 | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：NavDestinationState；  API声明：ON\_DISAPPEAR = 3  差异内容：ON\_DISAPPEAR = 3 | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：NavDestinationState；  API声明：ON\_WILL\_SHOW = 4  差异内容：ON\_WILL\_SHOW = 4 | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：NavDestinationState；  API声明：ON\_WILL\_HIDE = 5  差异内容：ON\_WILL\_HIDE = 5 | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：NavDestinationState；  API声明：ON\_WILL\_APPEAR = 6  差异内容：ON\_WILL\_APPEAR = 6 | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：NavDestinationState；  API声明：ON\_WILL\_DISAPPEAR = 7  差异内容：ON\_WILL\_DISAPPEAR = 7 | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：NavDestinationState；  API声明：ON\_BACKPRESS = 100  差异内容：ON\_BACKPRESS = 100 | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：uiObserver；  API声明： export enum RouterPageState  差异内容： export enum RouterPageState | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：RouterPageState；  API声明：ABOUT\_TO\_APPEAR = 0  差异内容：ABOUT\_TO\_APPEAR = 0 | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：RouterPageState；  API声明：ABOUT\_TO\_DISAPPEAR = 1  差异内容：ABOUT\_TO\_DISAPPEAR = 1 | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：RouterPageState；  API声明：ON\_PAGE\_SHOW = 2  差异内容：ON\_PAGE\_SHOW = 2 | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：RouterPageState；  API声明：ON\_PAGE\_HIDE = 3  差异内容：ON\_PAGE\_HIDE = 3 | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：RouterPageState；  API声明：ON\_BACK\_PRESS = 4  差异内容：ON\_BACK\_PRESS = 4 | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：uiObserver；  API声明： export enum ScrollEventType  差异内容： export enum ScrollEventType | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：ScrollEventType；  API声明：SCROLL\_START = 0  差异内容：SCROLL\_START = 0 | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：ScrollEventType；  API声明：SCROLL\_STOP = 1  差异内容：SCROLL\_STOP = 1 | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：uiObserver；  API声明： export interface NavDestinationInfo  差异内容： export interface NavDestinationInfo | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：NavDestinationInfo；  API声明：navigationId: ResourceStr;  差异内容：navigationId: ResourceStr; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：NavDestinationInfo；  API声明：name: ResourceStr;  差异内容：name: ResourceStr; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：NavDestinationInfo；  API声明：state: NavDestinationState;  差异内容：state: NavDestinationState; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：NavDestinationInfo；  API声明：index: number;  差异内容：index: number; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：NavDestinationInfo；  API声明：param?: Object;  差异内容：param?: Object; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：NavDestinationInfo；  API声明：navDestinationId: string;  差异内容：navDestinationId: string; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：uiObserver；  API声明： export interface NavigationInfo  差异内容： export interface NavigationInfo | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：NavigationInfo；  API声明：navigationId: string;  差异内容：navigationId: string; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：NavigationInfo；  API声明：pathStack: NavPathStack;  差异内容：pathStack: NavPathStack; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：uiObserver；  API声明： export interface ScrollEventInfo  差异内容： export interface ScrollEventInfo | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：ScrollEventInfo；  API声明：id: string;  差异内容：id: string; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：ScrollEventInfo；  API声明：uniqueId: number;  差异内容：uniqueId: number; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：ScrollEventInfo；  API声明：scrollEvent: ScrollEventType;  差异内容：scrollEvent: ScrollEventType; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：ScrollEventInfo；  API声明：offset: number;  差异内容：offset: number; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：uiObserver；  API声明： export interface ObserverOptions  差异内容： export interface ObserverOptions | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：ObserverOptions；  API声明：id: string;  差异内容：id: string; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：uiObserver；  API声明： export class RouterPageInfo  差异内容： export class RouterPageInfo | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：RouterPageInfo；  API声明：context: UIAbilityContext | UIContext;  差异内容：context: UIAbilityContext | UIContext; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：RouterPageInfo；  API声明：index: number;  差异内容：index: number; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：RouterPageInfo；  API声明：name: string;  差异内容：name: string; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：RouterPageInfo；  API声明：path: string;  差异内容：path: string; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：RouterPageInfo；  API声明：state: RouterPageState;  差异内容：state: RouterPageState; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：RouterPageInfo；  API声明：pageId: string;  差异内容：pageId: string; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：uiObserver；  API声明： export class DensityInfo  差异内容： export class DensityInfo | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：DensityInfo；  API声明：context: UIContext;  差异内容：context: UIContext; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：DensityInfo；  API声明：density: number;  差异内容：density: number; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：uiObserver；  API声明： export interface NavDestinationSwitchInfo  差异内容： export interface NavDestinationSwitchInfo | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：NavDestinationSwitchInfo；  API声明：context: UIAbilityContext | UIContext;  差异内容：context: UIAbilityContext | UIContext; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：NavDestinationSwitchInfo；  API声明：from: NavDestinationInfo | NavBar;  差异内容：from: NavDestinationInfo | NavBar; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：NavDestinationSwitchInfo；  API声明：to: NavDestinationInfo | NavBar;  差异内容：to: NavDestinationInfo | NavBar; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：NavDestinationSwitchInfo；  API声明：operation: NavigationOperation;  差异内容：operation: NavigationOperation; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：uiObserver；  API声明： export interface NavDestinationSwitchObserverOptions  差异内容： export interface NavDestinationSwitchObserverOptions | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：NavDestinationSwitchObserverOptions；  API声明：navigationId: ResourceStr;  差异内容：navigationId: ResourceStr; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：uiObserver；  API声明：export function on(type: 'navDestinationUpdate', options: {  navigationId: ResourceStr;  }, callback: Callback<NavDestinationInfo>): void;  差异内容：export function on(type: 'navDestinationUpdate', options: {  navigationId: ResourceStr;  }, callback: Callback<NavDestinationInfo>): void; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：uiObserver；  API声明：export function on(type: 'navDestinationUpdate', callback: Callback<NavDestinationInfo>): void;  差异内容：export function on(type: 'navDestinationUpdate', callback: Callback<NavDestinationInfo>): void; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：uiObserver；  API声明：export function off(type: 'navDestinationUpdate', options: {  navigationId: ResourceStr;  }, callback?: Callback<NavDestinationInfo>): void;  差异内容：export function off(type: 'navDestinationUpdate', options: {  navigationId: ResourceStr;  }, callback?: Callback<NavDestinationInfo>): void; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：uiObserver；  API声明：export function off(type: 'navDestinationUpdate', callback?: Callback<NavDestinationInfo>): void;  差异内容：export function off(type: 'navDestinationUpdate', callback?: Callback<NavDestinationInfo>): void; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：uiObserver；  API声明：export function on(type: 'scrollEvent', options: ObserverOptions, callback: Callback<ScrollEventInfo>): void;  差异内容：export function on(type: 'scrollEvent', options: ObserverOptions, callback: Callback<ScrollEventInfo>): void; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：uiObserver；  API声明：export function on(type: 'scrollEvent', callback: Callback<ScrollEventInfo>): void;  差异内容：export function on(type: 'scrollEvent', callback: Callback<ScrollEventInfo>): void; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：uiObserver；  API声明：export function off(type: 'scrollEvent', options: ObserverOptions, callback?: Callback<ScrollEventInfo>): void;  差异内容：export function off(type: 'scrollEvent', options: ObserverOptions, callback?: Callback<ScrollEventInfo>): void; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：uiObserver；  API声明：export function off(type: 'scrollEvent', callback?: Callback<ScrollEventInfo>): void;  差异内容：export function off(type: 'scrollEvent', callback?: Callback<ScrollEventInfo>): void; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：uiObserver；  API声明：export function on(type: 'routerPageUpdate', context: UIAbilityContext | UIContext, callback: Callback<RouterPageInfo>): void;  差异内容：export function on(type: 'routerPageUpdate', context: UIAbilityContext | UIContext, callback: Callback<RouterPageInfo>): void; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：uiObserver；  API声明：export function off(type: 'routerPageUpdate', context: UIAbilityContext | UIContext, callback?: Callback<RouterPageInfo>): void;  差异内容：export function off(type: 'routerPageUpdate', context: UIAbilityContext | UIContext, callback?: Callback<RouterPageInfo>): void; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：uiObserver；  API声明：export function on(type: 'densityUpdate', context: UIContext, callback: Callback<DensityInfo>): void;  差异内容：export function on(type: 'densityUpdate', context: UIContext, callback: Callback<DensityInfo>): void; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：uiObserver；  API声明：export function off(type: 'densityUpdate', context: UIContext, callback?: Callback<DensityInfo>): void;  差异内容：export function off(type: 'densityUpdate', context: UIContext, callback?: Callback<DensityInfo>): void; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：uiObserver；  API声明：export function on(type: 'willDraw', context: UIContext, callback: Callback<void>): void;  差异内容：export function on(type: 'willDraw', context: UIContext, callback: Callback<void>): void; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：uiObserver；  API声明：export function off(type: 'willDraw', context: UIContext, callback?: Callback<void>): void;  差异内容：export function off(type: 'willDraw', context: UIContext, callback?: Callback<void>): void; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：uiObserver；  API声明：export function on(type: 'didLayout', context: UIContext, callback: Callback<void>): void;  差异内容：export function on(type: 'didLayout', context: UIContext, callback: Callback<void>): void; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：uiObserver；  API声明：export function off(type: 'didLayout', context: UIContext, callback?: Callback<void>): void;  差异内容：export function off(type: 'didLayout', context: UIContext, callback?: Callback<void>): void; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：uiObserver；  API声明：export function on(type: 'navDestinationSwitch', context: UIAbilityContext | UIContext, callback: Callback<NavDestinationSwitchInfo>): void;  差异内容：export function on(type: 'navDestinationSwitch', context: UIAbilityContext | UIContext, callback: Callback<NavDestinationSwitchInfo>): void; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：uiObserver；  API声明：export function on(type: 'navDestinationSwitch', context: UIAbilityContext | UIContext, observerOptions: NavDestinationSwitchObserverOptions, callback: Callback<NavDestinationSwitchInfo>): void;  差异内容：export function on(type: 'navDestinationSwitch', context: UIAbilityContext | UIContext, observerOptions: NavDestinationSwitchObserverOptions, callback: Callback<NavDestinationSwitchInfo>): void; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：uiObserver；  API声明：export function off(type: 'navDestinationSwitch', context: UIAbilityContext | UIContext, callback?: Callback<NavDestinationSwitchInfo>): void;  差异内容：export function off(type: 'navDestinationSwitch', context: UIAbilityContext | UIContext, callback?: Callback<NavDestinationSwitchInfo>): void; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：uiObserver；  API声明：export function off(type: 'navDestinationSwitch', context: UIAbilityContext | UIContext, observerOptions: NavDestinationSwitchObserverOptions, callback?: Callback<NavDestinationSwitchInfo>): void;  差异内容：export function off(type: 'navDestinationSwitch', context: UIAbilityContext | UIContext, observerOptions: NavDestinationSwitchObserverOptions, callback?: Callback<NavDestinationSwitchInfo>): void; | api/@ohos.arkui.observer.d.ts |
| 新增API | NA | 类名：global；  API声明： interface ShapeSize  差异内容： interface ShapeSize | api/@ohos.arkui.shape.d.ts |
| 新增API | NA | 类名：ShapeSize；  API声明：width?: number | string;  差异内容：width?: number | string; | api/@ohos.arkui.shape.d.ts |
| 新增API | NA | 类名：ShapeSize；  API声明：height?: number | string;  差异内容：height?: number | string; | api/@ohos.arkui.shape.d.ts |
| 新增API | NA | 类名：global；  API声明： interface RectShapeOptions  差异内容： interface RectShapeOptions | api/@ohos.arkui.shape.d.ts |
| 新增API | NA | 类名：RectShapeOptions；  API声明：radius?: number | string | Array<number | string>;  差异内容：radius?: number | string | Array<number | string>; | api/@ohos.arkui.shape.d.ts |
| 新增API | NA | 类名：global；  API声明： interface RoundRectShapeOptions  差异内容： interface RoundRectShapeOptions | api/@ohos.arkui.shape.d.ts |
| 新增API | NA | 类名：RoundRectShapeOptions；  API声明：radiusWidth?: number | string;  差异内容：radiusWidth?: number | string; | api/@ohos.arkui.shape.d.ts |
| 新增API | NA | 类名：RoundRectShapeOptions；  API声明：radiusHeight?: number | string;  差异内容：radiusHeight?: number | string; | api/@ohos.arkui.shape.d.ts |
| 新增API | NA | 类名：global；  API声明： interface PathShapeOptions  差异内容： interface PathShapeOptions | api/@ohos.arkui.shape.d.ts |
| 新增API | NA | 类名：PathShapeOptions；  API声明：commands?: string;  差异内容：commands?: string; | api/@ohos.arkui.shape.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class CommonShapeMethod  差异内容： declare class CommonShapeMethod | api/@ohos.arkui.shape.d.ts |
| 新增API | NA | 类名：CommonShapeMethod；  API声明：offset(offset: Position): T;  差异内容：offset(offset: Position): T; | api/@ohos.arkui.shape.d.ts |
| 新增API | NA | 类名：CommonShapeMethod；  API声明：fill(color: ResourceColor): T;  差异内容：fill(color: ResourceColor): T; | api/@ohos.arkui.shape.d.ts |
| 新增API | NA | 类名：CommonShapeMethod；  API声明：position(position: Position): T;  差异内容：position(position: Position): T; | api/@ohos.arkui.shape.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class BaseShape  差异内容： declare class BaseShape | api/@ohos.arkui.shape.d.ts |
| 新增API | NA | 类名：BaseShape；  API声明：width(width: Length): T;  差异内容：width(width: Length): T; | api/@ohos.arkui.shape.d.ts |
| 新增API | NA | 类名：BaseShape；  API声明：height(height: Length): T;  差异内容：height(height: Length): T; | api/@ohos.arkui.shape.d.ts |
| 新增API | NA | 类名：BaseShape；  API声明：size(size: SizeOptions): T;  差异内容：size(size: SizeOptions): T; | api/@ohos.arkui.shape.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class RectShape  差异内容： export declare class RectShape | api/@ohos.arkui.shape.d.ts |
| 新增API | NA | 类名：RectShape；  API声明：radiusWidth(rWidth: number | string): RectShape;  差异内容：radiusWidth(rWidth: number | string): RectShape; | api/@ohos.arkui.shape.d.ts |
| 新增API | NA | 类名：RectShape；  API声明：radiusHeight(rHeight: number | string): RectShape;  差异内容：radiusHeight(rHeight: number | string): RectShape; | api/@ohos.arkui.shape.d.ts |
| 新增API | NA | 类名：RectShape；  API声明：radius(radius: number | string | Array<number | string>): RectShape;  差异内容：radius(radius: number | string | Array<number | string>): RectShape; | api/@ohos.arkui.shape.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class CircleShape  差异内容： export declare class CircleShape | api/@ohos.arkui.shape.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class EllipseShape  差异内容： export declare class EllipseShape | api/@ohos.arkui.shape.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class PathShape  差异内容： export declare class PathShape | api/@ohos.arkui.shape.d.ts |
| 新增API | NA | 类名：PathShape；  API声明：commands(commands: string): PathShape;  差异内容：commands(commands: string): PathShape; | api/@ohos.arkui.shape.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare interface Theme  差异内容： export declare interface Theme | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：Theme；  API声明：colors: Colors;  差异内容：colors: Colors; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare interface Colors  差异内容： export declare interface Colors | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：Colors；  API声明：brand: ResourceColor;  差异内容：brand: ResourceColor; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：Colors；  API声明：warning: ResourceColor;  差异内容：warning: ResourceColor; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：Colors；  API声明：alert: ResourceColor;  差异内容：alert: ResourceColor; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：Colors；  API声明：confirm: ResourceColor;  差异内容：confirm: ResourceColor; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：Colors；  API声明：fontPrimary: ResourceColor;  差异内容：fontPrimary: ResourceColor; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：Colors；  API声明：fontSecondary: ResourceColor;  差异内容：fontSecondary: ResourceColor; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：Colors；  API声明：fontTertiary: ResourceColor;  差异内容：fontTertiary: ResourceColor; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：Colors；  API声明：fontFourth: ResourceColor;  差异内容：fontFourth: ResourceColor; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：Colors；  API声明：fontEmphasize: ResourceColor;  差异内容：fontEmphasize: ResourceColor; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：Colors；  API声明：fontOnPrimary: ResourceColor;  差异内容：fontOnPrimary: ResourceColor; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：Colors；  API声明：fontOnSecondary: ResourceColor;  差异内容：fontOnSecondary: ResourceColor; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：Colors；  API声明：fontOnTertiary: ResourceColor;  差异内容：fontOnTertiary: ResourceColor; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：Colors；  API声明：fontOnFourth: ResourceColor;  差异内容：fontOnFourth: ResourceColor; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：Colors；  API声明：iconPrimary: ResourceColor;  差异内容：iconPrimary: ResourceColor; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：Colors；  API声明：iconSecondary: ResourceColor;  差异内容：iconSecondary: ResourceColor; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：Colors；  API声明：iconTertiary: ResourceColor;  差异内容：iconTertiary: ResourceColor; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：Colors；  API声明：iconFourth: ResourceColor;  差异内容：iconFourth: ResourceColor; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：Colors；  API声明：iconEmphasize: ResourceColor;  差异内容：iconEmphasize: ResourceColor; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：Colors；  API声明：iconSubEmphasize: ResourceColor;  差异内容：iconSubEmphasize: ResourceColor; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：Colors；  API声明：iconOnPrimary: ResourceColor;  差异内容：iconOnPrimary: ResourceColor; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：Colors；  API声明：iconOnSecondary: ResourceColor;  差异内容：iconOnSecondary: ResourceColor; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：Colors；  API声明：iconOnTertiary: ResourceColor;  差异内容：iconOnTertiary: ResourceColor; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：Colors；  API声明：iconOnFourth: ResourceColor;  差异内容：iconOnFourth: ResourceColor; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：Colors；  API声明：backgroundPrimary: ResourceColor;  差异内容：backgroundPrimary: ResourceColor; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：Colors；  API声明：backgroundSecondary: ResourceColor;  差异内容：backgroundSecondary: ResourceColor; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：Colors；  API声明：backgroundTertiary: ResourceColor;  差异内容：backgroundTertiary: ResourceColor; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：Colors；  API声明：backgroundFourth: ResourceColor;  差异内容：backgroundFourth: ResourceColor; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：Colors；  API声明：backgroundEmphasize: ResourceColor;  差异内容：backgroundEmphasize: ResourceColor; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：Colors；  API声明：compForegroundPrimary: ResourceColor;  差异内容：compForegroundPrimary: ResourceColor; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：Colors；  API声明：compBackgroundPrimary: ResourceColor;  差异内容：compBackgroundPrimary: ResourceColor; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：Colors；  API声明：compBackgroundPrimaryTran: ResourceColor;  差异内容：compBackgroundPrimaryTran: ResourceColor; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：Colors；  API声明：compBackgroundPrimaryContrary: ResourceColor;  差异内容：compBackgroundPrimaryContrary: ResourceColor; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：Colors；  API声明：compBackgroundGray: ResourceColor;  差异内容：compBackgroundGray: ResourceColor; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：Colors；  API声明：compBackgroundSecondary: ResourceColor;  差异内容：compBackgroundSecondary: ResourceColor; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：Colors；  API声明：compBackgroundTertiary: ResourceColor;  差异内容：compBackgroundTertiary: ResourceColor; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：Colors；  API声明：compBackgroundEmphasize: ResourceColor;  差异内容：compBackgroundEmphasize: ResourceColor; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：Colors；  API声明：compBackgroundNeutral: ResourceColor;  差异内容：compBackgroundNeutral: ResourceColor; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：Colors；  API声明：compEmphasizeSecondary: ResourceColor;  差异内容：compEmphasizeSecondary: ResourceColor; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：Colors；  API声明：compEmphasizeTertiary: ResourceColor;  差异内容：compEmphasizeTertiary: ResourceColor; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：Colors；  API声明：compDivider: ResourceColor;  差异内容：compDivider: ResourceColor; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：Colors；  API声明：compCommonContrary: ResourceColor;  差异内容：compCommonContrary: ResourceColor; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：Colors；  API声明：compBackgroundFocus: ResourceColor;  差异内容：compBackgroundFocus: ResourceColor; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：Colors；  API声明：compFocusedPrimary: ResourceColor;  差异内容：compFocusedPrimary: ResourceColor; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：Colors；  API声明：compFocusedSecondary: ResourceColor;  差异内容：compFocusedSecondary: ResourceColor; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：Colors；  API声明：compFocusedTertiary: ResourceColor;  差异内容：compFocusedTertiary: ResourceColor; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：Colors；  API声明：interactiveHover: ResourceColor;  差异内容：interactiveHover: ResourceColor; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：Colors；  API声明：interactivePressed: ResourceColor;  差异内容：interactivePressed: ResourceColor; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：Colors；  API声明：interactiveFocus: ResourceColor;  差异内容：interactiveFocus: ResourceColor; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：Colors；  API声明：interactiveActive: ResourceColor;  差异内容：interactiveActive: ResourceColor; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：Colors；  API声明：interactiveSelect: ResourceColor;  差异内容：interactiveSelect: ResourceColor; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：Colors；  API声明：interactiveClick: ResourceColor;  差异内容：interactiveClick: ResourceColor; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare interface CustomTheme  差异内容： export declare interface CustomTheme | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：CustomTheme；  API声明：colors?: CustomColors;  差异内容：colors?: CustomColors; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：global；  API声明：export declare type CustomColors = Partial<Colors>;  差异内容：export declare type CustomColors = Partial<Colors>; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class ThemeControl  差异内容： export declare class ThemeControl | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：ThemeControl；  API声明：static setDefaultTheme(theme: CustomTheme): void;  差异内容：static setDefaultTheme(theme: CustomTheme): void; | api/@ohos.arkui.theme.d.ts |
| 新增API | NA | 类名：global；  API声明： export class Font  差异内容： export class Font | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：Font；  API声明：registerFont(options: font.FontOptions): void;  差异内容：registerFont(options: font.FontOptions): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：Font；  API声明：getSystemFontList(): Array<string>;  差异内容：getSystemFontList(): Array<string>; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：Font；  API声明：getFontByName(fontName: string): font.FontInfo;  差异内容：getFontByName(fontName: string): font.FontInfo; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：global；  API声明： export class MediaQuery  差异内容： export class MediaQuery | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：MediaQuery；  API声明：matchMediaSync(condition: string): mediaQuery.MediaQueryListener;  差异内容：matchMediaSync(condition: string): mediaQuery.MediaQueryListener; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：global；  API声明： export class UIInspector  差异内容： export class UIInspector | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIInspector；  API声明：createComponentObserver(id: string): inspector.ComponentObserver;  差异内容：createComponentObserver(id: string): inspector.ComponentObserver; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：global；  API声明： export class Router  差异内容： export class Router | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：Router；  API声明：pushUrl(options: router.RouterOptions, callback: AsyncCallback<void>): void;  差异内容：pushUrl(options: router.RouterOptions, callback: AsyncCallback<void>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：Router；  API声明：pushUrl(options: router.RouterOptions): Promise<void>;  差异内容：pushUrl(options: router.RouterOptions): Promise<void>; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：Router；  API声明：pushUrl(options: router.RouterOptions, mode: router.RouterMode, callback: AsyncCallback<void>): void;  差异内容：pushUrl(options: router.RouterOptions, mode: router.RouterMode, callback: AsyncCallback<void>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：Router；  API声明：pushUrl(options: router.RouterOptions, mode: router.RouterMode): Promise<void>;  差异内容：pushUrl(options: router.RouterOptions, mode: router.RouterMode): Promise<void>; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：Router；  API声明：replaceUrl(options: router.RouterOptions, callback: AsyncCallback<void>): void;  差异内容：replaceUrl(options: router.RouterOptions, callback: AsyncCallback<void>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：Router；  API声明：replaceUrl(options: router.RouterOptions): Promise<void>;  差异内容：replaceUrl(options: router.RouterOptions): Promise<void>; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：Router；  API声明：replaceUrl(options: router.RouterOptions, mode: router.RouterMode, callback: AsyncCallback<void>): void;  差异内容：replaceUrl(options: router.RouterOptions, mode: router.RouterMode, callback: AsyncCallback<void>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：Router；  API声明：replaceUrl(options: router.RouterOptions, mode: router.RouterMode): Promise<void>;  差异内容：replaceUrl(options: router.RouterOptions, mode: router.RouterMode): Promise<void>; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：Router；  API声明：back(options?: router.RouterOptions): void;  差异内容：back(options?: router.RouterOptions): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：Router；  API声明：back(index: number, params?: Object): void;  差异内容：back(index: number, params?: Object): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：Router；  API声明：clear(): void;  差异内容：clear(): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：Router；  API声明：getLength(): string;  差异内容：getLength(): string; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：Router；  API声明：getState(): router.RouterState;  差异内容：getState(): router.RouterState; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：Router；  API声明：getStateByIndex(index: number): router.RouterState | undefined;  差异内容：getStateByIndex(index: number): router.RouterState | undefined; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：Router；  API声明：getStateByUrl(url: string): Array<router.RouterState>;  差异内容：getStateByUrl(url: string): Array<router.RouterState>; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：Router；  API声明：showAlertBeforeBackPage(options: router.EnableAlertOptions): void;  差异内容：showAlertBeforeBackPage(options: router.EnableAlertOptions): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：Router；  API声明：hideAlertBeforeBackPage(): void;  差异内容：hideAlertBeforeBackPage(): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：Router；  API声明：getParams(): Object;  差异内容：getParams(): Object; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：Router；  API声明：pushNamedRoute(options: router.NamedRouterOptions, callback: AsyncCallback<void>): void;  差异内容：pushNamedRoute(options: router.NamedRouterOptions, callback: AsyncCallback<void>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：Router；  API声明：pushNamedRoute(options: router.NamedRouterOptions): Promise<void>;  差异内容：pushNamedRoute(options: router.NamedRouterOptions): Promise<void>; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：Router；  API声明：pushNamedRoute(options: router.NamedRouterOptions, mode: router.RouterMode, callback: AsyncCallback<void>): void;  差异内容：pushNamedRoute(options: router.NamedRouterOptions, mode: router.RouterMode, callback: AsyncCallback<void>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：Router；  API声明：pushNamedRoute(options: router.NamedRouterOptions, mode: router.RouterMode): Promise<void>;  差异内容：pushNamedRoute(options: router.NamedRouterOptions, mode: router.RouterMode): Promise<void>; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：Router；  API声明：replaceNamedRoute(options: router.NamedRouterOptions, callback: AsyncCallback<void>): void;  差异内容：replaceNamedRoute(options: router.NamedRouterOptions, callback: AsyncCallback<void>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：Router；  API声明：replaceNamedRoute(options: router.NamedRouterOptions): Promise<void>;  差异内容：replaceNamedRoute(options: router.NamedRouterOptions): Promise<void>; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：Router；  API声明：replaceNamedRoute(options: router.NamedRouterOptions, mode: router.RouterMode, callback: AsyncCallback<void>): void;  差异内容：replaceNamedRoute(options: router.NamedRouterOptions, mode: router.RouterMode, callback: AsyncCallback<void>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：Router；  API声明：replaceNamedRoute(options: router.NamedRouterOptions, mode: router.RouterMode): Promise<void>;  差异内容：replaceNamedRoute(options: router.NamedRouterOptions, mode: router.RouterMode): Promise<void>; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：global；  API声明： export class PromptAction  差异内容： export class PromptAction | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：PromptAction；  API声明：showToast(options: promptAction.ShowToastOptions): void;  差异内容：showToast(options: promptAction.ShowToastOptions): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：PromptAction；  API声明：showDialog(options: promptAction.ShowDialogOptions, callback: AsyncCallback<promptAction.ShowDialogSuccessResponse>): void;  差异内容：showDialog(options: promptAction.ShowDialogOptions, callback: AsyncCallback<promptAction.ShowDialogSuccessResponse>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：PromptAction；  API声明：showDialog(options: promptAction.ShowDialogOptions): Promise<promptAction.ShowDialogSuccessResponse>;  差异内容：showDialog(options: promptAction.ShowDialogOptions): Promise<promptAction.ShowDialogSuccessResponse>; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：PromptAction；  API声明：showActionMenu(options: promptAction.ActionMenuOptions, callback: promptAction.ActionMenuSuccessResponse): void;  差异内容：showActionMenu(options: promptAction.ActionMenuOptions, callback: promptAction.ActionMenuSuccessResponse): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：PromptAction；  API声明：showActionMenu(options: promptAction.ActionMenuOptions, callback: AsyncCallback<promptAction.ActionMenuSuccessResponse>): void;  差异内容：showActionMenu(options: promptAction.ActionMenuOptions, callback: AsyncCallback<promptAction.ActionMenuSuccessResponse>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：PromptAction；  API声明：showActionMenu(options: promptAction.ActionMenuOptions): Promise<promptAction.ActionMenuSuccessResponse>;  差异内容：showActionMenu(options: promptAction.ActionMenuOptions): Promise<promptAction.ActionMenuSuccessResponse>; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：PromptAction；  API声明：openCustomDialog<T extends Object>(dialogContent: ComponentContent<T>, options?: promptAction.BaseDialogOptions): Promise<void>;  差异内容：openCustomDialog<T extends Object>(dialogContent: ComponentContent<T>, options?: promptAction.BaseDialogOptions): Promise<void>; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：PromptAction；  API声明：updateCustomDialog<T extends Object>(dialogContent: ComponentContent<T>, options: promptAction.BaseDialogOptions): Promise<void>;  差异内容：updateCustomDialog<T extends Object>(dialogContent: ComponentContent<T>, options: promptAction.BaseDialogOptions): Promise<void>; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：PromptAction；  API声明：closeCustomDialog<T extends Object>(dialogContent: ComponentContent<T>): Promise<void>;  差异内容：closeCustomDialog<T extends Object>(dialogContent: ComponentContent<T>): Promise<void>; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type ClickEventListenerCallback = (event: ClickEvent, node?: FrameNode) => void;  差异内容：declare type ClickEventListenerCallback = (event: ClickEvent, node?: FrameNode) => void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type GestureEventListenerCallback = (event: GestureEvent, node?: FrameNode) => void;  差异内容：declare type GestureEventListenerCallback = (event: GestureEvent, node?: FrameNode) => void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：global；  API声明： export class UIObserver  差异内容： export class UIObserver | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIObserver；  API声明：on(type: 'navDestinationUpdate', options: {  navigationId: ResourceStr;  }, callback: Callback<observer.NavDestinationInfo>): void;  差异内容：on(type: 'navDestinationUpdate', options: {  navigationId: ResourceStr;  }, callback: Callback<observer.NavDestinationInfo>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIObserver；  API声明：on(type: 'navDestinationUpdate', callback: Callback<observer.NavDestinationInfo>): void;  差异内容：on(type: 'navDestinationUpdate', callback: Callback<observer.NavDestinationInfo>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIObserver；  API声明：off(type: 'navDestinationUpdate', options: {  navigationId: ResourceStr;  }, callback?: Callback<observer.NavDestinationInfo>): void;  差异内容：off(type: 'navDestinationUpdate', options: {  navigationId: ResourceStr;  }, callback?: Callback<observer.NavDestinationInfo>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIObserver；  API声明：off(type: 'navDestinationUpdate', callback?: Callback<observer.NavDestinationInfo>): void;  差异内容：off(type: 'navDestinationUpdate', callback?: Callback<observer.NavDestinationInfo>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIObserver；  API声明：on(type: 'scrollEvent', options: observer.ObserverOptions, callback: Callback<observer.ScrollEventInfo>): void;  差异内容：on(type: 'scrollEvent', options: observer.ObserverOptions, callback: Callback<observer.ScrollEventInfo>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIObserver；  API声明：on(type: 'scrollEvent', callback: Callback<observer.ScrollEventInfo>): void;  差异内容：on(type: 'scrollEvent', callback: Callback<observer.ScrollEventInfo>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIObserver；  API声明：off(type: 'scrollEvent', options: observer.ObserverOptions, callback?: Callback<observer.ScrollEventInfo>): void;  差异内容：off(type: 'scrollEvent', options: observer.ObserverOptions, callback?: Callback<observer.ScrollEventInfo>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIObserver；  API声明：off(type: 'scrollEvent', callback?: Callback<observer.ScrollEventInfo>): void;  差异内容：off(type: 'scrollEvent', callback?: Callback<observer.ScrollEventInfo>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIObserver；  API声明：on(type: 'routerPageUpdate', callback: Callback<observer.RouterPageInfo>): void;  差异内容：on(type: 'routerPageUpdate', callback: Callback<observer.RouterPageInfo>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIObserver；  API声明：off(type: 'routerPageUpdate', callback?: Callback<observer.RouterPageInfo>): void;  差异内容：off(type: 'routerPageUpdate', callback?: Callback<observer.RouterPageInfo>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIObserver；  API声明：on(type: 'densityUpdate', callback: Callback<observer.DensityInfo>): void;  差异内容：on(type: 'densityUpdate', callback: Callback<observer.DensityInfo>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIObserver；  API声明：off(type: 'densityUpdate', callback?: Callback<observer.DensityInfo>): void;  差异内容：off(type: 'densityUpdate', callback?: Callback<observer.DensityInfo>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIObserver；  API声明：on(type: 'willDraw', callback: Callback<void>): void;  差异内容：on(type: 'willDraw', callback: Callback<void>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIObserver；  API声明：off(type: 'willDraw', callback?: Callback<void>): void;  差异内容：off(type: 'willDraw', callback?: Callback<void>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIObserver；  API声明：on(type: 'didLayout', callback: Callback<void>): void;  差异内容：on(type: 'didLayout', callback: Callback<void>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIObserver；  API声明：off(type: 'didLayout', callback?: Callback<void>): void;  差异内容：off(type: 'didLayout', callback?: Callback<void>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIObserver；  API声明：on(type: 'navDestinationSwitch', callback: Callback<observer.NavDestinationSwitchInfo>): void;  差异内容：on(type: 'navDestinationSwitch', callback: Callback<observer.NavDestinationSwitchInfo>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIObserver；  API声明：on(type: 'navDestinationSwitch', observerOptions: observer.NavDestinationSwitchObserverOptions, callback: Callback<observer.NavDestinationSwitchInfo>): void;  差异内容：on(type: 'navDestinationSwitch', observerOptions: observer.NavDestinationSwitchObserverOptions, callback: Callback<observer.NavDestinationSwitchInfo>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIObserver；  API声明：off(type: 'navDestinationSwitch', callback?: Callback<observer.NavDestinationSwitchInfo>): void;  差异内容：off(type: 'navDestinationSwitch', callback?: Callback<observer.NavDestinationSwitchInfo>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIObserver；  API声明：off(type: 'navDestinationSwitch', observerOptions: observer.NavDestinationSwitchObserverOptions, callback?: Callback<observer.NavDestinationSwitchInfo>): void;  差异内容：off(type: 'navDestinationSwitch', observerOptions: observer.NavDestinationSwitchObserverOptions, callback?: Callback<observer.NavDestinationSwitchInfo>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIObserver；  API声明：on(type: 'willClick', callback: ClickEventListenerCallback): void;  差异内容：on(type: 'willClick', callback: ClickEventListenerCallback): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIObserver；  API声明：on(type: 'willClick', callback: GestureEventListenerCallback): void;  差异内容：on(type: 'willClick', callback: GestureEventListenerCallback): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIObserver；  API声明：off(type: 'willClick', callback?: ClickEventListenerCallback): void;  差异内容：off(type: 'willClick', callback?: ClickEventListenerCallback): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIObserver；  API声明：off(type: 'willClick', callback?: GestureEventListenerCallback): void;  差异内容：off(type: 'willClick', callback?: GestureEventListenerCallback): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIObserver；  API声明：on(type: 'didClick', callback: ClickEventListenerCallback): void;  差异内容：on(type: 'didClick', callback: ClickEventListenerCallback): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIObserver；  API声明：on(type: 'didClick', callback: GestureEventListenerCallback): void;  差异内容：on(type: 'didClick', callback: GestureEventListenerCallback): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIObserver；  API声明：off(type: 'didClick', callback?: ClickEventListenerCallback): void;  差异内容：off(type: 'didClick', callback?: ClickEventListenerCallback): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIObserver；  API声明：off(type: 'didClick', callback?: GestureEventListenerCallback): void;  差异内容：off(type: 'didClick', callback?: GestureEventListenerCallback): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：global；  API声明： export class ComponentUtils  差异内容： export class ComponentUtils | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：ComponentUtils；  API声明：getRectangleById(id: string): componentUtils.ComponentInfo;  差异内容：getRectangleById(id: string): componentUtils.ComponentInfo; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：global；  API声明： export class OverlayManager  差异内容： export class OverlayManager | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：OverlayManager；  API声明：addComponentContent(content: ComponentContent, index?: number): void;  差异内容：addComponentContent(content: ComponentContent, index?: number): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：OverlayManager；  API声明：removeComponentContent(content: ComponentContent): void;  差异内容：removeComponentContent(content: ComponentContent): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：OverlayManager；  API声明：showComponentContent(content: ComponentContent): void;  差异内容：showComponentContent(content: ComponentContent): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：OverlayManager；  API声明：hideComponentContent(content: ComponentContent): void;  差异内容：hideComponentContent(content: ComponentContent): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：OverlayManager；  API声明：showAllComponentContents(): void;  差异内容：showAllComponentContents(): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：OverlayManager；  API声明：hideAllComponentContents(): void;  差异内容：hideAllComponentContents(): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：global；  API声明： export interface AtomicServiceBar  差异内容： export interface AtomicServiceBar | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：AtomicServiceBar；  API声明：setVisible(visible: boolean): void;  差异内容：setVisible(visible: boolean): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：AtomicServiceBar；  API声明：setBackgroundColor(color: Nullable<Color | number | string>): void;  差异内容：setBackgroundColor(color: Nullable<Color | number | string>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：AtomicServiceBar；  API声明：setTitleContent(content: string): void;  差异内容：setTitleContent(content: string): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：AtomicServiceBar；  API声明：setTitleFontStyle(font: FontStyle): void;  差异内容：setTitleFontStyle(font: FontStyle): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：AtomicServiceBar；  API声明：setIconColor(color: Nullable<Color | number | string>): void;  差异内容：setIconColor(color: Nullable<Color | number | string>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：global；  API声明： export class DragController  差异内容： export class DragController | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：DragController；  API声明：executeDrag(custom: CustomBuilder | DragItemInfo, dragInfo: dragController.DragInfo, callback: AsyncCallback<{  event: DragEvent;  extraParams: string;  }>): void;  差异内容：executeDrag(custom: CustomBuilder | DragItemInfo, dragInfo: dragController.DragInfo, callback: AsyncCallback<{  event: DragEvent;  extraParams: string;  }>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：DragController；  API声明：executeDrag(custom: CustomBuilder | DragItemInfo, dragInfo: dragController.DragInfo): Promise<{  event: DragEvent;  extraParams: string;  }>;  差异内容：executeDrag(custom: CustomBuilder | DragItemInfo, dragInfo: dragController.DragInfo): Promise<{  event: DragEvent;  extraParams: string;  }>; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：DragController；  API声明：createDragAction(customArray: Array<CustomBuilder | DragItemInfo>, dragInfo: dragController.DragInfo): dragController.DragAction;  差异内容：createDragAction(customArray: Array<CustomBuilder | DragItemInfo>, dragInfo: dragController.DragInfo): dragController.DragAction; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：DragController；  API声明：getDragPreview(): dragController.DragPreview;  差异内容：getDragPreview(): dragController.DragPreview; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：DragController；  API声明：setDragEventStrictReportingEnabled(enable: boolean): void;  差异内容：setDragEventStrictReportingEnabled(enable: boolean): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：global；  API声明： export class MeasureUtils  差异内容： export class MeasureUtils | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：MeasureUtils；  API声明：measureText(options: MeasureOptions): number;  差异内容：measureText(options: MeasureOptions): number; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：MeasureUtils；  API声明：measureTextSize(options: MeasureOptions): SizeOptions;  差异内容：measureTextSize(options: MeasureOptions): SizeOptions; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：global；  API声明： export class FocusController  差异内容： export class FocusController | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：FocusController；  API声明：clearFocus(): void;  差异内容：clearFocus(): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：FocusController；  API声明：requestFocus(key: string): void;  差异内容：requestFocus(key: string): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：global；  API声明：export type PointerStyle = pointer.PointerStyle;  差异内容：export type PointerStyle = pointer.PointerStyle; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：global；  API声明： export class CursorController  差异内容： export class CursorController | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：CursorController；  API声明：restoreDefault(): void;  差异内容：restoreDefault(): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：CursorController；  API声明：setCursor(value: PointerStyle): void;  差异内容：setCursor(value: PointerStyle): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：global；  API声明： export class ContextMenuController  差异内容： export class ContextMenuController | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：ContextMenuController；  API声明：close(): void;  差异内容：close(): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：global；  API声明：export type Context = common.Context;  差异内容：export type Context = common.Context; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：global；  API声明： export class ComponentSnapshot  差异内容： export class ComponentSnapshot | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：ComponentSnapshot；  API声明：get(id: string, callback: AsyncCallback<image.PixelMap>): void;  差异内容：get(id: string, callback: AsyncCallback<image.PixelMap>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：ComponentSnapshot；  API声明：get(id: string): Promise<image.PixelMap>;  差异内容：get(id: string): Promise<image.PixelMap>; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：ComponentSnapshot；  API声明：createFromBuilder(builder: CustomBuilder, callback: AsyncCallback<image.PixelMap>): void;  差异内容：createFromBuilder(builder: CustomBuilder, callback: AsyncCallback<image.PixelMap>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：ComponentSnapshot；  API声明：createFromBuilder(builder: CustomBuilder): Promise<image.PixelMap>;  差异内容：createFromBuilder(builder: CustomBuilder): Promise<image.PixelMap>; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：global；  API声明： export class UIContext  差异内容： export class UIContext | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：getFont(): Font;  差异内容：getFont(): Font; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：getMediaQuery(): MediaQuery;  差异内容：getMediaQuery(): MediaQuery; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：getUIInspector(): UIInspector;  差异内容：getUIInspector(): UIInspector; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：getFilteredInspectorTree(filters?: Array<string>): string;  差异内容：getFilteredInspectorTree(filters?: Array<string>): string; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：getFilteredInspectorTreeById(id: string, depth: number, filters?: Array<string>): string;  差异内容：getFilteredInspectorTreeById(id: string, depth: number, filters?: Array<string>): string; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：getRouter(): Router;  差异内容：getRouter(): Router; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：getPromptAction(): PromptAction;  差异内容：getPromptAction(): PromptAction; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：getComponentUtils(): ComponentUtils;  差异内容：getComponentUtils(): ComponentUtils; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：getUIObserver(): UIObserver;  差异内容：getUIObserver(): UIObserver; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：getOverlayManager(): OverlayManager;  差异内容：getOverlayManager(): OverlayManager; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：createAnimator(options: AnimatorOptions): AnimatorResult;  差异内容：createAnimator(options: AnimatorOptions): AnimatorResult; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：animateTo(value: AnimateParam, event: () => void): void;  差异内容：animateTo(value: AnimateParam, event: () => void): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：showAlertDialog(options: AlertDialogParamWithConfirm | AlertDialogParamWithButtons | AlertDialogParamWithOptions): void;  差异内容：showAlertDialog(options: AlertDialogParamWithConfirm | AlertDialogParamWithButtons | AlertDialogParamWithOptions): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：showActionSheet(value: ActionSheetOptions): void;  差异内容：showActionSheet(value: ActionSheetOptions): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：showDatePickerDialog(options: DatePickerDialogOptions): void;  差异内容：showDatePickerDialog(options: DatePickerDialogOptions): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：showTimePickerDialog(options: TimePickerDialogOptions): void;  差异内容：showTimePickerDialog(options: TimePickerDialogOptions): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：showTextPickerDialog(options: TextPickerDialogOptions): void;  差异内容：showTextPickerDialog(options: TextPickerDialogOptions): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：runScopedTask(callback: () => void): void;  差异内容：runScopedTask(callback: () => void): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：setKeyboardAvoidMode(value: KeyboardAvoidMode): void;  差异内容：setKeyboardAvoidMode(value: KeyboardAvoidMode): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：getKeyboardAvoidMode(): KeyboardAvoidMode;  差异内容：getKeyboardAvoidMode(): KeyboardAvoidMode; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：getAtomicServiceBar(): Nullable<AtomicServiceBar>;  差异内容：getAtomicServiceBar(): Nullable<AtomicServiceBar>; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：getDragController(): DragController;  差异内容：getDragController(): DragController; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：getMeasureUtils(): MeasureUtils;  差异内容：getMeasureUtils(): MeasureUtils; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：keyframeAnimateTo(param: KeyframeAnimateParam, keyframes: Array<KeyframeState>): void;  差异内容：keyframeAnimateTo(param: KeyframeAnimateParam, keyframes: Array<KeyframeState>): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：getFocusController(): FocusController;  差异内容：getFocusController(): FocusController; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：getFrameNodeById(id: string): FrameNode | null;  差异内容：getFrameNodeById(id: string): FrameNode | null; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：getFrameNodeByUniqueId(id: number): FrameNode | null;  差异内容：getFrameNodeByUniqueId(id: number): FrameNode | null; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：getCursorController(): CursorController;  差异内容：getCursorController(): CursorController; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：getContextMenuController(): ContextMenuController;  差异内容：getContextMenuController(): ContextMenuController; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：getComponentSnapshot(): ComponentSnapshot;  差异内容：getComponentSnapshot(): ComponentSnapshot; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：vp2px(value: number): number;  差异内容：vp2px(value: number): number; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：px2vp(value: number): number;  差异内容：px2vp(value: number): number; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：fp2px(value: number): number;  差异内容：fp2px(value: number): number; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：px2fp(value: number): number;  差异内容：px2fp(value: number): number; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：lpx2px(value: number): number;  差异内容：lpx2px(value: number): number; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：px2lpx(value: number): number;  差异内容：px2lpx(value: number): number; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：getSharedLocalStorage(): LocalStorage | undefined;  差异内容：getSharedLocalStorage(): LocalStorage | undefined; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：getHostContext(): Context | undefined;  差异内容：getHostContext(): Context | undefined; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：UIContext；  API声明：getWindowName(): string | undefined;  差异内容：getWindowName(): string | undefined; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：global；  API声明： export const enum KeyboardAvoidMode  差异内容： export const enum KeyboardAvoidMode | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：KeyboardAvoidMode；  API声明：OFFSET = 0  差异内容：OFFSET = 0 | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：KeyboardAvoidMode；  API声明：RESIZE = 1  差异内容：RESIZE = 1 | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：global；  API声明： declare namespace uiExtension  差异内容： declare namespace uiExtension | api/@ohos.arkui.uiExtension.d.ts |
| 新增API | NA | 类名：uiExtension；  API声明： interface WindowProxy  差异内容： interface WindowProxy | api/@ohos.arkui.uiExtension.d.ts |
| 新增API | NA | 类名：WindowProxy；  API声明：getWindowAvoidArea(type: window.AvoidAreaType): window.AvoidArea;  差异内容：getWindowAvoidArea(type: window.AvoidAreaType): window.AvoidArea; | api/@ohos.arkui.uiExtension.d.ts |
| 新增API | NA | 类名：WindowProxy；  API声明：on(type: 'avoidAreaChange', callback: Callback<AvoidAreaInfo>): void;  差异内容：on(type: 'avoidAreaChange', callback: Callback<AvoidAreaInfo>): void; | api/@ohos.arkui.uiExtension.d.ts |
| 新增API | NA | 类名：WindowProxy；  API声明：off(type: 'avoidAreaChange', callback?: Callback<AvoidAreaInfo>): void;  差异内容：off(type: 'avoidAreaChange', callback?: Callback<AvoidAreaInfo>): void; | api/@ohos.arkui.uiExtension.d.ts |
| 新增API | NA | 类名：WindowProxy；  API声明：on(type: 'windowSizeChange', callback: Callback<window.Size>): void;  差异内容：on(type: 'windowSizeChange', callback: Callback<window.Size>): void; | api/@ohos.arkui.uiExtension.d.ts |
| 新增API | NA | 类名：WindowProxy；  API声明：off(type: 'windowSizeChange', callback?: Callback<window.Size>): void;  差异内容：off(type: 'windowSizeChange', callback?: Callback<window.Size>): void; | api/@ohos.arkui.uiExtension.d.ts |
| 新增API | NA | 类名：WindowProxy；  API声明：createSubWindowWithOptions(name: string, subWindowOptions: window.SubWindowOptions): Promise<window.Window>;  差异内容：createSubWindowWithOptions(name: string, subWindowOptions: window.SubWindowOptions): Promise<window.Window>; | api/@ohos.arkui.uiExtension.d.ts |
| 新增API | NA | 类名：uiExtension；  API声明： interface AvoidAreaInfo  差异内容： interface AvoidAreaInfo | api/@ohos.arkui.uiExtension.d.ts |
| 新增API | NA | 类名：AvoidAreaInfo；  API声明：type: window.AvoidAreaType;  差异内容：type: window.AvoidAreaType; | api/@ohos.arkui.uiExtension.d.ts |
| 新增API | NA | 类名：AvoidAreaInfo；  API声明：area: window.AvoidArea;  差异内容：area: window.AvoidArea; | api/@ohos.arkui.uiExtension.d.ts |
| 新增API | NA | 类名：global；  API声明： declare namespace PiPWindow  差异内容： declare namespace PiPWindow | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPWindow；  API声明：function isPiPEnabled(): boolean;  差异内容：function isPiPEnabled(): boolean; | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPWindow；  API声明：function create(config: PiPConfiguration): Promise<PiPController>;  差异内容：function create(config: PiPConfiguration): Promise<PiPController>; | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPWindow；  API声明： interface PiPConfiguration  差异内容： interface PiPConfiguration | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPConfiguration；  API声明：context: BaseContext;  差异内容：context: BaseContext; | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPConfiguration；  API声明：componentController: XComponentController;  差异内容：componentController: XComponentController; | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPConfiguration；  API声明：navigationId?: string;  差异内容：navigationId?: string; | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPConfiguration；  API声明：templateType?: PiPTemplateType;  差异内容：templateType?: PiPTemplateType; | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPConfiguration；  API声明：contentWidth?: number;  差异内容：contentWidth?: number; | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPConfiguration；  API声明：contentHeight?: number;  差异内容：contentHeight?: number; | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPConfiguration；  API声明：controlGroups?: Array<PiPControlGroup>;  差异内容：controlGroups?: Array<PiPControlGroup>; | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPWindow；  API声明： enum PiPTemplateType  差异内容： enum PiPTemplateType | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPTemplateType；  API声明：VIDEO\_PLAY  差异内容：VIDEO\_PLAY | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPTemplateType；  API声明：VIDEO\_CALL  差异内容：VIDEO\_CALL | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPTemplateType；  API声明：VIDEO\_MEETING  差异内容：VIDEO\_MEETING | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPTemplateType；  API声明：VIDEO\_LIVE  差异内容：VIDEO\_LIVE | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPWindow；  API声明： enum PiPState  差异内容： enum PiPState | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPState；  API声明：ABOUT\_TO\_START = 1  差异内容：ABOUT\_TO\_START = 1 | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPState；  API声明：STARTED = 2  差异内容：STARTED = 2 | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPState；  API声明：ABOUT\_TO\_STOP = 3  差异内容：ABOUT\_TO\_STOP = 3 | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPState；  API声明：STOPPED = 4  差异内容：STOPPED = 4 | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPState；  API声明：ABOUT\_TO\_RESTORE = 5  差异内容：ABOUT\_TO\_RESTORE = 5 | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPState；  API声明：ERROR = 6  差异内容：ERROR = 6 | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPWindow；  API声明：type PiPControlGroup = VideoPlayControlGroup | VideoCallControlGroup | VideoMeetingControlGroup;  差异内容：type PiPControlGroup = VideoPlayControlGroup | VideoCallControlGroup | VideoMeetingControlGroup; | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPWindow；  API声明： enum VideoPlayControlGroup  差异内容： enum VideoPlayControlGroup | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：VideoPlayControlGroup；  API声明：VIDEO\_PREVIOUS\_NEXT = 101  差异内容：VIDEO\_PREVIOUS\_NEXT = 101 | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：VideoPlayControlGroup；  API声明：FAST\_FORWARD\_BACKWARD = 102  差异内容：FAST\_FORWARD\_BACKWARD = 102 | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPWindow；  API声明： enum VideoCallControlGroup  差异内容： enum VideoCallControlGroup | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：VideoCallControlGroup；  API声明：MICROPHONE\_SWITCH = 201  差异内容：MICROPHONE\_SWITCH = 201 | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：VideoCallControlGroup；  API声明：HANG\_UP\_BUTTON = 202  差异内容：HANG\_UP\_BUTTON = 202 | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：VideoCallControlGroup；  API声明：CAMERA\_SWITCH = 203  差异内容：CAMERA\_SWITCH = 203 | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPWindow；  API声明： enum VideoMeetingControlGroup  差异内容： enum VideoMeetingControlGroup | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：VideoMeetingControlGroup；  API声明：HANG\_UP\_BUTTON = 301  差异内容：HANG\_UP\_BUTTON = 301 | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：VideoMeetingControlGroup；  API声明：CAMERA\_SWITCH = 302  差异内容：CAMERA\_SWITCH = 302 | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：VideoMeetingControlGroup；  API声明：MUTE\_SWITCH = 303  差异内容：MUTE\_SWITCH = 303 | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPWindow；  API声明：type PiPActionEventType = PiPVideoActionEvent | PiPCallActionEvent | PiPMeetingActionEvent | PiPLiveActionEvent;  差异内容：type PiPActionEventType = PiPVideoActionEvent | PiPCallActionEvent | PiPMeetingActionEvent | PiPLiveActionEvent; | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPWindow；  API声明：type PiPVideoActionEvent = 'playbackStateChanged' | 'nextVideo' | 'previousVideo' | 'fastForward' | 'fastBackward';  差异内容：type PiPVideoActionEvent = 'playbackStateChanged' | 'nextVideo' | 'previousVideo' | 'fastForward' | 'fastBackward'; | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPWindow；  API声明：type PiPCallActionEvent = 'hangUp' | 'micStateChanged' | 'videoStateChanged';  差异内容：type PiPCallActionEvent = 'hangUp' | 'micStateChanged' | 'videoStateChanged'; | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPWindow；  API声明：type PiPMeetingActionEvent = 'hangUp' | 'voiceStateChanged' | 'videoStateChanged';  差异内容：type PiPMeetingActionEvent = 'hangUp' | 'voiceStateChanged' | 'videoStateChanged'; | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPWindow；  API声明：type PiPLiveActionEvent = 'playbackStateChanged';  差异内容：type PiPLiveActionEvent = 'playbackStateChanged'; | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPWindow；  API声明：type ControlPanelActionEventCallback = (event: PiPActionEventType, status?: number) => void;  差异内容：type ControlPanelActionEventCallback = (event: PiPActionEventType, status?: number) => void; | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPWindow；  API声明： interface PiPController  差异内容： interface PiPController | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPController；  API声明：startPiP(): Promise<void>;  差异内容：startPiP(): Promise<void>; | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPController；  API声明：stopPiP(): Promise<void>;  差异内容：stopPiP(): Promise<void>; | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPController；  API声明：setAutoStartEnabled(enable: boolean): void;  差异内容：setAutoStartEnabled(enable: boolean): void; | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPController；  API声明：updateContentSize(width: number, height: number): void;  差异内容：updateContentSize(width: number, height: number): void; | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPController；  API声明：on(type: 'stateChange', callback: (state: PiPState, reason: string) => void): void;  差异内容：on(type: 'stateChange', callback: (state: PiPState, reason: string) => void): void; | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPController；  API声明：off(type: 'stateChange'): void;  差异内容：off(type: 'stateChange'): void; | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPController；  API声明：on(type: 'controlPanelActionEvent', callback: ControlPanelActionEventCallback): void;  差异内容：on(type: 'controlPanelActionEvent', callback: ControlPanelActionEventCallback): void; | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：PiPController；  API声明：off(type: 'controlPanelActionEvent'): void;  差异内容：off(type: 'controlPanelActionEvent'): void; | api/@ohos.PiPWindow.d.ts |
| 新增API | NA | 类名：global；  API声明： declare namespace screenshot  差异内容： declare namespace screenshot | api/@ohos.screenshot.d.ts |
| 新增API | NA | 类名：screenshot；  API声明：function pick(): Promise<PickInfo>;  差异内容：function pick(): Promise<PickInfo>; | api/@ohos.screenshot.d.ts |
| 新增API | NA | 类名：screenshot；  API声明： interface PickInfo  差异内容： interface PickInfo | api/@ohos.screenshot.d.ts |
| 新增API | NA | 类名：PickInfo；  API声明：pickRect: Rect;  差异内容：pickRect: Rect; | api/@ohos.screenshot.d.ts |
| 新增API | NA | 类名：PickInfo；  API声明：pixelMap: image.PixelMap;  差异内容：pixelMap: image.PixelMap; | api/@ohos.screenshot.d.ts |
| 新增API | NA | 类名：screenshot；  API声明： interface Rect  差异内容： interface Rect | api/@ohos.screenshot.d.ts |
| 新增API | NA | 类名：Rect；  API声明：left: number;  差异内容：left: number; | api/@ohos.screenshot.d.ts |
| 新增API | NA | 类名：Rect；  API声明：top: number;  差异内容：top: number; | api/@ohos.screenshot.d.ts |
| 新增API | NA | 类名：Rect；  API声明：width: number;  差异内容：width: number; | api/@ohos.screenshot.d.ts |
| 新增API | NA | 类名：Rect；  API声明：height: number;  差异内容：height: number; | api/@ohos.screenshot.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class AlphabetIndexerModifier  差异内容： export declare class AlphabetIndexerModifier | api/arkui/AlphabetIndexerModifier.d.ts |
| 新增API | NA | 类名：AlphabetIndexerModifier；  API声明：applyNormalAttribute?(instance: AlphabetIndexerAttribute): void;  差异内容：applyNormalAttribute?(instance: AlphabetIndexerAttribute): void; | api/arkui/AlphabetIndexerModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class BlankModifier  差异内容： export declare class BlankModifier | api/arkui/BlankModifier.d.ts |
| 新增API | NA | 类名：BlankModifier；  API声明：applyNormalAttribute?(instance: BlankAttribute): void;  差异内容：applyNormalAttribute?(instance: BlankAttribute): void; | api/arkui/BlankModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum NodeRenderType  差异内容： declare enum NodeRenderType | api/arkui/BuilderNode.d.ts |
| 新增API | NA | 类名：NodeRenderType；  API声明：RENDER\_TYPE\_DISPLAY = 0  差异内容：RENDER\_TYPE\_DISPLAY = 0 | api/arkui/BuilderNode.d.ts |
| 新增API | NA | 类名：NodeRenderType；  API声明：RENDER\_TYPE\_TEXTURE = 1  差异内容：RENDER\_TYPE\_TEXTURE = 1 | api/arkui/BuilderNode.d.ts |
| 新增API | NA | 类名：global；  API声明： export interface RenderOptions  差异内容： export interface RenderOptions | api/arkui/BuilderNode.d.ts |
| 新增API | NA | 类名：RenderOptions；  API声明：selfIdealSize?: Size;  差异内容：selfIdealSize?: Size; | api/arkui/BuilderNode.d.ts |
| 新增API | NA | 类名：RenderOptions；  API声明：type?: NodeRenderType;  差异内容：type?: NodeRenderType; | api/arkui/BuilderNode.d.ts |
| 新增API | NA | 类名：RenderOptions；  API声明：surfaceId?: string;  差异内容：surfaceId?: string; | api/arkui/BuilderNode.d.ts |
| 新增API | NA | 类名：global；  API声明： export class BuilderNode  差异内容： export class BuilderNode | api/arkui/BuilderNode.d.ts |
| 新增API | NA | 类名：BuilderNode；  API声明：build(builder: WrappedBuilder<Args>, arg?: Object): void;  差异内容：build(builder: WrappedBuilder<Args>, arg?: Object): void; | api/arkui/BuilderNode.d.ts |
| 新增API | NA | 类名：BuilderNode；  API声明：update(arg: Object): void;  差异内容：update(arg: Object): void; | api/arkui/BuilderNode.d.ts |
| 新增API | NA | 类名：BuilderNode；  API声明：getFrameNode(): FrameNode | null;  差异内容：getFrameNode(): FrameNode | null; | api/arkui/BuilderNode.d.ts |
| 新增API | NA | 类名：BuilderNode；  API声明：postTouchEvent(event: TouchEvent): boolean;  差异内容：postTouchEvent(event: TouchEvent): boolean; | api/arkui/BuilderNode.d.ts |
| 新增API | NA | 类名：BuilderNode；  API声明：dispose(): void;  差异内容：dispose(): void; | api/arkui/BuilderNode.d.ts |
| 新增API | NA | 类名：BuilderNode；  API声明：reuse(param?: Object): void;  差异内容：reuse(param?: Object): void; | api/arkui/BuilderNode.d.ts |
| 新增API | NA | 类名：BuilderNode；  API声明：recycle(): void;  差异内容：recycle(): void; | api/arkui/BuilderNode.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class ButtonModifier  差异内容： export declare class ButtonModifier | api/arkui/ButtonModifier.d.ts |
| 新增API | NA | 类名：ButtonModifier；  API声明：applyNormalAttribute?(instance: ButtonAttribute): void;  差异内容：applyNormalAttribute?(instance: ButtonAttribute): void; | api/arkui/ButtonModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class CalendarPickerModifier  差异内容： export declare class CalendarPickerModifier | api/arkui/CalendarPickerModifier.d.ts |
| 新增API | NA | 类名：CalendarPickerModifier；  API声明：applyNormalAttribute?(instance: CalendarPickerAttribute): void;  差异内容：applyNormalAttribute?(instance: CalendarPickerAttribute): void; | api/arkui/CalendarPickerModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class CheckboxGroupModifier  差异内容： export declare class CheckboxGroupModifier | api/arkui/CheckboxGroupModifier.d.ts |
| 新增API | NA | 类名：CheckboxGroupModifier；  API声明：applyNormalAttribute?(instance: CheckboxGroupAttribute): void;  差异内容：applyNormalAttribute?(instance: CheckboxGroupAttribute): void; | api/arkui/CheckboxGroupModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class CheckboxModifier  差异内容： export declare class CheckboxModifier | api/arkui/CheckboxModifier.d.ts |
| 新增API | NA | 类名：CheckboxModifier；  API声明：applyNormalAttribute?(instance: CheckboxAttribute): void;  差异内容：applyNormalAttribute?(instance: CheckboxAttribute): void; | api/arkui/CheckboxModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class ColumnModifier  差异内容： export declare class ColumnModifier | api/arkui/ColumnModifier.d.ts |
| 新增API | NA | 类名：ColumnModifier；  API声明：applyNormalAttribute?(instance: ColumnAttribute): void;  差异内容：applyNormalAttribute?(instance: ColumnAttribute): void; | api/arkui/ColumnModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class ColumnSplitModifier  差异内容： export declare class ColumnSplitModifier | api/arkui/ColumnSplitModifier.d.ts |
| 新增API | NA | 类名：ColumnSplitModifier；  API声明：applyNormalAttribute?(instance: ColumnSplitAttribute): void;  差异内容：applyNormalAttribute?(instance: ColumnSplitAttribute): void; | api/arkui/ColumnSplitModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class CommonModifier  差异内容： export declare class CommonModifier | api/arkui/CommonModifier.d.ts |
| 新增API | NA | 类名：CommonModifier；  API声明：applyNormalAttribute?(instance: CommonAttribute): void;  差异内容：applyNormalAttribute?(instance: CommonAttribute): void; | api/arkui/CommonModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export class ComponentContent  差异内容： export class ComponentContent | api/arkui/ComponentContent.d.ts |
| 新增API | NA | 类名：ComponentContent；  API声明：update(args: T): void;  差异内容：update(args: T): void; | api/arkui/ComponentContent.d.ts |
| 新增API | NA | 类名：ComponentContent；  API声明：reuse(param?: Object): void;  差异内容：reuse(param?: Object): void; | api/arkui/ComponentContent.d.ts |
| 新增API | NA | 类名：ComponentContent；  API声明：recycle(): void;  差异内容：recycle(): void; | api/arkui/ComponentContent.d.ts |
| 新增API | NA | 类名：global；  API声明： export abstract class Content  差异内容： export abstract class Content | api/arkui/Content.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class CounterModifier  差异内容： export declare class CounterModifier | api/arkui/CounterModifier.d.ts |
| 新增API | NA | 类名：CounterModifier；  API声明：applyNormalAttribute?(instance: CounterAttribute): void;  差异内容：applyNormalAttribute?(instance: CounterAttribute): void; | api/arkui/CounterModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class DataPanelModifier  差异内容： export declare class DataPanelModifier | api/arkui/DataPanelModifier.d.ts |
| 新增API | NA | 类名：DataPanelModifier；  API声明：applyNormalAttribute?(instance: DataPanelAttribute): void;  差异内容：applyNormalAttribute?(instance: DataPanelAttribute): void; | api/arkui/DataPanelModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class DatePickerModifier  差异内容： export declare class DatePickerModifier | api/arkui/DatePickerModifier.d.ts |
| 新增API | NA | 类名：DatePickerModifier；  API声明：applyNormalAttribute?(instance: DatePickerAttribute): void;  差异内容：applyNormalAttribute?(instance: DatePickerAttribute): void; | api/arkui/DatePickerModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class DividerModifier  差异内容： export declare class DividerModifier | api/arkui/DividerModifier.d.ts |
| 新增API | NA | 类名：DividerModifier；  API声明：applyNormalAttribute?(instance: DividerAttribute): void;  差异内容：applyNormalAttribute?(instance: DividerAttribute): void; | api/arkui/DividerModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class FormComponentModifier  差异内容： export declare class FormComponentModifier | api/arkui/FormComponentModifier.d.ts |
| 新增API | NA | 类名：FormComponentModifier；  API声明：applyNormalAttribute?(instance: FormComponentAttribute): void;  差异内容：applyNormalAttribute?(instance: FormComponentAttribute): void; | api/arkui/FormComponentModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface LayoutConstraint  差异内容： declare interface LayoutConstraint | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：LayoutConstraint；  API声明：maxSize: Size;  差异内容：maxSize: Size; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：LayoutConstraint；  API声明：minSize: Size;  差异内容：minSize: Size; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：LayoutConstraint；  API声明：percentReference: Size;  差异内容：percentReference: Size; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：global；  API声明： export class FrameNode  差异内容： export class FrameNode | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：FrameNode；  API声明：getRenderNode(): RenderNode | null;  差异内容：getRenderNode(): RenderNode | null; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：FrameNode；  API声明：isModifiable(): boolean;  差异内容：isModifiable(): boolean; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：FrameNode；  API声明：appendChild(node: FrameNode): void;  差异内容：appendChild(node: FrameNode): void; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：FrameNode；  API声明：insertChildAfter(child: FrameNode, sibling: FrameNode | null): void;  差异内容：insertChildAfter(child: FrameNode, sibling: FrameNode | null): void; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：FrameNode；  API声明：removeChild(node: FrameNode): void;  差异内容：removeChild(node: FrameNode): void; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：FrameNode；  API声明：clearChildren(): void;  差异内容：clearChildren(): void; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：FrameNode；  API声明：getChild(index: number): FrameNode | null;  差异内容：getChild(index: number): FrameNode | null; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：FrameNode；  API声明：getFirstChild(): FrameNode | null;  差异内容：getFirstChild(): FrameNode | null; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：FrameNode；  API声明：getNextSibling(): FrameNode | null;  差异内容：getNextSibling(): FrameNode | null; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：FrameNode；  API声明：getPreviousSibling(): FrameNode | null;  差异内容：getPreviousSibling(): FrameNode | null; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：FrameNode；  API声明：getParent(): FrameNode | null;  差异内容：getParent(): FrameNode | null; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：FrameNode；  API声明：getChildrenCount(): number;  差异内容：getChildrenCount(): number; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：FrameNode；  API声明：dispose(): void;  差异内容：dispose(): void; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：FrameNode；  API声明：getPositionToWindow(): Position;  差异内容：getPositionToWindow(): Position; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：FrameNode；  API声明：getPositionToParent(): Position;  差异内容：getPositionToParent(): Position; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：FrameNode；  API声明：getMeasuredSize(): Size;  差异内容：getMeasuredSize(): Size; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：FrameNode；  API声明：getLayoutPosition(): Position;  差异内容：getLayoutPosition(): Position; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：FrameNode；  API声明：getUserConfigBorderWidth(): Edges<LengthMetrics>;  差异内容：getUserConfigBorderWidth(): Edges<LengthMetrics>; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：FrameNode；  API声明：getUserConfigPadding(): Edges<LengthMetrics>;  差异内容：getUserConfigPadding(): Edges<LengthMetrics>; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：FrameNode；  API声明：getUserConfigMargin(): Edges<LengthMetrics>;  差异内容：getUserConfigMargin(): Edges<LengthMetrics>; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：FrameNode；  API声明：getUserConfigSize(): SizeT<LengthMetrics>;  差异内容：getUserConfigSize(): SizeT<LengthMetrics>; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：FrameNode；  API声明：getId(): string;  差异内容：getId(): string; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：FrameNode；  API声明：getUniqueId(): number;  差异内容：getUniqueId(): number; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：FrameNode；  API声明：getNodeType(): string;  差异内容：getNodeType(): string; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：FrameNode；  API声明：getOpacity(): number;  差异内容：getOpacity(): number; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：FrameNode；  API声明：isVisible(): boolean;  差异内容：isVisible(): boolean; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：FrameNode；  API声明：isClipToFrame(): boolean;  差异内容：isClipToFrame(): boolean; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：FrameNode；  API声明：isAttached(): boolean;  差异内容：isAttached(): boolean; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：FrameNode；  API声明：getInspectorInfo(): Object;  差异内容：getInspectorInfo(): Object; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：FrameNode；  API声明：getCustomProperty(name: string): Object | undefined;  差异内容：getCustomProperty(name: string): Object | undefined; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：FrameNode；  API声明：onDraw?(context: DrawContext): void;  差异内容：onDraw?(context: DrawContext): void; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：FrameNode；  API声明：onMeasure(constraint: LayoutConstraint): void;  差异内容：onMeasure(constraint: LayoutConstraint): void; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：FrameNode；  API声明：onLayout(position: Position): void;  差异内容：onLayout(position: Position): void; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：FrameNode；  API声明：setMeasuredSize(size: Size): void;  差异内容：setMeasuredSize(size: Size): void; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：FrameNode；  API声明：setLayoutPosition(position: Position): void;  差异内容：setLayoutPosition(position: Position): void; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：FrameNode；  API声明：measure(constraint: LayoutConstraint): void;  差异内容：measure(constraint: LayoutConstraint): void; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：FrameNode；  API声明：layout(position: Position): void;  差异内容：layout(position: Position): void; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：FrameNode；  API声明：setNeedsLayout(): void;  差异内容：setNeedsLayout(): void; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：FrameNode；  API声明：invalidate(): void;  差异内容：invalidate(): void; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：FrameNode；  API声明：getPositionToScreen(): Position;  差异内容：getPositionToScreen(): Position; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：FrameNode；  API声明：getPositionToWindowWithTransform(): Position;  差异内容：getPositionToWindowWithTransform(): Position; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：FrameNode；  API声明：getPositionToParentWithTransform(): Position;  差异内容：getPositionToParentWithTransform(): Position; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：FrameNode；  API声明：getPositionToScreenWithTransform(): Position;  差异内容：getPositionToScreenWithTransform(): Position; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：FrameNode；  API声明：disposeTree(): void;  差异内容：disposeTree(): void; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：FrameNode；  API声明：addComponentContent<T>(content: ComponentContent<T>): void;  差异内容：addComponentContent<T>(content: ComponentContent<T>): void; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：global；  API声明： export interface TypedFrameNode  差异内容： export interface TypedFrameNode | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：TypedFrameNode；  API声明：initialize: C;  差异内容：initialize: C; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：TypedFrameNode；  API声明：readonly attribute: T;  差异内容：readonly attribute: T; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：global；  API声明： export namespace typeNode  差异内容： export namespace typeNode | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：type Text = TypedFrameNode<TextInterface, TextAttribute>;  差异内容：type Text = TypedFrameNode<TextInterface, TextAttribute>; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：function createNode(context: UIContext, nodeType: 'Text'): Text;  差异内容：function createNode(context: UIContext, nodeType: 'Text'): Text; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：function createNode(context: UIContext, nodeType: 'Column'): Column;  差异内容：function createNode(context: UIContext, nodeType: 'Column'): Column; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：function createNode(context: UIContext, nodeType: 'Row'): Row;  差异内容：function createNode(context: UIContext, nodeType: 'Row'): Row; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：function createNode(context: UIContext, nodeType: 'Stack'): Stack;  差异内容：function createNode(context: UIContext, nodeType: 'Stack'): Stack; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：function createNode(context: UIContext, nodeType: 'GridRow'): GridRow;  差异内容：function createNode(context: UIContext, nodeType: 'GridRow'): GridRow; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：function createNode(context: UIContext, nodeType: 'GridCol'): GridCol;  差异内容：function createNode(context: UIContext, nodeType: 'GridCol'): GridCol; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：function createNode(context: UIContext, nodeType: 'Flex'): Flex;  差异内容：function createNode(context: UIContext, nodeType: 'Flex'): Flex; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：function createNode(context: UIContext, nodeType: 'Swiper'): Swiper;  差异内容：function createNode(context: UIContext, nodeType: 'Swiper'): Swiper; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：function createNode(context: UIContext, nodeType: 'Progress'): Progress;  差异内容：function createNode(context: UIContext, nodeType: 'Progress'): Progress; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：function createNode(context: UIContext, nodeType: 'Scroll'): Scroll;  差异内容：function createNode(context: UIContext, nodeType: 'Scroll'): Scroll; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：function createNode(context: UIContext, nodeType: 'RelativeContainer'): RelativeContainer;  差异内容：function createNode(context: UIContext, nodeType: 'RelativeContainer'): RelativeContainer; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：function createNode(context: UIContext, nodeType: 'Divider'): Divider;  差异内容：function createNode(context: UIContext, nodeType: 'Divider'): Divider; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：function createNode(context: UIContext, nodeType: 'LoadingProgress'): LoadingProgress;  差异内容：function createNode(context: UIContext, nodeType: 'LoadingProgress'): LoadingProgress; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：function createNode(context: UIContext, nodeType: 'Search'): Search;  差异内容：function createNode(context: UIContext, nodeType: 'Search'): Search; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：function createNode(context: UIContext, nodeType: 'Blank'): Blank;  差异内容：function createNode(context: UIContext, nodeType: 'Blank'): Blank; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：function createNode(context: UIContext, nodeType: 'Image'): Image;  差异内容：function createNode(context: UIContext, nodeType: 'Image'): Image; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：function createNode(context: UIContext, nodeType: 'List'): List;  差异内容：function createNode(context: UIContext, nodeType: 'List'): List; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：function createNode(context: UIContext, nodeType: 'ListItem'): ListItem;  差异内容：function createNode(context: UIContext, nodeType: 'ListItem'): ListItem; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：type Column = TypedFrameNode<ColumnInterface, ColumnAttribute>;  差异内容：type Column = TypedFrameNode<ColumnInterface, ColumnAttribute>; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：type Row = TypedFrameNode<RowInterface, RowAttribute>;  差异内容：type Row = TypedFrameNode<RowInterface, RowAttribute>; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：type Stack = TypedFrameNode<StackInterface, StackAttribute>;  差异内容：type Stack = TypedFrameNode<StackInterface, StackAttribute>; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：type GridRow = TypedFrameNode<GridRowInterface, GridRowAttribute>;  差异内容：type GridRow = TypedFrameNode<GridRowInterface, GridRowAttribute>; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：type GridCol = TypedFrameNode<GridColInterface, GridColAttribute>;  差异内容：type GridCol = TypedFrameNode<GridColInterface, GridColAttribute>; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：type Flex = TypedFrameNode<FlexInterface, FlexAttribute>;  差异内容：type Flex = TypedFrameNode<FlexInterface, FlexAttribute>; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：type Swiper = TypedFrameNode<SwiperInterface, SwiperAttribute>;  差异内容：type Swiper = TypedFrameNode<SwiperInterface, SwiperAttribute>; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：type Progress = TypedFrameNode<ProgressInterface, ProgressAttribute>;  差异内容：type Progress = TypedFrameNode<ProgressInterface, ProgressAttribute>; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：type Scroll = TypedFrameNode<ScrollInterface, ScrollAttribute>;  差异内容：type Scroll = TypedFrameNode<ScrollInterface, ScrollAttribute>; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：type RelativeContainer = TypedFrameNode<RelativeContainerInterface, RelativeContainerAttribute>;  差异内容：type RelativeContainer = TypedFrameNode<RelativeContainerInterface, RelativeContainerAttribute>; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：type Divider = TypedFrameNode<DividerInterface, DividerAttribute>;  差异内容：type Divider = TypedFrameNode<DividerInterface, DividerAttribute>; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：type LoadingProgress = TypedFrameNode<LoadingProgressInterface, LoadingProgressAttribute>;  差异内容：type LoadingProgress = TypedFrameNode<LoadingProgressInterface, LoadingProgressAttribute>; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：type Search = TypedFrameNode<SearchInterface, SearchAttribute>;  差异内容：type Search = TypedFrameNode<SearchInterface, SearchAttribute>; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：type Blank = TypedFrameNode<BlankInterface, BlankAttribute>;  差异内容：type Blank = TypedFrameNode<BlankInterface, BlankAttribute>; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：type Image = TypedFrameNode<ImageInterface, ImageAttribute>;  差异内容：type Image = TypedFrameNode<ImageInterface, ImageAttribute>; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：type List = TypedFrameNode<ListInterface, ListAttribute>;  差异内容：type List = TypedFrameNode<ListInterface, ListAttribute>; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：typeNode；  API声明：type ListItem = TypedFrameNode<ListItemInterface, ListItemAttribute>;  差异内容：type ListItem = TypedFrameNode<ListItemInterface, ListItemAttribute>; | api/arkui/FrameNode.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class GaugeModifier  差异内容： export declare class GaugeModifier | api/arkui/GaugeModifier.d.ts |
| 新增API | NA | 类名：GaugeModifier；  API声明：applyNormalAttribute?(instance: GaugeAttribute): void;  差异内容：applyNormalAttribute?(instance: GaugeAttribute): void; | api/arkui/GaugeModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export interface Size  差异内容： export interface Size | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：Size；  API声明：width: number;  差异内容：width: number; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：Size；  API声明：height: number;  差异内容：height: number; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：global；  API声明： export class DrawContext  差异内容： export class DrawContext | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：global；  API声明： interface Vector2  差异内容： interface Vector2 | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：Vector2；  API声明：x: number;  差异内容：x: number; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：Vector2；  API声明：y: number;  差异内容：y: number; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：global；  API声明： interface Vector2T  差异内容： interface Vector2T | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：Vector2T；  API声明：x: T;  差异内容：x: T; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：Vector2T；  API声明：y: T;  差异内容：y: T; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：global；  API声明： interface Vector3  差异内容： interface Vector3 | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：Vector3；  API声明：x: number;  差异内容：x: number; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：Vector3；  API声明：y: number;  差异内容：y: number; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：Vector3；  API声明：z: number;  差异内容：z: number; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：global；  API声明：export type Matrix4 = [  number,  number,  number,  number,  number,  number,  number,  number,  number,  number,  number,  number,  number,  number,  number,  number  ];  差异内容：export type Matrix4 = [  number,  number,  number,  number,  number,  number,  number,  number,  number,  number,  number,  number,  number,  number,  number,  number  ]; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：global；  API声明：export type Offset = Vector2;  差异内容：export type Offset = Vector2; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：global；  API声明：export type Position = Vector2;  差异内容：export type Position = Vector2; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：global；  API声明：export type PositionT<T> = Vector2T<T>;  差异内容：export type PositionT<T> = Vector2T<T>; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：global；  API声明：export type Pivot = Vector2;  差异内容：export type Pivot = Vector2; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：global；  API声明：export type Scale = Vector2;  差异内容：export type Scale = Vector2; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：global；  API声明：export type Translation = Vector2;  差异内容：export type Translation = Vector2; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：global；  API声明：export type Rotation = Vector3;  差异内容：export type Rotation = Vector3; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare interface Frame  差异内容： export declare interface Frame | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：Frame；  API声明：x: number;  差异内容：x: number; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：Frame；  API声明：y: number;  差异内容：y: number; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：Frame；  API声明：width: number;  差异内容：width: number; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：Frame；  API声明：height: number;  差异内容：height: number; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：global；  API声明： export interface Edges  差异内容： export interface Edges | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：Edges；  API声明：left: T;  差异内容：left: T; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：Edges；  API声明：right: T;  差异内容：right: T; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：Edges；  API声明：top: T;  差异内容：top: T; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：Edges；  API声明：bottom: T;  差异内容：bottom: T; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum LengthUnit  差异内容： declare enum LengthUnit | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：LengthUnit；  API声明：PX = 0  差异内容：PX = 0 | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：LengthUnit；  API声明：VP = 1  差异内容：VP = 1 | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：LengthUnit；  API声明：FP = 2  差异内容：FP = 2 | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：LengthUnit；  API声明：PERCENT = 3  差异内容：PERCENT = 3 | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：LengthUnit；  API声明：LPX = 4  差异内容：LPX = 4 | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：global；  API声明： export interface SizeT  差异内容： export interface SizeT | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：SizeT；  API声明：width: T;  差异内容：width: T; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：SizeT；  API声明：height: T;  差异内容：height: T; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：global；  API声明： export enum LengthMetricsUnit  差异内容： export enum LengthMetricsUnit | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：LengthMetricsUnit；  API声明：DEFAULT = 0  差异内容：DEFAULT = 0 | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：LengthMetricsUnit；  API声明：PX = 1  差异内容：PX = 1 | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class LengthMetrics  差异内容： declare class LengthMetrics | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：LengthMetrics；  API声明：static px(value: number): LengthMetrics;  差异内容：static px(value: number): LengthMetrics; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：LengthMetrics；  API声明：static vp(value: number): LengthMetrics;  差异内容：static vp(value: number): LengthMetrics; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：LengthMetrics；  API声明：static fp(value: number): LengthMetrics;  差异内容：static fp(value: number): LengthMetrics; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：LengthMetrics；  API声明：static percent(value: number): LengthMetrics;  差异内容：static percent(value: number): LengthMetrics; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：LengthMetrics；  API声明：static lpx(value: number): LengthMetrics;  差异内容：static lpx(value: number): LengthMetrics; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：LengthMetrics；  API声明：public unit: LengthUnit;  差异内容：public unit: LengthUnit; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：LengthMetrics；  API声明：public value: number;  差异内容：public value: number; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class ColorMetrics  差异内容： declare class ColorMetrics | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：ColorMetrics；  API声明：static numeric(value: number): ColorMetrics;  差异内容：static numeric(value: number): ColorMetrics; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：ColorMetrics；  API声明：static rgba(red: number, green: number, blue: number, alpha?: number): ColorMetrics;  差异内容：static rgba(red: number, green: number, blue: number, alpha?: number): ColorMetrics; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：ColorMetrics；  API声明：static resourceColor(color: ResourceColor): ColorMetrics;  差异内容：static resourceColor(color: ResourceColor): ColorMetrics; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：ColorMetrics；  API声明：blendColor(overlayColor: ColorMetrics): ColorMetrics;  差异内容：blendColor(overlayColor: ColorMetrics): ColorMetrics; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：global；  API声明： interface Corners  差异内容： interface Corners | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：Corners；  API声明：topLeft: T;  差异内容：topLeft: T; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：Corners；  API声明：topRight: T;  差异内容：topRight: T; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：Corners；  API声明：bottomLeft: T;  差异内容：bottomLeft: T; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：Corners；  API声明：bottomRight: T;  差异内容：bottomRight: T; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：global；  API声明：export type CornerRadius = Corners<Vector2>;  差异内容：export type CornerRadius = Corners<Vector2>; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：global；  API声明：export type BorderRadiuses = Corners<number>;  差异内容：export type BorderRadiuses = Corners<number>; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：global；  API声明：export type Rect = common2D.Rect;  差异内容：export type Rect = common2D.Rect; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：global；  API声明： export interface RoundRect  差异内容： export interface RoundRect | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：RoundRect；  API声明：rect: Rect;  差异内容：rect: Rect; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：RoundRect；  API声明：corners: CornerRadius;  差异内容：corners: CornerRadius; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：global；  API声明： export interface Circle  差异内容： export interface Circle | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：Circle；  API声明：centerX: number;  差异内容：centerX: number; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：Circle；  API声明：centerY: number;  差异内容：centerY: number; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：Circle；  API声明：radius: number;  差异内容：radius: number; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：global；  API声明： export interface CommandPath  差异内容： export interface CommandPath | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：CommandPath；  API声明：commands: string;  差异内容：commands: string; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class ShapeMask  差异内容： export declare class ShapeMask | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：ShapeMask；  API声明：setRectShape(rect: Rect): void;  差异内容：setRectShape(rect: Rect): void; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：ShapeMask；  API声明：setRoundRectShape(roundRect: RoundRect): void;  差异内容：setRoundRectShape(roundRect: RoundRect): void; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：ShapeMask；  API声明：setCircleShape(circle: Circle): void;  差异内容：setCircleShape(circle: Circle): void; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：ShapeMask；  API声明：setOvalShape(oval: Rect): void;  差异内容：setOvalShape(oval: Rect): void; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：ShapeMask；  API声明：setCommandPath(path: CommandPath): void;  差异内容：setCommandPath(path: CommandPath): void; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：ShapeMask；  API声明：fillColor: number;  差异内容：fillColor: number; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：ShapeMask；  API声明：strokeColor: number;  差异内容：strokeColor: number; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：ShapeMask；  API声明：strokeWidth: number;  差异内容：strokeWidth: number; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：global；  API声明：export function edgeColors(all: number): Edges<number>;  差异内容：export function edgeColors(all: number): Edges<number>; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：global；  API声明：export function edgeWidths(all: number): Edges<number>;  差异内容：export function edgeWidths(all: number): Edges<number>; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：global；  API声明：export function borderStyles(all: BorderStyle): Edges<BorderStyle>;  差异内容：export function borderStyles(all: BorderStyle): Edges<BorderStyle>; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：global；  API声明：export function borderRadiuses(all: number): BorderRadiuses;  差异内容：export function borderRadiuses(all: number): BorderRadiuses; | api/arkui/Graphics.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class GridColModifier  差异内容： export declare class GridColModifier | api/arkui/GridColModifier.d.ts |
| 新增API | NA | 类名：GridColModifier；  API声明：applyNormalAttribute?(instance: GridColAttribute): void;  差异内容：applyNormalAttribute?(instance: GridColAttribute): void; | api/arkui/GridColModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class GridItemModifier  差异内容： export declare class GridItemModifier | api/arkui/GridItemModifier.d.ts |
| 新增API | NA | 类名：GridItemModifier；  API声明：applyNormalAttribute?(instance: GridItemAttribute): void;  差异内容：applyNormalAttribute?(instance: GridItemAttribute): void; | api/arkui/GridItemModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class GridModifier  差异内容： export declare class GridModifier | api/arkui/GridModifier.d.ts |
| 新增API | NA | 类名：GridModifier；  API声明：applyNormalAttribute?(instance: GridAttribute): void;  差异内容：applyNormalAttribute?(instance: GridAttribute): void; | api/arkui/GridModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class GridRowModifier  差异内容： export declare class GridRowModifier | api/arkui/GridRowModifier.d.ts |
| 新增API | NA | 类名：GridRowModifier；  API声明：applyNormalAttribute?(instance: GridRowAttribute): void;  差异内容：applyNormalAttribute?(instance: GridRowAttribute): void; | api/arkui/GridRowModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class HyperlinkModifier  差异内容： export declare class HyperlinkModifier | api/arkui/HyperlinkModifier.d.ts |
| 新增API | NA | 类名：HyperlinkModifier；  API声明：applyNormalAttribute?(instance: HyperlinkAttribute): void;  差异内容：applyNormalAttribute?(instance: HyperlinkAttribute): void; | api/arkui/HyperlinkModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class ImageAnimatorModifier  差异内容： export declare class ImageAnimatorModifier | api/arkui/ImageAnimatorModifier.d.ts |
| 新增API | NA | 类名：ImageAnimatorModifier；  API声明：applyNormalAttribute?(instance: ImageAnimatorAttribute): void;  差异内容：applyNormalAttribute?(instance: ImageAnimatorAttribute): void; | api/arkui/ImageAnimatorModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class ImageModifier  差异内容： export declare class ImageModifier | api/arkui/ImageModifier.d.ts |
| 新增API | NA | 类名：ImageModifier；  API声明：applyNormalAttribute?(instance: ImageAttribute): void;  差异内容：applyNormalAttribute?(instance: ImageAttribute): void; | api/arkui/ImageModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class ImageSpanModifier  差异内容： export declare class ImageSpanModifier | api/arkui/ImageSpanModifier.d.ts |
| 新增API | NA | 类名：ImageSpanModifier；  API声明：applyNormalAttribute?(instance: ImageSpanAttribute): void;  差异内容：applyNormalAttribute?(instance: ImageSpanAttribute): void; | api/arkui/ImageSpanModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class LineModifier  差异内容： export declare class LineModifier | api/arkui/LineModifier.d.ts |
| 新增API | NA | 类名：LineModifier；  API声明：applyNormalAttribute?(instance: LineAttribute): void;  差异内容：applyNormalAttribute?(instance: LineAttribute): void; | api/arkui/LineModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class ListItemGroupModifier  差异内容： export declare class ListItemGroupModifier | api/arkui/ListItemGroupModifier.d.ts |
| 新增API | NA | 类名：ListItemGroupModifier；  API声明：applyNormalAttribute?(instance: ListItemGroupAttribute): void;  差异内容：applyNormalAttribute?(instance: ListItemGroupAttribute): void; | api/arkui/ListItemGroupModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class ListItemModifier  差异内容： export declare class ListItemModifier | api/arkui/ListItemModifier.d.ts |
| 新增API | NA | 类名：ListItemModifier；  API声明：applyNormalAttribute?(instance: ListItemAttribute): void;  差异内容：applyNormalAttribute?(instance: ListItemAttribute): void; | api/arkui/ListItemModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class ListModifier  差异内容： export declare class ListModifier | api/arkui/ListModifier.d.ts |
| 新增API | NA | 类名：ListModifier；  API声明：applyNormalAttribute?(instance: ListAttribute): void;  差异内容：applyNormalAttribute?(instance: ListAttribute): void; | api/arkui/ListModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class LoadingProgressModifier  差异内容： export declare class LoadingProgressModifier | api/arkui/LoadingProgressModifier.d.ts |
| 新增API | NA | 类名：LoadingProgressModifier；  API声明：applyNormalAttribute?(instance: LoadingProgressAttribute): void;  差异内容：applyNormalAttribute?(instance: LoadingProgressAttribute): void; | api/arkui/LoadingProgressModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class MarqueeModifier  差异内容： export declare class MarqueeModifier | api/arkui/MarqueeModifier.d.ts |
| 新增API | NA | 类名：MarqueeModifier；  API声明：applyNormalAttribute?(instance: MarqueeAttribute): void;  差异内容：applyNormalAttribute?(instance: MarqueeAttribute): void; | api/arkui/MarqueeModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class MenuItemModifier  差异内容： export declare class MenuItemModifier | api/arkui/MenuItemModifier.d.ts |
| 新增API | NA | 类名：MenuItemModifier；  API声明：applyNormalAttribute?(instance: MenuItemAttribute): void;  差异内容：applyNormalAttribute?(instance: MenuItemAttribute): void; | api/arkui/MenuItemModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class MenuModifier  差异内容： export declare class MenuModifier | api/arkui/MenuModifier.d.ts |
| 新增API | NA | 类名：MenuModifier；  API声明：applyNormalAttribute?(instance: MenuAttribute): void;  差异内容：applyNormalAttribute?(instance: MenuAttribute): void; | api/arkui/MenuModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class NavDestinationModifier  差异内容： export declare class NavDestinationModifier | api/arkui/NavDestinationModifier.d.ts |
| 新增API | NA | 类名：NavDestinationModifier；  API声明：applyNormalAttribute?(instance: NavDestinationAttribute): void;  差异内容：applyNormalAttribute?(instance: NavDestinationAttribute): void; | api/arkui/NavDestinationModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class NavigationModifier  差异内容： export declare class NavigationModifier | api/arkui/NavigationModifier.d.ts |
| 新增API | NA | 类名：NavigationModifier；  API声明：applyNormalAttribute?(instance: NavigationAttribute): void;  差异内容：applyNormalAttribute?(instance: NavigationAttribute): void; | api/arkui/NavigationModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class NavigatorModifier  差异内容： export declare class NavigatorModifier | api/arkui/NavigatorModifier.d.ts |
| 新增API | NA | 类名：NavigatorModifier；  API声明：applyNormalAttribute?(instance: NavigatorAttribute): void;  差异内容：applyNormalAttribute?(instance: NavigatorAttribute): void; | api/arkui/NavigatorModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class NavRouterModifier  差异内容： export declare class NavRouterModifier | api/arkui/NavRouterModifier.d.ts |
| 新增API | NA | 类名：NavRouterModifier；  API声明：applyNormalAttribute?(instance: NavRouterAttribute): void;  差异内容：applyNormalAttribute?(instance: NavRouterAttribute): void; | api/arkui/NavRouterModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export class NodeContent  差异内容： export class NodeContent | api/arkui/NodeContent.d.ts |
| 新增API | NA | 类名：NodeContent；  API声明：addFrameNode(node: FrameNode): void;  差异内容：addFrameNode(node: FrameNode): void; | api/arkui/NodeContent.d.ts |
| 新增API | NA | 类名：NodeContent；  API声明：removeFrameNode(node: FrameNode): void;  差异内容：removeFrameNode(node: FrameNode): void; | api/arkui/NodeContent.d.ts |
| 新增API | NA | 类名：global；  API声明： export abstract class NodeController  差异内容： export abstract class NodeController | api/arkui/NodeController.d.ts |
| 新增API | NA | 类名：NodeController；  API声明：abstract makeNode(uiContext: UIContext): FrameNode | null;  差异内容：abstract makeNode(uiContext: UIContext): FrameNode | null; | api/arkui/NodeController.d.ts |
| 新增API | NA | 类名：NodeController；  API声明：aboutToResize?(size: Size): void;  差异内容：aboutToResize?(size: Size): void; | api/arkui/NodeController.d.ts |
| 新增API | NA | 类名：NodeController；  API声明：aboutToAppear?(): void;  差异内容：aboutToAppear?(): void; | api/arkui/NodeController.d.ts |
| 新增API | NA | 类名：NodeController；  API声明：aboutToDisappear?(): void;  差异内容：aboutToDisappear?(): void; | api/arkui/NodeController.d.ts |
| 新增API | NA | 类名：NodeController；  API声明：rebuild(): void;  差异内容：rebuild(): void; | api/arkui/NodeController.d.ts |
| 新增API | NA | 类名：NodeController；  API声明：onTouchEvent?(event: TouchEvent): void;  差异内容：onTouchEvent?(event: TouchEvent): void; | api/arkui/NodeController.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class PanelModifier  差异内容： export declare class PanelModifier | api/arkui/PanelModifier.d.ts |
| 新增API | NA | 类名：PanelModifier；  API声明：applyNormalAttribute?(instance: PanelAttribute): void;  差异内容：applyNormalAttribute?(instance: PanelAttribute): void; | api/arkui/PanelModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class PathModifier  差异内容： export declare class PathModifier | api/arkui/PathModifier.d.ts |
| 新增API | NA | 类名：PathModifier；  API声明：applyNormalAttribute?(instance: PathAttribute): void;  差异内容：applyNormalAttribute?(instance: PathAttribute): void; | api/arkui/PathModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class PatternLockModifier  差异内容： export declare class PatternLockModifier | api/arkui/PatternLockModifier.d.ts |
| 新增API | NA | 类名：PatternLockModifier；  API声明：applyNormalAttribute?(instance: PatternLockAttribute): void;  差异内容：applyNormalAttribute?(instance: PatternLockAttribute): void; | api/arkui/PatternLockModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class PolygonModifier  差异内容： export declare class PolygonModifier | api/arkui/PolygonModifier.d.ts |
| 新增API | NA | 类名：PolygonModifier；  API声明：applyNormalAttribute?(instance: PolygonAttribute): void;  差异内容：applyNormalAttribute?(instance: PolygonAttribute): void; | api/arkui/PolygonModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class PolylineModifier  差异内容： export declare class PolylineModifier | api/arkui/PolylineModifier.d.ts |
| 新增API | NA | 类名：PolylineModifier；  API声明：applyNormalAttribute?(instance: PolylineAttribute): void;  差异内容：applyNormalAttribute?(instance: PolylineAttribute): void; | api/arkui/PolylineModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class ProgressModifier  差异内容： export declare class ProgressModifier | api/arkui/ProgressModifier.d.ts |
| 新增API | NA | 类名：ProgressModifier；  API声明：applyNormalAttribute?(instance: ProgressAttribute): void;  差异内容：applyNormalAttribute?(instance: ProgressAttribute): void; | api/arkui/ProgressModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class QRCodeModifier  差异内容： export declare class QRCodeModifier | api/arkui/QRCodeModifier.d.ts |
| 新增API | NA | 类名：QRCodeModifier；  API声明：applyNormalAttribute?(instance: QRCodeAttribute): void;  差异内容：applyNormalAttribute?(instance: QRCodeAttribute): void; | api/arkui/QRCodeModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class RadioModifier  差异内容： export declare class RadioModifier | api/arkui/RadioModifier.d.ts |
| 新增API | NA | 类名：RadioModifier；  API声明：applyNormalAttribute?(instance: RadioAttribute): void;  差异内容：applyNormalAttribute?(instance: RadioAttribute): void; | api/arkui/RadioModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class RatingModifier  差异内容： export declare class RatingModifier | api/arkui/RatingModifier.d.ts |
| 新增API | NA | 类名：RatingModifier；  API声明：applyNormalAttribute?(instance: RatingAttribute): void;  差异内容：applyNormalAttribute?(instance: RatingAttribute): void; | api/arkui/RatingModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class RectModifier  差异内容： export declare class RectModifier | api/arkui/RectModifier.d.ts |
| 新增API | NA | 类名：RectModifier；  API声明：applyNormalAttribute?(instance: RectAttribute): void;  差异内容：applyNormalAttribute?(instance: RectAttribute): void; | api/arkui/RectModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class RefreshModifier  差异内容： export declare class RefreshModifier | api/arkui/RefreshModifier.d.ts |
| 新增API | NA | 类名：RefreshModifier；  API声明：applyNormalAttribute?(instance: RefreshAttribute): void;  差异内容：applyNormalAttribute?(instance: RefreshAttribute): void; | api/arkui/RefreshModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export class RenderNode  差异内容： export class RenderNode | api/arkui/RenderNode.d.ts |
| 新增API | NA | 类名：RenderNode；  API声明：appendChild(node: RenderNode): void;  差异内容：appendChild(node: RenderNode): void; | api/arkui/RenderNode.d.ts |
| 新增API | NA | 类名：RenderNode；  API声明：insertChildAfter(child: RenderNode, sibling: RenderNode | null): void;  差异内容：insertChildAfter(child: RenderNode, sibling: RenderNode | null): void; | api/arkui/RenderNode.d.ts |
| 新增API | NA | 类名：RenderNode；  API声明：removeChild(node: RenderNode): void;  差异内容：removeChild(node: RenderNode): void; | api/arkui/RenderNode.d.ts |
| 新增API | NA | 类名：RenderNode；  API声明：clearChildren(): void;  差异内容：clearChildren(): void; | api/arkui/RenderNode.d.ts |
| 新增API | NA | 类名：RenderNode；  API声明：getChild(index: number): RenderNode | null;  差异内容：getChild(index: number): RenderNode | null; | api/arkui/RenderNode.d.ts |
| 新增API | NA | 类名：RenderNode；  API声明：getFirstChild(): RenderNode | null;  差异内容：getFirstChild(): RenderNode | null; | api/arkui/RenderNode.d.ts |
| 新增API | NA | 类名：RenderNode；  API声明：getNextSibling(): RenderNode | null;  差异内容：getNextSibling(): RenderNode | null; | api/arkui/RenderNode.d.ts |
| 新增API | NA | 类名：RenderNode；  API声明：getPreviousSibling(): RenderNode | null;  差异内容：getPreviousSibling(): RenderNode | null; | api/arkui/RenderNode.d.ts |
| 新增API | NA | 类名：RenderNode；  API声明：draw(context: DrawContext): void;  差异内容：draw(context: DrawContext): void; | api/arkui/RenderNode.d.ts |
| 新增API | NA | 类名：RenderNode；  API声明：invalidate(): void;  差异内容：invalidate(): void; | api/arkui/RenderNode.d.ts |
| 新增API | NA | 类名：RenderNode；  API声明：dispose(): void;  差异内容：dispose(): void; | api/arkui/RenderNode.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class RichEditorModifier  差异内容： export declare class RichEditorModifier | api/arkui/RichEditorModifier.d.ts |
| 新增API | NA | 类名：RichEditorModifier；  API声明：applyNormalAttribute?(instance: RichEditorAttribute): void;  差异内容：applyNormalAttribute?(instance: RichEditorAttribute): void; | api/arkui/RichEditorModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class RowModifier  差异内容： export declare class RowModifier | api/arkui/RowModifier.d.ts |
| 新增API | NA | 类名：RowModifier；  API声明：applyNormalAttribute?(instance: RowAttribute): void;  差异内容：applyNormalAttribute?(instance: RowAttribute): void; | api/arkui/RowModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class RowSplitModifier  差异内容： export declare class RowSplitModifier | api/arkui/RowSplitModifier.d.ts |
| 新增API | NA | 类名：RowSplitModifier；  API声明：applyNormalAttribute?(instance: RowSplitAttribute): void;  差异内容：applyNormalAttribute?(instance: RowSplitAttribute): void; | api/arkui/RowSplitModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class ScrollModifier  差异内容： export declare class ScrollModifier | api/arkui/ScrollModifier.d.ts |
| 新增API | NA | 类名：ScrollModifier；  API声明：applyNormalAttribute?(instance: ScrollAttribute): void;  差异内容：applyNormalAttribute?(instance: ScrollAttribute): void; | api/arkui/ScrollModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class SearchModifier  差异内容： export declare class SearchModifier | api/arkui/SearchModifier.d.ts |
| 新增API | NA | 类名：SearchModifier；  API声明：applyNormalAttribute?(instance: SearchAttribute): void;  差异内容：applyNormalAttribute?(instance: SearchAttribute): void; | api/arkui/SearchModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class SelectModifier  差异内容： export declare class SelectModifier | api/arkui/SelectModifier.d.ts |
| 新增API | NA | 类名：SelectModifier；  API声明：applyNormalAttribute?(instance: SelectAttribute): void;  差异内容：applyNormalAttribute?(instance: SelectAttribute): void; | api/arkui/SelectModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class ShapeModifier  差异内容： export declare class ShapeModifier | api/arkui/ShapeModifier.d.ts |
| 新增API | NA | 类名：ShapeModifier；  API声明：applyNormalAttribute?(instance: ShapeAttribute): void;  差异内容：applyNormalAttribute?(instance: ShapeAttribute): void; | api/arkui/ShapeModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class SideBarContainerModifier  差异内容： export declare class SideBarContainerModifier | api/arkui/SideBarContainerModifier.d.ts |
| 新增API | NA | 类名：SideBarContainerModifier；  API声明：applyNormalAttribute?(instance: SideBarContainerAttribute): void;  差异内容：applyNormalAttribute?(instance: SideBarContainerAttribute): void; | api/arkui/SideBarContainerModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class SliderModifier  差异内容： export declare class SliderModifier | api/arkui/SliderModifier.d.ts |
| 新增API | NA | 类名：SliderModifier；  API声明：applyNormalAttribute?(instance: SliderAttribute): void;  差异内容：applyNormalAttribute?(instance: SliderAttribute): void; | api/arkui/SliderModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class SpanModifier  差异内容： export declare class SpanModifier | api/arkui/SpanModifier.d.ts |
| 新增API | NA | 类名：SpanModifier；  API声明：applyNormalAttribute?(instance: SpanAttribute): void;  差异内容：applyNormalAttribute?(instance: SpanAttribute): void; | api/arkui/SpanModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class StackModifier  差异内容： export declare class StackModifier | api/arkui/StackModifier.d.ts |
| 新增API | NA | 类名：StackModifier；  API声明：applyNormalAttribute?(instance: StackAttribute): void;  差异内容：applyNormalAttribute?(instance: StackAttribute): void; | api/arkui/StackModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class StepperItemModifier  差异内容： export declare class StepperItemModifier | api/arkui/StepperItemModifier.d.ts |
| 新增API | NA | 类名：StepperItemModifier；  API声明：applyNormalAttribute?(instance: StepperItemAttribute): void;  差异内容：applyNormalAttribute?(instance: StepperItemAttribute): void; | api/arkui/StepperItemModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class SwiperModifier  差异内容： export declare class SwiperModifier | api/arkui/SwiperModifier.d.ts |
| 新增API | NA | 类名：SwiperModifier；  API声明：applyNormalAttribute?(instance: SwiperAttribute): void;  差异内容：applyNormalAttribute?(instance: SwiperAttribute): void; | api/arkui/SwiperModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class SymbolGlyphModifier  差异内容： export declare class SymbolGlyphModifier | api/arkui/SymbolGlyphModifier.d.ts |
| 新增API | NA | 类名：SymbolGlyphModifier；  API声明：applyNormalAttribute?(instance: SymbolGlyphAttribute): void;  差异内容：applyNormalAttribute?(instance: SymbolGlyphAttribute): void; | api/arkui/SymbolGlyphModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class TabsModifier  差异内容： export declare class TabsModifier | api/arkui/TabsModifier.d.ts |
| 新增API | NA | 类名：TabsModifier；  API声明：applyNormalAttribute?(instance: TabsAttribute): void;  差异内容：applyNormalAttribute?(instance: TabsAttribute): void; | api/arkui/TabsModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class TextAreaModifier  差异内容： export declare class TextAreaModifier | api/arkui/TextAreaModifier.d.ts |
| 新增API | NA | 类名：TextAreaModifier；  API声明：applyNormalAttribute?(instance: TextAreaAttribute): void;  差异内容：applyNormalAttribute?(instance: TextAreaAttribute): void; | api/arkui/TextAreaModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class TextClockModifier  差异内容： export declare class TextClockModifier | api/arkui/TextClockModifier.d.ts |
| 新增API | NA | 类名：TextClockModifier；  API声明：applyNormalAttribute?(instance: TextClockAttribute): void;  差异内容：applyNormalAttribute?(instance: TextClockAttribute): void; | api/arkui/TextClockModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class TextInputModifier  差异内容： export declare class TextInputModifier | api/arkui/TextInputModifier.d.ts |
| 新增API | NA | 类名：TextInputModifier；  API声明：applyNormalAttribute?(instance: TextInputAttribute): void;  差异内容：applyNormalAttribute?(instance: TextInputAttribute): void; | api/arkui/TextInputModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class TextModifier  差异内容： export declare class TextModifier | api/arkui/TextModifier.d.ts |
| 新增API | NA | 类名：TextModifier；  API声明：applyNormalAttribute?(instance: TextAttribute): void;  差异内容：applyNormalAttribute?(instance: TextAttribute): void; | api/arkui/TextModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class TextPickerModifier  差异内容： export declare class TextPickerModifier | api/arkui/TextPickerModifier.d.ts |
| 新增API | NA | 类名：TextPickerModifier；  API声明：applyNormalAttribute?(instance: TextPickerAttribute): void;  差异内容：applyNormalAttribute?(instance: TextPickerAttribute): void; | api/arkui/TextPickerModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class TextTimerModifier  差异内容： export declare class TextTimerModifier | api/arkui/TextTimerModifier.d.ts |
| 新增API | NA | 类名：TextTimerModifier；  API声明：applyNormalAttribute?(instance: TextTimerAttribute): void;  差异内容：applyNormalAttribute?(instance: TextTimerAttribute): void; | api/arkui/TextTimerModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class TimePickerModifier  差异内容： export declare class TimePickerModifier | api/arkui/TimePickerModifier.d.ts |
| 新增API | NA | 类名：TimePickerModifier；  API声明：applyNormalAttribute?(instance: TimePickerAttribute): void;  差异内容：applyNormalAttribute?(instance: TimePickerAttribute): void; | api/arkui/TimePickerModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class ToggleModifier  差异内容： export declare class ToggleModifier | api/arkui/ToggleModifier.d.ts |
| 新增API | NA | 类名：ToggleModifier；  API声明：applyNormalAttribute?(instance: ToggleAttribute): void;  差异内容：applyNormalAttribute?(instance: ToggleAttribute): void; | api/arkui/ToggleModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class VideoModifier  差异内容： export declare class VideoModifier | api/arkui/VideoModifier.d.ts |
| 新增API | NA | 类名：VideoModifier；  API声明：applyNormalAttribute?(instance: VideoAttribute): void;  差异内容：applyNormalAttribute?(instance: VideoAttribute): void; | api/arkui/VideoModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class WaterFlowModifier  差异内容： export declare class WaterFlowModifier | api/arkui/WaterFlowModifier.d.ts |
| 新增API | NA | 类名：WaterFlowModifier；  API声明：applyNormalAttribute?(instance: WaterFlowAttribute): void;  差异内容：applyNormalAttribute?(instance: WaterFlowAttribute): void; | api/arkui/WaterFlowModifier.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class XComponentNode  差异内容： export declare class XComponentNode | api/arkui/XComponentNode.d.ts |
| 新增API | NA | 类名：XComponentNode；  API声明：onCreate(event?: Object): void;  差异内容：onCreate(event?: Object): void; | api/arkui/XComponentNode.d.ts |
| 新增API | NA | 类名：XComponentNode；  API声明：onDestroy(): void;  差异内容：onDestroy(): void; | api/arkui/XComponentNode.d.ts |
| 新增API | NA | 类名：XComponentNode；  API声明：changeRenderType(type: NodeRenderType): boolean;  差异内容：changeRenderType(type: NodeRenderType): boolean; | api/arkui/XComponentNode.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum CalendarAlign  差异内容： declare enum CalendarAlign | component/calendar\_picker.d.ts |
| 新增API | NA | 类名：CalendarAlign；  API声明：START = 0  差异内容：START = 0 | component/calendar\_picker.d.ts |
| 新增API | NA | 类名：CalendarAlign；  API声明：CENTER = 1  差异内容：CENTER = 1 | component/calendar\_picker.d.ts |
| 新增API | NA | 类名：CalendarAlign；  API声明：END = 2  差异内容：END = 2 | component/calendar\_picker.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface CalendarOptions  差异内容： declare interface CalendarOptions | component/calendar\_picker.d.ts |
| 新增API | NA | 类名：CalendarOptions；  API声明：hintRadius?: number | Resource;  差异内容：hintRadius?: number | Resource; | component/calendar\_picker.d.ts |
| 新增API | NA | 类名：CalendarOptions；  API声明：selected?: Date;  差异内容：selected?: Date; | component/calendar\_picker.d.ts |
| 新增API | NA | 类名：global；  API声明： interface CalendarPickerInterface  差异内容： interface CalendarPickerInterface | component/calendar\_picker.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class CalendarPickerAttribute  差异内容： declare class CalendarPickerAttribute | component/calendar\_picker.d.ts |
| 新增API | NA | 类名：CalendarPickerAttribute；  API声明：edgeAlign(alignType: CalendarAlign, offset?: Offset): CalendarPickerAttribute;  差异内容：edgeAlign(alignType: CalendarAlign, offset?: Offset): CalendarPickerAttribute; | component/calendar\_picker.d.ts |
| 新增API | NA | 类名：CalendarPickerAttribute；  API声明：textStyle(value: PickerTextStyle): CalendarPickerAttribute;  差异内容：textStyle(value: PickerTextStyle): CalendarPickerAttribute; | component/calendar\_picker.d.ts |
| 新增API | NA | 类名：CalendarPickerAttribute；  API声明：onChange(callback: (value: Date) => void): CalendarPickerAttribute;  差异内容：onChange(callback: (value: Date) => void): CalendarPickerAttribute; | component/calendar\_picker.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface CalendarDialogOptions  差异内容： declare interface CalendarDialogOptions | component/calendar\_picker.d.ts |
| 新增API | NA | 类名：CalendarDialogOptions；  API声明：onAccept?: (value: Date) => void;  差异内容：onAccept?: (value: Date) => void; | component/calendar\_picker.d.ts |
| 新增API | NA | 类名：CalendarDialogOptions；  API声明：onCancel?: () => void;  差异内容：onCancel?: () => void; | component/calendar\_picker.d.ts |
| 新增API | NA | 类名：CalendarDialogOptions；  API声明：onChange?: (value: Date) => void;  差异内容：onChange?: (value: Date) => void; | component/calendar\_picker.d.ts |
| 新增API | NA | 类名：CalendarDialogOptions；  API声明：backgroundColor?: ResourceColor;  差异内容：backgroundColor?: ResourceColor; | component/calendar\_picker.d.ts |
| 新增API | NA | 类名：CalendarDialogOptions；  API声明：backgroundBlurStyle?: BlurStyle;  差异内容：backgroundBlurStyle?: BlurStyle; | component/calendar\_picker.d.ts |
| 新增API | NA | 类名：CalendarDialogOptions；  API声明：acceptButtonStyle?: PickerDialogButtonStyle;  差异内容：acceptButtonStyle?: PickerDialogButtonStyle; | component/calendar\_picker.d.ts |
| 新增API | NA | 类名：CalendarDialogOptions；  API声明：cancelButtonStyle?: PickerDialogButtonStyle;  差异内容：cancelButtonStyle?: PickerDialogButtonStyle; | component/calendar\_picker.d.ts |
| 新增API | NA | 类名：CalendarDialogOptions；  API声明：onDidAppear?: () => void;  差异内容：onDidAppear?: () => void; | component/calendar\_picker.d.ts |
| 新增API | NA | 类名：CalendarDialogOptions；  API声明：onDidDisappear?: () => void;  差异内容：onDidDisappear?: () => void; | component/calendar\_picker.d.ts |
| 新增API | NA | 类名：CalendarDialogOptions；  API声明：onWillAppear?: () => void;  差异内容：onWillAppear?: () => void; | component/calendar\_picker.d.ts |
| 新增API | NA | 类名：CalendarDialogOptions；  API声明：onWillDisappear?: () => void;  差异内容：onWillDisappear?: () => void; | component/calendar\_picker.d.ts |
| 新增API | NA | 类名：CalendarDialogOptions；  API声明：shadow?: ShadowOptions | ShadowStyle;  差异内容：shadow?: ShadowOptions | ShadowStyle; | component/calendar\_picker.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class CalendarPickerDialog  差异内容： declare class CalendarPickerDialog | component/calendar\_picker.d.ts |
| 新增API | NA | 类名：CalendarPickerDialog；  API声明：static show(options?: CalendarDialogOptions): void;  差异内容：static show(options?: CalendarDialogOptions): void; | component/calendar\_picker.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const CalendarPicker: CalendarPickerInterface;  差异内容：declare const CalendarPicker: CalendarPickerInterface; | component/calendar\_picker.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const CalendarPickerInstance: CalendarPickerAttribute;  差异内容：declare const CalendarPickerInstance: CalendarPickerAttribute; | component/calendar\_picker.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type Scene = import('../api/@ohos.graphics.scene').Scene;  差异内容：declare type Scene = import('../api/@ohos.graphics.scene').Scene; | component/component3d.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum ModelType  差异内容： declare enum ModelType | component/component3d.d.ts |
| 新增API | NA | 类名：ModelType；  API声明：TEXTURE = 0  差异内容：TEXTURE = 0 | component/component3d.d.ts |
| 新增API | NA | 类名：ModelType；  API声明：SURFACE = 1  差异内容：SURFACE = 1 | component/component3d.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface SceneOptions  差异内容： declare interface SceneOptions | component/component3d.d.ts |
| 新增API | NA | 类名：SceneOptions；  API声明：scene?: Resource | Scene;  差异内容：scene?: Resource | Scene; | component/component3d.d.ts |
| 新增API | NA | 类名：SceneOptions；  API声明：modelType?: ModelType;  差异内容：modelType?: ModelType; | component/component3d.d.ts |
| 新增API | NA | 类名：global；  API声明： interface Component3DInterface  差异内容： interface Component3DInterface | component/component3d.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class Component3DAttribute  差异内容： declare class Component3DAttribute | component/component3d.d.ts |
| 新增API | NA | 类名：Component3DAttribute；  API声明：environment(uri: Resource): Component3DAttribute;  差异内容：environment(uri: Resource): Component3DAttribute; | component/component3d.d.ts |
| 新增API | NA | 类名：Component3DAttribute；  API声明：customRender(uri: Resource, selfRenderUpdate: boolean): Component3DAttribute;  差异内容：customRender(uri: Resource, selfRenderUpdate: boolean): Component3DAttribute; | component/component3d.d.ts |
| 新增API | NA | 类名：Component3DAttribute；  API声明：shader(uri: Resource): Component3DAttribute;  差异内容：shader(uri: Resource): Component3DAttribute; | component/component3d.d.ts |
| 新增API | NA | 类名：Component3DAttribute；  API声明：shaderImageTexture(uri: Resource): Component3DAttribute;  差异内容：shaderImageTexture(uri: Resource): Component3DAttribute; | component/component3d.d.ts |
| 新增API | NA | 类名：Component3DAttribute；  API声明：shaderInputBuffer(buffer: Array<number>): Component3DAttribute;  差异内容：shaderInputBuffer(buffer: Array<number>): Component3DAttribute; | component/component3d.d.ts |
| 新增API | NA | 类名：Component3DAttribute；  API声明：renderWidth(value: Dimension): Component3DAttribute;  差异内容：renderWidth(value: Dimension): Component3DAttribute; | component/component3d.d.ts |
| 新增API | NA | 类名：Component3DAttribute；  API声明：renderHeight(value: Dimension): Component3DAttribute;  差异内容：renderHeight(value: Dimension): Component3DAttribute; | component/component3d.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const Component3D: Component3DInterface;  差异内容：declare const Component3D: Component3DInterface; | component/component3d.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const Component3DInstance: Component3DAttribute;  差异内容：declare const Component3DInstance: Component3DAttribute; | component/component3d.d.ts |
| 新增API | NA | 类名：global；  API声明： interface ContainerSpanInterface  差异内容： interface ContainerSpanInterface | component/container\_span.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class ContainerSpanAttribute  差异内容： declare class ContainerSpanAttribute | component/container\_span.d.ts |
| 新增API | NA | 类名：ContainerSpanAttribute；  API声明：textBackgroundStyle(style: TextBackgroundStyle): ContainerSpanAttribute;  差异内容：textBackgroundStyle(style: TextBackgroundStyle): ContainerSpanAttribute; | component/container\_span.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const ContainerSpan: ContainerSpanInterface;  差异内容：declare const ContainerSpan: ContainerSpanInterface; | component/container\_span.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const ContainerSpanInstance: ContainerSpanAttribute;  差异内容：declare const ContainerSpanInstance: ContainerSpanAttribute; | component/container\_span.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type Content = import('../api/@ohos.arkui.node').Content;  差异内容：declare type Content = import('../api/@ohos.arkui.node').Content; | component/content\_slot.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class ContentSlotAttribute  差异内容： declare class ContentSlotAttribute | component/content\_slot.d.ts |
| 新增API | NA | 类名：global；  API声明： interface ContentSlotInterface  差异内容： interface ContentSlotInterface | component/content\_slot.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const ContentSlot: ContentSlotInterface;  差异内容：declare const ContentSlot: ContentSlotInterface; | component/content\_slot.d.ts |
| 新增API | NA | 类名：global；  API声明： interface EmbeddedComponentInterface  差异内容： interface EmbeddedComponentInterface | component/embedded\_component.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface TerminationInfo  差异内容： declare interface TerminationInfo | component/embedded\_component.d.ts |
| 新增API | NA | 类名：TerminationInfo；  API声明：code: number;  差异内容：code: number; | component/embedded\_component.d.ts |
| 新增API | NA | 类名：TerminationInfo；  API声明：want?: import('../api/@ohos.app.ability.Want').default;  差异内容：want?: import('../api/@ohos.app.ability.Want').default; | component/embedded\_component.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class EmbeddedComponentAttribute  差异内容： declare class EmbeddedComponentAttribute | component/embedded\_component.d.ts |
| 新增API | NA | 类名：EmbeddedComponentAttribute；  API声明：onTerminated(callback: import('../api/@ohos.base').Callback<TerminationInfo>): EmbeddedComponentAttribute;  差异内容：onTerminated(callback: import('../api/@ohos.base').Callback<TerminationInfo>): EmbeddedComponentAttribute; | component/embedded\_component.d.ts |
| 新增API | NA | 类名：EmbeddedComponentAttribute；  API声明：onError(callback: import('../api/@ohos.base').ErrorCallback): EmbeddedComponentAttribute;  差异内容：onError(callback: import('../api/@ohos.base').ErrorCallback): EmbeddedComponentAttribute; | component/embedded\_component.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const EmbeddedComponent: EmbeddedComponentInterface;  差异内容：declare const EmbeddedComponent: EmbeddedComponentInterface; | component/embedded\_component.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const EmbeddedComponentInstance: EmbeddedComponentAttribute;  差异内容：declare const EmbeddedComponentInstance: EmbeddedComponentAttribute; | component/embedded\_component.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type WindowMode = import('../api/@ohos.window').WindowMode;  差异内容：declare type WindowMode = import('../api/@ohos.window').WindowMode; | component/folder\_stack.d.ts |
| 新增API | NA | 类名：global；  API声明： interface FolderStackInterface  差异内容： interface FolderStackInterface | component/folder\_stack.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class FolderStackAttribute  差异内容： declare class FolderStackAttribute | component/folder\_stack.d.ts |
| 新增API | NA | 类名：FolderStackAttribute；  API声明：alignContent(value: Alignment): FolderStackAttribute;  差异内容：alignContent(value: Alignment): FolderStackAttribute; | component/folder\_stack.d.ts |
| 新增API | NA | 类名：FolderStackAttribute；  API声明：onFolderStateChange(callback: (event: {  /\*\*  \* folder state.  \*  \* @type { FoldStatus }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 11  \*/  foldStatus: FoldStatus;  }) => void): FolderStackAttribute;  差异内容：onFolderStateChange(callback: (event: {  /\*\*  \* folder state.  \*  \* @type { FoldStatus }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 11  \*/  foldStatus: FoldStatus;  }) => void): FolderStackAttribute; | component/folder\_stack.d.ts |
| 新增API | NA | 类名：FolderStackAttribute；  API声明：onHoverStatusChange(handler: (param: HoverEventParam) => void): FolderStackAttribute;  差异内容：onHoverStatusChange(handler: (param: HoverEventParam) => void): FolderStackAttribute; | component/folder\_stack.d.ts |
| 新增API | NA | 类名：FolderStackAttribute；  API声明：enableAnimation(value: boolean): FolderStackAttribute;  差异内容：enableAnimation(value: boolean): FolderStackAttribute; | component/folder\_stack.d.ts |
| 新增API | NA | 类名：FolderStackAttribute；  API声明：autoHalfFold(value: boolean): FolderStackAttribute;  差异内容：autoHalfFold(value: boolean): FolderStackAttribute; | component/folder\_stack.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface HoverEventParam  差异内容： declare interface HoverEventParam | component/folder\_stack.d.ts |
| 新增API | NA | 类名：HoverEventParam；  API声明：foldStatus: FoldStatus;  差异内容：foldStatus: FoldStatus; | component/folder\_stack.d.ts |
| 新增API | NA | 类名：HoverEventParam；  API声明：isHoverMode: boolean;  差异内容：isHoverMode: boolean; | component/folder\_stack.d.ts |
| 新增API | NA | 类名：HoverEventParam；  API声明：appRotation: AppRotation;  差异内容：appRotation: AppRotation; | component/folder\_stack.d.ts |
| 新增API | NA | 类名：HoverEventParam；  API声明：windowMode: WindowMode;  差异内容：windowMode: WindowMode; | component/folder\_stack.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const FolderStack: FolderStackInterface;  差异内容：declare const FolderStack: FolderStackInterface; | component/folder\_stack.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const FolderStackInstance: FolderStackAttribute;  差异内容：declare const FolderStackInstance: FolderStackAttribute; | component/folder\_stack.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface FormLinkOptions  差异内容： declare interface FormLinkOptions | component/form\_link.d.ts |
| 新增API | NA | 类名：FormLinkOptions；  API声明：action: string;  差异内容：action: string; | component/form\_link.d.ts |
| 新增API | NA | 类名：FormLinkOptions；  API声明：moduleName?: string;  差异内容：moduleName?: string; | component/form\_link.d.ts |
| 新增API | NA | 类名：FormLinkOptions；  API声明：bundleName?: string;  差异内容：bundleName?: string; | component/form\_link.d.ts |
| 新增API | NA | 类名：FormLinkOptions；  API声明：abilityName?: string;  差异内容：abilityName?: string; | component/form\_link.d.ts |
| 新增API | NA | 类名：FormLinkOptions；  API声明：uri?: string;  差异内容：uri?: string; | component/form\_link.d.ts |
| 新增API | NA | 类名：FormLinkOptions；  API声明：params?: Object;  差异内容：params?: Object; | component/form\_link.d.ts |
| 新增API | NA | 类名：global；  API声明： interface FormLinkInterface  差异内容： interface FormLinkInterface | component/form\_link.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class FormLinkAttribute  差异内容： declare class FormLinkAttribute | component/form\_link.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const FormLink: FormLinkInterface;  差异内容：declare const FormLink: FormLinkInterface; | component/form\_link.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const FormLinkInstance: FormLinkAttribute;  差异内容：declare const FormLinkInstance: FormLinkAttribute; | component/form\_link.d.ts |
| 新增API | NA | 类名：global；  API声明： interface ImageSpanInterface  差异内容： interface ImageSpanInterface | component/image\_span.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class ImageSpanAttribute  差异内容： declare class ImageSpanAttribute | component/image\_span.d.ts |
| 新增API | NA | 类名：ImageSpanAttribute；  API声明：verticalAlign(value: ImageSpanAlignment): ImageSpanAttribute;  差异内容：verticalAlign(value: ImageSpanAlignment): ImageSpanAttribute; | component/image\_span.d.ts |
| 新增API | NA | 类名：ImageSpanAttribute；  API声明：objectFit(value: ImageFit): ImageSpanAttribute;  差异内容：objectFit(value: ImageFit): ImageSpanAttribute; | component/image\_span.d.ts |
| 新增API | NA | 类名：ImageSpanAttribute；  API声明：onComplete(callback: ImageCompleteCallback): ImageSpanAttribute;  差异内容：onComplete(callback: ImageCompleteCallback): ImageSpanAttribute; | component/image\_span.d.ts |
| 新增API | NA | 类名：ImageSpanAttribute；  API声明：onError(callback: ImageErrorCallback): ImageSpanAttribute;  差异内容：onError(callback: ImageErrorCallback): ImageSpanAttribute; | component/image\_span.d.ts |
| 新增API | NA | 类名：ImageSpanAttribute；  API声明：alt(value: PixelMap): ImageSpanAttribute;  差异内容：alt(value: PixelMap): ImageSpanAttribute; | component/image\_span.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const ImageSpan: ImageSpanInterface;  差异内容：declare const ImageSpan: ImageSpanInterface; | component/image\_span.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const ImageSpanInstance: ImageSpanAttribute;  差异内容：declare const ImageSpanInstance: ImageSpanAttribute; | component/image\_span.d.ts |
| 新增API | NA | 类名：global；  API声明：type ImageCompleteCallback = (result: ImageLoadResult) => void;  差异内容：type ImageCompleteCallback = (result: ImageLoadResult) => void; | component/image\_span.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface ImageLoadResult  差异内容： declare interface ImageLoadResult | component/image\_span.d.ts |
| 新增API | NA | 类名：ImageLoadResult；  API声明：width: number;  差异内容：width: number; | component/image\_span.d.ts |
| 新增API | NA | 类名：ImageLoadResult；  API声明：height: number;  差异内容：height: number; | component/image\_span.d.ts |
| 新增API | NA | 类名：ImageLoadResult；  API声明：componentWidth: number;  差异内容：componentWidth: number; | component/image\_span.d.ts |
| 新增API | NA | 类名：ImageLoadResult；  API声明：componentHeight: number;  差异内容：componentHeight: number; | component/image\_span.d.ts |
| 新增API | NA | 类名：ImageLoadResult；  API声明：loadingStatus: number;  差异内容：loadingStatus: number; | component/image\_span.d.ts |
| 新增API | NA | 类名：ImageLoadResult；  API声明：contentWidth: number;  差异内容：contentWidth: number; | component/image\_span.d.ts |
| 新增API | NA | 类名：ImageLoadResult；  API声明：contentHeight: number;  差异内容：contentHeight: number; | component/image\_span.d.ts |
| 新增API | NA | 类名：ImageLoadResult；  API声明：contentOffsetX: number;  差异内容：contentOffsetX: number; | component/image\_span.d.ts |
| 新增API | NA | 类名：ImageLoadResult；  API声明：contentOffsetY: number;  差异内容：contentOffsetY: number; | component/image\_span.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum LocationIconStyle  差异内容： declare enum LocationIconStyle | component/location\_button.d.ts |
| 新增API | NA | 类名：LocationIconStyle；  API声明：FULL\_FILLED = 0  差异内容：FULL\_FILLED = 0 | component/location\_button.d.ts |
| 新增API | NA | 类名：LocationIconStyle；  API声明：LINES = 1  差异内容：LINES = 1 | component/location\_button.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum LocationDescription  差异内容： declare enum LocationDescription | component/location\_button.d.ts |
| 新增API | NA | 类名：LocationDescription；  API声明：CURRENT\_LOCATION = 0  差异内容：CURRENT\_LOCATION = 0 | component/location\_button.d.ts |
| 新增API | NA | 类名：LocationDescription；  API声明：ADD\_LOCATION = 1  差异内容：ADD\_LOCATION = 1 | component/location\_button.d.ts |
| 新增API | NA | 类名：LocationDescription；  API声明：SELECT\_LOCATION = 2  差异内容：SELECT\_LOCATION = 2 | component/location\_button.d.ts |
| 新增API | NA | 类名：LocationDescription；  API声明：SHARE\_LOCATION = 3  差异内容：SHARE\_LOCATION = 3 | component/location\_button.d.ts |
| 新增API | NA | 类名：LocationDescription；  API声明：SEND\_LOCATION = 4  差异内容：SEND\_LOCATION = 4 | component/location\_button.d.ts |
| 新增API | NA | 类名：LocationDescription；  API声明：LOCATING = 5  差异内容：LOCATING = 5 | component/location\_button.d.ts |
| 新增API | NA | 类名：LocationDescription；  API声明：LOCATION = 6  差异内容：LOCATION = 6 | component/location\_button.d.ts |
| 新增API | NA | 类名：LocationDescription；  API声明：SEND\_CURRENT\_LOCATION = 7  差异内容：SEND\_CURRENT\_LOCATION = 7 | component/location\_button.d.ts |
| 新增API | NA | 类名：LocationDescription；  API声明：RELOCATION = 8  差异内容：RELOCATION = 8 | component/location\_button.d.ts |
| 新增API | NA | 类名：LocationDescription；  API声明：PUNCH\_IN = 9  差异内容：PUNCH\_IN = 9 | component/location\_button.d.ts |
| 新增API | NA | 类名：LocationDescription；  API声明：CURRENT\_POSITION = 10  差异内容：CURRENT\_POSITION = 10 | component/location\_button.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface LocationButtonOptions  差异内容： declare interface LocationButtonOptions | component/location\_button.d.ts |
| 新增API | NA | 类名：LocationButtonOptions；  API声明：icon?: LocationIconStyle;  差异内容：icon?: LocationIconStyle; | component/location\_button.d.ts |
| 新增API | NA | 类名：LocationButtonOptions；  API声明：text?: LocationDescription;  差异内容：text?: LocationDescription; | component/location\_button.d.ts |
| 新增API | NA | 类名：LocationButtonOptions；  API声明：buttonType?: ButtonType;  差异内容：buttonType?: ButtonType; | component/location\_button.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum LocationButtonOnClickResult  差异内容： declare enum LocationButtonOnClickResult | component/location\_button.d.ts |
| 新增API | NA | 类名：LocationButtonOnClickResult；  API声明：SUCCESS = 0  差异内容：SUCCESS = 0 | component/location\_button.d.ts |
| 新增API | NA | 类名：LocationButtonOnClickResult；  API声明：TEMPORARY\_AUTHORIZATION\_FAILED = 1  差异内容：TEMPORARY\_AUTHORIZATION\_FAILED = 1 | component/location\_button.d.ts |
| 新增API | NA | 类名：global；  API声明： interface LocationButtonInterface  差异内容： interface LocationButtonInterface | component/location\_button.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class LocationButtonAttribute  差异内容： declare class LocationButtonAttribute | component/location\_button.d.ts |
| 新增API | NA | 类名：LocationButtonAttribute；  API声明：onClick(event: (event: ClickEvent, result: LocationButtonOnClickResult) => void): LocationButtonAttribute;  差异内容：onClick(event: (event: ClickEvent, result: LocationButtonOnClickResult) => void): LocationButtonAttribute; | component/location\_button.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const LocationButton: LocationButtonInterface;  差异内容：declare const LocationButton: LocationButtonInterface; | component/location\_button.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const LocationButtonInstance: LocationButtonAttribute;  差异内容：declare const LocationButtonInstance: LocationButtonAttribute; | component/location\_button.d.ts |
| 新增API | NA | 类名：global；  API声明： interface NodeContainerInterface  差异内容： interface NodeContainerInterface | component/node\_container.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class NodeContainerAttribute  差异内容： declare class NodeContainerAttribute | component/node\_container.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const NodeContainer: NodeContainerInterface;  差异内容：declare const NodeContainer: NodeContainerInterface; | component/node\_container.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const NodeContainerInstance: NodeContainerAttribute;  差异内容：declare const NodeContainerInstance: NodeContainerAttribute; | component/node\_container.d.ts |
| 新增API | NA | 类名：global；  API声明： interface ParticleOptions  差异内容： interface ParticleOptions | component/particle.d.ts |
| 新增API | NA | 类名：ParticleOptions；  API声明：emitter: EmitterOptions<PARTICLE>;  差异内容：emitter: EmitterOptions<PARTICLE>; | component/particle.d.ts |
| 新增API | NA | 类名：ParticleOptions；  API声明：color?: ParticleColorPropertyOptions<COLOR\_UPDATER>;  差异内容：color?: ParticleColorPropertyOptions<COLOR\_UPDATER>; | component/particle.d.ts |
| 新增API | NA | 类名：ParticleOptions；  API声明：opacity?: ParticlePropertyOptions<number, OPACITY\_UPDATER>;  差异内容：opacity?: ParticlePropertyOptions<number, OPACITY\_UPDATER>; | component/particle.d.ts |
| 新增API | NA | 类名：ParticleOptions；  API声明：scale?: ParticlePropertyOptions<number, SCALE\_UPDATER>;  差异内容：scale?: ParticlePropertyOptions<number, SCALE\_UPDATER>; | component/particle.d.ts |
| 新增API | NA | 类名：ParticleOptions；  API声明：velocity?: {  speed: [  number,  number  ];  angle: [  number,  number  ];  };  差异内容：velocity?: {  speed: [  number,  number  ];  angle: [  number,  number  ];  }; | component/particle.d.ts |
| 新增API | NA | 类名：ParticleOptions；  API声明：acceleration?: {  speed?: ParticlePropertyOptions<number, ACC\_SPEED\_UPDATER>;  angle?: ParticlePropertyOptions<number, ACC\_ANGLE\_UPDATER>;  };  差异内容：acceleration?: {  speed?: ParticlePropertyOptions<number, ACC\_SPEED\_UPDATER>;  angle?: ParticlePropertyOptions<number, ACC\_ANGLE\_UPDATER>;  }; | component/particle.d.ts |
| 新增API | NA | 类名：ParticleOptions；  API声明：spin?: ParticlePropertyOptions<number, SPIN\_UPDATER>;  差异内容：spin?: ParticlePropertyOptions<number, SPIN\_UPDATER>; | component/particle.d.ts |
| 新增API | NA | 类名：global；  API声明： interface PointParticleParameters  差异内容： interface PointParticleParameters | component/particle.d.ts |
| 新增API | NA | 类名：PointParticleParameters；  API声明：radius: VP;  差异内容：radius: VP; | component/particle.d.ts |
| 新增API | NA | 类名：global；  API声明： interface ImageParticleParameters  差异内容： interface ImageParticleParameters | component/particle.d.ts |
| 新增API | NA | 类名：ImageParticleParameters；  API声明：src: ResourceStr;  差异内容：src: ResourceStr; | component/particle.d.ts |
| 新增API | NA | 类名：ImageParticleParameters；  API声明：size: [  Dimension,  Dimension  ];  差异内容：size: [  Dimension,  Dimension  ]; | component/particle.d.ts |
| 新增API | NA | 类名：ImageParticleParameters；  API声明：objectFit?: ImageFit;  差异内容：objectFit?: ImageFit; | component/particle.d.ts |
| 新增API | NA | 类名：global；  API声明： interface ParticleConfigs  差异内容： interface ParticleConfigs | component/particle.d.ts |
| 新增API | NA | 类名：ParticleConfigs；  API声明：[ParticleType.POINT]: PointParticleParameters;  差异内容：[ParticleType.POINT]: PointParticleParameters; | component/particle.d.ts |
| 新增API | NA | 类名：ParticleConfigs；  API声明：[ParticleType.IMAGE]: ImageParticleParameters;  差异内容：[ParticleType.IMAGE]: ImageParticleParameters; | component/particle.d.ts |
| 新增API | NA | 类名：global；  API声明： interface EmitterProperty  差异内容： interface EmitterProperty | component/particle.d.ts |
| 新增API | NA | 类名：EmitterProperty；  API声明：index: number;  差异内容：index: number; | component/particle.d.ts |
| 新增API | NA | 类名：EmitterProperty；  API声明：emitRate?: number;  差异内容：emitRate?: number; | component/particle.d.ts |
| 新增API | NA | 类名：EmitterProperty；  API声明：position?: PositionT<number>;  差异内容：position?: PositionT<number>; | component/particle.d.ts |
| 新增API | NA | 类名：EmitterProperty；  API声明：size?: SizeT<number>;  差异内容：size?: SizeT<number>; | component/particle.d.ts |
| 新增API | NA | 类名：global；  API声明： interface EmitterOptions  差异内容： interface EmitterOptions | component/particle.d.ts |
| 新增API | NA | 类名：EmitterOptions；  API声明：particle: {  /  **\* Particle type.**  **\* @type { PARTICLE }**  **\* @syscap SystemCapability.ArkUI.ArkUI.Full**  **\* @crossplatform**  **\* @since 10**  **\*/**  **/\*\***  **\* Particle type.**  **\* @type { PARTICLE }**  **\* @syscap SystemCapability.ArkUI.ArkUI.Full**  **\* @crossplatform**  **\* @atomicservice**  **\* @since 11**  **\*/**  **type: PARTICLE;**  **/**    \* Particle config.  \* @type { ParticleConfigs[PARTICLE] }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 10  \*/  /  **\* Particle config.**  **\* @type { ParticleConfigs[PARTICLE] }**  **\* @syscap SystemCapability.ArkUI.ArkUI.Full**  **\* @crossplatform**  **\* @atomicservice**  **\* @since 11**  **\*/**  **config: ParticleConfigs[PARTICLE];**  **/\*\***  **\* Particle count.**  **\* @type { number }**  **\* @syscap SystemCapability.ArkUI.ArkUI.Full**  **\* @crossplatform**  **\* @since 10**  **\*/**  **/**    \* Particle count.  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @atomicservice  \* @since 11  \*/  count: number;  /  **\* Particle lifetime.**  **\* @type { ?number }**  **\* @default 1000**  **\* @syscap SystemCapability.ArkUI.ArkUI.Full**  **\* @crossplatform**  **\* @since 10**  **\*/**  **/\*\***  **\* Particle lifetime.**  **\* @type { ?number }**  **\* @default 1000**  **\* @syscap SystemCapability.ArkUI.ArkUI.Full**  **\* @crossplatform**  **\* @atomicservice**  **\* @since 11**  **\*/**  **lifetime?: number;**  **/**    \* Particle lifetimeRange,value range [0, ∞).  \* when lifetimeRange>lifetime,minimum lifetime is 0.  \* @type { ?number }  \* @default 0  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 12  \*/  lifetimeRange?: number;  };  差异内容：particle: {  /  **\* Particle type.**  **\* @type { PARTICLE }**  **\* @syscap SystemCapability.ArkUI.ArkUI.Full**  **\* @crossplatform**  **\* @since 10**  **\*/**  **/\*\***  **\* Particle type.**  **\* @type { PARTICLE }**  **\* @syscap SystemCapability.ArkUI.ArkUI.Full**  **\* @crossplatform**  **\* @atomicservice**  **\* @since 11**  **\*/**  **type: PARTICLE;**  **/**    \* Particle config.  \* @type { ParticleConfigs[PARTICLE] }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 10  \*/  /  **\* Particle config.**  **\* @type { ParticleConfigs[PARTICLE] }**  **\* @syscap SystemCapability.ArkUI.ArkUI.Full**  **\* @crossplatform**  **\* @atomicservice**  **\* @since 11**  **\*/**  **config: ParticleConfigs[PARTICLE];**  **/\*\***  **\* Particle count.**  **\* @type { number }**  **\* @syscap SystemCapability.ArkUI.ArkUI.Full**  **\* @crossplatform**  **\* @since 10**  **\*/**  **/**    \* Particle count.  \* @type { number }  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @atomicservice  \* @since 11  \*/  count: number;  /  **\* Particle lifetime.**  **\* @type { ?number }**  **\* @default 1000**  **\* @syscap SystemCapability.ArkUI.ArkUI.Full**  **\* @crossplatform**  **\* @since 10**  **\*/**  **/\*\***  **\* Particle lifetime.**  **\* @type { ?number }**  **\* @default 1000**  **\* @syscap SystemCapability.ArkUI.ArkUI.Full**  **\* @crossplatform**  **\* @atomicservice**  **\* @since 11**  **\*/**  **lifetime?: number;**  **/**    \* Particle lifetimeRange,value range [0, ∞).  \* when lifetimeRange>lifetime,minimum lifetime is 0.  \* @type { ?number }  \* @default 0  \* @syscap SystemCapability.ArkUI.ArkUI.Full  \* @crossplatform  \* @since 12  \*/  lifetimeRange?: number;  }; | component/particle.d.ts |
| 新增API | NA | 类名：EmitterOptions；  API声明：emitRate?: number;  差异内容：emitRate?: number; | component/particle.d.ts |
| 新增API | NA | 类名：EmitterOptions；  API声明：shape?: ParticleEmitterShape;  差异内容：shape?: ParticleEmitterShape; | component/particle.d.ts |
| 新增API | NA | 类名：EmitterOptions；  API声明：position?: [  Dimension,  Dimension  ];  差异内容：position?: [  Dimension,  Dimension  ]; | component/particle.d.ts |
| 新增API | NA | 类名：EmitterOptions；  API声明：size?: [  Dimension,  Dimension  ];  差异内容：size?: [  Dimension,  Dimension  ]; | component/particle.d.ts |
| 新增API | NA | 类名：global；  API声明： interface ParticlePropertyUpdaterConfigs  差异内容： interface ParticlePropertyUpdaterConfigs | component/particle.d.ts |
| 新增API | NA | 类名：ParticlePropertyUpdaterConfigs；  API声明：[ParticleUpdater.NONE]: void;  差异内容：[ParticleUpdater.NONE]: void; | component/particle.d.ts |
| 新增API | NA | 类名：ParticlePropertyUpdaterConfigs；  API声明：[ParticleUpdater.RANDOM]: [  T,  T  ];  差异内容：[ParticleUpdater.RANDOM]: [  T,  T  ]; | component/particle.d.ts |
| 新增API | NA | 类名：ParticlePropertyUpdaterConfigs；  API声明：[ParticleUpdater.CURVE]: Array<ParticlePropertyAnimation<T>>;  差异内容：[ParticleUpdater.CURVE]: Array<ParticlePropertyAnimation<T>>; | component/particle.d.ts |
| 新增API | NA | 类名：global；  API声明： interface ParticlePropertyOptions  差异内容： interface ParticlePropertyOptions | component/particle.d.ts |
| 新增API | NA | 类名：ParticlePropertyOptions；  API声明：range: [  TYPE,  TYPE  ];  差异内容：range: [  TYPE,  TYPE  ]; | component/particle.d.ts |
| 新增API | NA | 类名：ParticlePropertyOptions；  API声明：updater?: {  type: UPDATER;  config: ParticlePropertyUpdaterConfigs<TYPE>[UPDATER];  };  差异内容：updater?: {  type: UPDATER;  config: ParticlePropertyUpdaterConfigs<TYPE>[UPDATER];  }; | component/particle.d.ts |
| 新增API | NA | 类名：global；  API声明： interface ParticleColorPropertyUpdaterConfigs  差异内容： interface ParticleColorPropertyUpdaterConfigs | component/particle.d.ts |
| 新增API | NA | 类名：ParticleColorPropertyUpdaterConfigs；  API声明：[ParticleUpdater.NONE]: void;  差异内容：[ParticleUpdater.NONE]: void; | component/particle.d.ts |
| 新增API | NA | 类名：ParticleColorPropertyUpdaterConfigs；  API声明：[ParticleUpdater.RANDOM]: {  r: [  number,  number  ];  g: [  number,  number  ];  b: [  number,  number  ];  a: [  number,  number  ];  };  差异内容：[ParticleUpdater.RANDOM]: {  r: [  number,  number  ];  g: [  number,  number  ];  b: [  number,  number  ];  a: [  number,  number  ];  }; | component/particle.d.ts |
| 新增API | NA | 类名：ParticleColorPropertyUpdaterConfigs；  API声明：[ParticleUpdater.CURVE]: Array<ParticlePropertyAnimation<ResourceColor>>;  差异内容：[ParticleUpdater.CURVE]: Array<ParticlePropertyAnimation<ResourceColor>>; | component/particle.d.ts |
| 新增API | NA | 类名：global；  API声明： interface ParticleColorPropertyOptions  差异内容： interface ParticleColorPropertyOptions | component/particle.d.ts |
| 新增API | NA | 类名：ParticleColorPropertyOptions；  API声明：range: [  ResourceColor,  ResourceColor  ];  差异内容：range: [  ResourceColor,  ResourceColor  ]; | component/particle.d.ts |
| 新增API | NA | 类名：ParticleColorPropertyOptions；  API声明：distributionType?: DistributionType;  差异内容：distributionType?: DistributionType; | component/particle.d.ts |
| 新增API | NA | 类名：ParticleColorPropertyOptions；  API声明：updater?: {  type: UPDATER;  config: ParticleColorPropertyUpdaterConfigs[UPDATER];  };  差异内容：updater?: {  type: UPDATER;  config: ParticleColorPropertyUpdaterConfigs[UPDATER];  }; | component/particle.d.ts |
| 新增API | NA | 类名：global；  API声明： interface ParticlePropertyAnimation  差异内容： interface ParticlePropertyAnimation | component/particle.d.ts |
| 新增API | NA | 类名：ParticlePropertyAnimation；  API声明：from: T;  差异内容：from: T; | component/particle.d.ts |
| 新增API | NA | 类名：ParticlePropertyAnimation；  API声明：to: T;  差异内容：to: T; | component/particle.d.ts |
| 新增API | NA | 类名：ParticlePropertyAnimation；  API声明：startMillis: number;  差异内容：startMillis: number; | component/particle.d.ts |
| 新增API | NA | 类名：ParticlePropertyAnimation；  API声明：endMillis: number;  差异内容：endMillis: number; | component/particle.d.ts |
| 新增API | NA | 类名：ParticlePropertyAnimation；  API声明：curve?: Curve | ICurve;  差异内容：curve?: Curve | ICurve; | component/particle.d.ts |
| 新增API | NA | 类名：global；  API声明： interface ParticleInterface  差异内容： interface ParticleInterface | component/particle.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum ParticleType  差异内容： declare enum ParticleType | component/particle.d.ts |
| 新增API | NA | 类名：ParticleType；  API声明：POINT = 'point'  差异内容：POINT = 'point' | component/particle.d.ts |
| 新增API | NA | 类名：ParticleType；  API声明：IMAGE = 'image'  差异内容：IMAGE = 'image' | component/particle.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum ParticleEmitterShape  差异内容： declare enum ParticleEmitterShape | component/particle.d.ts |
| 新增API | NA | 类名：ParticleEmitterShape；  API声明：RECTANGLE = 'rectangle'  差异内容：RECTANGLE = 'rectangle' | component/particle.d.ts |
| 新增API | NA | 类名：ParticleEmitterShape；  API声明：CIRCLE = 'circle'  差异内容：CIRCLE = 'circle' | component/particle.d.ts |
| 新增API | NA | 类名：ParticleEmitterShape；  API声明：ELLIPSE = 'ellipse'  差异内容：ELLIPSE = 'ellipse' | component/particle.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum DistributionType  差异内容： declare enum DistributionType | component/particle.d.ts |
| 新增API | NA | 类名：DistributionType；  API声明：UNIFORM = 0  差异内容：UNIFORM = 0 | component/particle.d.ts |
| 新增API | NA | 类名：DistributionType；  API声明：GAUSSIAN = 1  差异内容：GAUSSIAN = 1 | component/particle.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum ParticleUpdater  差异内容： declare enum ParticleUpdater | component/particle.d.ts |
| 新增API | NA | 类名：ParticleUpdater；  API声明：NONE = 'none'  差异内容：NONE = 'none' | component/particle.d.ts |
| 新增API | NA | 类名：ParticleUpdater；  API声明：RANDOM = 'random'  差异内容：RANDOM = 'random' | component/particle.d.ts |
| 新增API | NA | 类名：ParticleUpdater；  API声明：CURVE = 'curve'  差异内容：CURVE = 'curve' | component/particle.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type SizeT<T> = import('../../../../api/arkui/Graphics').SizeT<T>;  差异内容：declare type SizeT<T> = import('../../../../api/arkui/Graphics').SizeT<T>; | component/particle.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type PositionT<T> = import('../../../../api/arkui/Graphics').PositionT<T>;  差异内容：declare type PositionT<T> = import('../../../../api/arkui/Graphics').PositionT<T>; | component/particle.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class ParticleAttribute  差异内容： declare class ParticleAttribute | component/particle.d.ts |
| 新增API | NA | 类名：ParticleAttribute；  API声明：disturbanceFields(fields: Array<DisturbanceFieldOptions>): ParticleAttribute;  差异内容：disturbanceFields(fields: Array<DisturbanceFieldOptions>): ParticleAttribute; | component/particle.d.ts |
| 新增API | NA | 类名：ParticleAttribute；  API声明：emitter(value: Array<EmitterProperty>): ParticleAttribute;  差异内容：emitter(value: Array<EmitterProperty>): ParticleAttribute; | component/particle.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const Particle: ParticleInterface;  差异内容：declare const Particle: ParticleInterface; | component/particle.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface DisturbanceFieldOptions  差异内容： declare interface DisturbanceFieldOptions | component/particle.d.ts |
| 新增API | NA | 类名：DisturbanceFieldOptions；  API声明：strength?: number;  差异内容：strength?: number; | component/particle.d.ts |
| 新增API | NA | 类名：DisturbanceFieldOptions；  API声明：shape?: DisturbanceFieldShape;  差异内容：shape?: DisturbanceFieldShape; | component/particle.d.ts |
| 新增API | NA | 类名：DisturbanceFieldOptions；  API声明：size?: SizeT<number>;  差异内容：size?: SizeT<number>; | component/particle.d.ts |
| 新增API | NA | 类名：DisturbanceFieldOptions；  API声明：position?: PositionT<number>;  差异内容：position?: PositionT<number>; | component/particle.d.ts |
| 新增API | NA | 类名：DisturbanceFieldOptions；  API声明：feather?: number;  差异内容：feather?: number; | component/particle.d.ts |
| 新增API | NA | 类名：DisturbanceFieldOptions；  API声明：noiseScale?: number;  差异内容：noiseScale?: number; | component/particle.d.ts |
| 新增API | NA | 类名：DisturbanceFieldOptions；  API声明：noiseFrequency?: number;  差异内容：noiseFrequency?: number; | component/particle.d.ts |
| 新增API | NA | 类名：DisturbanceFieldOptions；  API声明：noiseAmplitude?: number;  差异内容：noiseAmplitude?: number; | component/particle.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum DisturbanceFieldShape  差异内容： declare enum DisturbanceFieldShape | component/particle.d.ts |
| 新增API | NA | 类名：DisturbanceFieldShape；  API声明：RECT  差异内容：RECT | component/particle.d.ts |
| 新增API | NA | 类名：DisturbanceFieldShape；  API声明：CIRCLE  差异内容：CIRCLE | component/particle.d.ts |
| 新增API | NA | 类名：DisturbanceFieldShape；  API声明：ELLIPSE  差异内容：ELLIPSE | component/particle.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum PasteIconStyle  差异内容： declare enum PasteIconStyle | component/paste\_button.d.ts |
| 新增API | NA | 类名：PasteIconStyle；  API声明：LINES = 0  差异内容：LINES = 0 | component/paste\_button.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum PasteDescription  差异内容： declare enum PasteDescription | component/paste\_button.d.ts |
| 新增API | NA | 类名：PasteDescription；  API声明：PASTE = 0  差异内容：PASTE = 0 | component/paste\_button.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface PasteButtonOptions  差异内容： declare interface PasteButtonOptions | component/paste\_button.d.ts |
| 新增API | NA | 类名：PasteButtonOptions；  API声明：icon?: PasteIconStyle;  差异内容：icon?: PasteIconStyle; | component/paste\_button.d.ts |
| 新增API | NA | 类名：PasteButtonOptions；  API声明：text?: PasteDescription;  差异内容：text?: PasteDescription; | component/paste\_button.d.ts |
| 新增API | NA | 类名：PasteButtonOptions；  API声明：buttonType?: ButtonType;  差异内容：buttonType?: ButtonType; | component/paste\_button.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum PasteButtonOnClickResult  差异内容： declare enum PasteButtonOnClickResult | component/paste\_button.d.ts |
| 新增API | NA | 类名：PasteButtonOnClickResult；  API声明：SUCCESS = 0  差异内容：SUCCESS = 0 | component/paste\_button.d.ts |
| 新增API | NA | 类名：PasteButtonOnClickResult；  API声明：TEMPORARY\_AUTHORIZATION\_FAILED = 1  差异内容：TEMPORARY\_AUTHORIZATION\_FAILED = 1 | component/paste\_button.d.ts |
| 新增API | NA | 类名：global；  API声明： interface PasteButtonInterface  差异内容： interface PasteButtonInterface | component/paste\_button.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class PasteButtonAttribute  差异内容： declare class PasteButtonAttribute | component/paste\_button.d.ts |
| 新增API | NA | 类名：PasteButtonAttribute；  API声明：onClick(event: (event: ClickEvent, result: PasteButtonOnClickResult) => void): PasteButtonAttribute;  差异内容：onClick(event: (event: ClickEvent, result: PasteButtonOnClickResult) => void): PasteButtonAttribute; | component/paste\_button.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const PasteButton: PasteButtonInterface;  差异内容：declare const PasteButton: PasteButtonInterface; | component/paste\_button.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const PasteButtonInstance: PasteButtonAttribute;  差异内容：declare const PasteButtonInstance: PasteButtonAttribute; | component/paste\_button.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum RichEditorDeleteDirection  差异内容： declare enum RichEditorDeleteDirection | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorDeleteDirection；  API声明：BACKWARD  差异内容：BACKWARD | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorDeleteDirection；  API声明：FORWARD  差异内容：FORWARD | component/rich\_editor.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum RichEditorSpanType  差异内容： declare enum RichEditorSpanType | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorSpanType；  API声明：TEXT = 0  差异内容：TEXT = 0 | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorSpanType；  API声明：IMAGE = 1  差异内容：IMAGE = 1 | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorSpanType；  API声明：MIXED = 2  差异内容：MIXED = 2 | component/rich\_editor.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum RichEditorResponseType  差异内容： declare enum RichEditorResponseType | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorResponseType；  API声明：RIGHT\_CLICK = 0  差异内容：RIGHT\_CLICK = 0 | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorResponseType；  API声明：LONG\_PRESS = 1  差异内容：LONG\_PRESS = 1 | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorResponseType；  API声明：SELECT = 2  差异内容：SELECT = 2 | component/rich\_editor.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface RichEditorSpanPosition  差异内容： declare interface RichEditorSpanPosition | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorSpanPosition；  API声明：spanIndex: number;  差异内容：spanIndex: number; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorSpanPosition；  API声明：spanRange: [  number,  number  ];  差异内容：spanRange: [  number,  number  ]; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface RichEditorTextStyle  差异内容： declare interface RichEditorTextStyle | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorTextStyle；  API声明：fontColor?: ResourceColor;  差异内容：fontColor?: ResourceColor; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorTextStyle；  API声明：fontSize?: Length | number;  差异内容：fontSize?: Length | number; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorTextStyle；  API声明：fontStyle?: FontStyle;  差异内容：fontStyle?: FontStyle; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorTextStyle；  API声明：fontWeight?: number | FontWeight | string;  差异内容：fontWeight?: number | FontWeight | string; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorTextStyle；  API声明：fontFamily?: ResourceStr;  差异内容：fontFamily?: ResourceStr; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorTextStyle；  API声明：decoration?: {  type: TextDecorationType;  color?: ResourceColor;  };  差异内容：decoration?: {  type: TextDecorationType;  color?: ResourceColor;  }; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorTextStyle；  API声明：textShadow?: ShadowOptions | Array<ShadowOptions>;  差异内容：textShadow?: ShadowOptions | Array<ShadowOptions>; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorTextStyle；  API声明：letterSpacing?: number | string;  差异内容：letterSpacing?: number | string; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorTextStyle；  API声明：lineHeight?: number | string | Resource;  差异内容：lineHeight?: number | string | Resource; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorTextStyle；  API声明：fontFeature?: string;  差异内容：fontFeature?: string; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface LeadingMarginPlaceholder  差异内容： declare interface LeadingMarginPlaceholder | component/rich\_editor.d.ts |
| 新增API | NA | 类名：LeadingMarginPlaceholder；  API声明：pixelMap: PixelMap;  差异内容：pixelMap: PixelMap; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：LeadingMarginPlaceholder；  API声明：size: [  Dimension,  Dimension  ];  差异内容：size: [  Dimension,  Dimension  ]; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface RichEditorParagraphStyle  差异内容： declare interface RichEditorParagraphStyle | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorParagraphStyle；  API声明：textAlign?: TextAlign;  差异内容：textAlign?: TextAlign; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorParagraphStyle；  API声明：leadingMargin?: Dimension | LeadingMarginPlaceholder;  差异内容：leadingMargin?: Dimension | LeadingMarginPlaceholder; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorParagraphStyle；  API声明：wordBreak?: WordBreak;  差异内容：wordBreak?: WordBreak; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorParagraphStyle；  API声明：lineBreakStrategy?: LineBreakStrategy;  差异内容：lineBreakStrategy?: LineBreakStrategy; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface PasteEvent  差异内容： declare interface PasteEvent | component/rich\_editor.d.ts |
| 新增API | NA | 类名：PasteEvent；  API声明：preventDefault?: () => void;  差异内容：preventDefault?: () => void; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface RichEditorTextSpan  差异内容： declare interface RichEditorTextSpan | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorTextSpan；  API声明：spanPosition: RichEditorSpanPosition;  差异内容：spanPosition: RichEditorSpanPosition; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorTextSpan；  API声明：value: string;  差异内容：value: string; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorTextSpan；  API声明：textStyle?: RichEditorTextStyle;  差异内容：textStyle?: RichEditorTextStyle; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：global；  API声明： interface RichEditorLayoutStyle  差异内容： interface RichEditorLayoutStyle | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorLayoutStyle；  API声明：margin?: Dimension | Margin;  差异内容：margin?: Dimension | Margin; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorLayoutStyle；  API声明：borderRadius?: Dimension | BorderRadiuses;  差异内容：borderRadius?: Dimension | BorderRadiuses; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface RichEditorImageSpanStyle  差异内容： declare interface RichEditorImageSpanStyle | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorImageSpanStyle；  API声明：size?: [  Dimension,  Dimension  ];  差异内容：size?: [  Dimension,  Dimension  ]; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorImageSpanStyle；  API声明：verticalAlign?: ImageSpanAlignment;  差异内容：verticalAlign?: ImageSpanAlignment; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorImageSpanStyle；  API声明：objectFit?: ImageFit;  差异内容：objectFit?: ImageFit; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorImageSpanStyle；  API声明：layoutStyle?: RichEditorLayoutStyle;  差异内容：layoutStyle?: RichEditorLayoutStyle; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface RichEditorSymbolSpanStyle  差异内容： declare interface RichEditorSymbolSpanStyle | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorSymbolSpanStyle；  API声明：fontSize?: number | string | Resource;  差异内容：fontSize?: number | string | Resource; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorSymbolSpanStyle；  API声明：fontColor?: Array<ResourceColor>;  差异内容：fontColor?: Array<ResourceColor>; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorSymbolSpanStyle；  API声明：fontWeight?: number | FontWeight | string;  差异内容：fontWeight?: number | FontWeight | string; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorSymbolSpanStyle；  API声明：effectStrategy?: SymbolEffectStrategy;  差异内容：effectStrategy?: SymbolEffectStrategy; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorSymbolSpanStyle；  API声明：renderingStrategy?: SymbolRenderingStrategy;  差异内容：renderingStrategy?: SymbolRenderingStrategy; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface RichEditorTextStyleResult  差异内容： declare interface RichEditorTextStyleResult | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorTextStyleResult；  API声明：fontColor: ResourceColor;  差异内容：fontColor: ResourceColor; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorTextStyleResult；  API声明：fontSize: number;  差异内容：fontSize: number; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorTextStyleResult；  API声明：fontStyle: FontStyle;  差异内容：fontStyle: FontStyle; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorTextStyleResult；  API声明：fontWeight: number;  差异内容：fontWeight: number; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorTextStyleResult；  API声明：fontFamily: string;  差异内容：fontFamily: string; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorTextStyleResult；  API声明：decoration: {  type: TextDecorationType;  color: ResourceColor;  };  差异内容：decoration: {  type: TextDecorationType;  color: ResourceColor;  }; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorTextStyleResult；  API声明：letterSpacing?: number;  差异内容：letterSpacing?: number; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorTextStyleResult；  API声明：lineHeight?: number;  差异内容：lineHeight?: number; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorTextStyleResult；  API声明：fontFeature?: string;  差异内容：fontFeature?: string; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface RichEditorParagraphResult  差异内容： declare interface RichEditorParagraphResult | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorParagraphResult；  API声明：style: RichEditorParagraphStyle;  差异内容：style: RichEditorParagraphStyle; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorParagraphResult；  API声明：range: [  number,  number  ];  差异内容：range: [  number,  number  ]; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface RichEditorSymbolSpanStyleResult  差异内容： declare interface RichEditorSymbolSpanStyleResult | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorSymbolSpanStyleResult；  API声明：fontSize: number | string | Resource;  差异内容：fontSize: number | string | Resource; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorSymbolSpanStyleResult；  API声明：fontColor: Array<ResourceColor>;  差异内容：fontColor: Array<ResourceColor>; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorSymbolSpanStyleResult；  API声明：fontWeight: number | FontWeight | string;  差异内容：fontWeight: number | FontWeight | string; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorSymbolSpanStyleResult；  API声明：effectStrategy: SymbolEffectStrategy;  差异内容：effectStrategy: SymbolEffectStrategy; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorSymbolSpanStyleResult；  API声明：renderingStrategy: SymbolRenderingStrategy;  差异内容：renderingStrategy: SymbolRenderingStrategy; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface RichEditorTextSpanResult  差异内容： declare interface RichEditorTextSpanResult | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorTextSpanResult；  API声明：spanPosition: RichEditorSpanPosition;  差异内容：spanPosition: RichEditorSpanPosition; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorTextSpanResult；  API声明：value: string;  差异内容：value: string; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorTextSpanResult；  API声明：textStyle: RichEditorTextStyleResult;  差异内容：textStyle: RichEditorTextStyleResult; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorTextSpanResult；  API声明：offsetInSpan: [  number,  number  ];  差异内容：offsetInSpan: [  number,  number  ]; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorTextSpanResult；  API声明：symbolSpanStyle?: RichEditorSymbolSpanStyle;  差异内容：symbolSpanStyle?: RichEditorSymbolSpanStyle; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorTextSpanResult；  API声明：valueResource?: Resource;  差异内容：valueResource?: Resource; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorTextSpanResult；  API声明：paragraphStyle?: RichEditorParagraphStyle;  差异内容：paragraphStyle?: RichEditorParagraphStyle; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorTextSpanResult；  API声明：previewText?: string;  差异内容：previewText?: string; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface RichEditorImageSpanStyleResult  差异内容： declare interface RichEditorImageSpanStyleResult | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorImageSpanStyleResult；  API声明：size: [  number,  number  ];  差异内容：size: [  number,  number  ]; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorImageSpanStyleResult；  API声明：verticalAlign: ImageSpanAlignment;  差异内容：verticalAlign: ImageSpanAlignment; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorImageSpanStyleResult；  API声明：objectFit: ImageFit;  差异内容：objectFit: ImageFit; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorImageSpanStyleResult；  API声明：layoutStyle?: RichEditorLayoutStyle;  差异内容：layoutStyle?: RichEditorLayoutStyle; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface RichEditorImageSpanResult  差异内容： declare interface RichEditorImageSpanResult | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorImageSpanResult；  API声明：spanPosition: RichEditorSpanPosition;  差异内容：spanPosition: RichEditorSpanPosition; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorImageSpanResult；  API声明：valuePixelMap?: PixelMap;  差异内容：valuePixelMap?: PixelMap; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorImageSpanResult；  API声明：valueResourceStr?: ResourceStr;  差异内容：valueResourceStr?: ResourceStr; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorImageSpanResult；  API声明：imageStyle: RichEditorImageSpanStyleResult;  差异内容：imageStyle: RichEditorImageSpanStyleResult; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorImageSpanResult；  API声明：offsetInSpan: [  number,  number  ];  差异内容：offsetInSpan: [  number,  number  ]; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface RichEditorImageSpan  差异内容： declare interface RichEditorImageSpan | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorImageSpan；  API声明：spanPosition: RichEditorSpanPosition;  差异内容：spanPosition: RichEditorSpanPosition; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorImageSpan；  API声明：value: PixelMap | ResourceStr;  差异内容：value: PixelMap | ResourceStr; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorImageSpan；  API声明：imageStyle?: RichEditorImageSpanStyle;  差异内容：imageStyle?: RichEditorImageSpanStyle; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface RichEditorRange  差异内容： declare interface RichEditorRange | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorRange；  API声明：start?: number;  差异内容：start?: number; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorRange；  API声明：end?: number;  差异内容：end?: number; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface RichEditorGesture  差异内容： declare interface RichEditorGesture | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorGesture；  API声明：onClick?: (event: ClickEvent) => void;  差异内容：onClick?: (event: ClickEvent) => void; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorGesture；  API声明：onLongPress?: (event: GestureEvent) => void;  差异内容：onLongPress?: (event: GestureEvent) => void; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface RichEditorTextSpanOptions  差异内容： declare interface RichEditorTextSpanOptions | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorTextSpanOptions；  API声明：offset?: number;  差异内容：offset?: number; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorTextSpanOptions；  API声明：style?: RichEditorTextStyle;  差异内容：style?: RichEditorTextStyle; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorTextSpanOptions；  API声明：paragraphStyle?: RichEditorParagraphStyle;  差异内容：paragraphStyle?: RichEditorParagraphStyle; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorTextSpanOptions；  API声明：gesture?: RichEditorGesture;  差异内容：gesture?: RichEditorGesture; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface KeyboardOptions  差异内容： declare interface KeyboardOptions | component/rich\_editor.d.ts |
| 新增API | NA | 类名：KeyboardOptions；  API声明：supportAvoidance?: boolean;  差异内容：supportAvoidance?: boolean; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface RichEditorImageSpanOptions  差异内容： declare interface RichEditorImageSpanOptions | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorImageSpanOptions；  API声明：offset?: number;  差异内容：offset?: number; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorImageSpanOptions；  API声明：imageStyle?: RichEditorImageSpanStyle;  差异内容：imageStyle?: RichEditorImageSpanStyle; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorImageSpanOptions；  API声明：gesture?: RichEditorGesture;  差异内容：gesture?: RichEditorGesture; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface RichEditorBuilderSpanOptions  差异内容： declare interface RichEditorBuilderSpanOptions | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorBuilderSpanOptions；  API声明：offset?: number;  差异内容：offset?: number; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface PlaceholderStyle  差异内容： declare interface PlaceholderStyle | component/rich\_editor.d.ts |
| 新增API | NA | 类名：PlaceholderStyle；  API声明：font?: Font;  差异内容：font?: Font; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：PlaceholderStyle；  API声明：fontColor?: ResourceColor;  差异内容：fontColor?: ResourceColor; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface RichEditorSpanStyleOptions  差异内容： declare interface RichEditorSpanStyleOptions | component/rich\_editor.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface RichEditorParagraphStyleOptions  差异内容： declare interface RichEditorParagraphStyleOptions | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorParagraphStyleOptions；  API声明：style: RichEditorParagraphStyle;  差异内容：style: RichEditorParagraphStyle; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface RichEditorUpdateTextSpanStyleOptions  差异内容： declare interface RichEditorUpdateTextSpanStyleOptions | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorUpdateTextSpanStyleOptions；  API声明：textStyle: RichEditorTextStyle;  差异内容：textStyle: RichEditorTextStyle; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface RichEditorUpdateImageSpanStyleOptions  差异内容： declare interface RichEditorUpdateImageSpanStyleOptions | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorUpdateImageSpanStyleOptions；  API声明：imageStyle: RichEditorImageSpanStyle;  差异内容：imageStyle: RichEditorImageSpanStyle; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface RichEditorUpdateSymbolSpanStyleOptions  差异内容： declare interface RichEditorUpdateSymbolSpanStyleOptions | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorUpdateSymbolSpanStyleOptions；  API声明：symbolStyle: RichEditorSymbolSpanStyle;  差异内容：symbolStyle: RichEditorSymbolSpanStyle; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface RichEditorSymbolSpanOptions  差异内容： declare interface RichEditorSymbolSpanOptions | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorSymbolSpanOptions；  API声明：offset?: number;  差异内容：offset?: number; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorSymbolSpanOptions；  API声明：style?: RichEditorSymbolSpanStyle;  差异内容：style?: RichEditorSymbolSpanStyle; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface RichEditorSelection  差异内容： declare interface RichEditorSelection | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorSelection；  API声明：selection: [  number,  number  ];  差异内容：selection: [  number,  number  ]; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorSelection；  API声明：spans: Array<RichEditorTextSpanResult | RichEditorImageSpanResult>;  差异内容：spans: Array<RichEditorTextSpanResult | RichEditorImageSpanResult>; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface RichEditorInsertValue  差异内容： declare interface RichEditorInsertValue | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorInsertValue；  API声明：insertOffset: number;  差异内容：insertOffset: number; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorInsertValue；  API声明：insertValue: string;  差异内容：insertValue: string; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorInsertValue；  API声明：previewText?: string;  差异内容：previewText?: string; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface RichEditorDeleteValue  差异内容： declare interface RichEditorDeleteValue | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorDeleteValue；  API声明：offset: number;  差异内容：offset: number; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorDeleteValue；  API声明：direction: RichEditorDeleteDirection;  差异内容：direction: RichEditorDeleteDirection; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorDeleteValue；  API声明：length: number;  差异内容：length: number; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorDeleteValue；  API声明：richEditorDeleteSpans: Array<RichEditorTextSpanResult | RichEditorImageSpanResult>;  差异内容：richEditorDeleteSpans: Array<RichEditorTextSpanResult | RichEditorImageSpanResult>; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface RichEditorChangeValue  差异内容： declare interface RichEditorChangeValue | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorChangeValue；  API声明：rangeBefore: TextRange;  差异内容：rangeBefore: TextRange; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorChangeValue；  API声明：replacedSpans: Array<RichEditorTextSpanResult>;  差异内容：replacedSpans: Array<RichEditorTextSpanResult>; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorChangeValue；  API声明：replacedImageSpans: Array<RichEditorImageSpanResult>;  差异内容：replacedImageSpans: Array<RichEditorImageSpanResult>; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorChangeValue；  API声明：replacedSymbolSpans: Array<RichEditorTextSpanResult>;  差异内容：replacedSymbolSpans: Array<RichEditorTextSpanResult>; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface RichEditorOptions  差异内容： declare interface RichEditorOptions | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorOptions；  API声明：controller: RichEditorController;  差异内容：controller: RichEditorController; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface RichEditorStyledStringOptions  差异内容： declare interface RichEditorStyledStringOptions | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorStyledStringOptions；  API声明：controller: RichEditorStyledStringController;  差异内容：controller: RichEditorStyledStringController; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface SelectionMenuOptions  差异内容： declare interface SelectionMenuOptions | component/rich\_editor.d.ts |
| 新增API | NA | 类名：SelectionMenuOptions；  API声明：onAppear?: MenuOnAppearCallback;  差异内容：onAppear?: MenuOnAppearCallback; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：SelectionMenuOptions；  API声明：onDisappear?: () => void;  差异内容：onDisappear?: () => void; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class RichEditorBaseController  差异内容： declare class RichEditorBaseController | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorBaseController；  API声明：getCaretOffset(): number;  差异内容：getCaretOffset(): number; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorBaseController；  API声明：setCaretOffset(offset: number): boolean;  差异内容：setCaretOffset(offset: number): boolean; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorBaseController；  API声明：closeSelectionMenu(): void;  差异内容：closeSelectionMenu(): void; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorBaseController；  API声明：getTypingStyle(): RichEditorTextStyle;  差异内容：getTypingStyle(): RichEditorTextStyle; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorBaseController；  API声明：setTypingStyle(value: RichEditorTextStyle): void;  差异内容：setTypingStyle(value: RichEditorTextStyle): void; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorBaseController；  API声明：setSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void;  差异内容：setSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorBaseController；  API声明：isEditing(): boolean;  差异内容：isEditing(): boolean; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorBaseController；  API声明：stopEditing(): void;  差异内容：stopEditing(): void; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class RichEditorController  差异内容： declare class RichEditorController | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorController；  API声明：addTextSpan(value: string, options?: RichEditorTextSpanOptions): number;  差异内容：addTextSpan(value: string, options?: RichEditorTextSpanOptions): number; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorController；  API声明：addImageSpan(value: PixelMap | ResourceStr, options?: RichEditorImageSpanOptions): number;  差异内容：addImageSpan(value: PixelMap | ResourceStr, options?: RichEditorImageSpanOptions): number; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorController；  API声明：addBuilderSpan(value: CustomBuilder, options?: RichEditorBuilderSpanOptions): number;  差异内容：addBuilderSpan(value: CustomBuilder, options?: RichEditorBuilderSpanOptions): number; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorController；  API声明：addSymbolSpan(value: Resource, options?: RichEditorSymbolSpanOptions): number;  差异内容：addSymbolSpan(value: Resource, options?: RichEditorSymbolSpanOptions): number; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorController；  API声明：updateSpanStyle(value: RichEditorUpdateTextSpanStyleOptions | RichEditorUpdateImageSpanStyleOptions | RichEditorUpdateSymbolSpanStyleOptions): void;  差异内容：updateSpanStyle(value: RichEditorUpdateTextSpanStyleOptions | RichEditorUpdateImageSpanStyleOptions | RichEditorUpdateSymbolSpanStyleOptions): void; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorController；  API声明：updateParagraphStyle(value: RichEditorParagraphStyleOptions): void;  差异内容：updateParagraphStyle(value: RichEditorParagraphStyleOptions): void; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorController；  API声明：deleteSpans(value?: RichEditorRange): void;  差异内容：deleteSpans(value?: RichEditorRange): void; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorController；  API声明：getSpans(value?: RichEditorRange): Array<RichEditorImageSpanResult | RichEditorTextSpanResult>;  差异内容：getSpans(value?: RichEditorRange): Array<RichEditorImageSpanResult | RichEditorTextSpanResult>; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorController；  API声明：getParagraphs(value?: RichEditorRange): Array<RichEditorParagraphResult>;  差异内容：getParagraphs(value?: RichEditorRange): Array<RichEditorParagraphResult>; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorController；  API声明：getSelection(): RichEditorSelection;  差异内容：getSelection(): RichEditorSelection; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class RichEditorStyledStringController  差异内容： declare class RichEditorStyledStringController | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorStyledStringController；  API声明：setStyledString(styledString: StyledString): void;  差异内容：setStyledString(styledString: StyledString): void; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorStyledStringController；  API声明：getStyledString(): MutableStyledString;  差异内容：getStyledString(): MutableStyledString; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorStyledStringController；  API声明：getSelection(): RichEditorRange;  差异内容：getSelection(): RichEditorRange; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorStyledStringController；  API声明：onContentChanged(listener: StyledStringChangedListener): void;  差异内容：onContentChanged(listener: StyledStringChangedListener): void; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class RichEditorAttribute  差异内容： declare class RichEditorAttribute | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorAttribute；  API声明：onReady(callback: () => void): RichEditorAttribute;  差异内容：onReady(callback: () => void): RichEditorAttribute; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorAttribute；  API声明：onSelect(callback: (value: RichEditorSelection) => void): RichEditorAttribute;  差异内容：onSelect(callback: (value: RichEditorSelection) => void): RichEditorAttribute; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorAttribute；  API声明：onSelectionChange(callback: (value: RichEditorRange) => void): RichEditorAttribute;  差异内容：onSelectionChange(callback: (value: RichEditorRange) => void): RichEditorAttribute; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorAttribute；  API声明：aboutToIMEInput(callback: (value: RichEditorInsertValue) => boolean): RichEditorAttribute;  差异内容：aboutToIMEInput(callback: (value: RichEditorInsertValue) => boolean): RichEditorAttribute; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorAttribute；  API声明：onIMEInputComplete(callback: (value: RichEditorTextSpanResult) => void): RichEditorAttribute;  差异内容：onIMEInputComplete(callback: (value: RichEditorTextSpanResult) => void): RichEditorAttribute; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorAttribute；  API声明：aboutToDelete(callback: (value: RichEditorDeleteValue) => boolean): RichEditorAttribute;  差异内容：aboutToDelete(callback: (value: RichEditorDeleteValue) => boolean): RichEditorAttribute; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorAttribute；  API声明：onDeleteComplete(callback: () => void): RichEditorAttribute;  差异内容：onDeleteComplete(callback: () => void): RichEditorAttribute; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorAttribute；  API声明：copyOptions(value: CopyOptions): RichEditorAttribute;  差异内容：copyOptions(value: CopyOptions): RichEditorAttribute; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorAttribute；  API声明：bindSelectionMenu(spanType: RichEditorSpanType, content: CustomBuilder, responseType: ResponseType | RichEditorResponseType, options?: SelectionMenuOptions): RichEditorAttribute;  差异内容：bindSelectionMenu(spanType: RichEditorSpanType, content: CustomBuilder, responseType: ResponseType | RichEditorResponseType, options?: SelectionMenuOptions): RichEditorAttribute; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorAttribute；  API声明：customKeyboard(value: CustomBuilder, options?: KeyboardOptions): RichEditorAttribute;  差异内容：customKeyboard(value: CustomBuilder, options?: KeyboardOptions): RichEditorAttribute; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorAttribute；  API声明：onPaste(callback: (event?: PasteEvent) => void): RichEditorAttribute;  差异内容：onPaste(callback: (event?: PasteEvent) => void): RichEditorAttribute; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorAttribute；  API声明：enableDataDetector(enable: boolean): RichEditorAttribute;  差异内容：enableDataDetector(enable: boolean): RichEditorAttribute; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorAttribute；  API声明：enablePreviewText(enable: boolean): RichEditorAttribute;  差异内容：enablePreviewText(enable: boolean): RichEditorAttribute; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorAttribute；  API声明：dataDetectorConfig(config: TextDataDetectorConfig): RichEditorAttribute;  差异内容：dataDetectorConfig(config: TextDataDetectorConfig): RichEditorAttribute; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorAttribute；  API声明：placeholder(value: ResourceStr, style?: PlaceholderStyle): RichEditorAttribute;  差异内容：placeholder(value: ResourceStr, style?: PlaceholderStyle): RichEditorAttribute; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorAttribute；  API声明：caretColor(value: ResourceColor): RichEditorAttribute;  差异内容：caretColor(value: ResourceColor): RichEditorAttribute; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorAttribute；  API声明：selectedBackgroundColor(value: ResourceColor): RichEditorAttribute;  差异内容：selectedBackgroundColor(value: ResourceColor): RichEditorAttribute; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorAttribute；  API声明：onEditingChange(callback: Callback<boolean>): RichEditorAttribute;  差异内容：onEditingChange(callback: Callback<boolean>): RichEditorAttribute; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorAttribute；  API声明：enterKeyType(value: EnterKeyType): RichEditorAttribute;  差异内容：enterKeyType(value: EnterKeyType): RichEditorAttribute; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorAttribute；  API声明：onSubmit(callback: SubmitCallback): RichEditorAttribute;  差异内容：onSubmit(callback: SubmitCallback): RichEditorAttribute; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorAttribute；  API声明：onWillChange(callback: Callback<RichEditorChangeValue, boolean>): RichEditorAttribute;  差异内容：onWillChange(callback: Callback<RichEditorChangeValue, boolean>): RichEditorAttribute; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorAttribute；  API声明：onDidChange(callback: OnDidChangeCallback): RichEditorAttribute;  差异内容：onDidChange(callback: OnDidChangeCallback): RichEditorAttribute; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorAttribute；  API声明：onCut(callback: Callback<CutEvent>): RichEditorAttribute;  差异内容：onCut(callback: Callback<CutEvent>): RichEditorAttribute; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：RichEditorAttribute；  API声明：onCopy(callback: Callback<CopyEvent>): RichEditorAttribute;  差异内容：onCopy(callback: Callback<CopyEvent>): RichEditorAttribute; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface CutEvent  差异内容： declare interface CutEvent | component/rich\_editor.d.ts |
| 新增API | NA | 类名：CutEvent；  API声明：preventDefault?: Callback<void>;  差异内容：preventDefault?: Callback<void>; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface CopyEvent  差异内容： declare interface CopyEvent | component/rich\_editor.d.ts |
| 新增API | NA | 类名：CopyEvent；  API声明：preventDefault?: Callback<void>;  差异内容：preventDefault?: Callback<void>; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type SubmitCallback = (enterKey: EnterKeyType, event: SubmitEvent) => void;  差异内容：declare type SubmitCallback = (enterKey: EnterKeyType, event: SubmitEvent) => void; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type MenuOnAppearCallback = (start: number, end: number) => void;  差异内容：declare type MenuOnAppearCallback = (start: number, end: number) => void; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：global；  API声明： interface RichEditorInterface  差异内容： interface RichEditorInterface | component/rich\_editor.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const RichEditorInstance: RichEditorAttribute;  差异内容：declare const RichEditorInstance: RichEditorAttribute; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const RichEditor: RichEditorInterface;  差异内容：declare const RichEditor: RichEditorInterface; | component/rich\_editor.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum SaveIconStyle  差异内容： declare enum SaveIconStyle | component/save\_button.d.ts |
| 新增API | NA | 类名：SaveIconStyle；  API声明：FULL\_FILLED = 0  差异内容：FULL\_FILLED = 0 | component/save\_button.d.ts |
| 新增API | NA | 类名：SaveIconStyle；  API声明：LINES = 1  差异内容：LINES = 1 | component/save\_button.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum SaveDescription  差异内容： declare enum SaveDescription | component/save\_button.d.ts |
| 新增API | NA | 类名：SaveDescription；  API声明：DOWNLOAD = 0  差异内容：DOWNLOAD = 0 | component/save\_button.d.ts |
| 新增API | NA | 类名：SaveDescription；  API声明：DOWNLOAD\_FILE = 1  差异内容：DOWNLOAD\_FILE = 1 | component/save\_button.d.ts |
| 新增API | NA | 类名：SaveDescription；  API声明：SAVE = 2  差异内容：SAVE = 2 | component/save\_button.d.ts |
| 新增API | NA | 类名：SaveDescription；  API声明：SAVE\_IMAGE = 3  差异内容：SAVE\_IMAGE = 3 | component/save\_button.d.ts |
| 新增API | NA | 类名：SaveDescription；  API声明：SAVE\_FILE = 4  差异内容：SAVE\_FILE = 4 | component/save\_button.d.ts |
| 新增API | NA | 类名：SaveDescription；  API声明：DOWNLOAD\_AND\_SHARE = 5  差异内容：DOWNLOAD\_AND\_SHARE = 5 | component/save\_button.d.ts |
| 新增API | NA | 类名：SaveDescription；  API声明：RECEIVE = 6  差异内容：RECEIVE = 6 | component/save\_button.d.ts |
| 新增API | NA | 类名：SaveDescription；  API声明：CONTINUE\_TO\_RECEIVE = 7  差异内容：CONTINUE\_TO\_RECEIVE = 7 | component/save\_button.d.ts |
| 新增API | NA | 类名：SaveDescription；  API声明：SAVE\_TO\_GALLERY = 8  差异内容：SAVE\_TO\_GALLERY = 8 | component/save\_button.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface SaveButtonOptions  差异内容： declare interface SaveButtonOptions | component/save\_button.d.ts |
| 新增API | NA | 类名：SaveButtonOptions；  API声明：icon?: SaveIconStyle;  差异内容：icon?: SaveIconStyle; | component/save\_button.d.ts |
| 新增API | NA | 类名：SaveButtonOptions；  API声明：text?: SaveDescription;  差异内容：text?: SaveDescription; | component/save\_button.d.ts |
| 新增API | NA | 类名：SaveButtonOptions；  API声明：buttonType?: ButtonType;  差异内容：buttonType?: ButtonType; | component/save\_button.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum SaveButtonOnClickResult  差异内容： declare enum SaveButtonOnClickResult | component/save\_button.d.ts |
| 新增API | NA | 类名：SaveButtonOnClickResult；  API声明：SUCCESS = 0  差异内容：SUCCESS = 0 | component/save\_button.d.ts |
| 新增API | NA | 类名：SaveButtonOnClickResult；  API声明：TEMPORARY\_AUTHORIZATION\_FAILED = 1  差异内容：TEMPORARY\_AUTHORIZATION\_FAILED = 1 | component/save\_button.d.ts |
| 新增API | NA | 类名：global；  API声明： interface SaveButtonInterface  差异内容： interface SaveButtonInterface | component/save\_button.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class SaveButtonAttribute  差异内容： declare class SaveButtonAttribute | component/save\_button.d.ts |
| 新增API | NA | 类名：SaveButtonAttribute；  API声明：onClick(event: (event: ClickEvent, result: SaveButtonOnClickResult) => void): SaveButtonAttribute;  差异内容：onClick(event: (event: ClickEvent, result: SaveButtonOnClickResult) => void): SaveButtonAttribute; | component/save\_button.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const SaveButton: SaveButtonInterface;  差异内容：declare const SaveButton: SaveButtonInterface; | component/save\_button.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const SaveButtonInstance: SaveButtonAttribute;  差异内容：declare const SaveButtonInstance: SaveButtonAttribute; | component/save\_button.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum SecurityComponentLayoutDirection  差异内容： declare enum SecurityComponentLayoutDirection | component/security\_component.d.ts |
| 新增API | NA | 类名：SecurityComponentLayoutDirection；  API声明：HORIZONTAL = 0  差异内容：HORIZONTAL = 0 | component/security\_component.d.ts |
| 新增API | NA | 类名：SecurityComponentLayoutDirection；  API声明：VERTICAL = 1  差异内容：VERTICAL = 1 | component/security\_component.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class SecurityComponentMethod  差异内容： declare class SecurityComponentMethod | component/security\_component.d.ts |
| 新增API | NA | 类名：SecurityComponentMethod；  API声明：iconSize(value: Dimension): T;  差异内容：iconSize(value: Dimension): T; | component/security\_component.d.ts |
| 新增API | NA | 类名：SecurityComponentMethod；  API声明：layoutDirection(value: SecurityComponentLayoutDirection): T;  差异内容：layoutDirection(value: SecurityComponentLayoutDirection): T; | component/security\_component.d.ts |
| 新增API | NA | 类名：SecurityComponentMethod；  API声明：position(value: Position): T;  差异内容：position(value: Position): T; | component/security\_component.d.ts |
| 新增API | NA | 类名：SecurityComponentMethod；  API声明：markAnchor(value: Position): T;  差异内容：markAnchor(value: Position): T; | component/security\_component.d.ts |
| 新增API | NA | 类名：SecurityComponentMethod；  API声明：offset(value: Position): T;  差异内容：offset(value: Position): T; | component/security\_component.d.ts |
| 新增API | NA | 类名：SecurityComponentMethod；  API声明：fontSize(value: Dimension): T;  差异内容：fontSize(value: Dimension): T; | component/security\_component.d.ts |
| 新增API | NA | 类名：SecurityComponentMethod；  API声明：fontStyle(value: FontStyle): T;  差异内容：fontStyle(value: FontStyle): T; | component/security\_component.d.ts |
| 新增API | NA | 类名：SecurityComponentMethod；  API声明：fontWeight(value: number | FontWeight | string): T;  差异内容：fontWeight(value: number | FontWeight | string): T; | component/security\_component.d.ts |
| 新增API | NA | 类名：SecurityComponentMethod；  API声明：fontFamily(value: string | Resource): T;  差异内容：fontFamily(value: string | Resource): T; | component/security\_component.d.ts |
| 新增API | NA | 类名：SecurityComponentMethod；  API声明：fontColor(value: ResourceColor): T;  差异内容：fontColor(value: ResourceColor): T; | component/security\_component.d.ts |
| 新增API | NA | 类名：SecurityComponentMethod；  API声明：iconColor(value: ResourceColor): T;  差异内容：iconColor(value: ResourceColor): T; | component/security\_component.d.ts |
| 新增API | NA | 类名：SecurityComponentMethod；  API声明：backgroundColor(value: ResourceColor): T;  差异内容：backgroundColor(value: ResourceColor): T; | component/security\_component.d.ts |
| 新增API | NA | 类名：SecurityComponentMethod；  API声明：borderStyle(value: BorderStyle): T;  差异内容：borderStyle(value: BorderStyle): T; | component/security\_component.d.ts |
| 新增API | NA | 类名：SecurityComponentMethod；  API声明：borderWidth(value: Dimension): T;  差异内容：borderWidth(value: Dimension): T; | component/security\_component.d.ts |
| 新增API | NA | 类名：SecurityComponentMethod；  API声明：borderColor(value: ResourceColor): T;  差异内容：borderColor(value: ResourceColor): T; | component/security\_component.d.ts |
| 新增API | NA | 类名：SecurityComponentMethod；  API声明：borderRadius(value: Dimension): T;  差异内容：borderRadius(value: Dimension): T; | component/security\_component.d.ts |
| 新增API | NA | 类名：SecurityComponentMethod；  API声明：padding(value: Padding | Dimension): T;  差异内容：padding(value: Padding | Dimension): T; | component/security\_component.d.ts |
| 新增API | NA | 类名：SecurityComponentMethod；  API声明：textIconSpace(value: Dimension): T;  差异内容：textIconSpace(value: Dimension): T; | component/security\_component.d.ts |
| 新增API | NA | 类名：SecurityComponentMethod；  API声明：width(value: Length): T;  差异内容：width(value: Length): T; | component/security\_component.d.ts |
| 新增API | NA | 类名：SecurityComponentMethod；  API声明：height(value: Length): T;  差异内容：height(value: Length): T; | component/security\_component.d.ts |
| 新增API | NA | 类名：SecurityComponentMethod；  API声明：size(value: SizeOptions): T;  差异内容：size(value: SizeOptions): T; | component/security\_component.d.ts |
| 新增API | NA | 类名：SecurityComponentMethod；  API声明：constraintSize(value: ConstraintSizeOptions): T;  差异内容：constraintSize(value: ConstraintSizeOptions): T; | component/security\_component.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class StyledString  差异内容： declare class StyledString | component/styled\_string.d.ts |
| 新增API | NA | 类名：StyledString；  API声明：readonly length: number;  差异内容：readonly length: number; | component/styled\_string.d.ts |
| 新增API | NA | 类名：StyledString；  API声明：getString(): string;  差异内容：getString(): string; | component/styled\_string.d.ts |
| 新增API | NA | 类名：StyledString；  API声明：getStyles(start: number, length: number, styledKey?: StyledStringKey): Array<SpanStyle>;  差异内容：getStyles(start: number, length: number, styledKey?: StyledStringKey): Array<SpanStyle>; | component/styled\_string.d.ts |
| 新增API | NA | 类名：StyledString；  API声明：equals(other: StyledString): boolean;  差异内容：equals(other: StyledString): boolean; | component/styled\_string.d.ts |
| 新增API | NA | 类名：StyledString；  API声明：subStyledString(start: number, length?: number): StyledString;  差异内容：subStyledString(start: number, length?: number): StyledString; | component/styled\_string.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface StyleOptions  差异内容： declare interface StyleOptions | component/styled\_string.d.ts |
| 新增API | NA | 类名：StyleOptions；  API声明：start?: number;  差异内容：start?: number; | component/styled\_string.d.ts |
| 新增API | NA | 类名：StyleOptions；  API声明：length?: number;  差异内容：length?: number; | component/styled\_string.d.ts |
| 新增API | NA | 类名：StyleOptions；  API声明：styledKey: StyledStringKey;  差异内容：styledKey: StyledStringKey; | component/styled\_string.d.ts |
| 新增API | NA | 类名：StyleOptions；  API声明：styledValue: StyledStringValue;  差异内容：styledValue: StyledStringValue; | component/styled\_string.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface SpanStyle  差异内容： declare interface SpanStyle | component/styled\_string.d.ts |
| 新增API | NA | 类名：SpanStyle；  API声明：start: number;  差异内容：start: number; | component/styled\_string.d.ts |
| 新增API | NA | 类名：SpanStyle；  API声明：length: number;  差异内容：length: number; | component/styled\_string.d.ts |
| 新增API | NA | 类名：SpanStyle；  API声明：styledKey: StyledStringKey;  差异内容：styledKey: StyledStringKey; | component/styled\_string.d.ts |
| 新增API | NA | 类名：SpanStyle；  API声明：styledValue: StyledStringValue;  差异内容：styledValue: StyledStringValue; | component/styled\_string.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class TextStyle  差异内容： declare class TextStyle | component/styled\_string.d.ts |
| 新增API | NA | 类名：TextStyle；  API声明：readonly fontColor?: ResourceColor;  差异内容：readonly fontColor?: ResourceColor; | component/styled\_string.d.ts |
| 新增API | NA | 类名：TextStyle；  API声明：readonly fontFamily?: string;  差异内容：readonly fontFamily?: string; | component/styled\_string.d.ts |
| 新增API | NA | 类名：TextStyle；  API声明：readonly fontSize?: number;  差异内容：readonly fontSize?: number; | component/styled\_string.d.ts |
| 新增API | NA | 类名：TextStyle；  API声明：readonly fontWeight?: number;  差异内容：readonly fontWeight?: number; | component/styled\_string.d.ts |
| 新增API | NA | 类名：TextStyle；  API声明：readonly fontStyle?: FontStyle;  差异内容：readonly fontStyle?: FontStyle; | component/styled\_string.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface TextStyleInterface  差异内容： declare interface TextStyleInterface | component/styled\_string.d.ts |
| 新增API | NA | 类名：TextStyleInterface；  API声明：fontColor?: ResourceColor;  差异内容：fontColor?: ResourceColor; | component/styled\_string.d.ts |
| 新增API | NA | 类名：TextStyleInterface；  API声明：fontFamily?: ResourceStr;  差异内容：fontFamily?: ResourceStr; | component/styled\_string.d.ts |
| 新增API | NA | 类名：TextStyleInterface；  API声明：fontSize?: LengthMetrics;  差异内容：fontSize?: LengthMetrics; | component/styled\_string.d.ts |
| 新增API | NA | 类名：TextStyleInterface；  API声明：fontWeight?: number | FontWeight | string;  差异内容：fontWeight?: number | FontWeight | string; | component/styled\_string.d.ts |
| 新增API | NA | 类名：TextStyleInterface；  API声明：fontStyle?: FontStyle;  差异内容：fontStyle?: FontStyle; | component/styled\_string.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class DecorationStyle  差异内容： declare class DecorationStyle | component/styled\_string.d.ts |
| 新增API | NA | 类名：DecorationStyle；  API声明：readonly type: TextDecorationType;  差异内容：readonly type: TextDecorationType; | component/styled\_string.d.ts |
| 新增API | NA | 类名：DecorationStyle；  API声明：readonly color?: ResourceColor;  差异内容：readonly color?: ResourceColor; | component/styled\_string.d.ts |
| 新增API | NA | 类名：DecorationStyle；  API声明：readonly style?: TextDecorationStyle;  差异内容：readonly style?: TextDecorationStyle; | component/styled\_string.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface DecorationStyleInterface  差异内容： declare interface DecorationStyleInterface | component/styled\_string.d.ts |
| 新增API | NA | 类名：DecorationStyleInterface；  API声明：type: TextDecorationType;  差异内容：type: TextDecorationType; | component/styled\_string.d.ts |
| 新增API | NA | 类名：DecorationStyleInterface；  API声明：color?: ResourceColor;  差异内容：color?: ResourceColor; | component/styled\_string.d.ts |
| 新增API | NA | 类名：DecorationStyleInterface；  API声明：style?: TextDecorationStyle;  差异内容：style?: TextDecorationStyle; | component/styled\_string.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class BaselineOffsetStyle  差异内容： declare class BaselineOffsetStyle | component/styled\_string.d.ts |
| 新增API | NA | 类名：BaselineOffsetStyle；  API声明：readonly baselineOffset: number;  差异内容：readonly baselineOffset: number; | component/styled\_string.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class LetterSpacingStyle  差异内容： declare class LetterSpacingStyle | component/styled\_string.d.ts |
| 新增API | NA | 类名：LetterSpacingStyle；  API声明：readonly letterSpacing: number;  差异内容：readonly letterSpacing: number; | component/styled\_string.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class TextShadowStyle  差异内容： declare class TextShadowStyle | component/styled\_string.d.ts |
| 新增API | NA | 类名：TextShadowStyle；  API声明：readonly textShadow: Array<ShadowOptions>;  差异内容：readonly textShadow: Array<ShadowOptions>; | component/styled\_string.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class GestureStyle  差异内容： declare class GestureStyle | component/styled\_string.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface GestureStyleInterface  差异内容： declare interface GestureStyleInterface | component/styled\_string.d.ts |
| 新增API | NA | 类名：GestureStyleInterface；  API声明：onClick?: Callback<ClickEvent>;  差异内容：onClick?: Callback<ClickEvent>; | component/styled\_string.d.ts |
| 新增API | NA | 类名：GestureStyleInterface；  API声明：onLongPress?: Callback<GestureEvent>;  差异内容：onLongPress?: Callback<GestureEvent>; | component/styled\_string.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class ParagraphStyle  差异内容： declare class ParagraphStyle | component/styled\_string.d.ts |
| 新增API | NA | 类名：ParagraphStyle；  API声明：readonly textAlign?: TextAlign;  差异内容：readonly textAlign?: TextAlign; | component/styled\_string.d.ts |
| 新增API | NA | 类名：ParagraphStyle；  API声明：readonly textIndent?: number;  差异内容：readonly textIndent?: number; | component/styled\_string.d.ts |
| 新增API | NA | 类名：ParagraphStyle；  API声明：readonly maxLines?: number;  差异内容：readonly maxLines?: number; | component/styled\_string.d.ts |
| 新增API | NA | 类名：ParagraphStyle；  API声明：readonly overflow?: TextOverflow;  差异内容：readonly overflow?: TextOverflow; | component/styled\_string.d.ts |
| 新增API | NA | 类名：ParagraphStyle；  API声明：readonly wordBreak?: WordBreak;  差异内容：readonly wordBreak?: WordBreak; | component/styled\_string.d.ts |
| 新增API | NA | 类名：ParagraphStyle；  API声明：readonly leadingMargin?: number | LeadingMarginPlaceholder;  差异内容：readonly leadingMargin?: number | LeadingMarginPlaceholder; | component/styled\_string.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface ParagraphStyleInterface  差异内容： declare interface ParagraphStyleInterface | component/styled\_string.d.ts |
| 新增API | NA | 类名：ParagraphStyleInterface；  API声明：textAlign?: TextAlign;  差异内容：textAlign?: TextAlign; | component/styled\_string.d.ts |
| 新增API | NA | 类名：ParagraphStyleInterface；  API声明：textIndent?: LengthMetrics;  差异内容：textIndent?: LengthMetrics; | component/styled\_string.d.ts |
| 新增API | NA | 类名：ParagraphStyleInterface；  API声明：maxLines?: number;  差异内容：maxLines?: number; | component/styled\_string.d.ts |
| 新增API | NA | 类名：ParagraphStyleInterface；  API声明：overflow?: TextOverflow;  差异内容：overflow?: TextOverflow; | component/styled\_string.d.ts |
| 新增API | NA | 类名：ParagraphStyleInterface；  API声明：wordBreak?: WordBreak;  差异内容：wordBreak?: WordBreak; | component/styled\_string.d.ts |
| 新增API | NA | 类名：ParagraphStyleInterface；  API声明：leadingMargin?: LengthMetrics | LeadingMarginPlaceholder;  差异内容：leadingMargin?: LengthMetrics | LeadingMarginPlaceholder; | component/styled\_string.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class LineHeightStyle  差异内容： declare class LineHeightStyle | component/styled\_string.d.ts |
| 新增API | NA | 类名：LineHeightStyle；  API声明：readonly lineHeight: number;  差异内容：readonly lineHeight: number; | component/styled\_string.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type StyledStringValue = TextStyle | DecorationStyle | BaselineOffsetStyle | LetterSpacingStyle | TextShadowStyle | GestureStyle | ImageAttachment | ParagraphStyle | LineHeightStyle | CustomSpan;  差异内容：declare type StyledStringValue = TextStyle | DecorationStyle | BaselineOffsetStyle | LetterSpacingStyle | TextShadowStyle | GestureStyle | ImageAttachment | ParagraphStyle | LineHeightStyle | CustomSpan; | component/styled\_string.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class MutableStyledString  差异内容： declare class MutableStyledString | component/styled\_string.d.ts |
| 新增API | NA | 类名：MutableStyledString；  API声明：replaceString(start: number, length: number, other: string): void;  差异内容：replaceString(start: number, length: number, other: string): void; | component/styled\_string.d.ts |
| 新增API | NA | 类名：MutableStyledString；  API声明：insertString(start: number, other: string): void;  差异内容：insertString(start: number, other: string): void; | component/styled\_string.d.ts |
| 新增API | NA | 类名：MutableStyledString；  API声明：removeString(start: number, length: number): void;  差异内容：removeString(start: number, length: number): void; | component/styled\_string.d.ts |
| 新增API | NA | 类名：MutableStyledString；  API声明：replaceStyle(spanStyle: SpanStyle): void;  差异内容：replaceStyle(spanStyle: SpanStyle): void; | component/styled\_string.d.ts |
| 新增API | NA | 类名：MutableStyledString；  API声明：setStyle(spanStyle: SpanStyle): void;  差异内容：setStyle(spanStyle: SpanStyle): void; | component/styled\_string.d.ts |
| 新增API | NA | 类名：MutableStyledString；  API声明：removeStyle(start: number, length: number, styledKey: StyledStringKey): void;  差异内容：removeStyle(start: number, length: number, styledKey: StyledStringKey): void; | component/styled\_string.d.ts |
| 新增API | NA | 类名：MutableStyledString；  API声明：removeStyles(start: number, length: number): void;  差异内容：removeStyles(start: number, length: number): void; | component/styled\_string.d.ts |
| 新增API | NA | 类名：MutableStyledString；  API声明：clearStyles(): void;  差异内容：clearStyles(): void; | component/styled\_string.d.ts |
| 新增API | NA | 类名：MutableStyledString；  API声明：replaceStyledString(start: number, length: number, other: StyledString): void;  差异内容：replaceStyledString(start: number, length: number, other: StyledString): void; | component/styled\_string.d.ts |
| 新增API | NA | 类名：MutableStyledString；  API声明：insertStyledString(start: number, other: StyledString): void;  差异内容：insertStyledString(start: number, other: StyledString): void; | component/styled\_string.d.ts |
| 新增API | NA | 类名：MutableStyledString；  API声明：appendStyledString(other: StyledString): void;  差异内容：appendStyledString(other: StyledString): void; | component/styled\_string.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum StyledStringKey  差异内容： declare enum StyledStringKey | component/styled\_string.d.ts |
| 新增API | NA | 类名：StyledStringKey；  API声明：FONT = 0  差异内容：FONT = 0 | component/styled\_string.d.ts |
| 新增API | NA | 类名：StyledStringKey；  API声明：DECORATION = 1  差异内容：DECORATION = 1 | component/styled\_string.d.ts |
| 新增API | NA | 类名：StyledStringKey；  API声明：BASELINE\_OFFSET = 2  差异内容：BASELINE\_OFFSET = 2 | component/styled\_string.d.ts |
| 新增API | NA | 类名：StyledStringKey；  API声明：LETTER\_SPACING = 3  差异内容：LETTER\_SPACING = 3 | component/styled\_string.d.ts |
| 新增API | NA | 类名：StyledStringKey；  API声明：TEXT\_SHADOW = 4  差异内容：TEXT\_SHADOW = 4 | component/styled\_string.d.ts |
| 新增API | NA | 类名：StyledStringKey；  API声明：LINE\_HEIGHT = 5  差异内容：LINE\_HEIGHT = 5 | component/styled\_string.d.ts |
| 新增API | NA | 类名：StyledStringKey；  API声明：GESTURE = 100  差异内容：GESTURE = 100 | component/styled\_string.d.ts |
| 新增API | NA | 类名：StyledStringKey；  API声明：PARAGRAPH\_STYLE = 200  差异内容：PARAGRAPH\_STYLE = 200 | component/styled\_string.d.ts |
| 新增API | NA | 类名：StyledStringKey；  API声明：IMAGE = 300  差异内容：IMAGE = 300 | component/styled\_string.d.ts |
| 新增API | NA | 类名：StyledStringKey；  API声明：CUSTOM\_SPAN = 400  差异内容：CUSTOM\_SPAN = 400 | component/styled\_string.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class ImageAttachment  差异内容： declare class ImageAttachment | component/styled\_string.d.ts |
| 新增API | NA | 类名：ImageAttachment；  API声明：readonly value: PixelMap;  差异内容：readonly value: PixelMap; | component/styled\_string.d.ts |
| 新增API | NA | 类名：ImageAttachment；  API声明：readonly size?: SizeOptions;  差异内容：readonly size?: SizeOptions; | component/styled\_string.d.ts |
| 新增API | NA | 类名：ImageAttachment；  API声明：readonly verticalAlign?: ImageSpanAlignment;  差异内容：readonly verticalAlign?: ImageSpanAlignment; | component/styled\_string.d.ts |
| 新增API | NA | 类名：ImageAttachment；  API声明：readonly objectFit?: ImageFit;  差异内容：readonly objectFit?: ImageFit; | component/styled\_string.d.ts |
| 新增API | NA | 类名：ImageAttachment；  API声明：readonly layoutStyle?: ImageAttachmentLayoutStyle;  差异内容：readonly layoutStyle?: ImageAttachmentLayoutStyle; | component/styled\_string.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface ImageAttachmentInterface  差异内容： declare interface ImageAttachmentInterface | component/styled\_string.d.ts |
| 新增API | NA | 类名：ImageAttachmentInterface；  API声明：value: PixelMap;  差异内容：value: PixelMap; | component/styled\_string.d.ts |
| 新增API | NA | 类名：ImageAttachmentInterface；  API声明：size?: SizeOptions;  差异内容：size?: SizeOptions; | component/styled\_string.d.ts |
| 新增API | NA | 类名：ImageAttachmentInterface；  API声明：verticalAlign?: ImageSpanAlignment;  差异内容：verticalAlign?: ImageSpanAlignment; | component/styled\_string.d.ts |
| 新增API | NA | 类名：ImageAttachmentInterface；  API声明：objectFit?: ImageFit;  差异内容：objectFit?: ImageFit; | component/styled\_string.d.ts |
| 新增API | NA | 类名：ImageAttachmentInterface；  API声明：layoutStyle?: ImageAttachmentLayoutStyle;  差异内容：layoutStyle?: ImageAttachmentLayoutStyle; | component/styled\_string.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface ImageAttachmentLayoutStyle  差异内容： declare interface ImageAttachmentLayoutStyle | component/styled\_string.d.ts |
| 新增API | NA | 类名：ImageAttachmentLayoutStyle；  API声明：margin?: LengthMetrics | Margin;  差异内容：margin?: LengthMetrics | Margin; | component/styled\_string.d.ts |
| 新增API | NA | 类名：ImageAttachmentLayoutStyle；  API声明：padding?: LengthMetrics | Padding;  差异内容：padding?: LengthMetrics | Padding; | component/styled\_string.d.ts |
| 新增API | NA | 类名：ImageAttachmentLayoutStyle；  API声明：borderRadius?: LengthMetrics | BorderRadiuses;  差异内容：borderRadius?: LengthMetrics | BorderRadiuses; | component/styled\_string.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface CustomSpanMetrics  差异内容： declare interface CustomSpanMetrics | component/styled\_string.d.ts |
| 新增API | NA | 类名：CustomSpanMetrics；  API声明：width: number;  差异内容：width: number; | component/styled\_string.d.ts |
| 新增API | NA | 类名：CustomSpanMetrics；  API声明：height?: number;  差异内容：height?: number; | component/styled\_string.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface CustomSpanDrawInfo  差异内容： declare interface CustomSpanDrawInfo | component/styled\_string.d.ts |
| 新增API | NA | 类名：CustomSpanDrawInfo；  API声明：x: number;  差异内容：x: number; | component/styled\_string.d.ts |
| 新增API | NA | 类名：CustomSpanDrawInfo；  API声明：lineTop: number;  差异内容：lineTop: number; | component/styled\_string.d.ts |
| 新增API | NA | 类名：CustomSpanDrawInfo；  API声明：lineBottom: number;  差异内容：lineBottom: number; | component/styled\_string.d.ts |
| 新增API | NA | 类名：CustomSpanDrawInfo；  API声明：baseline: number;  差异内容：baseline: number; | component/styled\_string.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface CustomSpanMeasureInfo  差异内容： declare interface CustomSpanMeasureInfo | component/styled\_string.d.ts |
| 新增API | NA | 类名：CustomSpanMeasureInfo；  API声明：fontSize: number;  差异内容：fontSize: number; | component/styled\_string.d.ts |
| 新增API | NA | 类名：global；  API声明： declare abstract class CustomSpan  差异内容： declare abstract class CustomSpan | component/styled\_string.d.ts |
| 新增API | NA | 类名：CustomSpan；  API声明：abstract onMeasure(measureInfo: CustomSpanMeasureInfo): CustomSpanMetrics;  差异内容：abstract onMeasure(measureInfo: CustomSpanMeasureInfo): CustomSpanMetrics; | component/styled\_string.d.ts |
| 新增API | NA | 类名：CustomSpan；  API声明：abstract onDraw(context: DrawContext, drawInfo: CustomSpanDrawInfo): void;  差异内容：abstract onDraw(context: DrawContext, drawInfo: CustomSpanDrawInfo): void; | component/styled\_string.d.ts |
| 新增API | NA | 类名：global；  API声明： interface SymbolGlyphInterface  差异内容： interface SymbolGlyphInterface | component/symbolglyph.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum SymbolRenderingStrategy  差异内容： declare enum SymbolRenderingStrategy | component/symbolglyph.d.ts |
| 新增API | NA | 类名：SymbolRenderingStrategy；  API声明：SINGLE = 0  差异内容：SINGLE = 0 | component/symbolglyph.d.ts |
| 新增API | NA | 类名：SymbolRenderingStrategy；  API声明：MULTIPLE\_COLOR = 1  差异内容：MULTIPLE\_COLOR = 1 | component/symbolglyph.d.ts |
| 新增API | NA | 类名：SymbolRenderingStrategy；  API声明：MULTIPLE\_OPACITY = 2  差异内容：MULTIPLE\_OPACITY = 2 | component/symbolglyph.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum SymbolEffectStrategy  差异内容： declare enum SymbolEffectStrategy | component/symbolglyph.d.ts |
| 新增API | NA | 类名：SymbolEffectStrategy；  API声明：NONE = 0  差异内容：NONE = 0 | component/symbolglyph.d.ts |
| 新增API | NA | 类名：SymbolEffectStrategy；  API声明：SCALE = 1  差异内容：SCALE = 1 | component/symbolglyph.d.ts |
| 新增API | NA | 类名：SymbolEffectStrategy；  API声明：HIERARCHICAL = 2  差异内容：HIERARCHICAL = 2 | component/symbolglyph.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum EffectDirection  差异内容： declare enum EffectDirection | component/symbolglyph.d.ts |
| 新增API | NA | 类名：EffectDirection；  API声明：DOWN = 0  差异内容：DOWN = 0 | component/symbolglyph.d.ts |
| 新增API | NA | 类名：EffectDirection；  API声明：UP = 1  差异内容：UP = 1 | component/symbolglyph.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum EffectScope  差异内容： declare enum EffectScope | component/symbolglyph.d.ts |
| 新增API | NA | 类名：EffectScope；  API声明：LAYER = 0  差异内容：LAYER = 0 | component/symbolglyph.d.ts |
| 新增API | NA | 类名：EffectScope；  API声明：WHOLE = 1  差异内容：WHOLE = 1 | component/symbolglyph.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum EffectFillStyle  差异内容： declare enum EffectFillStyle | component/symbolglyph.d.ts |
| 新增API | NA | 类名：EffectFillStyle；  API声明：CUMULATIVE = 0  差异内容：CUMULATIVE = 0 | component/symbolglyph.d.ts |
| 新增API | NA | 类名：EffectFillStyle；  API声明：ITERATIVE = 1  差异内容：ITERATIVE = 1 | component/symbolglyph.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class SymbolEffect  差异内容： declare class SymbolEffect | component/symbolglyph.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class ScaleSymbolEffect  差异内容： declare class ScaleSymbolEffect | component/symbolglyph.d.ts |
| 新增API | NA | 类名：ScaleSymbolEffect；  API声明：scope?: EffectScope;  差异内容：scope?: EffectScope; | component/symbolglyph.d.ts |
| 新增API | NA | 类名：ScaleSymbolEffect；  API声明：direction?: EffectDirection;  差异内容：direction?: EffectDirection; | component/symbolglyph.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class HierarchicalSymbolEffect  差异内容： declare class HierarchicalSymbolEffect | component/symbolglyph.d.ts |
| 新增API | NA | 类名：HierarchicalSymbolEffect；  API声明：fillStyle?: EffectFillStyle;  差异内容：fillStyle?: EffectFillStyle; | component/symbolglyph.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class AppearSymbolEffect  差异内容： declare class AppearSymbolEffect | component/symbolglyph.d.ts |
| 新增API | NA | 类名：AppearSymbolEffect；  API声明：scope?: EffectScope;  差异内容：scope?: EffectScope; | component/symbolglyph.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class DisappearSymbolEffect  差异内容： declare class DisappearSymbolEffect | component/symbolglyph.d.ts |
| 新增API | NA | 类名：DisappearSymbolEffect；  API声明：scope?: EffectScope;  差异内容：scope?: EffectScope; | component/symbolglyph.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class BounceSymbolEffect  差异内容： declare class BounceSymbolEffect | component/symbolglyph.d.ts |
| 新增API | NA | 类名：BounceSymbolEffect；  API声明：scope?: EffectScope;  差异内容：scope?: EffectScope; | component/symbolglyph.d.ts |
| 新增API | NA | 类名：BounceSymbolEffect；  API声明：direction?: EffectDirection;  差异内容：direction?: EffectDirection; | component/symbolglyph.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class ReplaceSymbolEffect  差异内容： declare class ReplaceSymbolEffect | component/symbolglyph.d.ts |
| 新增API | NA | 类名：ReplaceSymbolEffect；  API声明：scope?: EffectScope;  差异内容：scope?: EffectScope; | component/symbolglyph.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class PulseSymbolEffect  差异内容： declare class PulseSymbolEffect | component/symbolglyph.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class SymbolGlyphAttribute  差异内容： declare class SymbolGlyphAttribute | component/symbolglyph.d.ts |
| 新增API | NA | 类名：SymbolGlyphAttribute；  API声明：fontSize(value: number | string | Resource): SymbolGlyphAttribute;  差异内容：fontSize(value: number | string | Resource): SymbolGlyphAttribute; | component/symbolglyph.d.ts |
| 新增API | NA | 类名：SymbolGlyphAttribute；  API声明：fontColor(value: Array<ResourceColor>): SymbolGlyphAttribute;  差异内容：fontColor(value: Array<ResourceColor>): SymbolGlyphAttribute; | component/symbolglyph.d.ts |
| 新增API | NA | 类名：SymbolGlyphAttribute；  API声明：fontWeight(value: number | FontWeight | string): SymbolGlyphAttribute;  差异内容：fontWeight(value: number | FontWeight | string): SymbolGlyphAttribute; | component/symbolglyph.d.ts |
| 新增API | NA | 类名：SymbolGlyphAttribute；  API声明：effectStrategy(value: SymbolEffectStrategy): SymbolGlyphAttribute;  差异内容：effectStrategy(value: SymbolEffectStrategy): SymbolGlyphAttribute; | component/symbolglyph.d.ts |
| 新增API | NA | 类名：SymbolGlyphAttribute；  API声明：renderingStrategy(value: SymbolRenderingStrategy): SymbolGlyphAttribute;  差异内容：renderingStrategy(value: SymbolRenderingStrategy): SymbolGlyphAttribute; | component/symbolglyph.d.ts |
| 新增API | NA | 类名：SymbolGlyphAttribute；  API声明：symbolEffect(symbolEffect: SymbolEffect, isActive?: boolean): SymbolGlyphAttribute;  差异内容：symbolEffect(symbolEffect: SymbolEffect, isActive?: boolean): SymbolGlyphAttribute; | component/symbolglyph.d.ts |
| 新增API | NA | 类名：SymbolGlyphAttribute；  API声明：symbolEffect(symbolEffect: SymbolEffect, triggerValue?: number): SymbolGlyphAttribute;  差异内容：symbolEffect(symbolEffect: SymbolEffect, triggerValue?: number): SymbolGlyphAttribute; | component/symbolglyph.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const SymbolGlyph: SymbolGlyphInterface;  差异内容：declare const SymbolGlyph: SymbolGlyphInterface; | component/symbolglyph.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const SymbolGlyphInstance: SymbolGlyphAttribute;  差异内容：declare const SymbolGlyphInstance: SymbolGlyphAttribute; | component/symbolglyph.d.ts |
| 新增API | NA | 类名：global；  API声明： interface SymbolSpanInterface  差异内容： interface SymbolSpanInterface | component/symbol\_span.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class SymbolSpanAttribute  差异内容： declare class SymbolSpanAttribute | component/symbol\_span.d.ts |
| 新增API | NA | 类名：SymbolSpanAttribute；  API声明：fontSize(value: number | string | Resource): SymbolSpanAttribute;  差异内容：fontSize(value: number | string | Resource): SymbolSpanAttribute; | component/symbol\_span.d.ts |
| 新增API | NA | 类名：SymbolSpanAttribute；  API声明：fontColor(value: Array<ResourceColor>): SymbolSpanAttribute;  差异内容：fontColor(value: Array<ResourceColor>): SymbolSpanAttribute; | component/symbol\_span.d.ts |
| 新增API | NA | 类名：SymbolSpanAttribute；  API声明：fontWeight(value: number | FontWeight | string): SymbolSpanAttribute;  差异内容：fontWeight(value: number | FontWeight | string): SymbolSpanAttribute; | component/symbol\_span.d.ts |
| 新增API | NA | 类名：SymbolSpanAttribute；  API声明：effectStrategy(value: SymbolEffectStrategy): SymbolSpanAttribute;  差异内容：effectStrategy(value: SymbolEffectStrategy): SymbolSpanAttribute; | component/symbol\_span.d.ts |
| 新增API | NA | 类名：SymbolSpanAttribute；  API声明：renderingStrategy(value: SymbolRenderingStrategy): SymbolSpanAttribute;  差异内容：renderingStrategy(value: SymbolRenderingStrategy): SymbolSpanAttribute; | component/symbol\_span.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const SymbolSpan: SymbolSpanInterface;  差异内容：declare const SymbolSpan: SymbolSpanInterface; | component/symbol\_span.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const SymbolSpanInstance: SymbolSpanAttribute;  差异内容：declare const SymbolSpanInstance: SymbolSpanAttribute; | component/symbol\_span.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum TextDataDetectorType  差异内容： declare enum TextDataDetectorType | component/text\_common.d.ts |
| 新增API | NA | 类名：TextDataDetectorType；  API声明：PHONE\_NUMBER = 0  差异内容：PHONE\_NUMBER = 0 | component/text\_common.d.ts |
| 新增API | NA | 类名：TextDataDetectorType；  API声明：URL = 1  差异内容：URL = 1 | component/text\_common.d.ts |
| 新增API | NA | 类名：TextDataDetectorType；  API声明：EMAIL = 2  差异内容：EMAIL = 2 | component/text\_common.d.ts |
| 新增API | NA | 类名：TextDataDetectorType；  API声明：ADDRESS = 3  差异内容：ADDRESS = 3 | component/text\_common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface TextDataDetectorConfig  差异内容： declare interface TextDataDetectorConfig | component/text\_common.d.ts |
| 新增API | NA | 类名：TextDataDetectorConfig；  API声明：types: TextDataDetectorType[];  差异内容：types: TextDataDetectorType[]; | component/text\_common.d.ts |
| 新增API | NA | 类名：TextDataDetectorConfig；  API声明：onDetectResultUpdate?: (result: string) => void;  差异内容：onDetectResultUpdate?: (result: string) => void; | component/text\_common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface TextRange  差异内容： declare interface TextRange | component/text\_common.d.ts |
| 新增API | NA | 类名：TextRange；  API声明：start?: number;  差异内容：start?: number; | component/text\_common.d.ts |
| 新增API | NA | 类名：TextRange；  API声明：end?: number;  差异内容：end?: number; | component/text\_common.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type OnDidChangeCallback = (rangeBefore: TextRange, rangeAfter: TextRange) => void;  差异内容：declare type OnDidChangeCallback = (rangeBefore: TextRange, rangeAfter: TextRange) => void; | component/text\_common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface TextBaseController  差异内容： declare interface TextBaseController | component/text\_common.d.ts |
| 新增API | NA | 类名：TextBaseController；  API声明：setSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void;  差异内容：setSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void; | component/text\_common.d.ts |
| 新增API | NA | 类名：TextBaseController；  API声明：closeSelectionMenu(): void;  差异内容：closeSelectionMenu(): void; | component/text\_common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface TextEditControllerEx  差异内容： declare interface TextEditControllerEx | component/text\_common.d.ts |
| 新增API | NA | 类名：TextEditControllerEx；  API声明：isEditing(): boolean;  差异内容：isEditing(): boolean; | component/text\_common.d.ts |
| 新增API | NA | 类名：TextEditControllerEx；  API声明：stopEditing(): void;  差异内容：stopEditing(): void; | component/text\_common.d.ts |
| 新增API | NA | 类名：TextEditControllerEx；  API声明：setCaretOffset(offset: number): boolean;  差异内容：setCaretOffset(offset: number): boolean; | component/text\_common.d.ts |
| 新增API | NA | 类名：TextEditControllerEx；  API声明：getCaretOffset(): number;  差异内容：getCaretOffset(): number; | component/text\_common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface StyledStringController  差异内容： declare interface StyledStringController | component/text\_common.d.ts |
| 新增API | NA | 类名：StyledStringController；  API声明：setStyledString(styledString: StyledString): void;  差异内容：setStyledString(styledString: StyledString): void; | component/text\_common.d.ts |
| 新增API | NA | 类名：StyledStringController；  API声明：getStyledString(): MutableStyledString;  差异内容：getStyledString(): MutableStyledString; | component/text\_common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface StyledStringChangedListener  差异内容： declare interface StyledStringChangedListener | component/text\_common.d.ts |
| 新增API | NA | 类名：StyledStringChangedListener；  API声明：onWillChange?: Callback<StyledStringChangeValue, boolean>;  差异内容：onWillChange?: Callback<StyledStringChangeValue, boolean>; | component/text\_common.d.ts |
| 新增API | NA | 类名：StyledStringChangedListener；  API声明：onDidChange?: OnDidChangeCallback;  差异内容：onDidChange?: OnDidChangeCallback; | component/text\_common.d.ts |
| 新增API | NA | 类名：global；  API声明： interface StyledStringChangeValue  差异内容： interface StyledStringChangeValue | component/text\_common.d.ts |
| 新增API | NA | 类名：StyledStringChangeValue；  API声明：range: TextRange;  差异内容：range: TextRange; | component/text\_common.d.ts |
| 新增API | NA | 类名：StyledStringChangeValue；  API声明：replacementString: StyledString;  差异内容：replacementString: StyledString; | component/text\_common.d.ts |
| 新增API | NA | 类名：StyledStringChangeValue；  API声明：previewText?: StyledString;  差异内容：previewText?: StyledString; | component/text\_common.d.ts |
| 新增API | NA | 类名：global；  API声明： interface CaretStyle  差异内容： interface CaretStyle | component/text\_common.d.ts |
| 新增API | NA | 类名：CaretStyle；  API声明：width?: Length;  差异内容：width?: Length; | component/text\_common.d.ts |
| 新增API | NA | 类名：CaretStyle；  API声明：color?: ResourceColor;  差异内容：color?: ResourceColor; | component/text\_common.d.ts |
| 新增API | NA | 类名：global；  API声明： interface FocusBoxStyle  差异内容： interface FocusBoxStyle | component/focus.d.ts |
| 新增API | NA | 类名：FocusBoxStyle；  API声明：margin?: LengthMetrics;  差异内容：margin?: LengthMetrics; | component/focus.d.ts |
| 新增API | NA | 类名：FocusBoxStyle；  API声明：strokeColor?: ColorMetrics;  差异内容：strokeColor?: ColorMetrics; | component/focus.d.ts |
| 新增API | NA | 类名：FocusBoxStyle；  API声明：strokeWidth?: LengthMetrics;  差异内容：strokeWidth?: LengthMetrics; | component/focus.d.ts |
| 新增API | NA | 类名：global；  API声明： interface RepeatItem  差异内容： interface RepeatItem | component/repeat.d.ts |
| 新增API | NA | 类名：RepeatItem；  API声明：item: T;  差异内容：item: T; | component/repeat.d.ts |
| 新增API | NA | 类名：RepeatItem；  API声明：index?: number;  差异内容：index?: number; | component/repeat.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class RepeatAttribute  差异内容： declare class RepeatAttribute | component/repeat.d.ts |
| 新增API | NA | 类名：RepeatAttribute；  API声明：each(itemGenerator: (repeatItem: RepeatItem<T>) => void): RepeatAttribute<T>;  差异内容：each(itemGenerator: (repeatItem: RepeatItem<T>) => void): RepeatAttribute<T>; | component/repeat.d.ts |
| 新增API | NA | 类名：RepeatAttribute；  API声明：key(keyGenerator: (item: T, index: number) => string): RepeatAttribute<T>;  差异内容：key(keyGenerator: (item: T, index: number) => string): RepeatAttribute<T>; | component/repeat.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const Repeat: <T>(arr: Array<T>) => RepeatAttribute<T>;  差异内容：declare const Repeat: <T>(arr: Array<T>) => RepeatAttribute<T>; | component/repeat.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type CustomTheme = import('../api/@ohos.arkui.theme').CustomTheme;  差异内容：declare type CustomTheme = import('../api/@ohos.arkui.theme').CustomTheme; | component/with\_theme.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface WithThemeOptions  差异内容： declare interface WithThemeOptions | component/with\_theme.d.ts |
| 新增API | NA | 类名：WithThemeOptions；  API声明：theme?: CustomTheme;  差异内容：theme?: CustomTheme; | component/with\_theme.d.ts |
| 新增API | NA | 类名：WithThemeOptions；  API声明：colorMode?: ThemeColorMode;  差异内容：colorMode?: ThemeColorMode; | component/with\_theme.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type WithThemeInterface = (options: WithThemeOptions) => WithThemeAttribute;  差异内容：declare type WithThemeInterface = (options: WithThemeOptions) => WithThemeAttribute; | component/with\_theme.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class WithThemeAttribute  差异内容： declare class WithThemeAttribute | component/with\_theme.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const WithTheme: WithThemeInterface;  差异内容：declare const WithTheme: WithThemeInterface; | component/with\_theme.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const WithThemeInstance: WithThemeAttribute;  差异内容：declare const WithThemeInstance: WithThemeAttribute; | component/with\_theme.d.ts |
| 删除API | 类名：SourceTool；  API声明：FINGER  差异内容：FINGER | NA | component/common.d.ts |
| 删除API | 类名：SourceTool；  API声明：PEN  差异内容：PEN | NA | component/common.d.ts |
| 删除API | 类名：global；  API声明： declare interface PixelMapMock  差异内容： declare interface PixelMapMock | NA | component/common.d.ts |
| 删除API | 类名：PixelMapMock；  API声明：release(): void;  差异内容：release(): void; | NA | component/common.d.ts |
| 删除API | 类名：CommonMethod；  API声明：borderStyle(value: BorderStyle): T;  差异内容：borderStyle(value: BorderStyle): T; | NA | component/common.d.ts |
| 删除API | 类名：CommonMethod；  API声明：borderStyle(value: EdgeStyles): T;  差异内容：borderStyle(value: EdgeStyles): T; | NA | component/common.d.ts |
| 删除API | 类名：CommonMethod；  API声明：borderWidth(value: Length): T;  差异内容：borderWidth(value: Length): T; | NA | component/common.d.ts |
| 删除API | 类名：CommonMethod；  API声明：borderWidth(value: EdgeWidths): T;  差异内容：borderWidth(value: EdgeWidths): T; | NA | component/common.d.ts |
| 删除API | 类名：CommonMethod；  API声明：borderColor(value: ResourceColor): T;  差异内容：borderColor(value: ResourceColor): T; | NA | component/common.d.ts |
| 删除API | 类名：CommonMethod；  API声明：borderColor(value: EdgeColors): T;  差异内容：borderColor(value: EdgeColors): T; | NA | component/common.d.ts |
| 删除API | 类名：CommonMethod；  API声明：borderRadius(value: Length): T;  差异内容：borderRadius(value: Length): T; | NA | component/common.d.ts |
| 删除API | 类名：CommonMethod；  API声明：borderRadius(value: BorderRadiuses): T;  差异内容：borderRadius(value: BorderRadiuses): T; | NA | component/common.d.ts |
| 删除API | 类名：CommonMethod；  API声明：mask(value: CircleAttribute | EllipseAttribute | PathAttribute | RectAttribute): T;  差异内容：mask(value: CircleAttribute | EllipseAttribute | PathAttribute | RectAttribute): T; | NA | component/common.d.ts |
| 删除API | 类名：CommonMethod；  API声明：bindMenu(content: { value: string; action: () => void }[] | CustomBuilder): T;  差异内容：bindMenu(content: { value: string; action: () => void }[] | CustomBuilder): T; | NA | component/common.d.ts |
| 删除API | 类名：CommonMethod；  API声明：bindContextMenu(content: CustomBuilder, responseType: ResponseType): T;  差异内容：bindContextMenu(content: CustomBuilder, responseType: ResponseType): T; | NA | component/common.d.ts |
| 删除API | 类名：global；  API声明： declare class View  差异内容： declare class View | NA | component/common.d.ts |
| 删除API | 类名：View；  API声明：create(value: any): any;  差异内容：create(value: any): any; | NA | component/common.d.ts |
| 删除API | 类名：ImageAttribute；  API声明：onError(callback: (event?: {  componentWidth: number;  componentHeight: number;  }) => void): ImageAttribute;  差异内容：onError(callback: (event?: {  componentWidth: number;  componentHeight: number;  }) => void): ImageAttribute; | NA | component/image.d.ts |
| 删除API | 类名：ImageAttribute；  API声明：onError(callback: (event?: {  componentWidth: number;  componentHeight: number;  message: string;  }) => void): ImageAttribute;  差异内容：onError(callback: (event?: {  componentWidth: number;  componentHeight: number;  message: string;  }) => void): ImageAttribute; | NA | component/image.d.ts |
| 删除API | 类名：TabsAttribute；  API声明：barMode(value: BarMode): TabsAttribute;  差异内容：barMode(value: BarMode): TabsAttribute; | NA | component/tabs.d.ts |
| 删除API | 类名：Resource；  API声明：readonly id: number;  差异内容：readonly id: number; | NA | component/units.d.ts |
| 删除API | 类名：Resource；  API声明：readonly type: number;  差异内容：readonly type: number; | NA | component/units.d.ts |
| 删除API | 类名：Resource；  API声明：readonly params?: any[];  差异内容：readonly params?: any[]; | NA | component/units.d.ts |
| 删除API | 类名：Resource；  API声明：readonly bundleName: string;  差异内容：readonly bundleName: string; | NA | component/units.d.ts |
| 删除API | 类名：Resource；  API声明：readonly moduleName: string;  差异内容：readonly moduleName: string; | NA | component/units.d.ts |
| 起始版本有变化 | 类名：CommonMethod；  API声明：key(value: string): T;  差异内容：8 | 类名：CommonMethod；  API声明：key(value: string): T;  差异内容：12 | component/common.d.ts |
| 起始版本有变化 | 类名：global；  API声明：declare type CustomBuilder = (() => any) | void;  差异内容：7 | 类名：global；  API声明：declare type CustomBuilder = (() => any) | void;  差异内容：8 | component/common.d.ts |
| 起始版本有变化 | 类名：Scroller；  API声明：scrollPage(value: {  next: boolean;  direction?: Axis;  });  差异内容：7 | 类名：Scroller；  API声明：scrollPage(value: {  next: boolean;  });  差异内容：9 | component/scroll.d.ts |
| 起始版本有变化 | 类名：Scroller；  API声明：scrollPage(value: {  next: boolean;  });  差异内容：9 | 类名：Scroller；  API声明：scrollPage(value: {  next: boolean;  direction?: Axis;  });  差异内容：7 | component/scroll.d.ts |
| 起始版本有变化 | 类名：TabsAttribute；  API声明：barWidth(value: Length): TabsAttribute;  差异内容：8 | 类名：TabsAttribute；  API声明：barWidth(value: Length): TabsAttribute;  差异内容：7 | component/tabs.d.ts |
| 起始版本有变化 | 类名：TabsAttribute；  API声明：barHeight(value: Length): TabsAttribute;  差异内容：8 | 类名：TabsAttribute；  API声明：barHeight(value: Length): TabsAttribute;  差异内容：7 | component/tabs.d.ts |
| 起始版本有变化 | 类名：TextAreaAttribute；  API声明：onCopy(callback: (value: string) => void): TextAreaAttribute;  差异内容：7 | 类名：TextAreaAttribute；  API声明：onCopy(callback: (value: string) => void): TextAreaAttribute;  差异内容：8 | component/text\_area.d.ts |
| 起始版本有变化 | 类名：TextAreaAttribute；  API声明：onCut(callback: (value: string) => void): TextAreaAttribute;  差异内容：7 | 类名：TextAreaAttribute；  API声明：onCut(callback: (value: string) => void): TextAreaAttribute;  差异内容：8 | component/text\_area.d.ts |
